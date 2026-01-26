#!/usr/bin/env python3
"""
Create Ch3_Fig1: Distributions of E and B0
============================================
Shows distributions of early-stage funding (E) and initial strategic breadth (B0).

Fix: Remove blue mean line from panel A per user request.
"""

import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
from pathlib import Path

# =============================================================================
# COLORS (consistent with thesis)
# =============================================================================
COLORS = {
    'primary': '#2C3E50',
    'histogram': '#95A5A6',
    'median': '#2C3E50',  # Dark line for median only
    'text': '#2C2C2C',
    'annotation_bg': 'white',
}

# =============================================================================
# LOAD DATA
# =============================================================================
script_dir = Path(__file__).parent.resolve()
data_path = script_dir / 'data' / 'processed' / 'thesis_panel_v3.nc'

if not data_path.exists():
    raise FileNotFoundError(f"Data file not found: {data_path}")

ds = xr.open_dataset(data_path)

# Extract variables
E = ds['E'].values  # Early-stage funding
B0 = ds['B_0'].values  # Initial strategic breadth (variable name is B_0)

# Filter valid values
E_valid = E[~np.isnan(E) & (E > 0)]  # Positive funding only
B0_valid = B0[~np.isnan(B0)]

# E is already in millions
print(f"E: N={len(E_valid)}, median=${np.median(E_valid):.1f}M, mean=${np.mean(E_valid):.1f}M")
print(f"B0: N={len(B0_valid)}, mean={np.mean(B0_valid):.1f}, std={np.std(B0_valid):.1f}")

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

fig, axes = plt.subplots(1, 2, figsize=(10, 4), facecolor='white')

# -----------------------------------------------------------------------------
# Panel A: Early Funding Distribution (log scale)
# -----------------------------------------------------------------------------
ax = axes[0]

# Log-transform for histogram bins
E_log = np.log10(E_valid)
bins = np.logspace(np.log10(E_valid.min()), np.log10(E_valid.max()), 50)

ax.hist(E_valid, bins=bins, color=COLORS['histogram'], edgecolor='white', linewidth=0.3, alpha=0.85)
ax.set_xscale('log')

# Median and Mean lines
median_E = np.median(E_valid)
mean_E = np.mean(E_valid)
ax.axvline(median_E, color=COLORS['median'], linestyle='--', linewidth=1.5, alpha=0.8, label='Median')
ax.axvline(mean_E, color=COLORS['median'], linestyle=':', linewidth=1.5, alpha=0.8, label='Mean')

# Annotation box (E is already in millions)
n_E = len(E_valid)
ax.annotate(
    f'N = {n_E:,}\nMedian = ${median_E:.1f}M\nMean = ${mean_E:.1f}M',
    xy=(0.97, 0.97), xycoords='axes fraction',
    ha='right', va='top', fontsize=9,
    bbox=dict(boxstyle='round,pad=0.4', facecolor=COLORS['annotation_bg'],
              edgecolor='#CCCCCC', alpha=0.9)
)

ax.set_xlabel('Early-stage funding, E ($M)', fontsize=10)
ax.set_ylabel('Frequency', fontsize=10)
ax.set_title('A. Early Funding Distribution', fontsize=11, fontweight='bold', loc='left')

# Clean spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# -----------------------------------------------------------------------------
# Panel B: Strategic Breadth Distribution
# -----------------------------------------------------------------------------
ax = axes[1]

bins_B = np.linspace(0, 100, 50)
ax.hist(B0_valid, bins=bins_B, color=COLORS['histogram'], edgecolor='white', linewidth=0.3, alpha=0.85)

# Annotation regions
ax.axvspan(0, 30, alpha=0.05, color='gray')
ax.axvspan(70, 100, alpha=0.05, color='gray')
ax.text(15, ax.get_ylim()[1]*0.4, 'Specific\n(Low B)', ha='center', va='center',
        fontsize=8, color='gray', fontstyle='italic')
ax.text(85, ax.get_ylim()[1]*0.4, 'Vague\n(High B)', ha='center', va='center',
        fontsize=8, color='gray', fontstyle='italic')

# Mean line (dashed)
mean_B0 = np.mean(B0_valid)
std_B0 = np.std(B0_valid)
ax.axvline(mean_B0, color=COLORS['median'], linestyle='--', linewidth=1.5, alpha=0.8)

# Annotation box
n_B = len(B0_valid)
ax.annotate(
    f'N = {n_B:,}\nMean = {mean_B0:.1f}\nSD = {std_B0:.1f}',
    xy=(0.97, 0.97), xycoords='axes fraction',
    ha='right', va='top', fontsize=9,
    bbox=dict(boxstyle='round,pad=0.4', facecolor=COLORS['annotation_bg'],
              edgecolor='#CCCCCC', alpha=0.9)
)

ax.set_xlabel('Initial strategic breadth, B$_0$ (0-100)', fontsize=10)
ax.set_ylabel('Frequency', fontsize=10)
ax.set_title('B. Strategic Breadth Distribution', fontsize=11, fontweight='bold', loc='left')

# Clean spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

# =============================================================================
# SAVE
# =============================================================================
img_dir = script_dir.parent / 'img'
overleaf_img = script_dir.parent / 'overleaf_upload' / 'img'

img_dir.mkdir(parents=True, exist_ok=True)

output_path = img_dir / 'Ch3_Fig1_distributions_E_B0.png'
fig.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
print(f"✓ Saved: {output_path}")

if overleaf_img.exists():
    fig.savefig(overleaf_img / 'Ch3_Fig1_distributions_E_B0.png',
                dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f"✓ Saved: {overleaf_img / 'Ch3_Fig1_distributions_E_B0.png'}")

# Also save to strategic_ambiguity location if exists
sail_img = script_dir.parent / 'strategic_ambiguity' / 'empirics' / 'src' / 'scripts' / 'paper_generation' / 'papers_v7_sail' / 'img'
if sail_img.exists():
    fig.savefig(sail_img / 'Ch3_Fig1_distributions_E_B0.png',
                dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f"✓ Saved: {sail_img / 'Ch3_Fig1_distributions_E_B0.png'}")

plt.close()
print("\nPanel A now shows both median (dashed) and mean (dotted blue) lines")
