#!/usr/bin/env python3
"""
THESIS FIGURE STYLE GUIDE
=========================
Unified color palette and style constants for all thesis figures.
Based on consolidated critiques from 10 design agents.

Usage:
    from thesis_figure_style import COLORS, STYLE, apply_style
"""

import matplotlib.pyplot as plt
import matplotlib as mpl

# =============================================================================
# THESIS COLOR PALETTE (Maryland Flag + Semantic Mapping)
# =============================================================================

COLORS = {
    # Semantic colors (from thesis LaTeX definitions)
    'paradox': '#28A745',      # Green - Funding-Growth Paradox
    'cage': '#DC3545',         # Red - Commitment Cage
    'flex': '#007BFF',         # Blue - Flexibility Flex

    # Neutral palette
    'text_dark': '#2D2926',    # Primary text
    'text_mid': '#5C5652',     # Secondary text
    'text_light': '#8A847D',   # Tertiary text
    'line_dark': '#3D3835',    # Dark lines
    'line_light': '#D4CFC7',   # Light lines/borders

    # Background
    'bg_white': '#FFFFFF',     # Standard white
    'bg_warm': '#FAF8F5',      # Warm off-white (for Ch5_Fig2)
    'bg_panel': '#F5F2ED',     # Panel background

    # Bar chart colors (grayscale with semantic accents)
    'bar_primary': '#4A4A4A',  # Primary bars
    'bar_secondary': '#7A7A7A', # Secondary bars
    'bar_tertiary': '#AAAAAA',  # Tertiary bars
    'bar_highlight': '#28A745', # Highlighted bar (paradox green)

    # Quantum exception (positive correlation)
    'quantum': '#28A745',      # Same as paradox green
}

# =============================================================================
# TYPOGRAPHY STANDARDS
# =============================================================================

STYLE = {
    # Font sizes (in points)
    'title_size': 14,
    'subtitle_size': 12,
    'axis_label_size': 11,
    'tick_label_size': 10,
    'annotation_size': 9,
    'legend_size': 9,

    # Font weights
    'title_weight': 'bold',
    'label_weight': 'normal',

    # Line widths
    'axis_linewidth': 0.8,
    'bar_linewidth': 0.5,
    'reference_linewidth': 1.5,

    # Figure dimensions
    'single_panel_width': 6,
    'single_panel_height': 4,
    'two_panel_width': 10,
    'two_panel_height': 4,
    'three_panel_width': 14,
    'three_panel_height': 5,

    # DPI
    'dpi': 300,
}

# =============================================================================
# MATPLOTLIB RC PARAMS
# =============================================================================

def apply_style():
    """Apply consistent style to all matplotlib figures."""
    plt.rcParams.update({
        # Font
        'font.family': 'sans-serif',
        'font.sans-serif': ['Helvetica Neue', 'Arial', 'DejaVu Sans'],
        'font.size': STYLE['tick_label_size'],

        # Axes
        'axes.titlesize': STYLE['title_size'],
        'axes.titleweight': STYLE['title_weight'],
        'axes.labelsize': STYLE['axis_label_size'],
        'axes.linewidth': STYLE['axis_linewidth'],
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.edgecolor': COLORS['line_dark'],
        'axes.labelcolor': COLORS['text_mid'],

        # Ticks
        'xtick.labelsize': STYLE['tick_label_size'],
        'ytick.labelsize': STYLE['tick_label_size'],
        'xtick.color': COLORS['text_light'],
        'ytick.color': COLORS['text_light'],

        # Legend
        'legend.fontsize': STYLE['legend_size'],
        'legend.frameon': False,

        # Figure
        'figure.dpi': STYLE['dpi'],
        'figure.facecolor': COLORS['bg_white'],
        'savefig.dpi': STYLE['dpi'],
        'savefig.facecolor': COLORS['bg_white'],
        'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.1,
    })

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_bar_colors(n_bars, highlight_index=None):
    """
    Get consistent bar colors for a bar chart.

    Args:
        n_bars: Number of bars
        highlight_index: Index of bar to highlight (e.g., for paradox Q4)

    Returns:
        List of colors
    """
    colors = [COLORS['bar_primary']] * n_bars
    if highlight_index is not None:
        colors[highlight_index] = COLORS['cage']  # Red for paradox/cage
    return colors


def format_large_number(n):
    """Format large numbers with K/M suffix."""
    if n >= 1_000_000:
        return f'{n/1_000_000:.1f}M'
    elif n >= 1_000:
        return f'{n/1_000:.0f}K'
    else:
        return str(n)


def add_panel_label(ax, label, loc='upper left'):
    """Add Nature/Science style panel label (A, B, C)."""
    if loc == 'upper left':
        x, y = -0.12, 1.05
    elif loc == 'upper right':
        x, y = 1.02, 1.05
    else:
        x, y = -0.12, 1.05

    ax.text(x, y, label, transform=ax.transAxes,
            fontsize=STYLE['subtitle_size'], fontweight='bold',
            color=COLORS['text_dark'], va='bottom', ha='left')


# =============================================================================
# PRINT SUMMARY
# =============================================================================

if __name__ == '__main__':
    print("THESIS FIGURE STYLE GUIDE")
    print("=" * 50)
    print("\nSEMANTIC COLORS:")
    print(f"  Paradox (Green): {COLORS['paradox']}")
    print(f"  Cage (Red):      {COLORS['cage']}")
    print(f"  Flex (Blue):     {COLORS['flex']}")
    print("\nTYPOGRAPHY:")
    print(f"  Title:      {STYLE['title_size']}pt {STYLE['title_weight']}")
    print(f"  Axis label: {STYLE['axis_label_size']}pt")
    print(f"  Tick label: {STYLE['tick_label_size']}pt")
    print(f"  Annotation: {STYLE['annotation_size']}pt")
    print("\nUsage: from thesis_figure_style import COLORS, STYLE, apply_style")
