#!/usr/bin/env python3
"""
generate_thesis_figures.py - Thesis Figure Generator with Consistent Color Scheme
==================================================================================

Generates all thesis figures with unified color palette for publication quality.

COLOR SCHEME (Final Agreed - 2026-01-11):
┌────────┬─────────────────┬────────────┬──────────┐
│ Symbol │ Variable        │ Color      │ Hex      │
├────────┼─────────────────┼────────────┼──────────┤
│ C      │ Commitment      │ Blue       │ #2E86AB  │
│ E      │ Early capital   │ Gold       │ #E9C46A  │
│ F      │ Flexibility     │ Green      │ #52B788  │
│ B      │ Breadth         │ Purple     │ #7B2CBF  │
│ R      │ Repositioning   │ Coral      │ #E76F51  │
│ G      │ Growth          │ Teal       │ #2A9D8F  │
│ L      │ Later Stage     │ Dark Gray  │ #264653  │
│ K      │ Kapital         │ Orange     │ #F4A261  │
└────────┴─────────────────┴────────────┴──────────┘

FIGURES TO GENERATE:
├── Ch1_G_E_paradox.png          - Capital Paradox (E vs G negative correlation)
├── Ch2_theory_mechanism.png     - Theory Mechanism (C→E→R→G) [user provided]
├── Ch2_R_E_golden_cage.png      - Golden Cage (E vs R negative correlation)
├── Ch4_L_archetype_mover.png    - Mover Advantage (Mover vs Stayer success)
├── Ch4_robustness_3x3.png       - Robustness checks
├── Ch5_L_industry_survival.png  - Industry heterogeneity
└── Ch5_L_Q_sweet_spot.png       - Sweet spot (optimal B quartile)

Usage:
    python generate_thesis_figures.py [--all | --fig1 | --fig2 | ...]

Author: Claude Code CLI
Date: 2026-01-11
"""

import argparse
from pathlib import Path
from datetime import datetime

import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap
from scipy.stats import spearmanr
import seaborn as sns

# ============================================================================
# COLOR SCHEME
# ============================================================================

COLORS = {
    'C': '#2E86AB',  # Commitment - Blue
    'E': '#E9C46A',  # Early capital - Gold
    'F': '#52B788',  # Flexibility - Green (latent)
    'B': '#7B2CBF',  # Breadth - Purple
    'R': '#E76F51',  # Repositioning - Coral
    'G': '#2A9D8F',  # Growth - Teal
    'L': '#264653',  # Later Stage - Dark Gray
    'K': '#F4A261',  # Kapital - Orange
    # Additional
    'positive': '#2A9D8F',  # Teal (good)
    'negative': '#E76F51',  # Coral (bad)
    'neutral': '#8D99AE',   # Gray
    'bg': '#FFFFFF',        # White background
    'grid': '#E5E5E5',      # Light gray grid
}

# Mover types
MOVER_COLORS = {
    'zoom_in': '#2E86AB',   # Blue - focusing
    'stayer': '#8D99AE',    # Gray - no movement
    'zoom_out': '#E76F51',  # Coral - expanding
}

# Quartile colors (B_0 quartiles)
QUARTILE_COLORS = {
    'Q1': '#264653',  # Dark - Low B (focused)
    'Q2': '#2A9D8F',  # Teal
    'Q3': '#E9C46A',  # Gold
    'Q4': '#E76F51',  # Coral - High B (vague)
}

# ============================================================================
# CONFIGURATION
# ============================================================================

SCRIPT_DIR = Path(__file__).parent.resolve()
DATA_DIR = SCRIPT_DIR / 'data' / 'processed'
OUTPUT_DIR = SCRIPT_DIR / 'figures'

# Figure settings
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica', 'Arial', 'DejaVu Sans'],
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
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
        raise FileNotFoundError(f"Panel not found: {nc_path}\nRun 00_data_pipeline.py first.")

    ds = xr.open_dataset(nc_path)
    df = pd.DataFrame({
        'company_id': ds['company'].values,
        'B_0': ds['B_0'].values,
        'B_T': ds['B_T'].values,
        'D': ds['D'].values,
        'R': ds['R'].values,
        'E': ds['E'].values,
        'K': ds['K'].values,
        'G': ds['G'].values,
        'L': ds['L'].values,
        'moved': ds['moved'].values,
        'mover_type': ds['mover_type'].values,
        'quartile_B0': ds['quartile_B0'].values,
        'sector': ds['sector'].values,
    })
    ds.close()
    return df


# ============================================================================
# FIGURE 1: Capital Paradox (Ch.1)
# ============================================================================

def fig1_capital_paradox(df, save=True):
    """
    Fig.1 Capital Paradox: ρ(G, E) < 0
    Shows that more early funding correlates with LOWER growth.
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Prepare data
    valid = df[(df['E'].notna()) & (df['G'].notna()) & (df['E'] > 0) & (df['G'] > 0)].copy()
    valid['log_E'] = np.log10(valid['E'])
    valid['log_G'] = np.log10(valid['G'])

    # Panel A: Scatter plot with regression
    ax = axes[0]

    # Sample for visibility
    sample = valid.sample(min(5000, len(valid)), random_state=42)

    ax.scatter(sample['log_E'], sample['log_G'],
               alpha=0.3, s=10, c=COLORS['E'], edgecolors='none')

    # Regression line
    z = np.polyfit(valid['log_E'], valid['log_G'], 1)
    p = np.poly1d(z)
    x_line = np.linspace(valid['log_E'].min(), valid['log_E'].max(), 100)
    ax.plot(x_line, p(x_line), color=COLORS['negative'], linewidth=2, linestyle='--')

    # Correlation
    rho, pval = spearmanr(valid['G'], valid['E'])

    ax.set_xlabel('Early Capital E (log₁₀ $M)')
    ax.set_ylabel('Growth G = K/E (log₁₀)')
    ax.set_title(f'A. Scatter: ρ(G, E) = {rho:.3f}***')
    ax.grid(True, alpha=0.3, color=COLORS['grid'])

    # Panel B: Box plot by E quartiles
    ax = axes[1]

    valid['E_quartile'] = pd.qcut(valid['E'], 4, labels=['Q1\n(Low E)', 'Q2', 'Q3', 'Q4\n(High E)'])

    quartile_order = ['Q1\n(Low E)', 'Q2', 'Q3', 'Q4\n(High E)']
    colors_q = [QUARTILE_COLORS['Q1'], QUARTILE_COLORS['Q2'],
                QUARTILE_COLORS['Q3'], QUARTILE_COLORS['Q4']]

    bp = ax.boxplot([valid[valid['E_quartile'] == q]['G'].dropna() for q in quartile_order],
                    labels=quartile_order, patch_artist=True)

    for patch, color in zip(bp['boxes'], colors_q):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)

    ax.set_ylabel('Growth G = K/E')
    ax.set_xlabel('Early Capital Quartile')
    ax.set_title('B. Growth by Early Capital Quartile')
    ax.set_ylim(0, 20)  # Cap for visibility
    ax.grid(True, alpha=0.3, color=COLORS['grid'], axis='y')

    plt.suptitle('Capital Paradox: More Early Funding → Lower Growth',
                 fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()

    if save:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        fig.savefig(OUTPUT_DIR / 'Ch1_G_E_paradox.png')
        print(f"  Saved: Ch1_G_E_paradox.png")

    return fig


# ============================================================================
# FIGURE 2: Golden Cage (Ch.2)
# ============================================================================

def fig2_golden_cage(df, save=True):
    """
    Fig.2 Golden Cage: E↑ → R↓
    Shows that more early funding correlates with LESS repositioning.
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Prepare data
    valid = df[(df['E'].notna()) & (df['R'].notna()) & (df['E'] > 0)].copy()
    valid['log_E'] = np.log10(valid['E'])

    # Panel A: Scatter
    ax = axes[0]

    sample = valid.sample(min(5000, len(valid)), random_state=42)

    ax.scatter(sample['log_E'], sample['R'],
               alpha=0.3, s=10, c=COLORS['E'], edgecolors='none')

    # Regression line
    z = np.polyfit(valid['log_E'], valid['R'], 1)
    p = np.poly1d(z)
    x_line = np.linspace(valid['log_E'].min(), valid['log_E'].max(), 100)
    ax.plot(x_line, p(x_line), color=COLORS['negative'], linewidth=2, linestyle='--')

    rho, pval = spearmanr(valid['R'], valid['E'])

    ax.set_xlabel('Early Capital E (log₁₀ $M)')
    ax.set_ylabel('Repositioning R = |B_T - B_0|')
    ax.set_title(f'A. Fund → Cage: ρ(R, E) = {rho:.3f}***')
    ax.grid(True, alpha=0.3, color=COLORS['grid'])

    # Panel B: Movement rate by E quartile
    ax = axes[1]

    valid['E_quartile'] = pd.qcut(valid['E'], 4, labels=['Q1\n(Low E)', 'Q2', 'Q3', 'Q4\n(High E)'])

    move_rates = valid.groupby('E_quartile')['moved'].mean() * 100

    colors_q = [QUARTILE_COLORS['Q1'], QUARTILE_COLORS['Q2'],
                QUARTILE_COLORS['Q3'], QUARTILE_COLORS['Q4']]
    bars = ax.bar(range(4), move_rates.values, color=colors_q, alpha=0.8, edgecolor='black')

    ax.set_xticks(range(4))
    ax.set_xticklabels(['Q1\n(Low E)', 'Q2', 'Q3', 'Q4\n(High E)'])
    ax.set_ylabel('Movement Rate (%)')
    ax.set_xlabel('Early Capital Quartile')
    ax.set_title('B. "Cage Effect": High E → Low Movement')
    ax.grid(True, alpha=0.3, color=COLORS['grid'], axis='y')

    # Add values on bars
    for bar, val in zip(bars, move_rates.values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{val:.1f}%', ha='center', va='bottom', fontsize=10)

    plt.suptitle('Golden Cage: More Early Funding → Less Strategic Repositioning',
                 fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()

    if save:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        fig.savefig(OUTPUT_DIR / 'Ch2_R_E_golden_cage.png')
        print(f"  Saved: Ch2_R_E_golden_cage.png")

    return fig


# ============================================================================
# FIGURE 4: Mover Advantage (Ch.4)
# ============================================================================

def fig4_mover_advantage(df, save=True):
    """
    Fig.4 Mover vs Stayer: Movement → Higher Success Rate
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Panel A: Success rate by mover type
    ax = axes[0]

    mover_success = df.groupby('mover_type')['L'].agg(['mean', 'count'])
    mover_success['pct'] = mover_success['mean'] * 100

    # Order: stayer, zoom_in, zoom_out
    order = ['stayer', 'zoom_in', 'zoom_out']
    labels = ['Stayer\n(No move)', 'Zoom In\n(Focus)', 'Zoom Out\n(Expand)']
    colors = [MOVER_COLORS[m] for m in order]

    heights = [mover_success.loc[m, 'pct'] if m in mover_success.index else 0 for m in order]
    counts = [mover_success.loc[m, 'count'] if m in mover_success.index else 0 for m in order]

    bars = ax.bar(range(3), heights, color=colors, alpha=0.8, edgecolor='black')

    ax.set_xticks(range(3))
    ax.set_xticklabels(labels)
    ax.set_ylabel('Success Rate (L=1) %')
    ax.set_title('A. Success Rate by Mover Type')
    ax.grid(True, alpha=0.3, color=COLORS['grid'], axis='y')

    for bar, val, n in zip(bars, heights, counts):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{val:.1f}%\n(n={n:,})', ha='center', va='bottom', fontsize=9)

    # Panel B: Success by R magnitude
    ax = axes[1]

    valid = df[df['R'].notna()].copy()
    valid['R_bin'] = pd.cut(valid['R'], bins=[0, 5, 10, 20, 100],
                            labels=['0-5', '5-10', '10-20', '20+'])

    r_success = valid.groupby('R_bin')['L'].mean() * 100

    colors_r = [COLORS['neutral'], COLORS['B'], COLORS['R'], COLORS['negative']]
    bars = ax.bar(range(4), r_success.values, color=colors_r, alpha=0.8, edgecolor='black')

    ax.set_xticks(range(4))
    ax.set_xticklabels(['0-5\n(Small)', '5-10', '10-20', '20+\n(Large)'])
    ax.set_ylabel('Success Rate (L=1) %')
    ax.set_xlabel('Repositioning Magnitude R')
    ax.set_title('B. Success Rate by Repositioning Magnitude')
    ax.grid(True, alpha=0.3, color=COLORS['grid'], axis='y')

    for bar, val in zip(bars, r_success.values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{val:.1f}%', ha='center', va='bottom', fontsize=10)

    # Calculate mover advantage
    mover_rate = df[df['moved'] == 1]['L'].mean() * 100
    stayer_rate = df[df['moved'] == 0]['L'].mean() * 100
    advantage = mover_rate / stayer_rate if stayer_rate > 0 else 0

    plt.suptitle(f'Mover Advantage: Movers {mover_rate:.1f}% vs Stayers {stayer_rate:.1f}% ({advantage:.2f}×)',
                 fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()

    if save:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        fig.savefig(OUTPUT_DIR / 'Ch4_L_archetype_mover.png')
        print(f"  Saved: Ch4_L_archetype_mover.png")

    return fig


# ============================================================================
# FIGURE 5: Sweet Spot (Ch.5)
# ============================================================================

def fig5_sweet_spot(df, save=True):
    """
    Fig.5 Sweet Spot: Optimal B quartile for success
    """
    fig, ax = plt.subplots(figsize=(8, 6))

    # Success by B_0 quartile
    q_success = df.groupby('quartile_B0')['L'].agg(['mean', 'count'])
    q_success['pct'] = q_success['mean'] * 100

    # Ensure order
    order = ['Q1', 'Q2', 'Q3', 'Q4']
    labels = ['Q1\n(Low B)\nFocused', 'Q2', 'Q3', 'Q4\n(High B)\nVague']
    colors = [QUARTILE_COLORS[q] for q in order]

    heights = [q_success.loc[q, 'pct'] if q in q_success.index else 0 for q in order]
    counts = [q_success.loc[q, 'count'] if q in q_success.index else 0 for q in order]

    bars = ax.bar(range(4), heights, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)

    ax.set_xticks(range(4))
    ax.set_xticklabels(labels)
    ax.set_ylabel('Success Rate (L=1) %')
    ax.set_xlabel('Initial Breadth (B₀) Quartile')
    ax.set_title('Sweet Spot: Optimal Strategic Ambiguity Level', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, color=COLORS['grid'], axis='y')

    # Highlight Q3 (if it's the sweet spot)
    max_idx = np.argmax(heights)
    bars[max_idx].set_edgecolor(COLORS['positive'])
    bars[max_idx].set_linewidth(3)

    for bar, val, n in zip(bars, heights, counts):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{val:.1f}%\n(n={n:,})', ha='center', va='bottom', fontsize=10)

    # Add arrow to sweet spot
    ax.annotate('Sweet Spot', xy=(max_idx, heights[max_idx]),
                xytext=(max_idx + 0.5, heights[max_idx] + 5),
                arrowprops=dict(arrowstyle='->', color=COLORS['positive'], lw=2),
                fontsize=12, color=COLORS['positive'], fontweight='bold')

    plt.tight_layout()

    if save:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        fig.savefig(OUTPUT_DIR / 'Ch5_L_Q_sweet_spot.png')
        print(f"  Saved: Ch5_L_Q_sweet_spot.png")

    return fig


# ============================================================================
# FIGURE: Correlation Summary
# ============================================================================

def fig_correlation_summary(df, save=True):
    """
    Summary figure showing all three key correlations.
    """
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    valid = df[(df['E'].notna()) & (df['G'].notna()) & (df['R'].notna()) &
               (df['E'] > 0) & (df['G'] > 0)].copy()
    valid['log_E'] = np.log1p(valid['E'])

    # 1. G vs E (Funding Paradox)
    ax = axes[0]
    rho1, _ = spearmanr(valid['G'], valid['log_E'])
    ax.scatter(valid['log_E'].sample(3000, random_state=42),
               valid['G'].sample(3000, random_state=42),
               alpha=0.2, s=5, c=COLORS['E'])
    ax.set_xlabel('log(E)')
    ax.set_ylabel('G = K/E')
    ax.set_title(f'Funding Paradox\nρ(G,E) = {rho1:+.3f}', color=COLORS['negative'])
    ax.set_ylim(0, 30)

    # 2. R vs E (Golden Cage)
    ax = axes[1]
    rho2, _ = spearmanr(valid['R'], valid['log_E'])
    ax.scatter(valid['log_E'].sample(3000, random_state=42),
               valid['R'].sample(3000, random_state=42),
               alpha=0.2, s=5, c=COLORS['E'])
    ax.set_xlabel('log(E)')
    ax.set_ylabel('R = |B_T - B_0|')
    ax.set_title(f'Golden Cage (Fund→Cage)\nρ(R,E) = {rho2:+.3f}', color=COLORS['negative'])

    # 3. G vs R (Reposition→Growth)
    ax = axes[2]
    rho3, _ = spearmanr(valid['G'], valid['R'])
    ax.scatter(valid['R'].sample(3000, random_state=42),
               valid['G'].sample(3000, random_state=42),
               alpha=0.2, s=5, c=COLORS['R'])
    ax.set_xlabel('R = |B_T - B_0|')
    ax.set_ylabel('G = K/E')
    ax.set_title(f'Reposition→Growth\nρ(G,R) = {rho3:+.3f}', color=COLORS['positive'])
    ax.set_ylim(0, 30)

    plt.suptitle('Golden Cage Mechanism: E → R(−) → G(+)',
                 fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()

    if save:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        fig.savefig(OUTPUT_DIR / 'summary_correlations.png')
        print(f"  Saved: summary_correlations.png")

    return fig


# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description='Generate thesis figures')
    parser.add_argument('--all', action='store_true', help='Generate all figures')
    parser.add_argument('--fig1', action='store_true', help='Capital Paradox')
    parser.add_argument('--fig2', action='store_true', help='Golden Cage')
    parser.add_argument('--fig4', action='store_true', help='Mover Advantage')
    parser.add_argument('--fig5', action='store_true', help='Sweet Spot')
    parser.add_argument('--summary', action='store_true', help='Correlation Summary')
    args = parser.parse_args()

    # If no args, generate all
    if not any([args.all, args.fig1, args.fig2, args.fig4, args.fig5, args.summary]):
        args.all = True

    print("=" * 60)
    print("THESIS FIGURE GENERATOR")
    print("=" * 60)
    print(f"Date: {datetime.now()}")
    print(f"Output: {OUTPUT_DIR}")
    print()

    # Load data
    print("Loading thesis panel...")
    df = load_panel()
    print(f"  N = {len(df):,} companies")
    print()

    # Generate figures
    print("Generating figures...")

    if args.all or args.fig1:
        print("\n[Fig.1] Capital Paradox...")
        fig1_capital_paradox(df)

    if args.all or args.fig2:
        print("\n[Fig.2] Golden Cage...")
        fig2_golden_cage(df)

    if args.all or args.fig4:
        print("\n[Fig.4] Mover Advantage...")
        fig4_mover_advantage(df)

    if args.all or args.fig5:
        print("\n[Fig.5] Sweet Spot...")
        fig5_sweet_spot(df)

    if args.all or args.summary:
        print("\n[Summary] Correlations...")
        fig_correlation_summary(df)

    print("\n" + "=" * 60)
    print("COMPLETE")
    print("=" * 60)

    plt.close('all')


if __name__ == '__main__':
    main()
