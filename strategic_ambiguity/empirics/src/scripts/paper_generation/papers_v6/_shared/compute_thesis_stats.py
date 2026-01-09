#!/usr/bin/env python3
"""
Compute and export thesis statistics from data.
NO HARD-CODING - all statistics computed from actual data.

This script generates a JSON file with all key statistics used in the thesis.
The pipeline script should read from this JSON instead of hard-coding values.

Usage:
    python compute_thesis_stats.py

Output:
    thesis_stats.json - All computed statistics
"""

import json
import numpy as np
import pandas as pd
import xarray as xr
from pathlib import Path
from scipy.stats import spearmanr, pearsonr

REPO_ROOT = Path("/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics")
DATA_DIR = REPO_ROOT / "data" / "processed"
OUTPUT_FILE = REPO_ROOT / ".thesis_stats.json"


def compute_stats():
    """Compute all thesis statistics from actual data."""
    print("=" * 60)
    print("Computing Thesis Statistics from Data")
    print("=" * 60)

    stats = {}

    # Load thesis panel
    nc_file = DATA_DIR / "thesis_panel_v3.nc"
    if not nc_file.exists():
        print(f"ERROR: {nc_file} not found")
        return None

    ds = xr.open_dataset(nc_file)

    df = pd.DataFrame({
        'company_id': ds['company'].values,
        'V_0': ds['V_0'].values,
        'V_T': ds['V_T'].values,
        'D': ds['D'].values,
        'M': ds['M'].values,
        'E': ds['E'].values,
        'G': ds['G'].values,
        'L': ds['L'].values,
        'moved': ds['moved'].values,
        'mover_type': ds['mover_type'].values,
    })
    ds.close()

    # Basic counts
    stats['N_total'] = int(len(df))
    stats['N_moved'] = int(df['moved'].sum())
    stats['N_stayed'] = stats['N_total'] - stats['N_moved']

    # Success rates
    mover_success = df[df['moved'] == True]['L'].mean()
    stayer_success = df[df['moved'] == False]['L'].mean()
    stats['success_rate_moved'] = round(float(mover_success * 100), 1)
    stats['success_rate_stayed'] = round(float(stayer_success * 100), 1)
    stats['movement_advantage'] = round(stats['success_rate_moved'] / stats['success_rate_stayed'], 1)

    # Mover type counts (3 archetypes)
    stats['N_zoom_in'] = int((df['mover_type'] == 'zoom_in').sum())
    stats['N_zoom_out'] = int((df['mover_type'] == 'zoom_out').sum())
    stats['N_stayer'] = int((df['mover_type'] == 'stayer').sum())

    # Correlations (filter valid data - remove NaN and inf)
    valid = df[df['E'].notna() & df['G'].notna() & (df['E'] > 0)].copy()
    valid['log_E'] = np.log1p(valid['E'])

    # Remove any remaining NaN/inf
    valid = valid.replace([np.inf, -np.inf], np.nan).dropna(subset=['G', 'M', 'V_0', 'L', 'log_E'])

    print(f"  Valid samples for correlations: {len(valid):,}")

    # rho(G, E) - Funding Paradox
    rho_G_E, p_G_E = spearmanr(valid['G'], valid['log_E'])
    stats['rho_G_E'] = round(float(rho_G_E), 3)
    stats['rho_G_E_p'] = float(p_G_E)
    stats['rho_G_E_sig'] = "***" if p_G_E < 0.001 else "**" if p_G_E < 0.01 else "*" if p_G_E < 0.05 else "ns"

    # rho(M, E) - Fund2Cage
    rho_M_E, p_M_E = spearmanr(valid['M'], valid['log_E'])
    stats['rho_M_E'] = round(float(rho_M_E), 3)
    stats['rho_M_E_p'] = float(p_M_E)
    stats['rho_M_E_sig'] = "***" if p_M_E < 0.001 else "**" if p_M_E < 0.01 else "*" if p_M_E < 0.05 else "ns"

    # rho(G, M) - Movement -> Growth
    rho_G_M, p_G_M = spearmanr(valid['G'], valid['M'])
    stats['rho_G_M'] = round(float(rho_G_M), 3)
    stats['rho_G_M_p'] = float(p_G_M)
    stats['rho_G_M_sig'] = "***" if p_G_M < 0.001 else "**" if p_G_M < 0.01 else "*" if p_G_M < 0.05 else "ns"

    # rho(V, L) - Vagueness -> Success
    rho_V_L, p_V_L = spearmanr(valid['V_0'], valid['L'])
    stats['rho_V_L'] = round(float(rho_V_L), 3)
    stats['rho_V_L_p'] = float(p_V_L)
    stats['rho_V_L_sig'] = "***" if p_V_L < 0.001 else "**" if p_V_L < 0.01 else "*" if p_V_L < 0.05 else "ns"

    # Overall success rate
    stats['success_rate_overall'] = round(float(df['L'].mean() * 100), 1)

    # Print summary
    print(f"\n  N = {stats['N_total']:,}")
    print(f"  Moved: {stats['N_moved']:,} ({stats['success_rate_moved']:.1f}% success)")
    print(f"  Stayed: {stats['N_stayed']:,} ({stats['success_rate_stayed']:.1f}% success)")
    print(f"  Movement Advantage: {stats['movement_advantage']}×")
    print(f"\n  Correlations:")
    print(f"    ρ(G, E) = {stats['rho_G_E']:+.3f}{stats['rho_G_E_sig']} (Funding Paradox)")
    print(f"    ρ(M, E) = {stats['rho_M_E']:+.3f}{stats['rho_M_E_sig']} (Fund2Cage)")
    print(f"    ρ(G, M) = {stats['rho_G_M']:+.3f}{stats['rho_G_M_sig']} (Movement→Growth)")
    print(f"    ρ(V, L) = {stats['rho_V_L']:+.3f}{stats['rho_V_L_sig']} (Vagueness→Success)")

    # Save to JSON
    OUTPUT_FILE.write_text(json.dumps(stats, indent=2))
    print(f"\n  Saved to: {OUTPUT_FILE}")

    return stats


if __name__ == '__main__':
    compute_stats()
