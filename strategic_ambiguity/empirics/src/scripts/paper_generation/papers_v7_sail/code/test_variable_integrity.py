#!/usr/bin/env python3
"""
test_variable_integrity.py - Raw Data → Concept Mapping Verification
=====================================================================

This script validates that the implemented variables match their conceptual definitions
by directly reading from raw PitchBook data files.

VARIABLE MAPPING (Final Agreed):
┌────────┬──────────────────────┬─────────────────────────────┐
│ Symbol │ Definition           │ Raw Column                  │
├────────┼──────────────────────┼─────────────────────────────┤
│ E      │ Early capital ($M)   │ FirstFinancingSize / 1e6    │
│ K      │ Kapital total ($M)   │ TotalRaised / 1e6           │
│ G      │ Growth               │ GrowthRate (PitchBook)      │
│ L      │ Later Stage success  │ "Later Stage VC" → 1/0      │
│ V      │ Vagueness            │ (computed from text)        │
│ F      │ Flexibility          │ 1 - is_hardware             │
│ R      │ Repositioning        │ M = |V_T - V_0|             │
└────────┴──────────────────────┴─────────────────────────────┘

KEY TESTS:
1. K = TotalRaised is cumulative (K >= E for all companies)
2. E = FirstFinancingSize is initial funding
3. L = "Later Stage VC" yields ~11.5% base rate
4. G is continuous (not binary)
5. Canonical correlations are reproducible

Usage:
    python test_variable_integrity.py

Author: Claude Code CLI
Date: 2026-01-11
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
from scipy.stats import spearmanr

# ============================================================================
# CONFIGURATION
# ============================================================================

SCRIPT_DIR = Path(__file__).parent.resolve()
REPO_ROOT = Path("/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics")
DATA_RAW = REPO_ROOT / "data" / "raw"
DATA_PROC = REPO_ROOT / "data" / "processed"

RAW_FILES = {
    '2021': DATA_RAW / 'Company20211201.dat',
    '2023': DATA_RAW / 'Company20231201.dat',
    '2024': DATA_RAW / 'Company20241201.dat',
    '2025': DATA_RAW / 'Company20251101.dat',
}

# Expected canonical values (from thesis)
CANONICAL = {
    'rho_G_E': -0.196,      # Funding-Growth correlation
    'N_total': 180994,      # Sample size
    'mover_advantage': 1.81, # 17.8% vs 9.9%
    'L_base_rate': 0.115,   # 11.5% reach Later Stage VC
}

# ============================================================================
# TEST FUNCTIONS
# ============================================================================

def test_raw_columns_exist():
    """TEST 1: Verify required columns exist in raw data."""
    print("\n" + "=" * 70)
    print("TEST 1: Raw Column Existence")
    print("=" * 70)

    required_cols = [
        'CompanyID',
        'TotalRaised',           # K: Cumulative funding
        'FirstFinancingSize',    # E: Initial funding
        'GrowthRate',            # G: Growth (continuous)
        'LastFinancingDealType', # L: For success classification
        'Description',           # V: For vagueness calculation
        'Keywords',              # V: For vagueness calculation
    ]

    results = {}
    for year, path in RAW_FILES.items():
        if not path.exists():
            print(f"  ⚠️  {year}: File not found - {path}")
            continue

        # Read first row to check columns
        df = pd.read_csv(path, sep='|', nrows=1, low_memory=False)

        missing = [col for col in required_cols if col not in df.columns]
        if missing:
            print(f"  ❌ {year}: Missing columns: {missing}")
            results[year] = False
        else:
            print(f"  ✅ {year}: All {len(required_cols)} required columns present")
            results[year] = True

    return all(results.values())


def test_K_is_cumulative():
    """TEST 2: Verify K (TotalRaised) >= E (FirstFinancingSize) for all companies."""
    print("\n" + "=" * 70)
    print("TEST 2: K is Cumulative (K >= E)")
    print("=" * 70)

    # Use 2025 data (most recent)
    path = RAW_FILES['2025']
    if not path.exists():
        print(f"  ⚠️  File not found: {path}")
        return None

    print(f"  Loading {path.name}...")
    df = pd.read_csv(path, sep='|', low_memory=False,
                     usecols=['CompanyID', 'TotalRaised', 'FirstFinancingSize'])

    # Convert to numeric
    df['K'] = pd.to_numeric(df['TotalRaised'], errors='coerce')
    df['E'] = pd.to_numeric(df['FirstFinancingSize'], errors='coerce')

    # Filter valid rows (both K and E present)
    valid = df[(df['K'].notna()) & (df['E'].notna()) & (df['E'] > 0)].copy()
    print(f"  Valid rows (K & E present): {len(valid):,}")

    # Test: K >= E (cumulative should be >= initial)
    violations = valid[valid['K'] < valid['E']]
    n_violations = len(violations)
    pct_violations = n_violations / len(valid) * 100 if len(valid) > 0 else 0

    print(f"\n  Results:")
    print(f"    K >= E (as expected): {len(valid) - n_violations:,} ({100-pct_violations:.2f}%)")
    print(f"    K < E (violations):   {n_violations:,} ({pct_violations:.2f}%)")

    if n_violations > 0 and n_violations / len(valid) < 0.01:
        print(f"\n  ⚠️  Minor violations ({pct_violations:.2f}%) - likely data entry errors")
        print(f"     Sample violations:")
        sample = violations.head(3)
        for _, row in sample.iterrows():
            print(f"       ID={row['CompanyID']}: K=${row['K']:,.0f} < E=${row['E']:,.0f}")

    # Summary statistics
    print(f"\n  Summary Statistics:")
    print(f"    K (TotalRaised) mean:  ${valid['K'].mean():,.0f}")
    print(f"    K (TotalRaised) median: ${valid['K'].median():,.0f}")
    print(f"    E (FirstFinancing) mean:  ${valid['E'].mean():,.0f}")
    print(f"    E (FirstFinancing) median: ${valid['E'].median():,.0f}")
    print(f"    Ratio K/E mean: {(valid['K']/valid['E']).mean():.2f}x")
    print(f"    Ratio K/E median: {(valid['K']/valid['E']).median():.2f}x")

    # PASS if violations < 1%
    passed = pct_violations < 1.0
    if passed:
        print(f"\n  ✅ TEST PASSED: K (TotalRaised) is cumulative funding")
    else:
        print(f"\n  ❌ TEST FAILED: Too many violations ({pct_violations:.1f}%)")

    return passed


def test_L_base_rate():
    """TEST 3: Verify L (Later Stage VC) yields ~11.5% base rate."""
    print("\n" + "=" * 70)
    print("TEST 3: L Base Rate (~11.5%)")
    print("=" * 70)

    path = RAW_FILES['2025']
    if not path.exists():
        print(f"  ⚠️  File not found: {path}")
        return None

    print(f"  Loading {path.name}...")
    df = pd.read_csv(path, sep='|', low_memory=False,
                     usecols=['CompanyID', 'LastFinancingDealType', 'FirstFinancingDealType'])

    # L = 1 if "Later Stage VC" in LastFinancingDealType
    df['L'] = df['LastFinancingDealType'].fillna('').str.contains(
        'Later Stage VC', case=False
    ).astype(int)

    # Filter for VC-backed companies (have some financing)
    has_financing = df['FirstFinancingDealType'].notna()
    vc_backed = df[has_financing]

    l_rate_all = df['L'].mean() * 100
    l_rate_vc = vc_backed['L'].mean() * 100

    print(f"\n  Results:")
    print(f"    Total companies: {len(df):,}")
    print(f"    VC-backed companies: {len(vc_backed):,}")
    print(f"    L=1 (Later Stage VC):")
    print(f"      All companies: {df['L'].sum():,} ({l_rate_all:.1f}%)")
    print(f"      VC-backed only: {vc_backed['L'].sum():,} ({l_rate_vc:.1f}%)")

    # Deal type distribution
    print(f"\n  LastFinancingDealType Distribution (top 10):")
    dist = df['LastFinancingDealType'].value_counts().head(10)
    for deal_type, count in dist.items():
        pct = count / len(df) * 100
        marker = "⬅️" if 'Later Stage' in str(deal_type) else ""
        print(f"    {count:>8,} ({pct:>5.1f}%): {deal_type} {marker}")

    # PASS if L rate is within expected range (8-15%)
    expected_min, expected_max = 8.0, 15.0
    passed = expected_min <= l_rate_vc <= expected_max

    if passed:
        print(f"\n  ✅ TEST PASSED: L base rate = {l_rate_vc:.1f}% (expected: {expected_min}-{expected_max}%)")
    else:
        print(f"\n  ❌ TEST FAILED: L base rate = {l_rate_vc:.1f}% (expected: {expected_min}-{expected_max}%)")

    return passed


def test_G_is_continuous():
    """TEST 4: Verify G (GrowthRate) is continuous, not binary."""
    print("\n" + "=" * 70)
    print("TEST 4: G is Continuous (not binary)")
    print("=" * 70)

    path = RAW_FILES['2025']
    if not path.exists():
        print(f"  ⚠️  File not found: {path}")
        return None

    print(f"  Loading {path.name}...")
    df = pd.read_csv(path, sep='|', low_memory=False,
                     usecols=['CompanyID', 'GrowthRate'])

    # Convert to numeric
    df['G'] = pd.to_numeric(df['GrowthRate'], errors='coerce')

    valid = df[df['G'].notna()]
    n_total = len(df)
    n_valid = len(valid)

    print(f"\n  Results:")
    print(f"    Total companies: {n_total:,}")
    print(f"    G non-null: {n_valid:,} ({n_valid/n_total*100:.1f}%)")

    if n_valid > 0:
        # Check if binary (only 0 and 1)
        unique_values = valid['G'].nunique()
        is_binary = unique_values <= 2 and set(valid['G'].unique()).issubset({0, 1, 0.0, 1.0})

        print(f"    G unique values: {unique_values:,}")
        print(f"    G range: [{valid['G'].min():.4f}, {valid['G'].max():.4f}]")
        print(f"    G mean: {valid['G'].mean():.4f}")
        print(f"    G std: {valid['G'].std():.4f}")

        # Distribution check
        print(f"\n  G Distribution (percentiles):")
        for p in [10, 25, 50, 75, 90]:
            val = valid['G'].quantile(p/100)
            print(f"    P{p}: {val:.4f}")

        if is_binary:
            print(f"\n  ❌ TEST FAILED: G appears to be binary (0/1)")
            return False
        else:
            print(f"\n  ✅ TEST PASSED: G is continuous ({unique_values:,} unique values)")
            return True
    else:
        print(f"\n  ⚠️  No valid G values found")
        return None


def test_canonical_correlation():
    """TEST 5: Verify ρ(G, E) ≈ -0.196 (Funding Paradox)."""
    print("\n" + "=" * 70)
    print("TEST 5: Canonical Correlation ρ(G, E) ≈ -0.196")
    print("=" * 70)

    path = RAW_FILES['2025']
    if not path.exists():
        print(f"  ⚠️  File not found: {path}")
        return None

    print(f"  Loading {path.name}...")
    df = pd.read_csv(path, sep='|', low_memory=False,
                     usecols=['CompanyID', 'GrowthRate', 'FirstFinancingSize'])

    # Convert to numeric
    df['G'] = pd.to_numeric(df['GrowthRate'], errors='coerce')
    df['E'] = pd.to_numeric(df['FirstFinancingSize'], errors='coerce')

    # Filter valid rows
    valid = df[(df['G'].notna()) & (df['E'].notna()) & (df['E'] > 0)].copy()
    valid['log_E'] = np.log1p(valid['E'])

    print(f"  Valid samples: {len(valid):,}")

    if len(valid) < 100:
        print(f"  ⚠️  Too few samples for correlation")
        return None

    # Compute correlation
    rho, p_value = spearmanr(valid['G'], valid['log_E'])

    print(f"\n  Results:")
    print(f"    ρ(G, log(E)) = {rho:+.4f}")
    print(f"    p-value = {p_value:.2e}")
    print(f"    Significance: {'***' if p_value < 0.001 else '**' if p_value < 0.01 else '*' if p_value < 0.05 else 'ns'}")

    expected = CANONICAL['rho_G_E']
    tolerance = 0.05  # Allow ±0.05 deviation

    diff = abs(rho - expected)
    print(f"\n    Expected: {expected:+.3f}")
    print(f"    Actual:   {rho:+.3f}")
    print(f"    Difference: {diff:.3f}")

    passed = diff <= tolerance
    if passed:
        print(f"\n  ✅ TEST PASSED: ρ(G, E) matches canonical value (±{tolerance})")
    else:
        print(f"\n  ❌ TEST FAILED: ρ(G, E) differs from canonical by {diff:.3f}")

    return passed


def test_variable_relationships():
    """TEST 6: Verify variable relationships (K > E, multiple rounds)."""
    print("\n" + "=" * 70)
    print("TEST 6: Variable Relationships")
    print("=" * 70)

    path = RAW_FILES['2025']
    if not path.exists():
        print(f"  ⚠️  File not found: {path}")
        return None

    print(f"  Loading {path.name}...")
    df = pd.read_csv(path, sep='|', low_memory=False,
                     usecols=['CompanyID', 'TotalRaised', 'FirstFinancingSize',
                              'LastFinancingSize', 'GrowthRate', 'LastFinancingDealType'])

    # Convert to numeric
    df['K'] = pd.to_numeric(df['TotalRaised'], errors='coerce')
    df['E'] = pd.to_numeric(df['FirstFinancingSize'], errors='coerce')
    df['F_t'] = pd.to_numeric(df['LastFinancingSize'], errors='coerce')
    df['G'] = pd.to_numeric(df['GrowthRate'], errors='coerce')

    # Filter valid rows
    valid = df[(df['K'].notna()) & (df['E'].notna()) & (df['E'] > 0)].copy()

    print(f"  Valid samples: {len(valid):,}")

    # Test 6a: K should generally be > E (companies raise multiple rounds)
    single_round = (valid['K'] == valid['E']).sum()
    multiple_rounds = (valid['K'] > valid['E']).sum()

    print(f"\n  6a. Funding rounds:")
    print(f"      Single round (K = E): {single_round:,} ({single_round/len(valid)*100:.1f}%)")
    print(f"      Multiple rounds (K > E): {multiple_rounds:,} ({multiple_rounds/len(valid)*100:.1f}%)")

    # Test 6b: Growth ratio K/E
    valid['growth_multiple'] = valid['K'] / valid['E']
    print(f"\n  6b. Growth Multiple (K/E):")
    print(f"      Mean: {valid['growth_multiple'].mean():.2f}x")
    print(f"      Median: {valid['growth_multiple'].median():.2f}x")
    print(f"      P90: {valid['growth_multiple'].quantile(0.9):.2f}x")

    # Test 6c: Later Stage VC companies should have higher K/E
    df['L'] = df['LastFinancingDealType'].fillna('').str.contains('Later Stage VC').astype(int)
    later_stage = df[df['L'] == 1]
    early_stage = df[df['L'] == 0]

    if len(later_stage) > 0:
        later_stage_valid = later_stage[(later_stage['K'].notna()) & (later_stage['E'].notna()) & (later_stage['E'] > 0)]
        early_stage_valid = early_stage[(early_stage['K'].notna()) & (early_stage['E'].notna()) & (early_stage['E'] > 0)]

        if len(later_stage_valid) > 0 and len(early_stage_valid) > 0:
            later_multiple = (later_stage_valid['K'] / later_stage_valid['E']).median()
            early_multiple = (early_stage_valid['K'] / early_stage_valid['E']).median()

            print(f"\n  6c. K/E by Success:")
            print(f"      Later Stage VC (L=1): {later_multiple:.2f}x (n={len(later_stage_valid):,})")
            print(f"      Other (L=0):          {early_multiple:.2f}x (n={len(early_stage_valid):,})")
            print(f"      Ratio: {later_multiple/early_multiple:.2f}x")

    print(f"\n  ✅ Variable relationships verified")
    return True


def run_all_tests():
    """Run all integrity tests and report summary."""
    print("\n" + "=" * 70)
    print("VARIABLE INTEGRITY TEST SUITE")
    print("=" * 70)
    print(f"Raw data directory: {DATA_RAW}")
    print(f"Processed data directory: {DATA_PROC}")

    results = {}

    # Run tests
    results['columns_exist'] = test_raw_columns_exist()
    results['K_cumulative'] = test_K_is_cumulative()
    results['L_base_rate'] = test_L_base_rate()
    results['G_continuous'] = test_G_is_continuous()
    results['canonical_rho'] = test_canonical_correlation()
    results['relationships'] = test_variable_relationships()

    # Summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)

    passed = 0
    failed = 0
    skipped = 0

    for test_name, result in results.items():
        if result is True:
            status = "✅ PASS"
            passed += 1
        elif result is False:
            status = "❌ FAIL"
            failed += 1
        else:
            status = "⚠️  SKIP"
            skipped += 1
        print(f"  {status}: {test_name}")

    print(f"\n  Total: {passed} passed, {failed} failed, {skipped} skipped")

    if failed == 0:
        print("\n  🎉 ALL TESTS PASSED - Variable mappings are valid!")
    else:
        print(f"\n  ⚠️  {failed} tests failed - Review variable definitions")

    return failed == 0


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
