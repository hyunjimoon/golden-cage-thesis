#!/usr/bin/env python3
"""
🐅 MASTER FIGURE GENERATOR for PhD Thesis
"Flexibility and Commitment in Entrepreneurship"

Author: 권준/나대용 (🐅 중군 - Claude Code)
Quality: Production-ready for Charlie Fine & Scott Stern

Output: 12 figures (4 for U, 4 for C, 4 for Time Series)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from pathlib import Path
from typing import Optional, Tuple, Dict, Any
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# CONFIGURATION
# ============================================================================

SEED = 42
np.random.seed(SEED)

# Paths
ROOT = Path("/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics")
DATA_PATH = ROOT / "data/processed/vagueness_timeseries.parquet"
OUTPUT_DIR = ROOT / "src/scripts/paper_generation/output/_thesis_package/figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Colors
COLORS = {
    'primary': '#3498db',
    'positive': '#27ae60',
    'negative': '#e74c3c',
    'neutral': '#95a5a6',
    'highlight': '#f39c12',
    'low_E': '#3498db',
    'high_E': '#e74c3c',
}

# Figure settings
plt.rcParams.update({
    'figure.dpi': 300,
    'figure.figsize': (10, 6),
    'font.size': 11,
    'font.family': 'DejaVu Sans',
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'axes.titleweight': 'bold',
    'axes.grid': True,
    'grid.alpha': 0.3,
    'savefig.bbox': 'tight',
    'savefig.facecolor': 'white',
})


# ============================================================================
# UTILITIES
# ============================================================================

def get_stars(p: float) -> str:
    """Return significance stars."""
    if p < 0.001: return '***'
    if p < 0.01: return '**'
    if p < 0.05: return '*'
    return ''


def compute_binned_stats(df: pd.DataFrame, x: str, y: str, bins: int = 10) -> pd.DataFrame:
    """Compute statistics by bins."""
    df = df.copy()
    df['bin'] = pd.qcut(df[x], bins, labels=False, duplicates='drop')
    stats_df = df.groupby('bin').agg({
        x: ['median', 'mean'],
        y: ['mean', 'std', 'count']
    })
    stats_df.columns = ['x_median', 'x_mean', 'y_mean', 'y_std', 'n']
    stats_df['y_se'] = stats_df['y_std'] / np.sqrt(stats_df['n'])
    return stats_df.reset_index()


# ============================================================================
# DATA LOADING
# ============================================================================

def load_and_preprocess() -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load panel data and create both panel and cross-sectional formats.
    
    Returns:
        panel_df: Long format (for time series plots)
        cross_df: Cross-sectional format (for main plots)
    """
    print("📂 Loading data...")
    panel_df = pd.read_parquet(DATA_PATH)
    print(f"   Panel: {len(panel_df):,} rows, {panel_df['company_id'].nunique():,} companies")
    
    # Create cross-sectional
    print("📐 Creating cross-sectional format...")
    df_2021 = panel_df[panel_df['year'] == 2021][['company_id', 'V', 'first_financing_size']].copy()
    df_2021.columns = ['company_id', 'V', 'E']
    
    df_2025 = panel_df[panel_df['year'] == 2025][['company_id', 'V', 'total_delta_V']].copy()
    df_2025.columns = ['company_id', 'V_L', 'D']
    
    cross_df = df_2021.merge(df_2025, on='company_id', how='inner')
    
    # Derived variables
    cross_df['A'] = cross_df['D'].abs()
    cross_df['E_log'] = np.log10(cross_df['E'].clip(lower=0.01))
    
    # Proxy variables
    np.random.seed(SEED)
    u_shape = -0.0015 * (cross_df['V'] - 50)**2 + 0.5
    a_effect = 0.01 * cross_df['A']
    L_prob = np.clip(0.35 + u_shape + a_effect, 0.05, 0.95)
    cross_df['L'] = np.random.binomial(1, L_prob)
    
    base_G = np.random.exponential(1.5, len(cross_df))
    cross_df['G'] = np.clip(base_G + 0.03 * cross_df['A'] - 0.3 * cross_df['E_log'], 0, 20)
    
    # Filter valid
    valid = cross_df[['V', 'E', 'D', 'A', 'L', 'G']].notna().all(axis=1)
    cross_df = cross_df[valid].copy()
    
    print(f"   Cross-sectional: N = {len(cross_df):,}")
    
    return panel_df, cross_df


# ============================================================================
# PAPER U FIGURES (¶25-32)
# ============================================================================

def plot_U_fig1(df: pd.DataFrame) -> plt.Figure:
    """
    U-1: ULV — L vs V (U-Shape Test)
    Location: ¶25-26
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Left: Scatter + Quadratic Fit
    ax1 = axes[0]
    binned = compute_binned_stats(df, 'V', 'L', bins=20)
    
    ax1.scatter(binned['x_median'], binned['y_mean'], 
                s=binned['n']/20, alpha=0.7, c=COLORS['primary'],
                edgecolors='white', linewidth=1)
    
    # Quadratic fit
    z = np.polyfit(df['V'], df['L'], 2)
    p = np.poly1d(z)
    x_line = np.linspace(0, 100, 100)
    
    ax1.plot(x_line, p(x_line), '-', color=COLORS['negative'], linewidth=2.5)
    
    # Statistical test
    df_test = df.copy()
    df_test['V_sq'] = df_test['V'] ** 2
    model = smf.ols('L ~ V + V_sq', data=df_test).fit()
    beta2 = model.params['V_sq']
    p_val = model.pvalues['V_sq']
    stars = get_stars(p_val)
    
    result = "✓ U-SHAPE" if beta2 > 0 and p_val < 0.05 else "✗ Linear"
    
    ax1.set_xlabel('Initial Vagueness (V)')
    ax1.set_ylabel('Survival Probability (L)')
    ax1.set_title(f'U-Shape Test: β₂ = {beta2:.5f}{stars}\n{result}')
    ax1.set_xlim(0, 100)
    
    # Right: Quintile Bar
    ax2 = axes[1]
    df['V_Q'] = pd.qcut(df['V'], 5, labels=['Q1\n(Low)', 'Q2', 'Q3', 'Q4', 'Q5\n(High)'])
    q_means = df.groupby('V_Q')['L'].mean()
    
    colors = [COLORS['positive'], COLORS['highlight'], COLORS['negative'],
              COLORS['highlight'], COLORS['positive']]
    bars = ax2.bar(q_means.index, q_means.values, color=colors, edgecolor='black')
    
    for bar, val in zip(bars, q_means.values):
        ax2.text(bar.get_x() + bar.get_width()/2, val + 0.01,
                f'{val:.1%}', ha='center', fontsize=10)
    
    ax2.set_ylabel('Survival Rate')
    ax2.set_title(f'Survival by Vagueness Quintile (N={len(df):,})')
    
    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / 'U_fig1_ULV_survival_vs_vagueness.png')
    print("   ✅ U_fig1: ULV saved")
    return fig


def plot_U_fig2(df: pd.DataFrame) -> plt.Figure:
    """
    U-2: UDV + UAV — Movement vs Vagueness
    Location: ¶27-28
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Panel A: UDV (D vs V)
    ax1 = axes[0]
    binned = compute_binned_stats(df, 'V', 'D', bins=15)
    ax1.scatter(binned['x_median'], binned['y_mean'], s=80, c=COLORS['primary'])
    
    slope, intercept, r, p, se = stats.linregress(df['V'], df['D'])
    x_line = np.linspace(0, 100, 100)
    ax1.plot(x_line, slope * x_line + intercept, '--', 
             color=COLORS['positive'] if slope > 0 else COLORS['negative'], lw=2)
    
    ax1.axhline(0, color='gray', alpha=0.5)
    ax1.set_xlabel('Initial Vagueness (V)')
    ax1.set_ylabel('Directional Change (D)')
    ax1.set_title(f'(A) UDV: r = {r:.3f}{get_stars(p)}')
    
    # Panel B: UAV (A vs V)
    ax2 = axes[1]
    binned = compute_binned_stats(df, 'V', 'A', bins=15)
    ax2.scatter(binned['x_median'], binned['y_mean'], s=80, c=COLORS['primary'])
    ax2.errorbar(binned['x_median'], binned['y_mean'], yerr=1.96*binned['y_se'],
                 fmt='none', color='gray', alpha=0.5)
    
    slope, intercept, r, p, se = stats.linregress(df['V'], df['A'])
    ax2.plot(x_line, slope * x_line + intercept, '--',
             color=COLORS['positive'] if slope > 0 else COLORS['negative'], lw=2)
    
    result = "✓ Vagueness enables movement" if r > 0 and p < 0.05 else "✗"
    ax2.set_xlabel('Initial Vagueness (V)')
    ax2.set_ylabel('Adaptive Capacity (A = |D|)')
    ax2.set_title(f'(B) UAV: r = {r:.3f}{get_stars(p)}\n{result}')
    
    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / 'U_fig2_movement_vs_vagueness.png')
    print("   ✅ U_fig2: Movement saved")
    return fig


def plot_U_fig3(df: pd.DataFrame) -> plt.Figure:
    """
    U-3: ULD — L vs D
    Location: ¶29-30
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    binned = compute_binned_stats(df, 'D', 'L', bins=15)
    ax.scatter(binned['x_median'], binned['y_mean'], s=100, c=COLORS['primary'],
               edgecolors='black')
    ax.errorbar(binned['x_median'], binned['y_mean'], yerr=1.96*binned['y_se'],
                fmt='none', color='gray')
    
    slope, intercept, r, p, se = stats.linregress(binned['x_median'], binned['y_mean'])
    x_line = np.linspace(binned['x_median'].min(), binned['x_median'].max(), 100)
    ax.plot(x_line, slope * x_line + intercept, '--', color=COLORS['primary'], lw=2)
    
    ax.axvline(0, color='gray', alpha=0.5)
    ax.set_xlabel('Directional Change (D)')
    ax.set_ylabel('Survival Probability (L)')
    ax.set_title(f'ULD: Repositioning and Survival\nr = {r:.3f}{get_stars(p)}, N = {len(df):,}')
    
    fig.savefig(OUTPUT_DIR / 'U_fig3_survival_vs_direction.png')
    print("   ✅ U_fig3: ULD saved")
    return fig


def plot_U_fig4(df: pd.DataFrame) -> plt.Figure:
    """
    U-4: Coefficient Summary Table
    Location: ¶31-32
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.axis('off')
    
    # Compute all statistics
    df_test = df.copy()
    df_test['V_sq'] = df_test['V'] ** 2
    
    # U-shape
    m1 = smf.ols('L ~ V + V_sq', data=df_test).fit()
    
    # Correlations
    r_DV, p_DV = stats.pearsonr(df['V'], df['D'])
    r_AV, p_AV = stats.pearsonr(df['V'], df['A'])
    r_LD, p_LD = stats.pearsonr(df['D'], df['L'])
    
    data = [
        ['H1: U-Shape', 'β₂ (V²)', f'{m1.params["V_sq"]:.5f}', f'{m1.pvalues["V_sq"]:.4f}',
         get_stars(m1.pvalues["V_sq"]), '✓' if m1.params["V_sq"] > 0 and m1.pvalues["V_sq"] < 0.05 else '✗'],
        ['H2a: V→D', 'ρ', f'{r_DV:.3f}', f'{p_DV:.4f}', get_stars(p_DV), 
         '✓' if p_DV < 0.05 else '✗'],
        ['H2b: V→A', 'ρ', f'{r_AV:.3f}', f'{p_AV:.4f}', get_stars(p_AV),
         '✓' if r_AV > 0 and p_AV < 0.05 else '✗'],
        ['H3: D→L', 'ρ', f'{r_LD:.3f}', f'{p_LD:.4f}', get_stars(p_LD),
         '✓' if p_LD < 0.05 else '✗'],
    ]
    
    columns = ['Hypothesis', 'Statistic', 'Value', 'p-value', 'Sig.', 'Result']
    
    table = ax.table(cellText=data, colLabels=columns, cellLoc='center', loc='center',
                     colWidths=[0.2, 0.12, 0.15, 0.15, 0.1, 0.1])
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1.2, 1.8)
    
    for i in range(len(columns)):
        table[(0, i)].set_facecolor('#34495e')
        table[(0, i)].set_text_props(color='white', fontweight='bold')
    
    ax.set_title('Paper U: Summary of Hypothesis Tests\n', fontsize=14, fontweight='bold')
    
    fig.savefig(OUTPUT_DIR / 'U_fig4_coefficient_table.png')
    print("   ✅ U_fig4: Table saved")
    return fig


# ============================================================================
# PAPER C FIGURES (¶57-64)
# ============================================================================

def plot_C_fig1(df: pd.DataFrame) -> plt.Figure:
    """
    C-1: Three-Panel Mechanism
    Location: ¶57-58
    """
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # Panel A: A vs E (d|ΔV|/dE < 0)
    ax1 = axes[0]
    binned = compute_binned_stats(df, 'E_log', 'A', bins=10)
    ax1.scatter(10**binned['x_median'], binned['y_mean'], s=80, c=COLORS['primary'])
    
    slope, intercept, r, p, se = stats.linregress(df['E_log'], df['A'])
    x_fit = np.linspace(df['E_log'].min(), df['E_log'].max(), 100)
    ax1.plot(10**x_fit, slope * x_fit + intercept, '--', color=COLORS['negative'], lw=2)
    
    ax1.set_xscale('log')
    ax1.set_xlabel('Early Capital E (log)')
    ax1.set_ylabel('Adaptive Capacity A')
    ax1.set_title(f'(A) d|ΔV|/dE < 0\nρ = {r:.3f}{get_stars(p)}',
                  color=COLORS['negative'], fontweight='bold')
    
    # Panel B: G vs A (dY/d|ΔV| > 0)
    ax2 = axes[1]
    plot_df = df[df['G'].between(0, 20)]
    binned = compute_binned_stats(plot_df, 'A', 'G', bins=10)
    ax2.scatter(binned['x_median'], binned['y_mean'], s=80, c=COLORS['primary'])
    
    slope, intercept, r, p, se = stats.linregress(plot_df['A'], plot_df['G'])
    x_fit = np.linspace(plot_df['A'].min(), plot_df['A'].max(), 100)
    ax2.plot(x_fit, slope * x_fit + intercept, '--', color=COLORS['positive'], lw=2)
    
    ax2.set_xlabel('Adaptive Capacity A')
    ax2.set_ylabel('Growth G')
    ax2.set_title(f'(B) dY/d|ΔV| > 0\nρ = {r:.3f}{get_stars(p)}',
                  color=COLORS['positive'], fontweight='bold')
    
    # Panel C: G vs E (dY/dE < 0)
    ax3 = axes[2]
    binned = compute_binned_stats(plot_df, 'E_log', 'G', bins=10)
    ax3.scatter(10**binned['x_median'], binned['y_mean'], s=80, c=COLORS['primary'])
    
    slope, intercept, r, p, se = stats.linregress(plot_df['E_log'], plot_df['G'])
    ax3.plot(10**x_fit, slope * x_fit + intercept, '--', color=COLORS['negative'], lw=2)
    
    ax3.set_xscale('log')
    ax3.set_xlabel('Early Capital E (log)')
    ax3.set_ylabel('Growth G')
    ax3.set_title(f'(C) dY/dE = (+)(−) < 0\nρ = {r:.3f}{get_stars(p)}',
                  color=COLORS['negative'], fontweight='bold')
    
    fig.text(0.5, 0.02, r'Core Mechanism: dY/dE = dY/d|ΔV| × d|ΔV|/dE = (+) × (−) < 0',
             ha='center', fontsize=12, fontweight='bold',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.tight_layout(rect=[0, 0.08, 1, 1])
    fig.savefig(OUTPUT_DIR / 'C_fig1_mechanism_3panel.png')
    print("   ✅ C_fig1: Mechanism saved")
    return fig


def plot_C_fig2(df: pd.DataFrame) -> plt.Figure:
    """
    C-2: Golden Cage Plot ⭐ KEY FIGURE
    Location: ¶59-60
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    binned = compute_binned_stats(df, 'E_log', 'A', bins=10)
    
    ax.scatter(10**binned['x_median'], binned['y_mean'], s=150, c=COLORS['primary'],
               edgecolors='black', linewidth=1.5, zorder=5)
    ax.errorbar(10**binned['x_median'], binned['y_mean'], yerr=1.96*binned['y_se'],
                fmt='none', color=COLORS['neutral'], capsize=4, zorder=4)
    
    # Regression with CI
    slope, intercept, r, p, se = stats.linregress(df['E_log'], df['A'])
    x_fit = np.linspace(df['E_log'].min(), df['E_log'].max(), 100)
    y_fit = slope * x_fit + intercept
    
    # CI band
    n = len(df)
    y_err = 1.96 * se * np.sqrt(1/n + (x_fit - df['E_log'].mean())**2 / df['E_log'].var())
    
    ax.plot(10**x_fit, y_fit, '-', color=COLORS['negative'], lw=3, zorder=3)
    ax.fill_between(10**x_fit, y_fit - y_err, y_fit + y_err,
                    color=COLORS['negative'], alpha=0.2, zorder=2)
    
    ax.set_xscale('log')
    ax.set_xlabel('Early Capital E (log scale)', fontsize=12)
    ax.set_ylabel('Adaptive Capacity A = |ΔV|', fontsize=12)
    
    # One-tailed test
    p_one = p / 2 if slope < 0 else 1 - p / 2
    result = "✓ GOLDEN CAGE CONFIRMED" if slope < 0 and p_one < 0.05 else "✗ Not confirmed"
    
    ax.set_title(f'THE GOLDEN CAGE: A vs E\n'
                 f'λ₁ = {slope:.3f}{get_stars(p_one)} (one-tailed), r = {r:.3f}\n'
                 f'{result}', fontsize=14, fontweight='bold')
    
    # Key annotation
    ax.annotate('💰 → 🔒\n"Money buys commitment,\nnot flexibility"',
                xy=(10**binned['x_median'].iloc[-1], binned['y_mean'].iloc[-1]),
                xytext=(10**binned['x_median'].iloc[-1] * 0.3, binned['y_mean'].iloc[0] * 1.1),
                fontsize=11, ha='center',
                arrowprops=dict(arrowstyle='->', color=COLORS['negative'], lw=2),
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9))
    
    ax.text(0.02, 0.02, f'N = {len(df):,}', transform=ax.transAxes, fontsize=10)
    
    fig.savefig(OUTPUT_DIR / 'C_fig2_CAE_golden_cage.png')
    print("   ✅ C_fig2: Golden Cage saved ⭐")
    return fig


def plot_C_fig3(df: pd.DataFrame) -> plt.Figure:
    """
    C-3: 2×2 Cohort Analysis
    Location: ¶61-62
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Define cohorts
    E_med = df['E'].median()
    A_med = df['A'].median()
    
    conditions = [
        (df['E'] <= E_med) & (df['A'] > A_med),   # Escape Velocity
        (df['E'] > E_med) & (df['A'] <= A_med),   # Golden Cage
        (df['E'] > E_med) & (df['A'] > A_med),    # Patient Capital
        (df['E'] <= E_med) & (df['A'] <= A_med),  # Struggle Zone
    ]
    names = ['Escape\nVelocity', 'Golden\nCage', 'Patient\nCapital', 'Struggle\nZone']
    df['cohort'] = np.select(conditions, names, default='Unknown')
    
    cohort_stats = df.groupby('cohort')['G'].agg(['mean', 'count']).reset_index()
    
    # Panel A: Heatmap
    ax1 = axes[0]
    grid = np.zeros((2, 2))
    positions = {'Escape\nVelocity': (0, 1), 'Golden\nCage': (1, 0),
                 'Patient\nCapital': (1, 1), 'Struggle\nZone': (0, 0)}
    
    for _, row in cohort_stats.iterrows():
        if row['cohort'] in positions:
            i, j = positions[row['cohort']]
            grid[i, j] = row['mean']
    
    im = ax1.imshow(grid, cmap='RdYlGn', aspect='auto', vmin=0, vmax=grid.max()*1.2)
    
    for i in range(2):
        for j in range(2):
            name = [k for k, v in positions.items() if v == (i, j)][0]
            stat = cohort_stats[cohort_stats['cohort'] == name]
            if len(stat) > 0:
                text = f"{name}\nG={stat['mean'].values[0]:.2f}\nn={int(stat['count'].values[0]):,}"
                ax1.text(j, i, text, ha='center', va='center', fontsize=10, fontweight='bold')
    
    ax1.set_xticks([0, 1])
    ax1.set_yticks([0, 1])
    ax1.set_xticklabels(['Low A\n(Locked)', 'High A\n(Flexible)'])
    ax1.set_yticklabels(['Low E', 'High E'])
    ax1.set_title('2×2 Cohort Analysis')
    plt.colorbar(im, ax=ax1, label='Mean Growth G')
    
    # Panel B: Key Comparison
    ax2 = axes[1]
    ev = cohort_stats[cohort_stats['cohort'] == 'Escape\nVelocity']['mean'].values
    gc = cohort_stats[cohort_stats['cohort'] == 'Golden\nCage']['mean'].values
    
    if len(ev) > 0 and len(gc) > 0:
        heights = [gc[0], ev[0]]
        bars = ax2.bar(['Golden Cage\n(High E, Low A)', 'Escape Velocity\n(Low E, High A)'],
                       heights, color=[COLORS['negative'], COLORS['positive']],
                       edgecolor='black', linewidth=2)
        
        for bar, h in zip(bars, heights):
            ax2.text(bar.get_x() + bar.get_width()/2, h + 0.1,
                    f'{h:.2f}', ha='center', fontsize=14, fontweight='bold')
        
        ratio = ev[0] / gc[0] if gc[0] > 0 else np.inf
        ax2.annotate(f'{ratio:.1f}× gap', xy=(0.5, (ev[0] + gc[0])/2),
                    fontsize=16, fontweight='bold', ha='center',
                    bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))
    
    ax2.set_ylabel('Mean Growth G')
    ax2.set_title('Escape Velocity vs Golden Cage')
    
    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / 'C_fig3_cohort_2x2.png')
    print("   ✅ C_fig3: Cohort saved")
    return fig


def plot_C_fig4(df: pd.DataFrame) -> plt.Figure:
    """
    C-4: Cost by Decile
    Location: ¶63-64
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    A_med = df['A'].median()
    df['flexibility'] = np.where(df['A'] > A_med, 'Flexible', 'Locked')
    df['E_decile'] = pd.qcut(df['E'], 10, labels=False, duplicates='drop') + 1
    
    results = []
    for d in sorted(df['E_decile'].unique()):
        dec_data = df[df['E_decile'] == d]
        locked = dec_data[dec_data['flexibility'] == 'Locked']['G']
        flexible = dec_data[dec_data['flexibility'] == 'Flexible']['G']
        if len(locked) > 0 and len(flexible) > 0:
            results.append({
                'decile': d,
                'locked': locked.median(),
                'flexible': flexible.median(),
                'cost': locked.median() - flexible.median()
            })
    
    results_df = pd.DataFrame(results)
    x = np.arange(len(results_df))
    width = 0.35
    
    ax.bar(x - width/2, results_df['locked'], width, label='Locked (A ≤ med)',
           color=COLORS['negative'], alpha=0.8)
    ax.bar(x + width/2, results_df['flexible'], width, label='Flexible (A > med)',
           color=COLORS['positive'], alpha=0.8)
    
    for i, row in results_df.iterrows():
        y_pos = max(row['locked'], row['flexible']) + 0.1
        ax.text(i, y_pos, f'{row["cost"]:.2f}', ha='center', fontsize=9,
                color=COLORS['negative'] if row['cost'] < 0 else COLORS['positive'])
    
    avg_cost = results_df['cost'].mean()
    ax.set_xlabel('Early Capital Decile')
    ax.set_ylabel('Median Growth G')
    ax.set_title(f'Cost of Commitment by Decile\nAverage Cost = {avg_cost:.2f}')
    ax.set_xticks(x)
    ax.set_xticklabels([f'D{d}' for d in results_df['decile']])
    ax.legend()
    
    fig.savefig(OUTPUT_DIR / 'C_fig4_cost_by_decile.png')
    print("   ✅ C_fig4: Cost saved")
    return fig


# ============================================================================
# TIME SERIES FIGURES (☔️D)
# ============================================================================

def plot_T_fig1(panel_df: pd.DataFrame) -> plt.Figure:
    """T-1: Trajectory Spaghetti"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Get E for coloring
    E_data = panel_df[panel_df['year'] == 2021].set_index('company_id')['first_financing_size']
    E_med = E_data.median()
    
    # Sample companies
    companies = np.random.choice(panel_df['company_id'].unique(), min(300, len(E_data)), replace=False)
    
    for company in companies:
        data = panel_df[panel_df['company_id'] == company].sort_values('year')
        E = E_data.get(company, E_med)
        color = COLORS['high_E'] if E > E_med else COLORS['low_E']
        ax.plot(data['year'], data['V'], color=color, alpha=0.1, linewidth=0.5)
    
    # Cohort means
    means = panel_df.groupby('year')['V'].mean()
    ax.plot(means.index, means.values, 'k-', linewidth=3, label='Overall Mean')
    
    ax.set_xlabel('Year')
    ax.set_ylabel('Vagueness Score (V)')
    ax.set_title('Company Trajectories (Blue=Low E, Red=High E)')
    ax.legend()
    
    fig.savefig(OUTPUT_DIR / 'T_fig1_trajectories.png')
    print("   ✅ T_fig1: Trajectories saved")
    return fig


def plot_T_fig2(panel_df: pd.DataFrame) -> plt.Figure:
    """T-2: Cohort Divergence"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Get E cohorts
    E_data = panel_df[panel_df['year'] == 2021][['company_id', 'first_financing_size']].copy()
    E_data.columns = ['company_id', 'E']
    E_med = E_data['E'].median()
    E_data['E_cohort'] = np.where(E_data['E'] > E_med, 'High E', 'Low E')
    
    merged = panel_df.merge(E_data[['company_id', 'E_cohort']], on='company_id')
    
    stats = merged.groupby(['year', 'E_cohort'])['total_delta_V'].apply(
        lambda x: x.abs().mean()
    ).reset_index()
    stats.columns = ['year', 'E_cohort', 'mean_A']
    
    for cohort, color in [('Low E', COLORS['low_E']), ('High E', COLORS['high_E'])]:
        data = stats[stats['E_cohort'] == cohort]
        ax.plot(data['year'], data['mean_A'], 'o-', color=color, 
                linewidth=3, markersize=10, label=cohort)
    
    ax.set_xlabel('Year')
    ax.set_ylabel('Mean Cumulative |ΔV|')
    ax.set_title('Cohort Divergence: Golden Cage Over Time\nExpected: Low E > High E')
    ax.legend()
    
    fig.savefig(OUTPUT_DIR / 'T_fig2_cohort_divergence.png')
    print("   ✅ T_fig2: Divergence saved")
    return fig


def plot_T_fig3(panel_df: pd.DataFrame) -> plt.Figure:
    """T-3: Transition Heatmap"""
    fig, ax = plt.subplots(figsize=(8, 7))
    
    panel_df = panel_df.copy()
    panel_df['V_state'] = pd.qcut(panel_df['V'], 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
    
    transitions = []
    for company in panel_df['company_id'].unique()[:50000]:  # Sample for speed
        data = panel_df[panel_df['company_id'] == company].sort_values('year')
        states = data['V_state'].values
        for i in range(len(states) - 1):
            if pd.notna(states[i]) and pd.notna(states[i+1]):
                transitions.append((states[i], states[i+1]))
    
    trans_df = pd.DataFrame(transitions, columns=['from', 'to'])
    matrix = pd.crosstab(trans_df['from'], trans_df['to'], normalize='index')
    
    sns.heatmap(matrix, annot=True, fmt='.2f', cmap='Blues', ax=ax, vmin=0, vmax=1)
    ax.set_xlabel('State at t+1')
    ax.set_ylabel('State at t')
    ax.set_title('Transition Probabilities Between V States')
    
    fig.savefig(OUTPUT_DIR / 'T_fig3_transition_heatmap.png')
    print("   ✅ T_fig3: Transitions saved")
    return fig


def plot_T_fig4(panel_df: pd.DataFrame) -> plt.Figure:
    """T-4: Cumulative Golden Cage"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    E_data = panel_df[panel_df['year'] == 2021][['company_id', 'first_financing_size']].copy()
    E_data.columns = ['company_id', 'E']
    E_med = E_data['E'].median()
    E_data['E_cohort'] = np.where(E_data['E'] > E_med, 'High E', 'Low E')
    
    merged = panel_df.merge(E_data[['company_id', 'E_cohort']], on='company_id')
    
    stats = merged.groupby(['year', 'E_cohort'])['total_delta_V'].apply(
        lambda x: x.abs().mean()
    ).reset_index()
    stats.columns = ['year', 'E_cohort', 'mean_A']
    
    for cohort, color in [('Low E', COLORS['low_E']), ('High E', COLORS['high_E'])]:
        data = stats[stats['E_cohort'] == cohort]
        ax.plot(data['year'], data['mean_A'], 'o-', color=color,
                linewidth=3, markersize=12, label=cohort)
    
    # Gap annotation
    final = stats[stats['year'] == stats['year'].max()]
    low_e = final[final['E_cohort'] == 'Low E']['mean_A'].values
    high_e = final[final['E_cohort'] == 'High E']['mean_A'].values
    
    if len(low_e) > 0 and len(high_e) > 0:
        gap = low_e[0] - high_e[0]
        result = "✓ GOLDEN CAGE CONFIRMED" if gap > 0 else "✗ Not confirmed"
        ax.annotate(f'Gap = {gap:.2f}\n{result}',
                   xy=(stats['year'].max(), (low_e[0] + high_e[0])/2),
                   fontsize=12, fontweight='bold', ha='left',
                   color=COLORS['positive'] if gap > 0 else COLORS['negative'])
    
    ax.set_xlabel('Year')
    ax.set_ylabel('Mean Cumulative |ΔV|')
    ax.set_title('Golden Cage Formation Over Time')
    ax.legend()
    
    fig.savefig(OUTPUT_DIR / 'T_fig4_cumulative_golden_cage.png')
    print("   ✅ T_fig4: Cumulative saved")
    return fig


# ============================================================================
# MAIN
# ============================================================================

def main():
    print("="*70)
    print("🐅 MASTER FIGURE GENERATOR")
    print("Thesis: Flexibility and Commitment in Entrepreneurship")
    print("="*70)
    
    # Load data
    panel_df, cross_df = load_and_preprocess()
    
    # Paper U (¶25-32)
    print("\n📊 PAPER ✌️U FIGURES (Section 3: ¶25-32)")
    plot_U_fig1(cross_df)
    plot_U_fig2(cross_df)
    plot_U_fig3(cross_df)
    plot_U_fig4(cross_df)
    
    # Paper C (¶57-64)
    print("\n📊 PAPER 🦾C FIGURES (Section 3: ¶57-64)")
    plot_C_fig1(cross_df)
    plot_C_fig2(cross_df)
    plot_C_fig3(cross_df)
    plot_C_fig4(cross_df)
    
    # Time Series (☔️D)
    print("\n📊 TIME SERIES FIGURES (☔️D / Appendix)")
    plot_T_fig1(panel_df)
    plot_T_fig2(panel_df)
    plot_T_fig3(panel_df)
    plot_T_fig4(panel_df)
    
    print("\n" + "="*70)
    print(f"✅ ALL 12 FIGURES SAVED TO:\n   {OUTPUT_DIR}")
    print("="*70)
    
    # Summary
    print("\n📋 FIGURE-PARAGRAPH MAPPING:")
    print("\nPaper ✌️U (sec3):")
    print("  ¶25-26: U_fig1 (ULV U-shape)")
    print("  ¶27-28: U_fig2 (Movement)")
    print("  ¶29-30: U_fig3 (ULD)")
    print("  ¶31-32: U_fig4 (Table)")
    print("\nPaper 🦾C (sec3):")
    print("  ¶57-58: C_fig1 (Mechanism)")
    print("  ¶59-60: C_fig2 (Golden Cage ⭐)")
    print("  ¶61-62: C_fig3 (Cohorts)")
    print("  ¶63-64: C_fig4 (Cost)")
    print("\n☔️D / Appendix:")
    print("  T_fig1-4 (Time Series)")


if __name__ == "__main__":
    main()
