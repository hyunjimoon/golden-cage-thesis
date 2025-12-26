#!/usr/bin/env python3
"""
Diagnostic plots for PitchBook's GrowthRate (employee/web growth)
vs thesis arguments.

Tests:
1. Capital Paradox: ρ(G, E) < 0?
2. Adaptation → Growth: ρ(G, A) > 0?
3. Cash2Cage: ρ(A, E) < 0?
4. Mover advantage: Movers have higher G than Stayers?
5. Archetype dG/dE patterns

Comparison: G_funding vs G_pitchbook
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
OUTPUT_DIR = SCRIPT_DIR

def load_data():
    """Load and prepare data with both G definitions."""
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
        feat_dedup[['CompanyID', 'total_raised', 'GrowthRate', 'last_financing_deal_type']],
        left_on='company_id',
        right_on='CompanyID',
        how='left'
    )

    # Both G definitions
    panel['G_funding'] = panel['total_raised'] / panel['E']
    panel.loc[panel['total_raised'].isna() & panel['E'].notna(), 'G_funding'] = 1.0
    panel['G_pitchbook'] = panel['GrowthRate']

    # Success
    panel['L'] = panel['last_financing_deal_type'].str.contains('Later Stage VC', na=False).astype(int)

    return panel


def create_diagnostic_figure(df):
    """Create 2x3 diagnostic figure comparing both G definitions."""

    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Thesis Argument Tests: G_funding vs G_pitchbook (GrowthRate)',
                 fontsize=14, fontweight='bold', y=1.02)

    # Prepare data
    valid_funding = df.dropna(subset=['G_funding', 'E', 'A'])
    valid_funding = valid_funding[np.isfinite(valid_funding['G_funding']) & (valid_funding['E'] > 0)]

    valid_pb = df.dropna(subset=['G_pitchbook', 'E', 'A'])
    valid_pb = valid_pb[np.isfinite(valid_pb['G_pitchbook']) & (valid_pb['E'] > 0)]

    colors = {'zoom_in': '#2ecc71', 'zoom_out': '#e74c3c', 'stayer': '#95a5a6', 'horizontal': '#3498db'}

    # ===== Row 1: G_funding (Thesis Definition) =====

    # Plot 1a: G_funding vs E (Capital Paradox)
    ax = axes[0, 0]
    for mtype in ['stayer', 'zoom_in', 'zoom_out', 'horizontal']:
        subset = valid_funding[valid_funding['mover_type'] == mtype]
        if len(subset) > 0:
            ax.scatter(np.log1p(subset['E']), np.log1p(subset['G_funding']),
                      alpha=0.1, s=5, c=colors[mtype], label=mtype)

    rho, p = spearmanr(valid_funding['G_funding'], np.log1p(valid_funding['E']))
    ax.set_xlabel('log(E) - Early Funding')
    ax.set_ylabel('log(G_funding)')
    ax.set_title(f'Capital Paradox Test\nρ(G,E) = {rho:.3f}*** {"✅" if rho < 0 else "❌"}')
    ax.legend(loc='upper right', fontsize=8)

    # Plot 1b: G_funding vs A (Adaptation → Growth)
    ax = axes[0, 1]
    for mtype in ['stayer', 'zoom_in', 'zoom_out', 'horizontal']:
        subset = valid_funding[valid_funding['mover_type'] == mtype]
        if len(subset) > 0:
            ax.scatter(subset['A'], np.log1p(subset['G_funding']),
                      alpha=0.1, s=5, c=colors[mtype], label=mtype)

    rho, p = spearmanr(valid_funding['G_funding'], valid_funding['A'])
    ax.set_xlabel('A - Adaptive Capacity |D|')
    ax.set_ylabel('log(G_funding)')
    ax.set_title(f'Adaptation→Growth Test\nρ(G,A) = {rho:.3f}*** {"✅" if rho > 0 else "❌"}')

    # Plot 1c: G_funding by Archetype (boxplot)
    ax = axes[0, 2]
    archetype_order = ['stayer', 'horizontal', 'zoom_in', 'zoom_out']
    box_data = [np.log1p(valid_funding[valid_funding['mover_type'] == m]['G_funding'].clip(upper=100))
                for m in archetype_order]
    bp = ax.boxplot(box_data, labels=archetype_order, patch_artist=True)
    for patch, mtype in zip(bp['boxes'], archetype_order):
        patch.set_facecolor(colors[mtype])
        patch.set_alpha(0.7)
    ax.set_ylabel('log(G_funding)')
    ax.set_title('G_funding by Archetype\n(Movers > Stayers?)')
    ax.axhline(y=np.median(box_data[0]), color='gray', linestyle='--', alpha=0.5)

    # ===== Row 2: G_pitchbook (Employee/Web Growth) =====

    # Plot 2a: G_pitchbook vs E
    ax = axes[1, 0]
    for mtype in ['stayer', 'zoom_in', 'zoom_out', 'horizontal']:
        subset = valid_pb[valid_pb['mover_type'] == mtype]
        if len(subset) > 0:
            ax.scatter(np.log1p(subset['E']), subset['G_pitchbook'].clip(-5, 10),
                      alpha=0.1, s=5, c=colors[mtype], label=mtype)

    rho, p = spearmanr(valid_pb['G_pitchbook'], np.log1p(valid_pb['E']))
    ax.set_xlabel('log(E) - Early Funding')
    ax.set_ylabel('G_pitchbook (clipped)')
    ax.set_title(f'Capital Paradox Test\nρ(G,E) = {rho:.3f} {"✅" if rho < 0 else "❌ (positive!)"}')
    ax.legend(loc='upper right', fontsize=8)

    # Plot 2b: G_pitchbook vs A
    ax = axes[1, 1]
    for mtype in ['stayer', 'zoom_in', 'zoom_out', 'horizontal']:
        subset = valid_pb[valid_pb['mover_type'] == mtype]
        if len(subset) > 0:
            ax.scatter(subset['A'], subset['G_pitchbook'].clip(-5, 10),
                      alpha=0.1, s=5, c=colors[mtype], label=mtype)

    rho, p = spearmanr(valid_pb['G_pitchbook'], valid_pb['A'])
    ax.set_xlabel('A - Adaptive Capacity |D|')
    ax.set_ylabel('G_pitchbook (clipped)')
    ax.set_title(f'Adaptation→Growth Test\nρ(G,A) = {rho:.3f}** {"✅" if rho > 0 else "❌"}')

    # Plot 2c: G_pitchbook by Archetype
    ax = axes[1, 2]
    box_data_pb = [valid_pb[valid_pb['mover_type'] == m]['G_pitchbook'].clip(-5, 10)
                   for m in archetype_order]
    bp = ax.boxplot(box_data_pb, labels=archetype_order, patch_artist=True)
    for patch, mtype in zip(bp['boxes'], archetype_order):
        patch.set_facecolor(colors[mtype])
        patch.set_alpha(0.7)
    ax.set_ylabel('G_pitchbook (clipped)')
    ax.set_title('G_pitchbook by Archetype\n(Movers > Stayers?)')
    ax.axhline(y=np.median(box_data_pb[0]), color='gray', linestyle='--', alpha=0.5)

    # Add row labels
    fig.text(0.02, 0.75, 'G_funding\n(total_raised/E)\nN=180,860',
             fontsize=11, fontweight='bold', va='center', rotation=90)
    fig.text(0.02, 0.28, 'G_pitchbook\n(employee/web)\nN=74,857',
             fontsize=11, fontweight='bold', va='center', rotation=90)

    plt.tight_layout()
    plt.subplots_adjust(left=0.08)

    return fig


def create_dGdE_comparison(df):
    """Create dG/dE slope comparison by archetype for both G definitions."""

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    archetypes = ['zoom_in', 'zoom_out', 'stayer', 'horizontal']
    colors = {'zoom_in': '#2ecc71', 'zoom_out': '#e74c3c', 'stayer': '#95a5a6', 'horizontal': '#3498db'}

    for idx, (g_col, title, ax) in enumerate([
        ('G_funding', 'G_funding = total_raised / E', axes[0]),
        ('G_pitchbook', 'G_pitchbook (Employee/Web Growth)', axes[1])
    ]):
        valid = df.dropna(subset=[g_col, 'E', 'A'])
        valid = valid[np.isfinite(valid[g_col]) & (valid['E'] > 0)]

        results = []
        for mtype in archetypes:
            subset = valid[valid['mover_type'] == mtype]
            if len(subset) > 30:
                # Log transform for funding, raw for pitchbook
                if g_col == 'G_funding':
                    y = np.log1p(subset[g_col].clip(0, 1000))
                else:
                    y = subset[g_col].clip(-10, 20)
                x = np.log1p(subset['E'])

                slope, intercept, r, p, se = linregress(x, y)
                results.append({
                    'archetype': mtype,
                    'slope': slope,
                    'se': se,
                    'p': p,
                    'n': len(subset),
                    'sig': '***' if p < 0.001 else '**' if p < 0.01 else '*' if p < 0.05 else ''
                })

        # Bar plot
        x_pos = np.arange(len(results))
        slopes = [r['slope'] for r in results]
        errors = [1.96 * r['se'] for r in results]
        bar_colors = [colors[r['archetype']] for r in results]

        bars = ax.bar(x_pos, slopes, yerr=errors, capsize=5, color=bar_colors, alpha=0.8, edgecolor='black')
        ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)

        # Labels
        labels = [f"{r['archetype']}\n(N={r['n']:,})\n{r['sig']}" for r in results]
        ax.set_xticks(x_pos)
        ax.set_xticklabels(labels)
        ax.set_ylabel('dG/dE (slope)')
        ax.set_title(f'{title}\n(N={len(valid):,})')

        # Color bars by sign
        for bar, slope in zip(bars, slopes):
            if slope < 0:
                bar.set_hatch('///')

    fig.suptitle('dG/dE by Archetype: Comparing Two G Definitions', fontsize=14, fontweight='bold')
    plt.tight_layout()

    return fig


def create_selection_bias_check(df):
    """Check if companies with GrowthRate differ systematically."""

    fig, axes = plt.subplots(1, 3, figsize=(14, 5))

    df['has_growthrate'] = df['G_pitchbook'].notna()

    # Plot 1: E distribution
    ax = axes[0]
    ax.hist(np.log1p(df[df['has_growthrate']]['E']), bins=50, alpha=0.6,
            label=f'Has GrowthRate (N={df["has_growthrate"].sum():,})', density=True)
    ax.hist(np.log1p(df[~df['has_growthrate']]['E']), bins=50, alpha=0.6,
            label=f'No GrowthRate (N={(~df["has_growthrate"]).sum():,})', density=True)
    ax.set_xlabel('log(E)')
    ax.set_ylabel('Density')
    ax.set_title('Early Funding Distribution')
    ax.legend()

    # Plot 2: L (success) rate
    ax = axes[1]
    l_with = df[df['has_growthrate']]['L'].mean() * 100
    l_without = df[~df['has_growthrate']]['L'].mean() * 100
    bars = ax.bar(['Has GrowthRate', 'No GrowthRate'], [l_with, l_without],
                  color=['#3498db', '#95a5a6'], edgecolor='black')
    ax.set_ylabel('Success Rate (%)')
    ax.set_title(f'Success Rate by GrowthRate Availability\n({l_with:.1f}% vs {l_without:.1f}%)')
    for bar, val in zip(bars, [l_with, l_without]):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{val:.1f}%', ha='center', fontweight='bold')

    # Plot 3: Mover type distribution
    ax = axes[2]
    mover_with = df[df['has_growthrate']]['mover_type'].value_counts(normalize=True) * 100
    mover_without = df[~df['has_growthrate']]['mover_type'].value_counts(normalize=True) * 100

    x = np.arange(4)
    width = 0.35
    order = ['stayer', 'horizontal', 'zoom_in', 'zoom_out']

    ax.bar(x - width/2, [mover_with.get(m, 0) for m in order], width,
           label='Has GrowthRate', color='#3498db', alpha=0.8)
    ax.bar(x + width/2, [mover_without.get(m, 0) for m in order], width,
           label='No GrowthRate', color='#95a5a6', alpha=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(order)
    ax.set_ylabel('Percentage (%)')
    ax.set_title('Archetype Distribution')
    ax.legend()

    fig.suptitle('Selection Bias Check: Who Has GrowthRate Data?', fontsize=14, fontweight='bold')
    plt.tight_layout()

    return fig


def main():
    print("Loading data...")
    df = load_data()

    print(f"Total companies: {len(df):,}")
    print(f"With G_funding: {df['G_funding'].notna().sum():,}")
    print(f"With G_pitchbook: {df['G_pitchbook'].notna().sum():,}")

    # Create figures
    print("\nCreating diagnostic figures...")

    fig1 = create_diagnostic_figure(df)
    fig1.savefig(OUTPUT_DIR / 'diagnostic_growthrate_comparison.png', dpi=150, bbox_inches='tight')
    print(f"  Saved: diagnostic_growthrate_comparison.png")

    fig2 = create_dGdE_comparison(df)
    fig2.savefig(OUTPUT_DIR / 'diagnostic_dGdE_by_archetype.png', dpi=150, bbox_inches='tight')
    print(f"  Saved: diagnostic_dGdE_by_archetype.png")

    fig3 = create_selection_bias_check(df)
    fig3.savefig(OUTPUT_DIR / 'diagnostic_selection_bias.png', dpi=150, bbox_inches='tight')
    print(f"  Saved: diagnostic_selection_bias.png")

    plt.close('all')
    print("\nDone!")


if __name__ == '__main__':
    main()
