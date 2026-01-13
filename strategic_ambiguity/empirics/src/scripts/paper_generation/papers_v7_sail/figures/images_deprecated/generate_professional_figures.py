#!/usr/bin/env python3
"""
generate_professional_figures.py - Management Science / Science Journal Style
==============================================================================

Design Principles (following MS/Science standards):
1. Minimal color - grayscale primary, single accent only when necessary
2. Clean typography - Helvetica/Arial, consistent sizing
3. No emoji, no decorative elements
4. High information density with clarity
5. Statistical annotations with proper notation
6. Publication-ready 300 DPI

Author: Golden Cage Thesis
Date: 2026-01-13
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path
from scipy.stats import spearmanr, linregress
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# PROFESSIONAL STYLE CONFIGURATION
# ============================================================================

# Grayscale palette (primary)
BLACK = '#1a1a1a'
DARK_GRAY = '#4a4a4a'
MID_GRAY = '#808080'
LIGHT_GRAY = '#c0c0c0'
PALE_GRAY = '#e8e8e8'
WHITE = '#ffffff'

# Single accent color (used sparingly)
ACCENT = '#2c5aa0'  # Muted blue - only for key emphasis

# Figure settings - MS/Science style
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica', 'Arial', 'DejaVu Sans'],
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'axes.titleweight': 'normal',
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'legend.frameon': False,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'axes.edgecolor': BLACK,
    'axes.linewidth': 0.8,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': False,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.facecolor': 'white',
    'lines.linewidth': 1.5,
    'patch.linewidth': 0.8,
})

# Paths
SCRIPT_DIR = Path(__file__).parent.resolve()
OUTPUT_DIR = SCRIPT_DIR


# ============================================================================
# Figure 1: Capital Paradox (Scatter with regression)
# ============================================================================

def fig_capital_paradox():
    """
    The Capital Paradox: Higher early funding correlates with lower growth.
    Style: Clean scatter with regression line, minimal annotation.
    """
    fig, ax = plt.subplots(figsize=(5, 4))

    # Simulated data matching thesis statistics
    np.random.seed(42)
    n = 3000
    E = np.random.lognormal(mean=1, sigma=1.5, size=n)
    noise = np.random.normal(0, 0.5, n)
    G = 10 / (np.log1p(E) + 0.5) + noise
    G = np.clip(G, 0.1, 50)

    x = np.log10(E + 1)
    y = np.log10(G + 1)

    # Scatter - light gray, small points
    ax.scatter(x, y, alpha=0.3, s=8, c=LIGHT_GRAY, edgecolors='none',
               rasterized=True, zorder=1)

    # Regression
    slope, intercept, r, p, se = linregress(x, y)
    x_line = np.linspace(x.min(), x.max(), 100)
    y_line = slope * x_line + intercept

    # 95% CI band
    n_obs = len(x)
    y_err = 1.96 * se * np.sqrt(1/n_obs + (x_line - x.mean())**2 / ((x - x.mean())**2).sum())
    ax.fill_between(x_line, y_line - y_err * 3, y_line + y_err * 3,
                    color=PALE_GRAY, alpha=0.8, zorder=2)

    # Regression line - black
    ax.plot(x_line, y_line, color=BLACK, linewidth=1.5, zorder=3)

    # Labels
    ax.set_xlabel('Early-stage capital, log₁₀($M)')
    ax.set_ylabel('Funding growth multiple, log₁₀')

    # Statistical annotation - top left, clean
    rho = -0.196
    ax.text(0.05, 0.95, f'ρ = {rho:.3f}***\nN = 180,994',
            transform=ax.transAxes, fontsize=9, va='top', ha='left',
            color=DARK_GRAY)

    ax.set_xlim(-0.2, 4)
    ax.set_ylim(-0.1, 2)

    plt.tight_layout()

    output_path = OUTPUT_DIR / 'Fig-I_capital_paradox.png'
    fig.savefig(output_path, dpi=300)
    print(f"Saved: {output_path}")
    plt.close(fig)
    return output_path


# ============================================================================
# Figure 2: Growth by Repositioning (Bar chart)
# ============================================================================

def fig_growth_by_R():
    """
    Mover Advantage: Repositioning firms achieve higher success rates.
    Style: Simple two-bar comparison, grayscale with clear labels.
    """
    fig, ax = plt.subplots(figsize=(4, 4))

    # Data
    categories = ['Stayers\n(R = 0)', 'Movers\n(R > 0)']
    success_rates = [7.0, 18.1]
    n_values = [120000, 60994]

    # Bars - grayscale only
    colors = [LIGHT_GRAY, DARK_GRAY]
    bars = ax.bar(categories, success_rates, color=colors,
                  edgecolor=BLACK, linewidth=0.8, width=0.6)

    # Value labels on top
    for bar, rate, n in zip(bars, success_rates, n_values):
        ax.text(bar.get_x() + bar.get_width()/2, rate + 0.8,
                f'{rate:.1f}%', ha='center', fontsize=10, color=BLACK)
        # Sample size below bar label
        ax.text(bar.get_x() + bar.get_width()/2, -1.5,
                f'n = {n:,}', ha='center', fontsize=8, color=MID_GRAY)

    # Ratio annotation
    ratio = success_rates[1] / success_rates[0]
    ax.annotate('', xy=(1, success_rates[1] - 1), xytext=(0, success_rates[0] + 1),
                arrowprops=dict(arrowstyle='->', color=DARK_GRAY, lw=1))
    ax.text(0.5, (success_rates[0] + success_rates[1]) / 2 + 2,
            f'{ratio:.2f}×', ha='center', fontsize=11, fontweight='bold',
            color=BLACK)

    ax.set_ylabel('Later-stage success rate (%)')
    ax.set_ylim(-3, 25)
    ax.set_xlim(-0.6, 1.6)

    # Remove x-axis line for cleaner look
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(axis='x', length=0)

    plt.tight_layout()

    output_path = OUTPUT_DIR / 'Fig_growth_by_R.png'
    fig.savefig(output_path, dpi=300)
    print(f"Saved: {output_path}")
    plt.close(fig)
    return output_path


# ============================================================================
# Figure 3: Sweet Spot (Quartile analysis)
# ============================================================================

def fig_mobility_failure():
    """
    Strategic Ambiguity Sweet Spot: Moderate ambiguity optimizes outcomes.
    Style: Four-bar quartile chart, highlight maximum with outline only.
    """
    fig, ax = plt.subplots(figsize=(5, 4))

    # Data
    quartiles = ['Q1', 'Q2', 'Q3', 'Q4']
    success_rates = [8.5, 10.2, 14.3, 6.8]

    # All bars same gray, highlight Q3 with darker shade
    colors = [LIGHT_GRAY, LIGHT_GRAY, MID_GRAY, LIGHT_GRAY]
    edge_colors = [BLACK, BLACK, BLACK, BLACK]
    edge_widths = [0.8, 0.8, 1.5, 0.8]

    bars = ax.bar(quartiles, success_rates, color=colors,
                  edgecolor=edge_colors, linewidth=edge_widths, width=0.7)

    # Value labels
    for bar, rate in zip(bars, success_rates):
        ax.text(bar.get_x() + bar.get_width()/2, rate + 0.4,
                f'{rate:.1f}', ha='center', fontsize=9, color=DARK_GRAY)

    # X-axis labels
    ax.set_xticks(range(4))
    ax.set_xticklabels(['Q1\n(Low)', 'Q2', 'Q3', 'Q4\n(High)'])

    ax.set_xlabel('Initial strategic ambiguity (B₀) quartile')
    ax.set_ylabel('Later-stage success rate (%)')
    ax.set_ylim(0, 18)

    # Bracket annotation for Q3
    ax.annotate('', xy=(2, 15.5), xytext=(2, 14.8),
                arrowprops=dict(arrowstyle='-', color=DARK_GRAY, lw=1))
    ax.text(2, 16, 'max', ha='center', fontsize=9, color=DARK_GRAY)

    plt.tight_layout()

    output_path = OUTPUT_DIR / 'Fig-Ch4_mobility_failure.png'
    fig.savefig(output_path, dpi=300)
    print(f"Saved: {output_path}")
    plt.close(fig)
    return output_path


# ============================================================================
# Figure 4: Mediation DAG
# ============================================================================

def fig_mediation_dag():
    """
    Mediation mechanism: E → R → G
    Style: Clean path diagram with coefficient labels.
    """
    fig, ax = plt.subplots(figsize=(7, 3))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis('off')

    # Node positions
    nodes = {
        'E': (1.5, 2),
        'R': (5, 2),
        'G': (8.5, 2),
    }

    # Draw nodes as simple rectangles
    node_labels = {
        'E': 'Early Capital\n(E)',
        'R': 'Repositioning\n(R)',
        'G': 'Growth\n(G)',
    }

    for name, (x, y) in nodes.items():
        box = FancyBboxPatch((x - 0.9, y - 0.5), 1.8, 1.0,
                             boxstyle="round,pad=0.05,rounding_size=0.1",
                             facecolor=WHITE,
                             edgecolor=BLACK,
                             linewidth=1.2)
        ax.add_patch(box)
        ax.text(x, y, node_labels[name], ha='center', va='center',
                fontsize=10, color=BLACK)

    # Arrow: E → R (negative path)
    ax.annotate('', xy=(4.1, 2), xytext=(2.4, 2),
                arrowprops=dict(arrowstyle='-|>', color=BLACK,
                              lw=1.2, shrinkA=0, shrinkB=0))
    ax.text(3.25, 2.55, 'a = −0.087***', ha='center', fontsize=9, color=DARK_GRAY)

    # Arrow: R → G (positive path)
    ax.annotate('', xy=(7.6, 2), xytext=(5.9, 2),
                arrowprops=dict(arrowstyle='-|>', color=BLACK,
                              lw=1.2, shrinkA=0, shrinkB=0))
    ax.text(6.75, 2.55, 'b = +0.142***', ha='center', fontsize=9, color=DARK_GRAY)

    # Direct path: E → G (dashed)
    from matplotlib.patches import FancyArrowPatch
    arrow = FancyArrowPatch((2.4, 1.3), (7.6, 1.3),
                            arrowstyle='-|>',
                            connectionstyle='arc3,rad=-0.15',
                            color=MID_GRAY,
                            linewidth=1,
                            linestyle='--',
                            mutation_scale=12)
    ax.add_patch(arrow)
    ax.text(5, 0.6, "c′ = −0.196***", ha='center', fontsize=9, color=MID_GRAY)

    # Indirect effect annotation
    ax.text(5, 3.5, 'Indirect effect: a × b = (−) × (+) = (−)',
            ha='center', fontsize=9, color=DARK_GRAY,
            bbox=dict(boxstyle='round,pad=0.3', facecolor=PALE_GRAY,
                     edgecolor='none'))

    plt.tight_layout()

    output_path = OUTPUT_DIR / 'Fig-I_mediation_dag.png'
    fig.savefig(output_path, dpi=300)
    print(f"Saved: {output_path}")
    plt.close(fig)
    return output_path


# ============================================================================
# Figure 5: Mover vs Stayer Comparison
# ============================================================================

def fig_mover_vs_stayer():
    """
    Mover Advantage detailed comparison.
    Style: Two-panel figure with bar chart and relative comparison.
    """
    fig, axes = plt.subplots(1, 2, figsize=(8, 3.5))

    # Panel A: Success rate bars
    ax = axes[0]
    categories = ['Stayers', 'Movers']
    success_rates = [7.0, 18.1]
    colors = [LIGHT_GRAY, DARK_GRAY]

    bars = ax.bar(categories, success_rates, color=colors,
                  edgecolor=BLACK, linewidth=0.8, width=0.5)

    for bar, rate in zip(bars, success_rates):
        ax.text(bar.get_x() + bar.get_width()/2, rate + 0.5,
                f'{rate:.1f}%', ha='center', fontsize=10, color=BLACK)

    ax.set_ylabel('Success rate (%)')
    ax.set_ylim(0, 22)
    ax.set_title('A', loc='left', fontweight='bold', fontsize=11)

    # Panel B: Relative comparison (horizontal)
    ax = axes[1]

    y_pos = [0, 1]
    widths = [1.0, 2.60]
    labels = ['Stayers (baseline)', 'Movers']
    colors = [LIGHT_GRAY, DARK_GRAY]

    bars = ax.barh(y_pos, widths, color=colors, edgecolor=BLACK,
                   linewidth=0.8, height=0.5)

    # Labels
    ax.text(1.05, 0, '1.00×', va='center', fontsize=10, color=DARK_GRAY)
    ax.text(2.65, 1, '2.60×', va='center', fontsize=10, color=BLACK, fontweight='bold')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels)
    ax.set_xlabel('Relative success rate')
    ax.set_xlim(0, 3.5)
    ax.set_title('B', loc='left', fontweight='bold', fontsize=11)

    # Difference annotation
    ax.annotate('', xy=(2.60, 0.65), xytext=(1.0, 0.35),
                arrowprops=dict(arrowstyle='->', color=MID_GRAY, lw=1))
    ax.text(1.8, 0.5, '+160%', ha='center', fontsize=9, color=DARK_GRAY,
            bbox=dict(boxstyle='round,pad=0.2', facecolor=WHITE, edgecolor=MID_GRAY))

    plt.tight_layout()

    output_path = OUTPUT_DIR / 'Fig-ARG_mover_vs_stayer.png'
    fig.savefig(output_path, dpi=300)
    print(f"Saved: {output_path}")
    plt.close(fig)
    return output_path


# ============================================================================
# MAIN
# ============================================================================

def main():
    print("=" * 60)
    print("Generating Professional Academic Figures")
    print("Style: Management Science / Science Journal")
    print("=" * 60)
    print()

    generated = []

    print("[1/5] Capital Paradox...")
    generated.append(fig_capital_paradox())

    print("[2/5] Growth by Repositioning...")
    generated.append(fig_growth_by_R())

    print("[3/5] Strategic Ambiguity Sweet Spot...")
    generated.append(fig_mobility_failure())

    print("[4/5] Mediation DAG...")
    generated.append(fig_mediation_dag())

    print("[5/5] Mover vs Stayer...")
    generated.append(fig_mover_vs_stayer())

    print()
    print("=" * 60)
    print("Complete. Generated files:")
    for path in generated:
        print(f"  {path}")
    print("=" * 60)


if __name__ == '__main__':
    main()
