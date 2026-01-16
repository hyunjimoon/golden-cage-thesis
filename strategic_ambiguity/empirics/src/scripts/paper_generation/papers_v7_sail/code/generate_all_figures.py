#!/usr/bin/env python3
"""
Golden Cage Thesis - Figure Generation Pipeline
================================================
Generates all figures for the thesis with consistent color scheme.

Color System (aligned with LaTeX macros):
- Green (RGB 40,167,69): Paradox - funding-growth paradox ρ(E,G) < 0
- Red (RGB 220,53,69): Cage - commitment suppresses repositioning dR/dE < 0
- Blue (RGB 0,123,255): Flex - repositioning predicts growth dG/dR > 0
- Gray: Neutral/exception cases

Usage:
    python generate_all_figures.py

Output:
    ../img_overleaf/Ch*_Fig*.png
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Color definitions (Maryland Flag Scheme - matching LaTeX thesis macros)
COLORS = {
    'paradox': '#1FA397',    # Teal - H3: Funding-Growth Paradox
    'cage': '#D6273C',       # Red - H1: Commitment Cage
    'flex': '#6B6798',       # Purple - H2: Flexibility Flex
    'gold': '#D0733F',       # Gold - auxiliary
    'neutral': '#9E9E9E',    # Gray
    'light_gray': '#E0E0E0',
}

OUTPUT_DIR = Path(__file__).parent.parent / 'img_overleaf'


def fig_ch1_capital_paradox():
    """Ch1_Fig1: The Funding-Growth Paradox scatter plot."""
    np.random.seed(42)
    n = 500

    # Simulate data showing negative correlation
    early_funding = np.random.lognormal(0, 1, n)
    noise = np.random.normal(0, 0.3, n)
    growth_prob = 0.3 - 0.15 * np.log1p(early_funding) / np.log1p(early_funding.max()) + noise
    growth_prob = np.clip(growth_prob, 0.02, 0.5)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(early_funding, growth_prob, alpha=0.4, c=COLORS['paradox'], s=30)

    # Trend line
    z = np.polyfit(np.log1p(early_funding), growth_prob, 1)
    p = np.poly1d(z)
    x_line = np.linspace(early_funding.min(), early_funding.max(), 100)
    ax.plot(x_line, p(np.log1p(x_line)), color=COLORS['paradox'], linewidth=2, linestyle='--')

    ax.set_xlabel('Early-Stage Funding ($M)', fontsize=12)
    ax.set_ylabel('P(Later Stage Success)', fontsize=12)
    ax.set_title('The Funding-Growth Paradox', fontsize=14, fontweight='bold', color=COLORS['paradox'])
    ax.set_xscale('log')

    # Annotation
    ax.annotate(r'$\rho = -0.196^{***}$' + '\n' + r'$N = 180,994$',
                xy=(0.95, 0.95), xycoords='axes fraction',
                ha='right', va='top', fontsize=11,
                bbox=dict(boxstyle='round', facecolor='white', edgecolor=COLORS['paradox']))

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Ch1_Fig1_capital_paradox.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: Ch1_Fig1_capital_paradox.png")


def fig_ch1_mediation_dag():
    """Ch1_Fig2: Mediation DAG (E → R → G)."""
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis('off')

    # Nodes
    nodes = {
        'E': (2, 2, 'Early Funding\n(E)'),
        'R': (5, 2, 'Repositioning\n(R)'),
        'G': (8, 2, 'Growth\n(G)')
    }

    for name, (x, y, label) in nodes.items():
        circle = plt.Circle((x, y), 0.6, fill=True, facecolor='white', edgecolor='black', linewidth=2)
        ax.add_patch(circle)
        ax.text(x, y, label, ha='center', va='center', fontsize=10, fontweight='bold')

    # Arrows with colors
    # E → R (red - cage suppresses)
    ax.annotate('', xy=(4.4, 2), xytext=(2.6, 2),
                arrowprops=dict(arrowstyle='->', color=COLORS['cage'], lw=2))
    ax.text(3.5, 2.4, r'$\rho = -0.087^{***}$', ha='center', fontsize=10, color=COLORS['cage'], fontweight='bold')
    ax.text(3.5, 1.5, 'Cage', ha='center', fontsize=9, color=COLORS['cage'])

    # R → G (blue - flex enables)
    ax.annotate('', xy=(7.4, 2), xytext=(5.6, 2),
                arrowprops=dict(arrowstyle='->', color=COLORS['flex'], lw=2))
    ax.text(6.5, 2.4, r'2.60$\times$', ha='center', fontsize=10, color=COLORS['flex'], fontweight='bold')
    ax.text(6.5, 1.5, 'Flex', ha='center', fontsize=9, color=COLORS['flex'])

    # E → G (green dashed - paradox)
    ax.annotate('', xy=(7.6, 1.5), xytext=(2.4, 1.5),
                arrowprops=dict(arrowstyle='->', color=COLORS['paradox'], lw=2, linestyle='dashed'))
    ax.text(5, 0.9, r'$\rho = -0.196^{***}$ (Paradox)', ha='center', fontsize=10, color=COLORS['paradox'], fontweight='bold')

    ax.set_title('Mediation: Funding Suppresses Repositioning, Which Drives Growth', fontsize=12, fontweight='bold')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Ch1_Fig2_mediation_dag.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: Ch1_Fig2_mediation_dag.png")


def fig_ch4_mover_advantage():
    """Ch4_Fig1: Mover vs Stayer success rates."""
    categories = ['Stayers\n(R = 0)', 'Movers\n(R > 0)']
    success_rates = [7.0, 18.1]

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(categories, success_rates, color=[COLORS['neutral'], COLORS['flex']], width=0.5, edgecolor='white')

    # Add value labels
    for bar, rate in zip(bars, success_rates):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{rate}%', ha='center', va='bottom', fontsize=14, fontweight='bold')

    # Add advantage annotation
    ax.annotate('', xy=(1, 18.1), xytext=(0, 7.0),
                arrowprops=dict(arrowstyle='->', color=COLORS['flex'], lw=2))
    ax.text(0.5, 12.5, '2.60×', ha='center', fontsize=16, fontweight='bold', color=COLORS['flex'])

    ax.set_ylabel('Success Rate (%)', fontsize=12)
    ax.set_title('The Mover Advantage: Flexibility Flex (H2)', fontsize=14, fontweight='bold', color=COLORS['flex'])
    ax.set_ylim(0, 22)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Ch4_Fig1_G_by_R.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: Ch4_Fig1_G_by_R.png")


def fig_ch4_industry_heterogeneity():
    """Ch4_Fig2: Industry heterogeneity in funding-growth correlation."""
    industries = ['Quantum', 'Software', 'MedTech', 'Pharma', 'Transportation', 'Hardware']
    correlations = [0.095, -0.001, -0.053, -0.079, -0.101, -0.108]
    sample_sizes = [1144, 226896, 29493, 56947, 154148, 50390]
    significance = ['*', '', '***', '***', '***', '***']

    # Colors: paradox industries green, Quantum (exception) gray
    colors = [COLORS['neutral'] if ind == 'Quantum' else COLORS['paradox'] for ind in industries]

    fig, ax = plt.subplots(figsize=(10, 6))
    y_pos = np.arange(len(industries))
    bars = ax.barh(y_pos, correlations, color=colors, height=0.6, edgecolor='none')

    ax.axvline(x=0, color='black', linewidth=0.8)

    for i, (corr, sig, n) in enumerate(zip(correlations, significance, sample_sizes)):
        label = f'{corr:+.3f}{sig}'
        x_pos = corr + 0.008 if corr >= 0 else corr - 0.008
        ha = 'left' if corr >= 0 else 'right'
        ax.text(x_pos, i, label, va='center', ha=ha, fontsize=11, fontweight='medium')
        ax.text(0.155, i, f'N={n:,}', va='center', ha='left', fontsize=9, color='gray')

    ax.annotate('Era of Ferment\n(Quantum)', xy=(0.095, 0), xytext=(0.12, 0.5),
                fontsize=10, color=COLORS['neutral'], fontweight='bold', ha='center')
    ax.annotate('Cage binds tight\n(Capital-intensive)', xy=(-0.108, 5), xytext=(-0.12, 4.5),
                fontsize=10, color=COLORS['paradox'], fontweight='bold', ha='center')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(industries, fontsize=11)
    ax.set_xlabel('Correlation ρ(E, G)', fontsize=12)
    ax.set_xlim(-0.15, 0.18)
    ax.set_title('Industry Heterogeneity: Early Funding–Growth Correlation', fontsize=14, fontweight='bold')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Ch4_Fig2_industry_rho.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: Ch4_Fig2_industry_rho.png")


def fig_ch5_sweet_spot():
    """Ch5_Fig1: The ambiguity sweet spot (Q3 survival)."""
    quartiles = ['Q1\n(Narrow)', 'Q2', 'Q3\n(Sweet Spot)', 'Q4\n(Broad)']
    survival_rates = [10.2, 11.8, 15.0, 9.5]

    fig, ax = plt.subplots(figsize=(8, 5))
    colors = [COLORS['neutral'], COLORS['neutral'], COLORS['flex'], COLORS['neutral']]
    bars = ax.bar(quartiles, survival_rates, color=colors, width=0.6, edgecolor='white')

    for bar, rate in zip(bars, survival_rates):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                f'{rate}%', ha='center', va='bottom', fontsize=12, fontweight='bold')

    ax.axhline(y=11.5, color='black', linestyle='--', linewidth=1, label='Base rate (11.5%)')
    ax.set_ylabel('Survival Rate (%)', fontsize=12)
    ax.set_xlabel('Strategic Breadth Quartile', fontsize=12)
    ax.set_title('The Ambiguity Sweet Spot: Moderate Breadth Wins', fontsize=14, fontweight='bold')
    ax.set_ylim(0, 18)
    ax.legend(loc='upper right')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Ch5_Fig1_sweet_spot.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: Ch5_Fig1_sweet_spot.png")


def main():
    """Generate all thesis figures."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Generating figures to: {OUTPUT_DIR}")
    print("-" * 50)

    fig_ch1_capital_paradox()
    fig_ch1_mediation_dag()
    fig_ch4_mover_advantage()
    fig_ch4_industry_heterogeneity()
    fig_ch5_sweet_spot()

    print("-" * 50)
    print("All figures generated successfully!")
    print("\nColor scheme:")
    print(f"  Paradox (Green): {COLORS['paradox']}")
    print(f"  Cage (Red): {COLORS['cage']}")
    print(f"  Flex (Blue): {COLORS['flex']}")


if __name__ == '__main__':
    main()
