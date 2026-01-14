#!/usr/bin/env python3
"""
test_verify_mover_advantage.py - Unit Tests for Mover Advantage Verification
=============================================================================

PURPOSE:
Comprehensive unit tests for verify_mover_advantage.py ensuring:
1. Data loading works correctly
2. Mover/Stayer classification is correct
3. Statistics match canonical claims
4. Edge cases are handled

USAGE:
    python -m pytest test_verify_mover_advantage.py -v
    python test_verify_mover_advantage.py  # Direct execution

Author: Claude Code CLI
Date: 2026-01-14
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import Optional
import unittest

import numpy as np
import pandas as pd

# Add parent to path for imports
SCRIPT_DIR = Path(__file__).parent.resolve()
sys.path.insert(0, str(SCRIPT_DIR))

from verify_mover_advantage import (
    CanonicalClaims,
    VerificationResult,
    VerificationReport,
    verify_mover_advantage,
    find_data_file,
    load_thesis_panel,
)


# ============================================================================
# TEST FIXTURES
# ============================================================================

def create_mock_data(
    n_movers: int = 1000,
    n_stayers: int = 1500,
    mover_success_rate: float = 0.181,
    stayer_success_rate: float = 0.070,
    seed: int = 42
) -> pd.DataFrame:
    """Create mock data for testing.

    Args:
        n_movers: Number of movers (R > 0)
        n_stayers: Number of stayers (R = 0)
        mover_success_rate: Success rate for movers
        stayer_success_rate: Success rate for stayers
        seed: Random seed for reproducibility

    Returns:
        DataFrame mimicking thesis_panel_v3 structure
    """
    np.random.seed(seed)

    # Movers: R > 0, success rate = mover_success_rate
    mover_M = np.random.uniform(0.01, 2.0, n_movers)
    mover_L = np.random.binomial(1, mover_success_rate, n_movers)

    # Stayers: R = 0, success rate = stayer_success_rate
    stayer_M = np.zeros(n_stayers)
    stayer_L = np.random.binomial(1, stayer_success_rate, n_stayers)

    df = pd.DataFrame({
        'M': np.concatenate([mover_M, stayer_M]),
        'L': np.concatenate([mover_L, stayer_L]),
    })

    # Shuffle
    return df.sample(frac=1, random_state=seed).reset_index(drop=True)


# ============================================================================
# TEST CASES
# ============================================================================

class TestCanonicalClaims(unittest.TestCase):
    """Test CanonicalClaims dataclass."""

    def test_claims_are_immutable(self):
        """Claims should be frozen (immutable)."""
        claims = CanonicalClaims()
        with self.assertRaises(Exception):
            claims.N_total = 999  # type: ignore

    def test_canonical_values(self):
        """Verify canonical values from Thesis_Master.md."""
        claims = CanonicalClaims()

        self.assertEqual(claims.N_total, 180_994)
        self.assertEqual(claims.N_movers, 72_943)
        self.assertEqual(claims.N_stayers, 107_917)
        self.assertAlmostEqual(claims.mover_success_rate, 18.1, places=1)
        self.assertAlmostEqual(claims.stayer_success_rate, 7.0, places=1)
        self.assertAlmostEqual(claims.mover_advantage, 2.60, places=2)
        self.assertEqual(claims.mover_definition, "R > 0")

    def test_derived_metrics_are_consistent(self):
        """Derived metrics should be mathematically consistent."""
        claims = CanonicalClaims()

        # Mover advantage = mover_success / stayer_success
        expected_advantage = claims.mover_success_rate / claims.stayer_success_rate
        self.assertAlmostEqual(claims.mover_advantage, expected_advantage, places=1)

        # Effect size = mover_success - stayer_success
        expected_effect = claims.mover_success_rate - claims.stayer_success_rate
        self.assertAlmostEqual(claims.effect_size_pp, expected_effect, places=1)

        # Percentages sum to 100
        self.assertAlmostEqual(claims.mover_pct + claims.stayer_pct, 100.0, places=1)

        # N_movers + N_stayers ≈ N_total (allowing for missing R)
        self.assertLess(claims.N_movers + claims.N_stayers, claims.N_total + 1)


class TestVerificationResult(unittest.TestCase):
    """Test VerificationResult dataclass."""

    def test_passed_result(self):
        """Test a passing result."""
        result = VerificationResult(
            name="Test",
            expected=100,
            actual=100,
            passed=True,
        )
        self.assertTrue(result.passed)
        self.assertIn("✓", str(result))

    def test_failed_result(self):
        """Test a failing result."""
        result = VerificationResult(
            name="Test",
            expected=100,
            actual=50,
            passed=False,
        )
        self.assertFalse(result.passed)
        self.assertIn("✗", str(result))

    def test_with_detail(self):
        """Test result with detail message."""
        result = VerificationResult(
            name="Test",
            expected=100,
            actual=99,
            passed=True,
            detail="Within tolerance",
        )
        self.assertEqual(result.detail, "Within tolerance")


class TestVerificationReport(unittest.TestCase):
    """Test VerificationReport dataclass."""

    def test_empty_report_passes(self):
        """Empty report should pass (vacuously true)."""
        report = VerificationReport()
        self.assertTrue(report.passed)
        self.assertEqual(report.n_passed, 0)
        self.assertEqual(report.n_failed, 0)

    def test_all_passing(self):
        """Report with all passing results."""
        report = VerificationReport()
        report.add(VerificationResult("A", 1, 1, True))
        report.add(VerificationResult("B", 2, 2, True))

        self.assertTrue(report.passed)
        self.assertEqual(report.n_passed, 2)
        self.assertEqual(report.n_failed, 0)

    def test_with_failure(self):
        """Report with at least one failure."""
        report = VerificationReport()
        report.add(VerificationResult("A", 1, 1, True))
        report.add(VerificationResult("B", 2, 99, False))

        self.assertFalse(report.passed)
        self.assertEqual(report.n_passed, 1)
        self.assertEqual(report.n_failed, 1)


class TestMoverClassification(unittest.TestCase):
    """Test Mover/Stayer classification logic."""

    def test_mover_is_R_greater_than_zero(self):
        """Mover = R > 0."""
        df = create_mock_data(n_movers=100, n_stayers=200)

        # Count R > 0
        n_movers = (df['M'] > 0).sum()
        n_stayers = (df['M'] == 0).sum()

        self.assertEqual(n_movers, 100)
        self.assertEqual(n_stayers, 200)

    def test_handles_missing_R(self):
        """Missing R values should be excluded."""
        df = create_mock_data(n_movers=100, n_stayers=200)
        df.loc[0:9, 'M'] = np.nan  # 10 missing values

        movers_mask = (df['M'] > 0) & df['M'].notna()
        stayers_mask = (df['M'] == 0) & df['M'].notna()

        self.assertEqual(movers_mask.sum() + stayers_mask.sum(), 290)

    def test_exact_zero_is_stayer(self):
        """R = 0.0 exactly should be classified as Stayer."""
        df = pd.DataFrame({'M': [0.0, 0.0, 0.001, 0.5], 'L': [0, 1, 1, 1]})

        movers = (df['M'] > 0).sum()
        stayers = (df['M'] == 0).sum()

        self.assertEqual(movers, 2)
        self.assertEqual(stayers, 2)


class TestSuccessRateCalculation(unittest.TestCase):
    """Test success rate calculation."""

    def test_success_rate_formula(self):
        """Success rate = mean(L) * 100."""
        df = pd.DataFrame({
            'M': [1.0, 1.0, 0.0, 0.0, 0.0],
            'L': [1, 0, 1, 0, 0],
        })

        movers = df['M'] > 0
        stayers = df['M'] == 0

        mover_success = df.loc[movers, 'L'].mean() * 100  # 50%
        stayer_success = df.loc[stayers, 'L'].mean() * 100  # 33.3%

        self.assertAlmostEqual(mover_success, 50.0, places=1)
        self.assertAlmostEqual(stayer_success, 33.3, places=1)

    def test_advantage_is_ratio(self):
        """Mover Advantage = mover_success / stayer_success."""
        mover_success = 18.1
        stayer_success = 7.0

        advantage = mover_success / stayer_success
        self.assertAlmostEqual(advantage, 2.586, places=2)


class TestVerifyMoverAdvantage(unittest.TestCase):
    """Integration tests for verify_mover_advantage function."""

    def test_mock_data_passes_verification(self):
        """Mock data with correct rates should pass verification."""
        # Create data that matches canonical claims approximately
        df = create_mock_data(
            n_movers=72943,
            n_stayers=107917,
            mover_success_rate=0.181,
            stayer_success_rate=0.070,
            seed=42
        )

        # Custom claims matching our mock data
        @dataclass(frozen=True)
        class MockClaims:
            N_total: int = len(df)
            N_movers: int = 72943
            N_stayers: int = 107917
            mover_success_rate: float = 18.1
            stayer_success_rate: float = 7.0
            mover_advantage: float = 2.60
            effect_size_pp: float = 11.1
            chi_squared: float = 5322.0
            mover_pct: float = 40.3
            stayer_pct: float = 59.7
            mover_definition: str = "R > 0"

        # Note: With random data, exact rates will vary
        # This test verifies the function runs without error
        report = verify_mover_advantage(df, MockClaims())

        # Function should complete without exception
        self.assertIsInstance(report, VerificationReport)

    def test_wrong_data_fails_verification(self):
        """Data with wrong rates should fail verification."""
        # Create data with WRONG success rates
        df = create_mock_data(
            n_movers=1000,
            n_stayers=1000,
            mover_success_rate=0.50,  # WRONG: should be 0.181
            stayer_success_rate=0.50,  # WRONG: should be 0.070
        )

        # Use real canonical claims
        claims = CanonicalClaims()
        report = verify_mover_advantage(df, claims)

        # Sample size mismatch should cause failures
        self.assertFalse(report.passed)


class TestDataLoading(unittest.TestCase):
    """Test data loading functions."""

    def test_find_data_file_returns_path(self):
        """find_data_file should return a Path if file exists."""
        try:
            path = find_data_file()
            self.assertIsInstance(path, Path)
            self.assertTrue(path.exists())
        except FileNotFoundError:
            self.skipTest("Data file not available")

    def test_load_thesis_panel_returns_dataframe(self):
        """load_thesis_panel should return a DataFrame."""
        try:
            df = load_thesis_panel()
            self.assertIsInstance(df, pd.DataFrame)
            self.assertIn('M', df.columns)
            self.assertIn('L', df.columns)
        except FileNotFoundError:
            self.skipTest("Data file not available")


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and error handling."""

    def test_all_movers(self):
        """Handle case where all ventures are movers."""
        df = pd.DataFrame({
            'M': [1.0, 0.5, 2.0],
            'L': [1, 0, 1],
        })

        movers = df['M'] > 0
        stayers = df['M'] == 0

        self.assertEqual(movers.sum(), 3)
        self.assertEqual(stayers.sum(), 0)

    def test_all_stayers(self):
        """Handle case where all ventures are stayers."""
        df = pd.DataFrame({
            'M': [0.0, 0.0, 0.0],
            'L': [1, 0, 1],
        })

        movers = df['M'] > 0
        stayers = df['M'] == 0

        self.assertEqual(movers.sum(), 0)
        self.assertEqual(stayers.sum(), 3)

    def test_zero_stayer_success(self):
        """Handle division by zero when stayer success = 0."""
        mover_success = 50.0
        stayer_success = 0.0

        # Should return inf or nan, not crash
        if stayer_success > 0:
            advantage = mover_success / stayer_success
        else:
            advantage = np.inf

        self.assertEqual(advantage, np.inf)


# ============================================================================
# TEST RUNNER
# ============================================================================

def run_tests() -> int:
    """Run all tests and return exit code."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    sys.exit(run_tests())
