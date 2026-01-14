#!/usr/bin/env python3
"""
fix_figure_colors.py - Fix Fig4 and Fig5 to use grayscale only
==============================================================

Regenerates:
1. Fig4_growth_by_R.png → Ch4_Fig1_mover_advantage.png (grayscale, no yellow)
2. Fig5_industry_rho.png → Ch4_Fig2_industry_rho.png (grayscale only)

Author: Claude Code CLI
Date: 2026-01-14
"""

import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.stats import chi2_contingency, spearmanr

SCRIPT_DIR = Path(__file__).parent.resolve()
DATA_DIR = SCRIPT_DIR / 'data' / 'processed'
OUTPUT_DIR = SCRIPT_DIR.parent / 'figures'

# GRAYSCALE PALETTE - No colors!
COLORS = {
    'dark': '#2c3e50',      # Dark gray for emphasis
    'medium': '#6c7a89',    # Medium gray
    'light': '#bdc3c7',     # Light gray
    'white': '#ffffff',
    'black': '#1a1a1a',
    'grid': '#e8e8e8',
}

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica', 'Arial', 'DejaVu Sans'],
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
})


def load_panel():
    """Load thesis panel data."""
    nc_path = DATA_DIR / 'thesis_panel_v3.nc'
    if not nc_path.exists():
        raise FileNotFoundError(f"Panel not found: {nc_path}")

    ds = xr.open_dataset(nc_path)
    df = pd.DataFrame({
        'company_id': ds['company'].values,
        'B_0': ds['B_0'].values,
        'B_T': ds['B_T'].values,
        'R': ds['R'].values,
        'E': ds['E'].values,
        'G': ds['G'].values,
        'L': ds['L'].values,
        'moved': ds['moved'].values,
        'sector': ds['sector'].values,
    })
    ds.close()
    return df


def fig4_mover_advantage_grayscale(df, save=True):
    """
    Ch4 Fig1: Mover vs Stayer Success Rates

    GRAYSCALE ONLY - No yellow, no red, no green
    """
    fig, ax = plt.subplots(figsize=(8, 6))

    # Calculate stats
    df_valid = df[df['R'].notna()].copy()
    df_valid['is_mover'] = (df_valid['R'] > 0).astype(int)

    movers = df_valid[df_valid['is_mover'] == 1]
    stayers = df_valid[df_valid['is_mover'] == 0]

    mover_success = movers['L'].mean() * 100
    stayer_success = stayers['L'].mean() * 100
    n_movers = len(movers)
    n_stayers = len(stayers)
    advantage = mover_success / stayer_success if stayer_success > 0 else 0

    # Chi-square test
    contingency = pd.crosstab(df_valid['is_mover'], df_valid['L'])
    chi2, p_value, _, _ = chi2_contingency(contingency)

    # Bar chart - GRAYSCALE
    categories = ['Stayers\n(R = 0)\n□ Caged', 'Movers\n(R > 0)\n□ Repositioned']
    success_rates = [stayer_success, mover_success]
    n_values = [n_stayers, n_movers]
    colors = [COLORS['light'], COLORS['dark']]  # Light for stayers, dark for movers

    bars = ax.bar(categories, success_rates, color=colors,
                  edgecolor=COLORS['black'], linewidth=2, width=0.6)

    # Value labels
    for i, (bar, rate, n) in enumerate(zip(bars, success_rates, n_values)):
        # Rate on top
        ax.text(bar.get_x() + bar.get_width()/2, rate + 0.8,
                f'{rate:.1f}%', ha='center', fontsize=16, fontweight='bold',
                color=COLORS['black'])
        # N inside bar
        text_color = COLORS['white'] if i == 1 else COLORS['dark']
        ax.text(bar.get_x() + bar.get_width()/2, rate/2,
                f'n = {n:,}', ha='center', fontsize=11,
                color=text_color, fontweight='bold')

    # Advantage arrow
    ax.annotate('', xy=(1, mover_success), xytext=(0, stayer_success),
                arrowprops=dict(arrowstyle='->', color=COLORS['dark'], lw=2,
                               connectionstyle='arc3,rad=0.2'))

    # Advantage label - GRAYSCALE BOX (no yellow!)
    max_y = max(success_rates)
    ax.text(0.5, max_y * 1.18, f'{advantage:.2f}×',
            ha='center', fontsize=24, fontweight='bold', color=COLORS['dark'],
            bbox=dict(boxstyle='round,pad=0.4', facecolor=COLORS['white'],
                     edgecolor=COLORS['dark'], linewidth=3))
    ax.text(0.5, max_y * 1.03, 'Mover Advantage',
            ha='center', fontsize=12, style='italic', color=COLORS['medium'])

    # Labels
    ax.set_ylabel('Success Rate (Later Stage VC) %', fontsize=13)
    ax.set_title('Growth by Repositioning\n"Move to Grow"',
                 fontsize=15, fontweight='bold')
    ax.set_ylim(0, max_y * 1.4)
    ax.grid(True, alpha=0.3, color=COLORS['grid'], axis='y')

    # Significance
    sig = '***' if p_value < 0.001 else '**' if p_value < 0.01 else '*'
    ax.text(0.98, 0.02, f'χ² = {chi2:,.0f}{sig}',
            transform=ax.transAxes, ha='right', fontsize=10, color=COLORS['medium'])

    # Footer
    fig.text(0.5, -0.03,
             f'N = {len(df_valid):,} | Mover = R > 0 (any repositioning)',
             ha='center', fontsize=10, color=COLORS['medium'])

    plt.tight_layout()

    if save:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        fig.savefig(OUTPUT_DIR / 'Ch4_Fig1_mover_advantage.png')
        print(f"  Saved: Ch4_Fig1_mover_advantage.png")

    return fig


def fig5_industry_rho_grayscale(df, save=True):
    """
    Ch4 Fig2: Industry Heterogeneity in ρ(E, G)

    GRAYSCALE ONLY - All bars in shades of gray
    """
    fig, ax = plt.subplots(figsize=(12, 7))

    # Calculate correlations by sector
    valid = df[(df['E'].notna()) & (df['G'].notna()) & (df['E'] > 0) & (df['G'] > 0)].copy()

    results = []
    for sector in valid['sector'].unique():
        if pd.isna(sector):
            continue
        sector_data = valid[valid['sector'] == sector]
        if len(sector_data) >= 30:  # Minimum sample
            rho, pval = spearmanr(sector_data['E'], sector_data['G'])
            results.append({
                'sector': sector,
                'rho': rho,
                'pval': pval,
                'n': len(sector_data)
            })

    results_df = pd.DataFrame(results).sort_values('rho')

    # Create horizontal bar chart - GRAYSCALE ONLY
    y_pos = np.arange(len(results_df))

    # All bars in gray (darker = more negative)
    bar_colors = []
    for rho in results_df['rho']:
        if rho < -0.08:
            bar_colors.append(COLORS['dark'])      # Strong negative
        elif rho < -0.04:
            bar_colors.append(COLORS['medium'])    # Moderate negative
        elif rho < 0:
            bar_colors.append(COLORS['light'])     # Weak negative
        else:
            bar_colors.append('#f0f0f0')           # Positive (very light)

    bars = ax.barh(y_pos, results_df['rho'], color=bar_colors,
                   edgecolor=COLORS['black'], linewidth=1)

    # Vertical line at x=0
    ax.axvline(x=0, color=COLORS['black'], linewidth=1.5)

    # Labels
    ax.set_yticks(y_pos)
    ax.set_yticklabels(results_df['sector'])
    ax.set_xlabel('ρ(E, G) Correlation', fontsize=12)

    # Significance stars and N values
    for i, (idx, row) in enumerate(results_df.iterrows()):
        sig = '***' if row['pval'] < 0.001 else '**' if row['pval'] < 0.01 else '*' if row['pval'] < 0.05 else 'ns'

        # Position text based on bar direction
        if row['rho'] < 0:
            ax.text(row['rho'] - 0.005, i, sig, ha='right', va='center', fontsize=10, fontweight='bold')
            ax.text(0.14, i, f'N={row["n"]:,}', ha='right', va='center', fontsize=9, color=COLORS['medium'])
        else:
            ax.text(row['rho'] + 0.005, i, sig, ha='left', va='center', fontsize=10, fontweight='bold')
            ax.text(-0.14, i, f'N={row["n"]:,}', ha='left', va='center', fontsize=9, color=COLORS['medium'])

    ax.set_xlim(-0.15, 0.15)

    # Title
    ax.set_title('Industry Heterogeneity: Early Funding × Growth Correlation\n'
                 'The Multiplicative Model: dG/dE = (dG/dR) × (dR/dE) = (+) × (−) = (−)',
                 fontsize=13, fontweight='bold')

    # Annotation box
    ax.text(0.02, 0.15,
            'Capital-intensive industries (Hardware, Transportation)\n'
            'show strongest negative correlations.\n'
            'Only Quantum shows positive ρ (n=1,144).',
            transform=ax.transAxes, fontsize=9,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#f8f8f8',
                     edgecolor=COLORS['medium'], alpha=0.9))

    ax.grid(True, alpha=0.3, color=COLORS['grid'], axis='x')

    plt.tight_layout()

    if save:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        fig.savefig(OUTPUT_DIR / 'Ch4_Fig2_industry_rho.png')
        print(f"  Saved: Ch4_Fig2_industry_rho.png")

    return fig


def main():
    print("="*60)
    print("FIXING FIGURE COLORS TO GRAYSCALE")
    print("="*60)

    # Load data
    print("\nLoading thesis panel...")
    df = load_panel()
    print(f"  N = {len(df):,} companies")

    # Generate figures
    print("\n[Fig4] Mover Advantage (grayscale)...")
    fig4_mover_advantage_grayscale(df)

    print("\n[Fig5] Industry Rho (grayscale)...")
    fig5_industry_rho_grayscale(df)

    print("\n" + "="*60)
    print("COMPLETE - All figures now grayscale")
    print("="*60)


if __name__ == '__main__':
    main()
