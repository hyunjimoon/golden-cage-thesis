#!/usr/bin/env python3
"""
Create Ch2 Fig1: Sorting Mechanism (Two-Panel)
==============================================
Left Panel: Causal DAG with hypothesis labels
Right Panel: Sorting illustration (Before/After Funding)

Colors:
- H1 (E→F, ρ(E,F)<0): Red (#E53935)
- H2 (F→G, ρ(F,G)>0): Blue (#4A90D9)
- H3 (E→G): Green (#28A745)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch
import numpy as np
from pathlib import Path

# =============================================================================
# COLOR PALETTE
# =============================================================================
COLOR_H1 = '#E53935'      # Red - Cage
COLOR_H2 = '#4A90D9'      # Blue - Flex
COLOR_H3 = '#28A745'      # Green - Paradox
COLOR_TEXT = '#2D2926'    # Dark text
COLOR_GRAY = '#808080'    # Gray for text
COLOR_BELIEVER = '#3D3D3D'   # Dark gray - Believers
COLOR_SKEPTIC = '#B0B0B0'    # Light gray - Skeptics

# =============================================================================
# FIGURE SETUP - Two panels
# =============================================================================
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica Neue', 'Helvetica', 'Arial'],
    'font.size': 12,
})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), facecolor='white')

# =============================================================================
# LEFT PANEL: CAUSAL DAG
# =============================================================================
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.set_aspect('equal')
ax1.axis('off')
ax1.set_title('(A) Causal Model', fontsize=14, fontweight='bold', pad=10)

# Node positions
pos_C = (2, 7.5)
pos_E = (6, 7.5)
pos_F = (4, 3.5)
pos_G = (8, 3.5)
node_radius = 0.55

def draw_arrow(ax, start, end, color, offset_start=0.7, offset_end=0.7, style='-', lw=3):
    """Draw arrow between two points with offset for node radius."""
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    dist = np.sqrt(dx**2 + dy**2)
    dx_norm, dy_norm = dx/dist, dy/dist
    x1 = start[0] + dx_norm * offset_start
    y1 = start[1] + dy_norm * offset_start
    x2 = end[0] - dx_norm * offset_end
    y2 = end[1] - dy_norm * offset_end

    if style == '--':
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                   linestyle=(0, (5, 3)), mutation_scale=20), zorder=5)
    else:
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                   mutation_scale=20), zorder=5)

# Draw nodes
# C node (dashed red)
c_circle = Circle(pos_C, node_radius, fill=False, edgecolor=COLOR_H1,
                  linewidth=2.5, linestyle='--', zorder=10)
ax1.add_patch(c_circle)
ax1.text(pos_C[0], pos_C[1], 'C', ha='center', va='center',
         fontsize=20, fontweight='bold', color=COLOR_H1, zorder=11)

# E node (red)
e_circle = Circle(pos_E, node_radius, fill=False, edgecolor=COLOR_H1,
                  linewidth=2.5, zorder=10)
ax1.add_patch(e_circle)
ax1.text(pos_E[0], pos_E[1], 'E', ha='center', va='center',
         fontsize=20, fontweight='bold', color=COLOR_H1, zorder=11)

# F node (red)
f_circle = Circle(pos_F, node_radius, fill=False, edgecolor=COLOR_H1,
                  linewidth=2.5, zorder=10)
ax1.add_patch(f_circle)
ax1.text(pos_F[0], pos_F[1], 'F', ha='center', va='center',
         fontsize=20, fontweight='bold', color=COLOR_H1, zorder=11)

# G node (blue)
g_circle = Circle(pos_G, node_radius, fill=False, edgecolor=COLOR_H2,
                  linewidth=2.5, zorder=10)
ax1.add_patch(g_circle)
ax1.text(pos_G[0], pos_G[1], 'G', ha='center', va='center',
         fontsize=20, fontweight='bold', color=COLOR_H2, zorder=11)

# =============================================================================
# DRAW ARROWS - 5X QUALITY: Precise positioning, NO OVERLAP
# =============================================================================

# C → E (solid red)
draw_arrow(ax1, pos_C, pos_E, COLOR_H1)
ax1.text(4.0, 8.1, '+', ha='center', va='center',
         fontsize=22, fontweight='bold', color=COLOR_H1)

# C → F (solid red) - minus sign CLOSE to the line
draw_arrow(ax1, pos_C, pos_F, COLOR_H1)
ax1.text(2.5, 5.8, '−', ha='center', va='center',
         fontsize=26, fontweight='bold', color=COLOR_H1)

# E → F (H1, DASHED red) - H1 label to RIGHT of arrow, higher up
draw_arrow(ax1, pos_E, pos_F, COLOR_H1, style='--')
ax1.text(5.8, 6.0, 'H1', ha='center', va='center',
         fontsize=18, fontweight='bold', color=COLOR_H1)
ax1.text(5.4, 4.8, '−', ha='center', va='center',
         fontsize=26, fontweight='bold', color=COLOR_H1)

# F → G (H2, solid blue) - label below arrow
draw_arrow(ax1, pos_F, pos_G, COLOR_H2)
ax1.text(6.0, 2.5, 'H2', ha='center', va='center',
         fontsize=18, fontweight='bold', color=COLOR_H2)
ax1.text(6.0, 4.0, '+', ha='center', va='center',
         fontsize=22, fontweight='bold', color=COLOR_H2)

# E → G (H3, dashed green) - label to right of arrow
draw_arrow(ax1, pos_E, pos_G, COLOR_H3, style='--')
ax1.text(8.0, 5.8, 'H3', ha='center', va='center',
         fontsize=18, fontweight='bold', color=COLOR_H3)
ax1.text(7.4, 5.2, '−', ha='center', va='center',
         fontsize=26, fontweight='bold', color=COLOR_H3)

# =============================================================================
# RIGHT PANEL: SORTING ILLUSTRATION
# =============================================================================
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.set_aspect('equal')
ax2.axis('off')
ax2.set_title('(B) Sorting Mechanism', fontsize=14, fontweight='bold', pad=10)

# Before Funding - 2x2 grid (mixed believers and skeptics)
ax2.text(1.5, 9, 'Before Funding', ha='center', va='center',
         fontsize=12, fontweight='bold', color=COLOR_TEXT)
ax2.text(1.5, 8.3, '(Diverse beliefs)', ha='center', va='center',
         fontsize=10, color=COLOR_GRAY, fontstyle='italic')

# 2x2 grid positions for Before
before_positions = [(0.8, 6.5), (2.2, 6.5), (0.8, 5.0), (2.2, 5.0)]
before_colors = [COLOR_BELIEVER, COLOR_SKEPTIC, COLOR_SKEPTIC, COLOR_BELIEVER]

for pos, color in zip(before_positions, before_colors):
    circle = Circle(pos, 0.4, facecolor=color, edgecolor='none', zorder=10)
    ax2.add_patch(circle)

# Arrow: Sorting
ax2.annotate('', xy=(5.5, 5.75), xytext=(3.5, 5.75),
             arrowprops=dict(arrowstyle='->', color=COLOR_TEXT, lw=2.5, mutation_scale=20))
ax2.text(4.5, 6.5, 'Sorting', ha='center', va='center',
         fontsize=12, fontweight='bold', color=COLOR_TEXT)
ax2.text(4.5, 4.9, '(Van den Steen)', ha='center', va='center',
         fontsize=9, color=COLOR_GRAY, fontstyle='italic')

# After Funding - 2x2 grid (homogeneous - all believers)
ax2.text(7.0, 9, 'After Funding', ha='center', va='center',
         fontsize=12, fontweight='bold', color=COLOR_TEXT)
ax2.text(7.0, 8.3, '(Homogeneous)', ha='center', va='center',
         fontsize=10, color=COLOR_GRAY, fontstyle='italic')

# 2x2 grid for After (all believers)
after_positions = [(6.3, 6.5), (7.7, 6.5), (6.3, 5.0), (7.7, 5.0)]
for pos in after_positions:
    circle = Circle(pos, 0.4, facecolor=COLOR_BELIEVER, edgecolor='none', zorder=10)
    ax2.add_patch(circle)

# Out column (skeptics left)
ax2.text(9.2, 9, 'Out', ha='center', va='center',
         fontsize=11, fontweight='bold', color=COLOR_GRAY)
out_positions = [(9.2, 6.5), (9.2, 5.0)]
for pos in out_positions:
    circle = Circle(pos, 0.4, facecolor=COLOR_SKEPTIC, edgecolor='none', zorder=10)
    ax2.add_patch(circle)

# Legend
ax2.text(1.5, 2.5, 'Legend:', ha='left', va='center',
         fontsize=11, fontweight='bold', color=COLOR_TEXT)
# Believer
believer_legend = Circle((1.8, 1.7), 0.3, facecolor=COLOR_BELIEVER, edgecolor='none')
ax2.add_patch(believer_legend)
ax2.text(2.5, 1.7, 'Believers', ha='left', va='center', fontsize=11, color=COLOR_TEXT)
# Skeptic
skeptic_legend = Circle((5.0, 1.7), 0.3, facecolor=COLOR_SKEPTIC, edgecolor='none')
ax2.add_patch(skeptic_legend)
ax2.text(5.7, 1.7, 'Skeptics', ha='left', va='center', fontsize=11, color=COLOR_TEXT)

# =============================================================================
# SAVE
# =============================================================================
plt.tight_layout()

script_dir = Path(__file__).parent.resolve()
img_dir = script_dir.parent / 'img'
overleaf_img = script_dir.parent / 'overleaf_upload' / 'img'

img_dir.mkdir(parents=True, exist_ok=True)

output_path = img_dir / 'Ch2_Fig1_sorting_mechanism.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')

if overleaf_img.exists():
    plt.savefig(overleaf_img / 'Ch2_Fig1_sorting_mechanism.png', dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')

plt.close()

print(f"✓ Figure saved to: {output_path}")
print("\nTwo-panel design:")
print("  (A) Causal DAG: H1=Red, H2=Blue, H3=Green")
print("  (B) Sorting: Before/After funding with believers/skeptics")
