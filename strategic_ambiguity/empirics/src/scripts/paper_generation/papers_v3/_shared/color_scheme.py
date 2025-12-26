"""
Thesis Color Scheme - Central Reference
========================================

NEW COLOR SCHEME (from handwritten notes analysis):
⚫ Stayer = Black/Dark
🟢 Horizontal = Green
🔴 Zoom In = Red
🔵 Zoom Out = Blue

Usage:
    from _shared.color_scheme import COLORS, get_archetype_color

    # In matplotlib:
    ax.scatter(x, y, c=COLORS['zoom_in'])

    # Or by archetype:
    color = get_archetype_color('stayer')
"""

# Primary archetype colors
COLORS = {
    # Archetype colors
    'stayer': '#264653',      # ⚫ Black/Dark - No movement
    'horizontal': '#2A9D8F',  # 🟢 Green - Lateral movement
    'zoom_in': '#E63946',     # 🔴 Red - Focus (D < 0)
    'zoom_out': '#457B9D',    # 🔵 Blue - Expand (D > 0)

    # Semantic colors
    'primary': '#457B9D',     # Blue
    'secondary': '#E63946',   # Red
    'accent': '#F4A261',      # Orange
    'neutral': '#264653',     # Dark
    'success': '#2A9D8F',     # Green

    # For positive/negative effects
    'positive': '#2A9D8F',    # Green
    'negative': '#264653',    # Dark
}

# RGB versions (for matplotlib where needed)
COLORS_RGB = {
    'stayer': (38, 70, 83),
    'horizontal': (42, 157, 143),
    'zoom_in': (230, 57, 70),
    'zoom_out': (69, 123, 157),
}

# Normalized RGB (0-1 scale)
COLORS_RGB_NORM = {
    k: tuple(v/255 for v in rgb)
    for k, rgb in COLORS_RGB.items()
}

def get_archetype_color(archetype: str) -> str:
    """Get hex color for an archetype."""
    return COLORS.get(archetype.lower(), '#264653')

def get_archetype_color_rgb(archetype: str) -> tuple:
    """Get RGB tuple (0-255) for an archetype."""
    return COLORS_RGB.get(archetype.lower(), (38, 70, 83))

def get_archetype_color_rgb_norm(archetype: str) -> tuple:
    """Get normalized RGB tuple (0-1) for an archetype."""
    return COLORS_RGB_NORM.get(archetype.lower(), (0.15, 0.27, 0.33))

# For matplotlib color maps
ARCHETYPE_ORDER = ['stayer', 'horizontal', 'zoom_in', 'zoom_out']
ARCHETYPE_COLORS = [COLORS[a] for a in ARCHETYPE_ORDER]

# Color scheme documentation
COLOR_LEGEND = """
Archetype Color Scheme
======================

| Type | Emoji | Color | Hex | RGB |
|:-----|:-----:|:------|:----|:----|
| Stayer | ⚫ | Black/Dark | #264653 | (38, 70, 83) |
| Horizontal | 🟢 | Green | #2A9D8F | (42, 157, 143) |
| Zoom In | 🔴 | Red | #E63946 | (230, 57, 70) |
| Zoom Out | 🔵 | Blue | #457B9D | (69, 123, 157) |

Semantic Meaning:
- Stayer (⚫): "Stuck" - represents learning trap, inability to move
- Horizontal (🟢): "Lateral" - represents growth through parallel movement
- Zoom In (🔴): "Focus" - represents strategic narrowing
- Zoom Out (🔵): "Expand" - represents strategic broadening
"""

if __name__ == '__main__':
    print(COLOR_LEGEND)
    print("\nHex Codes:")
    for k, v in COLORS.items():
        print(f"  {k}: {v}")
