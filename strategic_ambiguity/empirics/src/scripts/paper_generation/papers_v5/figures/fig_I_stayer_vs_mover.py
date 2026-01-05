import matplotlib.pyplot as plt
import numpy as np

# Set style
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(6, 4), facecolor='#0a0e14')
ax.set_facecolor('#0a0e14')

# Data
categories = ['Stayer\n(A ≈ 0)', 'Mover\n(A > 0)']
survival_rates = [9.9, 17.9]
colors = ['#c9d1d9', '#69db7c']

# Bar chart
bars = ax.bar(categories, survival_rates, color=colors, width=0.6, edgecolor='white', linewidth=1.5)

# Add value labels
for bar, rate in zip(bars, survival_rates):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.8,
            f'{rate}%', ha='center', va='bottom', fontsize=14, fontweight='bold', color='white')

# Add ratio annotation
ax.annotate('', xy=(1, 17.9), xytext=(0, 9.9),
            arrowprops=dict(arrowstyle='->', color='#ffd43b', lw=2))
ax.text(0.5, 14, '1.8×', ha='center', va='center', fontsize=12,
        color='#ffd43b', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#0a0e14', edgecolor='#ffd43b'))

# Labels
ax.set_ylabel('Survival Rate (%)', fontsize=11, color='white')
ax.set_title('The Funding Paradox\ndG/dF < 0: Movement Predicts Growth',
             fontsize=13, fontweight='bold', color='#ff6b6b', pad=15)

# Styling
ax.set_ylim(0, 22)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#21262d')
ax.spines['bottom'].set_color('#21262d')
ax.tick_params(colors='#7d8590')
ax.yaxis.grid(True, linestyle='--', alpha=0.3, color='#21262d')

# Add subtitle
ax.text(0.5, -0.15, 'N = 180,994 | ρ(G,F) = −0.196***',
        transform=ax.transAxes, ha='center', fontsize=9, color='#7d8590')

plt.tight_layout()
plt.savefig('/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/papers_v5/figures/fig_I_stayer_vs_mover.png',
            dpi=150, facecolor='#0a0e14', edgecolor='none', bbox_inches='tight')
plt.close()
print("Figure saved: fig_I_stayer_vs_mover.png")
