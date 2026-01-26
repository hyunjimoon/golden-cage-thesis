#!/usr/bin/env python3
"""
Create Ch5 Fig2: Three Solutions to the Golden Cage
===================================================
WORLD-CLASS figure design with NO OVERLAPPING TEXT.

Panel order: (A) Scope, (B) Sequencing, (C) Synchronized
Colors: GRAYSCALE (가장 안전 - print-safe)

Design principles:
- ZERO text overlap
- Maximum whitespace
- Tufte-inspired data-ink ratio
- 70-year-old readable fonts
- Grayscale for print safety
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
from pathlib import Path

# =============================================================================
# COLOR PALETTE - GRAYSCALE (가장 안전)
# =============================================================================
COLORS = {
    'primary': '#2C3E50',
    'black': '#1E1E1E',
    'white': '#FFFFFF',
    'gray_dark': '#4A4A4A',
    'gray_light': '#E8E8E8',
    'gray_mid': '#9E9E9E',
}

# All panels in grayscale for consistency and print safety
COLOR_SCOPE = '#5D5D5D'      # Medium gray
COLOR_SEQ = '#3D3D3D'        # Dark gray
COLOR_SYNC = '#7D7D7D'       # Light-medium gray

# =============================================================================
# FIGURE SETUP - wider spacing between panels
# =============================================================================
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica Neue', 'Helvetica', 'Arial'],
    'font.size': 12,
})

fig = plt.figure(figsize=(15, 5), facecolor='white', dpi=150)

# More space between panels (wspace=0.25)
gs = fig.add_gridspec(2, 3, height_ratios=[0.08, 0.92],
                      hspace=0.02, wspace=0.25,
                      left=0.05, right=0.95, top=0.92, bottom=0.08)

# =============================================================================
# PANEL A: SCOPE - Sweet Spot Curve
# =============================================================================
ax1_header = fig.add_subplot(gs[0, 0])
ax1 = fig.add_subplot(gs[1, 0])

# Header
ax1_header.set_xlim(0, 1)
ax1_header.set_ylim(0, 1)
rect1 = FancyBboxPatch((0.02, 0.1), 0.96, 0.8, boxstyle="round,pad=0.02",
                        facecolor=COLOR_SCOPE, edgecolor='none')
ax1_header.add_patch(rect1)
ax1_header.text(0.5, 0.5, '(A) Scope',
                ha='center', va='center', fontsize=16, fontweight='bold',
                color='white', zorder=10)
ax1_header.axis('off')

# Data
x_q = [0, 1, 2, 3]
y_surv = [7.1, 11.4, 15.0, 10.7]

x_smooth = np.linspace(0, 3, 100)
coeffs = np.polyfit(x_q, y_surv, 3)
y_smooth = np.polyval(coeffs, x_smooth)

# Plot
ax1.set_xlim(-0.3, 3.3)
ax1.set_ylim(0, 18)
ax1.axvspan(1.5, 2.5, alpha=0.12, color=COLOR_SCOPE)
ax1.fill_between(x_smooth, 0, y_smooth, alpha=0.06, color=COLOR_SCOPE)
ax1.plot(x_smooth, y_smooth, color=COLOR_SCOPE, linewidth=3, zorder=3)
ax1.scatter(x_q, y_surv, s=100, color=COLOR_SCOPE, zorder=4, edgecolor='white', linewidth=2)

# Labels
for x, y in zip(x_q, y_surv):
    ax1.annotate(f'{y}%', (x, y + 0.8), ha='center', va='bottom',
                 fontsize=13, fontweight='bold', color=COLORS['primary'])

ax1.set_xticks(x_q)
ax1.set_xticklabels(['Q1', 'Q2', 'Q3', 'Q4'], fontsize=12)
ax1.set_ylabel('Success Rate (%)', fontsize=13)
ax1.set_xlabel('Strategic Breadth', fontsize=13)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.set_yticks([0, 5, 10, 15])
ax1.tick_params(labelsize=11)

# =============================================================================
# PANEL B: SEQUENCING - Funding Ladder (SELF-CONTAINED, no overflow)
# =============================================================================
ax2_header = fig.add_subplot(gs[0, 1])
ax2 = fig.add_subplot(gs[1, 1])

# Header
ax2_header.set_xlim(0, 1)
ax2_header.set_ylim(0, 1)
rect2 = FancyBboxPatch((0.02, 0.1), 0.96, 0.8, boxstyle="round,pad=0.02",
                        facecolor=COLOR_SEQ, edgecolor='none')
ax2_header.add_patch(rect2)
ax2_header.text(0.5, 0.5, '(B) Sequencing',
                ha='center', va='center', fontsize=16, fontweight='bold',
                color='white', zorder=10)
ax2_header.axis('off')

# Ladder - COMPACT, all text INSIDE panel bounds
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

# Rungs (centered, no side annotations that overflow) - grayscale gradient
rungs = [
    {'y': 2, 'label': 'Non-Dilutive', 'color': '#E0E0E0'},   # Lightest
    {'y': 5, 'label': 'Matching', 'color': '#B0B0B0'},       # Medium
    {'y': 8, 'label': 'VC', 'color': '#707070'},             # Darkest
]

# Ladder sides
ax2.plot([2.5, 2.5], [0.5, 9.5], color=COLORS['primary'], linewidth=2.5)
ax2.plot([7.5, 7.5], [0.5, 9.5], color=COLORS['primary'], linewidth=2.5)

# Rungs
for rung in rungs:
    y = rung['y']
    rung_patch = FancyBboxPatch((2.5, y - 0.6), 5, 1.2,
                                 boxstyle="round,pad=0.05",
                                 facecolor=rung['color'],
                                 edgecolor=COLORS['primary'], linewidth=2)
    ax2.add_patch(rung_patch)
    ax2.text(5, y, rung['label'], ha='center', va='center',
             fontsize=14, fontweight='bold', color=COLORS['primary'])

# Arrow (inside bounds)
ax2.annotate('', xy=(1.2, 9), xytext=(1.2, 1),
             arrowprops=dict(arrowstyle='->', color=COLORS['primary'],
                            lw=2.5, mutation_scale=20))

ax2.axis('off')

# =============================================================================
# PANEL C: SYNCHRONIZED - 2x2 Matrix (SELF-CONTAINED)
# =============================================================================
ax3_header = fig.add_subplot(gs[0, 2])
ax3 = fig.add_subplot(gs[1, 2])

# Header
ax3_header.set_xlim(0, 1)
ax3_header.set_ylim(0, 1)
rect3 = FancyBboxPatch((0.02, 0.1), 0.96, 0.8, boxstyle="round,pad=0.02",
                        facecolor=COLOR_SYNC, edgecolor='none')
ax3_header.add_patch(rect3)
ax3_header.text(0.5, 0.5, '(C) Synchronized',
                ha='center', va='center', fontsize=16, fontweight='bold',
                color='white', zorder=10)
ax3_header.axis('off')

# 2x2 Matrix - all elements inside bounds
ax3.set_xlim(0, 10)
ax3.set_ylim(0, 10)

# Trap zones (positioned away from edges) - grayscale
trap1 = FancyBboxPatch((1, 5.5), 3.5, 3.5, boxstyle="round,pad=0.1",
                        facecolor='#D0D0D0', alpha=0.6, edgecolor='#808080', linewidth=2)
ax3.add_patch(trap1)

trap2 = FancyBboxPatch((5.5, 1), 3.5, 3.5, boxstyle="round,pad=0.1",
                        facecolor='#D0D0D0', alpha=0.6, edgecolor='#808080', linewidth=2)
ax3.add_patch(trap2)

# Diagonal arrow
ax3.annotate('', xy=(8.5, 8.5), xytext=(1.5, 1.5),
             arrowprops=dict(arrowstyle='->', color=COLORS['primary'],
                            lw=3, mutation_scale=20))

# Labels INSIDE boxes (no overflow)
ax3.text(2.75, 7.25, 'Market\nPull', ha='center', va='center',
         fontsize=13, fontweight='bold', color=COLOR_SYNC)

ax3.text(7.25, 2.75, 'Capability\nPush', ha='center', va='center',
         fontsize=13, fontweight='bold', color=COLOR_SYNC)

# Balanced Growth label
ax3.text(5, 5, 'Balanced', ha='center', va='center',
         fontsize=12, fontweight='bold', color=COLORS['primary'],
         bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                   edgecolor=COLORS['primary'], linewidth=2))

# Axis labels INSIDE panel
ax3.text(5, 0.3, 'Ops Capability', ha='center', va='bottom', fontsize=11, color=COLORS['gray_dark'])
ax3.text(0.3, 5, 'Market Size', ha='left', va='center', fontsize=11, color=COLORS['gray_dark'], rotation=90)

ax3.axis('off')

# =============================================================================
# SAVE
# =============================================================================
script_dir = Path(__file__).parent.resolve()
img_dir = script_dir.parent / 'img'
overleaf_img = script_dir.parent / 'overleaf_upload' / 'img'

img_dir.mkdir(parents=True, exist_ok=True)

output_path = img_dir / 'Ch5_Fig2_three_solutions.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')

if overleaf_img.exists():
    plt.savefig(overleaf_img / 'Ch5_Fig2_three_solutions.png', dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')

plt.close()

print(f"✓ Figure saved to: {output_path}")
print("\nWorld-class design: NO OVERLAP, clean minimalist aesthetics")
