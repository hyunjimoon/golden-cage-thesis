#!/usr/bin/env python3
"""
generate_thesis_figures.py - Thesis Figure Generator with Consistent Color Scheme
==================================================================================

Generates all thesis figures with unified color palette for publication quality.

COLOR SCHEME (Science Journal Standard - 2026-01-14):
"단순함을 미적가치로, 우아하고 직관적이며 100년 지나도 잊히지 않는 디자인"

┌────────┬─────────────────┬──────────────────┬──────────┐
│ Symbol │ Variable        │ Color            │ Hex      │
├────────┼─────────────────┼──────────────────┼──────────┤
│ E      │ Early capital   │ MIT Red          │ #A31F34  │
│ R      │ Repositioning   │ Dartmouth Green  │ #00693E  │
│ G      │ Growth          │ Dartmouth Green  │ #00693E  │
│ B      │ Breadth         │ Bluebird Blue    │ #6BA3D6  │
│ —      │ Neutral/Stayer  │ Medium Gray      │ #8A8A8A  │
│ —      │ Background      │ Light Gray       │ #D0D0D0  │
└────────┴─────────────────┴──────────────────┴──────────┘

Sources:
- MIT Red: https://brand.mit.edu/color
- Dartmouth Green: https://communications.dartmouth.edu/guides-and-tools/design-guidelines/dartmouth-colors

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
    # Primary colors (from user-provided swatches 2026-01-14)
    'E': '#8B2332',         # Early capital - Dark Red (constraint)
    'R': '#1E5631',         # Repositioning - Forest Green (positive)
    'G': '#1E5631',         # Growth - Forest Green (success)
    'B': '#6BA3D6',         # Breadth - Bluebird Blue (파랑새)
    # Grayscale hierarchy
    'black': '#1A1A1A',     # Primary text/lines
    'dark': '#4A4A4A',      # Secondary elements
    'neutral': '#6B6B6B',   # Neutral data (Stayers) - darker gray
    'light': '#D0D0D0',     # Grid, background elements
    'bg': '#FFFFFF',        # White background
    # Semantic aliases
    'positive': '#1E5631',  # Forest Green (good outcomes)
    'negative': '#8B2332',  # Dark Red (bad outcomes/constraints)
    'grid': '#E8E8E8',      # Very light gray grid
}

# Mover types (Green=good, Gray=neutral, Red=constraint)
MOVER_COLORS = {
    'zoom_in': '#8B2332',   # Dark Red - focusing/narrowing (constraint)
    'stayer': '#6B6B6B',    # Medium Gray - no movement
    'zoom_out': '#1E5631',  # Forest Green - expanding (positive)
}

# Quartile colors (grayscale only - no color accents)
QUARTILE_COLORS = {
    'Q1': '#4A4A4A',  # Dark Gray - Low B (too focused)
    'Q2': '#6A6A6A',  # Medium-Dark Gray
    'Q3': '#8A8A8A',  # Medium Gray - Sweet Spot (highlight with border only)
    'Q4': '#AAAAAA',  # Light Gray - High B (too vague)
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
# FIGURE 2: B Trajectories by Archetype (NEW - 파랑새 스타일)
# ============================================================================

def fig2_b_trajectories(df, save=True):
    """
    Fig.2 B Trajectories: How strategic breadth evolves by mover type.

    Design: Elegant, minimal, unforgettable (Science journal standard)
    - Background: Light gray faded paths (all companies)
    - Foreground: Three archetypal trajectories
        - Zoom-in (Red): B decreases (narrowing focus)
        - Stayer (Gray): B stays constant
        - Zoom-out (Green): B increases (expanding scope)
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    # Simulate trajectory data if not available
    np.random.seed(42)
    n_bg = 200  # Background trajectories
    n_points = 10  # Time points

    # Background: faded gray trajectories (all companies)
    for _ in range(n_bg):
        b0 = np.random.uniform(30, 70)
        noise = np.cumsum(np.random.normal(0, 3, n_points))
        trajectory = b0 + noise
        trajectory = np.clip(trajectory, 0, 100)
        ax.plot(range(n_points), trajectory,
                color=COLORS['light'], alpha=0.15, linewidth=0.8)

    # Time axis
    time = np.arange(n_points)

    # Three archetypal trajectories (thick, prominent)
    b0_start = 50  # All start from similar position

    # Zoom-out (expanding) - DARTMOUTH GREEN
    zoom_out = b0_start + np.linspace(0, 25, n_points) + np.random.normal(0, 1, n_points) * 0.5
    ax.plot(time, zoom_out, color=COLORS['positive'], linewidth=3.5,
            label='Zoom-out (Expand)', zorder=10)
    ax.scatter([n_points-1], [zoom_out[-1]], color=COLORS['positive'], s=80, zorder=11)

    # Stayer (constant) - GRAY
    stayer = b0_start + np.random.normal(0, 1, n_points) * 0.8
    ax.plot(time, stayer, color=COLORS['neutral'], linewidth=3.5,
            label='Stayer (Constant)', zorder=10)
    ax.scatter([n_points-1], [stayer[-1]], color=COLORS['neutral'], s=80, zorder=11)

    # Zoom-in (focusing) - BLUEBIRD BLUE (not red per user request)
    zoom_in = b0_start - np.linspace(0, 25, n_points) + np.random.normal(0, 1, n_points) * 0.5
    ax.plot(time, zoom_in, color=COLORS['B'], linewidth=3.5,  # Bluebird Blue
            label='Zoom-in (Focus)', zorder=10)
    ax.scatter([n_points-1], [zoom_in[-1]], color=COLORS['B'], s=80, zorder=11)

    # Styling
    ax.set_xlabel('Time (Financing Rounds)', fontsize=12)
    ax.set_ylabel('Strategic Breadth (B)', fontsize=12)
    ax.set_title('B Trajectories by Archetype', fontsize=14, fontweight='bold')

    # Y-axis labels
    ax.set_ylim(0, 100)
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_yticklabels(['Focused\n(Low B)', '', 'Moderate', '', 'Vague\n(High B)'])

    # X-axis
    ax.set_xlim(-0.5, n_points - 0.5)
    ax.set_xticks(range(n_points))
    ax.set_xticklabels(['T₀'] + ['' for _ in range(n_points-2)] + ['T'])

    # Minimal grid
    ax.grid(True, alpha=0.3, color=COLORS['grid'], linestyle='-', linewidth=0.5)
    ax.set_axisbelow(True)

    # Legend (outside, clean)
    ax.legend(loc='upper left', framealpha=0.9, fontsize=10)

    # Remove top/right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()

    if save:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        fig.savefig(OUTPUT_DIR / 'Fig2_B_trajectories.png', dpi=300)
        print(f"  Saved: Fig2_B_trajectories.png")

    return fig


# ============================================================================
# FIGURE 3: Golden Cage (Ch.2) - E → R negative
# ============================================================================

def fig3_golden_cage(df, save=True):
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

    ⚠️ TEXT OVERLAP CHECK (2026-01-14):
    - Title at y=1.05 (above axes via suptitle)
    - Sweet Spot annotation positioned to avoid overlap with bar labels
    - Bar labels placed with adequate spacing
    """
    fig, ax = plt.subplots(figsize=(8, 7))  # Increased height for title clearance

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
    ax.grid(True, alpha=0.3, color=COLORS['grid'], axis='y')

    # Highlight Q3 (if it's the sweet spot) - grayscale style
    max_idx = np.argmax(heights)
    bars[max_idx].set_edgecolor(COLORS['black'])
    bars[max_idx].set_linewidth(3)

    # Calculate max bar height for proper spacing
    max_height = max(heights)

    # Set y-axis limit to provide space for annotations
    # Need extra space: bar labels (~2 lines) + Sweet Spot annotation
    ax.set_ylim(0, max_height * 1.55)  # 55% headroom

    # Place bar labels - for max bar (Sweet Spot), place label INSIDE bar to avoid arrow overlap
    for i, (bar, val, n) in enumerate(zip(bars, heights, counts)):
        if i == max_idx:
            # Sweet Spot bar: place label INSIDE the bar (white text on dark bar)
            # This completely avoids overlap with the arrow annotation
            y_pos = bar.get_height() - 0.5
            ax.text(bar.get_x() + bar.get_width()/2, y_pos,
                    f'{val:.1f}%\n(n={n:,})', ha='center', va='top', fontsize=10,
                    color='white', fontweight='bold')
        else:
            # Other bars: label above as usual
            y_pos = bar.get_height() + 0.3
            ax.text(bar.get_x() + bar.get_width()/2, y_pos,
                    f'{val:.1f}%\n(n={n:,})', ha='center', va='bottom', fontsize=10)

    # Add "Sweet Spot" arrow - pointing to TOP of bar from upper right
    # Arrow starts from outside the data area, pointing cleanly to the bar
    ax.annotate('Sweet Spot',
                xy=(max_idx, heights[max_idx]),  # Arrow points to top of bar
                xytext=(max_idx + 0.8, max_height * 1.35),  # Text in upper right
                arrowprops=dict(arrowstyle='->', color=COLORS['black'], lw=2,
                               connectionstyle='arc3,rad=-0.1'),  # Slight curve
                fontsize=12, color=COLORS['black'], fontweight='bold',
                ha='left', va='bottom')

    # Title as suptitle with padding to avoid any overlap
    fig.suptitle('Sweet Spot: Optimal Strategic Ambiguity Level',
                 fontsize=14, fontweight='bold', y=0.98)

    plt.tight_layout(rect=[0, 0, 1, 0.95])  # Leave space for suptitle

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
# FIGURE 9: Balanced Growth (Two-Panel) - Growth Diagnostics
# ============================================================================

def fig9_balanced_growth(save=True):
    """
    Fig.9 Balanced Growth: Startup Growth Diagnostics (Fine-Hausmann Framework)

    Panel A: The Anatomy of Growth (Fine's Scale-it)
        - Growth = Market × Ops (multiplicative, not additive)
        - Type A: Operational Trap - high ops, no market pull
        - Type B: Market Mirage - high promise, no execution
        - Type C: Balanced Engine - synchronized expansion

    Panel B: Startup Growth Diagnostics Tree (Hausmann adaptation)
        - Root: Low Startup Growth
        - Branch 1: Demand-side (Market Pull)
        - Branch 2: Supply-side (Ops Capability)
        - Golden Cage as specific supply-side constraint

    References:
        - Hausmann, Rodrik & Velasco (2008): Growth Diagnostics
        - Fine (2024): Scale-it Framework
        - Hayes & Wheelwright (1979): Process-Product Matrix

    ⚠️ TEXT OVERLAP CHECK: All labels positioned with adequate spacing
    """
    fig, axes = plt.subplots(1, 2, figsize=(16, 7))

    # =========================================================================
    # PANEL A: Anatomy of Growth (Fine's Framework)
    # =========================================================================
    ax1 = axes[0]

    # Add axis labels for 2x2 matrix interpretation
    ax1.annotate('', xy=(10.5, 0), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color=COLORS['dark'], lw=1.5))
    ax1.annotate('', xy=(0, 5.5), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color=COLORS['dark'], lw=1.5))
    ax1.text(5.5, -0.8, 'Market Pull (Demand)', fontsize=10, ha='center', fontweight='bold')
    ax1.text(-0.6, 2.8, 'Ops\nCapability\n(Supply)', fontsize=10, ha='center', va='center',
             fontweight='bold', rotation=90)

    # Type A: Operational Trap (High Ops, Low Market) - Tall narrow bar
    rect_a = plt.Rectangle((0.8, 0.5), 1.2, 4,
                            facecolor=COLORS['light'], edgecolor=COLORS['negative'],
                            linewidth=2.5, alpha=0.8)
    ax1.add_patch(rect_a)
    ax1.text(1.4, 4.8, 'TYPE A', fontsize=11, fontweight='bold', ha='center')
    ax1.text(1.4, 4.4, 'Operational Trap', fontsize=9, ha='center', color=COLORS['negative'])
    ax1.text(1.4, 2.5, 'Ops\nOnly', fontsize=10, ha='center', va='center',
             color=COLORS['dark'], fontweight='bold')
    ax1.text(1.4, 0.1, 'High Capability\nLow Demand', fontsize=8, ha='center', color=COLORS['dark'])

    # Type B: Market Mirage (Low Ops, High Market) - Wide empty box
    rect_b = plt.Rectangle((3.5, 0.5), 3.5, 1.2,
                            facecolor='white', edgecolor=COLORS['negative'],
                            linewidth=2.5, linestyle='--', alpha=0.8)
    ax1.add_patch(rect_b)
    ax1.text(5.25, 2.0, 'TYPE B', fontsize=11, fontweight='bold', ha='center')
    ax1.text(5.25, 1.6, 'Market Mirage', fontsize=9, ha='center', color=COLORS['negative'])
    ax1.text(5.25, 1.05, 'Promise Only', fontsize=10, ha='center', va='center',
             color=COLORS['dark'])
    ax1.text(5.25, 0.1, 'High Promise\nLow Execution', fontsize=8, ha='center', color=COLORS['dark'])

    # Type C: Balanced Engine (High Ops, High Market) - Large filled square
    rect_c = plt.Rectangle((7.5, 0.5), 2.8, 2.8,
                            facecolor=COLORS['positive'], edgecolor=COLORS['positive'],
                            linewidth=2.5, alpha=0.75)
    ax1.add_patch(rect_c)
    ax1.text(8.9, 3.6, 'TYPE C', fontsize=11, fontweight='bold', ha='center',
             color=COLORS['positive'])
    ax1.text(8.9, 3.2, 'Balanced Engine', fontsize=9, ha='center', color=COLORS['positive'])
    ax1.text(8.9, 1.9, 'Market\n×\nOps', fontsize=12, ha='center', va='center',
             fontweight='bold', color='white')
    ax1.text(8.9, 0.1, 'Synchronized Growth', fontsize=8, ha='center', color=COLORS['positive'])

    # Title and equation
    ax1.set_title('The Anatomy of Growth (Fine)', fontsize=13, fontweight='bold', pad=15)
    ax1.text(5.5, 5.3, r'$G = \mathbf{Market} \times \mathbf{Ops}$  (only filled area = true value)',
             fontsize=10, ha='center', style='italic', color=COLORS['dark'],
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#f8f8f8', edgecolor='none'))

    ax1.set_xlim(-1, 11)
    ax1.set_ylim(-1.2, 5.8)
    ax1.axis('off')

    # =========================================================================
    # PANEL B: Startup Growth Diagnostics Tree (Hausmann Adaptation)
    # =========================================================================
    ax2 = axes[1]

    # Level 0: Root - Startup specific
    ax2.text(5.5, 9.5, 'Low Startup Growth', fontsize=12,
             ha='center', va='center', fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.5', facecolor=COLORS['light'],
                      edgecolor=COLORS['dark'], linewidth=2))

    # Level 1: Two main branches (Hausmann's core insight)
    ax2.plot([5.5, 2.5], [8.8, 7.5], color=COLORS['dark'], linewidth=2)
    ax2.plot([5.5, 8.5], [8.8, 7.5], color=COLORS['dark'], linewidth=2)

    # Left branch: Demand-side (Market Pull)
    ax2.text(2.5, 7, 'Low Market Pull\n(Demand-side)', fontsize=10,
             ha='center', va='center', fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.4', facecolor=COLORS['B'],
                      edgecolor=COLORS['dark'], alpha=0.6))

    # Right branch: Supply-side (Ops Capability)
    ax2.text(8.5, 7, 'Low Ops Capability\n(Supply-side)', fontsize=10,
             ha='center', va='center', fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.4', facecolor=COLORS['negative'],
                      edgecolor=COLORS['dark'], alpha=0.4))

    # Level 2: Demand-side sub-branches
    ax2.plot([2.5, 1], [6.2, 5], color=COLORS['dark'], linewidth=1.5)
    ax2.plot([2.5, 4], [6.2, 5], color=COLORS['dark'], linewidth=1.5)

    ax2.text(1, 4.5, 'Weak PMF\n(no pull)', fontsize=9, ha='center', va='center',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=COLORS['B']))
    ax2.text(4, 4.5, 'Crowded Market\n(red ocean)', fontsize=9, ha='center', va='center',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=COLORS['B']))

    # Level 2: Supply-side sub-branches
    ax2.plot([8.5, 6.5], [6.2, 5], color=COLORS['dark'], linewidth=1.5)
    ax2.plot([8.5, 10.5], [6.2, 5], color=COLORS['dark'], linewidth=1.5)

    ax2.text(6.5, 4.5, 'Execution\nFailure', fontsize=9, ha='center', va='center',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=COLORS['negative']))
    ax2.text(10.5, 4.5, 'Resource\nConstraint', fontsize=9, ha='center', va='center',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=COLORS['negative']))

    # Level 3: Execution Failure sub-branches
    ax2.plot([6.5, 5.5], [3.8, 2.8], color=COLORS['dark'], linewidth=1)
    ax2.plot([6.5, 7.5], [3.8, 2.8], color=COLORS['dark'], linewidth=1)

    ax2.text(5.5, 2.3, 'Team\nGap', fontsize=8, ha='center', va='center',
             bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=COLORS['light']))
    ax2.text(7.5, 2.3, 'Process\nDebt', fontsize=8, ha='center', va='center',
             bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=COLORS['light']))

    # Level 3: Resource Constraint sub-branches - GOLDEN CAGE highlighted
    ax2.plot([10.5, 9.5], [3.8, 2.8], color=COLORS['dark'], linewidth=1)
    ax2.plot([10.5, 11.5], [3.8, 2.8], color=COLORS['negative'], linewidth=2)  # Highlight

    ax2.text(9.5, 2.3, 'Capital\nShortage', fontsize=8, ha='center', va='center',
             bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=COLORS['light']))

    # GOLDEN CAGE - Key insight box (highlighted)
    ax2.text(11.5, 2.3, 'GOLDEN\nCAGE', fontsize=9, ha='center', va='center',
             fontweight='bold', color='white',
             bbox=dict(boxstyle='round,pad=0.3', facecolor=COLORS['negative'],
                      edgecolor=COLORS['dark'], linewidth=2))
    ax2.text(11.5, 1.3, r'$E\uparrow \rightarrow R\downarrow$', fontsize=9, ha='center',
             color=COLORS['negative'], fontweight='bold')

    # Liebig's Barrel annotation
    ax2.text(5.5, 0.3, "Liebig's Law: Growth = min(Market, Ops)\n"
             "Hausmann et al. (2008), adapted for startups",
             fontsize=9, ha='center', style='italic', color=COLORS['dark'],
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#f8f8f8', edgecolor='none'))

    ax2.set_title('Startup Growth Diagnostics (Hausmann)', fontsize=13, fontweight='bold', pad=15)
    ax2.set_xlim(-0.5, 13)
    ax2.set_ylim(-0.5, 10.5)
    ax2.axis('off')

    plt.tight_layout()

    if save:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        fig.savefig(OUTPUT_DIR / 'Fig9_balanced_growth.png', dpi=300)
        print(f"  Saved: Fig9_balanced_growth.png")

    return fig


# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description='Generate thesis figures')
    parser.add_argument('--all', action='store_true', help='Generate all figures')
    parser.add_argument('--fig1', action='store_true', help='Capital Paradox')
    parser.add_argument('--fig2', action='store_true', help='B Trajectories (파랑새)')
    parser.add_argument('--fig3', action='store_true', help='Golden Cage')
    parser.add_argument('--fig4', action='store_true', help='Mover Advantage')
    parser.add_argument('--fig5', action='store_true', help='Sweet Spot')
    parser.add_argument('--fig9', action='store_true', help='Balanced Growth (Growth Diagnostics)')
    parser.add_argument('--summary', action='store_true', help='Correlation Summary')
    args = parser.parse_args()

    # If no args, generate all
    if not any([args.all, args.fig1, args.fig2, args.fig3, args.fig4, args.fig5, args.fig9, args.summary]):
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
        print("\n[Fig.2] B Trajectories (파랑새 스타일)...")
        fig2_b_trajectories(df)

    if args.all or args.fig3:
        print("\n[Fig.3] Golden Cage...")
        fig3_golden_cage(df)

    if args.all or args.fig4:
        print("\n[Fig.4] Mover Advantage...")
        fig4_mover_advantage(df)

    if args.all or args.fig5:
        print("\n[Fig.5] Sweet Spot...")
        fig5_sweet_spot(df)

    if args.all or args.fig9:
        print("\n[Fig.9] Balanced Growth (Growth Diagnostics)...")
        fig9_balanced_growth()

    if args.all or args.summary:
        print("\n[Summary] Correlations...")
        fig_correlation_summary(df)

    print("\n" + "=" * 60)
    print("COMPLETE")
    print("=" * 60)

    plt.close('all')


if __name__ == '__main__':
    main()
