#!/usr/bin/env python3
"""
verify_mover_advantage.py - Rigorous Verification of Mover Advantage Claims
============================================================================

PURPOSE:
Verify the 2.60× Mover Advantage (18.1% vs 7.0%) from Thesis_Master.md.
This is the MOST CRITICAL figure in the thesis and must be reproduced exactly.

CANONICAL CLAIMS (from Thesis_Master.md §4.3.2):
- Mover Success Rate:  18.1%
- Stayer Success Rate:  7.0%
- Mover Advantage:      2.60× = 18.1 / 7.0
- Chi-Square:           χ² = 5,322 (p < 0.001)
- Effect Size:          +11.1 pp (18.1% - 7.0%)

DEFINITION:
- Mover:  R > 0 (any repositioning)
- Stayer: R = 0 (no repositioning)
- R = |V_T - V_0| = |B_T - B_0| (magnitude of strategic breadth change)

DATA SOURCE:
- thesis_panel_v3.nc (N = 180,994)
- Column mapping: M = R (magnitude), L = G (success/growth binary)

RELATIONSHIP TO OTHER METRICS:
1. Success Rate (L): Binary - reached Later Stage VC (0/1)
   → Used for Mover Advantage = 2.60×
2. Funding Growth (G): Continuous - (F_t - E) / E
   → Used in §4.6 case studies (Hope Care 2.71×, Leap Green 0.80×)
   → Ratio ≈ 3.4× is case-specific, NOT population statistic

Author: Claude Code CLI
Date: 2026-01-14
Version: 1.0.0
"""

from __future__ import annotations

import json
import logging
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Tuple, Dict, Any

import numpy as np
import pandas as pd
import xarray as xr
from scipy.stats import (
    spearmanr, mannwhitneyu, chi2_contingency,
    bootstrap, median_abs_deviation
)

# ============================================================================
# CONFIGURATION
# ============================================================================

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%H:%M:%S'
)
log = logging.getLogger(__name__)

SCRIPT_DIR = Path(__file__).parent.resolve()
DATA_DIR = SCRIPT_DIR / 'data'
REPO_ROOT = Path("/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics")

# Tolerance levels for verification
TOLERANCE = {
    'percentage': 0.5,   # ±0.5 percentage points
    'ratio': 0.05,       # ±5% for ratios
    'chi2': 500,         # ±500 for chi-square (thesis claims 5,322)
}

# ============================================================================
# CANONICAL CLAIMS (from Thesis_Master.md)
# ============================================================================

@dataclass(frozen=True)
class CanonicalClaims:
    """Immutable canonical claims from Thesis_Master.md.

    These are the GROUND TRUTH values that must be verified.
    Source: §4.3.2 "The Mover Advantage: 2.60×"
    """
    # Sample sizes
    N_total: int = 180_994
    N_movers: int = 72_943
    N_stayers: int = 107_917

    # Success rates (percentages)
    mover_success_rate: float = 18.1
    stayer_success_rate: float = 7.0

    # Derived metrics
    mover_advantage: float = 2.60
    effect_size_pp: float = 11.1  # percentage points
    chi_squared: float = 5_322.0

    # Percentages
    mover_pct: float = 40.3
    stayer_pct: float = 59.7

    # Definition
    mover_definition: str = "R > 0"


# ============================================================================
# DATA LOADING
# ============================================================================

def find_data_file() -> Path:
    """Find thesis_panel_v3.nc in possible locations."""
    candidates = [
        DATA_DIR / 'thesis_panel_v3.nc',
        DATA_DIR / 'processed' / 'thesis_panel_v3.nc',
        REPO_ROOT / 'data' / 'processed' / 'thesis_panel_v3.nc',
    ]

    for path in candidates:
        if path.exists():
            return path

    raise FileNotFoundError(
        f"thesis_panel_v3.nc not found. Searched:\n" +
        "\n".join(f"  - {p}" for p in candidates)
    )


def load_thesis_panel() -> pd.DataFrame:
    """Load and validate thesis panel data.

    Returns:
        DataFrame with columns: company, M, L, E, G, V_0, V_T, D, moved
    """
    path = find_data_file()
    log.info(f"Loading: {path}")

    ds = xr.open_dataset(path)
    df = ds.to_dataframe().reset_index()
    ds.close()

    # Validate required columns
    required = ['M', 'L']
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    log.info(f"Loaded {len(df):,} rows, columns: {list(df.columns)}")
    return df


# ============================================================================
# CORE VERIFICATION
# ============================================================================

@dataclass
class VerificationResult:
    """Result of a single verification check."""
    name: str
    expected: Any
    actual: Any
    passed: bool
    tolerance: float = 0.0
    detail: str = ""

    def __str__(self) -> str:
        status = "✓" if self.passed else "✗"
        return f"{status} {self.name}: expected={self.expected}, actual={self.actual}"


@dataclass
class VerificationReport:
    """Complete verification report."""
    results: list = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return all(r.passed for r in self.results)

    @property
    def n_passed(self) -> int:
        return sum(1 for r in self.results if r.passed)

    @property
    def n_failed(self) -> int:
        return len(self.results) - self.n_passed

    def add(self, result: VerificationResult) -> None:
        self.results.append(result)
        status = "PASS" if result.passed else "FAIL"
        log.info(f"  [{status}] {result.name}")
        log.info(f"         Expected: {result.expected}")
        log.info(f"         Actual:   {result.actual}")
        if result.detail:
            log.info(f"         Note: {result.detail}")


def verify_mover_advantage(
    df: pd.DataFrame,
    claims: CanonicalClaims = CanonicalClaims()
) -> VerificationReport:
    """Verify all Mover Advantage claims against data.

    Args:
        df: DataFrame with M (repositioning) and L (success) columns
        claims: Canonical claims to verify against

    Returns:
        VerificationReport with all test results
    """
    report = VerificationReport()

    log.info("\n" + "="*70)
    log.info("MOVER ADVANTAGE VERIFICATION")
    log.info("="*70)

    # -------------------------------------------------------------------------
    # 1. Sample Size
    # -------------------------------------------------------------------------
    log.info("\n[1] Sample Size")
    report.add(VerificationResult(
        name="Total N",
        expected=claims.N_total,
        actual=len(df),
        passed=len(df) == claims.N_total,
    ))

    # -------------------------------------------------------------------------
    # 2. Mover/Stayer Classification
    # -------------------------------------------------------------------------
    log.info("\n[2] Mover/Stayer Classification (R > 0)")

    R = df['M']  # M = magnitude of repositioning
    movers_mask = (R > 0) & R.notna()
    stayers_mask = (R == 0) & R.notna()

    N_movers = movers_mask.sum()
    N_stayers = stayers_mask.sum()
    N_valid = N_movers + N_stayers

    report.add(VerificationResult(
        name="N Movers",
        expected=claims.N_movers,
        actual=N_movers,
        passed=abs(N_movers - claims.N_movers) < 100,
        detail=f"Diff: {abs(N_movers - claims.N_movers)}"
    ))

    report.add(VerificationResult(
        name="N Stayers",
        expected=claims.N_stayers,
        actual=N_stayers,
        passed=abs(N_stayers - claims.N_stayers) < 100,
        detail=f"Diff: {abs(N_stayers - claims.N_stayers)}"
    ))

    mover_pct = N_movers / N_valid * 100
    stayer_pct = N_stayers / N_valid * 100

    report.add(VerificationResult(
        name="Mover %",
        expected=f"{claims.mover_pct}%",
        actual=f"{mover_pct:.1f}%",
        passed=abs(mover_pct - claims.mover_pct) < TOLERANCE['percentage'],
    ))

    report.add(VerificationResult(
        name="Stayer %",
        expected=f"{claims.stayer_pct}%",
        actual=f"{stayer_pct:.1f}%",
        passed=abs(stayer_pct - claims.stayer_pct) < TOLERANCE['percentage'],
    ))

    # -------------------------------------------------------------------------
    # 3. Success Rates
    # -------------------------------------------------------------------------
    log.info("\n[3] Success Rates")

    L = df['L']  # L = later stage success (binary)

    mover_success = L[movers_mask].mean() * 100
    stayer_success = L[stayers_mask].mean() * 100

    report.add(VerificationResult(
        name="Mover Success Rate",
        expected=f"{claims.mover_success_rate}%",
        actual=f"{mover_success:.1f}%",
        passed=abs(mover_success - claims.mover_success_rate) < TOLERANCE['percentage'],
    ))

    report.add(VerificationResult(
        name="Stayer Success Rate",
        expected=f"{claims.stayer_success_rate}%",
        actual=f"{stayer_success:.1f}%",
        passed=abs(stayer_success - claims.stayer_success_rate) < TOLERANCE['percentage'],
    ))

    # -------------------------------------------------------------------------
    # 4. Mover Advantage
    # -------------------------------------------------------------------------
    log.info("\n[4] Mover Advantage")

    advantage = mover_success / stayer_success if stayer_success > 0 else np.nan

    report.add(VerificationResult(
        name="Mover Advantage",
        expected=f"{claims.mover_advantage}×",
        actual=f"{advantage:.2f}×",
        passed=abs(advantage - claims.mover_advantage) < TOLERANCE['ratio'],
        detail=f"= {mover_success:.1f}% / {stayer_success:.1f}%"
    ))

    effect_size = mover_success - stayer_success
    report.add(VerificationResult(
        name="Effect Size (pp)",
        expected=f"+{claims.effect_size_pp} pp",
        actual=f"+{effect_size:.1f} pp",
        passed=abs(effect_size - claims.effect_size_pp) < TOLERANCE['percentage'],
    ))

    # -------------------------------------------------------------------------
    # 5. Chi-Square Test
    # -------------------------------------------------------------------------
    log.info("\n[5] Statistical Significance")

    valid_mask = movers_mask | stayers_mask
    contingency = pd.crosstab(
        movers_mask[valid_mask].astype(int),
        L[valid_mask]
    )

    if contingency.shape == (2, 2):
        chi2, p_value, dof, _ = chi2_contingency(contingency)

        report.add(VerificationResult(
            name="Chi-Square",
            expected=f"χ² ≈ {claims.chi_squared:,.0f}",
            actual=f"χ² = {chi2:,.1f}",
            passed=abs(chi2 - claims.chi_squared) < TOLERANCE['chi2'],
            detail=f"p = {p_value:.2e}"
        ))

    # -------------------------------------------------------------------------
    # Summary
    # -------------------------------------------------------------------------
    log.info("\n" + "="*70)
    log.info("VERIFICATION SUMMARY")
    log.info("="*70)
    log.info(f"Total Tests: {len(report.results)}")
    log.info(f"Passed: {report.n_passed}")
    log.info(f"Failed: {report.n_failed}")

    if report.passed:
        log.info("\n✓ ALL TESTS PASSED - Thesis claims verified")
    else:
        log.error("\n✗ SOME TESTS FAILED")
        for r in report.results:
            if not r.passed:
                log.error(f"  - {r}")

    return report


# ============================================================================
# JSON OUTPUT
# ============================================================================

def export_verification_json(report: VerificationReport, path: Path) -> None:
    """Export verification results to JSON."""
    data = {
        'verified': bool(report.passed),
        'n_tests': len(report.results),
        'n_passed': report.n_passed,
        'n_failed': report.n_failed,
        'results': [
            {
                'name': r.name,
                'expected': str(r.expected),
                'actual': str(r.actual),
                'passed': bool(r.passed),
                'detail': r.detail,
            }
            for r in report.results
        ]
    }

    path.write_text(json.dumps(data, indent=2))
    log.info(f"Saved verification results: {path}")


# ============================================================================
# MAIN
# ============================================================================

def main() -> int:
    """Run Mover Advantage verification.

    Returns:
        0 if all tests pass, 1 otherwise
    """
    log.info("="*70)
    log.info("MOVER ADVANTAGE VERIFICATION")
    log.info("Verifying 2.60× (18.1% vs 7.0%) from Thesis_Master.md")
    log.info("="*70)

    try:
        # Load data
        df = load_thesis_panel()

        # Run verification
        claims = CanonicalClaims()
        report = verify_mover_advantage(df, claims)

        # Export results
        output_path = DATA_DIR / 'mover_advantage_verification.json'
        export_verification_json(report, output_path)

        return 0 if report.passed else 1

    except Exception as e:
        log.exception(f"Verification failed: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
