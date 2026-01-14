"""
Figure 9: Balanced Growth Framework (Fine 2022)
Panel A: Growth Anatomy (2×2 Matrix)
Panel B: The Diagonal Principle
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

# Grayscale color scheme (no red, gold, blue)
COLORS = {
    'dark': '#333333',       # Dark gray for text
    'medium': '#666666',     # Medium gray
    'light': '#999999',      # Light gray
    'lighter': '#CCCCCC',    # Lighter gray
    'lightest': '#E8E8E8',   # Background
    'white': '#FFFFFF',
    'black': '#000000'
}

def create_panel_a(ax):
    """Panel A: Growth Anatomy 2×2 Matrix"""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')

    # Draw quadrants - all in grayscale
    # Type A: Operational Trap (Low Market, High Ops) - top left
    rect_a = FancyBboxPatch((0.5, 5.5), 4, 4,
                             boxstyle="round,pad=0.05",
                             facecolor=COLORS['light'], alpha=0.8,
                             edgecolor='white', linewidth=2)
    ax.add_patch(rect_a)

    # Type C: Balanced Engine (High Market, High Ops) - top right (diagonal = success)
    rect_c = FancyBboxPatch((5.5, 5.5), 4, 4,
                             boxstyle="round,pad=0.05",
                             facecolor=COLORS['dark'], alpha=0.9,
                             edgecolor='white', linewidth=2)
    ax.add_patch(rect_c)

    # Dead Zone (Low Market, Low Ops) - bottom left
    rect_dead = FancyBboxPatch((0.5, 0.5), 4, 4,
                                boxstyle="round,pad=0.05",
                                facecolor=COLORS['lightest'], alpha=0.8,
                                edgecolor='white', linewidth=2)
    ax.add_patch(rect_dead)

    # Type B: Market Mirage (High Market, Low Ops) - bottom right
    rect_b = FancyBboxPatch((5.5, 0.5), 4, 4,
                             boxstyle="round,pad=0.05",
                             facecolor=COLORS['light'], alpha=0.8,
                             edgecolor='white', linewidth=2)
    ax.add_patch(rect_b)

    # Labels for quadrants
    ax.text(2.5, 8.2, 'OPERATIONAL\nTRAP', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')
    ax.text(2.5, 6.3, 'NxStage', ha='center', va='center',
            fontsize=9, color='white', style='italic')

    ax.text(7.5, 8.2, 'BALANCED\nENGINE', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')
    ax.text(7.5, 6.3, '★ Diagonal', ha='center', va='center',
            fontsize=9, color='white', style='italic')

    ax.text(2.5, 2.5, 'DEAD\nZONE', ha='center', va='center',
            fontsize=11, fontweight='bold', color=COLORS['medium'])

    ax.text(7.5, 3.2, 'MARKET\nMIRAGE', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')
    ax.text(7.5, 1.3, 'SkinnyGirl', ha='center', va='center',
            fontsize=9, color='white', style='italic')

    # Draw diagonal arrow (success path)
    ax.annotate('', xy=(8.5, 8.5), xytext=(1.5, 1.5),
                arrowprops=dict(arrowstyle='->', color=COLORS['dark'],
                               lw=2, ls='--'))

    # Axis labels
    ax.set_xlabel('Market Pull →', fontsize=12, fontweight='bold')
    ax.set_ylabel('Ops Capability →', fontsize=12, fontweight='bold')

    # Axis ticks
    ax.set_xticks([2.5, 7.5])
    ax.set_xticklabels(['Low', 'High'], fontsize=10)
    ax.set_yticks([2.5, 7.5])
    ax.set_yticklabels(['Low', 'High'], fontsize=10)

    # Title and equation
    ax.set_title('Panel A: Growth Anatomy\nG = Market × Ops',
                 fontsize=13, fontweight='bold', pad=10)

    # Remove spines
    for spine in ax.spines.values():
        spine.set_visible(False)


def create_panel_b(ax):
    """Panel B: The Diagonal Principle - simplified"""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Simple diagonal visualization
    # Draw coordinate system
    ax.arrow(1, 1, 0, 7, head_width=0.2, head_length=0.2, fc=COLORS['dark'], ec=COLORS['dark'])
    ax.arrow(1, 1, 7, 0, head_width=0.2, head_length=0.2, fc=COLORS['dark'], ec=COLORS['dark'])

    ax.text(0.5, 8.5, 'Ops\nCapability', ha='center', va='center', fontsize=10, fontweight='bold')
    ax.text(8.5, 0.5, 'Market\nPull', ha='center', va='center', fontsize=10, fontweight='bold')

    # Draw diagonal (success path)
    ax.plot([1.5, 7.5], [1.5, 7.5], color=COLORS['dark'], lw=3, ls='-')
    ax.text(7.8, 7.8, 'Diagonal\n(Success)', ha='left', va='center', fontsize=9, fontweight='bold')

    # Off-diagonal examples
    # NxStage: High Ops, Low Market (above diagonal)
    ax.scatter([3], [6], s=200, c=COLORS['medium'], marker='o', zorder=5)
    ax.text(3, 6.8, 'NxStage', ha='center', va='bottom', fontsize=9, style='italic')
    ax.annotate('', xy=(4.5, 4.5), xytext=(3, 6),
                arrowprops=dict(arrowstyle='->', color=COLORS['light'], lw=1.5))
    ax.text(2.2, 5.2, '↓ Need\nMarket', ha='center', va='center', fontsize=8, color=COLORS['medium'])

    # SkinnyGirl: High Market, Low Ops (below diagonal)
    ax.scatter([6], [3], s=200, c=COLORS['medium'], marker='s', zorder=5)
    ax.text(6, 2.2, 'SkinnyGirl', ha='center', va='top', fontsize=9, style='italic')
    ax.annotate('', xy=(4.5, 4.5), xytext=(6, 3),
                arrowprops=dict(arrowstyle='->', color=COLORS['light'], lw=1.5))
    ax.text(6.8, 4.2, '↑ Need\nOps', ha='center', va='center', fontsize=8, color=COLORS['medium'])

    # Motional (on diagonal, staged)
    ax.scatter([4.5], [4.5], s=250, c=COLORS['dark'], marker='D', zorder=5)
    ax.text(4.5, 3.7, 'Motional\n(staged)', ha='center', va='top', fontsize=9, fontweight='bold')

    # Title
    ax.set_title("Panel B: The Diagonal Principle\nStay on the diagonal through staged commitment",
                 fontsize=13, fontweight='bold', pad=10)

    # Key message
    ax.text(5, 0.8, 'Diagnose bottleneck → Stage commitment to address it',
            ha='center', va='center', fontsize=10, style='italic', color=COLORS['dark'])


def main():
    # Create figure with two panels
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

    # Set background
    fig.patch.set_facecolor('white')

    # Create panels
    create_panel_a(ax1)
    create_panel_b(ax2)

    # Main title
    fig.suptitle('Figure 9: Balanced Growth Framework (Fine 2022)',
                 fontsize=14, fontweight='bold', y=0.98)

    plt.tight_layout(rect=[0, 0, 1, 0.95])

    # Save figure
    output_path = '/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/papers_v7_sail/figures/Fig9_balanced_growth.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"Figure saved to: {output_path}")

    plt.close()


if __name__ == "__main__":
    main()
