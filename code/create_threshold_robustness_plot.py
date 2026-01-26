#!/usr/bin/env python3
"""
Create AppC_Fig2: Threshold Robustness Test
============================================
Shows mover advantage is robust across different R thresholds.

Fixes:
- All bars should be the same color (consistent)
- Median threshold should be in logical order (after R > 0, before R > 1)
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# =============================================================================
# COLORS (consistent with thesis)
# =============================================================================
COLORS = {
    'primary': '#2C3E50',      # Dark blue-gray
    'bar': '#4A90D9',          # Signature Blue - matching Ch4_Fig1_G_by_R
    'highlight': '#E74C3C',    # Red for emphasis
    'gray': '#95A5A6',
    'text': '#2C2C2C',
}

# =============================================================================
# DATA (from thesis analysis)
# =============================================================================
# Threshold data - minimal set for key insight
# R > 10, 15, 20 removed (same values, no new information)
thresholds = [
    {'label': 'R > 0', 'advantage': 2.60, 'movers_pct': 40},
    {'label': 'R > 0.5\n(median)', 'advantage': 1.81, 'movers_pct': 20},
    {'label': 'R > 1', 'advantage': 1.72, 'movers_pct': 14},
    {'label': 'R > 5', 'advantage': 1.63, 'movers_pct': 9},
]

# =============================================================================
# FIGURE
# =============================================================================
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica Neue', 'Helvetica', 'Arial'],
    'font.size': 9,
    'axes.titlesize': 11,
    'axes.labelsize': 10,
})

fig, ax = plt.subplots(figsize=(8, 5), facecolor='white')

# Extract data
labels = [t['label'] for t in thresholds]
advantages = [t['advantage'] for t in thresholds]
movers_pcts = [t['movers_pct'] for t in thresholds]

x = np.arange(len(labels))
width = 0.65

# All bars same color (blue)
bars = ax.bar(x, advantages, width, color=COLORS['bar'], edgecolor='none', alpha=0.85)

# Add value labels on top
for bar, adv in zip(bars, advantages):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
            f'{adv:.2f}×', ha='center', va='bottom', fontsize=10, fontweight='bold',
            color=COLORS['text'])

# Add mover percentage labels inside bars
for bar, pct in zip(bars, movers_pcts):
    ax.text(bar.get_x() + bar.get_width()/2, 0.3,
            f'({pct}%\nMovers)', ha='center', va='bottom', fontsize=8,
            color='white', alpha=0.9)

# Reference line at 1.0 (no advantage)
ax.axhline(y=1.0, color=COLORS['gray'], linestyle='--', linewidth=1.5, alpha=0.7)
ax.text(len(labels) - 0.5, 1.05, 'No advantage', ha='right', va='bottom',
        fontsize=8, color=COLORS['gray'], fontstyle='italic')

# Styling
ax.set_ylabel('Mover Advantage (×)', fontsize=11)
ax.set_xlabel('Repositioning Threshold', fontsize=11)
ax.set_title('Robustness Test: Mover Advantage Across Different Thresholds',
             fontsize=12, fontweight='bold', pad=15)

ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=9)
ax.set_ylim(0, 3.2)
ax.set_xlim(-0.5, len(labels) - 0.5)

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Grid
ax.grid(True, axis='y', alpha=0.2, linewidth=0.5)
ax.set_axisbelow(True)

plt.tight_layout()

# =============================================================================
# SAVE
# =============================================================================
script_dir = Path(__file__).parent.resolve()
img_dir = script_dir.parent / 'img'
overleaf_img = script_dir.parent / 'overleaf_upload' / 'img'

img_dir.mkdir(parents=True, exist_ok=True)

output_path = img_dir / 'AppC_Fig2_threshold_robustness.png'
fig.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
print(f"✓ Saved: {output_path}")

if overleaf_img.exists():
    fig.savefig(overleaf_img / 'AppC_Fig2_threshold_robustness.png',
                dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f"✓ Saved: {overleaf_img / 'AppC_Fig2_threshold_robustness.png'}")

plt.close()
print("\nFixes applied:")
print("  • All bars now same color (blue)")
print("  • Median threshold in logical position (after R > 0)")
