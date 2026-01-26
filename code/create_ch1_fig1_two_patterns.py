#!/usr/bin/env python3
"""
Create Ch1 Fig1: Two Patterns of the Golden Cage
=================================================
10X PROFESSIONAL QUALITY - Science/Nature Journal Standard

Panel (A): Funding Suppresses Repositioning
Panel (B): Repositioning Predicts Success

Language from abstract:
- "funding suppresses repositioning"
- "repositioning predicts success"
- "movers outperform stayers by 2.6 times"

Design Philosophy:
- ZERO text overlap
- Maximum whitespace
- Tufte-inspired data-ink ratio
- 70-year-old readable fonts
- Clean, minimal academic style

Author: Golden Cage Thesis
Date: 2026-01-18
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# =============================================================================
# COLOR PALETTE (Science Journal Standard)
# =============================================================================
COLORS = {
    'cage': '#C62828',        # Deep Red - Commitment Cage (more professional)
    'flex': '#4A90D9',        # Signature Blue - matching Ch4_Fig1_G_by_R
    'gray_bar': '#9E9E9E',    # Medium gray for non-highlighted bars
    'text_dark': '#212121',   # Near black
    'text_mid': '#616161',    # Medium gray
    'text_light': '#9E9E9E',  # Light gray
}

# =============================================================================
# FIGURE SETTINGS - Professional Journal Quality
# =============================================================================
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica Neue', 'Helvetica', 'Arial'],
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.8,
    'ytick.major.width': 0.8,
})

# =============================================================================
# DATA
# =============================================================================

# Panel A: Funding Suppresses Repositioning
quartiles_a = ['Q1', 'Q2', 'Q3', 'Q4']
repo_rates = [47.1, 44.7, 40.0, 29.3]

# Panel B: Repositioning Predicts Success
categories_b = ['Stayers', 'Movers']
success_rates = [6.7, 17.6]

# =============================================================================
# CREATE FIGURE - Wide format for two panels
# =============================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4), facecolor='white')
fig.subplots_adjust(wspace=0.35)  # More space between panels

# =============================================================================
# PANEL A: FUNDING SUPPRESSES REPOSITIONING
# =============================================================================
x_a = np.arange(len(quartiles_a))

# Colors: gradient from light to dark, Q4 in red
colors_a = ['#BDBDBD', '#A0A0A0', '#808080', COLORS['cage']]

bars_a = ax1.bar(x_a, repo_rates, color=colors_a, edgecolor='none', width=0.65)

# Value labels INSIDE bars (no overlap with anything)
for i, (bar, rate) in enumerate(zip(bars_a, repo_rates)):
    y_pos = bar.get_height() - 3.5
    color = 'white' if i == 3 else COLORS['text_dark']
    ax1.text(bar.get_x() + bar.get_width()/2, y_pos,
             f'{rate}%', ha='center', va='top', fontsize=12,
             fontweight='bold', color=color)

# X-axis with funding level indicators
ax1.set_xticks(x_a)
ax1.set_xticklabels(quartiles_a, fontsize=11)
ax1.text(0, -7, 'Low', ha='center', fontsize=9, color=COLORS['text_light'])
ax1.text(3, -7, 'High', ha='center', fontsize=9, color=COLORS['text_light'])

# Axis labels
ax1.set_xlabel('Early Funding (E)', fontsize=12, color=COLORS['text_mid'], labelpad=12)
ax1.set_ylabel('Repositioning Rate (%)', fontsize=12, color=COLORS['text_mid'])
ax1.set_ylim(0, 55)

# Title - using abstract language
ax1.set_title('(A) Funding Suppresses Repositioning', fontsize=13,
              fontweight='bold', color=COLORS['text_dark'], loc='left', pad=12)

# Subtle grid
ax1.yaxis.grid(True, linestyle='-', alpha=0.15, color='gray')
ax1.set_axisbelow(True)

# =============================================================================
# PANEL B: REPOSITIONING PREDICTS SUCCESS
# =============================================================================
x_b = np.arange(len(categories_b))

# Colors: Gray for Stayers, Blue for Movers
colors_b = [COLORS['gray_bar'], COLORS['flex']]

bars_b = ax2.bar(x_b, success_rates, color=colors_b, edgecolor='none', width=0.55)

# Value labels INSIDE bars
for i, (bar, rate) in enumerate(zip(bars_b, success_rates)):
    y_pos = bar.get_height() - 1.2
    color = 'white' if i == 1 else COLORS['text_dark']
    ax2.text(bar.get_x() + bar.get_width()/2, y_pos,
             f'{rate}%', ha='center', va='top', fontsize=13,
             fontweight='bold', color=color)

# 2.6x annotation - clean box between bars, positioned high
ax2.text(0.5, 19.5, '2.6x', ha='center', va='center', fontsize=16,
         fontweight='bold', color=COLORS['flex'])

# Axis labels
ax2.set_xticks(x_b)
ax2.set_xticklabels(categories_b, fontsize=11)
ax2.set_xlabel('Repositioning (R)', fontsize=12, color=COLORS['text_mid'])
ax2.set_ylabel('Success Rate (%)', fontsize=12, color=COLORS['text_mid'])
ax2.set_ylim(0, 22)

# Title - using abstract language
ax2.set_title('(B) Repositioning Predicts Success', fontsize=13,
              fontweight='bold', color=COLORS['text_dark'], loc='left', pad=12)

# Subtle grid
ax2.yaxis.grid(True, linestyle='-', alpha=0.15, color='gray')
ax2.set_axisbelow(True)

# =============================================================================
# SAMPLE SIZE - Bottom right, subtle
# =============================================================================
fig.text(0.98, 0.02, 'N = 168,011', ha='right', va='bottom',
         fontsize=9, color=COLORS['text_light'], fontstyle='italic')

# =============================================================================
# SAVE TO ALL LOCATIONS
# =============================================================================
plt.tight_layout()

script_dir = Path(__file__).parent.resolve()
img_dir = script_dir.parent / 'img'
overleaf_img = script_dir.parent / 'overleaf_upload' / 'img'
sail_img = script_dir.parent / 'strategic_ambiguity' / 'empirics' / 'src' / 'scripts' / 'paper_generation' / 'papers_v7_sail' / 'img'

img_dir.mkdir(parents=True, exist_ok=True)

output_path = img_dir / 'Ch1_Fig1_two_patterns.png'
fig.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
print(f'Saved: {output_path}')

if overleaf_img.exists():
    fig.savefig(overleaf_img / 'Ch1_Fig1_two_patterns.png', dpi=300,
                bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f'Saved: {overleaf_img / "Ch1_Fig1_two_patterns.png"}')

if sail_img.exists():
    fig.savefig(sail_img / 'Ch1_Fig1_two_patterns.png', dpi=300,
                bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f'Saved: {sail_img / "Ch1_Fig1_two_patterns.png"}')

plt.close()

print("\n" + "=" * 60)
print("Ch1_Fig1: Two Patterns (10X PROFESSIONAL QUALITY)")
print("=" * 60)
print("(A) Funding Suppresses Repositioning")
print("    Q1: 47.1% -> Q4: 29.3%")
print("(B) Repositioning Predicts Success")
print("    Movers outperform Stayers by 2.6x")
print("=" * 60)
