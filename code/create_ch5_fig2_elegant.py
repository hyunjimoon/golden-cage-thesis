#!/usr/bin/env python3
"""
Create Ch5 Fig2: Three Solutions to the Golden Cage
===================================================
Elegant, minimalist design preserving original's sophistication.

Design principles:
- Warm, muted palette with sparse color accents
- Generous whitespace
- No overlapping text
- Consistent typography
- Subtle cage metaphor
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, PathPatch, Circle
from matplotlib.path import Path
import numpy as np

# =============================================================================
# COLOR PALETTE - Muted, elegant with Maryland accents
# =============================================================================
COLORS = {
    # Base palette (warm, muted)
    'bg_warm': '#FAF8F5',       # Warm off-white
    'bg_panel': '#F5F2ED',      # Subtle panel background
    'text_dark': '#2D2926',     # Near-black for text
    'text_mid': '#5C5652',      # Medium gray for secondary text
    'text_light': '#8A847D',    # Light gray for tertiary
    'line_dark': '#3D3835',     # Dark lines
    'line_light': '#D4CFC7',    # Light lines/borders

    # Maryland accents (used sparingly)
    'accent_blue': '#1E4D8C',   # For Panel 1
    'accent_red': '#C41E3A',    # For Panel 2 (muted red)
    'accent_gold': '#D4A017',   # For Panel 3 (muted gold)

    # Trap zones
    'trap_fill': '#F0E6D3',     # Warm beige for trap areas
    'sweet_spot': '#E8EEF4',    # Cool blue tint for sweet spot
}

# =============================================================================
# FIGURE SETUP
# =============================================================================
fig = plt.figure(figsize=(15, 5), facecolor=COLORS['bg_warm'], dpi=150)

# Three panels with spacing
gs = fig.add_gridspec(1, 3, wspace=0.15,
                      left=0.03, right=0.97, top=0.85, bottom=0.12)

# Main title - positioned higher to avoid overlap with panel numbers
fig.suptitle('Three Escapes from the Golden Cage',
             fontsize=16, fontweight='normal', color=COLORS['text_dark'],
             y=0.98, fontfamily='sans-serif')

# =============================================================================
# HELPER: Draw elegant cage
# =============================================================================
def draw_cage(ax, x, y, width=1.0, height=1.2, color='#3D3835', lw=1.5, alpha=0.7):
    """Draw an elegant cage icon."""
    # Top arc
    theta = np.linspace(0, np.pi, 30)
    arc_x = x + (width/2) * np.cos(theta)
    arc_y = y + height/2 + (height/4) * np.sin(theta)
    ax.plot(arc_x, arc_y, color=color, lw=lw, alpha=alpha)

    # Bottom line
    ax.plot([x - width/2, x + width/2], [y - height/2, y - height/2],
            color=color, lw=lw, alpha=alpha)

    # Vertical bars
    n_bars = 5
    for i in range(n_bars):
        bar_x = x - width/2 + (i / (n_bars-1)) * width
        ax.plot([bar_x, bar_x], [y - height/2, y + height/2],
                color=color, lw=lw*0.7, alpha=alpha*0.8)

# =============================================================================
# PANEL 1: Strategic Ambiguity - Sweet Spot
# =============================================================================
ax1 = fig.add_subplot(gs[0])
ax1.set_facecolor(COLORS['bg_panel'])

# Panel number and title
ax1.text(0.5, 1.08, '1', transform=ax1.transAxes, ha='center', va='bottom',
         fontsize=18, fontweight='bold', color=COLORS['accent_blue'], alpha=0.25)
ax1.text(0.5, 1.01, 'What to Commit To', transform=ax1.transAxes,
         ha='center', va='bottom', fontsize=11, fontweight='bold',
         color=COLORS['text_dark'])

# Data
x_q = np.array([1, 2, 3, 4])
y_surv = np.array([7.1, 11.4, 15.0, 10.7])

# Smooth curve
x_smooth = np.linspace(0.8, 4.2, 100)
coeffs = np.polyfit(x_q, y_surv, 3)
y_smooth = np.polyval(coeffs, x_smooth)

# Sweet spot highlight (subtle)
ax1.axvspan(2.5, 3.5, alpha=0.4, color=COLORS['sweet_spot'], zorder=1)

# Curve
ax1.fill_between(x_smooth, 0, y_smooth, alpha=0.08, color=COLORS['accent_blue'])
ax1.plot(x_smooth, y_smooth, color=COLORS['accent_blue'], linewidth=2.5, zorder=3)

# Data points
ax1.scatter(x_q, y_surv, s=80, color=COLORS['accent_blue'], zorder=4,
            edgecolor='white', linewidth=2)

# Labels - carefully positioned to avoid overlap
label_offsets = [(0, 1.5), (0, 1.5), (0, 1.5), (0, -2.2)]
for i, (x, y, offset) in enumerate(zip(x_q, y_surv, label_offsets)):
    va = 'bottom' if offset[1] > 0 else 'top'
    ax1.annotate(f'{y}%', (x, y + offset[1]*0.3),
                 ha='center', va=va, fontsize=10, fontweight='bold',
                 color=COLORS['text_dark'])

# X-axis labels
ax1.set_xticks(x_q)
ax1.set_xticklabels(['Q1', 'Q2', 'Q3', 'Q4'], fontsize=10, color=COLORS['text_mid'])
ax1.set_xlim(0.5, 4.5)
ax1.set_ylim(0, 18)

# Axis labels
ax1.set_xlabel('Positioning Breadth', fontsize=10, color=COLORS['text_mid'],
               labelpad=8)
ax1.text(0.5, -0.18, 'Narrow                                              Broad',
         transform=ax1.transAxes, ha='center', fontsize=8,
         color=COLORS['text_light'])

ax1.set_ylabel('Success Rate (%)', fontsize=10, color=COLORS['text_mid'])

# Clean up spines
for spine in ['top', 'right']:
    ax1.spines[spine].set_visible(False)
for spine in ['bottom', 'left']:
    ax1.spines[spine].set_color(COLORS['line_light'])
ax1.tick_params(colors=COLORS['text_light'])
ax1.set_yticks([0, 5, 10, 15])

# Key insight - positioned in clear space
ax1.text(3, 4, 'Sweet Spot',
         ha='center', va='center', fontsize=9, fontstyle='italic',
         color=COLORS['accent_blue'], fontweight='bold')

# =============================================================================
# PANEL 2: Balanced Growth - Diagonal Path
# =============================================================================
ax2 = fig.add_subplot(gs[1])
ax2.set_facecolor(COLORS['bg_panel'])

# Panel number and title
ax2.text(0.5, 1.08, '2', transform=ax2.transAxes, ha='center', va='bottom',
         fontsize=18, fontweight='bold', color=COLORS['accent_red'], alpha=0.25)
ax2.text(0.5, 1.01, 'How to Grow', transform=ax2.transAxes,
         ha='center', va='bottom', fontsize=11, fontweight='bold',
         color=COLORS['text_dark'])

ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

# Trap zones (subtle fill)
# Scale Trap (top-left)
trap1 = FancyBboxPatch((0.5, 5.5), 4, 4, boxstyle="round,pad=0.15",
                        facecolor=COLORS['trap_fill'], edgecolor=COLORS['line_light'],
                        linewidth=1.5, alpha=0.8)
ax2.add_patch(trap1)

# Ops Trap (bottom-right)
trap2 = FancyBboxPatch((5.5, 0.5), 4, 4, boxstyle="round,pad=0.15",
                        facecolor=COLORS['trap_fill'], edgecolor=COLORS['line_light'],
                        linewidth=1.5, alpha=0.8)
ax2.add_patch(trap2)

# Diagonal arrow (the escape path)
ax2.annotate('', xy=(8.2, 8.2), xytext=(1.8, 1.8),
             arrowprops=dict(arrowstyle='->', color=COLORS['text_dark'],
                            lw=2, mutation_scale=15))

# Balanced Growth label on diagonal
ax2.text(5.3, 5.8, 'Balanced Growth',
         ha='center', va='center', fontsize=10, fontweight='bold',
         color=COLORS['text_dark'], rotation=45,
         bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                   edgecolor=COLORS['line_light'], linewidth=1))

# Trap labels - positioned to avoid overlap
ax2.text(2.5, 8.2, 'Scale Trap', ha='center', va='center',
         fontsize=10, fontweight='bold', color=COLORS['accent_red'])
ax2.text(2.5, 6.8, 'demand without\ndelivery capacity', ha='center', va='center',
         fontsize=8, color=COLORS['text_light'], linespacing=1.2)

ax2.text(7.5, 3.5, 'Ops Trap', ha='center', va='center',
         fontsize=10, fontweight='bold', color=COLORS['accent_red'])
ax2.text(7.5, 2.1, 'capability without\nmarket pull', ha='center', va='center',
         fontsize=8, color=COLORS['text_light'], linespacing=1.2)

# Cage icons in trap zones
draw_cage(ax2, 2.5, 7.5, width=0.8, height=1.0, color=COLORS['line_dark'], alpha=0.2)
draw_cage(ax2, 7.5, 2.8, width=0.8, height=1.0, color=COLORS['line_dark'], alpha=0.2)

# Axis labels
ax2.text(5, -0.8, 'Operational Capability', ha='center', fontsize=10,
         color=COLORS['text_mid'])
ax2.text(-0.8, 5, 'Market\nMaturity', ha='center', va='center', fontsize=10,
         color=COLORS['text_mid'], rotation=90, linespacing=1.1)

# Corner labels
ax2.text(0.3, -0.3, 'Low', fontsize=8, color=COLORS['text_light'])
ax2.text(9.3, -0.3, 'High', fontsize=8, color=COLORS['text_light'])
ax2.text(-0.5, 0.3, 'Low', fontsize=8, color=COLORS['text_light'], rotation=90)
ax2.text(-0.5, 9.3, 'High', fontsize=8, color=COLORS['text_light'], rotation=90)

# Key insight
ax2.text(5, 0.3, 'Growth = Market × Ops',
         ha='center', va='bottom', fontsize=8, fontstyle='italic',
         color=COLORS['text_light'])

ax2.axis('off')

# =============================================================================
# PANEL 3: Financial Vehicle - Funding Ladder
# =============================================================================
ax3 = fig.add_subplot(gs[2])
ax3.set_facecolor(COLORS['bg_panel'])

# Panel number and title
ax3.text(0.5, 1.08, '3', transform=ax3.transAxes, ha='center', va='bottom',
         fontsize=18, fontweight='bold', color=COLORS['accent_gold'], alpha=0.25)
ax3.text(0.5, 1.01, 'How to Fund', transform=ax3.transAxes,
         ha='center', va='bottom', fontsize=11, fontweight='bold',
         color=COLORS['text_dark'])

ax3.set_xlim(0, 10)
ax3.set_ylim(0, 10)

# =============================================================================
# LADDER DESIGN - More realistic ladder shape
# =============================================================================
ladder_left = 2.8
ladder_right = 7.2
ladder_bottom = 0.8
ladder_top = 9.2

# Ladder sides (angled slightly for perspective)
side_offset = 0.3  # Slight taper at top
ax3.plot([ladder_left, ladder_left + side_offset],
         [ladder_bottom, ladder_top],
         color=COLORS['line_dark'], linewidth=4, solid_capstyle='round')
ax3.plot([ladder_right, ladder_right - side_offset],
         [ladder_bottom, ladder_top],
         color=COLORS['line_dark'], linewidth=4, solid_capstyle='round')

# Rungs (horizontal bars of the ladder)
rung_data = [
    {'y': 2.0, 'label': 'Non-Dilutive', 'sub': 'NSF · DARPA · DOE',
     'benefit': 'No governance strings'},
    {'y': 5.0, 'label': 'Matching Capital', 'sub': 'State & Local',
     'benefit': 'Compounds credibility'},
    {'y': 8.0, 'label': 'Thesis-Driven VC', 'sub': 'After validation',
     'benefit': 'Negotiate from strength'},
]

for i, rung in enumerate(rung_data):
    y = rung['y']
    # Calculate x positions based on ladder taper
    progress = (y - ladder_bottom) / (ladder_top - ladder_bottom)
    left_x = ladder_left + progress * side_offset
    right_x = ladder_right - progress * side_offset

    # Draw the rung (wooden bar look)
    rung_rect = FancyBboxPatch(
        (left_x + 0.1, y - 0.25),
        right_x - left_x - 0.2, 0.5,
        boxstyle="round,pad=0.02",
        facecolor=COLORS['trap_fill'],  # Warm wood-like color
        edgecolor=COLORS['line_dark'],
        linewidth=1.5
    )
    ax3.add_patch(rung_rect)

    # Label on the rung
    ax3.text((left_x + right_x) / 2, y, rung['label'],
             ha='center', va='center', fontsize=9, fontweight='bold',
             color=COLORS['text_dark'])

    # Sublabel below rung
    ax3.text((left_x + right_x) / 2, y - 0.6, rung['sub'],
             ha='center', va='top', fontsize=7, color=COLORS['text_light'])

# Benefits on right side (aligned with rungs)
ax3.text(8.0, 8.0, '• ' + rung_data[2]['benefit'], ha='left', va='center',
         fontsize=8, color=COLORS['text_mid'])
ax3.text(8.0, 5.0, '• ' + rung_data[1]['benefit'], ha='left', va='center',
         fontsize=8, color=COLORS['text_mid'])
ax3.text(8.0, 2.0, '• ' + rung_data[0]['benefit'], ha='left', va='center',
         fontsize=8, color=COLORS['text_mid'])

# Time arrow on left
ax3.annotate('', xy=(1.3, 8.5), xytext=(1.3, 1.5),
             arrowprops=dict(arrowstyle='->', color=COLORS['text_light'],
                            lw=1.5, mutation_scale=12))
ax3.text(0.9, 5, 'Time', ha='center', va='center', rotation=90,
         fontsize=9, color=COLORS['text_light'])

# Key insight at bottom
ax3.text(5.0, 0.3, 'Delay governance capture',
         ha='center', va='bottom', fontsize=8, fontstyle='italic',
         color=COLORS['text_light'])

ax3.axis('off')

# =============================================================================
# SAVE
# =============================================================================
output_path = '/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/papers_v7_sail/img/Ch5_Fig2_three_solutions.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight',
            facecolor=COLORS['bg_warm'], edgecolor='none')
plt.close()

print(f"✓ Elegant figure saved to: {output_path}")
