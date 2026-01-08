"""
C Module Prescription Figure: Commit to Move
Key Message: Movement is the prescription - direction depends on your trap
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Set up figure
fig, ax = plt.subplots(1, 1, figsize=(12, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

# Title
ax.text(5, 7.5, 'COMMIT TO MOVE', fontsize=24, fontweight='bold',
        ha='center', va='center', color='#1a1a2e')
ax.text(5, 7.0, 'Prescription by Archetype', fontsize=14,
        ha='center', va='center', color='#666666', style='italic')

# Three columns for three archetypes
col_positions = [1.7, 5, 8.3]
col_width = 2.8

# Colors
colors = {
    'stayer': '#e74c3c',      # Red - trapped
    'zoom_in': '#3498db',     # Blue - focus
    'zoom_out': '#2ecc71'     # Green - expand
}

# Archetype data
archetypes = [
    {
        'name': 'STAYER',
        'trap': 'Trapped (no movement)',
        'symptom': 'High E, Low M',
        'prescription': 'FORCE MOVEMENT',
        'actions': [
            'Set pivot deadline',
            'Hire "doubters"',
            'Kill zombie projects'
        ],
        'color': colors['stayer']
    },
    {
        'name': 'ZOOM IN',
        'trap': 'High V to Low V',
        'symptom': 'Broad to Focused',
        'prescription': 'COMMIT TO FOCUS',
        'actions': [
            'Narrow scope early',
            'Depth > breadth',
            'Build moat in niche'
        ],
        'color': colors['zoom_in']
    },
    {
        'name': 'ZOOM OUT',
        'trap': 'Low V to High V',
        'symptom': 'Focused to Broad',
        'prescription': 'COMMIT TO EXPAND',
        'actions': [
            'Platform from product',
            'Adjacent markets',
            'Build ecosystem'
        ],
        'color': colors['zoom_out']
    }
]

# Draw columns
for i, (pos, arch) in enumerate(zip(col_positions, archetypes)):
    # Box
    box = mpatches.FancyBboxPatch(
        (pos - col_width/2, 1.2), col_width, 5.2,
        boxstyle="round,pad=0.05,rounding_size=0.2",
        facecolor='white', edgecolor=arch['color'], linewidth=3
    )
    ax.add_patch(box)

    # Header (circle marker instead of emoji)
    ax.plot(pos - 0.8, 6.0, 'o', markersize=15, color=arch['color'])
    ax.text(pos + 0.1, 6.0, arch['name'], fontsize=16, fontweight='bold',
            ha='center', va='center', color=arch['color'])

    # Trap description
    ax.text(pos, 5.4, arch['trap'], fontsize=11, ha='center', va='center', color='#444')
    ax.text(pos, 5.0, arch['symptom'], fontsize=10, ha='center', va='center',
            color='#888', style='italic')

    # Divider
    ax.plot([pos - col_width/2 + 0.2, pos + col_width/2 - 0.2], [4.6, 4.6],
            color='#ddd', linewidth=1)

    # Prescription
    ax.text(pos, 4.2, arch['prescription'], fontsize=13, fontweight='bold',
            ha='center', va='center', color=arch['color'])

    # Actions (with bullet points)
    for j, action in enumerate(arch['actions']):
        ax.text(pos, 3.5 - j*0.5, f"• {action}", fontsize=10, ha='center', va='center', color='#333')

# Bottom equation box
bottom_box = mpatches.FancyBboxPatch(
    (1.5, 0.2), 7, 0.8,
    boxstyle="round,pad=0.05,rounding_size=0.2",
    facecolor='#f8f9fa', edgecolor='#1a1a2e', linewidth=2
)
ax.add_patch(bottom_box)
ax.text(5, 0.6, 'dG/dE < 0   =>   Movement is the cure, not more funding',
        fontsize=12, ha='center', va='center', color='#1a1a2e',
        style='italic', fontweight='bold')

plt.tight_layout()
plt.savefig('/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/papers_v4/figures/C_fig1_prescription.png',
            dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

print("C_fig1_prescription.png created successfully!")
