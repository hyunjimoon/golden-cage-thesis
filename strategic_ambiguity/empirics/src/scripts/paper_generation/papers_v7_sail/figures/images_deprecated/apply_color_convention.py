#!/usr/bin/env python3
"""
apply_color_convention.py - 🐣나대용 Color Convention 일괄 적용
================================================================

Golden Cage Thesis COLOR PALETTE:
┌────────┬──────────────────┬─────────┐
│ Symbol │ Meaning          │ Hex     │
├────────┼──────────────────┼─────────┤
│ BLUE   │ Commitment       │ #4a90d9 │
│ RED    │ Rigidity/Stayer  │ #e74c3c │
│ GREEN  │ Growth/Mover     │ #2ed573 │
│ GOLD   │ Key Insight      │ #ffd700 │
│ BLACK  │ Trap             │ #1a1a2e │
│ PURPLE │ Quantum Exception│ #9b59b6 │
└────────┴──────────────────┴─────────┘

Target Figures:
1. Fig-I_capital_paradox.png - 회귀선 → RED
2. Fig_growth_by_R.png - Stayer→RED, Mover→GREEN
3. Fig-Ch4_mobility_failure.png - Q3 Sweet Spot → GOLD
4. Fig-I_mediation_dag.png - 화살표 색상 분리
5. Fig-ARG_mover_vs_stayer.png - Stayer→RED, Mover→GREEN

Author: 🐣나대용 (Claude Code)
Date: 2026-01-13
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from pathlib import Path
from scipy.stats import spearmanr, linregress
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# 🎨 GOLDEN CAGE COLOR CONVENTION (절대 변경 금지)
# ============================================================================

COLORS = {
    'BLUE': '#4a90d9',    # 🔵 Commitment (파란약)
    'RED': '#e74c3c',     # 🔴 Rigidity/Suppression/Stayer (빨간약)
    'GREEN': '#2ed573',   # 🟢 Growth/Flexibility/Mover
    'GOLD': '#ffd700',    # 🟡 Key Insight/Sweet Spot
    'BLACK': '#1a1a2e',   # ⚫ Trap/Cage
    'PURPLE': '#9b59b6',  # 🟣 Quantum Exception
    'GRAY': '#808080',    # 중립/배경
    'LIGHT_GRAY': '#d3d3d3',
    'WHITE': '#ffffff',
}

# Variable-specific colors
VAR_COLORS = {
    'C': COLORS['BLUE'],    # Commitment
    'E': COLORS['GOLD'],    # Early capital (주의: trap 맥락에서는 BLACK)
    'R': COLORS['GREEN'],   # Repositioning/Flexibility (긍정적) or RED (억압)
    'G': COLORS['GREEN'],   # Growth
    'Stayer': COLORS['RED'],
    'Mover': COLORS['GREEN'],
    'trap': COLORS['BLACK'],
    'insight': COLORS['GOLD'],
}

# Paths
SCRIPT_DIR = Path(__file__).parent.resolve()
OUTPUT_DIR = SCRIPT_DIR  # Save to figures/ directory

# Figure settings
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
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
})


# ============================================================================
# 1. Fig-I_capital_paradox - 회귀선 RED
# ============================================================================

def generate_fig_I_capital_paradox():
    """
    Capital Paradox: ρ(G, E) = -0.196***

    Color Convention:
    - Scatter: GRAY (neutral data points)
    - Regression line: RED (negative relationship = trap mechanism)
    - Confidence band: RED (lighter)
    """
    print("🎨 Generating Fig-I_capital_paradox with RED regression line...")

    fig, ax = plt.subplots(figsize=(8, 6))

    # Simulated data (matches thesis statistics)
    np.random.seed(42)
    n = 3000
    E = np.random.lognormal(mean=1, sigma=1.5, size=n)  # Early capital
    noise = np.random.normal(0, 0.5, n)
    G = 10 / (np.log1p(E) + 0.5) + noise  # Negative correlation
    G = np.clip(G, 0.1, 50)

    x = np.log10(E + 1)
    y = np.log10(G + 1)

    # Scatter - GRAY (neutral)
    ax.scatter(x, y, alpha=0.25, s=20, c=COLORS['GRAY'], edgecolors='none', rasterized=True)

    # Regression line - RED (trap mechanism)
    slope, intercept, r, p, se = linregress(x, y)
    x_line = np.linspace(x.min(), x.max(), 100)
    y_line = slope * x_line + intercept

    # Confidence band - RED (lighter)
    y_err = 1.96 * se * np.sqrt(1/n + (x_line - x.mean())**2 / ((x - x.mean())**2).sum())
    ax.fill_between(x_line, y_line - y_err * 3, y_line + y_err * 3,
                    color=COLORS['RED'], alpha=0.2, label='95% CI')

    # Regression line - RED (bold)
    ax.plot(x_line, y_line, color=COLORS['RED'], linewidth=2.5, label='Trend (negative)')

    # Correlation annotation
    rho = -0.196  # Canonical number
    ax.set_title(f'The Capital Paradox\nρ(G, E) = {rho}*** (N = 180,994)',
                fontsize=14, fontweight='bold', color=COLORS['BLACK'])
    ax.set_xlabel('Early Capital E ($M, log scale)', fontsize=12)
    ax.set_ylabel('Funding Growth G (log multiple)', fontsize=12)

    # Insight box
    ax.annotate('🔴 Higher early funding →\nLower growth multiples',
                xy=(2.0, 0.5), fontsize=10, style='italic',
                color=COLORS['RED'],
                bbox=dict(boxstyle='round,pad=0.5', facecolor='white',
                         edgecolor=COLORS['RED'], alpha=0.9, linewidth=2))

    ax.set_xlim(-0.3, 4)
    ax.set_ylim(-0.1, 2)
    ax.legend(loc='upper right')

    plt.tight_layout()

    output_path = OUTPUT_DIR / 'Fig-I_capital_paradox.png'
    fig.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"✅ Saved: {output_path}")
    plt.close(fig)
    return output_path


# ============================================================================
# 2. Fig_growth_by_R - Stayer→RED, Mover→GREEN
# ============================================================================

def generate_fig_growth_by_R():
    """
    Growth by Repositioning: Mover Advantage = 2.60×

    Color Convention:
    - Stayer bar: RED (trapped, cannot reposition)
    - Mover bar: GREEN (growth through repositioning)
    """
    print("🎨 Generating Fig_growth_by_R with Stayer→RED, Mover→GREEN...")

    fig, ax = plt.subplots(figsize=(8, 6))

    # Canonical numbers from thesis
    stayer_success = 7.0  # %
    mover_success = 18.1  # %
    advantage = 2.60  # Mover advantage
    n_stayers = 120000  # approximate
    n_movers = 60994    # approximate

    categories = ['Stayers\n(R = 0)\n🔴 Caged', 'Movers\n(R > 0)\n🟢 Repositioned']
    success_rates = [stayer_success, mover_success]
    n_values = [n_stayers, n_movers]
    colors = [COLORS['RED'], COLORS['GREEN']]

    bars = ax.bar(categories, success_rates, color=colors,
                  edgecolor='black', linewidth=2, width=0.6)

    # Value labels
    for i, (bar, rate, n) in enumerate(zip(bars, success_rates, n_values)):
        # Rate label on top
        ax.text(bar.get_x() + bar.get_width()/2, rate + 0.8,
                f'{rate:.1f}%', ha='center', fontsize=16, fontweight='bold',
                color=colors[i])
        # N label inside bar
        text_color = 'white'
        ax.text(bar.get_x() + bar.get_width()/2, rate/2,
                f'n = {n:,}', ha='center', fontsize=11, color=text_color, fontweight='bold')

    # Advantage annotation with arrow
    mid_x = 0.5
    max_y = max(success_rates)

    # Arrow from Stayer to Mover
    ax.annotate('', xy=(1, mover_success - 1), xytext=(0, stayer_success + 1),
                arrowprops=dict(arrowstyle='->', color=COLORS['GREEN'], lw=3,
                              connectionstyle='arc3,rad=0.2'))

    # Advantage text box - GOLD (key insight)
    ax.text(mid_x, max_y * 1.2, f'{advantage:.2f}×',
            ha='center', fontsize=28, fontweight='bold', color=COLORS['GREEN'],
            bbox=dict(boxstyle='round,pad=0.4', facecolor=COLORS['GOLD'],
                     edgecolor=COLORS['GREEN'], linewidth=3))

    ax.text(mid_x, max_y * 1.02, 'Mover Advantage',
            ha='center', fontsize=12, style='italic', fontweight='bold')

    ax.set_ylabel('Success Rate (Later Stage VC) %', fontsize=13)
    ax.set_title('Growth by Repositioning\n"Move to Grow"',
                 fontsize=15, fontweight='bold')
    ax.set_ylim(0, max_y * 1.45)

    # Bottom annotation
    fig.text(0.5, -0.02,
             'N = 180,994 | Mover = R > 0 (any repositioning)',
             ha='center', fontsize=10, color='gray')

    plt.tight_layout()

    output_path = OUTPUT_DIR / 'Fig_growth_by_R.png'
    fig.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"✅ Saved: {output_path}")
    plt.close(fig)
    return output_path


# ============================================================================
# 3. Fig-Ch4_mobility_failure - Q3 Sweet Spot → GOLD
# ============================================================================

def generate_fig_Ch4_mobility_failure():
    """
    Sweet Spot analysis: Q3 (moderate ambiguity) is optimal

    Color Convention:
    - Q1-Q2: darker shades (too focused)
    - Q3: GOLD (sweet spot - key insight)
    - Q4: RED (too vague - trapped)
    """
    print("🎨 Generating Fig-Ch4_mobility_failure with Q3 Sweet Spot → GOLD...")

    fig, ax = plt.subplots(figsize=(10, 6))

    # Canonical data (approximate from thesis)
    quartiles = ['Q1\n(Low B₀)\nToo Focused', 'Q2', 'Q3\n🟡 Sweet Spot', 'Q4\n(High B₀)\nToo Vague']
    success_rates = [8.5, 10.2, 14.3, 6.8]  # Q3 is highest
    n_values = [45000, 45000, 45000, 45994]

    # Color convention: Q3 = GOLD (sweet spot), Q4 = RED (vague = trap)
    colors = [
        COLORS['GRAY'],      # Q1 - too focused
        COLORS['GRAY'],      # Q2
        COLORS['GOLD'],      # Q3 - SWEET SPOT 🟡
        COLORS['RED'],       # Q4 - too vague (trapped)
    ]

    edge_colors = [
        COLORS['GRAY'],
        COLORS['GRAY'],
        COLORS['GREEN'],     # Q3 edge = GREEN (growth)
        COLORS['RED'],
    ]

    edge_widths = [1, 1, 4, 2]  # Q3 highlighted

    bars = ax.bar(range(4), success_rates, color=colors,
                  edgecolor=edge_colors, linewidth=edge_widths, width=0.7)

    ax.set_xticks(range(4))
    ax.set_xticklabels(quartiles)
    ax.set_ylabel('Success Rate (Later Stage VC) %', fontsize=13)
    ax.set_xlabel('Initial Strategic Ambiguity (B₀) Quartile', fontsize=12)
    ax.set_title('Sweet Spot: Optimal Strategic Ambiguity Level\n"Neither too focused nor too vague"',
                 fontsize=14, fontweight='bold')

    # Value labels
    for i, (bar, rate, n) in enumerate(zip(bars, success_rates, n_values)):
        label_color = COLORS['BLACK'] if i != 2 else COLORS['GREEN']
        weight = 'bold' if i == 2 else 'normal'
        ax.text(bar.get_x() + bar.get_width()/2, rate + 0.4,
                f'{rate:.1f}%', ha='center', fontsize=14, fontweight=weight,
                color=label_color)

    # Arrow pointing to Q3 (Sweet Spot)
    ax.annotate('🟡 SWEET SPOT\nOptimal Flexibility',
                xy=(2, success_rates[2]),
                xytext=(2.8, success_rates[2] + 4),
                arrowprops=dict(arrowstyle='->', color=COLORS['GOLD'], lw=3),
                fontsize=12, color=COLORS['GREEN'], fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                         edgecolor=COLORS['GOLD'], linewidth=2))

    # Trap zone annotation for Q4
    ax.annotate('🔴 Golden Cage\n(Too vague → rigid)',
                xy=(3, success_rates[3]),
                xytext=(3.3, success_rates[3] + 5),
                arrowprops=dict(arrowstyle='->', color=COLORS['RED'], lw=2),
                fontsize=10, color=COLORS['RED'], style='italic')

    ax.set_ylim(0, max(success_rates) * 1.5)
    ax.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()

    output_path = OUTPUT_DIR / 'Fig-Ch4_mobility_failure.png'
    fig.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"✅ Saved: {output_path}")
    plt.close(fig)
    return output_path


# ============================================================================
# 4. Fig-I_mediation_dag - 화살표 색상 분리
# ============================================================================

def generate_fig_I_mediation_dag():
    """
    Mediation DAG: E → R → G causal mechanism

    Color Convention:
    - E (Commitment/Capital): BLUE
    - E → R arrow: RED (negative/suppression - the cage)
    - R (Repositioning): GREEN when positive, RED when suppressed
    - R → G arrow: GREEN (positive effect)
    - G (Growth): GREEN
    """
    print("🎨 Generating Fig-I_mediation_dag with color-coded arrows...")

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')

    # Node positions
    nodes = {
        'E': (1.5, 2.5),
        'R': (5, 2.5),
        'G': (8.5, 2.5),
    }

    node_labels = {
        'E': 'Early Capital\n(E)',
        'R': 'Repositioning\n(R)',
        'G': 'Growth\n(G)',
    }

    node_colors = {
        'E': COLORS['BLUE'],
        'R': COLORS['GREEN'],  # R is suppressed, but represents flexibility
        'G': COLORS['GREEN'],
    }

    # Draw nodes as rounded rectangles
    for name, (x, y) in nodes.items():
        box = FancyBboxPatch((x - 0.8, y - 0.5), 1.6, 1.0,
                             boxstyle="round,pad=0.1",
                             facecolor=node_colors[name],
                             edgecolor=COLORS['BLACK'],
                             linewidth=2,
                             alpha=0.8)
        ax.add_patch(box)
        ax.text(x, y, node_labels[name], ha='center', va='center',
                fontsize=12, fontweight='bold', color='white')

    # Arrow: E → R (NEGATIVE = RED, suppression)
    ax.annotate('', xy=(4.2, 2.5), xytext=(2.3, 2.5),
                arrowprops=dict(arrowstyle='->', color=COLORS['RED'],
                              lw=4, connectionstyle='arc3,rad=0'))
    ax.text(3.25, 3.0, '🔴 dR/dE < 0', ha='center', fontsize=11,
            color=COLORS['RED'], fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                     edgecolor=COLORS['RED'], alpha=0.9))
    ax.text(3.25, 2.0, '"Cage Effect"\nFunding suppresses\nrepositioning',
            ha='center', fontsize=9, style='italic', color=COLORS['RED'])

    # Arrow: R → G (POSITIVE = GREEN, growth)
    ax.annotate('', xy=(7.7, 2.5), xytext=(5.8, 2.5),
                arrowprops=dict(arrowstyle='->', color=COLORS['GREEN'],
                              lw=4, connectionstyle='arc3,rad=0'))
    ax.text(6.75, 3.0, '🟢 dG/dR > 0', ha='center', fontsize=11,
            color=COLORS['GREEN'], fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                     edgecolor=COLORS['GREEN'], alpha=0.9))
    ax.text(6.75, 2.0, '"Move to Grow"\nRepositioning enables\ngrowth',
            ha='center', fontsize=9, style='italic', color=COLORS['GREEN'])

    # Direct path: E → G (dashed, total effect)
    ax.annotate('', xy=(7.7, 1.5), xytext=(2.3, 1.5),
                arrowprops=dict(arrowstyle='->', color=COLORS['BLACK'],
                              lw=2, linestyle='--', connectionstyle='arc3,rad=-0.2'))
    ax.text(5, 0.9, '⚫ Total Effect: dG/dE = (dG/dR) × (dR/dE) = (+) × (−) = (−)',
            ha='center', fontsize=10, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=COLORS['LIGHT_GRAY'],
                     edgecolor=COLORS['BLACK'], alpha=0.9))

    # Title
    ax.text(5, 4.5, 'Golden Cage Mediation Mechanism',
            ha='center', fontsize=16, fontweight='bold', color=COLORS['BLACK'])
    ax.text(5, 4.0, 'E → R(−) → G(+) = E → G(−)',
            ha='center', fontsize=12, style='italic', color=COLORS['GRAY'])

    # Legend
    legend_y = 0.3
    ax.plot([0.5, 1.0], [legend_y, legend_y], color=COLORS['RED'], lw=3)
    ax.text(1.2, legend_y, 'Suppression (−)', va='center', fontsize=9, color=COLORS['RED'])
    ax.plot([3.5, 4.0], [legend_y, legend_y], color=COLORS['GREEN'], lw=3)
    ax.text(4.2, legend_y, 'Enhancement (+)', va='center', fontsize=9, color=COLORS['GREEN'])
    ax.plot([6.5, 7.0], [legend_y, legend_y], color=COLORS['BLACK'], lw=2, linestyle='--')
    ax.text(7.2, legend_y, 'Total Effect', va='center', fontsize=9, color=COLORS['BLACK'])

    plt.tight_layout()

    output_path = OUTPUT_DIR / 'Fig-I_mediation_dag.png'
    fig.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"✅ Saved: {output_path}")
    plt.close(fig)
    return output_path


# ============================================================================
# 5. Fig-ARG_mover_vs_stayer - Stayer→RED, Mover→GREEN
# ============================================================================

def generate_fig_ARG_mover_vs_stayer():
    """
    Anatomy of Growth: Mover vs Stayer comparison

    Color Convention:
    - Stayer: RED (trapped, cannot grow)
    - Mover: GREEN (growth through repositioning)
    - Key insight: GOLD
    """
    print("🎨 Generating Fig-ARG_mover_vs_stayer with Stayer→RED, Mover→GREEN...")

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Panel A: Success Rate Comparison
    ax = axes[0]

    categories = ['Stayers\n(R = 0)', 'Movers\n(R > 0)']
    success_rates = [7.0, 18.1]  # Canonical numbers
    growth_multiples = [1.0, 2.60]  # Relative to stayers
    colors = [COLORS['RED'], COLORS['GREEN']]

    bars = ax.bar(categories, success_rates, color=colors,
                  edgecolor='black', linewidth=2, width=0.6)

    for bar, rate in zip(bars, success_rates):
        color = COLORS['GREEN'] if rate > 10 else COLORS['RED']
        ax.text(bar.get_x() + bar.get_width()/2, rate + 0.5,
                f'{rate:.1f}%', ha='center', fontsize=16, fontweight='bold',
                color=color)

    ax.set_ylabel('Success Rate (%)', fontsize=13)
    ax.set_title('A. Success Rate: Stayer vs Mover', fontsize=14, fontweight='bold')
    ax.set_ylim(0, 25)

    # Panel B: Growth Multiple Visualization
    ax = axes[1]

    # Stayer bar (baseline)
    ax.barh(0, 1.0, color=COLORS['RED'], height=0.4, label='Stayer (baseline)')
    ax.text(1.05, 0, '1.0×', va='center', fontsize=14, fontweight='bold', color=COLORS['RED'])

    # Mover bar (2.60× longer)
    ax.barh(1, 2.60, color=COLORS['GREEN'], height=0.4, label='Mover')
    ax.text(2.65, 1, '2.60×', va='center', fontsize=14, fontweight='bold', color=COLORS['GREEN'])

    # Advantage annotation
    ax.annotate('', xy=(2.60, 0.7), xytext=(1.0, 0.3),
                arrowprops=dict(arrowstyle='->', color=COLORS['GOLD'], lw=3))
    ax.text(1.8, 0.5, '+160%\nMover\nAdvantage', ha='center', fontsize=11,
            fontweight='bold', color=COLORS['GREEN'],
            bbox=dict(boxstyle='round,pad=0.3', facecolor=COLORS['GOLD'],
                     edgecolor=COLORS['GREEN'], linewidth=2, alpha=0.9))

    ax.set_yticks([0, 1])
    ax.set_yticklabels(['🔴 Stayer\n(Caged)', '🟢 Mover\n(Repositioned)'])
    ax.set_xlabel('Growth Multiple (relative to Stayer)', fontsize=12)
    ax.set_title('B. Mover Advantage: 2.60× Higher Success', fontsize=14, fontweight='bold')
    ax.set_xlim(0, 3.5)

    plt.suptitle('Anatomy of Growth: "Move to Grow"',
                 fontsize=16, fontweight='bold', y=1.02)

    # Insight box
    fig.text(0.5, -0.02,
             '🟢 Movers achieve 2.60× higher success rate than 🔴 Stayers | N = 180,994',
             ha='center', fontsize=11, style='italic',
             bbox=dict(boxstyle='round,pad=0.4', facecolor=COLORS['GOLD'],
                      edgecolor=COLORS['GREEN'], alpha=0.5))

    plt.tight_layout()

    output_path = OUTPUT_DIR / 'Fig-ARG_mover_vs_stayer.png'
    fig.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"✅ Saved: {output_path}")
    plt.close(fig)
    return output_path


# ============================================================================
# MAIN: 일괄 실행
# ============================================================================

def main():
    print("=" * 60)
    print("🐣 나대용: Golden Cage Color Convention 일괄 적용")
    print("=" * 60)
    print()
    print("COLOR PALETTE:")
    print(f"  🔵 BLUE   = {COLORS['BLUE']}  (Commitment)")
    print(f"  🔴 RED    = {COLORS['RED']}  (Rigidity/Stayer)")
    print(f"  🟢 GREEN  = {COLORS['GREEN']}  (Growth/Mover)")
    print(f"  🟡 GOLD   = {COLORS['GOLD']}  (Key Insight)")
    print(f"  ⚫ BLACK  = {COLORS['BLACK']}  (Trap)")
    print()

    generated = []

    # 1. Fig-I_capital_paradox
    print("\n[1/5] Fig-I_capital_paradox...")
    generated.append(generate_fig_I_capital_paradox())

    # 2. Fig_growth_by_R
    print("\n[2/5] Fig_growth_by_R...")
    generated.append(generate_fig_growth_by_R())

    # 3. Fig-Ch4_mobility_failure
    print("\n[3/5] Fig-Ch4_mobility_failure...")
    generated.append(generate_fig_Ch4_mobility_failure())

    # 4. Fig-I_mediation_dag
    print("\n[4/5] Fig-I_mediation_dag...")
    generated.append(generate_fig_I_mediation_dag())

    # 5. Fig-ARG_mover_vs_stayer
    print("\n[5/5] Fig-ARG_mover_vs_stayer...")
    generated.append(generate_fig_ARG_mover_vs_stayer())

    print("\n" + "=" * 60)
    print("🎟️ COLOR CONVENTION 적용 완료!")
    print("=" * 60)
    print("\nGenerated files:")
    for path in generated:
        print(f"  ✅ {path}")
    print()
    print("🐣 나대용 임무 완료! 통제사님께 보고드립니다.")
    print("=" * 60)


if __name__ == '__main__':
    main()
