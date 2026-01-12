#!/usr/bin/env python3
"""
Generate Fig-E (Anatomy of Growth) with unified thesis style.
Matches: Fig-I, Fig-ARG, Fig-CFR1, Fig-P1 styling.

Style: White background, grayscale, minimal, clean
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path

# Paths
SCRIPT_DIR = Path(__file__).parent.resolve()
OUTPUT_DIR = SCRIPT_DIR / 'images'

# Unified thesis style
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'axes.edgecolor': '#333333',
    'axes.linewidth': 0.8,
    'axes.grid': False,
})

# Grayscale palette (matching other thesis figures)
GRAY_DARK = '#4a4a4a'
GRAY_MID = '#808080'
GRAY_LIGHT = '#c0c0c0'
GRAY_FILL = '#e8e8e8'
GRAY_EDGE = '#333333'


def create_anatomy_of_growth():
    """
    Generate 'The Anatomy of Growth' figure.
    Three growth types:
    - TYPE A: STUNTED (Golden Cage) - Ops only, narrow
    - TYPE B: HOLLOW (Mirage) - Market only, wide but thin
    - TYPE C: PARALLEL (Engine) - Market × Ops, synchronized
    """

    fig, axes = plt.subplots(1, 3, figsize=(14, 6))
    fig.suptitle('The Anatomy of Growth', fontsize=18, fontweight='bold',
                 color=GRAY_DARK, y=0.98)

    # Common settings
    box_height_max = 0.8
    box_width_max = 0.8

    # =========================================
    # TYPE A: STUNTED Growth (Golden Cage)
    # =========================================
    ax = axes[0]
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    # Tall, narrow rectangle (Ops Only)
    rect_a = patches.FancyBboxPatch(
        (0.35, 0.15), 0.15, 0.7,
        boxstyle="round,pad=0.02",
        facecolor=GRAY_FILL,
        edgecolor=GRAY_EDGE,
        linewidth=2.5
    )
    ax.add_patch(rect_a)

    # Label inside
    ax.text(0.425, 0.5, 'Ops\nOnly', ha='center', va='center',
            fontsize=11, color=GRAY_DARK, rotation=90, fontweight='medium')

    # Type label
    ax.text(0.5, 0.95, 'TYPE A: STUNTED Growth', ha='center', va='top',
            fontsize=13, fontweight='bold', color=GRAY_DARK)
    ax.text(0.5, 0.88, '(The Golden Cage)', ha='center', va='top',
            fontsize=11, style='italic', color=GRAY_MID)

    # Bottom labels
    ax.text(0.5, 0.08, 'High Friction', ha='center', va='top',
            fontsize=10, color=GRAY_MID)
    ax.text(0.5, 0.02, 'Low Market', ha='center', va='top',
            fontsize=10, color=GRAY_MID)

    # =========================================
    # VS separator
    # =========================================
    # Add "vs" between first and second
    fig.text(0.355, 0.5, 'vs', ha='center', va='center',
             fontsize=14, color=GRAY_LIGHT, fontweight='bold')

    # =========================================
    # TYPE B: HOLLOW Growth (Mirage)
    # =========================================
    ax = axes[1]
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    # Wide, short rectangle (Promise Only)
    rect_b = patches.FancyBboxPatch(
        (0.1, 0.4), 0.65, 0.2,
        boxstyle="round,pad=0.02",
        facecolor=GRAY_FILL,
        edgecolor=GRAY_EDGE,
        linewidth=2.5
    )
    ax.add_patch(rect_b)

    # Label inside
    ax.text(0.425, 0.5, 'Promise Only', ha='center', va='center',
            fontsize=11, color=GRAY_DARK, fontweight='medium')

    # Type label
    ax.text(0.5, 0.95, 'TYPE B: HOLLOW Growth', ha='center', va='top',
            fontsize=13, fontweight='bold', color=GRAY_DARK)
    ax.text(0.5, 0.88, '(The Mirage)', ha='center', va='top',
            fontsize=11, style='italic', color=GRAY_MID)

    # Bottom labels
    ax.text(0.5, 0.08, 'High Market', ha='center', va='top',
            fontsize=10, color=GRAY_MID)
    ax.text(0.5, 0.02, 'Low Capability', ha='center', va='top',
            fontsize=10, color=GRAY_MID)

    # =========================================
    # VS separator
    # =========================================
    fig.text(0.645, 0.5, 'vs', ha='center', va='center',
             fontsize=14, color=GRAY_LIGHT, fontweight='bold')

    # =========================================
    # TYPE C: PARALLEL Growth (Engine)
    # =========================================
    ax = axes[2]
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    # Large filled square (Market × Ops)
    rect_c = patches.FancyBboxPatch(
        (0.15, 0.2), 0.55, 0.55,
        boxstyle="round,pad=0.02",
        facecolor=GRAY_MID,  # Darker fill to show "filled area"
        edgecolor=GRAY_EDGE,
        linewidth=3
    )
    ax.add_patch(rect_c)

    # Label inside (white text for contrast)
    ax.text(0.425, 0.475, 'Market × Ops', ha='center', va='center',
            fontsize=13, color='white', fontweight='bold')

    # Type label
    ax.text(0.5, 0.95, 'TYPE C: PARALLEL Growth', ha='center', va='top',
            fontsize=13, fontweight='bold', color=GRAY_DARK)
    ax.text(0.5, 0.88, '(The Engine)', ha='center', va='top',
            fontsize=11, style='italic', color=GRAY_MID)

    # Bottom labels
    ax.text(0.5, 0.08, 'Synchronized', ha='center', va='top',
            fontsize=10, color=GRAY_MID)
    ax.text(0.5, 0.02, 'Expansion', ha='center', va='top',
            fontsize=10, color=GRAY_MID)

    # =========================================
    # Bottom insight
    # =========================================
    fig.text(0.5, 0.01,
             'Growth = Market × Ops  |  Only filled area represents true value',
             ha='center', va='bottom', fontsize=11, style='italic', color=GRAY_DARK)

    plt.tight_layout(rect=[0, 0.05, 1, 0.93])

    return fig


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / 'Fig-E_anatomy_of_growth.png'

    print("Generating Fig-E (Anatomy of Growth) - Unified Style...")
    fig = create_anatomy_of_growth()

    fig.savefig(output_path, dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"Saved: {output_path}")

    # Also save as PDF for high quality
    pdf_path = OUTPUT_DIR / 'Fig-E_anatomy_of_growth.pdf'
    fig.savefig(pdf_path, format='pdf', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"Saved: {pdf_path}")

    plt.close(fig)

    print(f"\n✅ Complete!")
    print(f"   Output: {output_path}")


if __name__ == '__main__':
    main()
