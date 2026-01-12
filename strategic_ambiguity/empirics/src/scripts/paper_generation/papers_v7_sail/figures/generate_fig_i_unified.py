#!/usr/bin/env python3
"""
Generate Fig-I (Capital Paradox) with unified thesis style.
Matches: Fig-ARG, Fig-CFR1, Fig-P1 styling.

Style: White background, grayscale, minimal, clean
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import spearmanr, linregress
import warnings
warnings.filterwarnings('ignore')

# Paths
SCRIPT_DIR = Path(__file__).parent.resolve()
REPO_ROOT = SCRIPT_DIR.parent.parent.parent.parent.parent
DATA_DIR = REPO_ROOT / 'data' / 'processed'
OUTPUT_DIR = SCRIPT_DIR / 'images'

# Unified thesis style
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'axes.edgecolor': '#333333',
    'axes.linewidth': 0.8,
    'axes.grid': False,
    'grid.alpha': 0.3,
})

# Grayscale palette (matching other thesis figures)
GRAY_DARK = '#4a4a4a'
GRAY_MID = '#808080'
GRAY_LIGHT = '#c0c0c0'
GRAY_FILL = '#e0e0e0'


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

    # Merge features
    feat_dedup = feat.drop_duplicates('CompanyID').copy()
    panel = panel.merge(
        feat_dedup[['CompanyID', 'total_raised']],
        left_on='company_id',
        right_on='CompanyID',
        how='left'
    )

    # G = total_raised / E (Funding Growth Multiple)
    panel['G'] = panel['total_raised'] / panel['E']
    panel.loc[panel['total_raised'].isna() & panel['E'].notna(), 'G'] = 1.0

    return panel


def plot_capital_paradox_unified(df, output_path):
    """
    Generate Fig-I with unified thesis style.
    Matches Fig-CFR1 aesthetic: grayscale, clean, white background.
    """
    fig, ax = plt.subplots(figsize=(8, 6))

    # Filter valid data
    valid = df.dropna(subset=['G', 'E'])
    valid = valid[(valid['E'] > 0) & (valid['G'] > 0) & (valid['G'] < 1000)]

    # Log transform
    x = np.log10(valid['E'] + 1)
    y = np.log10(valid['G'] + 1)

    # Sample for visibility
    if len(valid) > 3000:
        sample_idx = np.random.choice(len(valid), 3000, replace=False)
        x_sample = x.iloc[sample_idx]
        y_sample = y.iloc[sample_idx]
    else:
        x_sample = x
        y_sample = y

    # Scatter plot - unified gray style
    ax.scatter(x_sample, y_sample,
               alpha=0.25, s=20,
               c=GRAY_MID,
               edgecolors='none',
               rasterized=True)

    # Regression line with confidence band
    slope, intercept, r, p, se = linregress(x, y)
    x_line = np.linspace(x.min(), x.max(), 100)
    y_line = slope * x_line + intercept

    # Confidence band (approximate)
    n = len(x)
    y_err = 1.96 * se * np.sqrt(1/n + (x_line - x.mean())**2 / ((x - x.mean())**2).sum())

    ax.fill_between(x_line, y_line - y_err * 5, y_line + y_err * 5,
                    color=GRAY_LIGHT, alpha=0.4, label='95% CI')
    ax.plot(x_line, y_line, color=GRAY_DARK, linewidth=2.5, label=f'Trend')

    # Correlation
    rho, p_val = spearmanr(valid['G'], valid['E'])

    # Title and labels
    ax.set_title(f'The Capital Paradox\nρ(G, E) = {rho:.3f}*** (N = {len(valid):,})',
                fontsize=14, fontweight='bold', color=GRAY_DARK)
    ax.set_xlabel('Early Capital E ($M, log scale)', fontsize=12, color=GRAY_DARK)
    ax.set_ylabel('Funding Growth G (log multiple)', fontsize=12, color=GRAY_DARK)

    # Annotation box - matching other figures
    ax.annotate('Higher early funding →\nLower growth multiples',
                xy=(2.3, 0.4), fontsize=10, style='italic',
                color=GRAY_DARK,
                bbox=dict(boxstyle='round,pad=0.5',
                         facecolor='white',
                         edgecolor=GRAY_LIGHT,
                         alpha=0.9))

    # N label (matching Fig-CFR1 style)
    ax.text(0.02, 0.02, f'N = {len(valid):,}',
            transform=ax.transAxes, fontsize=10, color=GRAY_MID)

    # Axis limits
    ax.set_xlim(-0.3, 5)
    ax.set_ylim(-0.1, 3)

    # Spine styling
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(GRAY_LIGHT)
    ax.spines['bottom'].set_color(GRAY_LIGHT)

    # Tick styling
    ax.tick_params(colors=GRAY_MID)

    plt.tight_layout()

    # Save
    fig.savefig(output_path, dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"Saved: {output_path}")

    plt.close(fig)
    return rho, len(valid)


def main():
    print("Loading data...")
    df = load_data()
    print(f"Loaded {len(df):,} records")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / 'Fig-I_capital_paradox.png'

    print("Generating Fig-I (Capital Paradox) - Unified Style...")
    rho, n = plot_capital_paradox_unified(df, output_path)

    print(f"\n✅ Complete!")
    print(f"   ρ(G,E) = {rho:.3f}***")
    print(f"   N = {n:,}")
    print(f"   Output: {output_path}")


if __name__ == '__main__':
    main()
