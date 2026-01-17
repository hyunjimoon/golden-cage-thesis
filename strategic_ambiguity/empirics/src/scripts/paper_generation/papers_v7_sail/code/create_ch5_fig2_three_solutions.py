#!/usr/bin/env python3
"""
Create Ch5 Fig2: Three Solutions to the Golden Cage
===================================================
Professional diagram with unified visual language.

Design principles applied:
- Consistent color palette (Maryland flag colors)
- Unified typography hierarchy
- Cage metaphor integrated across all panels
- High data-ink ratio (Tufte)
- Print-ready text sizing
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch, Circle
import numpy as np

# =============================================================================
# COLOR PALETTE (Maryland Flag - from thesis)
# =============================================================================
COLORS = {
    'red': '#E03C31',      # Crossland red
    'gold': '#FFD200',     # Crossland gold
    'black': '#2D2926',    # Calvert black
    'white': '#FFFFFF',    # Calvert white
    'gray_dark': '#4A4A4A',
    'gray_light': '#E8E8E8',
    'gray_mid': '#9B9B9B',
    'blue_accent': '#1E4D8C',  # Complementary
}

# Semantic colors for the three solutions
COLOR_AMBIGUITY = COLORS['blue_accent']   # Panel 1
COLOR_GROWTH = COLORS['red']              # Panel 2
COLOR_FUNDING = COLORS['gold']            # Panel 3
COLOR_CAGE = COLORS['black']              # Cage elements

# =============================================================================
# FIGURE SETUP
# =============================================================================
fig = plt.figure(figsize=(14, 6), facecolor='white', dpi=150)

# Create gridspec for three panels with shared header
gs = fig.add_gridspec(2, 3, height_ratios=[0.08, 0.92],
                      hspace=0.02, wspace=0.12,
                      left=0.05, right=0.95, top=0.90, bottom=0.08)

# =============================================================================
# MAIN TITLE
# =============================================================================
fig.suptitle('Three Escapes from the Golden Cage',
             fontsize=18, fontweight='bold', color=COLORS['black'],
             y=0.98)

# =============================================================================
# HELPER: Draw cage bars (simplified)
# =============================================================================
def draw_cage_icon(ax, x, y, size=0.15, color=COLOR_CAGE, alpha=0.6, open_pct=0):
    """Draw a small cage icon. open_pct controls how 'open' the bars are."""
    bar_width = size * 0.08
    n_bars = 5
    spacing = size / (n_bars - 1)

    # Vertical bars
    for i in range(n_bars):
        bar_x = x - size/2 + i * spacing
        # Open bars bend outward
        offset = open_pct * (abs(i - n_bars//2) / (n_bars//2)) * size * 0.3
        ax.plot([bar_x - offset, bar_x + offset], [y - size/2, y + size/2],
                color=color, linewidth=1.5, alpha=alpha)

    # Top and bottom bars
    ax.plot([x - size/2, x + size/2], [y + size/2, y + size/2],
            color=color, linewidth=2, alpha=alpha)
    ax.plot([x - size/2, x + size/2], [y - size/2, y - size/2],
            color=color, linewidth=2, alpha=alpha)

# =============================================================================
# PANEL 1: Strategic Ambiguity - Sweet Spot
# =============================================================================
ax1_header = fig.add_subplot(gs[0, 0])
ax1 = fig.add_subplot(gs[1, 0])

# Header
ax1_header.set_xlim(0, 1)
ax1_header.set_ylim(0, 1)
# Add colored rectangle as background
rect1 = FancyBboxPatch((0.02, 0.1), 0.96, 0.8, boxstyle="round,pad=0.02",
                        facecolor=COLOR_AMBIGUITY, edgecolor='none')
ax1_header.add_patch(rect1)
ax1_header.text(0.5, 0.5, '1. WHAT to commit to',
                ha='center', va='center', fontsize=12, fontweight='bold',
                color='white', zorder=10)
ax1_header.set_facecolor('none')
ax1_header.axis('off')

# Sweet spot curve
ax1.set_xlim(-0.5, 4.5)
ax1.set_ylim(0, 18)

# Data points (quartiles)
x_q = [0, 1, 2, 3]
y_surv = [7.1, 11.4, 15.0, 10.7]
labels = ['Q1\nNarrow', 'Q2', 'Q3\nSweet\nSpot', 'Q4\nBroad']

# Smooth curve
x_smooth = np.linspace(0, 3, 100)
# Fit a polynomial for smooth curve
coeffs = np.polyfit(x_q, y_surv, 3)
y_smooth = np.polyval(coeffs, x_smooth)

# Sweet spot zone (Q2-Q3 region)
ax1.axvspan(1.5, 2.5, alpha=0.2, color=COLOR_AMBIGUITY, label='Sweet Spot Zone')

# Plot curve and points
ax1.fill_between(x_smooth, 0, y_smooth, alpha=0.1, color=COLOR_AMBIGUITY)
ax1.plot(x_smooth, y_smooth, color=COLOR_AMBIGUITY, linewidth=3, zorder=3)
ax1.scatter(x_q, y_surv, s=120, color=COLOR_AMBIGUITY, zorder=4, edgecolor='white', linewidth=2)

# Labels for each point
for i, (x, y, label) in enumerate(zip(x_q, y_surv, labels)):
    va = 'bottom' if i != 2 else 'bottom'
    ax1.annotate(f'{y}%', (x, y + 0.8), ha='center', va='bottom',
                 fontsize=11, fontweight='bold', color=COLORS['black'])

# X-axis labels
ax1.set_xticks(x_q)
ax1.set_xticklabels(['Q1\nNarrow', 'Q2', 'Q3\nOptimal', 'Q4\nBroad'], fontsize=10)

# Axis styling
ax1.set_ylabel('Survival Rate (%)', fontsize=11, fontweight='bold')
ax1.set_xlabel('Positioning Breadth', fontsize=11, fontweight='bold')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.set_yticks([0, 5, 10, 15])

# Key insight text
ax1.text(2, 1.5, 'Commit to direction,\nnot destination',
         ha='center', va='bottom', fontsize=10, fontstyle='italic',
         color=COLORS['gray_dark'],
         bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=COLORS['gray_light']))

# Small cage icon (opening)
draw_cage_icon(ax1, 3.8, 14, size=1.8, alpha=0.3, open_pct=0.5)

# =============================================================================
# PANEL 2: Balanced Growth - Diagonal Path
# =============================================================================
ax2_header = fig.add_subplot(gs[0, 1])
ax2 = fig.add_subplot(gs[1, 1])

# Header
ax2_header.set_xlim(0, 1)
ax2_header.set_ylim(0, 1)
rect2 = FancyBboxPatch((0.02, 0.1), 0.96, 0.8, boxstyle="round,pad=0.02",
                        facecolor=COLOR_GROWTH, edgecolor='none')
ax2_header.add_patch(rect2)
ax2_header.text(0.5, 0.5, '2. HOW to grow',
                ha='center', va='center', fontsize=12, fontweight='bold',
                color='white', zorder=10)
ax2_header.set_facecolor('none')
ax2_header.axis('off')

# 2x2 matrix
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

# Quadrant backgrounds
# Top-left: Scale Trap (high demand, low ops)
trap1 = FancyBboxPatch((0.5, 5.5), 4, 4, boxstyle="round,pad=0.1",
                        facecolor=COLORS['gold'], alpha=0.3, edgecolor=COLOR_GROWTH, linewidth=2)
ax2.add_patch(trap1)

# Bottom-right: Operational Trap (low demand, high ops)
trap2 = FancyBboxPatch((5.5, 0.5), 4, 4, boxstyle="round,pad=0.1",
                        facecolor=COLORS['gold'], alpha=0.3, edgecolor=COLOR_GROWTH, linewidth=2)
ax2.add_patch(trap2)

# Diagonal success zone
ax2.fill([0.5, 5, 9.5, 5, 0.5], [0.5, 5, 9.5, 5, 0.5],
         alpha=0.0)  # Invisible, just for reference

# Diagonal arrow (the escape path)
ax2.annotate('', xy=(8.5, 8.5), xytext=(1.5, 1.5),
             arrowprops=dict(arrowstyle='->', color=COLORS['black'],
                            lw=3, mutation_scale=20))

# Diagonal label
ax2.text(5, 5.8, 'Balanced\nGrowth', ha='center', va='center',
         fontsize=11, fontweight='bold', color=COLORS['black'],
         bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                   edgecolor=COLORS['black'], linewidth=2))

# Trap labels
ax2.text(2.5, 7.5, 'SCALE\nTRAP', ha='center', va='center',
         fontsize=10, fontweight='bold', color=COLOR_GROWTH)
ax2.text(2.5, 6.2, 'Demand without\ndelivery capacity', ha='center', va='center',
         fontsize=8, color=COLORS['gray_dark'], fontstyle='italic')

ax2.text(7.5, 2.5, 'OPS\nTRAP', ha='center', va='center',
         fontsize=10, fontweight='bold', color=COLOR_GROWTH)
ax2.text(7.5, 1.3, 'Capability without\nmarket pull', ha='center', va='center',
         fontsize=8, color=COLORS['gray_dark'], fontstyle='italic')

# Axis labels
ax2.set_xlabel('Operational Capability (Supply)', fontsize=11, fontweight='bold')
ax2.set_ylabel('Market Maturity (Demand)', fontsize=11, fontweight='bold')

# Remove ticks but keep labels
ax2.set_xticks([])
ax2.set_yticks([])

# Add Low/High labels
ax2.text(0.5, -0.5, 'Low', fontsize=9, ha='center', color=COLORS['gray_dark'])
ax2.text(9.5, -0.5, 'High', fontsize=9, ha='center', color=COLORS['gray_dark'])
ax2.text(-0.5, 0.5, 'Low', fontsize=9, ha='center', va='center',
         rotation=90, color=COLORS['gray_dark'])
ax2.text(-0.5, 9.5, 'High', fontsize=9, ha='center', va='center',
         rotation=90, color=COLORS['gray_dark'])

# Draw small cage icons in trap zones
draw_cage_icon(ax2, 1.5, 8.5, size=1.2, color=COLOR_CAGE, alpha=0.4)
draw_cage_icon(ax2, 8.5, 1.5, size=1.2, color=COLOR_CAGE, alpha=0.4)

# Key insight
ax2.text(5, 0.3, 'Growth = Market × Ops', ha='center', va='bottom',
         fontsize=9, fontstyle='italic', color=COLORS['gray_dark'])

ax2.set_aspect('equal')
ax2.axis('off')

# =============================================================================
# PANEL 3: Financial Vehicle - Funding Ladder
# =============================================================================
ax3_header = fig.add_subplot(gs[0, 2])
ax3 = fig.add_subplot(gs[1, 2])

# Header
ax3_header.set_xlim(0, 1)
ax3_header.set_ylim(0, 1)
rect3 = FancyBboxPatch((0.02, 0.1), 0.96, 0.8, boxstyle="round,pad=0.02",
                        facecolor=COLOR_FUNDING, edgecolor='none')
ax3_header.add_patch(rect3)
ax3_header.text(0.5, 0.5, '3. HOW to fund',
                ha='center', va='center', fontsize=12, fontweight='bold',
                color=COLORS['black'], zorder=10)
ax3_header.set_facecolor('none')
ax3_header.axis('off')

# Ladder visualization
ax3.set_xlim(0, 10)
ax3.set_ylim(0, 10)

# Draw ladder rungs (bottom to top)
rungs = [
    {'y': 1.5, 'label': 'Non-Dilutive', 'sublabel': 'NSF, DARPA, DOE',
     'benefit': 'Credibility, no governance strings', 'color': COLORS['gray_light']},
    {'y': 4.5, 'label': 'Matching Capital', 'sublabel': 'State/Local grants',
     'benefit': 'Extends runway, preserves signal', 'color': COLORS['gray_mid']},
    {'y': 7.5, 'label': 'Thesis-Driven VC', 'sublabel': 'After validation',
     'benefit': 'From strength, not desperation', 'color': COLOR_FUNDING},
]

# Draw ladder sides
ax3.plot([2, 2], [0.5, 9], color=COLORS['black'], linewidth=3)
ax3.plot([8, 8], [0.5, 9], color=COLORS['black'], linewidth=3)

# Draw rungs and labels
for rung in rungs:
    y = rung['y']

    # Rung bar
    rung_patch = FancyBboxPatch((2, y - 0.4), 6, 0.8,
                                 boxstyle="round,pad=0.05",
                                 facecolor=rung['color'],
                                 edgecolor=COLORS['black'], linewidth=2)
    ax3.add_patch(rung_patch)

    # Main label (on the rung)
    ax3.text(5, y, rung['label'], ha='center', va='center',
             fontsize=11, fontweight='bold', color=COLORS['black'])

# Side annotations (benefits)
ax3.text(9.2, 1.5, '• No board seats\n• Technical credibility',
         ha='left', va='center', fontsize=8, color=COLORS['gray_dark'])
ax3.text(9.2, 4.5, '• Compounds signal\n• Extends runway',
         ha='left', va='center', fontsize=8, color=COLORS['gray_dark'])
ax3.text(9.2, 7.5, '• Negotiate from strength\n• Market clarity',
         ha='left', va='center', fontsize=8, color=COLORS['gray_dark'])

# Upward arrow showing progression
ax3.annotate('', xy=(1, 8.5), xytext=(1, 1),
             arrowprops=dict(arrowstyle='->', color=COLORS['black'],
                            lw=2, mutation_scale=15))
ax3.text(0.5, 4.5, 'Time', ha='center', va='center', rotation=90,
         fontsize=10, color=COLORS['gray_dark'])

# Key insight at bottom
ax3.text(5, 0.2, 'Delay governance capture\nuntil signals clarify',
         ha='center', va='bottom', fontsize=9, fontstyle='italic',
         color=COLORS['gray_dark'])

# Draw cage at top (representing what you're climbing out of)
draw_cage_icon(ax3, 5, 9.3, size=1.0, alpha=0.3, open_pct=0.8)

ax3.axis('off')

# =============================================================================
# SAVE
# =============================================================================
output_path = '/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/papers_v7_sail/img/Ch5_Fig2_three_solutions_v2.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()

print(f"✓ Figure saved to: {output_path}")
print("\nDesign features:")
print("  • Unified color palette (Maryland flag)")
print("  • Consistent typography hierarchy")
print("  • Cage metaphor integrated across all panels")
print("  • High data-ink ratio")
print("  • Print-ready (300 DPI)")
