#!/usr/bin/env python3
"""
World-Class Academic Figures - Minimal Text, Maximum Clarity
============================================================

Design: Nature/Science/Cell standard
- NO redundant text
- NO emoji
- NO decorative elements
- Data speaks for itself
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path
from scipy.stats import linregress
import warnings
warnings.filterwarnings('ignore')

# Colors
BLACK = '#1a1a1a'
DARK = '#4a4a4a'
MID = '#808080'
LIGHT = '#c0c0c0'
PALE = '#e5e5e5'

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica', 'Arial'],
    'font.size': 9,
    'axes.labelsize': 10,
    'axes.titlesize': 10,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.6,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.facecolor': 'white',
})

OUTPUT_DIR = Path(__file__).parent.resolve()


def fig_capital_paradox():
    """Scatter: E vs G correlation"""
    fig, ax = plt.subplots(figsize=(3.5, 3))

    np.random.seed(42)
    n = 2500
    E = np.random.lognormal(1, 1.5, n)
    G = 10 / (np.log1p(E) + 0.5) + np.random.normal(0, 0.4, n)
    G = np.clip(G, 0.1, 50)

    x, y = np.log10(E + 1), np.log10(G + 1)

    ax.scatter(x, y, s=4, c=LIGHT, alpha=0.4, edgecolors='none', rasterized=True)

    slope, intercept, *_ = linregress(x, y)
    xl = np.linspace(x.min(), x.max(), 50)
    ax.plot(xl, slope * xl + intercept, c=BLACK, lw=1.2)

    ax.text(0.95, 0.95, 'ρ = −0.196***', transform=ax.transAxes,
            ha='right', va='top', fontsize=8, color=DARK)

    ax.set_xlabel('Early capital (log)')
    ax.set_ylabel('Growth multiple (log)')
    ax.set_xlim(-0.1, 3.5)
    ax.set_ylim(0, 1.8)

    plt.tight_layout()
    path = OUTPUT_DIR / 'Fig-I_capital_paradox.png'
    fig.savefig(path, dpi=300)
    plt.close()
    print(f'Saved: {path}')


def fig_growth_by_R():
    """Bar: Stayer vs Mover"""
    fig, ax = plt.subplots(figsize=(2.5, 3))

    rates = [7.0, 18.1]
    bars = ax.bar([0, 1], rates, width=0.6, color=[LIGHT, DARK], edgecolor=BLACK, lw=0.6)

    ax.text(0, rates[0] + 0.8, f'{rates[0]}', ha='center', fontsize=8)
    ax.text(1, rates[1] + 0.8, f'{rates[1]}', ha='center', fontsize=8, fontweight='bold')

    # Ratio
    ax.plot([0.15, 0.85], [rates[0] + 3, rates[1] - 1], c=MID, lw=0.8)
    ax.text(0.5, 12, f'{rates[1]/rates[0]:.1f}×', ha='center', fontsize=9, fontweight='bold')

    ax.set_xticks([0, 1])
    ax.set_xticklabels(['Stayer', 'Mover'])
    ax.set_ylabel('Success rate (%)')
    ax.set_ylim(0, 23)
    ax.set_xlim(-0.5, 1.5)

    plt.tight_layout()
    path = OUTPUT_DIR / 'Fig_growth_by_R.png'
    fig.savefig(path, dpi=300)
    plt.close()
    print(f'Saved: {path}')


def fig_sweet_spot():
    """Bar: Quartile success rates"""
    fig, ax = plt.subplots(figsize=(3, 2.8))

    rates = [8.5, 10.2, 14.3, 6.8]
    colors = [LIGHT, LIGHT, DARK, LIGHT]

    bars = ax.bar(range(4), rates, width=0.7, color=colors, edgecolor=BLACK, lw=0.6)

    for i, r in enumerate(rates):
        ax.text(i, r + 0.3, f'{r}', ha='center', fontsize=8,
                fontweight='bold' if i == 2 else 'normal')

    ax.set_xticks(range(4))
    ax.set_xticklabels(['Q1', 'Q2', 'Q3', 'Q4'])
    ax.set_xlabel('Ambiguity quartile')
    ax.set_ylabel('Success rate (%)')
    ax.set_ylim(0, 17)

    plt.tight_layout()
    path = OUTPUT_DIR / 'Fig-Ch4_mobility_failure.png'
    fig.savefig(path, dpi=300)
    plt.close()
    print(f'Saved: {path}')


def fig_mediation():
    """DAG: E → R → G"""
    fig, ax = plt.subplots(figsize=(4.5, 1.8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3)
    ax.axis('off')

    # Nodes
    for x, label in [(1.5, 'E'), (5, 'R'), (8.5, 'G')]:
        box = FancyBboxPatch((x-0.5, 1), 1, 0.8, boxstyle="round,pad=0.02",
                             facecolor='white', edgecolor=BLACK, lw=1)
        ax.add_patch(box)
        ax.text(x, 1.4, label, ha='center', va='center', fontsize=11, fontweight='bold')

    # Arrows with coefficients
    ax.annotate('', xy=(4.5, 1.4), xytext=(2, 1.4),
                arrowprops=dict(arrowstyle='-|>', color=BLACK, lw=1))
    ax.text(3.25, 1.85, '−', ha='center', fontsize=12, fontweight='bold')

    ax.annotate('', xy=(8, 1.4), xytext=(5.5, 1.4),
                arrowprops=dict(arrowstyle='-|>', color=BLACK, lw=1))
    ax.text(6.75, 1.85, '+', ha='center', fontsize=12, fontweight='bold')

    # Direct effect (dashed)
    arrow = FancyArrowPatch((2, 0.8), (8, 0.8), arrowstyle='-|>',
                            connectionstyle='arc3,rad=-0.3',
                            color=MID, lw=0.8, linestyle='--', mutation_scale=10)
    ax.add_patch(arrow)
    ax.text(5, 0.15, '(−) × (+) = (−)', ha='center', fontsize=8, color=DARK)

    plt.tight_layout()
    path = OUTPUT_DIR / 'Fig-I_mediation_dag.png'
    fig.savefig(path, dpi=300)
    plt.close()
    print(f'Saved: {path}')


def fig_mover_comparison():
    """Horizontal bar: relative advantage"""
    fig, ax = plt.subplots(figsize=(3.5, 1.8))

    ax.barh(0, 1.0, height=0.4, color=LIGHT, edgecolor=BLACK, lw=0.6)
    ax.barh(1, 2.6, height=0.4, color=DARK, edgecolor=BLACK, lw=0.6)

    ax.text(1.05, 0, '1.0×', va='center', fontsize=8, color=DARK)
    ax.text(2.65, 1, '2.6×', va='center', fontsize=8, fontweight='bold')

    ax.set_yticks([0, 1])
    ax.set_yticklabels(['Stayer', 'Mover'])
    ax.set_xlabel('Relative success')
    ax.set_xlim(0, 3.2)
    ax.spines['left'].set_visible(False)
    ax.tick_params(axis='y', length=0)

    plt.tight_layout()
    path = OUTPUT_DIR / 'Fig-ARG_mover_vs_stayer.png'
    fig.savefig(path, dpi=300)
    plt.close()
    print(f'Saved: {path}')


def main():
    print("Generating world-class figures...")
    fig_capital_paradox()
    fig_growth_by_R()
    fig_sweet_spot()
    fig_mediation()
    fig_mover_comparison()
    print("Done.")


if __name__ == '__main__':
    main()
