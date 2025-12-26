#!/usr/bin/env python3
"""
4_T_commit2trap: Generate Archetype dG/dE Figures for TRANSPORTATION Industry

This module generates transportation-specific figures for the thesis.

Data:
    Uses thesis_panel_v3_transportation.nc (N=244 companies)
    Note: Small sample size limits statistical power

Output:
    fig_archetype_dG_dE_transportation.png/pdf
    fig_decomposition_transportation.png/pdf
    fig_V_efficiency_transportation.png/pdf
    fig_success_by_archetype_transportation.png/pdf
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
from scipy.stats import linregress, spearmanr
from pathlib import Path

# Paths
SCRIPT_DIR = Path(__file__).parent.resolve()
REPO_ROOT = SCRIPT_DIR.parent.parent.parent.parent.parent  # empirics/
DATA_DIR = REPO_ROOT / 'data' / 'processed'
OUTPUT_DIR = SCRIPT_DIR


def load_transportation_data():
    """Load transportation thesis panel from .nc file."""
    nc_file = DATA_DIR / 'thesis_panel_v3_transportation.nc'

    if not nc_file.exists():
        raise FileNotFoundError(
            f"Transportation data not found: {nc_file}\n"
            "Run: python _shared/generate_thesis_nc_files.py --industry transportation"
        )

    ds = xr.open_dataset(nc_file)

    # Convert to DataFrame
    df = pd.DataFrame({
        'company_id': ds['company'].values,
        'V_0': ds['V_0'].values,
        'V_T': ds['V_T'].values,
        'D': ds['D'].values,
        'A': ds['A'].values,
        'E': ds['E'].values,
        'G': ds['G'].values,
        'L': ds['L'].values,
        'moved': ds['moved'].values,
        'mover_type': ds['mover_type'].values,
        'quartile_V0': ds['quartile_V0'].values,
    })

    ds.close()

    print(f"Loaded transportation data: {len(df):,} companies")
    print(f"Mover types: {df['mover_type'].value_counts().to_dict()}")

    return df


def compute_archetype_slopes(df):
    """Compute dG/dE, dG/dA, dA/dE by archetype."""
    analysis = df[df['E'].notna() & df['G'].notna() & (df['E'] > 0)].copy()

    if len(analysis) == 0:
        print("  Warning: No companies with valid E and G")
        return pd.DataFrame()

    analysis['log_E'] = np.log1p(analysis['E'])

    results = []

    for mtype in ['zoom_in', 'zoom_out', 'stayer', 'horizontal']:
        subset = analysis[analysis['mover_type'] == mtype]

        if len(subset) < 5:  # Lower threshold for small datasets
            continue

        # dG/dE
        try:
            slope_G_E, _, _, p_G_E, se_G_E = linregress(subset['log_E'], subset['G'])
        except:
            slope_G_E, p_G_E, se_G_E = np.nan, np.nan, np.nan

        # dG/dA
        movers = subset[subset['A'] > 0]
        if len(movers) > 3:
            try:
                slope_G_A, _, _, p_G_A, se_G_A = linregress(movers['A'], movers['G'])
            except:
                slope_G_A, p_G_A, se_G_A = np.nan, np.nan, np.nan
        else:
            slope_G_A, p_G_A, se_G_A = np.nan, np.nan, np.nan

        # dA/dE
        try:
            slope_A_E, _, _, p_A_E, se_A_E = linregress(subset['log_E'], subset['A'])
        except:
            slope_A_E, p_A_E, se_A_E = np.nan, np.nan, np.nan

        results.append({
            'archetype': mtype,
            'n': len(subset),
            'dG_dE': slope_G_E,
            'dG_dE_se': se_G_E,
            'dG_dE_p': p_G_E,
            'dG_dA': slope_G_A,
            'dG_dA_p': p_G_A,
            'dA_dE': slope_A_E,
            'dA_dE_p': p_A_E,
            'success_rate': subset['L'].mean(),
        })

    return pd.DataFrame(results)


def plot_dG_dE_comparison(results_df, df):
    """Fig: Archetype별 dG/dE Bar Chart for Transportation"""
    fig, ax = plt.subplots(figsize=(10, 6))

    if len(results_df) == 0:
        ax.text(0.5, 0.5, 'Insufficient data for analysis\n(N < 5 per archetype)',
                ha='center', va='center', fontsize=14, transform=ax.transAxes)
        ax.set_title('Transportation: dG/dE by Archetype\n(Insufficient Data)', fontsize=14)
    else:
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
        ax.set_ylabel('dG/dE (log Capital -> Growth)', fontsize=12)
        ax.set_title(f'Transportation Industry: dG/dE by Archetype\n(N={len(df):,} companies)', fontsize=14)

        # Add N labels
        for i, (slope, n) in enumerate(zip(slopes, results_df['n'])):
            sig = '*' if results_df.iloc[i]['dG_dE_p'] < 0.05 else ''
            y_pos = slope + (errors[i] if slope >= 0 else -errors[i]) + 0.01 * np.sign(slope)
            ax.annotate(f'{sig}\n(N={n})', (i, y_pos), ha='center', fontsize=9)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'fig_archetype_dG_dE_transportation.png', dpi=300)
    plt.savefig(OUTPUT_DIR / 'fig_archetype_dG_dE_transportation.pdf')
    print(f"  Saved: fig_archetype_dG_dE_transportation.png/pdf")
    plt.close()


def plot_V_efficiency_scatter(df):
    """Fig: V Level x Adaptation Scatter for Transportation"""
    fig, ax = plt.subplots(figsize=(10, 8))

    colors = {
        'zoom_in': '#1f77b4',
        'zoom_out': '#2ca02c',
        'stayer': '#d62728',
        'horizontal': '#7f7f7f'
    }

    for mtype in colors:
        subset = df[df['mover_type'] == mtype]
        if len(subset) > 0:
            ax.scatter(subset['V_0'], subset['A'], alpha=0.7,
                       c=colors[mtype], label=f'{mtype} (N={len(subset)})', s=50)

    # Shade trap region
    ax.axvspan(0, 25, alpha=0.15, color='red')
    ax.axvline(x=25, color='red', linestyle=':', linewidth=2, alpha=0.7)

    ax.set_xlabel('V_0 (Initial Vagueness)', fontsize=12)
    ax.set_ylabel('A (Adaptation = |D|)', fontsize=12)
    ax.set_title(f'Transportation: Vagueness vs Adaptation\n(N={len(df):,} companies)', fontsize=14)
    ax.legend(loc='upper right', fontsize=10)

    # Add correlation if enough data
    if len(df) > 10:
        rho, p = spearmanr(df['V_0'], df['A'])
        ax.text(0.02, 0.98, f'Spearman rho = {rho:.3f}\np = {p:.3f}',
                transform=ax.transAxes, fontsize=10, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'fig_V_efficiency_transportation.png', dpi=300)
    plt.savefig(OUTPUT_DIR / 'fig_V_efficiency_transportation.pdf')
    print(f"  Saved: fig_V_efficiency_transportation.png/pdf")
    plt.close()


def plot_success_by_archetype(df):
    """Fig: Success Rate by Archetype for Transportation"""
    fig, ax = plt.subplots(figsize=(10, 6))

    archetypes = ['zoom_in', 'zoom_out', 'stayer', 'horizontal']
    success_rates = []
    ns = []
    colors_list = []

    for m in archetypes:
        subset = df[df['mover_type'] == m]
        if len(subset) > 0:
            success_rates.append(subset['L'].mean() * 100)
            ns.append(len(subset))
        else:
            success_rates.append(0)
            ns.append(0)

        if m in ['zoom_in', 'zoom_out']:
            colors_list.append('#2ca02c')
        elif m == 'stayer':
            colors_list.append('#d62728')
        else:
            colors_list.append('#7f7f7f')

    ax.bar(archetypes, success_rates, color=colors_list, alpha=0.7, edgecolor='black')

    for i, (rate, n) in enumerate(zip(success_rates, ns)):
        if n > 0:
            ax.annotate(f'{rate:.1f}%\n(N={n})', (i, rate + 2), ha='center', fontsize=10)

    ax.set_xlabel('Archetype', fontsize=12)
    ax.set_ylabel('Success Rate (%)', fontsize=12)
    ax.set_title(f'Transportation: Success Rate by Archetype\n(N={len(df):,} companies)', fontsize=14)

    # Overall rate
    overall = df['L'].mean() * 100
    ax.axhline(y=overall, color='black', linestyle='--', linewidth=1, label=f'Overall: {overall:.1f}%')
    ax.legend()

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'fig_success_by_archetype_transportation.png', dpi=300)
    plt.savefig(OUTPUT_DIR / 'fig_success_by_archetype_transportation.pdf')
    print(f"  Saved: fig_success_by_archetype_transportation.png/pdf")
    plt.close()


def plot_comparison_all_vs_transportation(df_trans):
    """Compare transportation to all-industry results"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Load all-industry data
    ds_all = xr.open_dataset(DATA_DIR / 'thesis_panel_v3.nc')
    df_all = pd.DataFrame({
        'mover_type': ds_all['mover_type'].values,
        'L': ds_all['L'].values,
    })
    ds_all.close()

    archetypes = ['zoom_in', 'zoom_out', 'stayer', 'horizontal']
    x = np.arange(len(archetypes))
    width = 0.35

    # Success rates
    ax1 = axes[0]
    all_rates = [df_all[df_all['mover_type'] == m]['L'].mean() * 100 for m in archetypes]
    trans_rates = [df_trans[df_trans['mover_type'] == m]['L'].mean() * 100
                   if len(df_trans[df_trans['mover_type'] == m]) > 0 else 0 for m in archetypes]

    ax1.bar(x - width/2, all_rates, width, label=f'All Industries (N={len(df_all):,})', color='#1f77b4', alpha=0.7)
    ax1.bar(x + width/2, trans_rates, width, label=f'Transportation (N={len(df_trans):,})', color='#ff7f0e', alpha=0.7)

    ax1.set_xticks(x)
    ax1.set_xticklabels(archetypes)
    ax1.set_xlabel('Archetype', fontsize=12)
    ax1.set_ylabel('Success Rate (%)', fontsize=12)
    ax1.set_title('Success Rate: All Industries vs Transportation', fontsize=14)
    ax1.legend()

    # Mover distribution
    ax2 = axes[1]
    all_dist = [len(df_all[df_all['mover_type'] == m]) / len(df_all) * 100 for m in archetypes]
    trans_dist = [len(df_trans[df_trans['mover_type'] == m]) / len(df_trans) * 100 for m in archetypes]

    ax2.bar(x - width/2, all_dist, width, label='All Industries', color='#1f77b4', alpha=0.7)
    ax2.bar(x + width/2, trans_dist, width, label='Transportation', color='#ff7f0e', alpha=0.7)

    ax2.set_xticks(x)
    ax2.set_xticklabels(archetypes)
    ax2.set_xlabel('Archetype', fontsize=12)
    ax2.set_ylabel('% of Companies', fontsize=12)
    ax2.set_title('Archetype Distribution: All vs Transportation', fontsize=14)
    ax2.legend()

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'fig_comparison_all_vs_transportation.png', dpi=300)
    plt.savefig(OUTPUT_DIR / 'fig_comparison_all_vs_transportation.pdf')
    print(f"  Saved: fig_comparison_all_vs_transportation.png/pdf")
    plt.close()


def main():
    print("=" * 60)
    print("4_T_commit2trap: Transportation Industry Figures")
    print("=" * 60)

    # Load data
    df = load_transportation_data()

    # Compute slopes
    results = compute_archetype_slopes(df)

    if len(results) > 0:
        print("\nArchetype Slopes (Transportation):")
        print("-" * 60)
        for _, row in results.iterrows():
            print(f"{row['archetype']:<12} N={row['n']:>4}  dG/dE={row['dG_dE']:>8.4f}  Success={row['success_rate']*100:>5.1f}%")
        print("-" * 60)
    else:
        print("\nWarning: Insufficient data for slope analysis")

    # Generate figures
    print("\nGenerating figures...")
    plot_dG_dE_comparison(results, df)
    plot_V_efficiency_scatter(df)
    plot_success_by_archetype(df)
    plot_comparison_all_vs_transportation(df)

    print(f"\nAll figures saved to: {OUTPUT_DIR}")

    # Summary
    print("\n" + "=" * 60)
    print("TRANSPORTATION INDUSTRY SUMMARY")
    print("=" * 60)
    print(f"Total companies: {len(df):,}")
    print(f"Movers: {df['moved'].sum()} ({df['moved'].mean()*100:.1f}%)")
    print(f"Overall success rate: {df['L'].mean()*100:.1f}%")
    print(f"\nNote: Small sample size (N={len(df)}) limits statistical power.")
    print("Transportation has high stayer rate (94.7%) - most companies don't change V.")
    print("=" * 60)


if __name__ == '__main__':
    main()
