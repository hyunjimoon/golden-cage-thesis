#!/usr/bin/env python3
"""
Create colored DAG figures for thesis:
- Ch1_Fig2_mediation_dag.png: Red (Cage), Blue (Flex), Green (Paradox)
- Ch2_Fig1_sorting_mechanism.png: Red upper commitment cage

READABILITY FIX: Clean rectangular boxes, visible arrows, large fonts
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch
import numpy as np
from pathlib import Path

# Thesis colors
COLORS = {
    'cage': '#DC3545',      # Red - Commitment Cage
    'flex': '#007BFF',      # Blue - Flexibility Flex
    'paradox': '#28A745',   # Green - Funding-Growth Paradox
    'text_dark': '#2D2926',
    'text_mid': '#5C5652',
    'bg_white': '#FFFFFF',
}

# Multiple output directories
SCRIPT_DIR = Path(__file__).parent.resolve()
IMG_DIR = SCRIPT_DIR.parent / 'img'
OVERLEAF_IMG = SCRIPT_DIR.parent / 'overleaf_upload' / 'img'
SAIL_IMG = SCRIPT_DIR.parent / 'strategic_ambiguity' / 'empirics' / 'src' / 'scripts' / 'paper_generation' / 'papers_v7_sail' / 'img'


def save_figure(fig, filename):
    """Save figure to all output directories."""
    IMG_DIR.mkdir(parents=True, exist_ok=True)

    output_path = IMG_DIR / filename
    fig.savefig(output_path, dpi=300, facecolor='white', bbox_inches='tight')
    print(f'✓ Saved: {output_path}')

    if OVERLEAF_IMG.exists():
        fig.savefig(OVERLEAF_IMG / filename, dpi=300, facecolor='white', bbox_inches='tight')
        print(f'✓ Saved: {OVERLEAF_IMG / filename}')

    if SAIL_IMG.exists():
        fig.savefig(SAIL_IMG / filename, dpi=300, facecolor='white', bbox_inches='tight')
        print(f'✓ Saved: {SAIL_IMG / filename}')


def draw_box(ax, x, y, width, height, color, text, fontsize=14):
    """Draw a clean rectangular box with text."""
    rect = Rectangle((x - width/2, y - height/2), width, height,
                     facecolor='white', edgecolor=color, linewidth=3)
    ax.add_patch(rect)
    ax.text(x, y, text, ha='center', va='center',
            fontsize=fontsize, fontweight='bold', color=COLORS['text_dark'])


def draw_arrow(ax, x1, y1, x2, y2, color, dashed=False):
    """Draw a visible arrow between two points."""
    style = 'dashed' if dashed else 'solid'
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='-|>',
                               color=color,
                               lw=3,
                               linestyle=style,
                               mutation_scale=25,
                               shrinkA=5, shrinkB=5))


def create_mediation_dag():
    """Create Ch1_Fig2: Three-panel mediation DAG with colors.

    10X QUALITY: Maximum visibility, no rho values, clean design.
    """

    fig, axes = plt.subplots(1, 3, figsize=(16, 5), facecolor='white')

    # Font sizes - LARGER for visibility
    TITLE_SIZE = 20
    BOX_TEXT_SIZE = 15
    SIGN_SIZE = 36
    CAPTION_SIZE = 13

    # Box dimensions - LARGER
    BOX_W = 3.0
    BOX_H = 1.6

    for ax in axes:
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.axis('off')
        ax.set_aspect('equal')

    # =========================================================================
    # Panel 1: H1 - Commitment Cage (RED)
    # =========================================================================
    ax1 = axes[0]

    # Title with H1 label
    ax1.text(5, 5.5, 'H1: Commitment Cage', fontsize=TITLE_SIZE, fontweight='bold',
             ha='center', color=COLORS['cage'])

    # Boxes - LARGER, BOLDER
    draw_box(ax1, 2.5, 2.8, BOX_W, BOX_H, COLORS['cage'], 'Early\nFunding (E)', BOX_TEXT_SIZE)
    draw_box(ax1, 7.5, 2.8, BOX_W, BOX_H, COLORS['cage'], 'Flexibility\n(F)', BOX_TEXT_SIZE)

    # Arrow - THICKER
    draw_arrow(ax1, 2.5 + BOX_W/2 + 0.15, 2.8, 7.5 - BOX_W/2 - 0.15, 2.8, COLORS['cage'])

    # Minus sign above arrow - LARGER
    ax1.text(5, 4.0, '−', fontsize=SIGN_SIZE, ha='center', va='center',
             fontweight='bold', color=COLORS['cage'])

    # Caption - NO rho, simple message
    ax1.text(5, 0.8, 'More funding → Less flexibility', ha='center', va='center',
             fontsize=CAPTION_SIZE, color=COLORS['text_mid'], fontstyle='italic')

    # =========================================================================
    # Panel 2: H2 - Flexibility Flex (BLUE)
    # =========================================================================
    ax2 = axes[1]

    # Title with H2 label
    ax2.text(5, 5.5, 'H2: Flexibility Flex', fontsize=TITLE_SIZE, fontweight='bold',
             ha='center', color=COLORS['flex'])

    # Boxes
    draw_box(ax2, 2.5, 2.8, BOX_W, BOX_H, COLORS['flex'], 'Flexibility\n(F)', BOX_TEXT_SIZE)
    draw_box(ax2, 7.5, 2.8, BOX_W, BOX_H, COLORS['flex'], 'Growth\n(G)', BOX_TEXT_SIZE)

    # Arrow
    draw_arrow(ax2, 2.5 + BOX_W/2 + 0.15, 2.8, 7.5 - BOX_W/2 - 0.15, 2.8, COLORS['flex'])

    # Plus sign above arrow
    ax2.text(5, 4.0, '+', fontsize=SIGN_SIZE, ha='center', va='center',
             fontweight='bold', color=COLORS['flex'])

    # Caption - NO rho
    ax2.text(5, 0.8, 'More flexibility → More growth', ha='center', va='center',
             fontsize=CAPTION_SIZE, color=COLORS['text_mid'], fontstyle='italic')

    # =========================================================================
    # Panel 3: H3 - Funding-Growth Paradox (GREEN)
    # =========================================================================
    ax3 = axes[2]

    # Title with H3 label
    ax3.text(5, 5.5, 'H3: The Paradox', fontsize=TITLE_SIZE, fontweight='bold',
             ha='center', color=COLORS['paradox'])

    # Formula above - CLEARER
    ax3.text(5, 4.2, '(−) × (+) = −', fontsize=18, ha='center', va='center',
             fontweight='bold', color=COLORS['paradox'])

    # Boxes
    draw_box(ax3, 2.5, 2.8, BOX_W, BOX_H, COLORS['paradox'], 'Early\nFunding (E)', BOX_TEXT_SIZE)
    draw_box(ax3, 7.5, 2.8, BOX_W, BOX_H, COLORS['paradox'], 'Growth\n(G)', BOX_TEXT_SIZE)

    # Dashed arrow
    draw_arrow(ax3, 2.5 + BOX_W/2 + 0.15, 2.8, 7.5 - BOX_W/2 - 0.15, 2.8, COLORS['paradox'], dashed=True)

    # Caption - NO rho
    ax3.text(5, 0.8, 'Net effect: More E → Less G', ha='center', va='center',
             fontsize=CAPTION_SIZE, color=COLORS['text_mid'], fontstyle='italic')

    plt.tight_layout()
    save_figure(fig, 'Ch1_Fig2_mediation_dag.png')
    plt.close()


def create_sorting_mechanism():
    """Create Ch2_Fig1: Sorting mechanism with red commitment cage.

    Clean design with rectangular boxes and visible arrows.
    """

    fig, ax = plt.subplots(figsize=(14, 9), facecolor='white')
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Font sizes
    MAIN_TITLE_SIZE = 18
    BOX_TEXT_SIZE = 11
    SIGN_SIZE = 20
    SECTION_TITLE_SIZE = 13
    SUBTITLE_SIZE = 11
    LEGEND_SIZE = 11

    # Main title (RED)
    ax.text(7, 9.3, 'Commitment Cage', fontsize=MAIN_TITLE_SIZE, fontweight='bold',
            ha='center', color=COLORS['cage'])

    # =========================================================================
    # Upper chain: C → E → Belief Homogeneity → R
    # =========================================================================
    box_y = 7.5
    box_h = 1.2
    box_positions = [
        (1.5, 2.2, 'Commitment\n(C)'),
        (5.0, 2.4, 'Early Funding\n(E)'),
        (8.7, 2.6, 'Belief\nHomogeneity'),
        (12.3, 2.2, 'Repositioning\n(R)'),
    ]

    for (x, w, text) in box_positions:
        rect = Rectangle((x - w/2, box_y - box_h/2), w, box_h,
                         facecolor='white', edgecolor=COLORS['cage'], linewidth=2.5)
        ax.add_patch(rect)
        ax.text(x, box_y, text, ha='center', va='center',
                fontsize=BOX_TEXT_SIZE, fontweight='bold', color=COLORS['text_dark'])

    # Arrows between boxes with signs
    arrow_data = [
        (1.5 + 2.2/2, 5.0 - 2.4/2, '+'),
        (5.0 + 2.4/2, 8.7 - 2.6/2, '+'),
        (8.7 + 2.6/2, 12.3 - 2.2/2, '−'),
    ]

    for (x1, x2, sign) in arrow_data:
        # Arrow
        ax.annotate('', xy=(x2 + 0.1, box_y), xytext=(x1 - 0.1, box_y),
                    arrowprops=dict(arrowstyle='-|>',
                                   color=COLORS['cage'],
                                   lw=2.5,
                                   mutation_scale=20))
        # Sign above arrow
        mid_x = (x1 + x2) / 2
        ax.text(mid_x, box_y + 0.9, sign, fontsize=SIGN_SIZE, ha='center',
                fontweight='bold', color=COLORS['cage'])

    # =========================================================================
    # Lower section: Before/After Funding with sorting
    # =========================================================================

    # Before Funding
    ax.text(3, 5.3, 'Before Funding', fontsize=SECTION_TITLE_SIZE, fontweight='bold', ha='center')
    ax.text(3, 4.85, '(Diverse beliefs)', fontsize=SUBTITLE_SIZE, ha='center', color=COLORS['text_mid'])

    # 3x3 grid of circles (mixed believers/skeptics)
    positions_before = [
        (1.8, 4.0), (3.0, 4.0), (4.2, 4.0),
        (1.8, 3.0), (3.0, 3.0), (4.2, 3.0),
        (1.8, 2.0), (3.0, 2.0), (4.2, 2.0),
    ]
    colors_before = ['dark', 'light', 'dark',
                     'dark', 'light', 'dark',
                     'dark', 'light', 'dark']

    for (x, y), c in zip(positions_before, colors_before):
        color = '#3A3A3A' if c == 'dark' else '#AAAAAA'
        circle = plt.Circle((x, y), 0.38, facecolor=color, edgecolor='white', linewidth=1)
        ax.add_patch(circle)

    # Sorting arrow
    ax.annotate('', xy=(8.2, 3.0), xytext=(5.2, 3.0),
                arrowprops=dict(arrowstyle='-|>',
                               color=COLORS['text_dark'],
                               lw=3,
                               mutation_scale=22))
    ax.text(6.7, 3.7, 'Sorting', fontsize=SECTION_TITLE_SIZE, fontweight='bold', ha='center')
    ax.text(6.7, 2.3, '(Van den Steen)', fontsize=SUBTITLE_SIZE, ha='center', color=COLORS['text_mid'])

    # After Funding
    ax.text(11, 5.3, 'After Funding', fontsize=SECTION_TITLE_SIZE, fontweight='bold', ha='center')
    ax.text(11, 4.85, '(Homogeneous beliefs)', fontsize=SUBTITLE_SIZE, ha='center', color=COLORS['text_mid'])

    # 3x3 grid of circles (all believers)
    positions_after = [
        (9.8, 4.0), (11.0, 4.0), (12.2, 4.0),
        (9.8, 3.0), (11.0, 3.0), (12.2, 3.0),
        (9.8, 2.0), (11.0, 2.0), (12.2, 2.0),
    ]

    for (x, y) in positions_after:
        circle = plt.Circle((x, y), 0.38, facecolor='#3A3A3A', edgecolor='white', linewidth=1)
        ax.add_patch(circle)

    # Skeptics pushed out
    ax.text(13.4, 4.6, 'Out', fontsize=10, ha='center', color=COLORS['text_mid'], fontweight='bold')
    skeptic_out = [(13.4, 3.9), (13.4, 3.0), (13.4, 2.1)]
    for (x, y) in skeptic_out:
        circle = plt.Circle((x, y), 0.32, facecolor='#CCCCCC', edgecolor='white', linewidth=1)
        ax.add_patch(circle)

    # Legend
    legend_y = 0.8
    circle_b = plt.Circle((1.8, legend_y), 0.28, facecolor='#3A3A3A', edgecolor='white', linewidth=1)
    ax.add_patch(circle_b)
    ax.text(2.3, legend_y, 'Believers', fontsize=LEGEND_SIZE, va='center', fontweight='medium')

    circle_s = plt.Circle((4.5, legend_y), 0.28, facecolor='#AAAAAA', edgecolor='white', linewidth=1)
    ax.add_patch(circle_s)
    ax.text(5.0, legend_y, 'Skeptics', fontsize=LEGEND_SIZE, va='center', fontweight='medium')

    plt.tight_layout()
    save_figure(fig, 'Ch2_Fig1_sorting_mechanism.png')
    plt.close()


if __name__ == '__main__':
    print("Creating colored DAG figures...")
    print("=" * 50)
    create_mediation_dag()
    create_sorting_mechanism()
    print("=" * 50)
    print("✓ All DAG figures created!")
