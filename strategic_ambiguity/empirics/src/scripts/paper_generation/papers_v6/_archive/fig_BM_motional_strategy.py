import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Set style
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(12, 8), facecolor='#0a0e14')
ax.set_facecolor('#0a0e14')
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis('off')

# Colors
C_RED = '#ff6b6b'
C_YELLOW = '#ffd43b'
C_GREEN = '#69db7c'
C_BLUE = '#4dabf7'
C_GRAY = '#7d8590'
C_WHITE = '#e6edf3'

# Title
ax.text(6, 7.6, 'MOTIONAL $4B STRATEGY MAP', ha='center', va='center',
        fontsize=16, fontweight='bold', color=C_WHITE)
ax.text(6, 7.2, 'Q×Tools Framework Application', ha='center', va='center',
        fontsize=10, color=C_GRAY)

# ============ LEFT: CURRENT STATE ============
# Lock-in/Lock-out box
rect = FancyBboxPatch((0.3, 4.5), 2.8, 2.2, boxstyle="round,pad=0.05",
                       facecolor='#1a1a2e', edgecolor=C_RED, linewidth=2)
ax.add_patch(rect)
ax.text(1.7, 6.3, 'CURRENT', ha='center', fontsize=9, color=C_RED, fontweight='bold')
ax.text(1.7, 5.7, 'Lock-IN:', ha='center', fontsize=8, color=C_WHITE)
ax.text(1.7, 5.3, 'L4 Robotaxi Only', ha='center', fontsize=9, color=C_YELLOW)
ax.text(1.7, 4.9, 'Lock-OUT:', ha='center', fontsize=8, color=C_WHITE)
ax.text(1.7, 4.5, 'Trucking, ADAS', ha='center', fontsize=9, color=C_GRAY)

# ============ CENTER: THREE QUESTIONS ============
# Q1: HOW TO SCALE
q1_box = FancyBboxPatch((3.8, 5.2), 2.4, 1.5, boxstyle="round,pad=0.05",
                         facecolor='#1a1a2e', edgecolor=C_YELLOW, linewidth=2)
ax.add_patch(q1_box)
ax.text(5, 6.4, 'Q1: HOW TO SCALE?', ha='center', fontsize=9, color=C_YELLOW, fontweight='bold')
ax.text(5, 6.0, '* Platformize', ha='center', fontsize=8, color=C_WHITE)
ax.text(5, 5.6, '* Capitalize', ha='center', fontsize=8, color=C_WHITE)
ax.text(5, 5.2, '-> Modular SW Stack', ha='center', fontsize=7, color=C_GREEN, style='italic')

# Q2: HOW TO BUILD
q2_box = FancyBboxPatch((3.8, 3.2), 2.4, 1.8, boxstyle="round,pad=0.05",
                         facecolor='#1a1a2e', edgecolor=C_RED, linewidth=2)
ax.add_patch(q2_box)
ax.text(5, 4.7, 'Q2: HOW TO BUILD?', ha='center', fontsize=9, color=C_RED, fontweight='bold')
ax.text(5, 4.3, '* Collaborate', ha='center', fontsize=8, color=C_WHITE)
ax.text(5, 3.95, '  Uber/Lyft (delivery)', ha='center', fontsize=7, color=C_GRAY)
ax.text(5, 3.6, '  Hyundai (production)', ha='center', fontsize=7, color=C_GRAY)
ax.text(5, 3.25, '-> Ops Capability', ha='center', fontsize=7, color=C_GREEN, style='italic')

# Q3: WHERE TO PLAY
q3_box = FancyBboxPatch((3.8, 1.2), 2.4, 1.8, boxstyle="round,pad=0.05",
                         facecolor='#1a1a2e', edgecolor=C_GREEN, linewidth=2)
ax.add_patch(q3_box)
ax.text(5, 2.7, 'Q3: WHERE TO PLAY?', ha='center', fontsize=9, color=C_GREEN, fontweight='bold')
ax.text(5, 2.3, '* Segment', ha='center', fontsize=8, color=C_WHITE)
ax.text(5, 1.95, '  Robotaxi vs Trucking', ha='center', fontsize=7, color=C_GRAY)
ax.text(5, 1.6, '  B2B vs B2C', ha='center', fontsize=7, color=C_GRAY)
ax.text(5, 1.25, '-> Market Focus', ha='center', fontsize=7, color=C_GREEN, style='italic')

# ============ RIGHT: OUTCOME SCENARIOS ============
# Scenario A: Robotaxi B2C
sc_a = FancyBboxPatch((7, 5.5), 2.2, 1.2, boxstyle="round,pad=0.05",
                       facecolor='#1a1a2e', edgecolor=C_BLUE, linewidth=1.5)
ax.add_patch(sc_a)
ax.text(8.1, 6.4, 'Path A: Robotaxi B2C', ha='center', fontsize=8, color=C_BLUE, fontweight='bold')
ax.text(8.1, 6.0, 'vs Waymo', ha='center', fontsize=7, color=C_GRAY)
ax.text(8.1, 5.65, 'High Risk, High Reward', ha='center', fontsize=7, color=C_RED)

# Scenario B: Trucking B2B
sc_b = FancyBboxPatch((7, 3.8), 2.2, 1.2, boxstyle="round,pad=0.05",
                       facecolor='#1a1a2e', edgecolor=C_GREEN, linewidth=2)
ax.add_patch(sc_b)
ax.text(8.1, 4.7, 'Path B: Trucking B2B', ha='center', fontsize=8, color=C_GREEN, fontweight='bold')
ax.text(8.1, 4.3, 'vs Aurora', ha='center', fontsize=7, color=C_GRAY)
ax.text(8.1, 3.95, '[Recommended]', ha='center', fontsize=7, color=C_GREEN, fontweight='bold')

# Scenario C: Hybrid
sc_c = FancyBboxPatch((7, 2.1), 2.2, 1.2, boxstyle="round,pad=0.05",
                       facecolor='#1a1a2e', edgecolor=C_GRAY, linewidth=1)
ax.add_patch(sc_c)
ax.text(8.1, 3.0, 'Path C: Hybrid', ha='center', fontsize=8, color=C_GRAY, fontweight='bold')
ax.text(8.1, 2.6, 'Both Markets', ha='center', fontsize=7, color=C_GRAY)
ax.text(8.1, 2.25, 'Resource Spread Risk', ha='center', fontsize=7, color=C_YELLOW)

# ============ FAR RIGHT: NFSC PHASE ============
nfsc_box = FancyBboxPatch((9.8, 3.5), 2, 3, boxstyle="round,pad=0.05",
                           facecolor='#1a1a2e', edgecolor=C_WHITE, linewidth=1)
ax.add_patch(nfsc_box)
ax.text(10.8, 6.2, 'NFSC', ha='center', fontsize=9, color=C_WHITE, fontweight='bold')

# NAIL phase
ax.add_patch(FancyBboxPatch((10, 5.3), 1.6, 0.7, boxstyle="round,pad=0.02",
                             facecolor=(1, 0.83, 0.23, 0.2), edgecolor=C_YELLOW, linewidth=1))
ax.text(10.8, 5.8, 'NAIL', ha='center', fontsize=8, color=C_YELLOW, fontweight='bold')
ax.text(10.8, 5.45, '18mo validation', ha='center', fontsize=6, color=C_GRAY)

# Arrow
ax.annotate('', xy=(10.8, 4.9), xytext=(10.8, 5.2),
            arrowprops=dict(arrowstyle='->', color=C_WHITE, lw=1.5))
ax.text(11.3, 5.05, 'μ→0/1', ha='left', fontsize=6, color=C_BLUE)

# SCALE phase
ax.add_patch(FancyBboxPatch((10, 4.0), 1.6, 0.7, boxstyle="round,pad=0.02",
                             facecolor=(0.41, 0.86, 0.49, 0.2), edgecolor=C_GREEN, linewidth=1))
ax.text(10.8, 4.5, 'SCALE', ha='center', fontsize=8, color=C_GREEN, fontweight='bold')
ax.text(10.8, 4.15, 'Full Commit', ha='center', fontsize=6, color=C_GRAY)

# ============ ARROWS ============
# Current → Q1
ax.annotate('', xy=(3.8, 5.9), xytext=(3.1, 5.5),
            arrowprops=dict(arrowstyle='->', color=C_GRAY, lw=1.5))

# Q1 → Q2
ax.annotate('', xy=(5, 5.0), xytext=(5, 5.2),
            arrowprops=dict(arrowstyle='->', color=C_GRAY, lw=1))

# Q2 → Q3
ax.annotate('', xy=(5, 3.0), xytext=(5, 3.2),
            arrowprops=dict(arrowstyle='->', color=C_GRAY, lw=1))

# Q boxes → Scenarios
ax.annotate('', xy=(7, 6.1), xytext=(6.2, 5.9),
            arrowprops=dict(arrowstyle='->', color=C_GRAY, lw=1, ls='--'))
ax.annotate('', xy=(7, 4.4), xytext=(6.2, 4.1),
            arrowprops=dict(arrowstyle='->', color=C_GREEN, lw=2))
ax.annotate('', xy=(7, 2.7), xytext=(6.2, 2.1),
            arrowprops=dict(arrowstyle='->', color=C_GRAY, lw=1, ls='--'))

# Scenario B → NFSC
ax.annotate('', xy=(9.8, 4.85), xytext=(9.2, 4.4),
            arrowprops=dict(arrowstyle='->', color=C_GREEN, lw=2))

# ============ BOTTOM LEGEND ============
ax.text(6, 0.5, 'Funding Paradox Solution: Nail with Flexibility (Q1-Q3) → Scale with Commitment (NFSC)',
        ha='center', fontsize=9, color=C_YELLOW, style='italic')

plt.tight_layout()
plt.savefig('/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/papers_v5/figures/fig_BM_motional_strategy.png',
            dpi=150, facecolor='#0a0e14', edgecolor='none', bbox_inches='tight')
plt.close()
print("Figure saved: fig_BM_motional_strategy.png")
