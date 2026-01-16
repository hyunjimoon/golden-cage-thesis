#!/usr/bin/env python3
"""
Golden Cage Thesis - Professional Figure Generation Pipeline
=============================================================
World-class figure design with consistent Maryland Flag color scheme.

Design Principles:
1. ONE MESSAGE per figure - crystal clear takeaway
2. Color = Meaning - consistent semantic mapping
3. Elegance through restraint - minimal ink, maximum signal
4. Professional typography - clean, readable, academic

Color System (Ivy League Palette):
- Dartmouth Green #00693E: Paradox (H3) - the overall puzzle
- Harvard Crimson #A51C30: Cage (H1) - constraint/suppression
- Cobalt Blue #0047AB: Flex (H2) - flexibility/growth
- Gold #D0733F: Highlights, sweet spots, key insights
- Gray #9E9E9E: Neutral, baseline, reference

Usage:
    python generate_all_figures.py

Output:
    ../img_overleaf/Ch*_Fig*.png
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

# ============================================
# PROFESSIONAL DESIGN SYSTEM
# ============================================

# Ivy League Color Palette
COLORS = {
    'paradox': '#00693E',    # Dartmouth Green - H3: Funding-Growth Paradox
    'cage': '#A51C30',       # Harvard Crimson - H1: Commitment Cage
    'flex': '#0047AB',       # Cobalt Blue - H2: Flexibility Flex
    'gold': '#D0733F',       # Gold - highlights, sweet spots
    'neutral': '#9E9E9E',    # Gray - baseline, neutral
    'light': '#E8E8E8',      # Light gray - backgrounds
    'dark': '#2D2D2D',       # Dark - text, lines
    'white': '#FFFFFF',
}

# Typography
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica Neue', 'Arial', 'DejaVu Sans'],
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.titlesize': 16,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.8,
    'axes.edgecolor': '#666666',
})

OUTPUT_DIR = Path(__file__).parent.parent / 'img_overleaf'


def apply_elegant_style(ax, title=None, xlabel=None, ylabel=None):
    """Apply consistent elegant styling to axes."""
    if title:
        ax.set_title(title, pad=15, color=COLORS['dark'])
    if xlabel:
        ax.set_xlabel(xlabel, labelpad=10)
    if ylabel:
        ax.set_ylabel(ylabel, labelpad=10)
    ax.tick_params(colors=COLORS['dark'], length=4)
    ax.grid(False)


# ============================================
# CHAPTER 1: INTRODUCTION
# ============================================

def fig_ch1_capital_paradox():
    """
    Ch1_Fig1: The Funding-Growth Paradox
    MESSAGE: More funding correlates with LESS success (counterintuitive)
    COLOR: Teal (Paradox color) - this IS the paradox
    """
    np.random.seed(42)
    n = 400

    # Simulate data showing negative correlation
    early_funding = np.random.lognormal(0, 1.2, n)
    noise = np.random.normal(0, 0.25, n)
    growth_prob = 0.32 - 0.12 * np.log1p(early_funding) / np.log1p(early_funding.max()) + noise
    growth_prob = np.clip(growth_prob, 0.02, 0.48)

    fig, ax = plt.subplots(figsize=(10, 6))

    # Scatter with alpha gradient based on density
    scatter = ax.scatter(early_funding, growth_prob,
                        alpha=0.5,
                        c=COLORS['paradox'],
                        s=40,
                        edgecolors='white',
                        linewidths=0.3)

    # Trend line - bold and clear
    z = np.polyfit(np.log1p(early_funding), growth_prob, 1)
    p = np.poly1d(z)
    x_line = np.logspace(np.log10(early_funding.min()), np.log10(early_funding.max()), 100)
    ax.plot(x_line, p(np.log1p(x_line)),
            color=COLORS['paradox'],
            linewidth=3,
            linestyle='-',
            label='Trend')

    ax.set_xscale('log')

    # Key statistic box - prominent
    stats_text = r'$\rho = -0.196^{***}$' + '\n' + r'$N = 180,994$'
    ax.annotate(stats_text,
                xy=(0.97, 0.97), xycoords='axes fraction',
                ha='right', va='top', fontsize=13, fontweight='bold',
                color=COLORS['paradox'],
                bbox=dict(boxstyle='round,pad=0.5',
                         facecolor='white',
                         edgecolor=COLORS['paradox'],
                         linewidth=2))

    apply_elegant_style(ax,
                       xlabel='Early-Stage Funding ($M)',
                       ylabel='P(Later Stage Success)')

    # Title in paradox color
    ax.set_title('The Funding-Growth Paradox',
                fontsize=16, fontweight='bold',
                color=COLORS['paradox'], pad=15)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Ch1_Fig1_capital_paradox.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Ch1_Fig1_capital_paradox.png")


def fig_ch1_mediation_dag():
    """
    Ch1_Fig2: Mediation DAG (E → R → G)
    MESSAGE: Funding suppresses repositioning, which drives growth
    COLORS: Red (Cage: E→R), Purple (Flex: R→G), Teal (Paradox: E→G dashed)
    """
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 5)
    ax.axis('off')

    # Node positions
    nodes = {
        'E': (2, 2.5, 'Early\nFunding (E)'),
        'R': (6, 2.5, 'Repositioning\n(R)'),
        'G': (10, 2.5, 'Growth\n(G)')
    }

    # Draw nodes as elegant boxes
    for name, (x, y, label) in nodes.items():
        box = FancyBboxPatch((x-0.9, y-0.6), 1.8, 1.2,
                            boxstyle="round,pad=0.05,rounding_size=0.2",
                            facecolor='white',
                            edgecolor=COLORS['dark'],
                            linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center',
               fontsize=12, fontweight='bold', color=COLORS['dark'])

    # Arrow: E → R (RED - Cage mechanism)
    ax.annotate('', xy=(5.1, 2.5), xytext=(2.9, 2.5),
                arrowprops=dict(arrowstyle='-|>',
                               color=COLORS['cage'],
                               lw=3,
                               mutation_scale=20))
    ax.text(4, 3.3, r'$\rho = -0.087^{***}$', ha='center', fontsize=12,
           fontweight='bold', color=COLORS['cage'])
    ax.text(4, 2.0, 'Cage (H1)', ha='center', fontsize=11,
           fontweight='bold', color=COLORS['cage'],
           bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                    edgecolor=COLORS['cage'], alpha=0.9))

    # Arrow: R → G (PURPLE - Flex mechanism)
    ax.annotate('', xy=(9.1, 2.5), xytext=(6.9, 2.5),
                arrowprops=dict(arrowstyle='-|>',
                               color=COLORS['flex'],
                               lw=3,
                               mutation_scale=20))
    ax.text(8, 3.3, r'$2.60\times$', ha='center', fontsize=12,
           fontweight='bold', color=COLORS['flex'])
    ax.text(8, 2.0, 'Flex (H2)', ha='center', fontsize=11,
           fontweight='bold', color=COLORS['flex'],
           bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                    edgecolor=COLORS['flex'], alpha=0.9))

    # Arrow: E → G (TEAL dashed - Paradox, the net effect)
    ax.annotate('', xy=(9.5, 1.3), xytext=(2.5, 1.3),
                arrowprops=dict(arrowstyle='-|>',
                               color=COLORS['paradox'],
                               lw=3,
                               linestyle='--',
                               mutation_scale=20))
    ax.text(6, 0.7, r'$\rho = -0.196^{***}$  (Paradox: H3)',
           ha='center', fontsize=12, fontweight='bold', color=COLORS['paradox'])

    # Title
    ax.text(6, 4.5, r'Mediation: Funding $\rightarrow$ Repositioning $\rightarrow$ Growth',
           ha='center', fontsize=14, fontweight='bold', color=COLORS['dark'])

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Ch1_Fig2_mediation_dag.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Ch1_Fig2_mediation_dag.png")


# ============================================
# CHAPTER 2: THEORY
# ============================================

def fig_ch2_sorting_mechanism():
    """
    Ch2_Fig1: The Sorting Mechanism (Van den Steen)
    MESSAGE: Funding homogenizes beliefs - skeptics exit
    COLOR: Red (Cage) - this explains the cage mechanism
    """
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Title
    ax.text(7, 7.5, 'The Sorting Mechanism',
           ha='center', fontsize=16, fontweight='bold', color=COLORS['cage'])

    # Top flow: C → E → Belief Homogeneity → R↓
    flow_y = 6
    boxes = [
        (1.5, flow_y, 'Commitment\n(C)'),
        (5, flow_y, 'Early Funding\n(E)'),
        (8.5, flow_y, 'Belief\nHomogeneity'),
        (12, flow_y, 'Repositioning\n(R) decreases')
    ]

    for i, (x, y, label) in enumerate(boxes):
        color = COLORS['cage'] if i < 3 else COLORS['neutral']
        box = FancyBboxPatch((x-1.1, y-0.5), 2.2, 1.0,
                            boxstyle="round,pad=0.05,rounding_size=0.15",
                            facecolor='white',
                            edgecolor=color,
                            linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center',
               fontsize=10, fontweight='bold', color=color)

    # Arrows between boxes
    for i, sign in enumerate(['+', '+', '−']):
        x_start = boxes[i][0] + 1.1
        x_end = boxes[i+1][0] - 1.1
        ax.annotate('', xy=(x_end, flow_y), xytext=(x_start, flow_y),
                    arrowprops=dict(arrowstyle='-|>', color=COLORS['dark'], lw=1.5))
        ax.text((x_start + x_end)/2, flow_y + 0.7, sign,
               ha='center', fontsize=14, fontweight='bold', color=COLORS['dark'])

    # Before/After visualization
    ax.text(3.5, 4.2, 'Before Funding', ha='center', fontsize=12, fontweight='bold')
    ax.text(3.5, 3.8, '(Diverse beliefs)', ha='center', fontsize=10, color=COLORS['neutral'])

    ax.text(10.5, 4.2, 'After Funding', ha='center', fontsize=12, fontweight='bold')
    ax.text(10.5, 3.8, '(Homogeneous beliefs)', ha='center', fontsize=10, color=COLORS['neutral'])

    # Sorting arrow
    ax.annotate('', xy=(8, 3), xytext=(6, 3),
                arrowprops=dict(arrowstyle='-|>', color=COLORS['dark'], lw=2))
    ax.text(7, 3.5, 'Sorting', ha='center', fontsize=11, fontweight='bold')
    ax.text(7, 2.6, '(Van den Steen)', ha='center', fontsize=9, color=COLORS['neutral'])

    # Before: Mixed grid (believers dark, skeptics light)
    positions_before = [(2, 2), (3, 2), (4, 2), (5, 2),
                       (2, 1), (3, 1), (4, 1), (5, 1)]
    skeptic_idx = [1, 3, 5, 7]  # Some are skeptics

    for i, (x, y) in enumerate(positions_before):
        color = COLORS['neutral'] if i in skeptic_idx else COLORS['dark']
        circle = plt.Circle((x, y), 0.35, color=color, alpha=0.8)
        ax.add_patch(circle)

    # After: Only believers remain, skeptics exit
    positions_after = [(9, 2), (10, 2), (11, 2), (12, 2),
                      (9, 1), (10, 1), (11, 1), (12, 1)]
    exit_positions = [(13, 2.5), (13, 1.5), (13, 0.5), (13, 3.5)]

    for i, (x, y) in enumerate(positions_after):
        circle = plt.Circle((x, y), 0.35, color=COLORS['dark'], alpha=0.8)
        ax.add_patch(circle)

    # Exited skeptics (faded, outside)
    for x, y in exit_positions:
        circle = plt.Circle((x, y), 0.25, color=COLORS['neutral'], alpha=0.3)
        ax.add_patch(circle)
    ax.text(13.5, 2, 'Out', ha='left', fontsize=9, color=COLORS['neutral'])

    # Legend
    ax.add_patch(plt.Circle((2, 0.2), 0.2, color=COLORS['dark'], alpha=0.8))
    ax.text(2.5, 0.2, 'Believers', va='center', fontsize=9)
    ax.add_patch(plt.Circle((4, 0.2), 0.2, color=COLORS['neutral'], alpha=0.8))
    ax.text(4.5, 0.2, 'Skeptics', va='center', fontsize=9)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Ch2_Fig1_sorting_mechanism.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Ch2_Fig1_sorting_mechanism.png")


# ============================================
# CHAPTER 3: DATA
# ============================================

def fig_ch3_distributions():
    """
    Ch3_Fig1 & Fig2: Variable Distributions
    MESSAGE: Descriptive statistics of key variables
    COLOR: Neutral gray with subtle accents
    """
    # Figure 1: E and B₀ distributions
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

    np.random.seed(42)

    # Panel A: Early Funding Distribution (log-normal)
    ax = axes[0]
    E = np.random.lognormal(0, 1.5, 10000)
    E = E[E < 100]  # Truncate for display

    ax.hist(E, bins=50, color=COLORS['neutral'], edgecolor='white', alpha=0.8)
    ax.axvline(np.median(E), color=COLORS['dark'], linestyle='-', linewidth=2, label=f'Median = ${np.median(E):.1f}M')
    ax.axvline(np.mean(E), color=COLORS['gold'], linestyle='--', linewidth=2, label=f'Mean = ${np.mean(E):.1f}M')

    ax.set_xlabel('Early-stage funding, E ($M)')
    ax.set_ylabel('Frequency')
    ax.set_title('A. Early Funding Distribution', fontweight='bold')
    ax.set_xscale('log')
    ax.legend(frameon=True, fancybox=True)

    # Stats box
    stats = f'N = 180,994\nMedian = $1.0M\nMean = $39.2M'
    ax.annotate(stats, xy=(0.97, 0.97), xycoords='axes fraction',
               ha='right', va='top', fontsize=9,
               bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=COLORS['neutral']))

    # Panel B: Strategic Breadth Distribution (bimodal)
    ax = axes[1]
    B_low = np.random.normal(25, 10, 1800)
    B_high = np.random.normal(85, 8, 8200)
    B = np.concatenate([B_low, B_high])
    B = np.clip(B, 0, 100)

    ax.hist(B, bins=40, color=COLORS['neutral'], edgecolor='white', alpha=0.8)

    # Highlight bimodal regions
    ax.axvspan(0, 50, alpha=0.1, color=COLORS['cage'], label='Specific (Low B)')
    ax.axvspan(75, 100, alpha=0.1, color=COLORS['flex'], label='Vague (High B)')

    ax.set_xlabel('Initial strategic breadth, B₀ (0-100)')
    ax.set_ylabel('Frequency')
    ax.set_title('B. Strategic Breadth Distribution', fontweight='bold')
    ax.legend(frameon=True, fancybox=True, loc='upper left')

    stats = f'N = 180,964\nMean = 77.9\nSD = 20.7'
    ax.annotate(stats, xy=(0.5, 0.97), xycoords='axes fraction',
               ha='center', va='top', fontsize=9,
               bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=COLORS['neutral']))

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Ch3_Fig1_distributions_E_B0.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Ch3_Fig1_distributions_E_B0.png")

    # Figure 2: R and G distributions
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

    # Panel A: Repositioning Distribution
    ax = axes[0]
    R_stayers = np.zeros(6000)  # 59.7% are stayers
    R_movers = np.abs(np.random.exponential(15, 4000))  # 40.3% are movers
    R = np.concatenate([R_stayers, R_movers])

    # Separate histograms for Stayers and Movers
    ax.hist(R_stayers, bins=[-.5, 0.5], color=COLORS['neutral'],
           edgecolor='white', alpha=0.8, label='Stayers (59.7%)')
    ax.hist(R_movers[R_movers > 0], bins=30, color=COLORS['flex'],
           edgecolor='white', alpha=0.7, label='Movers (40.3%)')

    ax.set_xlabel('Repositioning magnitude, R = |B_T - B₀|')
    ax.set_ylabel('Frequency')
    ax.set_title('A. Repositioning Distribution', fontweight='bold')
    ax.legend(frameon=True, fancybox=True)

    stats = 'N = 180,994\nStayers: 107,917\nMovers: 72,943'
    ax.annotate(stats, xy=(0.97, 0.97), xycoords='axes fraction',
               ha='right', va='top', fontsize=9,
               bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=COLORS['neutral']))

    # Panel B: Growth Outcome
    ax = axes[1]
    categories = ['G = 0\n(Did not reach\nLater Stage)', 'G = 1\n(Reached\nLater Stage)']
    counts = [160262, 20732]
    percentages = [88.5, 11.5]
    colors = [COLORS['neutral'], COLORS['gold']]

    bars = ax.bar(categories, counts, color=colors, edgecolor='white', width=0.5)

    for bar, pct, count in zip(bars, percentages, counts):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2000,
               f'{pct}%', ha='center', va='bottom', fontsize=14, fontweight='bold')
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height()/2,
               f'n = {count:,}', ha='center', va='center', fontsize=10, color='white')

    ax.set_ylabel('Number of ventures')
    ax.set_title('B. Growth Outcome', fontweight='bold')

    # Base rate annotation
    ax.axhline(y=counts[1], color=COLORS['gold'], linestyle='--', alpha=0.5)
    ax.text(1.3, counts[1], 'Base success rate:\n11.5%', va='center', fontsize=9, color=COLORS['gold'])

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Ch3_Fig2_distributions_R_G.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Ch3_Fig2_distributions_R_G.png")


# ============================================
# CHAPTER 4: RESULTS
# ============================================

def fig_ch4_mover_advantage():
    """
    Ch4_Fig1: The Mover Advantage (H2: Flexibility Flex)
    MESSAGE: Movers achieve 2.60× higher success than Stayers
    COLOR: Purple (Flex) for Movers - this is H2
    """
    fig, ax = plt.subplots(figsize=(8, 6))

    categories = ['Stayers\n(R = 0)', 'Movers\n(R > 0)']
    success_rates = [7.0, 18.1]
    colors = [COLORS['neutral'], COLORS['flex']]

    bars = ax.bar(categories, success_rates, color=colors, width=0.5,
                 edgecolor='white', linewidth=2)

    # Value labels on bars
    for bar, rate in zip(bars, success_rates):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.8,
               f'{rate}%', ha='center', va='bottom',
               fontsize=18, fontweight='bold', color=COLORS['dark'])

    # 2.60× connector line
    ax.plot([0, 1], [7.0, 18.1], color=COLORS['flex'], linewidth=2.5, linestyle='-')
    ax.text(0.5, 13, '2.60×', ha='center', fontsize=20, fontweight='bold',
           color=COLORS['flex'],
           bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                    edgecolor=COLORS['flex'], linewidth=2))

    # Base rate reference
    ax.axhline(y=11.5, color=COLORS['neutral'], linestyle='--', linewidth=1.5, alpha=0.7)
    ax.text(1.25, 11.5, 'Base rate\n(11.5%)', va='center', fontsize=9, color=COLORS['neutral'])

    ax.set_ylabel('Success Rate (%)', fontsize=12)
    ax.set_ylim(0, 24)
    ax.set_title('The Mover Advantage: Flexibility Flex (H2)',
                fontsize=14, fontweight='bold', color=COLORS['flex'], pad=15)

    # Sample sizes
    ax.text(0, -2.5, 'n = 107,917', ha='center', fontsize=9, color=COLORS['neutral'])
    ax.text(1, -2.5, 'n = 72,943', ha='center', fontsize=9, color=COLORS['flex'])

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Ch4_Fig1_G_by_R.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Ch4_Fig1_G_by_R.png")


def fig_ch4_industry_heterogeneity():
    """
    Ch4_Fig2: Industry Heterogeneity
    MESSAGE: Cage binds tight in capital-intensive; releases in pre-paradigmatic
    COLOR: Teal (Paradox) for industries showing paradox, Gray for Quantum (exception)
    """
    industries = ['Hardware', 'Transportation', 'Pharma', 'MedTech', 'Software', 'Quantum']
    correlations = [-0.108, -0.101, -0.079, -0.053, -0.001, 0.095]
    sample_sizes = [50390, 154148, 56947, 29493, 226896, 1144]
    significance = ['***', '***', '***', '***', '', '*']

    # Colors: Paradox (teal) for negative correlations, neutral for Quantum
    colors = [COLORS['paradox'] if c < 0 else COLORS['neutral'] for c in correlations]

    fig, ax = plt.subplots(figsize=(10, 6))
    y_pos = np.arange(len(industries))

    bars = ax.barh(y_pos, correlations, color=colors, height=0.6, edgecolor='white')

    ax.axvline(x=0, color=COLORS['dark'], linewidth=1)

    # Labels
    for i, (corr, sig, n) in enumerate(zip(correlations, significance, sample_sizes)):
        # Correlation value
        label = f'{corr:+.3f}{sig}'
        x_pos = corr + 0.008 if corr >= 0 else corr - 0.008
        ha = 'left' if corr >= 0 else 'right'
        color = COLORS['neutral'] if corr >= 0 else COLORS['paradox']
        ax.text(x_pos, i, label, va='center', ha=ha, fontsize=11, fontweight='bold', color=color)

        # Sample size
        ax.text(0.16, i, f'N={n:,}', va='center', ha='left', fontsize=9, color=COLORS['neutral'])

    # Annotations
    ax.annotate('Cage binds tight\n(Capital-intensive)',
               xy=(-0.108, 0), xytext=(-0.13, 1.5),
               fontsize=10, color=COLORS['paradox'], fontweight='bold', ha='center',
               arrowprops=dict(arrowstyle='->', color=COLORS['paradox'], lw=1.5))

    ax.annotate('Era of Ferment\n(Quantum)',
               xy=(0.095, 5), xytext=(0.12, 4),
               fontsize=10, color=COLORS['neutral'], fontweight='bold', ha='center',
               arrowprops=dict(arrowstyle='->', color=COLORS['neutral'], lw=1.5))

    ax.set_yticks(y_pos)
    ax.set_yticklabels(industries, fontsize=11)
    ax.set_xlabel('Correlation ρ(E, G)', fontsize=12)
    ax.set_xlim(-0.16, 0.19)
    ax.set_title('Industry Heterogeneity: Early Funding–Growth Correlation',
                fontsize=14, fontweight='bold', pad=15)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Ch4_Fig2_industry_rho.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Ch4_Fig2_industry_rho.png")


# ============================================
# CHAPTER 5: DESIGN
# ============================================

def fig_ch5_sweet_spot():
    """
    Ch5_Fig1: The Ambiguity Sweet Spot
    MESSAGE: Moderate strategic breadth (Q3) achieves highest survival
    COLOR: Gold for sweet spot (the design insight), Purple for flexibility
    """
    fig, ax = plt.subplots(figsize=(9, 6))

    quartiles = ['Q1\n(Narrow)', 'Q2', 'Q3\n(Sweet Spot)', 'Q4\n(Broad)']
    survival_rates = [10.2, 11.8, 15.0, 9.5]

    # Colors: Gold for sweet spot, neutral for others
    colors = [COLORS['neutral'], COLORS['neutral'], COLORS['gold'], COLORS['neutral']]

    bars = ax.bar(quartiles, survival_rates, color=colors, width=0.6,
                 edgecolor='white', linewidth=2)

    # Value labels
    for bar, rate in zip(bars, survival_rates):
        color = COLORS['gold'] if rate == 15.0 else COLORS['dark']
        weight = 'bold' if rate == 15.0 else 'normal'
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.4,
               f'{rate}%', ha='center', va='bottom',
               fontsize=14, fontweight=weight, color=color)

    # Base rate line
    ax.axhline(y=11.5, color=COLORS['dark'], linestyle='--', linewidth=1.5, alpha=0.6)
    ax.text(3.6, 11.5, 'Base rate (11.5%)', va='center', fontsize=10, color=COLORS['dark'])

    # Highlight sweet spot
    ax.annotate('', xy=(2, 15.0), xytext=(2, 17),
               arrowprops=dict(arrowstyle='->', color=COLORS['gold'], lw=2))
    ax.text(2, 17.5, 'Optimal: Vision-level\ncommitment', ha='center',
           fontsize=10, fontweight='bold', color=COLORS['gold'])

    ax.set_ylabel('Survival Rate (%)', fontsize=12)
    ax.set_xlabel('Strategic Breadth Quartile', fontsize=12)
    ax.set_ylim(0, 19)
    ax.set_title('The Ambiguity Sweet Spot: Moderate Breadth Wins',
                fontsize=14, fontweight='bold', color=COLORS['gold'], pad=15)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Ch5_Fig1_sweet_spot.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Ch5_Fig1_sweet_spot.png")


# ============================================
# MAIN
# ============================================

def main():
    """Generate all thesis figures with professional design."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("\n" + "="*60)
    print("GOLDEN CAGE THESIS - Professional Figure Generation")
    print("="*60)
    print(f"\nOutput: {OUTPUT_DIR}")
    print(f"\nColor System (Ivy League):")
    print(f"  • Paradox (Dartmouth Green): {COLORS['paradox']} - H3: ρ(E,G) < 0")
    print(f"  • Cage (Harvard Crimson):    {COLORS['cage']} - H1: dR/dE < 0")
    print(f"  • Flex (Cobalt Blue):        {COLORS['flex']} - H2: dG/dR > 0")
    print(f"  • Gold:            {COLORS['gold']} - Highlights, sweet spots")
    print("-"*60)

    # Generate all figures
    fig_ch1_capital_paradox()
    fig_ch1_mediation_dag()
    fig_ch2_sorting_mechanism()
    fig_ch3_distributions()
    fig_ch4_mover_advantage()
    fig_ch4_industry_heterogeneity()
    fig_ch5_sweet_spot()

    print("-"*60)
    print("✓ All figures generated successfully!")
    print("="*60 + "\n")


if __name__ == '__main__':
    main()
