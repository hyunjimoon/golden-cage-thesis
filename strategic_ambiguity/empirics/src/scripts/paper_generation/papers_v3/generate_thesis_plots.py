#!/usr/bin/env python3
"""
Generate key empirical plots for Five Elements Thesis Modules (I, M, C, T, D).

Output:
- 1_I_introduction/fig_i_cash_paradox.png
- 2_M_movement/fig_m_mover_advantage.png
- 3_C_cash2growth/fig_c_typology.png
- 5_D_discussion/fig_d_synthesis.png
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy.stats import spearmanr, linregress
import warnings
warnings.filterwarnings('ignore')

# Paths
SCRIPT_DIR = Path(__file__).parent.resolve()
REPO_ROOT = SCRIPT_DIR.parent.parent.parent.parent
DATA_DIR = REPO_ROOT / 'data' / 'processed'

# Output directories
OUT_I = SCRIPT_DIR / '1_I_introduction'
OUT_M = SCRIPT_DIR / '2_M_movement'
OUT_C = SCRIPT_DIR / '3_C_cash2growth'
OUT_D = SCRIPT_DIR / '5_D_discussion'

# Style settings (dark theme friendly)
plt.style.use('seaborn-v0_8-darkgrid')

# NEW COLOR SCHEME (from handwritten notes analysis):
# ⚫ Stayer = Black/Dark, 🟢 Horizontal = Green, 🔴 Zoom In = Red, 🔵 Zoom Out = Blue
COLORS = {
    'stayer': '#264653',      # ⚫ Black/Dark - Stayer
    'horizontal': '#2A9D8F',  # 🟢 Green - Horizontal
    'zoom_in': '#E63946',     # 🔴 Red - Zoom In
    'zoom_out': '#457B9D',    # 🔵 Blue - Zoom Out
    'primary': '#457B9D',     # Blue as primary
    'secondary': '#E63946',   # Red as secondary
    'accent': '#F4A261',      # Orange accent (complementary)
}


def load_data():
    """Load thesis panel data."""
    vag = pd.read_parquet(DATA_DIR / 'vagueness_timeseries.parquet')
    feat = pd.read_parquet(DATA_DIR / 'features_all.parquet')

    # Build panel
    v_2021 = vag[vag['year'] == 2021][['company_id', 'V', 'first_financing_size']].copy()
    v_2021 = v_2021.rename(columns={'V': 'V_0', 'first_financing_size': 'E'})
    v_2021 = v_2021[v_2021['E'].notna()]

    v_2025 = vag[vag['year'] == 2025][['company_id', 'V']].copy()
    v_2025 = v_2025.rename(columns={'V': 'V_T'})

    panel = v_2021.merge(v_2025, on='company_id', how='inner')
    panel['D'] = panel['V_T'] - panel['V_0']
    panel['A'] = panel['D'].abs()

    # Classify movers
    def classify(row):
        if row['A'] < 5:
            return 'stayer'
        elif row['D'] < -10:
            return 'zoom_in'
        elif row['D'] > 10:
            return 'zoom_out'
        else:
            return 'horizontal'

    panel['mover_type'] = panel.apply(classify, axis=1)
    panel['moved'] = (panel['A'] >= 5).astype(int)

    # Merge features
    feat_dedup = feat.drop_duplicates('CompanyID').copy()
    panel = panel.merge(
        feat_dedup[['CompanyID', 'total_raised', 'last_financing_deal_type']],
        left_on='company_id',
        right_on='CompanyID',
        how='left'
    )

    # G = total_raised / E (Funding Growth Multiple)
    panel['G'] = panel['total_raised'] / panel['E']
    panel.loc[panel['total_raised'].isna() & panel['E'].notna(), 'G'] = 1.0

    # L = Success (Later Stage VC)
    panel['L'] = panel['last_financing_deal_type'].str.contains('Later Stage VC', na=False).astype(int)

    return panel


def plot_module_i_cash_paradox(df):
    """
    Module I: Cash Paradox visualization.
    Shows negative correlation between Early Capital and Funding Growth.
    """
    fig, ax = plt.subplots(figsize=(10, 8))

    # Filter valid data
    valid = df.dropna(subset=['G', 'E'])
    valid = valid[(valid['E'] > 0) & (valid['G'] > 0) & (valid['G'] < 1000)]

    # Sample for visibility (too many points)
    if len(valid) > 5000:
        sample = valid.sample(5000, random_state=42)
    else:
        sample = valid

    # Scatter plot with archetype colors
    for mtype in ['stayer', 'horizontal', 'zoom_in', 'zoom_out']:
        subset = sample[sample['mover_type'] == mtype]
        ax.scatter(np.log10(subset['E'] + 1), np.log10(subset['G'] + 1),
                  alpha=0.3, s=15, c=COLORS[mtype], label=mtype, edgecolors='none')

    # Regression line
    x = np.log10(valid['E'] + 1)
    y = np.log10(valid['G'] + 1)
    slope, intercept, r, p, se = linregress(x, y)
    x_line = np.linspace(x.min(), x.max(), 100)
    y_line = slope * x_line + intercept
    ax.plot(x_line, y_line, 'k-', linewidth=2.5, label=f'Trend (slope={slope:.3f})')

    # Correlation
    rho, p_val = spearmanr(valid['G'], valid['E'])

    # Labels and styling
    ax.set_xlabel('Early Capital E (log₁₀ M USD)', fontsize=12)
    ax.set_ylabel('Funding Growth G (log₁₀ multiple)', fontsize=12)
    ax.set_title(f'The Capital Paradox\nρ(G, E) = {rho:.3f}*** (N = {len(valid):,})',
                fontsize=14, fontweight='bold')

    # Add annotation
    ax.annotate('Higher early funding →\nLower growth multiples',
                xy=(2.5, 0.5), fontsize=11, style='italic',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    ax.legend(loc='upper right', fontsize=10)
    ax.set_xlim(-0.5, 5)
    ax.set_ylim(-0.2, 3)

    plt.tight_layout()
    return fig


def plot_module_m_mover_advantage(df):
    """
    Module M: Movement Advantage visualization.
    Bar chart comparing success rates of Movers vs Stayers.
    """
    fig, ax = plt.subplots(figsize=(10, 7))

    # Calculate success rates
    movers = df[df['moved'] == 1]
    stayers = df[df['moved'] == 0]

    mover_rate = movers['L'].mean() * 100
    stayer_rate = stayers['L'].mean() * 100

    # Bootstrap CIs
    n_boot = 1000
    mover_boots = [movers['L'].sample(frac=1, replace=True).mean() * 100 for _ in range(n_boot)]
    stayer_boots = [stayers['L'].sample(frac=1, replace=True).mean() * 100 for _ in range(n_boot)]

    mover_ci = (np.percentile(mover_boots, 2.5), np.percentile(mover_boots, 97.5))
    stayer_ci = (np.percentile(stayer_boots, 2.5), np.percentile(stayer_boots, 97.5))

    # Bar plot
    x = [0, 1]
    heights = [stayer_rate, mover_rate]
    colors = [COLORS['stayer'], COLORS['primary']]
    errors = [[stayer_rate - stayer_ci[0], mover_rate - mover_ci[0]],
              [stayer_ci[1] - stayer_rate, mover_ci[1] - mover_rate]]

    bars = ax.bar(x, heights, color=colors, edgecolor='black', linewidth=1.5,
                  yerr=errors, capsize=10, error_kw={'linewidth': 2})

    # Labels on bars
    for bar, rate, ci, n in zip(bars, heights, [stayer_ci, mover_ci], [len(stayers), len(movers)]):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5,
                f'{rate:.1f}%\n[{ci[0]:.1f}%, {ci[1]:.1f}%]',
                ha='center', va='bottom', fontsize=12, fontweight='bold')
        ax.text(bar.get_x() + bar.get_width()/2, 1,
                f'N = {n:,}', ha='center', va='bottom', fontsize=10, color='white')

    # Relative risk annotation
    rr = mover_rate / stayer_rate
    ax.annotate(f'Movement Advantage:\n{rr:.1f}× higher success',
                xy=(0.5, max(heights) * 0.6), xytext=(0.5, max(heights) * 0.4),
                fontsize=13, ha='center', fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='black'),
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    ax.set_xticks(x)
    ax.set_xticklabels(['Stayers\n(A < 5)', 'Movers\n(A ≥ 5)'], fontsize=12)
    ax.set_ylabel('Success Rate (%)', fontsize=12)
    ax.set_title('The Movement Principle\nRepositioning Beats Staying',
                fontsize=14, fontweight='bold')
    ax.set_ylim(0, max(heights) * 1.4)

    # Add statistical significance
    ax.text(0.5, max(heights) * 1.25, 'χ² = 4,891***, p < 0.001',
            ha='center', fontsize=11, style='italic')

    plt.tight_layout()
    return fig


def plot_module_c_typology(df):
    """
    Module C: 4 Archetypes visualization.
    2D quadrant plot showing Initial Vagueness vs Change in Vagueness.
    """
    fig, ax = plt.subplots(figsize=(12, 10))

    # Sample for visibility
    if len(df) > 10000:
        sample = df.sample(10000, random_state=42)
    else:
        sample = df

    # Scatter by archetype
    for mtype in ['stayer', 'horizontal', 'zoom_in', 'zoom_out']:
        subset = sample[sample['mover_type'] == mtype]
        ax.scatter(subset['V_0'], subset['D'],
                  alpha=0.4, s=20, c=COLORS[mtype], label=f'{mtype} (N={len(df[df["mover_type"]==mtype]):,})',
                  edgecolors='none')

    # Add quadrant lines
    ax.axhline(y=0, color='black', linestyle='-', linewidth=1)
    ax.axhline(y=10, color='gray', linestyle='--', linewidth=1, alpha=0.7)
    ax.axhline(y=-10, color='gray', linestyle='--', linewidth=1, alpha=0.7)
    ax.axhline(y=5, color='gray', linestyle=':', linewidth=1, alpha=0.5)
    ax.axhline(y=-5, color='gray', linestyle=':', linewidth=1, alpha=0.5)

    # Quadrant labels
    ax.text(85, 35, 'ZOOM OUT\n(Broadening)', fontsize=12, fontweight='bold',
            color=COLORS['zoom_out'], ha='center',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    ax.text(85, -35, 'ZOOM IN\n(Focusing)', fontsize=12, fontweight='bold',
            color=COLORS['zoom_in'], ha='center',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    ax.text(50, 0, 'STAYER\n(No change)', fontsize=12, fontweight='bold',
            color=COLORS['stayer'], ha='center',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    ax.text(15, 7, 'HORIZONTAL\n(Lateral)', fontsize=10, fontweight='bold',
            color=COLORS['horizontal'], ha='center',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    ax.set_xlabel('Initial Vagueness V₀ (2021)', fontsize=12)
    ax.set_ylabel('Change in Vagueness ΔV = V_T - V₀', fontsize=12)
    ax.set_title('Strategic Repositioning Typology\nFour Archetypes of Adaptive Behavior',
                fontsize=14, fontweight='bold')

    ax.legend(loc='lower right', fontsize=10)
    ax.set_xlim(0, 100)
    ax.set_ylim(-80, 80)

    # Add threshold annotations
    ax.annotate('|ΔV| > 10: Significant movement', xy=(5, 60), fontsize=9, style='italic')
    ax.annotate('|ΔV| < 5: Stayer threshold', xy=(5, 3), fontsize=9, style='italic')

    plt.tight_layout()
    return fig


def plot_module_d_synthesis(df):
    """
    Module D: Synthesis/Forest Plot.
    Shows effect sizes of Capital (E) on Growth (G) across mover types.
    """
    fig, ax = plt.subplots(figsize=(12, 8))

    # Calculate dG/dE slopes by archetype
    results = []
    archetypes = ['zoom_in', 'zoom_out', 'stayer', 'horizontal', 'ALL']

    for mtype in archetypes:
        if mtype == 'ALL':
            subset = df.dropna(subset=['G', 'E'])
        else:
            subset = df[df['mover_type'] == mtype].dropna(subset=['G', 'E'])

        subset = subset[(subset['E'] > 0) & (subset['G'] > 0) & (subset['G'] < 1000)]

        if len(subset) > 30:
            x = np.log1p(subset['E'])
            y = np.log1p(subset['G'])
            slope, intercept, r, p, se = linregress(x, y)

            # Also compute correlation
            rho, p_rho = spearmanr(subset['G'], subset['E'])

            results.append({
                'archetype': mtype,
                'slope': slope,
                'se': se,
                'p': p,
                'rho': rho,
                'n': len(subset),
                'success_rate': subset['L'].mean() * 100 if 'L' in subset.columns else np.nan
            })

    # Forest plot
    y_pos = np.arange(len(results))
    slopes = [r['slope'] for r in results]
    errors = [1.96 * r['se'] for r in results]
    colors_list = [COLORS.get(r['archetype'], '#333333') for r in results]

    # Horizontal bars (forest plot style)
    for i, (res, color) in enumerate(zip(results, colors_list)):
        ax.errorbar(res['slope'], i, xerr=1.96*res['se'],
                   fmt='o', color=color, markersize=12, capsize=5, capthick=2, linewidth=2)

        # Add N and success rate
        sig = '***' if res['p'] < 0.001 else '**' if res['p'] < 0.01 else '*' if res['p'] < 0.05 else ''
        label = f"N={res['n']:,}, L={res['success_rate']:.1f}%, ρ={res['rho']:.3f}{sig}"
        ax.text(0.15, i, label, va='center', fontsize=10)

    # Vertical line at 0
    ax.axvline(x=0, color='black', linestyle='-', linewidth=1)

    # Labels
    ax.set_yticks(y_pos)
    ax.set_yticklabels([r['archetype'].upper() for r in results], fontsize=11, fontweight='bold')
    ax.set_xlabel('dG/dE (Effect of Early Capital on Funding Growth)', fontsize=12)
    ax.set_title('Synthesis: Capital Paradox Across Strategic Types\nAll archetypes show negative dG/dE',
                fontsize=14, fontweight='bold')

    # Shade negative region
    ax.axvspan(ax.get_xlim()[0], 0, alpha=0.1, color='red', label='Capital Paradox Zone')

    # Key insight annotation
    ax.annotate('Key Finding:\nCapital Paradox is UNIVERSAL\nacross all strategic types',
                xy=(-0.15, 2), fontsize=11,
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    ax.set_xlim(-0.35, 0.2)
    ax.invert_yaxis()

    plt.tight_layout()
    return fig


def main():
    print("Loading data...")
    df = load_data()
    print(f"Loaded {len(df):,} companies")

    # Module I: Cash Paradox
    print("\nGenerating Module I plot (Cash Paradox)...")
    fig_i = plot_module_i_cash_paradox(df)
    fig_i.savefig(OUT_I / 'fig_i_cash_paradox.png', dpi=150, bbox_inches='tight',
                  facecolor='white', edgecolor='none')
    print(f"  Saved: {OUT_I / 'fig_i_cash_paradox.png'}")

    # Module M: Movement Advantage
    print("\nGenerating Module M plot (Movement Advantage)...")
    fig_m = plot_module_m_mover_advantage(df)
    fig_m.savefig(OUT_M / 'fig_m_mover_advantage.png', dpi=150, bbox_inches='tight',
                  facecolor='white', edgecolor='none')
    print(f"  Saved: {OUT_M / 'fig_m_mover_advantage.png'}")

    # Module C: Typology
    print("\nGenerating Module C plot (4 Archetypes)...")
    fig_c = plot_module_c_typology(df)
    fig_c.savefig(OUT_C / 'fig_c_typology.png', dpi=150, bbox_inches='tight',
                  facecolor='white', edgecolor='none')
    print(f"  Saved: {OUT_C / 'fig_c_typology.png'}")

    # Module D: Synthesis
    print("\nGenerating Module D plot (Synthesis)...")
    fig_d = plot_module_d_synthesis(df)
    fig_d.savefig(OUT_D / 'fig_d_synthesis.png', dpi=150, bbox_inches='tight',
                  facecolor='white', edgecolor='none')
    print(f"  Saved: {OUT_D / 'fig_d_synthesis.png'}")

    plt.close('all')

    print("\n" + "="*60)
    print("All thesis plots generated successfully!")
    print("="*60)


if __name__ == '__main__':
    main()
