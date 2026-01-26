#!/usr/bin/env python3
"""
Create AppC_Fig1: Bimodal Distribution Analysis
===============================================
Professional visualization with improved readability:
- Panel A: B₀ distribution showing bimodal pattern
- Panel B: R distribution with threshold lines

Design fixes:
- Labels positioned outside histogram bars (no overlap)
- Clean legend placement
- Consistent thesis color scheme
"""

import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
from pathlib import Path

# =============================================================================
# THESIS COLOR SCHEME
# =============================================================================
COLORS = {
    'cage': '#DC3545',      # Red - Commitment Cage
    'flex': '#007BFF',      # Blue - Flexibility Flex
    'paradox': '#28A745',   # Green - Paradox
    'primary': '#2C3E50',   # Dark gray
    'gray': '#95A5A6',      # Medium gray
    'light_gray': '#ECF0F1',
    'orange': '#F39C12',    # Orange for thresholds
}

# =============================================================================
# LOAD DATA
# =============================================================================
script_dir = Path(__file__).parent.resolve()
data_path = script_dir / 'data' / 'processed' / 'thesis_panel_v3.nc'

ds = xr.open_dataset(data_path)
B0 = ds['B_0'].values
R = ds['R'].values

B0_valid = B0[~np.isnan(B0)]
R_valid = R[~np.isnan(R)]

print(f"B₀: N={len(B0_valid):,}, range=[{B0_valid.min():.1f}, {B0_valid.max():.1f}]")
print(f"R:  N={len(R_valid):,}, range=[{R_valid.min():.1f}, {R_valid.max():.1f}]")

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
# PANEL A: Bimodal B₀ Distribution
# =============================================================================
ax1 = axes[0]

# Histogram - show full distribution with subtle coloring
bins_B0 = np.arange(0, 95, 2.5)  # Finer bins to show bimodal pattern

# Simple gray histogram - no coloring (B₀ not directly related to R/flexibility)
n, bins_edges, patches = ax1.hist(B0_valid, bins=bins_B0, color=COLORS['gray'],
                                   alpha=0.7, edgecolor='white', linewidth=0.3)

# Statistics annotation
median_B0 = np.median(B0_valid)
mean_B0 = np.mean(B0_valid)

ax1.axvline(median_B0, color=COLORS['primary'], linestyle='--', linewidth=1.5, alpha=0.8, label=f'Median = {median_B0:.1f}')
ax1.axvline(mean_B0, color=COLORS['primary'], linestyle=':', linewidth=1.5, alpha=0.8, label=f'Mean = {mean_B0:.1f}')

# Stats box
ax1.annotate(f'N = {len(B0_valid):,}\nMedian = {median_B0:.1f}\nMean = {mean_B0:.1f}',
             xy=(0.97, 0.97), xycoords='axes fraction',
             ha='right', va='top',
             fontsize=10, fontweight='medium',
             bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                      edgecolor=COLORS['primary'], linewidth=1, alpha=0.95))

ax1.legend(loc='upper left', framealpha=0.95, fontsize=9)

# Styling
ax1.set_xlabel('Initial Strategic Breadth, B₀', fontsize=11)
ax1.set_ylabel('Frequency', fontsize=11)
ax1.set_title('A. Bimodal B₀ Distribution', fontsize=12, fontweight='bold', loc='left')
ax1.set_xlim(0, 90)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# =============================================================================
# PANEL B: R Distribution with Thresholds
# =============================================================================
ax2 = axes[1]

# Exclude R=0 (Stayers) to show Mover distribution more clearly
R_movers = R_valid[R_valid > 0]

# Histogram for R > 0
bins_R = np.linspace(0, 35, 40)
ax2.hist(R_movers[R_movers <= 35], bins=bins_R, color=COLORS['gray'],
         alpha=0.75, edgecolor='white', linewidth=0.3)

# Key thresholds - all in blue with different intensities
mover_threshold = 1  # R > 1 defines Mover in thesis

# Threshold lines - blue family with varying opacity/saturation
# R=1: darkest blue (full opacity)
# R=5: medium blue
# R=10: lighter blue
ax2.axvline(mover_threshold, color=COLORS['flex'], linestyle='-',
            linewidth=2.5, alpha=1.0, label='R = 1 (Mover threshold)')
ax2.axvline(5, color=COLORS['flex'], linestyle='--',
            linewidth=2, alpha=0.6, label='R = 5')
ax2.axvline(10, color=COLORS['flex'], linestyle=':',
            linewidth=2.5, alpha=0.4, label='R = 10')

# Statistics annotation
n_stayers = (R_valid == 0).sum()
n_movers = (R_valid > 0).sum()
pct_stayers = n_stayers / len(R_valid) * 100
pct_movers = n_movers / len(R_valid) * 100

# Stats box in upper left
stats_text = f'Stayers (R=0): {pct_stayers:.1f}%\nMovers (R>0): {pct_movers:.1f}%'
ax2.annotate(stats_text,
             xy=(0.97, 0.97), xycoords='axes fraction',
             ha='right', va='top',
             fontsize=10, fontweight='medium',
             bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                      edgecolor=COLORS['primary'], linewidth=1, alpha=0.95))

# Legend (compact, positioned to avoid overlap)
ax2.legend(loc='center right', framealpha=0.95, fontsize=9,
           frameon=True, edgecolor='gray')

# Styling
ax2.set_xlabel('Repositioning Magnitude, R (Movers only)', fontsize=11)
ax2.set_ylabel('Frequency', fontsize=11)
ax2.set_title('B. R Distribution (R > 0)', fontsize=12, fontweight='bold', loc='left')
ax2.set_xlim(0, 35)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()

# =============================================================================
# SAVE
# =============================================================================
img_dir = script_dir.parent / 'img'
overleaf_img = script_dir.parent / 'overleaf_upload' / 'img'
sail_img = script_dir.parent / 'strategic_ambiguity' / 'empirics' / 'src' / 'scripts' / 'paper_generation' / 'papers_v7_sail' / 'img'

img_dir.mkdir(parents=True, exist_ok=True)

output_path = img_dir / 'AppC_Fig1_bimodal_distribution.png'
fig.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
print(f"✓ Saved: {output_path}")

if overleaf_img.exists():
    fig.savefig(overleaf_img / 'AppC_Fig1_bimodal_distribution.png',
                dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f"✓ Saved: {overleaf_img / 'AppC_Fig1_bimodal_distribution.png'}")

if sail_img.exists():
    fig.savefig(sail_img / 'AppC_Fig1_bimodal_distribution.png',
                dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f"✓ Saved: {sail_img / 'AppC_Fig1_bimodal_distribution.png'}")

plt.close()
print("\n✓ Figure redesigned with improved readability:")
print("  - Labels in white boxes, positioned above histograms")
print("  - Clean legend for thresholds")
print("  - Consistent thesis color scheme")
