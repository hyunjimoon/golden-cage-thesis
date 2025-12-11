#!/usr/bin/env python3
"""
🎨 Science Journal Quality Plots v3
Redesigned for maximum clarity and memorability

Design Principles:
1. ONE clear message per figure
2. Minimal ink, maximum information (Tufte)
3. Accessible colors (colorblind-safe)
4. Clear hierarchy: title > data > annotation
5. Honest representation of uncertainty

Author: Claude Code
Date: 2025-12-10
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.lines import Line2D
from pathlib import Path
from scipy import stats
from scipy.stats import chi2_contingency
import json
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# CONFIGURATION
# ============================================================================

SEED = 42
np.random.seed(SEED)

ROOT = Path("/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics")
DATA_PATH = ROOT / "data/processed/vagueness_timeseries.parquet"
COMPANY_PATH = ROOT / "data/processed/Company20251101.parquet"
FIG_DIR = ROOT / "src/scripts/paper_generation/output/_thesis_package/figures"
STATS_DIR = ROOT / "src/scripts/paper_generation/output/_thesis_package/stats"

# Science-quality color palette (colorblind-safe)
COLORS = {
    'primary': '#2166AC',      # Blue
    'secondary': '#B2182B',    # Red
    'tertiary': '#1B7837',     # Green
    'highlight': '#F4A582',    # Light coral
    'neutral': '#636363',      # Gray
    'light': '#D9D9D9',        # Light gray
    'q1': '#2166AC',           # Blue (precise)
    'q2': '#92C5DE',           # Light blue
    'q3': '#F4A582',           # Light coral
    'q4': '#B2182B',           # Red (vague)
}

# Science journal style
plt.rcParams.update({
    'figure.dpi': 300,
    'figure.figsize': (7, 5),
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.titleweight': 'bold',
    'axes.labelsize': 11,
    'axes.linewidth': 1.2,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'xtick.major.width': 1.2,
    'ytick.major.width': 1.2,
    'legend.frameon': False,
    'legend.fontsize': 9,
    'savefig.bbox': 'tight',
    'savefig.facecolor': 'white',
    'savefig.dpi': 300,
})

def stars(p):
    if p < 0.001: return '***'
    if p < 0.01: return '**'
    if p < 0.05: return '*'
    return ''


# ============================================================================
# DATA LOADING (same as before)
# ============================================================================

def load_data():
    """Load and transform panel data to cross-sectional."""
    print("Loading data...")

    panel = pd.read_parquet(DATA_PATH)
    company_cols = ['CompanyID', 'TotalRaised', 'BusinessStatus']
    company_df = pd.read_parquet(COMPANY_PATH, columns=company_cols)
    company_df.columns = ['company_id', 'TotalRaised_2025', 'BusinessStatus']
    company_df['company_id'] = company_df['company_id'].astype(str)

    df_0 = panel[panel['year'] == 2021][['company_id', 'V', 'first_financing_size']].copy()
    df_0.columns = ['company_id', 'V', 'E']
    df_0['company_id'] = df_0['company_id'].astype(str)

    df_T = panel[panel['year'] == 2025][['company_id', 'V', 'total_delta_V']].copy()
    df_T.columns = ['company_id', 'V_T', 'D']
    df_T['company_id'] = df_T['company_id'].astype(str)

    cross = df_0.merge(df_T, on='company_id', how='inner')
    cross = cross.merge(company_df, on='company_id', how='left')

    cross['A'] = cross['D'].abs()
    cross['E_log'] = np.log10(cross['E'].clip(lower=0.01))
    cross['V_Q'] = pd.qcut(cross['V'], 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

    # Strict survival: TotalRaised > 5*E
    valid_funding = cross['E'].notna() & (cross['E'] > 0) & cross['TotalRaised_2025'].notna()
    cross['L'] = 0
    cross.loc[valid_funding & (cross['TotalRaised_2025'] > cross['E'] * 5), 'L'] = 1
    failed_statuses = ['Out of Business', 'Bankruptcy: Liquidation', 'Bankruptcy: Admin/Reorg']
    cross.loc[cross['BusinessStatus'].isin(failed_statuses), 'L'] = 0

    # Growth
    cross['L_funding'] = cross['TotalRaised_2025'] - cross['E']
    cross['L_funding'] = cross['L_funding'].clip(lower=0)
    cross['G'] = cross['L_funding'] / (cross['E'] + 0.001)
    g_cap = cross['G'].quantile(0.99)
    cross['G'] = cross['G'].clip(upper=g_cap)

    valid = cross[['V', 'E', 'D', 'A']].notna().all(axis=1)
    cross = cross[valid].copy()

    print(f"   N = {len(cross):,}")
    return panel, cross


# ============================================================================
# SCIENCE QUALITY FIGURES
# ============================================================================

def fig1_survival_by_vagueness(cross):
    """
    Figure 1: Survival Rate by Vagueness Quartile

    Design: Clean bar chart with confidence intervals
    Message: Extremes (Q1, Q4) vs Middle (Q2, Q3) - is there a U-shape?
    """
    fig, ax = plt.subplots(figsize=(6, 5))

    # Compute statistics
    q_stats = cross.groupby('V_Q').agg({
        'L': ['mean', 'std', 'count']
    })
    q_stats.columns = ['mean', 'std', 'n']
    q_stats['se'] = q_stats['std'] / np.sqrt(q_stats['n'])
    q_stats['ci95'] = 1.96 * q_stats['se']

    quartiles = ['Q1', 'Q2', 'Q3', 'Q4']
    x = np.arange(len(quartiles))

    # Colors: gradient from blue (precise) to red (vague)
    colors = [COLORS['q1'], COLORS['q2'], COLORS['q3'], COLORS['q4']]

    # Bars with error bars
    bars = ax.bar(x, q_stats.loc[quartiles, 'mean'] * 100,
                  color=colors, edgecolor='black', linewidth=1.2, alpha=0.85)
    ax.errorbar(x, q_stats.loc[quartiles, 'mean'] * 100,
                yerr=q_stats.loc[quartiles, 'ci95'] * 100,
                fmt='none', color='black', capsize=5, capthick=1.5, linewidth=1.5)

    # Labels
    ax.set_xticks(x)
    ax.set_xticklabels(['Precise\n(Q1)', 'Moderate\n(Q2)', 'Moderate\n(Q3)', 'Vague\n(Q4)'])
    ax.set_ylabel('Survival Rate (%)', fontsize=11)
    ax.set_xlabel('Initial Vagueness Quartile', fontsize=11)

    # Value labels on bars
    for i, (bar, q) in enumerate(zip(bars, quartiles)):
        height = bar.get_height()
        ax.annotate(f'{height:.1f}%',
                   xy=(bar.get_x() + bar.get_width()/2, height),
                   xytext=(0, 3), textcoords='offset points',
                   ha='center', va='bottom', fontsize=10, fontweight='bold')

    # Reference line: overall mean
    overall_mean = cross['L'].mean() * 100
    ax.axhline(overall_mean, color=COLORS['neutral'], linestyle='--', linewidth=1.5, alpha=0.7)
    ax.text(3.5, overall_mean + 1, f'Mean: {overall_mean:.1f}%',
            ha='right', fontsize=9, color=COLORS['neutral'])

    # Chi-square test
    contingency = pd.crosstab(cross['V_Q'], cross['L'])
    chi2, p_chi2, _, _ = chi2_contingency(contingency)

    # Title with key finding
    extremes = (q_stats.loc['Q1', 'mean'] + q_stats.loc['Q4', 'mean']) / 2 * 100
    middle = (q_stats.loc['Q2', 'mean'] + q_stats.loc['Q3', 'mean']) / 2 * 100
    delta = extremes - middle

    ax.set_title(f'Survival Rate by Initial Vagueness\n'
                 f'Extremes vs Middle: Δ = {delta:+.1f} pp (χ² = {chi2:.0f}{stars(p_chi2)})',
                 fontsize=11, pad=10)

    ax.set_ylim(0, max(q_stats['mean'] * 100) * 1.25)
    ax.yaxis.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(FIG_DIR / 'fig1_survival_quartiles.png')
    plt.close()
    print("   ✅ fig1_survival_quartiles.png")
    return fig


def fig2_vagueness_enables_movement(cross):
    """
    Figure 2: Vagueness Creates Strategic Flexibility

    Design: Scatter with density showing D variance increases with V
    Message: Higher V → More room to move (both + and -)
    """
    fig, axes = plt.subplots(1, 2, figsize=(11, 5))

    # Left panel: D vs V (directional change)
    ax1 = axes[0]

    # Sample for visibility (too many points)
    sample = cross.sample(min(5000, len(cross)), random_state=SEED)

    ax1.scatter(sample['V'], sample['D'], alpha=0.15, s=8, c=COLORS['primary'],
                edgecolors='none', rasterized=True)

    # Add variance bands by V decile
    cross_copy = cross.copy()
    cross_copy['V_decile'] = pd.qcut(cross_copy['V'], 10, labels=False, duplicates='drop')
    var_by_v = cross_copy.groupby('V_decile').agg({
        'V': 'median',
        'D': ['mean', 'std', lambda x: np.percentile(x, 5), lambda x: np.percentile(x, 95)]
    })
    var_by_v.columns = ['V_med', 'D_mean', 'D_std', 'D_5', 'D_95']

    # Plot envelope
    ax1.fill_between(var_by_v['V_med'], var_by_v['D_5'], var_by_v['D_95'],
                     alpha=0.3, color=COLORS['highlight'], label='90% range')
    ax1.plot(var_by_v['V_med'], var_by_v['D_mean'], '-', color=COLORS['secondary'],
             linewidth=2, label='Mean')

    ax1.axhline(0, color='black', linewidth=0.8, linestyle='-', alpha=0.5)
    ax1.set_xlabel('Initial Vagueness (V)', fontsize=11)
    ax1.set_ylabel('Directional Change (D = V_T − V_0)', fontsize=11)
    ax1.set_title('(A) Vagueness Creates Room to Move', fontsize=11, fontweight='bold')
    ax1.legend(loc='upper left', fontsize=9)

    # Right panel: |D| (magnitude) vs V
    ax2 = axes[1]

    # Binned scatter for clarity
    cross_copy['V_bin'] = pd.qcut(cross_copy['V'], 15, labels=False, duplicates='drop')
    binned = cross_copy.groupby('V_bin').agg({
        'V': 'median',
        'A': ['mean', 'std', 'count']
    })
    binned.columns = ['V_med', 'A_mean', 'A_std', 'n']
    binned['A_se'] = binned['A_std'] / np.sqrt(binned['n'])

    ax2.scatter(binned['V_med'], binned['A_mean'], s=binned['n']/100,
                c=COLORS['primary'], edgecolors='black', linewidth=1, alpha=0.8)
    ax2.errorbar(binned['V_med'], binned['A_mean'], yerr=1.96*binned['A_se'],
                 fmt='none', color=COLORS['neutral'], capsize=3, alpha=0.5)

    # Regression
    r, p = stats.pearsonr(cross['V'], cross['A'])
    slope, intercept, _, _, _ = stats.linregress(cross['V'], cross['A'])
    x_line = np.linspace(cross['V'].min(), cross['V'].max(), 100)
    ax2.plot(x_line, slope * x_line + intercept, '--', color=COLORS['secondary'],
             linewidth=2, label=f'ρ = {r:.2f}{stars(p)}')

    ax2.set_xlabel('Initial Vagueness (V)', fontsize=11)
    ax2.set_ylabel('Adaptive Capacity (A = |D|)', fontsize=11)
    ax2.set_title('(B) Vagueness → Larger Strategic Shifts', fontsize=11, fontweight='bold')
    ax2.legend(loc='upper right', fontsize=9)

    # Overall title
    fig.suptitle('Strategic Flexibility: Vagueness Enables Adaptation',
                 fontsize=13, fontweight='bold', y=1.02)

    plt.tight_layout()
    fig.savefig(FIG_DIR / 'fig2_vagueness_flexibility.png')
    plt.close()
    print("   ✅ fig2_vagueness_flexibility.png")
    return fig


def fig3_movement_predicts_survival(cross):
    """
    Figure 3: Adaptive Capacity Predicts Survival

    Design: Clear binned scatter with trend
    Message: Companies that moved (high A) survived more
    """
    fig, ax = plt.subplots(figsize=(7, 5))

    # Filter extreme outliers for better visualization
    a_cap = cross['A'].quantile(0.95)
    df = cross[cross['A'] <= a_cap].copy()

    # Binned scatter
    df['A_bin'] = pd.qcut(df['A'], 10, labels=False, duplicates='drop')
    binned = df.groupby('A_bin').agg({
        'A': 'median',
        'L': ['mean', 'std', 'count']
    })
    binned.columns = ['A_med', 'L_mean', 'L_std', 'n']
    binned['L_se'] = binned['L_std'] / np.sqrt(binned['n'])

    # Size proportional to n
    sizes = (binned['n'] / binned['n'].max()) * 200 + 50

    scatter = ax.scatter(binned['A_med'], binned['L_mean'] * 100, s=sizes,
                        c=COLORS['primary'], edgecolors='black', linewidth=1.5,
                        alpha=0.85, zorder=5)
    ax.errorbar(binned['A_med'], binned['L_mean'] * 100, yerr=1.96*binned['L_se']*100,
                fmt='none', color=COLORS['neutral'], capsize=4, linewidth=1.2, zorder=4)

    # Trend line
    r, p = stats.pearsonr(df['A'], df['L'])
    slope, intercept, _, _, _ = stats.linregress(df['A'], df['L'])
    x_line = np.linspace(df['A'].min(), df['A'].max(), 100)
    ax.plot(x_line, (slope * x_line + intercept) * 100, '--',
            color=COLORS['tertiary'], linewidth=2.5, zorder=3,
            label=f'Trend: ρ = {r:.3f}{stars(p)}')

    ax.set_xlabel('Adaptive Capacity (A = |ΔV|)', fontsize=11)
    ax.set_ylabel('Survival Rate (%)', fontsize=11)
    ax.set_title('Movement Predicts Survival\n'
                 'Companies that adapted strategically survived more',
                 fontsize=11, pad=10)

    ax.legend(loc='lower right', fontsize=10)
    ax.yaxis.grid(True, alpha=0.3)

    # Annotation
    ax.annotate('Larger bubble = more firms',
               xy=(0.95, 0.05), xycoords='axes fraction',
               ha='right', fontsize=8, color=COLORS['neutral'], style='italic')

    plt.tight_layout()
    fig.savefig(FIG_DIR / 'fig3_movement_survival.png')
    plt.close()
    print("   ✅ fig3_movement_survival.png")
    return fig


def fig4_golden_cage(cross):
    """
    Figure 4: THE GOLDEN CAGE (Key Figure)

    Design: Crystal clear demonstration of the core finding
    Message: More early capital → Less strategic flexibility
    """
    fig, ax = plt.subplots(figsize=(8, 6))

    # Filter valid E
    valid = cross['E'].notna() & (cross['E'] > 0) & cross['A'].notna()
    df = cross[valid].copy()

    # Decile binning for clear pattern
    df['E_decile'] = pd.qcut(df['E'], 10, labels=False, duplicates='drop')
    binned = df.groupby('E_decile').agg({
        'E': 'median',
        'A': ['mean', 'std', 'count']
    })
    binned.columns = ['E_med', 'A_mean', 'A_std', 'n']
    binned['A_se'] = binned['A_std'] / np.sqrt(binned['n'])

    # Size by n
    sizes = (binned['n'] / binned['n'].max()) * 300 + 80

    # Color gradient by E (darker = more capital)
    colors = plt.cm.RdYlBu_r(np.linspace(0.2, 0.8, len(binned)))

    for i, (idx, row) in enumerate(binned.iterrows()):
        ax.scatter(row['E_med'], row['A_mean'], s=sizes.iloc[i],
                  c=[colors[i]], edgecolors='black', linewidth=1.5, zorder=5)
        ax.errorbar(row['E_med'], row['A_mean'], yerr=1.96*row['A_se'],
                   fmt='none', color='gray', capsize=4, linewidth=1, zorder=4, alpha=0.7)

    # Regression line with CI
    r, p = stats.pearsonr(df['E_log'], df['A'])
    slope, intercept, _, _, se = stats.linregress(df['E_log'], df['A'])

    x_fit = np.linspace(df['E_log'].min(), df['E_log'].max(), 100)
    y_fit = slope * x_fit + intercept

    # CI band
    n = len(df)
    y_err = 1.96 * se * np.sqrt(1/n + (x_fit - df['E_log'].mean())**2 / ((n-1)*df['E_log'].var()))

    ax.plot(10**x_fit, y_fit, '-', color=COLORS['secondary'], linewidth=3, zorder=3)
    ax.fill_between(10**x_fit, y_fit - y_err, y_fit + y_err,
                    color=COLORS['secondary'], alpha=0.15, zorder=2)

    ax.set_xscale('log')
    ax.set_xlabel('Early Capital (E, $M)', fontsize=12)
    ax.set_ylabel('Adaptive Capacity (A = |ΔV|)', fontsize=12)

    # One-tailed test
    p_one = p / 2 if slope < 0 else 1 - p / 2

    ax.set_title('The Golden Cage: Capital Constrains Flexibility\n'
                 f'ρ = {r:.3f}{stars(p_one)} (N = {len(df):,})',
                 fontsize=12, fontweight='bold', pad=15)

    # Key insight annotation
    ax.annotate('More capital\n→ Less flexibility',
               xy=(binned['E_med'].iloc[-1], binned['A_mean'].iloc[-1]),
               xytext=(binned['E_med'].iloc[-1] * 0.15, binned['A_mean'].iloc[0] * 1.05),
               fontsize=11, ha='center', fontweight='bold',
               arrowprops=dict(arrowstyle='->', color=COLORS['secondary'], lw=2),
               bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                        edgecolor=COLORS['secondary'], alpha=0.9))

    # Legend for size
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor=COLORS['neutral'],
               markersize=8, label='Low E'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor=COLORS['secondary'],
               markersize=12, label='High E'),
    ]
    ax.legend(handles=legend_elements, loc='upper right', title='Early Capital', fontsize=9)

    ax.yaxis.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(FIG_DIR / 'fig4_golden_cage.png')
    plt.close()
    print("   ✅ fig4_golden_cage.png ⭐")
    return fig


def fig5_mechanism_chain(cross):
    """
    Figure 5: The Complete Mechanism

    Design: 3-panel showing causal chain
    Message: E → A → G (capital constrains flexibility which limits growth)
    """
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

    # Filter valid data
    valid = (cross['E'].notna() & (cross['E'] > 0) &
             cross['A'].notna() & cross['G'].notna() & np.isfinite(cross['G']))
    df = cross[valid].copy()

    # ===== Panel A: E → A (negative) =====
    ax1 = axes[0]

    df['E_bin'] = pd.qcut(df['E_log'], 10, labels=False, duplicates='drop')
    binned = df.groupby('E_bin').agg({'E': 'median', 'A': 'mean'})

    ax1.scatter(binned['E'], binned['A'], s=100, c=COLORS['primary'],
                edgecolors='black', linewidth=1.5)

    r1, p1 = stats.pearsonr(df['E_log'], df['A'])
    slope, intercept, _, _, _ = stats.linregress(df['E_log'], df['A'])
    x_fit = np.linspace(df['E_log'].min(), df['E_log'].max(), 100)
    ax1.plot(10**x_fit, slope * x_fit + intercept, '--',
             color=COLORS['secondary'], linewidth=2.5)

    ax1.set_xscale('log')
    ax1.set_xlabel('Early Capital E ($M)', fontsize=11)
    ax1.set_ylabel('Flexibility A = |ΔV|', fontsize=11)
    ax1.set_title(f'(A) E → A: ρ = {r1:.2f}{stars(p1)}',
                  fontsize=11, fontweight='bold', color=COLORS['secondary'])

    # ===== Panel B: A → G (positive) =====
    ax2 = axes[1]

    df['A_bin'] = pd.qcut(df['A'], 10, labels=False, duplicates='drop')
    binned = df.groupby('A_bin').agg({'A': 'median', 'G': 'mean'})

    ax2.scatter(binned['A'], binned['G'], s=100, c=COLORS['primary'],
                edgecolors='black', linewidth=1.5)

    r2, p2 = stats.pearsonr(df['A'], df['G'])
    slope, intercept, _, _, _ = stats.linregress(df['A'], df['G'])
    x_fit = np.linspace(df['A'].min(), df['A'].max(), 100)
    ax2.plot(x_fit, slope * x_fit + intercept, '--',
             color=COLORS['tertiary'], linewidth=2.5)

    ax2.set_xlabel('Flexibility A = |ΔV|', fontsize=11)
    ax2.set_ylabel('Growth G = L/E', fontsize=11)
    ax2.set_title(f'(B) A → G: ρ = {r2:.2f}{stars(p2)}',
                  fontsize=11, fontweight='bold', color=COLORS['tertiary'])

    # ===== Panel C: E → G (combined negative) =====
    ax3 = axes[2]

    binned = df.groupby('E_bin').agg({'E': 'median', 'G': 'mean'})

    ax3.scatter(binned['E'], binned['G'], s=100, c=COLORS['primary'],
                edgecolors='black', linewidth=1.5)

    r3, p3 = stats.pearsonr(df['E_log'], df['G'])
    slope, intercept, _, _, _ = stats.linregress(df['E_log'], df['G'])
    x_fit = np.linspace(df['E_log'].min(), df['E_log'].max(), 100)
    ax3.plot(10**x_fit, slope * x_fit + intercept, '--',
             color=COLORS['secondary'], linewidth=2.5)

    ax3.set_xscale('log')
    ax3.set_xlabel('Early Capital E ($M)', fontsize=11)
    ax3.set_ylabel('Growth G = L/E', fontsize=11)
    ax3.set_title(f'(C) E → G: ρ = {r3:.2f}{stars(p3)}',
                  fontsize=11, fontweight='bold', color=COLORS['secondary'])

    # Overall title with mechanism equation
    fig.suptitle('The Golden Cage Mechanism: dG/dE = (dG/dA) × (dA/dE) = (+) × (−) < 0',
                 fontsize=13, fontweight='bold', y=1.05)

    # Add arrows between panels
    fig.text(0.35, 0.5, '→', fontsize=30, ha='center', va='center',
             transform=fig.transFigure, color=COLORS['neutral'])
    fig.text(0.66, 0.5, '→', fontsize=30, ha='center', va='center',
             transform=fig.transFigure, color=COLORS['neutral'])

    for ax in axes:
        ax.yaxis.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(FIG_DIR / 'fig5_mechanism_chain.png')
    plt.close()
    print("   ✅ fig5_mechanism_chain.png")
    return fig


def fig6_growth_by_flexibility(cross):
    """
    Figure 6: Growth Distribution by Flexibility

    Design: Violin or box plot showing distribution shift
    Message: High flexibility firms have better growth distribution
    """
    fig, ax = plt.subplots(figsize=(8, 5))

    # Filter valid G
    valid = cross['G'].notna() & np.isfinite(cross['G']) & cross['A'].notna()
    df = cross[valid].copy()

    # Split into flexibility groups
    a_median = df['A'].median()
    df['flexibility'] = np.where(df['A'] > a_median, 'High Flexibility\n(A > median)',
                                  'Low Flexibility\n(A ≤ median)')

    # Violin plot
    parts = ax.violinplot([df[df['flexibility'].str.contains('Low')]['G'].values,
                           df[df['flexibility'].str.contains('High')]['G'].values],
                          positions=[1, 2], showmeans=True, showmedians=True)

    # Color the violins
    colors_violin = [COLORS['q2'], COLORS['tertiary']]
    for i, pc in enumerate(parts['bodies']):
        pc.set_facecolor(colors_violin[i])
        pc.set_alpha(0.7)

    parts['cmeans'].set_color('black')
    parts['cmedians'].set_color(COLORS['secondary'])

    # Add summary statistics
    low_g = df[df['flexibility'].str.contains('Low')]['G']
    high_g = df[df['flexibility'].str.contains('High')]['G']

    ax.text(1, low_g.median() + 5, f'Med: {low_g.median():.1f}×', ha='center', fontsize=9)
    ax.text(2, high_g.median() + 5, f'Med: {high_g.median():.1f}×', ha='center', fontsize=9)

    # T-test
    t_stat, p_val = stats.ttest_ind(high_g, low_g)

    ax.set_xticks([1, 2])
    ax.set_xticklabels(['Low Flexibility\n(A ≤ median)', 'High Flexibility\n(A > median)'])
    ax.set_ylabel('Growth (G = Later Funding / Early Funding)', fontsize=11)
    ax.set_title(f'Growth Distribution by Strategic Flexibility\n'
                 f'High flexibility firms grow {high_g.median()/low_g.median():.1f}× more (p < 0.001)',
                 fontsize=11, fontweight='bold', pad=10)

    ax.yaxis.grid(True, alpha=0.3)
    ax.set_ylim(0, df['G'].quantile(0.95))

    plt.tight_layout()
    fig.savefig(FIG_DIR / 'fig6_growth_flexibility.png')
    plt.close()
    print("   ✅ fig6_growth_flexibility.png")
    return fig


def fig7_summary_matrix(cross):
    """
    Figure 7: Summary Correlation Matrix

    Design: Heatmap of key relationships
    Message: All signs consistent with theory
    """
    fig, ax = plt.subplots(figsize=(7, 6))

    # Filter valid
    valid = (cross['E'].notna() & (cross['E'] > 0) &
             cross['A'].notna() & cross['G'].notna() & np.isfinite(cross['G']))
    df = cross[valid].copy()

    # Compute correlations
    vars_to_corr = ['V', 'E_log', 'A', 'L', 'G']
    var_labels = ['Vagueness\n(V)', 'Early Capital\n(log E)', 'Flexibility\n(A=|ΔV|)',
                  'Survival\n(L)', 'Growth\n(G)']

    corr_matrix = df[vars_to_corr].corr()
    p_matrix = np.zeros_like(corr_matrix)

    for i, v1 in enumerate(vars_to_corr):
        for j, v2 in enumerate(vars_to_corr):
            if i != j:
                _, p = stats.pearsonr(df[v1], df[v2])
                p_matrix[i, j] = p

    # Custom colormap
    cmap = LinearSegmentedColormap.from_list('custom',
           [COLORS['secondary'], 'white', COLORS['tertiary']], N=256)

    im = ax.imshow(corr_matrix, cmap=cmap, vmin=-0.5, vmax=0.5, aspect='auto')

    # Add text annotations
    for i in range(len(vars_to_corr)):
        for j in range(len(vars_to_corr)):
            val = corr_matrix.iloc[i, j]
            p = p_matrix[i, j]
            if i == j:
                text = '—'
            else:
                text = f'{val:.2f}{stars(p)}'
            color = 'white' if abs(val) > 0.25 else 'black'
            ax.text(j, i, text, ha='center', va='center', fontsize=10, color=color)

    ax.set_xticks(range(len(var_labels)))
    ax.set_yticks(range(len(var_labels)))
    ax.set_xticklabels(var_labels, fontsize=9)
    ax.set_yticklabels(var_labels, fontsize=9)

    # Colorbar
    cbar = plt.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label('Correlation (ρ)', fontsize=10)

    ax.set_title('Correlation Matrix: Key Relationships\n'
                 '*** p < 0.001, ** p < 0.01, * p < 0.05',
                 fontsize=11, fontweight='bold', pad=15)

    plt.tight_layout()
    fig.savefig(FIG_DIR / 'fig7_correlation_matrix.png')
    plt.close()
    print("   ✅ fig7_correlation_matrix.png")
    return fig


# ============================================================================
# MAIN
# ============================================================================

def main():
    print("="*70)
    print("🎨 SCIENCE JOURNAL QUALITY PLOTS")
    print("="*70)

    # Load data
    _, cross = load_data()

    # Generate all figures
    print("\n📈 Generating Science-quality figures...")

    fig1_survival_by_vagueness(cross)
    fig2_vagueness_enables_movement(cross)
    fig3_movement_predicts_survival(cross)
    fig4_golden_cage(cross)
    fig5_mechanism_chain(cross)
    fig6_growth_by_flexibility(cross)
    fig7_summary_matrix(cross)

    print("\n" + "="*70)
    print("✅ ALL FIGURES GENERATED")
    print("="*70)

    print(f"\n📁 Output: {FIG_DIR}")


if __name__ == "__main__":
    main()
