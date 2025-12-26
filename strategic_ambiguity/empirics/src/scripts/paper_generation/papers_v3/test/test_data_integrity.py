#!/usr/bin/env python3
"""
Comprehensive Data Integrity Tests for Thesis Pipeline

SBC-inspired validation: If the pipeline is correct, derived statistics
should match source truth within tolerance.

Usage:
    python test_data_integrity.py [--verbose] [--json-output]
"""

import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, field
from typing import List, Tuple, Optional
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import xarray as xr
from scipy.stats import spearmanr, ks_2samp

# Paths
SCRIPT_DIR = Path(__file__).parent.resolve()
REPO_ROOT = SCRIPT_DIR.parent.parent.parent.parent.parent
DATA_RAW = REPO_ROOT / 'data' / 'raw'
DATA_PROC = REPO_ROOT / 'data' / 'processed'


@dataclass
class TestResult:
    """Single test result."""
    test_id: str
    name: str
    passed: bool
    severity: str  # CRITICAL, ERROR, WARNING, INFO
    message: str
    expected: Optional[str] = None
    actual: Optional[str] = None
    details: dict = field(default_factory=dict)


class DataValidator:
    """Comprehensive data validation suite."""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.results: List[TestResult] = []
        self.data_loaded = False

    def log(self, msg: str):
        if self.verbose:
            print(f"  {msg}")

    def load_data(self):
        """Load all data sources."""
        self.log("Loading vagueness_timeseries.parquet...")
        self.vag = pd.read_parquet(DATA_PROC / 'vagueness_timeseries.parquet')

        self.log("Loading features_all.parquet...")
        self.feat = pd.read_parquet(DATA_PROC / 'features_all.parquet')

        self.log("Loading thesis_panel_v3.nc...")
        self.panel_ds = xr.open_dataset(DATA_PROC / 'thesis_panel_v3.nc')
        self.panel = self._ds_to_df(self.panel_ds)

        self.data_loaded = True
        self.log(f"Loaded: vag={len(self.vag):,}, feat={len(self.feat):,}, panel={len(self.panel):,}")

    def _ds_to_df(self, ds: xr.Dataset) -> pd.DataFrame:
        """Convert xarray Dataset to DataFrame."""
        return pd.DataFrame({
            'company_id': ds['company'].values,
            'V_0': ds['V_0'].values,
            'V_T': ds['V_T'].values,
            'D': ds['D'].values,
            'M': ds['M'].values,
            'E': ds['E'].values,
            'G': ds['G'].values,
            'L': ds['L'].values,
            'mover_type': ds['mover_type'].values,
        })

    def add_result(self, test_id: str, name: str, passed: bool, severity: str,
                   message: str, expected: str = None, actual: str = None, **details):
        self.results.append(TestResult(
            test_id=test_id, name=name, passed=passed, severity=severity,
            message=message, expected=expected, actual=actual, details=details
        ))

    # =========================================================================
    # Category 1: Identity Tests
    # =========================================================================

    def test_T1_1_company_count(self):
        """T1.1: Company count consistency."""
        # Companies with E in 2021 should match panel count
        v_2021 = self.vag[self.vag['year'] == 2021]
        v_2021_with_E = v_2021[v_2021['first_financing_size'].notna()]
        expected = len(v_2021_with_E)
        actual = len(self.panel)

        # Allow small tolerance for merge losses
        passed = abs(expected - actual) / expected < 0.01
        self.add_result(
            'T1.1', 'Company count consistency', passed, 'CRITICAL',
            f"Panel N matches source within 1%",
            expected=str(expected), actual=str(actual)
        )

    def test_T1_2_E_values_match(self):
        """T1.2: E values match first_financing_size."""
        v_2021 = self.vag[self.vag['year'] == 2021][['company_id', 'first_financing_size']].copy()
        v_2021 = v_2021.rename(columns={'first_financing_size': 'E_source'})

        merged = self.panel.merge(v_2021, on='company_id', how='inner')
        valid = merged.dropna(subset=['E', 'E_source'])

        if len(valid) > 0:
            max_diff = np.abs(valid['E'] - valid['E_source']).max()
            passed = max_diff < 1e-6
        else:
            passed = False
            max_diff = np.nan

        self.add_result(
            'T1.2', 'E values match first_financing_size', passed, 'CRITICAL',
            f"Max difference: {max_diff}",
            expected="< 1e-6", actual=f"{max_diff:.2e}"
        )

    def test_T1_3_V_values_match(self):
        """T1.3: V values match vagueness scores."""
        v_2021 = self.vag[self.vag['year'] == 2021][['company_id', 'V']].copy()
        v_2021 = v_2021.rename(columns={'V': 'V_source'})

        merged = self.panel.merge(v_2021, on='company_id', how='inner')
        valid = merged.dropna(subset=['V_0', 'V_source'])

        if len(valid) > 0:
            max_diff = np.abs(valid['V_0'] - valid['V_source']).max()
            passed = max_diff < 1e-6
        else:
            passed = False
            max_diff = np.nan

        self.add_result(
            'T1.3', 'V_0 values match vagueness source', passed, 'CRITICAL',
            f"Max difference: {max_diff}",
            expected="< 1e-6", actual=f"{max_diff:.2e}"
        )

    # =========================================================================
    # Category 2: Transformation Tests
    # =========================================================================

    def test_T2_1_D_formula(self):
        """T2.1: D = V_T - V_0."""
        valid = self.panel.dropna(subset=['V_0', 'V_T', 'D'])
        computed_D = valid['V_T'] - valid['V_0']
        max_diff = np.abs(valid['D'] - computed_D).max()
        passed = max_diff < 1e-10

        self.add_result(
            'T2.1', 'D = V_T - V_0', passed, 'CRITICAL',
            f"Formula verification",
            expected="max_diff < 1e-10", actual=f"{max_diff:.2e}"
        )

    def test_T2_2_M_formula(self):
        """T2.2: M = |D|."""
        valid = self.panel.dropna(subset=['D', 'M'])
        computed_M = np.abs(valid['D'])
        max_diff = np.abs(valid['M'] - computed_M).max()
        passed = max_diff < 1e-10

        self.add_result(
            'T2.2', 'M = |D|', passed, 'CRITICAL',
            f"Formula verification",
            expected="max_diff < 1e-10", actual=f"{max_diff:.2e}"
        )

    def test_T2_3_G_formula(self):
        """T2.3: G = total_raised / E."""
        # Merge with features to get total_raised
        feat_dedup = self.feat.drop_duplicates('CompanyID')
        merged = self.panel.merge(
            feat_dedup[['CompanyID', 'total_raised']],
            left_on='company_id', right_on='CompanyID', how='left'
        )

        # G should equal total_raised / E (or 1.0 if total_raised is NaN)
        valid = merged[(merged['E'] > 0) & merged['total_raised'].notna()]
        computed_G = valid['total_raised'] / valid['E']

        if len(valid) > 0:
            # Allow for G=1.0 fallback cases
            diff = np.abs(valid['G'] - computed_G)
            max_diff = diff.max()
            passed = max_diff < 1e-4 or (diff > 1e-4).mean() < 0.01
        else:
            passed = True
            max_diff = 0

        self.add_result(
            'T2.3', 'G = total_raised / E', passed, 'CRITICAL',
            f"Formula verification (with 1% tolerance for edge cases)",
            expected="max_diff < 1e-4", actual=f"{max_diff:.4f}"
        )

    def test_T2_4_L_formula(self):
        """T2.4: L = "Later Stage VC" indicator."""
        feat_dedup = self.feat.drop_duplicates('CompanyID')
        merged = self.panel.merge(
            feat_dedup[['CompanyID', 'last_financing_deal_type']],
            left_on='company_id', right_on='CompanyID', how='left'
        )

        computed_L = merged['last_financing_deal_type'].str.contains(
            'Later Stage VC', na=False
        ).astype(int)

        match_rate = (merged['L'] == computed_L).mean()
        passed = match_rate > 0.99

        self.add_result(
            'T2.4', 'L = "Later Stage VC" indicator', passed, 'CRITICAL',
            f"Match rate: {match_rate*100:.2f}%",
            expected="> 99%", actual=f"{match_rate*100:.2f}%"
        )

    # =========================================================================
    # Category 3: Classification Tests
    # =========================================================================

    def test_T3_1_stayer_classification(self):
        """T3.1: Stayer classification (M < 5)."""
        stayers = self.panel[self.panel['mover_type'] == 'stayer']
        correct = (stayers['M'] < 5).all()

        self.add_result(
            'T3.1', 'Stayer classification (M < 5)', correct, 'CRITICAL',
            f"All stayers have M < 5",
            expected="True", actual=str(correct)
        )

    def test_T3_2_zoom_in_classification(self):
        """T3.2: Zoom-in classification (M >= 5 AND D < -10)."""
        zoom_in = self.panel[self.panel['mover_type'] == 'zoom_in']
        correct = ((zoom_in['M'] >= 5) & (zoom_in['D'] < -10)).all()

        self.add_result(
            'T3.2', 'Zoom-in classification', correct, 'CRITICAL',
            f"All zoom_in have M >= 5 AND D < -10",
            expected="True", actual=str(correct)
        )

    def test_T3_3_zoom_out_classification(self):
        """T3.3: Zoom-out classification (M >= 5 AND D > 10)."""
        zoom_out = self.panel[self.panel['mover_type'] == 'zoom_out']
        correct = ((zoom_out['M'] >= 5) & (zoom_out['D'] > 10)).all()

        self.add_result(
            'T3.3', 'Zoom-out classification', correct, 'CRITICAL',
            f"All zoom_out have M >= 5 AND D > 10",
            expected="True", actual=str(correct)
        )

    def test_T3_4_horizontal_classification(self):
        """T3.4: Horizontal classification (M >= 5 AND -10 <= D <= 10)."""
        horiz = self.panel[self.panel['mover_type'] == 'horizontal']
        # Exclude NaN values from check
        valid_horiz = horiz.dropna(subset=['M', 'D'])
        correct = ((valid_horiz['M'] >= 5) & (valid_horiz['D'] >= -10) & (valid_horiz['D'] <= 10)).all()
        n_nan = len(horiz) - len(valid_horiz)

        self.add_result(
            'T3.4', 'Horizontal classification', correct, 'CRITICAL',
            f"All horizontal have M >= 5 AND -10 <= D <= 10 (excl. {n_nan} NaN)",
            expected="True", actual=str(correct)
        )

    def test_T3_5_partition_completeness(self):
        """T3.5: All companies classified exactly once."""
        types = self.panel['mover_type'].value_counts()
        total = types.sum()
        n_panel = len(self.panel)

        passed = total == n_panel
        self.add_result(
            'T3.5', 'Partition completeness', passed, 'CRITICAL',
            f"Sum of type counts equals N",
            expected=str(n_panel), actual=str(total)
        )

    # =========================================================================
    # Category 4: Statistical Invariance Tests
    # =========================================================================

    def test_T4_1_N_after_filter(self):
        """T4.1: N after E filter ~ 180,860."""
        n = len(self.panel)
        expected = 180860
        tolerance = 500

        passed = abs(n - expected) < tolerance
        self.add_result(
            'T4.1', 'N after E filter', passed, 'ERROR',
            f"N within {tolerance} of expected",
            expected=f"{expected} ± {tolerance}", actual=str(n)
        )

    def test_T4_2_L_base_rate(self):
        """T4.2: L base rate ~ 11.5%."""
        l_rate = self.panel['L'].mean() * 100
        expected = 11.5
        tolerance = 0.5

        passed = abs(l_rate - expected) < tolerance
        self.add_result(
            'T4.2', 'L base rate', passed, 'ERROR',
            f"L rate within {tolerance}pp of expected",
            expected=f"{expected}% ± {tolerance}pp", actual=f"{l_rate:.2f}%"
        )

    def test_T4_3_rho_G_E(self):
        """T4.3: ρ(G, E) ~ -0.196."""
        valid = self.panel.dropna(subset=['G', 'E'])
        valid = valid[(valid['E'] > 0) & np.isfinite(valid['G'])]

        rho, _ = spearmanr(valid['G'], np.log1p(valid['E']))
        expected = -0.196
        tolerance = 0.03

        passed = abs(rho - expected) < tolerance
        self.add_result(
            'T4.3', 'ρ(G, E)', passed, 'ERROR',
            f"Correlation within tolerance",
            expected=f"{expected} ± {tolerance}", actual=f"{rho:.4f}"
        )

    def test_T4_4_rho_G_M(self):
        """T4.4: ρ(G, M) ~ +0.209."""
        valid = self.panel.dropna(subset=['G', 'M'])
        valid = valid[np.isfinite(valid['G']) & np.isfinite(valid['M'])]

        rho, _ = spearmanr(valid['G'], valid['M'])
        expected = 0.209
        tolerance = 0.03

        passed = abs(rho - expected) < tolerance
        self.add_result(
            'T4.4', 'ρ(G, M)', passed, 'ERROR',
            f"Correlation within tolerance",
            expected=f"{expected} ± {tolerance}", actual=f"{rho:.4f}"
        )

    def test_T4_5_rho_M_E(self):
        """T4.5: ρ(M, E) ~ -0.117."""
        valid = self.panel.dropna(subset=['M', 'E'])
        valid = valid[(valid['E'] > 0) & np.isfinite(valid['M'])]

        rho, _ = spearmanr(valid['M'], np.log1p(valid['E']))
        expected = -0.117
        tolerance = 0.03

        passed = abs(rho - expected) < tolerance
        self.add_result(
            'T4.5', 'ρ(M, E)', passed, 'ERROR',
            f"Correlation within tolerance",
            expected=f"{expected} ± {tolerance}", actual=f"{rho:.4f}"
        )

    # =========================================================================
    # Category 5: Distributional Tests
    # =========================================================================

    def test_T5_1_V0_range(self):
        """T5.1: V_0 range [0, 100]."""
        valid = self.panel['V_0'].dropna()
        in_range = (valid >= 0).all() and (valid <= 100).all()

        self.add_result(
            'T5.1', 'V_0 range [0, 100]', in_range, 'ERROR',
            f"Range: [{valid.min():.1f}, {valid.max():.1f}]",
            expected="[0, 100]", actual=f"[{valid.min():.1f}, {valid.max():.1f}]"
        )

    def test_T5_2_VT_range(self):
        """T5.2: V_T range [0, 100]."""
        valid = self.panel['V_T'].dropna()
        in_range = (valid >= 0).all() and (valid <= 100).all()

        self.add_result(
            'T5.2', 'V_T range [0, 100]', in_range, 'ERROR',
            f"Range: [{valid.min():.1f}, {valid.max():.1f}]",
            expected="[0, 100]", actual=f"[{valid.min():.1f}, {valid.max():.1f}]"
        )

    def test_T5_5_G_positivity(self):
        """T5.5: G >= 0 (or NaN)."""
        valid = self.panel['G'].dropna()
        n_negative = (valid < 0).sum()
        passed = n_negative == 0

        self.add_result(
            'T5.5', 'G positivity', passed, 'WARNING',
            f"Negative G values: {n_negative}",
            expected="0", actual=str(n_negative)
        )

    def test_T5_6_L_binary(self):
        """T5.6: L ∈ {0, 1}."""
        unique = set(self.panel['L'].unique())
        passed = unique.issubset({0, 1})

        self.add_result(
            'T5.6', 'L binary', passed, 'CRITICAL',
            f"Unique L values: {unique}",
            expected="{0, 1}", actual=str(unique)
        )

    # =========================================================================
    # Category 6: Merge Integrity Tests
    # =========================================================================

    def test_T6_1_no_duplicates(self):
        """T6.1: No duplicate company_ids."""
        n_unique = self.panel['company_id'].nunique()
        n_total = len(self.panel)
        passed = n_unique == n_total

        self.add_result(
            'T6.1', 'No duplicate company_ids', passed, 'CRITICAL',
            f"Unique: {n_unique}, Total: {n_total}",
            expected=str(n_total), actual=str(n_unique)
        )

    # =========================================================================
    # Category 8: Edge Case Tests
    # =========================================================================

    def test_T8_4_no_inf(self):
        """T8.4: No infinite values in G."""
        n_inf = np.isinf(self.panel['G']).sum()
        passed = n_inf == 0

        self.add_result(
            'T8.4', 'No infinite G values', passed, 'CRITICAL',
            f"Infinite values: {n_inf}",
            expected="0", actual=str(n_inf)
        )

    # =========================================================================
    # Category 10: Regression Tests
    # =========================================================================

    def test_T10_1_mover_success_rate(self):
        """T10.1: Mover success rate ~ 17.7%."""
        movers = self.panel[self.panel['mover_type'] != 'stayer']
        rate = movers['L'].mean() * 100
        expected = 17.7
        tolerance = 1.0

        passed = abs(rate - expected) < tolerance
        self.add_result(
            'T10.1', 'Mover success rate', passed, 'WARNING',
            f"Rate within {tolerance}pp",
            expected=f"{expected}% ± {tolerance}pp", actual=f"{rate:.1f}%"
        )

    def test_T10_2_stayer_success_rate(self):
        """T10.2: Stayer success rate ~ 10.8%."""
        stayers = self.panel[self.panel['mover_type'] == 'stayer']
        rate = stayers['L'].mean() * 100
        expected = 10.8
        tolerance = 1.0

        passed = abs(rate - expected) < tolerance
        self.add_result(
            'T10.2', 'Stayer success rate', passed, 'WARNING',
            f"Rate within {tolerance}pp",
            expected=f"{expected}% ± {tolerance}pp", actual=f"{rate:.1f}%"
        )

    def test_T10_4_stayer_proportion(self):
        """T10.4: Stayer proportion ~ 91%."""
        prop = (self.panel['mover_type'] == 'stayer').mean() * 100
        expected = 91.0
        tolerance = 2.0

        passed = abs(prop - expected) < tolerance
        self.add_result(
            'T10.4', 'Stayer proportion', passed, 'WARNING',
            f"Proportion within {tolerance}pp",
            expected=f"{expected}% ± {tolerance}pp", actual=f"{prop:.1f}%"
        )

    # =========================================================================
    # Run All Tests
    # =========================================================================

    def run_all_tests(self):
        """Run all tests and return results."""
        if not self.data_loaded:
            self.load_data()

        # Category 1: Identity Tests
        self.test_T1_1_company_count()
        self.test_T1_2_E_values_match()
        self.test_T1_3_V_values_match()

        # Category 2: Transformation Tests
        self.test_T2_1_D_formula()
        self.test_T2_2_M_formula()
        self.test_T2_3_G_formula()
        self.test_T2_4_L_formula()

        # Category 3: Classification Tests
        self.test_T3_1_stayer_classification()
        self.test_T3_2_zoom_in_classification()
        self.test_T3_3_zoom_out_classification()
        self.test_T3_4_horizontal_classification()
        self.test_T3_5_partition_completeness()

        # Category 4: Statistical Invariance Tests
        self.test_T4_1_N_after_filter()
        self.test_T4_2_L_base_rate()
        self.test_T4_3_rho_G_E()
        self.test_T4_4_rho_G_M()
        self.test_T4_5_rho_M_E()

        # Category 5: Distributional Tests
        self.test_T5_1_V0_range()
        self.test_T5_2_VT_range()
        self.test_T5_5_G_positivity()
        self.test_T5_6_L_binary()

        # Category 6: Merge Integrity Tests
        self.test_T6_1_no_duplicates()

        # Category 8: Edge Case Tests
        self.test_T8_4_no_inf()

        # Category 10: Regression Tests
        self.test_T10_1_mover_success_rate()
        self.test_T10_2_stayer_success_rate()
        self.test_T10_4_stayer_proportion()

        return self.results

    def generate_report(self) -> str:
        """Generate human-readable report."""
        lines = []
        lines.append("=" * 80)
        lines.append("DATA VALIDATION REPORT")
        lines.append("=" * 80)
        lines.append(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append(f"Data: thesis_panel_v3.nc")
        lines.append("")

        # Summary by severity
        for severity in ['CRITICAL', 'ERROR', 'WARNING', 'INFO']:
            tests = [r for r in self.results if r.severity == severity]
            passed = sum(1 for r in tests if r.passed)
            failed = len(tests) - passed
            if severity in ['CRITICAL', 'ERROR']:
                lines.append(f"{severity}: {failed} FAILED / {passed} PASSED")
            else:
                lines.append(f"{severity}: {failed} FLAGGED / {passed} PASSED")

        lines.append("")
        lines.append("-" * 80)
        lines.append("DETAILED RESULTS")
        lines.append("-" * 80)

        for r in self.results:
            status = "[PASS]" if r.passed else "[FAIL]"
            lines.append(f"{status} {r.test_id} {r.name}: {r.message}")
            if not r.passed:
                lines.append(f"       Expected: {r.expected}, Actual: {r.actual}")

        lines.append("")
        lines.append("=" * 80)

        # Overall status
        critical_failed = sum(1 for r in self.results if r.severity == 'CRITICAL' and not r.passed)
        error_failed = sum(1 for r in self.results if r.severity == 'ERROR' and not r.passed)

        if critical_failed > 0:
            lines.append("OVERALL STATUS: FAIL (CRITICAL)")
        elif error_failed > 0:
            lines.append("OVERALL STATUS: FAIL (ERROR)")
        else:
            warning_failed = sum(1 for r in self.results if r.severity == 'WARNING' and not r.passed)
            if warning_failed > 0:
                lines.append("OVERALL STATUS: PASS (with warnings)")
            else:
                lines.append("OVERALL STATUS: PASS")

        lines.append("=" * 80)

        return "\n".join(lines)

    def to_json(self) -> dict:
        """Export results as JSON."""
        return {
            'timestamp': datetime.now().isoformat(),
            'data_file': 'thesis_panel_v3.nc',
            'summary': {
                'total': len(self.results),
                'passed': sum(1 for r in self.results if r.passed),
                'failed': sum(1 for r in self.results if not r.passed),
            },
            'results': [
                {
                    'test_id': r.test_id,
                    'name': r.name,
                    'passed': r.passed,
                    'severity': r.severity,
                    'message': r.message,
                    'expected': r.expected,
                    'actual': r.actual,
                }
                for r in self.results
            ]
        }


def main():
    parser = argparse.ArgumentParser(description='Run data integrity tests')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    parser.add_argument('--json-output', '-j', action='store_true', help='Output as JSON')
    args = parser.parse_args()

    print("Running data integrity tests...")
    validator = DataValidator(verbose=args.verbose)
    validator.run_all_tests()

    if args.json_output:
        result = validator.to_json()
        print(json.dumps(result, indent=2))
    else:
        print(validator.generate_report())

    # Exit code
    critical_failed = sum(1 for r in validator.results if r.severity == 'CRITICAL' and not r.passed)
    error_failed = sum(1 for r in validator.results if r.severity == 'ERROR' and not r.passed)

    if critical_failed > 0:
        sys.exit(2)
    elif error_failed > 0:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
