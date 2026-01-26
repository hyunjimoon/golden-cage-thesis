#!/usr/bin/env python3
"""
Create Ch3_Fig2: R and G Distributions
======================================
Professional visualization following minimal complexity principle.

Improvements applied:
- Panel A: Inset for R>0 detail (main histogram dominated by R=0)
- Panel B: Horizontal bar for better proportion visibility
- Consistent typography and color scheme
- Unified axis labels and statistics box style
"""

import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
from pathlib import Path

# =============================================================================
# COLOR SCHEME (thesis standard)
# =============================================================================
COLORS = {
    'primary': '#2C3E50',      # Dark blue-gray
    'flex': '#007BFF',         # Blue - Flexibility (R)
    'paradox': '#28A745',      # Green - Growth (G)
    'gray': '#95A5A6',         # Medium gray
    'light_gray': '#ECF0F1',   # Light gray
    'success': '#28A745',      # Green for G=1
    'fail': '#6C757D',         # Gray for G=0
}

# =============================================================================
# LOAD DATA
# =============================================================================
script_dir = Path(__file__).parent.resolve()
data_path = script_dir / 'data' / 'processed' / 'thesis_panel_v3.nc'

ds = xr.open_dataset(data_path)
R = ds['R'].values
G = ds['G'].values

R_valid = R[~np.isnan(R)]
G_valid = G[~np.isnan(G)]

N = len(R_valid)
n_stayers = (R_valid == 0).sum()
n_movers = (R_valid > 0).sum()
pct_stayers = n_stayers / N * 100
pct_movers = n_movers / N * 100

n_success = G_valid.sum()
n_fail = len(G_valid) - n_success
pct_success = n_success / len(G_valid) * 100
pct_fail = n_fail / len(G_valid) * 100

print(f"N = {N:,}")
print(f"Stayers (R=0): {n_stayers:,} ({pct_stayers:.1f}%)")
print(f"Movers (R>0): {n_movers:,} ({pct_movers:.1f}%)")
print(f"Success (G=1): {int(n_success):,} ({pct_success:.1f}%)")

# =============================================================================
# FIGURE SETUP
# =============================================================================
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica Neue', 'Helvetica', 'Arial'],
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.labelsize': 11,
})

fig, axes = plt.subplots(1, 2, figsize=(12, 5), facecolor='white')

# =============================================================================
# PANEL A: R Distribution with Inset
# =============================================================================
ax1 = axes[0]

# Main histogram (all R)
bins_R = np.arange(0, 65, 2)
n_hist, bins_edges, patches = ax1.hist(R_valid, bins=bins_R, color=COLORS['gray'],
                                        alpha=0.75, edgecolor='white', linewidth=0.3)

# Color R=0 bar differently
patches[0].set_facecolor(COLORS['gray'])
patches[0].set_alpha(0.9)

# Color R>0 bars in blue
for patch in patches[1:]:
    patch.set_facecolor(COLORS['flex'])
    patch.set_alpha(0.7)

# Vertical line at R=1 (Mover threshold)
ax1.axvline(1, color=COLORS['flex'], linestyle='-', linewidth=2, alpha=0.9)

# Styling
ax1.set_xlabel('Repositioning Magnitude, R', fontsize=11)
ax1.set_ylabel('Number of Ventures', fontsize=11)
ax1.set_title('A. Repositioning Distribution', fontsize=12, fontweight='bold', loc='left')
ax1.set_xlim(-1, 65)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Inset for R > 0 detail (positioned in upper right, away from R=0 spike)
ax_inset = ax1.inset_axes([0.50, 0.40, 0.48, 0.55])  # [x, y, width, height]
R_movers = R_valid[R_valid > 0]
bins_inset = np.arange(0, 40, 1)
ax_inset.hist(R_movers[R_movers < 40], bins=bins_inset, color=COLORS['flex'],
              alpha=0.7, edgecolor='white', linewidth=0.2)
ax_inset.axvline(1, color=COLORS['flex'], linestyle='-', linewidth=1.5, alpha=0.9)
ax_inset.set_xlabel('R (Movers only)', fontsize=8)
ax_inset.set_ylabel('Count', fontsize=8)
ax_inset.tick_params(labelsize=7)
ax_inset.spines['top'].set_visible(False)
ax_inset.spines['right'].set_visible(False)
ax_inset.set_facecolor('#FAFAFA')

# Stats in inset title area
ax_inset.set_title(f'Movers (R>0): {pct_movers:.1f}%', fontsize=9, fontweight='bold', color=COLORS['flex'])

# =============================================================================
# PANEL B: Growth Outcome (Horizontal Stacked Bar)
# =============================================================================
ax2 = axes[1]

# Horizontal stacked bar (better for proportion comparison)
bar_height = 0.5
y_pos = 0

# Draw stacked bar
ax2.barh(y_pos, pct_fail, height=bar_height, color=COLORS['fail'],
         edgecolor='white', linewidth=1, label=f'G=0 (No Later Stage)')
ax2.barh(y_pos, pct_success, height=bar_height, left=pct_fail,
         color=COLORS['success'], edgecolor='white', linewidth=1, label=f'G=1 (Later Stage)')

# Labels on bars
ax2.text(pct_fail/2, y_pos, f'{pct_fail:.1f}%\n(n={int(n_fail):,})',
         ha='center', va='center', fontsize=11, fontweight='bold', color='white')
ax2.text(pct_fail + pct_success/2, y_pos, f'{pct_success:.1f}%\n(n={int(n_success):,})',
         ha='center', va='center', fontsize=11, fontweight='bold', color='white')

# Base rate annotation
ax2.annotate(f'Base Success Rate: {pct_success:.1f}%',
             xy=(0.97, 0.85), xycoords='axes fraction',
             ha='right', va='top',
             fontsize=11, fontweight='bold', color=COLORS['success'],
             bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                      edgecolor=COLORS['success'], linewidth=1.5, alpha=0.95))

# Styling
ax2.set_xlim(0, 100)
ax2.set_ylim(-0.5, 0.5)
ax2.set_xlabel('Percentage of Ventures (%)', fontsize=11)
ax2.set_yticks([])
ax2.set_title('B. Growth Outcome', fontsize=12, fontweight='bold', loc='left')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)

# Legend
ax2.legend(loc='lower right', framealpha=0.95, fontsize=10)

plt.tight_layout()

# =============================================================================
# SAVE
# =============================================================================
img_dir = script_dir.parent / 'img'
overleaf_img = script_dir.parent / 'overleaf_upload' / 'img'
sail_img = script_dir.parent / 'strategic_ambiguity' / 'empirics' / 'src' / 'scripts' / 'paper_generation' / 'papers_v7_sail' / 'img'

img_dir.mkdir(parents=True, exist_ok=True)

output_path = img_dir / 'Ch3_Fig2_distributions_R_G.png'
fig.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
print(f"✓ Saved: {output_path}")

if overleaf_img.exists():
    fig.savefig(overleaf_img / 'Ch3_Fig2_distributions_R_G.png',
                dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f"✓ Saved: {overleaf_img / 'Ch3_Fig2_distributions_R_G.png'}")

if sail_img.exists():
    fig.savefig(sail_img / 'Ch3_Fig2_distributions_R_G.png',
                dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f"✓ Saved: {sail_img / 'Ch3_Fig2_distributions_R_G.png'}")

plt.close()
print("\n✓ Ch3_Fig2 redesigned with minimal complexity principle:")
print("  - Panel A: Inset shows R>0 detail")
print("  - Panel B: Horizontal bar for clear proportion")
print("  - Unified color scheme (blue=R, green=G)")
