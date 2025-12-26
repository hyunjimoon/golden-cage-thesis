#!/usr/bin/env python3
"""
Generate .nc files for thesis I-M-C-T-D figures and tables.

This script creates clean, validated NetCDF files from raw/processed data.
All .nc files are saved to data/processed/ for use by chapter scripts.

Usage:
    python generate_thesis_nc_files.py [--industry transportation|quantum|all]

Output:
    data/processed/thesis_panel_v3.nc
    data/processed/vagueness_quartile_stats.nc
    data/processed/movement_stats.nc
    data/processed/correlation_panel.nc
    data/processed/mover_typology.nc
    data/processed/effectiveness_efficiency_by_type.nc
    data/processed/learning_capacity.nc
"""

import sys
from pathlib import Path
import argparse

import pandas as pd
import numpy as np
import xarray as xr
from scipy import stats
from scipy.stats import linregress, spearmanr, siegelslopes

# Paths
SCRIPT_DIR = Path(__file__).parent.resolve()
# _shared -> papers_v3 -> paper_generation -> scripts -> src -> empirics
REPO_ROOT = SCRIPT_DIR.parent.parent.parent.parent.parent  # empirics/
DATA_DIR = REPO_ROOT / 'data' / 'processed'
OUTPUT_DIR = DATA_DIR  # Save to same location


def load_and_merge_data(industry_filter=None):
    """
    Load and merge vagueness_timeseries with features_all.

    CRITICAL FILTERING:
    - Only include companies with first_financing_size (E) in 2021
    - This gives N ≈ 180,860 (matching statistics.md)
    - L = "Later Stage VC" in last_financing_deal_type (11.5% base rate)

    Args:
        industry_filter: None for all, 'transportation', 'quantum', or sector name

    Returns:
        Clean DataFrame with thesis variables
    """
    print(f"Loading data from: {DATA_DIR}")

    # Load vagueness timeseries (V over time)
    vag = pd.read_parquet(DATA_DIR / 'vagueness_timeseries.parquet')
    print(f"  vagueness_timeseries: {len(vag):,} rows, {vag['company_id'].nunique():,} companies")

    # Load features (E, G, L, sector)
    feat = pd.read_parquet(DATA_DIR / 'features_all.parquet')
    print(f"  features_all: {len(feat):,} rows")

    # Step 1: Get V_0 (2021) - ONLY companies with first_financing_size (E)
    v_2021 = vag[vag['year'] == 2021][['company_id', 'V', 'first_financing_size']].copy()
    v_2021 = v_2021.rename(columns={'V': 'V_0', 'first_financing_size': 'E'})

    # CRITICAL: Filter to companies with E (early funding)
    # This is the key filter that gives N ≈ 180,860
    v_2021 = v_2021[v_2021['E'].notna()]
    print(f"  Companies with E (first_financing_size) in 2021: {len(v_2021):,}")

    # Step 2: Get V_T (2025)
    v_2025 = vag[vag['year'] == 2025][['company_id', 'V']].copy()
    v_2025 = v_2025.rename(columns={'V': 'V_T'})

    # Merge V_0 and V_T
    panel = v_2021.merge(v_2025, on='company_id', how='inner')
    print(f"  Companies with both V_0, V_T, and E: {len(panel):,}")

    # Industry filter (applied after E filter)
    if industry_filter == 'transportation':
        trans = pd.read_parquet(DATA_DIR / 'companies_21_23-24-25_transportation.parquet')
        trans_ids = set(trans['CompanyID'].astype(str))
        panel = panel[panel['company_id'].astype(str).isin(trans_ids)]
        print(f"  Filtered to transportation: {len(panel):,} companies")
    elif industry_filter == 'quantum':
        quantum = pd.read_parquet(DATA_DIR / 'companies_21_23-24-25_quantum.parquet')
        quantum_ids = set(quantum['CompanyID'].astype(str))
        panel = panel[panel['company_id'].astype(str).isin(quantum_ids)]
        print(f"  Filtered to quantum: {len(panel):,} companies")
    elif industry_filter and industry_filter != 'all':
        # Filter by sector_fe
        sector_ids = set(feat[feat['sector_fe'] == industry_filter]['CompanyID'].astype(str))
        panel = panel[panel['company_id'].astype(str).isin(sector_ids)]
        print(f"  Filtered to {industry_filter}: {len(panel):,} companies")

    # Step 3: Calculate D (Direction) and M (Movement)
    panel['D'] = panel['V_T'] - panel['V_0']
    panel['M'] = panel['D'].abs()

    # Step 4: Classify mover_type
    def classify_mover(row):
        if row['M'] < 5:
            return 'stayer'
        elif row['D'] < -10:
            return 'zoom_in'
        elif row['D'] > 10:
            return 'zoom_out'
        else:
            return 'horizontal'

    panel['mover_type'] = panel.apply(classify_mover, axis=1)
    panel['moved'] = (panel['M'] >= 5).astype(int)

    # Step 5: Create quartiles of V_0
    try:
        panel['quartile_V0'] = pd.qcut(panel['V_0'], 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
    except ValueError:
        # For small samples with duplicate bin edges, use duplicates='drop'
        panel['quartile_V0'] = pd.qcut(panel['V_0'], 4, labels=False, duplicates='drop')
        panel['quartile_V0'] = panel['quartile_V0'].map({0: 'Q1', 1: 'Q2', 2: 'Q3', 3: 'Q4'})
        print(f"  Note: Quartile binning adjusted for small sample")

    # Step 6: Merge with features_all (deduplicated) for L and G
    feat_dedup = feat.drop_duplicates('CompanyID').copy()
    feat_dedup['CompanyID_str'] = feat_dedup['CompanyID'].astype(str)
    panel['company_id_str'] = panel['company_id'].astype(str)

    panel = panel.merge(
        feat_dedup[['CompanyID_str', 'total_raised',
                    'last_financing_deal_type', 'sector_fe']],
        left_on='company_id_str',
        right_on='CompanyID_str',
        how='left'
    )

    # Step 7: Create clean G and L variables
    #
    # G: Funding Growth Multiple (THESIS DEFINITION)
    # Formula: G = F_t / E = total_raised / first_financing_size
    #
    # This measures how much total funding a company raised relative to early funding
    # G > 1 means company raised more funding after initial round
    # G = 1 means company only had initial funding
    # G < 1 means data inconsistency (shouldn't happen)
    #
    # NOTE: PitchBook's 'GrowthRate' column is a DIFFERENT metric (employee/web growth)
    #       Do NOT use GrowthRate for thesis G variable!
    #
    panel['G'] = panel['total_raised'] / panel['E']

    # Handle edge cases
    # - If total_raised is NaN but E exists, G = 1 (only initial funding)
    # - If E = 0 (shouldn't happen due to filter), G = NaN
    panel.loc[panel['total_raised'].isna() & panel['E'].notna(), 'G'] = 1.0
    panel.loc[panel['E'] == 0, 'G'] = np.nan

    # L: Later Stage VC (STRICT definition matching 11.5% base rate)
    # This matches statistics.md exactly
    panel['L'] = panel['last_financing_deal_type'].str.contains(
        'Later Stage VC', na=False
    ).astype(int)

    # Industry
    panel['industry'] = panel['sector_fe'].fillna('Other')

    # Clean up columns
    panel = panel[['company_id', 'V_0', 'V_T', 'D', 'M', 'E', 'G', 'L',
                   'quartile_V0', 'mover_type', 'moved', 'industry']].copy()

    print(f"\n  Final panel: {len(panel):,} companies")
    print(f"  Mover types: {panel['mover_type'].value_counts().to_dict()}")
    print(f"  With G: {panel['G'].notna().sum():,} ({panel['G'].notna().mean()*100:.1f}%)")
    print(f"  Success rate (L=1): {panel['L'].mean()*100:.1f}% (target: 11.5%)")

    # Validation
    if abs(panel['L'].mean() - 0.115) > 0.01:
        print(f"  WARNING: L rate ({panel['L'].mean()*100:.1f}%) differs from expected (11.5%)")

    return panel


def save_thesis_panel(df, suffix=''):
    """Save thesis_panel_v3.nc"""
    filename = f'thesis_panel_v3{suffix}.nc'

    # Ensure consistent string types
    company_ids = df['company_id'].astype(str).values
    quartile_vals = np.array([str(x) for x in df['quartile_V0'].values])
    mover_vals = np.array([str(x) for x in df['mover_type'].values])
    industry_vals = np.array([str(x) for x in df['industry'].values])

    # Convert to xarray Dataset
    ds = xr.Dataset({
        'V_0': ('company', df['V_0'].values.astype(np.float64)),
        'V_T': ('company', df['V_T'].values.astype(np.float64)),
        'D': ('company', df['D'].values.astype(np.float64)),
        'M': ('company', df['M'].values.astype(np.float64)),
        'E': ('company', df['E'].values.astype(np.float64)),
        'G': ('company', df['G'].values.astype(np.float64)),
        'L': ('company', df['L'].values.astype(np.int32)),
        'moved': ('company', df['moved'].values.astype(np.int32)),
        'quartile_V0': ('company', quartile_vals),
        'mover_type': ('company', mover_vals),
        'industry': ('company', industry_vals),
    }, coords={
        'company': company_ids,
    }, attrs={
        'description': 'Thesis master panel with vagueness and outcome variables',
        'n_companies': len(df),
        'created': pd.Timestamp.now().isoformat(),
    })

    ds.to_netcdf(OUTPUT_DIR / filename)
    print(f"  Saved: {filename} ({len(df):,} companies)")
    return ds


def save_vagueness_quartile_stats(df, suffix=''):
    """Save vagueness_quartile_stats.nc"""
    filename = f'vagueness_quartile_stats{suffix}.nc'

    stats_list = []
    for q in ['Q1', 'Q2', 'Q3', 'Q4']:
        q_data = df[df['quartile_V0'] == q]
        stayers = q_data[q_data['moved'] == 0]
        movers = q_data[q_data['moved'] == 1]

        # Bootstrap CI for success rate
        n_boot = 1000
        if len(q_data) > 0:
            boot_means = [q_data['L'].sample(frac=1, replace=True).mean() for _ in range(n_boot)]
            ci_low = np.percentile(boot_means, 2.5)
            ci_high = np.percentile(boot_means, 97.5)
        else:
            ci_low = ci_high = np.nan

        stats_list.append({
            'quartile': q,
            'success_rate': q_data['L'].mean() if len(q_data) > 0 else np.nan,
            'success_rate_ci_low': ci_low,
            'success_rate_ci_high': ci_high,
            'n_ventures': len(q_data),
            'movement_rate': q_data['moved'].mean() if len(q_data) > 0 else np.nan,
            'success_stayers': stayers['L'].mean() if len(stayers) > 0 else np.nan,
            'success_movers': movers['L'].mean() if len(movers) > 0 else np.nan,
            'V_0_mean': q_data['V_0'].mean() if len(q_data) > 0 else np.nan,
            'V_0_min': q_data['V_0'].min() if len(q_data) > 0 else np.nan,
            'V_0_max': q_data['V_0'].max() if len(q_data) > 0 else np.nan,
        })

    stats_df = pd.DataFrame(stats_list)

    ds = xr.Dataset({
        'success_rate': ('quartile', stats_df['success_rate'].values),
        'success_rate_ci_low': ('quartile', stats_df['success_rate_ci_low'].values),
        'success_rate_ci_high': ('quartile', stats_df['success_rate_ci_high'].values),
        'n_ventures': ('quartile', stats_df['n_ventures'].values),
        'movement_rate': ('quartile', stats_df['movement_rate'].values),
        'success_stayers': ('quartile', stats_df['success_stayers'].values),
        'success_movers': ('quartile', stats_df['success_movers'].values),
        'V_0_mean': ('quartile', stats_df['V_0_mean'].values),
        'V_0_min': ('quartile', stats_df['V_0_min'].values),
        'V_0_max': ('quartile', stats_df['V_0_max'].values),
    }, coords={
        'quartile': ['Q1', 'Q2', 'Q3', 'Q4'],
    })

    ds.to_netcdf(OUTPUT_DIR / filename)
    print(f"  Saved: {filename}")
    return stats_df


def save_movement_stats(df, suffix=''):
    """Save movement_stats.nc"""
    filename = f'movement_stats{suffix}.nc'

    results = []

    # Stayers vs Movers
    for moved_val, label in [(0, 'stayed'), (1, 'moved')]:
        group = df[df['moved'] == moved_val]
        if len(group) > 0:
            n_boot = 1000
            boot_means = [group['L'].sample(frac=1, replace=True).mean() for _ in range(n_boot)]
            results.append({
                'group': label,
                'success_rate': group['L'].mean(),
                'success_rate_ci_low': np.percentile(boot_means, 2.5),
                'success_rate_ci_high': np.percentile(boot_means, 97.5),
                'n_ventures': len(group),
            })

    # By mover type
    for mtype in ['zoom_in', 'zoom_out', 'horizontal', 'stayer']:
        group = df[df['mover_type'] == mtype]
        if len(group) > 0:
            results.append({
                'group': mtype,
                'success_rate': group['L'].mean(),
                'success_rate_ci_low': np.nan,
                'success_rate_ci_high': np.nan,
                'n_ventures': len(group),
            })

    stats_df = pd.DataFrame(results)

    # Calculate relative risk and NNT
    stayed_rate = df[df['moved'] == 0]['L'].mean()
    stats_df['relative_risk'] = stats_df['success_rate'] / stayed_rate if stayed_rate > 0 else np.nan
    stats_df['nnt'] = 1 / (stats_df['success_rate'] - stayed_rate)
    stats_df['nnt'] = stats_df['nnt'].replace([np.inf, -np.inf], np.nan)

    ds = xr.Dataset({
        'success_rate': ('group', stats_df['success_rate'].values),
        'success_rate_ci_low': ('group', stats_df['success_rate_ci_low'].values),
        'success_rate_ci_high': ('group', stats_df['success_rate_ci_high'].values),
        'n_ventures': ('group', stats_df['n_ventures'].values),
        'relative_risk': ('group', stats_df['relative_risk'].values),
        'nnt': ('group', stats_df['nnt'].values),
    }, coords={
        'group': stats_df['group'].values,
    })

    ds.to_netcdf(OUTPUT_DIR / filename)
    print(f"  Saved: {filename}")
    return stats_df


def save_effectiveness_efficiency_by_type(df, suffix=''):
    """Save effectiveness_efficiency_by_type.nc with dG/dM, dM/dE, dG/dE

    METHODOLOGY UPDATE (2025-12-20):
    - G = raw multiple (total_raised / E), NOT log-transformed
    - Using Siegel's repeated medians (median regression) instead of OLS
    - Rationale: robust to outliers (G can be 83M+), focuses on "typical" company
    - Inspired by Nanda's approach and 김정하 교수님's wisdom
    """
    filename = f'effectiveness_efficiency_by_type{suffix}.nc'

    # Filter to companies with valid E and G
    analysis = df[df['E'].notna() & df['G'].notna() & (df['E'] > 0)].copy()
    analysis['log_E'] = np.log1p(analysis['E'])

    results = []

    for mtype in ['zoom_in', 'zoom_out', 'stayer', 'horizontal']:
        subset = analysis[analysis['mover_type'] == mtype]

        if len(subset) < 10:
            continue

        # dG/dE: Capital -> Growth (Total Effect) - MEDIAN REGRESSION
        try:
            slope_G_E, intercept_G_E = siegelslopes(subset['G'], subset['log_E'])
            # For comparison, also compute OLS p-value
            _, _, _, p_G_E, se_G_E = linregress(subset['log_E'], subset['G'])
        except:
            slope_G_E, p_G_E, se_G_E = np.nan, np.nan, np.nan

        # dG/dM: Movement -> Growth (Effectiveness) - MEDIAN REGRESSION
        movers = subset[subset['M'] > 0]
        if len(movers) > 10:
            try:
                slope_G_M, intercept_G_M = siegelslopes(movers['G'], movers['M'])
                # For comparison, also compute OLS p-value
                _, _, _, p_G_M, se_G_M = linregress(movers['M'], movers['G'])
            except:
                slope_G_M, p_G_M, se_G_M = np.nan, np.nan, np.nan
        else:
            slope_G_M, p_G_M, se_G_M = np.nan, np.nan, np.nan

        # dM/dE: Capital -> Movement (Efficiency) - MEDIAN REGRESSION
        try:
            slope_M_E, intercept_M_E = siegelslopes(subset['M'], subset['log_E'])
            # For comparison, also compute OLS p-value
            _, _, _, p_M_E, se_M_E = linregress(subset['log_E'], subset['M'])
        except:
            slope_M_E, p_M_E, se_M_E = np.nan, np.nan, np.nan

        # Spearman correlations
        try:
            rho_G_E, _ = spearmanr(subset['log_E'], subset['G'])
        except:
            rho_G_E = np.nan

        results.append({
            'archetype': mtype,
            'n': len(subset),
            'n_with_E_G': len(subset),

            # dG/dE (Total Effect)
            'dG_dE': slope_G_E,
            'dG_dE_se': se_G_E,
            'dG_dE_p': p_G_E,

            # dG/dM (Effectiveness)
            'dG_dM': slope_G_M,
            'dG_dM_se': se_G_M,
            'dG_dM_p': p_G_M,

            # dM/dE (Efficiency)
            'dM_dE': slope_M_E,
            'dM_dE_se': se_M_E,
            'dM_dE_p': p_M_E,

            # Correlations
            'rho_G_E': rho_G_E,

            # Success rate
            'success_rate': subset['L'].mean(),
        })

    if not results:
        print(f"  Skipped: {filename} (no valid data)")
        return None

    eff_df = pd.DataFrame(results)

    ds = xr.Dataset({
        'n': ('archetype', eff_df['n'].values),
        'dG_dE': ('archetype', eff_df['dG_dE'].values),
        'dG_dE_se': ('archetype', eff_df['dG_dE_se'].values),
        'dG_dE_p': ('archetype', eff_df['dG_dE_p'].values),
        'dG_dM': ('archetype', eff_df['dG_dM'].values),
        'dG_dM_se': ('archetype', eff_df['dG_dM_se'].values),
        'dG_dM_p': ('archetype', eff_df['dG_dM_p'].values),
        'dM_dE': ('archetype', eff_df['dM_dE'].values),
        'dM_dE_se': ('archetype', eff_df['dM_dE_se'].values),
        'dM_dE_p': ('archetype', eff_df['dM_dE_p'].values),
        'rho_G_E': ('archetype', eff_df['rho_G_E'].values),
        'success_rate': ('archetype', eff_df['success_rate'].values),
    }, coords={
        'archetype': eff_df['archetype'].values,
    }, attrs={
        'description': 'Effectiveness (dG/dM) and Efficiency (dM/dE) by archetype',
        'hypothesis_H1': 'dG/dM > 0 for all archetypes (Effectiveness)',
        'hypothesis_H2': 'dM/dE varies by D (+ for movers, - for stayers)',
    })

    ds.to_netcdf(OUTPUT_DIR / filename)
    print(f"  Saved: {filename}")

    # Print summary
    print("\n  Hypothesis Test Summary:")
    print("  " + "-" * 60)
    for _, row in eff_df.iterrows():
        sign_dG_dE = '+' if row['dG_dE'] > 0 else '-'
        sign_dM_dE = '+' if row['dM_dE'] > 0 else '-'
        sig = '***' if row['dG_dE_p'] < 0.001 else '**' if row['dG_dE_p'] < 0.01 else '*' if row['dG_dE_p'] < 0.05 else ''
        print(f"  {row['archetype']:<12} N={row['n']:>6,}  dG/dE={row['dG_dE']:>8.4f}{sig:<3}  dM/dE={row['dM_dE']:>8.4f} ({sign_dM_dE})")
    print("  " + "-" * 60)

    return eff_df


def save_learning_capacity(suffix=''):
    """Save learning_capacity.nc (theoretical, not data-dependent)"""
    filename = f'learning_capacity{suffix}.nc'

    V = np.linspace(0, 100, 101)
    mu = np.linspace(0, 1, 101)

    V_grid, mu_grid = np.meshgrid(V, mu)

    # Learning capacity = mu * (1 - mu) / (τ + 1)
    # where τ = 100 - V (precision = 100 - vagueness)
    # Therefore: capacity = mu * (1 - mu) / (101 - V)
    #
    # Interpretation:
    #   - High V (vague) → Low τ → High capacity → HARD to trap (good)
    #   - Low V (precise) → High τ → Low capacity → EASY to trap (bad)
    tau_grid = 100 - V_grid
    capacity = mu_grid * (1 - mu_grid) / (tau_grid + 1)

    ds = xr.Dataset({
        'learning_capacity': (['mu', 'V'], capacity),
        'tau': (['V'], 100 - V),  # τ = 100 - V mapping
        'trap_001': (['mu', 'V'], capacity < 0.001),
        'trap_005': (['mu', 'V'], capacity < 0.005),
        'trap_01': (['mu', 'V'], capacity < 0.01),
    }, coords={
        'V': V,
        'mu': mu,
    }, attrs={
        'description': 'Learning trap condition: mu(1-mu) < epsilon*(tau+1) where tau=100-V',
        'equation': 'capacity = mu * (1 - mu) / (tau + 1) = mu * (1 - mu) / (101 - V)',
        'tau_definition': 'tau = 100 - V (precision parameter)',
    })

    ds.to_netcdf(OUTPUT_DIR / filename)
    print(f"  Saved: {filename}")
    return ds


def main():
    parser = argparse.ArgumentParser(description='Generate thesis .nc files')
    parser.add_argument('--industry', type=str, default='all',
                        help='Industry filter: all, transportation, quantum, or sector name')
    args = parser.parse_args()

    industry = args.industry if args.industry != 'all' else None
    suffix = f'_{args.industry}' if args.industry != 'all' else ''

    print("=" * 60)
    print(f"Generating Thesis .nc Files")
    if industry:
        print(f"Industry Filter: {industry}")
    print("=" * 60)

    # Load and merge data
    df = load_and_merge_data(industry_filter=industry)

    # Generate all .nc files
    print("\nGenerating .nc files...")
    save_thesis_panel(df, suffix)
    save_vagueness_quartile_stats(df, suffix)
    save_movement_stats(df, suffix)
    save_effectiveness_efficiency_by_type(df, suffix)
    save_learning_capacity(suffix)

    print("\n" + "=" * 60)
    print(f"All .nc files saved to: {OUTPUT_DIR}")
    print("=" * 60)


if __name__ == '__main__':
    main()
