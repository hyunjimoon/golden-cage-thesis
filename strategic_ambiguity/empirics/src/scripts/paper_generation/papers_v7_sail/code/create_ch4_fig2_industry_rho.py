#!/usr/bin/env python3
"""
Generate Ch4_Fig2_industry_rho.png
Industry Heterogeneity: Early Funding-Growth Correlation

Color scheme aligned with thesis macros:
- Green (ParadoxColor RGB 40,167,69): Industries showing the paradox (negative ρ)
- Gray: Quantum (the exception, positive ρ)
"""

import matplotlib.pyplot as plt
import numpy as np

# Data from thesis
industries = ['Quantum', 'Software', 'MedTech', 'Pharma', 'Transportation', 'Hardware']
correlations = [0.095, -0.001, -0.053, -0.079, -0.101, -0.108]
sample_sizes = [1144, 226896, 29493, 56947, 154148, 50390]
significance = ['*', '', '***', '***', '***', '***']

# Colors aligned with thesis color definitions
PARADOX_GREEN = '#28a745'  # RGB(40,167,69) - for industries showing the paradox
EXCEPTION_GRAY = '#9E9E9E'  # Gray for Quantum (the exception)

# Assign colors: Quantum gets gray, all others get green (paradox)
colors = [EXCEPTION_GRAY if ind == 'Quantum' else PARADOX_GREEN for ind in industries]

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Horizontal bar chart
y_pos = np.arange(len(industries))
bars = ax.barh(y_pos, correlations, color=colors, height=0.6, edgecolor='none')

# Add vertical line at x=0
ax.axvline(x=0, color='black', linewidth=0.8)

# Labels for each bar
for i, (corr, sig, n) in enumerate(zip(correlations, significance, sample_sizes)):
    # Correlation value with significance
    label = f'{corr:+.3f}{sig}'
    x_pos = corr + 0.008 if corr >= 0 else corr - 0.008
    ha = 'left' if corr >= 0 else 'right'
    ax.text(x_pos, i, label, va='center', ha=ha, fontsize=11, fontweight='medium')

    # Sample size on the right
    ax.text(0.155, i, f'N={n:,}', va='center', ha='left', fontsize=9, color='gray')

# Annotations
ax.annotate('Era of Ferment\n(Quantum)',
            xy=(0.095, 0), xytext=(0.12, 0.5),
            fontsize=10, color=EXCEPTION_GRAY, fontweight='bold',
            ha='center')

ax.annotate('Cage binds tight\n(Capital-intensive)',
            xy=(-0.108, 5), xytext=(-0.12, 4.5),
            fontsize=10, color=PARADOX_GREEN, fontweight='bold',
            ha='center')

# Formatting
ax.set_yticks(y_pos)
ax.set_yticklabels(industries, fontsize=11)
ax.set_xlabel('Correlation ρ(E, G)', fontsize=12)
ax.set_xlim(-0.15, 0.18)
ax.set_title('Industry Heterogeneity: Early Funding–Growth Correlation', fontsize=14, fontweight='bold')

# Remove spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('/Users/hyunjimoon/golden-cage-thesis/strategic_ambiguity/empirics/src/scripts/paper_generation/papers_v7_sail/img_overleaf/Ch4_Fig2_industry_rho.png',
            dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

print("Figure saved: Ch4_Fig2_industry_rho.png")
print("Color scheme: Green = Paradox industries, Gray = Quantum (exception)")
