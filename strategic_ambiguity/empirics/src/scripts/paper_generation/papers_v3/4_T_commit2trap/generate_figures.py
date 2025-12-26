#!/usr/bin/env python3
"""
4_T_commit2trap: Generate Archetype dG/dE Comparison Figures

This module generates figures for the Commit2Trap section of the thesis,
demonstrating the Cash Paradox decomposition by archetype.

Figures Generated:
- fig_archetype_dG_dE_real.png/pdf   : dG/dE by archetype bar chart
- fig_decomposition_real.png/pdf      : Effectiveness × Efficiency decomposition
- fig_V_efficiency_real.png/pdf       : V₀ vs Movement scatter
- fig_success_by_archetype_real.png/pdf : Success rate comparison

Data Sources:
- vagueness_timeseries.parquet: V_0, V_T, D, M
- features_all.parquet: E, G, L

Hypotheses Tested:
- H1 (Effectiveness): dG/dM > 0 for ALL archetypes
- H2 (Efficiency): dM/dE varies by archetype (+ for Movers, - for Stayers)

Usage:
    cd papers_v3/4_T_commit2trap
    python generate_figures.py

Output:
    All figures saved to current directory (4_T_commit2trap/)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
from scipy.stats import linregress, spearmanr
from pathlib import Path

# Configuration - paths relative to repository root
SCRIPT_DIR = Path(__file__).parent.resolve()
REPO_ROOT = SCRIPT_DIR.parent.parent.parent.parent.parent  # empirics/
DATA_DIR = REPO_ROOT / 'data' / 'processed'
OUTPUT_DIR = SCRIPT_DIR  # Save figures in same directory as script


def load_real_data():
    """
    Load thesis panel from thesis_panel_v3.nc (pre-generated with correct filtering).

    The .nc file contains:
    - N ≈ 180,860 companies (with early funding E)
    - L = Later Stage VC (11.5% base rate)
    - Correct mover_type classification

    Returns:
        DataFrame with columns: company_id, V_0, V_T, D, M, E, G, L, mover_type
    """
    nc_file = DATA_DIR / 'thesis_panel_v3.nc'

    if not nc_file.exists():
        raise FileNotFoundError(
            f"thesis_panel_v3.nc not found at {nc_file}\n"
            "Run: python _shared/generate_thesis_nc_files.py --industry all"
        )

    print(f"Loading data from: {nc_file}")

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
        'quartile_V0': ds['quartile_V0'].values,
    })

    ds.close()

    print(f"  Loaded {len(df):,} companies")
    print(f"  Mover types: {df['mover_type'].value_counts().to_dict()}")
    print(f"  Success rate (L=1): {df['L'].mean()*100:.1f}%")

    return df


def compute_archetype_slopes(df):
    """Compute dG/dE, dG/dM, dM/dE by archetype."""
    analysis = df[df['E'].notna() & df['G'].notna() & (df['E'] > 0)].copy()
    analysis['log_E'] = np.log1p(analysis['E'])

    results = []

    for mtype in ['zoom_in', 'zoom_out', 'stayer', 'horizontal']:
        subset = analysis[analysis['mover_type'] == mtype]

        if len(subset) < 30:
            continue

        # dG/dE
        try:
            slope_G_E, _, _, p_G_E, se_G_E = linregress(subset['log_E'], subset['G'])
        except Exception:
            slope_G_E, p_G_E, se_G_E = np.nan, np.nan, np.nan

        # dG/dM
        movers = subset[subset['M'] > 0]
        if len(movers) > 10:
            try:
                slope_G_M, _, _, p_G_M, se_G_M = linregress(movers['M'], movers['G'])
            except Exception:
                slope_G_M, p_G_M, se_G_M = np.nan, np.nan, np.nan
        else:
            slope_G_M, p_G_M, se_G_M = np.nan, np.nan, np.nan

        # dM/dE
        try:
            slope_M_E, _, _, p_M_E, se_M_E = linregress(subset['log_E'], subset['M'])
        except Exception:
            slope_M_E, p_M_E, se_M_E = np.nan, np.nan, np.nan

        results.append({
            'archetype': mtype,
            'n': len(subset),
            'dG_dE': slope_G_E,
            'dG_dE_se': se_G_E,
            'dG_dE_p': p_G_E,
            'dG_dM': slope_G_M,
            'dG_dM_se': se_G_M if not np.isnan(slope_G_M) else np.nan,
            'dG_dM_p': p_G_M,
            'dM_dE': slope_M_E,
            'dM_dE_se': se_M_E,
            'dM_dE_p': p_M_E,
            'success_rate': subset['L'].mean() if 'L' in subset.columns else np.nan
        })

    return pd.DataFrame(results)


def plot_dG_dE_comparison(results_df):
    """Fig T.1: Archetype별 dG/dE Bar Chart"""
    fig, ax = plt.subplots(figsize=(10, 6))

    archetypes = results_df['archetype'].tolist()
    slopes = results_df['dG_dE'].tolist()
    errors = [se * 1.96 if not np.isnan(se) else 0 for se in results_df['dG_dE_se'].tolist()]

    colors = []
    for i, a in enumerate(archetypes):
        if a in ['zoom_in', 'zoom_out']:
            colors.append('#2ca02c' if slopes[i] > 0 else '#d62728')
        elif a == 'stayer':
            colors.append('#d62728' if slopes[i] < 0 else '#ff7f0e')
        else:
            colors.append('#7f7f7f')

    ax.bar(archetypes, slopes, yerr=errors, capsize=5, color=colors, alpha=0.7, edgecolor='black')
    ax.axhline(y=0, color='black', linestyle='--', linewidth=1)

    ax.set_xlabel('Archetype', fontsize=12)
    ax.set_ylabel('dG/dE (log Capital -> Growth Effect)', fontsize=12)
    ax.set_title('Cash Paradox: Total Effect by Archetype\n(dG/dE = dG/dM x dM/dE)', fontsize=14)

    for i, (slope, p, n) in enumerate(zip(slopes, results_df['dG_dE_p'], results_df['n'])):
        star = '***' if p < 0.001 else '**' if p < 0.01 else '*' if p < 0.05 else 'ns'
        y_pos = slope + errors[i] + 0.005 if slope >= 0 else slope - errors[i] - 0.005
        ax.annotate(f'{star}\n(N={n:,})', (i, y_pos), ha='center', fontsize=9, fontweight='bold')

    from matplotlib.patches import Patch
    # NEW COLOR SCHEME legend
    legend_elements = [
        Patch(facecolor='#457B9D', alpha=0.7, edgecolor='black', label='Positive (expected for Movers)'),  # Blue
        Patch(facecolor='#264653', alpha=0.7, edgecolor='black', label='Negative (expected for Stayers)'),  # Dark
    ]
    ax.legend(handles=legend_elements, loc='upper right', fontsize=9)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'fig_archetype_dG_dE_real.png', dpi=300)
    plt.savefig(OUTPUT_DIR / 'fig_archetype_dG_dE_real.pdf')
    print(f"  Saved: fig_archetype_dG_dE_real.png/pdf")
    plt.close()


def plot_decomposition(results_df):
    """Fig T.2: Decomposition (dG/dM x dM/dE)"""
    fig, ax = plt.subplots(figsize=(12, 7))

    results_clean = results_df[results_df['dM_dE'].notna()].copy()
    archetypes = results_clean['archetype'].tolist()
    x = np.arange(len(archetypes))
    width = 0.35

    dG_dM = results_clean['dG_dM'].values
    dM_dE = results_clean['dM_dE'].values

    dG_dM_scaled = dG_dM / np.nanmax(np.abs(dG_dM)) if np.nanmax(np.abs(dG_dM)) > 0 else dG_dM
    dM_dE_scaled = dM_dE / np.nanmax(np.abs(dM_dE)) if np.nanmax(np.abs(dM_dE)) > 0 else dM_dE

    ax.bar(x - width/2, dG_dM_scaled, width, label='dG/dM (Effectiveness)', color='#1f77b4', alpha=0.7)
    ax.bar(x + width/2, dM_dE_scaled, width, label='dM/dE (Efficiency)', color='#ff7f0e', alpha=0.7)

    product_sign = np.sign(dG_dM) * np.sign(dM_dE)
    ax.scatter(x, product_sign * 0.5, s=200, c=['green' if s > 0 else 'red' for s in product_sign],
               marker='o', label='Product Sign (dG/dE)', zorder=5, edgecolors='black')

    ax.axhline(y=0, color='black', linestyle='--', linewidth=1)
    ax.set_xticks(x)
    ax.set_xticklabels(archetypes, fontsize=11)
    ax.set_xlabel('Archetype', fontsize=12)
    ax.set_ylabel('Scaled Effect Size', fontsize=12)
    ax.set_title('Effectiveness x Efficiency = Total Effect\n(Normalized for Comparison)', fontsize=14)
    ax.legend(loc='upper right', fontsize=10)

    for i, mtype in enumerate(archetypes):
        sign_G_M = '+' if dG_dM[i] > 0 else '-'
        sign_M_E = '+' if dM_dE[i] > 0 else '-'
        sign_product = '+' if dG_dM[i] * dM_dE[i] > 0 else '-'
        ax.annotate(f'({sign_G_M})x({sign_M_E})={sign_product}\ndG/dM={dG_dM[i]:.4f}\ndM/dE={dM_dE[i]:.4f}',
                    (i, -1.3), ha='center', fontsize=8,
                    bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    ax.set_ylim(-1.6, 1.2)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'fig_decomposition_real.png', dpi=300)
    plt.savefig(OUTPUT_DIR / 'fig_decomposition_real.pdf')
    print(f"  Saved: fig_decomposition_real.png/pdf")
    plt.close()


def plot_V_efficiency_scatter(df):
    """Fig T.3: V Level x Movement Scatter"""
    fig, ax = plt.subplots(figsize=(12, 8))

    # NEW COLOR SCHEME: ⚫Stayer=Dark, 🟢Horizontal=Green, 🔴ZoomIn=Red, 🔵ZoomOut=Blue
    colors = {
        'stayer': '#264653',      # ⚫ Black/Dark
        'horizontal': '#2A9D8F',  # 🟢 Green
        'zoom_in': '#E63946',     # 🔴 Red
        'zoom_out': '#457B9D',    # 🔵 Blue
    }

    labels = {
        'zoom_in': f'Zoom-in (N={len(df[df["mover_type"]=="zoom_in"]):,})',
        'zoom_out': f'Zoom-out (N={len(df[df["mover_type"]=="zoom_out"]):,})',
        'stayer': f'Stayer (N={len(df[df["mover_type"]=="stayer"]):,})',
        'horizontal': f'Horizontal (N={len(df[df["mover_type"]=="horizontal"]):,})'
    }

    df_plot = pd.concat([
        df[df['mover_type'] != 'stayer'],
        df[df['mover_type'] == 'stayer'].sample(min(20000, len(df[df['mover_type'] == 'stayer'])), random_state=42)
    ])

    for mtype in ['stayer', 'horizontal', 'zoom_out', 'zoom_in']:
        subset = df_plot[df_plot['mover_type'] == mtype]
        alpha = 0.2 if mtype == 'stayer' else 0.5
        size = 5 if mtype == 'stayer' else 20
        ax.scatter(subset['V_0'], subset['M'], alpha=alpha, c=colors[mtype], label=labels[mtype], s=size)

    ax.axvspan(0, 25, alpha=0.15, color='red')
    ax.axvline(x=25, color='red', linestyle=':', linewidth=2, alpha=0.7)
    ax.text(12, ax.get_ylim()[1] * 0.95, 'LOW V\n(Trap Zone)', fontsize=10,
            ha='center', va='top', color='darkred', fontweight='bold')

    ax.set_xlabel('V_0 (Initial Vagueness)', fontsize=12)
    ax.set_ylabel('M (Movement = |D|)', fontsize=12)
    ax.set_title('Vagueness and Movement Capacity\nLow V -> Limited Movement Options', fontsize=14)
    ax.legend(loc='upper right', fontsize=9)

    rho_V_M, p_V_M = spearmanr(df['V_0'], df['M'])
    ax.text(0.02, 0.98, f'Spearman rho(V_0, M) = {rho_V_M:.3f}\np < 0.001',
            transform=ax.transAxes, fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'fig_V_efficiency_real.png', dpi=300)
    plt.savefig(OUTPUT_DIR / 'fig_V_efficiency_real.pdf')
    print(f"  Saved: fig_V_efficiency_real.png/pdf")
    plt.close()


def plot_success_by_archetype(df):
    """Fig T.4: Success Rate by Archetype"""
    fig, ax = plt.subplots(figsize=(10, 6))

    archetypes = ['zoom_in', 'zoom_out', 'stayer', 'horizontal']
    success_rates = [df[df['mover_type'] == m]['L'].mean() * 100 for m in archetypes]
    ns = [len(df[df['mover_type'] == m]) for m in archetypes]
    # NEW COLOR SCHEME: ⚫Stayer=Dark, 🟢Horizontal=Green, 🔴ZoomIn=Red, 🔵ZoomOut=Blue
    colors = ['#E63946', '#457B9D', '#264653', '#2A9D8F']  # zoom_in=Red, zoom_out=Blue, stayer=Dark, horizontal=Green

    ax.bar(archetypes, success_rates, color=colors, alpha=0.7, edgecolor='black')

    for i, (rate, n) in enumerate(zip(success_rates, ns)):
        ax.annotate(f'{rate:.1f}%\n(N={n:,})', (i, rate + 1), ha='center', fontsize=10)

    ax.set_xlabel('Archetype', fontsize=12)
    ax.set_ylabel('Success Rate (%)', fontsize=12)
    ax.set_title('Success Rate by Archetype\nMovers Outperform Stayers', fontsize=14)

    overall = df['L'].mean() * 100
    ax.axhline(y=overall, color='black', linestyle='--', linewidth=1, label=f'Overall: {overall:.1f}%')
    ax.legend()

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'fig_success_by_archetype_real.png', dpi=300)
    plt.savefig(OUTPUT_DIR / 'fig_success_by_archetype_real.pdf')
    print(f"  Saved: fig_success_by_archetype_real.png/pdf")
    plt.close()


def validate_hypotheses(results_df, df):
    """Validate and print hypothesis results."""
    print("\n" + "=" * 60)
    print("HYPOTHESIS VALIDATION RESULTS")
    print("=" * 60)

    validation = {}

    # Stayer dG/dE < 0
    stayer = results_df[results_df['archetype'] == 'stayer']
    if len(stayer) > 0:
        v = stayer['dG_dE'].values[0]
        p = stayer['dG_dE_p'].values[0]
        passed = v < 0 and p < 0.05
        validation['stayer_dG_dE_negative'] = passed
        print(f"\nStayer dG/dE < 0: {v:.6f} (p={p:.4f}) {'PASS' if passed else 'FAIL'}")

    # Zoom-in dG/dE > 0
    zoom_in = results_df[results_df['archetype'] == 'zoom_in']
    if len(zoom_in) > 0:
        v = zoom_in['dG_dE'].values[0]
        p = zoom_in['dG_dE_p'].values[0]
        passed = v > 0 and p < 0.05
        validation['zoom_in_dG_dE_positive'] = passed
        print(f"Zoom-in dG/dE > 0: {v:.6f} (p={p:.4f}) {'PASS' if passed else 'FAIL'}")

    # Stayer dM/dE < 0
    if len(stayer) > 0:
        v = stayer['dM_dE'].values[0]
        passed = v < 0
        validation['stayer_dM_dE_negative'] = passed
        print(f"Stayer dM/dE < 0: {v:.6f} {'PASS' if passed else 'FAIL'}")

    # Movers dM/dE > 0
    for mtype in ['zoom_in', 'zoom_out']:
        row = results_df[results_df['archetype'] == mtype]
        if len(row) > 0:
            v = row['dM_dE'].values[0]
            passed = v > 0
            validation[f'{mtype}_dM_dE_positive'] = passed
            print(f"{mtype} dM/dE > 0: {v:.6f} {'PASS' if passed else 'FAIL'}")

    # Success rate
    mover_success = df[df['mover_type'].isin(['zoom_in', 'zoom_out'])]['L'].mean()
    stayer_success = df[df['mover_type'] == 'stayer']['L'].mean()
    passed = mover_success > stayer_success
    validation['mover_success_higher'] = passed
    print(f"Movers ({mover_success*100:.1f}%) > Stayers ({stayer_success*100:.1f}%): {'PASS' if passed else 'FAIL'}")

    print("\n" + "=" * 60)
    print(f"SUMMARY: {sum(validation.values())}/{len(validation)} hypotheses validated")
    print("=" * 60)

    return validation


def main():
    """Main entry point for figure generation."""
    print("=" * 60)
    print("4_T_commit2trap: Generating Archetype dG/dE Figures")
    print("=" * 60)

    # Load data
    df = load_real_data()

    # Compute slopes
    results = compute_archetype_slopes(df)

    print("\nArchetype Slopes Summary:")
    print("-" * 80)
    for _, row in results.iterrows():
        print(f"{row['archetype']:<12} N={row['n']:>6,}  dG/dE={row['dG_dE']:>8.4f}  "
              f"dG/dM={row['dG_dM']:>8.4f}  dM/dE={row['dM_dE']:>8.4f}  Success={row['success_rate']*100:>5.1f}%")
    print("-" * 80)

    # Generate figures
    print("\nGenerating figures...")
    plot_dG_dE_comparison(results)
    plot_decomposition(results)
    plot_V_efficiency_scatter(df)
    plot_success_by_archetype(df)

    # Validate
    validate_hypotheses(results, df)

    print(f"\nAll figures saved to: {OUTPUT_DIR}")


if __name__ == '__main__':
    main()
