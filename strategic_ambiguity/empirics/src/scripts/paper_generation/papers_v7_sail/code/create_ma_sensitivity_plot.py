#!/usr/bin/env python3
"""
Create M&A Sensitivity Analysis Visualization

Compares how the three core thesis relationships change under different
M&A coding assumptions: Failure (G=0), Success (G=1), Censored (excluded).
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Paths
SCRIPT_DIR = Path(__file__).parent
DATA_PATH = SCRIPT_DIR / 'data' / 'processed' / 'ma_sensitivity_results.json'
OUTPUT_PATH = SCRIPT_DIR.parent / 'img_overleaf' / 'AppC_Fig3_ma_sensitivity.png'

# Thesis color scheme (from latex(thesis)_color_definitions.tex)
COLORS = {
    'cage': '#DC3545',     # Red - Commitment Cage (H1), rho(E,R)
    'flex': '#007BFF',     # Blue - Flexibility Flex (H2), rho(R,G)
    'paradox': '#28A745',  # Green - Funding-Growth Paradox (H3), rho(E,G)
    'black': '#1E1E1E',    # Near black
    'gray': '#6C757D',     # Gray for scenarios/bounds
}

def load_results():
    """Load M&A sensitivity results."""
    with open(DATA_PATH, 'r') as f:
        return json.load(f)

def create_visualization(results):
    """Create bar chart comparing M&A coding approaches."""

    # Scenarios to plot (exclude baseline since it equals M&A=Failure)
    scenarios = ['M&A = Failure (G=0)', 'M&A = Success (G=1)', 'M&A = Censored (excluded)']
    scenario_labels = ['M&A = Failure\n(G=0)', 'M&A = Success\n(G=1)', 'M&A = Censored\n(excluded)']

    # Metrics to compare
    metrics = ['rho_ER', 'rho_RG', 'rho_EG']
    metric_labels = ['ρ(E,R)\nCommitment Cage', 'ρ(R,G)\nFlexibility Flex', 'ρ(E,G)\nFunding-Growth Paradox']

    # Extract values
    values = {}
    for scenario in scenarios:
        values[scenario] = [results[scenario][m] for m in metrics]

    # Create figure
    fig, axes = plt.subplots(1, 3, figsize=(14, 5))
    fig.suptitle('M&A Sensitivity Analysis: Robustness of Core Relationships',
                 fontsize=14, fontweight='bold', y=1.02)

    x = np.arange(len(scenarios))
    width = 0.6

    # Plot each metric
    for idx, (metric, label) in enumerate(zip(metrics, metric_labels)):
        ax = axes[idx]

        vals = [results[s][metric] for s in scenarios]

        # Color bars based on sign (hypothesis direction) using thesis color scheme
        if metric == 'rho_ER':
            # H1: Should be negative (cage effect) - Red
            bar_colors = [COLORS['cage'] if v < 0 else COLORS['gray'] for v in vals]
            hypothesis_line = 0
            robust = all(v < 0 for v in vals)
        elif metric == 'rho_RG':
            # H2: Should be positive (flexibility helps) - Blue
            bar_colors = [COLORS['flex'] if v > 0 else COLORS['gray'] for v in vals]
            hypothesis_line = 0
            robust = all(v > 0 for v in vals)
        else:  # rho_EG
            # H3: Should be negative (paradox) - Green
            bar_colors = [COLORS['paradox'] if v < 0 else COLORS['gray'] for v in vals]
            hypothesis_line = 0
            robust = all(v < 0 for v in vals)

        bars = ax.bar(x, vals, width, color=bar_colors, edgecolor=COLORS['black'], linewidth=1.5)

        # Add value labels on bars
        for bar, val in zip(bars, vals):
            height = bar.get_height()
            va = 'bottom' if height >= 0 else 'top'
            offset = 0.01 if height >= 0 else -0.01
            ax.annotate(f'{val:+.3f}',
                       xy=(bar.get_x() + bar.get_width() / 2, height),
                       xytext=(0, 3 if height >= 0 else -3),
                       textcoords="offset points",
                       ha='center', va=va, fontsize=10, fontweight='bold')

        # Reference line at zero
        ax.axhline(y=0, color=COLORS['black'], linestyle='-', linewidth=1)

        # Styling
        ax.set_ylabel('Spearman ρ', fontsize=11)
        ax.set_xticks(x)
        ax.set_xticklabels(scenario_labels, fontsize=9)
        ax.set_title(label, fontsize=11, fontweight='bold')

        # Add robustness indicator
        status = 'ROBUST' if robust else 'NOT ROBUST'
        status_color = COLORS['black'] if robust else COLORS['cage']
        ax.text(0.5, 0.95, status, transform=ax.transAxes,
                ha='center', va='top', fontsize=10, fontweight='bold',
                color=status_color,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=status_color, alpha=0.8))

        # Set y-axis limits to show all values clearly
        ymin, ymax = ax.get_ylim()
        padding = max(abs(ymin), abs(ymax)) * 0.3
        ax.set_ylim(min(ymin, -0.05) - padding * 0.5, max(ymax, 0.05) + padding)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

    plt.tight_layout()

    # Add footnote
    fig.text(0.5, -0.02,
             'Note: Baseline (current) equals M&A=Failure since M&A companies have G=0 in raw data.\n'
             'Robustness requires sign consistency across all M&A coding approaches.',
             ha='center', fontsize=9, style='italic', color=COLORS['gray'])

    return fig

def create_mover_advantage_plot(results):
    """Create separate plot for Mover Advantage comparison."""

    scenarios = ['M&A = Failure (G=0)', 'M&A = Success (G=1)', 'M&A = Censored (excluded)']
    scenario_labels = ['M&A = Failure\n(G=0)', 'M&A = Success\n(G=1)', 'M&A = Censored\n(excluded)']

    fig, ax = plt.subplots(figsize=(8, 5))

    x = np.arange(len(scenarios))
    width = 0.6

    vals = [results[s]['mover_advantage'] for s in scenarios]

    # Color: blue (flex) if > 1 (Movers outperform), gray otherwise
    bar_colors = [COLORS['flex'] if v > 1 else COLORS['gray'] for v in vals]

    bars = ax.bar(x, vals, width, color=bar_colors, edgecolor=COLORS['black'], linewidth=1.5)

    # Add value labels
    for bar, val in zip(bars, vals):
        height = bar.get_height()
        ax.annotate(f'{val:.2f}×',
                   xy=(bar.get_x() + bar.get_width() / 2, height),
                   xytext=(0, 3),
                   textcoords="offset points",
                   ha='center', va='bottom', fontsize=12, fontweight='bold')

    # Reference line at 1.0 (no advantage)
    ax.axhline(y=1.0, color=COLORS['cage'], linestyle='--', linewidth=2, label='No Advantage')

    # Styling
    ax.set_ylabel('Mover Advantage (Success Rate Ratio)', fontsize=11)
    ax.set_xticks(x)
    ax.set_xticklabels(scenario_labels, fontsize=10)
    ax.set_title('Mover Advantage Across M&A Coding Approaches', fontsize=12, fontweight='bold')

    # Robustness check
    robust = all(v > 1 for v in vals)
    status = 'ROBUST: Movers outperform in all scenarios' if robust else 'NOT ROBUST'
    ax.text(0.5, 0.95, status, transform=ax.transAxes,
            ha='center', va='top', fontsize=11, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=COLORS['black'], alpha=0.8))

    ax.set_ylim(0, max(vals) * 1.2)
    ax.legend(loc='lower right')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()

    return fig

def main():
    print("=" * 60)
    print("M&A SENSITIVITY ANALYSIS VISUALIZATION")
    print("=" * 60)

    # Load results
    results = load_results()
    print(f"\nLoaded results from: {DATA_PATH}")

    # Create main visualization
    fig1 = create_visualization(results)
    fig1.savefig(OUTPUT_PATH, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"\n✅ Saved correlation comparison to: {OUTPUT_PATH}")

    # Create Mover Advantage plot
    ma_output = OUTPUT_PATH.parent / 'AppC_Fig4_mover_advantage_sensitivity.png'
    fig2 = create_mover_advantage_plot(results)
    fig2.savefig(ma_output, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"✅ Saved Mover Advantage plot to: {ma_output}")

    # Print summary table
    print("\n" + "=" * 80)
    print("SUMMARY: M&A SENSITIVITY ANALYSIS")
    print("=" * 80)
    print(f"\n{'Scenario':<25} {'N':>10} {'G rate':>10} {'ρ(E,R)':>10} {'ρ(R,G)':>10} {'ρ(E,G)':>10} {'MA':>8}")
    print("-" * 80)

    for scenario, data in results.items():
        print(f"{scenario:<25} {data['n']:>10,} {data['g_rate']:>9.1f}% {data['rho_ER']:>+10.4f} "
              f"{data['rho_RG']:>+10.4f} {data['rho_EG']:>+10.4f} {data['mover_advantage']:>7.2f}×")

    print("\n" + "=" * 80)
    print("ROBUSTNESS ASSESSMENT")
    print("=" * 80)

    # Check robustness
    scenarios = ['M&A = Failure (G=0)', 'M&A = Success (G=1)', 'M&A = Censored (excluded)']

    rho_ER_robust = all(results[s]['rho_ER'] < 0 for s in scenarios)
    rho_RG_robust = all(results[s]['rho_RG'] > 0 for s in scenarios)
    rho_EG_robust = all(results[s]['rho_EG'] < 0 for s in scenarios)
    ma_robust = all(results[s]['mover_advantage'] > 1 for s in scenarios)

    print(f"\n  ρ(E,R) < 0 (Commitment Cage):      {'✅ ROBUST' if rho_ER_robust else '❌ NOT ROBUST'}")
    print(f"  ρ(R,G) > 0 (Flexibility Flex):     {'✅ ROBUST' if rho_RG_robust else '❌ NOT ROBUST'}")
    print(f"  ρ(E,G) < 0 (Funding-Growth Paradox): {'✅ ROBUST' if rho_EG_robust else '❌ NOT ROBUST'}")
    print(f"  Mover Advantage > 1:               {'✅ ROBUST' if ma_robust else '❌ NOT ROBUST'}")

    print("\n" + "=" * 80)
    print("IMPLICATIONS FOR THESIS")
    print("=" * 80)

    if not rho_EG_robust:
        print("""
⚠️  CRITICAL FINDING: The Funding-Growth Paradox (ρ(E,G) < 0) is NOT robust.

When M&A is coded as success (G=1), the correlation FLIPS to POSITIVE (+0.146).
This means the "paradox" depends entirely on how M&A outcomes are interpreted.

RECOMMENDED ACTION:
1. Acknowledge this sensitivity in Chapter 6 (Limitations)
2. Present the baseline result (M&A = Failure) as the primary analysis
3. Note that coding M&A as success reverses the finding
4. Argue for the M&A = Failure coding based on:
   - M&A often represents founder exit, not growth success
   - Most M&A are acqui-hires or asset sales, not billion-dollar exits
   - The thesis studies GROWTH via Later Stage VC, not any exit
""")

    print("\n✅ Visualization complete.")

if __name__ == '__main__':
    main()
