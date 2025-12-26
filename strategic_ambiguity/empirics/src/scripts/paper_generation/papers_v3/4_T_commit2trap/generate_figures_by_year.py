#!/usr/bin/env python3
"""
Generate fig_decomposition_real_{year}.png for 2023, 2024, 2025

THESIS MESSAGE: Commit to adaptation - first direction, then speed.
The decomposition shows how Effectiveness × Efficiency = Total Effect.

SCIENCE JOURNAL QUALITY STANDARDS:
1. Clear visual hierarchy - main message prominent
2. Consistent color scheme across thesis
3. Minimal clutter, maximum information density
4. Publication-ready: 300 DPI, vector PDF
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress, spearmanr
from pathlib import Path

# Paths
REPO_ROOT = Path("/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics")
DATA_DIR = REPO_ROOT / "data" / "processed"
OUTPUT_DIR = REPO_ROOT / "src/scripts/paper_generation/papers_v3/4_T_commit2trap"

# ============================================================================
# THESIS COLOR SCHEME - Consistent across all figures
# ============================================================================
COLORS = {
    # Archetype colors
    'zoom_in': '#E63946',     # 🔴 Red - Focus trajectory
    'zoom_out': '#457B9D',    # 🔵 Blue - Expand trajectory
    'stayer': '#264653',      # ⚫ Dark teal - Fixed position
    'horizontal': '#2A9D8F',  # 🟢 Green - Lateral movement

    # Sign colors (for bar charts)
    'positive': '#2A9D8F',    # Teal - Good/positive effect
    'negative': '#E76F51',    # Coral - Bad/negative effect

    # Text and grid
    'text_dark': '#1a1a1a',
    'text_medium': '#444444',
    'grid': '#cccccc',
    'axis': '#666666',
}

# Display names with clear interpretation
DISPLAY_NAMES = {
    'zoom_in': 'Zoom In',
    'zoom_out': 'Zoom Out',
    'stayer': 'Stayer',
    'horizontal': 'Horizontal'
}


def set_publication_style():
    """Set matplotlib style for science journal quality."""
    plt.rcParams.update({
        'font.family': 'sans-serif',
        'font.sans-serif': ['Arial', 'Helvetica Neue', 'DejaVu Sans'],
        'font.size': 11,
        'axes.labelsize': 12,
        'axes.titlesize': 14,
        'axes.titleweight': 'bold',
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'legend.fontsize': 9,
        'figure.titlesize': 16,
        'axes.linewidth': 1.0,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'figure.facecolor': 'white',
        'axes.facecolor': 'white',
        'savefig.facecolor': 'white',
        'savefig.edgecolor': 'none',
    })


def load_data_for_year(target_year):
    """Load panel data with V_T from target_year."""
    print(f"\n{'='*60}")
    print(f"Loading data for year: {target_year}")
    print(f"{'='*60}")

    vag = pd.read_parquet(DATA_DIR / "vagueness_timeseries.parquet")

    # V_0 from 2021 (with E)
    v_2021 = vag[vag['year'] == 2021][['company_id', 'V', 'first_financing_size']].copy()
    v_2021 = v_2021.rename(columns={'V': 'V_0', 'first_financing_size': 'E'})
    v_2021 = v_2021[v_2021['E'].notna() & (v_2021['E'] > 0)]

    # V_T from target_year
    v_target = vag[vag['year'] == target_year][['company_id', 'V']].copy()
    v_target = v_target.rename(columns={'V': 'V_T'})

    panel = v_2021.merge(v_target, on='company_id', how='inner')
    print(f"  Ventures with V_0 (2021) and V_T ({target_year}): {len(panel):,}")

    panel['D'] = panel['V_T'] - panel['V_0']
    panel['A'] = panel['D'].abs()

    def classify_mover(row):
        if row['A'] < 5:
            return 'stayer'
        elif row['D'] < -10:
            return 'zoom_in'
        elif row['D'] > 10:
            return 'zoom_out'
        else:
            return 'horizontal'

    panel['mover_type'] = panel.apply(classify_mover, axis=1)

    # Load features for G
    feat = pd.read_parquet(DATA_DIR / "features_all.parquet")
    feat_dedup = feat.drop_duplicates('CompanyID')
    feat_dedup['CompanyID_str'] = feat_dedup['CompanyID'].astype(str)
    panel['company_id_str'] = panel['company_id'].astype(str)

    panel = panel.merge(
        feat_dedup[['CompanyID_str', 'total_raised']],
        left_on='company_id_str',
        right_on='CompanyID_str',
        how='left'
    )

    panel['G'] = panel['total_raised'] / panel['E']
    panel.loc[panel['total_raised'].isna() & panel['E'].notna(), 'G'] = 1.0

    print(f"  Mover types: {panel['mover_type'].value_counts().to_dict()}")
    print(f"  With valid G: {panel['G'].notna().sum():,}")

    return panel


def compute_slopes(df):
    """Compute Spearman ρ for dG/dA and dA/dE by archetype."""
    analysis = df[df['E'].notna() & df['G'].notna() & (df['E'] > 0)].copy()
    analysis['log_E'] = np.log1p(analysis['E'])

    results = []

    for mtype in ['zoom_in', 'zoom_out', 'stayer']:
        subset = analysis[analysis['mover_type'] == mtype]

        if len(subset) < 30:
            print(f"  Warning: {mtype} has only {len(subset)} samples")
            continue

        # ρ(G, A): Movement → Growth (Effectiveness)
        movers = subset[subset['A'] > 0]
        if len(movers) > 10:
            rho_G_A, p_G_A = spearmanr(movers['A'], movers['G'])
        else:
            rho_G_A, p_G_A = np.nan, np.nan

        # ρ(A, E): Capital → Movement (Efficiency)
        rho_A_E, p_A_E = spearmanr(subset['log_E'], subset['A'])

        results.append({
            'archetype': mtype,
            'n': len(subset),
            'rho_G_A': rho_G_A,
            'p_G_A': p_G_A,
            'rho_A_E': rho_A_E,
            'p_A_E': p_A_E,
        })

    return pd.DataFrame(results)


def plot_decomposition(results_df, year, output_dir):
    """Generate decomposition figure with science journal quality.

    DESIGN PHILOSOPHY:
    - The equation layout (× and =) makes the multiplication relationship visual
    - Color encodes sign: teal = positive, coral = negative
    - Actual ρ values annotated for transparency
    - Key finding box summarizes the main takeaway
    """
    set_publication_style()

    from matplotlib.gridspec import GridSpec
    from matplotlib.patches import Patch

    # Extract data
    dG_dA = results_df['rho_G_A'].values
    dA_dE = results_df['rho_A_E'].values
    dG_dE = dG_dA * dA_dE  # Total effect
    ns = results_df['n'].values
    archetypes = results_df['archetype'].tolist()
    n_arch = len(archetypes)

    # Create figure
    fig = plt.figure(figsize=(15, 6))
    gs = GridSpec(2, 7, figure=fig,
                  height_ratios=[6, 1.2],
                  width_ratios=[3, 0.5, 3, 0.5, 3, 0.3, 1.8],
                  hspace=0.25)

    ax_eff = fig.add_subplot(gs[0, 0])
    ax_x = fig.add_subplot(gs[0, 1])
    ax_efcy = fig.add_subplot(gs[0, 2])
    ax_eq = fig.add_subplot(gs[0, 3])
    ax_total = fig.add_subplot(gs[0, 4])
    ax_legend = fig.add_subplot(gs[0, 6])
    ax_takeaway = fig.add_subplot(gs[1, :])

    x = np.arange(n_arch)
    width = 0.6

    def draw_panel(ax, values, title, ylabel):
        """Draw a single panel with consistent style."""
        # Color by sign
        bar_colors = [COLORS['positive'] if v >= 0 else COLORS['negative'] for v in values]

        bars = ax.bar(x, values, width, color=bar_colors, alpha=0.9,
                     edgecolor='white', linewidth=1.5)

        # Zero line
        ax.axhline(y=0, color=COLORS['text_dark'], linestyle='-', linewidth=1.2, zorder=1)

        # Annotate values
        for i, (bar, val) in enumerate(zip(bars, values)):
            offset = 0.012 if val >= 0 else -0.018
            va = 'bottom' if val >= 0 else 'top'
            ax.annotate(f'{val:+.3f}', xy=(i, val + offset),
                       ha='center', va=va,
                       fontsize=10, fontweight='bold',
                       color=COLORS['text_dark'])

        # Style
        ax.set_xticks(x)
        ax.set_xticklabels([DISPLAY_NAMES.get(a, a) for a in archetypes],
                          fontsize=10, fontweight='medium')
        ax.set_ylabel(ylabel, fontsize=11, fontweight='bold', labelpad=8)
        ax.set_title(title, fontsize=13, fontweight='bold', pad=12,
                    color=COLORS['text_dark'])

        # Symmetric y-axis
        max_abs = max(abs(min(values)), abs(max(values)), 0.05) * 1.4
        ax.set_ylim(-max_abs, max_abs)

        # Light grid
        ax.yaxis.grid(True, linestyle='--', alpha=0.4, color=COLORS['grid'])
        ax.set_axisbelow(True)

        ax.spines['left'].set_color(COLORS['axis'])
        ax.spines['bottom'].set_color(COLORS['axis'])

        return bars

    # Draw panels
    draw_panel(ax_eff, dG_dA, 'Effectiveness', 'ρ(G, A)\nMovement → Growth')
    draw_panel(ax_efcy, dA_dE, 'Efficiency', 'ρ(A, E)\nFunding → Movement')
    draw_panel(ax_total, dG_dE, 'Total Effect', 'ρ(G,A) × ρ(A,E)\nFunding → Growth')

    # Operators
    for ax_sym, symbol in [(ax_x, '×'), (ax_eq, '=')]:
        ax_sym.text(0.5, 0.5, symbol, fontsize=32, ha='center', va='center',
                   fontweight='bold', color=COLORS['text_medium'])
        ax_sym.axis('off')

    # Legend
    legend_elements = [
        Patch(facecolor=COLORS['zoom_in'], label=f"Zoom In (n={ns[archetypes.index('zoom_in')]:,})"),
        Patch(facecolor=COLORS['zoom_out'], label=f"Zoom Out (n={ns[archetypes.index('zoom_out')]:,})"),
        Patch(facecolor=COLORS['stayer'], label=f"Stayer (n={ns[archetypes.index('stayer')]:,})"),
        Patch(facecolor='white', label=''),
        Patch(facecolor=COLORS['positive'], label='ρ > 0 (beneficial)'),
        Patch(facecolor=COLORS['negative'], label='ρ < 0 (constraining)'),
    ]
    ax_legend.legend(handles=legend_elements, loc='center', fontsize=9,
                    frameon=True, fancybox=True, framealpha=0.95,
                    edgecolor=COLORS['grid'])
    ax_legend.axis('off')

    # Takeaway box
    ax_takeaway.axis('off')

    # Build interpretation
    interp_parts = []
    for i, arch in enumerate(archetypes):
        s_ga = '+' if dG_dA[i] >= 0 else '−'
        s_ae = '+' if dA_dE[i] >= 0 else '−'
        s_tot = '+' if dG_dE[i] >= 0 else '−'
        interp_parts.append(f"{DISPLAY_NAMES[arch]}: ({s_ga})×({s_ae})={s_tot}")

    takeaway = (
        f"DECOMPOSITION ({year}):  " + "   |   ".join(interp_parts) + "\n"
        f"Zoom In shows (+)×(+)=(+): funding enables movement that drives growth. "
        f"Stayers show constraint: funding does not produce beneficial movement."
    )

    ax_takeaway.text(0.5, 0.5, takeaway, ha='center', va='center',
                    fontsize=10, fontweight='medium',
                    transform=ax_takeaway.transAxes,
                    bbox=dict(boxstyle='round,pad=0.5',
                             facecolor='#FFF9E6',
                             edgecolor='#E6A800',
                             linewidth=1.5))

    # Title
    plt.suptitle(f'Funding Paradox Decomposition — {year}\n'
                 f'dG/dE = (dG/dA) × (dA/dE)',
                 fontsize=14, fontweight='bold', y=0.98, color=COLORS['text_dark'])

    plt.tight_layout(rect=[0, 0.03, 1, 0.92])

    # Save
    png_path = output_dir / f'fig_decomposition_real_{year}.png'
    pdf_path = output_dir / f'fig_decomposition_real_{year}.pdf'
    plt.savefig(png_path, dpi=300, bbox_inches='tight')
    plt.savefig(pdf_path, bbox_inches='tight')
    print(f"  Saved: {png_path.name} and {pdf_path.name}")
    plt.close()

    return png_path


def main():
    print("="*60)
    print("Generating Decomposition Figures by Year")
    print("Message: Commit to adaptation - first direction, then speed")
    print("="*60)

    summary = []

    for year in [2023, 2024, 2025]:
        df = load_data_for_year(year)
        results = compute_slopes(df)
        results['year'] = year
        summary.append(results)

        print(f"\n  Results for {year}:")
        print(f"    {'Archetype':<12} {'ρ(G,A)':>10} {'ρ(A,E)':>10} {'Total':>10}")
        print(f"    {'-'*12} {'-'*10} {'-'*10} {'-'*10}")
        for _, row in results.iterrows():
            total = row['rho_G_A'] * row['rho_A_E']
            print(f"    {row['archetype']:<12} {row['rho_G_A']:>+10.3f} {row['rho_A_E']:>+10.3f} {total:>+10.4f}")

        plot_decomposition(results, year, OUTPUT_DIR)

    # Summary
    all_results = pd.concat(summary, ignore_index=True)

    print("\n" + "="*60)
    print("SUMMARY: ρ(G,A) by Year — Movement → Growth")
    print("="*60)
    print(all_results.pivot(index='archetype', columns='year', values='rho_G_A').to_string())

    print("\n" + "="*60)
    print("SUMMARY: ρ(A,E) by Year — Funding → Movement")
    print("="*60)
    print(all_results.pivot(index='archetype', columns='year', values='rho_A_E').to_string())

    print(f"\nAll figures saved to: {OUTPUT_DIR}")


if __name__ == '__main__':
    main()
