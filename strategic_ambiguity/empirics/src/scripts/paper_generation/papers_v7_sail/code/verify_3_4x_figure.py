#!/usr/bin/env python3
"""
verify_3_4x_figure.py - Rigorous Verification of the 3.4× Mover Advantage
=========================================================================

Critical verification script for the most important figure in the thesis:
The funding growth multiple comparison between Movers and Stayers.

Expected values from §4.6 illustrative cases:
- Hope Care (Broadening Mover): G = 2.71×
- True Botanicals (Narrowing Mover): G = 2.45×
- Leap Green Energy (Stayer): G = 0.80×
- Mover/Stayer ratio ≈ 3.4×

This script verifies these figures using multiple methods:
1. Direct calculation from raw data
2. Cross-validation with different definitions
3. Statistical significance testing
4. Sensitivity analysis

Author: Claude Code CLI
Date: 2026-01-14
"""

import json
import numpy as np
import pandas as pd
import xarray as xr
from pathlib import Path
from scipy.stats import (
    spearmanr, pearsonr, mannwhitneyu, ttest_ind,
    bootstrap, median_abs_deviation
)
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# PATHS
# ============================================================================
SCRIPT_DIR = Path(__file__).parent.resolve()
DATA_DIR = SCRIPT_DIR / 'data'
REPO_ROOT = Path("/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics")
PROCESSED_DATA = REPO_ROOT / "data" / "processed"

# Try multiple locations for data
DATA_PATHS = [
    DATA_DIR / 'thesis_panel_v3.nc',
    DATA_DIR / 'processed' / 'thesis_panel_v3.nc',
    PROCESSED_DATA / 'thesis_panel_v3.nc',
]

# ============================================================================
# OUTPUT FORMATTING
# ============================================================================
def print_header(title):
    """Print formatted header."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)

def print_section(title):
    """Print section header."""
    print(f"\n--- {title} ---")

def print_result(label, value, unit="", note=""):
    """Print formatted result."""
    note_str = f"  ({note})" if note else ""
    print(f"  {label}: {value}{unit}{note_str}")

# ============================================================================
# DATA LOADING
# ============================================================================
def load_data():
    """Load thesis panel data from available sources."""
    for path in DATA_PATHS:
        if path.exists():
            ds = xr.open_dataset(path)
            df = ds.to_dataframe().reset_index()
            ds.close()
            print(f"✓ Loaded data from: {path}")
            print(f"  Rows: {len(df):,}")
            print(f"  Columns: {list(df.columns)}")
            return df

    raise FileNotFoundError(f"No data file found. Tried: {DATA_PATHS}")

# ============================================================================
# CORE VERIFICATION: G (Growth Multiple) Definition
# ============================================================================
def verify_G_definition(df):
    """
    Verify the G (Growth Multiple) calculation.

    G = (F_T - E) / E = Funding Growth Multiple
    Where:
    - E = Early funding (Series A amount)
    - F_T = Total funding at time T
    """
    print_section("G (Growth Multiple) Definition Verification")

    # Check what columns we have
    if 'G' in df.columns:
        g_values = df['G'].dropna()
        print(f"  G column exists: {len(g_values):,} valid values")
        print(f"  G range: [{g_values.min():.3f}, {g_values.max():.3f}]")
        print(f"  G mean: {g_values.mean():.3f}")
        print(f"  G median: {g_values.median():.3f}")
        return df

    # Calculate G from E if needed
    if 'E' in df.columns and 'total_raised' in df.columns:
        df['G_calc'] = (df['total_raised'] - df['E']) / df['E']
        print("  Calculated G from E and total_raised")
        return df

    print("  WARNING: Cannot verify G calculation - missing columns")
    return df

# ============================================================================
# CORE VERIFICATION: Mover/Stayer Classification
# ============================================================================
def classify_movers_stayers(df):
    """
    Classify ventures as Movers (R > 0) or Stayers (R = 0).

    R = |V_T - V_0| = Magnitude of repositioning
    Or equivalently: R = M (magnitude column)
    """
    print_section("Mover/Stayer Classification")

    # Use M column if available (magnitude of repositioning)
    if 'M' in df.columns:
        df['R'] = df['M'].copy()
        print("  Using M column for repositioning magnitude")
    elif 'D' in df.columns:
        df['R'] = df['D'].abs()
        print("  Calculated R from |D|")
    elif 'V_0' in df.columns and 'V_T' in df.columns:
        df['R'] = (df['V_T'] - df['V_0']).abs()
        print("  Calculated R from |V_T - V_0|")
    else:
        print("  ERROR: Cannot compute R - missing columns")
        return df, None, None

    # Filter valid values
    df_valid = df[df['R'].notna() & df['G'].notna()].copy()

    # Classify: Mover (R > 0) vs Stayer (R = 0)
    df_valid['is_mover'] = (df_valid['R'] > 0).astype(int)

    movers = df_valid[df_valid['is_mover'] == 1]
    stayers = df_valid[df_valid['is_mover'] == 0]

    print(f"\n  Total valid: {len(df_valid):,}")
    print(f"  Movers (R > 0): {len(movers):,} ({len(movers)/len(df_valid)*100:.1f}%)")
    print(f"  Stayers (R = 0): {len(stayers):,} ({len(stayers)/len(df_valid)*100:.1f}%)")

    return df_valid, movers, stayers

# ============================================================================
# PRIMARY VERIFICATION: 3.4× Figure
# ============================================================================
def verify_3_4x_ratio(df_valid, movers, stayers):
    """
    CRITICAL: Verify the 3.4× Mover Advantage in funding growth.

    Expected from §4.6:
    - Movers: ~2.71× funding growth
    - Stayers: ~0.80× funding growth
    - Ratio: ~3.4×
    """
    print_header("3.4× MOVER ADVANTAGE VERIFICATION")

    # -------------------------------------------------------------------------
    # 1. PRIMARY METRIC: Median Funding Growth Multiple (G)
    # -------------------------------------------------------------------------
    print_section("1. Primary Metric: Median Funding Growth (G)")

    mover_G_median = movers['G'].median()
    stayer_G_median = stayers['G'].median()
    ratio_median = mover_G_median / stayer_G_median if stayer_G_median != 0 else np.nan

    print_result("Mover median G", f"{mover_G_median:.3f}", "×")
    print_result("Stayer median G", f"{stayer_G_median:.3f}", "×")
    print_result("Mover/Stayer Ratio", f"{ratio_median:.2f}", "×", "TARGET: ~3.4×")

    # -------------------------------------------------------------------------
    # 2. ROBUSTNESS CHECK: Mean Funding Growth
    # -------------------------------------------------------------------------
    print_section("2. Robustness: Mean Funding Growth (G)")

    mover_G_mean = movers['G'].mean()
    stayer_G_mean = stayers['G'].mean()
    ratio_mean = mover_G_mean / stayer_G_mean if stayer_G_mean != 0 else np.nan

    print_result("Mover mean G", f"{mover_G_mean:.3f}", "×")
    print_result("Stayer mean G", f"{stayer_G_mean:.3f}", "×")
    print_result("Mover/Stayer Ratio (mean)", f"{ratio_mean:.2f}", "×")

    # -------------------------------------------------------------------------
    # 3. ALTERNATIVE METRIC: Success Rate (Binary L)
    # -------------------------------------------------------------------------
    print_section("3. Alternative Metric: Success Rate (L)")

    if 'L' in df_valid.columns:
        mover_success = movers['L'].mean() * 100
        stayer_success = stayers['L'].mean() * 100
        ratio_success = mover_success / stayer_success if stayer_success > 0 else np.nan

        print_result("Mover success rate", f"{mover_success:.1f}", "%")
        print_result("Stayer success rate", f"{stayer_success:.1f}", "%")
        print_result("Mover Advantage", f"{ratio_success:.2f}", "×", "TARGET: ~2.6×")

    # -------------------------------------------------------------------------
    # 4. STATISTICAL SIGNIFICANCE
    # -------------------------------------------------------------------------
    print_section("4. Statistical Significance Tests")

    # Mann-Whitney U test (non-parametric)
    u_stat, p_mann = mannwhitneyu(movers['G'], stayers['G'], alternative='greater')
    print_result("Mann-Whitney U", f"{u_stat:,.0f}")
    print_result("p-value (one-sided)", f"{p_mann:.2e}", note="Movers > Stayers")

    # Welch's t-test (parametric)
    t_stat, p_ttest = ttest_ind(movers['G'], stayers['G'], equal_var=False)
    print_result("Welch's t", f"{t_stat:.2f}")
    print_result("p-value (two-sided)", f"{p_ttest:.2e}")

    # Effect size (Cohen's d)
    pooled_std = np.sqrt((movers['G'].std()**2 + stayers['G'].std()**2) / 2)
    cohens_d = (mover_G_mean - stayer_G_mean) / pooled_std if pooled_std > 0 else np.nan
    print_result("Cohen's d", f"{cohens_d:.3f}", note="Effect size")

    # -------------------------------------------------------------------------
    # 5. BOOTSTRAP CONFIDENCE INTERVALS
    # -------------------------------------------------------------------------
    print_section("5. Bootstrap 95% Confidence Intervals")

    def ratio_statistic(mover_g, stayer_g, axis=None):
        """Calculate median ratio for bootstrap."""
        m_med = np.median(mover_g, axis=axis)
        s_med = np.median(stayer_g, axis=axis)
        return m_med / s_med if np.all(s_med != 0) else np.nan

    # Bootstrap the ratio
    n_bootstrap = 1000
    bootstrap_ratios = []
    for _ in range(n_bootstrap):
        m_sample = movers['G'].sample(n=len(movers), replace=True)
        s_sample = stayers['G'].sample(n=len(stayers), replace=True)
        s_med = s_sample.median()
        if s_med != 0 and not np.isnan(s_med):
            ratio = m_sample.median() / s_med
            if not np.isnan(ratio):
                bootstrap_ratios.append(ratio)

    if len(bootstrap_ratios) > 0:
        bootstrap_ratios = np.array(bootstrap_ratios)
        ci_lower = np.percentile(bootstrap_ratios, 2.5)
        ci_upper = np.percentile(bootstrap_ratios, 97.5)
    else:
        ci_lower, ci_upper = np.nan, np.nan
        print("  WARNING: Bootstrap failed due to zero medians")

    print_result("Median Ratio", f"{ratio_median:.2f}", "×")
    print_result("95% CI", f"[{ci_lower:.2f}, {ci_upper:.2f}]", "×")

    # -------------------------------------------------------------------------
    # 6. VALIDATION AGAINST CASE STUDIES
    # -------------------------------------------------------------------------
    print_section("6. Case Study Validation")
    print("  Expected from §4.6 illustrative cases:")
    print("    - Hope Care (Broadening Mover): G = 2.71×")
    print("    - True Botanicals (Narrowing Mover): G = 2.45×")
    print("    - Leap Green Energy (Stayer): G = 0.80×")
    print("    - Average Mover: (2.71 + 2.45) / 2 = 2.58×")
    print("    - Expected Ratio: 2.58 / 0.80 = 3.23×")

    return {
        'mover_G_median': mover_G_median,
        'stayer_G_median': stayer_G_median,
        'ratio_median': ratio_median,
        'mover_G_mean': mover_G_mean,
        'stayer_G_mean': stayer_G_mean,
        'ratio_mean': ratio_mean,
        'p_mann_whitney': p_mann,
        'p_ttest': p_ttest,
        'cohens_d': cohens_d,
        'ci_95': (ci_lower, ci_upper),
        'n_movers': len(movers),
        'n_stayers': len(stayers),
    }

# ============================================================================
# SENSITIVITY ANALYSIS
# ============================================================================
def sensitivity_analysis(df_valid):
    """
    Test sensitivity of the 3.4× ratio to different definitions.
    """
    print_header("SENSITIVITY ANALYSIS")

    print_section("1. Varying Mover Threshold")
    print("  Testing different thresholds for Mover classification:")

    thresholds = [0, 0.01, 0.05, 0.10, 0.25]

    for thresh in thresholds:
        movers_t = df_valid[df_valid['R'] > thresh]
        stayers_t = df_valid[df_valid['R'] <= thresh]

        if len(movers_t) > 10 and len(stayers_t) > 10:
            m_med = movers_t['G'].median()
            s_med = stayers_t['G'].median()
            ratio = m_med / s_med if s_med != 0 else np.nan
            print(f"    R > {thresh:.2f}: Ratio = {ratio:.2f}× (n_m={len(movers_t):,}, n_s={len(stayers_t):,})")

    print_section("2. Quartile Analysis")
    df_valid['R_quartile'] = pd.qcut(df_valid['R'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

    for q in ['Q1', 'Q2', 'Q3', 'Q4']:
        q_data = df_valid[df_valid['R_quartile'] == q]
        g_med = q_data['G'].median()
        print(f"    {q} (R): G median = {g_med:.3f}×")

# ============================================================================
# CONSISTENCY CHECK WITH EXISTING STATS
# ============================================================================
def check_consistency_with_stats(results):
    """
    Check consistency with previously computed statistics.
    """
    print_header("CONSISTENCY CHECK")

    stats_file = REPO_ROOT / ".thesis_stats.json"
    if stats_file.exists():
        with open(stats_file) as f:
            saved_stats = json.load(f)

        print_section("Comparing with .thesis_stats.json")

        if 'success_rate_moved' in saved_stats:
            print(f"  Saved Mover success: {saved_stats['success_rate_moved']}%")
        if 'success_rate_stayed' in saved_stats:
            print(f"  Saved Stayer success: {saved_stats['success_rate_stayed']}%")
        if 'movement_advantage' in saved_stats:
            print(f"  Saved Movement Advantage: {saved_stats['movement_advantage']}×")
    else:
        print("  No .thesis_stats.json found")

# ============================================================================
# MAIN
# ============================================================================
def compare_mover_definitions(df):
    """
    Compare different Mover definitions to understand discrepancy.
    """
    print_header("MOVER DEFINITION COMPARISON")

    # Filter to valid G values
    df_valid = df[df['G'].notna()].copy()

    # Definition 1: 'moved' column (original from dataset)
    if 'moved' in df_valid.columns:
        print_section("1. 'moved' column (original threshold)")
        movers_orig = df_valid[df_valid['moved'] == True]
        stayers_orig = df_valid[df_valid['moved'] == False]

        print(f"  Movers: {len(movers_orig):,}")
        print(f"  Stayers: {len(stayers_orig):,}")

        if 'L' in df_valid.columns:
            m_success = movers_orig['L'].mean() * 100
            s_success = stayers_orig['L'].mean() * 100
            ratio = m_success / s_success if s_success > 0 else np.nan
            print(f"  Mover success rate: {m_success:.1f}%")
            print(f"  Stayer success rate: {s_success:.1f}%")
            print(f"  Mover Advantage: {ratio:.2f}×")

        # G-based ratio
        m_g = movers_orig['G'].median()
        s_g = stayers_orig['G'].median()
        print(f"  Mover G median: {m_g:.3f}")
        print(f"  Stayer G median: {s_g:.3f}")

    # Definition 2: R > 0 (any movement)
    if 'M' in df_valid.columns:
        print_section("2. R > 0 (any movement)")
        df_valid['R'] = df_valid['M']
        movers_r0 = df_valid[df_valid['R'] > 0]
        stayers_r0 = df_valid[df_valid['R'] == 0]

        print(f"  Movers: {len(movers_r0):,}")
        print(f"  Stayers: {len(stayers_r0):,}")

        if 'L' in df_valid.columns:
            m_success = movers_r0['L'].mean() * 100
            s_success = stayers_r0['L'].mean() * 100
            ratio = m_success / s_success if s_success > 0 else np.nan
            print(f"  Mover success rate: {m_success:.1f}%")
            print(f"  Stayer success rate: {s_success:.1f}%")
            print(f"  Mover Advantage: {ratio:.2f}×")

    # Definition 3: R > median(R)
    if 'M' in df_valid.columns:
        print_section("3. R > median(R) (above-median movement)")
        median_r = df_valid['R'].median()
        movers_med = df_valid[df_valid['R'] > median_r]
        stayers_med = df_valid[df_valid['R'] <= median_r]

        print(f"  Threshold: R > {median_r:.3f}")
        print(f"  Movers: {len(movers_med):,}")
        print(f"  Stayers: {len(stayers_med):,}")

        if 'L' in df_valid.columns:
            m_success = movers_med['L'].mean() * 100
            s_success = stayers_med['L'].mean() * 100
            ratio = m_success / s_success if s_success > 0 else np.nan
            print(f"  Mover success rate: {m_success:.1f}%")
            print(f"  Stayer success rate: {s_success:.1f}%")
            print(f"  Mover Advantage: {ratio:.2f}×")

    # Definition 4: Top 25% movers vs Bottom 25%
    print_section("4. Top 25% vs Bottom 25% (quartile extremes)")
    q25 = df_valid['M'].quantile(0.25)
    q75 = df_valid['M'].quantile(0.75)
    top_movers = df_valid[df_valid['M'] >= q75]
    bottom_stayers = df_valid[df_valid['M'] <= q25]

    print(f"  Top 25% (M >= {q75:.3f}): {len(top_movers):,}")
    print(f"  Bottom 25% (M <= {q25:.3f}): {len(bottom_stayers):,}")

    if 'L' in df_valid.columns:
        m_success = top_movers['L'].mean() * 100
        s_success = bottom_stayers['L'].mean() * 100
        ratio = m_success / s_success if s_success > 0 else np.nan
        print(f"  Top 25% success rate: {m_success:.1f}%")
        print(f"  Bottom 25% success rate: {s_success:.1f}%")
        print(f"  Advantage: {ratio:.2f}×")


def main():
    print_header("3.4× MOVER ADVANTAGE - RIGOROUS VERIFICATION")
    print("This script verifies the most critical figure in the thesis:")
    print("The funding growth multiple ratio between Movers and Stayers")

    # Load data
    df = load_data()

    # Verify G definition
    df = verify_G_definition(df)

    # FIRST: Compare different mover definitions
    compare_mover_definitions(df)

    # Classify Movers/Stayers
    df_valid, movers, stayers = classify_movers_stayers(df)

    if movers is None or stayers is None:
        print("\nERROR: Could not classify Movers/Stayers")
        return

    # PRIMARY VERIFICATION
    results = verify_3_4x_ratio(df_valid, movers, stayers)

    # Sensitivity analysis
    sensitivity_analysis(df_valid)

    # Consistency check
    check_consistency_with_stats(results)

    # =========================================================================
    # FINAL VERDICT
    # =========================================================================
    print_header("FINAL VERDICT")

    ratio = results['ratio_median']
    ci_lower, ci_upper = results['ci_95']
    p_value = results['p_mann_whitney']

    print(f"\n  Computed Mover/Stayer Ratio: {ratio:.2f}×")
    print(f"  95% Confidence Interval: [{ci_lower:.2f}, {ci_upper:.2f}]×")
    print(f"  Statistical Significance: p = {p_value:.2e}")

    # Check if 3.4× is within CI
    target = 3.4
    if ci_lower <= target <= ci_upper:
        print(f"\n  ✓ TARGET (3.4×) IS WITHIN 95% CI")
    elif ratio > target:
        print(f"\n  ⚠ Computed ratio ({ratio:.2f}×) is HIGHER than target (3.4×)")
    else:
        print(f"\n  ⚠ Computed ratio ({ratio:.2f}×) is LOWER than target (3.4×)")

    # Statistical significance
    if p_value < 0.001:
        print("  ✓ HIGHLY SIGNIFICANT (p < 0.001)")
    elif p_value < 0.05:
        print("  ✓ SIGNIFICANT (p < 0.05)")
    else:
        print("  ✗ NOT SIGNIFICANT (p >= 0.05)")

    print("\n" + "=" * 70)
    print("  VERIFICATION COMPLETE")
    print("=" * 70)

    return results

if __name__ == '__main__':
    results = main()
