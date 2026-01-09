#!/usr/bin/env python3
"""
01_raw_to_processed.py - Data Pipeline for Thesis Analysis
==========================================================

This script creates thesis_panel_v3.nc from raw data with proper variable definitions.

FIXES APPLIED:
1. G: Use ONLY GrowthRate (continuous), NOT growth (binary 0/1)
2. E: first_financing_size from vagueness_timeseries (2021 values)
3. L: "Later Stage VC" in last_financing_deal_type (11.5% base rate)

Data Flow:
    raw/Company*.dat → processed/features_all.parquet
    ↓
    processed/vagueness_timeseries.parquet (V over time, E from 2021)
    ↓
    processed/thesis_panel_v3.nc (final analysis panel)

Usage:
    python 01_raw_to_processed.py [--validate-only] [--industry transportation|quantum]

Output:
    data/processed/thesis_panel_v3.nc (N≈180,000 or N≈74,000 with G filter)
"""

import sys
from pathlib import Path
import argparse

import pandas as pd
import numpy as np
import xarray as xr
from scipy.stats import spearmanr

# Paths
SCRIPT_DIR = Path(__file__).parent.resolve()
REPO_ROOT = SCRIPT_DIR.parent.parent.parent.parent.parent  # empirics/
DATA_RAW = REPO_ROOT / 'data' / 'raw'
DATA_PROC = REPO_ROOT / 'data' / 'processed'


def load_source_data():
    """Load source files with diagnostics."""
    print("=" * 60)
    print("STEP 1: Load Source Data")
    print("=" * 60)

    # 1. Vagueness timeseries (V, E from 2021)
    vag_path = DATA_PROC / 'vagueness_timeseries.parquet'
    print(f"\n[1a] Loading {vag_path.name}...")
    vag = pd.read_parquet(vag_path)
    print(f"     Rows: {len(vag):,}")
    print(f"     Companies: {vag['company_id'].nunique():,}")
    print(f"     Years: {sorted(vag['year'].unique())}")
    print(f"     Columns: {vag.columns.tolist()}")

    # 2. Features (G, L, sector)
    feat_path = DATA_PROC / 'features_all.parquet'
    print(f"\n[1b] Loading {feat_path.name}...")
    feat = pd.read_parquet(feat_path)
    print(f"     Rows: {len(feat):,}")
    print(f"     Companies: {feat['CompanyID'].nunique():,}")

    # Diagnose G columns
    print("\n     G variable diagnostic:")
    print(f"       growth (BINARY!): non-null={feat['growth'].notna().sum():,}, zeros={(feat['growth']==0).sum():,}")
    print(f"       GrowthRate (continuous): non-null={feat['GrowthRate'].notna().sum():,}")

    return vag, feat


def build_panel(vag, feat, require_G=True, industry_filter=None):
    """
    Build analysis panel with CORRECTED variable definitions.

    Args:
        vag: Vagueness timeseries DataFrame
        feat: Features DataFrame
        require_G: If True, only include companies with real GrowthRate (N≈74,000)
                   If False, include all companies with E (N≈180,000)
        industry_filter: 'transportation', 'quantum', or None

    Returns:
        Clean panel DataFrame
    """
    print("\n" + "=" * 60)
    print("STEP 2: Build Analysis Panel")
    print("=" * 60)

    # Step 2a: Extract V_0 (2021) with E
    print("\n[2a] Extract V_0 and E from 2021...")
    v_2021 = vag[vag['year'] == 2021][['company_id', 'V', 'first_financing_size']].copy()
    v_2021 = v_2021.rename(columns={'V': 'V_0', 'first_financing_size': 'E'})
    print(f"     Companies in 2021: {len(v_2021):,}")

    # Filter for companies with E (early funding)
    v_2021 = v_2021[v_2021['E'].notna()]
    print(f"     Companies with E: {len(v_2021):,}")

    # Step 2b: Extract V_T (2025)
    print("\n[2b] Extract V_T from 2025...")
    v_2025 = vag[vag['year'] == 2025][['company_id', 'V']].copy()
    v_2025 = v_2025.rename(columns={'V': 'V_T'})
    print(f"     Companies in 2025: {len(v_2025):,}")

    # Step 2c: Merge V_0 and V_T
    print("\n[2c] Merge V_0 and V_T...")
    panel = v_2021.merge(v_2025, on='company_id', how='inner')
    print(f"     Companies with V_0, V_T, E: {len(panel):,}")

    # Step 2d: Compute D and M
    print("\n[2d] Compute D (direction) and M (movement)...")
    panel['D'] = panel['V_T'] - panel['V_0']
    panel['M'] = panel['D'].abs()

    # Step 2e: Classify mover types (3 archetypes: stayer, zoom_in, zoom_out)
    # Note: horizontal (M>=5 but |D|<=10) merged into stayer
    def classify_mover(row):
        if row['D'] < -10 and row['M'] >= 5:
            return 'zoom_in'
        elif row['D'] > 10 and row['M'] >= 5:
            return 'zoom_out'
        else:
            return 'stayer'  # includes M<5 and horizontal movers

    panel['mover_type'] = panel.apply(classify_mover, axis=1)
    panel['moved'] = (panel['mover_type'] != 'stayer').astype(int)

    print("     Mover types:")
    for mt, count in panel['mover_type'].value_counts().items():
        print(f"       {mt}: {count:,} ({count/len(panel)*100:.1f}%)")

    # Step 2f: Create V_0 quartiles
    try:
        panel['quartile_V0'] = pd.qcut(panel['V_0'], 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
    except ValueError:
        panel['quartile_V0'] = pd.qcut(panel['V_0'], 4, labels=False, duplicates='drop')
        panel['quartile_V0'] = panel['quartile_V0'].map({0: 'Q1', 1: 'Q2', 2: 'Q3', 3: 'Q4'})

    # Step 2g: Merge with features for G and L
    print("\n[2g] Merge with features for G and L...")

    # Deduplicate features
    feat_dedup = feat.drop_duplicates('CompanyID').copy()

    # CRITICAL FIX: Only use GrowthRate (continuous), NOT growth (binary)
    if require_G:
        feat_dedup = feat_dedup[feat_dedup['GrowthRate'].notna()]
        print(f"     Companies with real GrowthRate: {len(feat_dedup):,}")

    # Prepare for merge
    feat_dedup['CompanyID_str'] = feat_dedup['CompanyID'].astype(str)
    panel['company_id_str'] = panel['company_id'].astype(str)

    # Merge
    merge_cols = ['CompanyID_str', 'GrowthRate', 'last_financing_deal_type', 'sector_fe']
    panel = panel.merge(
        feat_dedup[merge_cols],
        left_on='company_id_str',
        right_on='CompanyID_str',
        how='inner' if require_G else 'left'
    )

    print(f"     After merge: {len(panel):,}")

    # Step 2h: Create clean G and L
    print("\n[2h] Create G (growth) and L (success)...")

    # G: ONLY GrowthRate (no fallback to binary growth!)
    panel['G'] = panel['GrowthRate']

    # L: Later Stage VC (strict definition for 11.5% base rate)
    panel['L'] = panel['last_financing_deal_type'].str.contains(
        'Later Stage VC', na=False
    ).astype(int)

    print(f"     G non-null: {panel['G'].notna().sum():,}")
    print(f"     G mean: {panel['G'].mean():.2f}")
    print(f"     L base rate: {panel['L'].mean()*100:.1f}%")

    # Industry filter
    if industry_filter == 'transportation':
        trans_path = DATA_PROC / 'companies_21_23-24-25_transportation.parquet'
        if trans_path.exists():
            trans = pd.read_parquet(trans_path)
            trans_ids = set(trans['CompanyID'].astype(str))
            panel = panel[panel['company_id_str'].isin(trans_ids)]
            print(f"\n     Filtered to transportation: {len(panel):,}")
    elif industry_filter == 'quantum':
        quant_path = DATA_PROC / 'companies_21_23-24-25_quantum.parquet'
        if quant_path.exists():
            quant = pd.read_parquet(quant_path)
            quant_ids = set(quant['CompanyID'].astype(str))
            panel = panel[panel['company_id_str'].isin(quant_ids)]
            print(f"\n     Filtered to quantum: {len(panel):,}")

    # Industry label
    panel['industry'] = panel['sector_fe'].fillna('Other')

    return panel


def validate_panel(panel):
    """Validate panel against expected statistics."""
    print("\n" + "=" * 60)
    print("STEP 3: Validation")
    print("=" * 60)

    issues = []

    # Check N
    n = len(panel)
    print(f"\n[3a] Sample size: N = {n:,}")

    # Check L rate
    l_rate = panel['L'].mean() * 100
    print(f"[3b] L base rate: {l_rate:.1f}%")
    if abs(l_rate - 11.5) > 2:
        issues.append(f"L rate {l_rate:.1f}% differs from expected 11.5%")

    # Check G distribution
    g_nonzero = (panel['G'] != 0).mean() * 100
    print(f"[3c] G non-zero: {g_nonzero:.1f}%")
    if g_nonzero < 50:
        issues.append(f"G has {100-g_nonzero:.1f}% zeros - possible binary corruption")

    # Check correlations
    print("\n[3d] Key correlations:")

    valid = panel.dropna(subset=['G', 'M', 'E'])
    if len(valid) > 100:
        rho_GE, p_GE = spearmanr(valid['G'], np.log1p(valid['E']))
        rho_ME, p_ME = spearmanr(valid['M'], np.log1p(valid['E']))
        rho_GM, p_GM = spearmanr(valid['G'], valid['M'])

        print(f"     ρ(G, log(E)) = {rho_GE:+.4f} (p={p_GE:.2e})")
        print(f"     ρ(M, log(E)) = {rho_ME:+.4f} (p={p_ME:.2e})")
        print(f"     ρ(G, M)      = {rho_GM:+.4f} (p={p_GM:.2e})")

    # Summary
    if issues:
        print("\n⚠️  VALIDATION ISSUES:")
        for issue in issues:
            print(f"     - {issue}")
    else:
        print("\n✅ All validations passed!")

    return len(issues) == 0


def save_to_netcdf(panel, output_path):
    """Save panel to NetCDF format."""
    print("\n" + "=" * 60)
    print("STEP 4: Save to NetCDF")
    print("=" * 60)

    # Prepare data arrays
    n = len(panel)

    ds = xr.Dataset({
        'V_0': ('company', panel['V_0'].values),
        'V_T': ('company', panel['V_T'].values),
        'D': ('company', panel['D'].values),
        'M': ('company', panel['M'].values),
        'E': ('company', panel['E'].values),
        'G': ('company', panel['G'].fillna(np.nan).values),
        'L': ('company', panel['L'].values),
        'moved': ('company', panel['moved'].values),
        'mover_type': ('company', np.array([str(x) for x in panel['mover_type'].values])),
        'quartile_V0': ('company', np.array([str(x) for x in panel['quartile_V0'].values])),
    }, coords={
        'company': panel['company_id'].values,
    })

    # Add attributes
    ds.attrs['created'] = str(pd.Timestamp.now())
    ds.attrs['n_companies'] = n
    ds.attrs['l_base_rate'] = float(panel['L'].mean())
    ds.attrs['g_source'] = 'GrowthRate only (continuous)'
    ds.attrs['e_source'] = 'first_financing_size (2021)'
    ds.attrs['l_definition'] = 'Later Stage VC in last_financing_deal_type'

    # Variable attributes
    ds['V_0'].attrs['description'] = 'Initial vagueness (2021)'
    ds['V_T'].attrs['description'] = 'Final vagueness (2025)'
    ds['D'].attrs['description'] = 'Direction = V_T - V_0'
    ds['M'].attrs['description'] = 'Movement = |D|'
    ds['E'].attrs['description'] = 'Early funding (M USD)'
    ds['G'].attrs['description'] = 'Growth rate (continuous, from GrowthRate)'
    ds['L'].attrs['description'] = 'Success = Later Stage VC (11.5% base)'
    ds['moved'].attrs['description'] = 'Binary: moved (M >= 5)'
    ds['mover_type'].attrs['description'] = 'zoom_in/zoom_out/stayer (3 archetypes)'
    ds['quartile_V0'].attrs['description'] = 'Quartile of initial V'

    # Save
    ds.to_netcdf(output_path)
    print(f"\n✅ Saved: {output_path}")
    print(f"   N = {n:,} companies")
    print(f"   L = {panel['L'].mean()*100:.1f}%")

    return ds


def main():
    parser = argparse.ArgumentParser(description='Build thesis analysis panel')
    parser.add_argument('--validate-only', action='store_true',
                        help='Only validate existing data')
    parser.add_argument('--industry', type=str, default=None,
                        choices=['transportation', 'quantum'],
                        help='Filter to specific industry')
    parser.add_argument('--include-missing-G', action='store_true',
                        help='Include companies without GrowthRate (larger N but G may be NaN)')
    args = parser.parse_args()

    print("=" * 60)
    print("THESIS DATA PIPELINE")
    print("=" * 60)
    print(f"Date: {pd.Timestamp.now()}")
    print(f"Industry filter: {args.industry or 'all'}")
    print(f"Require G: {not args.include_missing_G}")
    print()

    # Load data
    vag, feat = load_source_data()

    # Build panel
    panel = build_panel(
        vag, feat,
        require_G=not args.include_missing_G,
        industry_filter=args.industry
    )

    # Validate
    is_valid = validate_panel(panel)

    if args.validate_only:
        print("\n[Validate-only mode - not saving]")
        return

    # Save
    if args.industry:
        output_path = DATA_PROC / f'thesis_panel_v3_{args.industry}.nc'
    else:
        suffix = '' if args.include_missing_G else '_strict'
        output_path = DATA_PROC / f'thesis_panel_v3{suffix}.nc'

    save_to_netcdf(panel, output_path)

    print("\n" + "=" * 60)
    print("PIPELINE COMPLETE")
    print("=" * 60)


if __name__ == '__main__':
    main()
