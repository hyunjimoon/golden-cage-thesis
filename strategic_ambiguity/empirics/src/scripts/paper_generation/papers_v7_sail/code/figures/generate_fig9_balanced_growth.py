"""
Figure 9: Balanced Growth Framework (Fine/Hausmann)
Panel A: Growth Anatomy (2×2 Matrix)
Panel B: Growth Diagnostics Tree
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

# Color scheme (consistent with Ch2_Fig1_B_trajectories.png)
COLORS = {
    'green': '#2E8B57',      # Balanced Engine (Zoom-out)
    'blue': '#4682B4',       # Zoom-in
    'gray': '#808080',       # Stayer / Dead Zone
    'red': '#CD5C5C',        # Operational Trap
    'gold': '#DAA520',       # Market Mirage / Golden Cage
    'light_gray': '#E8E8E8', # Background
    'text': '#333333'
}

def create_panel_a(ax):
    """Panel A: Growth Anatomy 2×2 Matrix"""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')

    # Draw quadrants
    # Type A: Operational Trap (Low Market, High Ops) - top left
    rect_a = FancyBboxPatch((0.5, 5.5), 4, 4,
                             boxstyle="round,pad=0.05",
                             facecolor=COLORS['red'], alpha=0.7,
                             edgecolor='white', linewidth=2)
    ax.add_patch(rect_a)

    # Type C: Balanced Engine (High Market, High Ops) - top right
    rect_c = FancyBboxPatch((5.5, 5.5), 4, 4,
                             boxstyle="round,pad=0.05",
                             facecolor=COLORS['green'], alpha=0.8,
                             edgecolor='white', linewidth=2)
    ax.add_patch(rect_c)

    # Dead Zone (Low Market, Low Ops) - bottom left
    rect_dead = FancyBboxPatch((0.5, 0.5), 4, 4,
                                boxstyle="round,pad=0.05",
                                facecolor=COLORS['gray'], alpha=0.4,
                                edgecolor='white', linewidth=2)
    ax.add_patch(rect_dead)

    # Type B: Market Mirage (High Market, Low Ops) - bottom right
    rect_b = FancyBboxPatch((5.5, 0.5), 4, 4,
                             boxstyle="round,pad=0.05",
                             facecolor=COLORS['gold'], alpha=0.7,
                             edgecolor='white', linewidth=2)
    ax.add_patch(rect_b)

    # Labels for quadrants
    ax.text(2.5, 8.2, 'OPERATIONAL\nTRAP', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')
    ax.text(2.5, 6.5, '(Type A)', ha='center', va='center',
            fontsize=9, color='white', alpha=0.9)

    ax.text(7.5, 8.2, 'BALANCED\nENGINE', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')
    ax.text(7.5, 6.5, '(Type C)', ha='center', va='center',
            fontsize=9, color='white', alpha=0.9)

    ax.text(2.5, 2.5, 'DEAD\nZONE', ha='center', va='center',
            fontsize=11, fontweight='bold', color=COLORS['text'], alpha=0.7)

    ax.text(7.5, 3.2, 'MARKET\nMIRAGE', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')
    ax.text(7.5, 1.5, '(Type B)', ha='center', va='center',
            fontsize=9, color='white', alpha=0.9)

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
    """Panel B: Growth Diagnostics Tree (Hausmann08)"""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Tree structure coordinates
    # Level 0: Root
    root_y = 9.5
    root_x = 5

    # Level 1: Demand-side vs Supply-side
    l1_y = 7.5
    demand_x = 2.5
    supply_x = 7.5

    # Level 2: Sub-categories
    l2_y = 5.5
    # Demand side
    pmf_x = 1.5
    crowded_x = 3.5
    # Supply side
    execution_x = 6.5
    resource_x = 8.5

    # Level 3: Execution breakdown
    l3_y = 3.5
    team_x = 5.8
    cage_x = 7.2

    # Draw connections (lines)
    line_color = COLORS['gray']
    lw = 1.5

    # Root to Level 1
    ax.plot([root_x, demand_x], [root_y - 0.3, l1_y + 0.5], color=line_color, lw=lw)
    ax.plot([root_x, supply_x], [root_y - 0.3, l1_y + 0.5], color=line_color, lw=lw)

    # Demand side to Level 2
    ax.plot([demand_x, pmf_x], [l1_y - 0.5, l2_y + 0.4], color=line_color, lw=lw)
    ax.plot([demand_x, crowded_x], [l1_y - 0.5, l2_y + 0.4], color=line_color, lw=lw)

    # Supply side to Level 2
    ax.plot([supply_x, execution_x], [l1_y - 0.5, l2_y + 0.4], color=line_color, lw=lw)
    ax.plot([supply_x, resource_x], [l1_y - 0.5, l2_y + 0.4], color=line_color, lw=lw)

    # Execution to Level 3
    ax.plot([execution_x, team_x], [l2_y - 0.4, l3_y + 0.5], color=line_color, lw=lw)
    ax.plot([execution_x, cage_x], [l2_y - 0.4, l3_y + 0.5], color=COLORS['gold'], lw=2.5)

    # Draw nodes
    node_height = 0.8

    # Root node
    root_box = FancyBboxPatch((root_x - 1.8, root_y - 0.3), 3.6, node_height,
                               boxstyle="round,pad=0.02",
                               facecolor=COLORS['light_gray'],
                               edgecolor=COLORS['text'], linewidth=1.5)
    ax.add_patch(root_box)
    ax.text(root_x, root_y + 0.1, 'Low Startup Growth\n(G < median)',
            ha='center', va='center', fontsize=9, fontweight='bold')

    # Level 1 nodes
    # Demand-side
    demand_box = FancyBboxPatch((demand_x - 1.3, l1_y - 0.3), 2.6, node_height,
                                 boxstyle="round,pad=0.02",
                                 facecolor='#FFE4E1',  # Light red
                                 edgecolor=COLORS['red'], linewidth=1.5)
    ax.add_patch(demand_box)
    ax.text(demand_x, l1_y + 0.1, 'DEMAND-SIDE\n(Low Market Pull)',
            ha='center', va='center', fontsize=8, fontweight='bold', color=COLORS['red'])

    # Supply-side
    supply_box = FancyBboxPatch((supply_x - 1.3, l1_y - 0.3), 2.6, node_height,
                                 boxstyle="round,pad=0.02",
                                 facecolor='#E6E6FA',  # Light blue
                                 edgecolor=COLORS['blue'], linewidth=1.5)
    ax.add_patch(supply_box)
    ax.text(supply_x, l1_y + 0.1, 'SUPPLY-SIDE\n(Low Ops Capability)',
            ha='center', va='center', fontsize=8, fontweight='bold', color=COLORS['blue'])

    # Level 2 nodes
    # PMF
    ax.add_patch(FancyBboxPatch((pmf_x - 0.7, l2_y - 0.2), 1.4, 0.6,
                                 boxstyle="round,pad=0.02",
                                 facecolor='white', edgecolor=COLORS['gray'], linewidth=1))
    ax.text(pmf_x, l2_y + 0.1, 'Weak\nPMF', ha='center', va='center', fontsize=7)

    # Crowded Market
    ax.add_patch(FancyBboxPatch((crowded_x - 0.7, l2_y - 0.2), 1.4, 0.6,
                                 boxstyle="round,pad=0.02",
                                 facecolor='white', edgecolor=COLORS['gray'], linewidth=1))
    ax.text(crowded_x, l2_y + 0.1, 'Crowded\nMarket', ha='center', va='center', fontsize=7)

    # Execution Failure
    ax.add_patch(FancyBboxPatch((execution_x - 0.8, l2_y - 0.2), 1.6, 0.6,
                                 boxstyle="round,pad=0.02",
                                 facecolor='white', edgecolor=COLORS['gray'], linewidth=1))
    ax.text(execution_x, l2_y + 0.1, 'Execution\nFailure', ha='center', va='center', fontsize=7)

    # Resource Constraint
    ax.add_patch(FancyBboxPatch((resource_x - 0.8, l2_y - 0.2), 1.6, 0.6,
                                 boxstyle="round,pad=0.02",
                                 facecolor='white', edgecolor=COLORS['gray'], linewidth=1))
    ax.text(resource_x, l2_y + 0.1, 'Resource\nConstraint', ha='center', va='center', fontsize=7)

    # Level 3 nodes
    # Team Gap
    ax.add_patch(FancyBboxPatch((team_x - 0.6, l3_y - 0.2), 1.2, 0.6,
                                 boxstyle="round,pad=0.02",
                                 facecolor='white', edgecolor=COLORS['gray'], linewidth=1))
    ax.text(team_x, l3_y + 0.1, 'Team\nGap', ha='center', va='center', fontsize=7)

    # Golden Cage (highlighted!)
    cage_box = FancyBboxPatch((cage_x - 0.9, l3_y - 0.4), 1.8, 1.0,
                               boxstyle="round,pad=0.02",
                               facecolor=COLORS['gold'], alpha=0.9,
                               edgecolor='#B8860B', linewidth=2.5)
    ax.add_patch(cage_box)
    ax.text(cage_x, l3_y + 0.3, 'GOLDEN\nCAGE', ha='center', va='center',
            fontsize=8, fontweight='bold', color='white')
    ax.text(cage_x, l3_y - 0.15, 'E↑ → R↓', ha='center', va='center',
            fontsize=7, color='white', style='italic')

    # Title
    ax.set_title("Panel B: Growth Diagnostics Tree\nLiebig's Law: Growth = min(Market, Ops)",
                 fontsize=13, fontweight='bold', pad=10)

    # Legend note
    ax.text(5, 1.5, '★ Golden Cage = Funding Trap under Supply-side Constraint',
            ha='center', va='center', fontsize=9, style='italic', color=COLORS['gold'])


def main():
    # Create figure with two panels
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

    # Set background
    fig.patch.set_facecolor('white')

    # Create panels
    create_panel_a(ax1)
    create_panel_b(ax2)

    # Main title
    fig.suptitle('Figure 9: Balanced Growth Framework (Fine 2024; Hausmann et al. 2008)',
                 fontsize=14, fontweight='bold', y=0.98)

    plt.tight_layout(rect=[0, 0, 1, 0.95])

    # Save figure
    output_path = '/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/papers_v7_sail/figures/Fig9_balanced_growth.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"Figure saved to: {output_path}")

    plt.close()


if __name__ == "__main__":
    main()
