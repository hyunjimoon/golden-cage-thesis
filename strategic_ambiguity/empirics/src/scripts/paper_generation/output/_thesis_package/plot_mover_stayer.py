#!/usr/bin/env python3
"""
🐅 M_fig5_mover_stayer.py
Solving the Puzzle: Movement Explains Everything

Creates a 2-panel figure showing:
- Left: Aggregate success rate by Vagueness Quartile (the anomaly)
- Right: Decomposed success by Movers vs Stayers (the explanation)

Reproduces the "Q3 Anomaly Explained" visualization.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# CONFIGURATION
# ============================================================================

ROOT = Path("/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics")
DATA_PATH = ROOT / "data/processed/vagueness_timeseries.parquet"
COMPANY_PATH = ROOT / "data/processed/Company20251101.parquet"
FIG_DIR = ROOT / "src/scripts/paper_generation/output/_thesis_package/figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# Elegant color palette (matching the reference image)
COLORS = {
    'stayer': '#4a6fa5',     # Muted blue for Stayers
    'mover': '#d4a05a',      # Golden/orange for Movers
    'aggregate': '#3d5a80',  # Darker blue for aggregate bars
    'background': '#f5f3ef', # Warm light background
    'text': '#2b2b2b',       # Dark text
    'annotation': '#f0e6d3', # Annotation box background
}

plt.rcParams.update({
    'figure.dpi': 300,
    'figure.facecolor': COLORS['background'],
    'axes.facecolor': COLORS['background'],
    'font.size': 11,
    'font.family': 'DejaVu Sans',
    'axes.titleweight': 'bold',
    'axes.labelweight': 'normal',
    'savefig.bbox': 'tight',
    'savefig.facecolor': COLORS['background'],
})

# ============================================================================
# DATA LOADING
# ============================================================================

def load_data():
    """Load and prepare cross-sectional data."""
    print("📂 Loading data...")
    
    # Load vagueness timeseries
    panel = pd.read_parquet(DATA_PATH)
    
    # Load company outcomes
    company_cols = ['CompanyID', 'TotalRaised', 'BusinessStatus', 'LastFinancingDealType']
    company_df = pd.read_parquet(COMPANY_PATH, columns=company_cols)
    company_df.columns = ['company_id', 'TotalRaised_2025', 'BusinessStatus', 'LastFinancingDealType']
    company_df['company_id'] = company_df['company_id'].astype(str)
    
    # t=0 (2021)
    df_0 = panel[panel['year'] == 2021][['company_id', 'V', 'first_financing_size']].copy()
    df_0.columns = ['company_id', 'V', 'E']
    df_0['company_id'] = df_0['company_id'].astype(str)
    
    # t=T (2025)
    df_T = panel[panel['year'] == 2025][['company_id', 'V', 'total_delta_V']].copy()
    df_T.columns = ['company_id', 'V_T', 'D']
    df_T['company_id'] = df_T['company_id'].astype(str)
    
    # Merge
    cross = df_0.merge(df_T, on='company_id', how='inner')
    cross = cross.merge(company_df, on='company_id', how='left')
    
    # Derived variables
    cross['A'] = cross['D'].abs()
    cross['V_Q'] = pd.qcut(cross['V'], 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
    
    # L = Long-term Success (Later Stage VC)
    cross['L'] = (cross['LastFinancingDealType'] == 'Later Stage VC').astype(int)
    failed_statuses = ['Out of Business', 'Bankruptcy: Liquidation', 'Bankruptcy: Admin/Reorg']
    cross.loc[cross['BusinessStatus'].isin(failed_statuses), 'L'] = 0
    
    # Mover vs Stayer classification
    cross['is_mover'] = (cross['D'] != 0).astype(int)
    cross['mover_label'] = cross['is_mover'].map({0: 'Stayer', 1: 'Mover'})
    
    # Filter valid
    valid = cross[['V', 'D', 'A']].notna().all(axis=1)
    cross = cross[valid].copy()
    
    print(f"   N = {len(cross):,}")
    print(f"   Movers: {cross['is_mover'].sum():,} ({cross['is_mover'].mean()*100:.1f}%)")
    print(f"   L (Success) rate: {cross['L'].mean()*100:.1f}%")
    
    return cross

# ============================================================================
# MAIN FIGURE: MOVER/STAYER DECOMPOSITION
# ============================================================================

def plot_mover_stayer_decomposition(cross):
    """
    Create the key figure: Movement Explains Everything
    
    Left panel: Aggregate success by quartile (shows the anomaly)
    Right panel: Decomposed by Movers vs Stayers (explains the anomaly)
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # ========== COMPUTE STATISTICS ==========
    
    # Aggregate by quartile
    agg_stats = cross.groupby('V_Q').agg({
        'L': ['mean', 'count'],
        'is_mover': 'mean'
    }).round(4)
    agg_stats.columns = ['success_rate', 'n', 'mover_rate']
    agg_stats['success_pct'] = agg_stats['success_rate'] * 100
    
    # Decomposed by quartile × mover status
    decomp_stats = cross.groupby(['V_Q', 'mover_label']).agg({
        'L': ['mean', 'count']
    }).round(4)
    decomp_stats.columns = ['success_rate', 'n']
    decomp_stats['success_pct'] = decomp_stats['success_rate'] * 100
    decomp_stats = decomp_stats.reset_index()
    
    print("\n📊 Aggregate Stats by Quartile:")
    print(agg_stats)
    
    print("\n📊 Decomposed Stats:")
    print(decomp_stats.pivot(index='V_Q', columns='mover_label', values='success_pct'))
    
    # ========== PANEL A: THE ANOMALY ==========
    
    ax1 = axes[0]
    
    quartiles = ['Q1', 'Q2', 'Q3', 'Q4']
    x_pos = np.arange(len(quartiles))
    heights = [agg_stats.loc[q, 'success_pct'] for q in quartiles]
    
    bars = ax1.bar(x_pos, heights, 
                   color=COLORS['aggregate'], 
                   edgecolor='black', 
                   linewidth=1.2,
                   width=0.6)
    
    # Value labels on bars
    for bar, height in zip(bars, heights):
        ax1.text(bar.get_x() + bar.get_width()/2, height + 0.3, 
                 f'{height:.1f}%',
                 ha='center', va='bottom', 
                 fontsize=12, fontweight='bold',
                 color=COLORS['text'])
    
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(quartiles, fontsize=11)
    ax1.set_xlabel('Bar', fontsize=11)
    ax1.set_ylabel('Success Rate', fontsize=11)
    ax1.set_ylim(0, max(heights) * 1.25)
    
    # Remove top and right spines
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    
    ax1.set_title('The Anomaly', fontsize=14, fontweight='bold', pad=10)
    
    # Subtitle annotation
    ax1.text(0.5, 1.02, 'Aggregate Success Rate\nby Initial Vagueness Quartile',
             transform=ax1.transAxes, ha='center', va='bottom',
             fontsize=10, style='italic', color='gray')
    
    # ========== PANEL B: THE EXPLANATION ==========
    
    ax2 = axes[1]
    
    # Prepare data for stacked bars
    stayer_heights = []
    mover_heights = []
    
    for q in quartiles:
        stayer_row = decomp_stats[(decomp_stats['V_Q'] == q) & (decomp_stats['mover_label'] == 'Stayer')]
        mover_row = decomp_stats[(decomp_stats['V_Q'] == q) & (decomp_stats['mover_label'] == 'Mover')]
        
        stayer_pct = stayer_row['success_pct'].values[0] if len(stayer_row) > 0 else 0
        mover_pct = mover_row['success_pct'].values[0] if len(mover_row) > 0 else 0
        
        stayer_heights.append(stayer_pct)
        mover_heights.append(mover_pct)
    
    bar_width = 0.6
    
    # Draw stacked bars (Stayers at bottom, Movers on top)
    bars_stayer = ax2.bar(x_pos, stayer_heights, 
                          color=COLORS['stayer'], 
                          edgecolor='black',
                          linewidth=1.2,
                          width=bar_width,
                          label='Stayers')
    
    bars_mover = ax2.bar(x_pos, mover_heights, 
                         bottom=stayer_heights,
                         color=COLORS['mover'],
                         edgecolor='black',
                         linewidth=1.2,
                         width=bar_width,
                         label='Movers')
    
    # Labels on stacked bars
    for i, (q, sh, mh) in enumerate(zip(quartiles, stayer_heights, mover_heights)):
        # Stayer label (in the middle of stayer bar)
        ax2.text(i, sh/2, f'Stayers\n{sh:.1f}%',
                 ha='center', va='center',
                 fontsize=9, fontweight='bold',
                 color='white')
        
        # Mover label (in the middle of mover bar)
        ax2.text(i, sh + mh/2, f'Movers\n{mh:.1f}%',
                 ha='center', va='center',
                 fontsize=9, fontweight='bold',
                 color='black')
    
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels(quartiles, fontsize=11)
    ax2.set_xlabel('Bar', fontsize=11)
    ax2.set_ylabel('', fontsize=11)
    ax2.set_ylim(0, max(np.array(stayer_heights) + np.array(mover_heights)) * 1.15)
    
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    
    ax2.set_title('The Explanation', fontsize=14, fontweight='bold', pad=10)
    
    # Subtitle annotation  
    ax2.text(0.5, 1.02, 'Decomposed Success: Movers vs. Stayers\nby Initial Vagueness Quartile',
             transform=ax2.transAxes, ha='center', va='bottom',
             fontsize=10, style='italic', color='gray')
    
    # ========== ARROW BETWEEN PANELS ==========
    
    # Add arrow from left to right panel
    arrow_props = dict(arrowstyle='->', color=COLORS['mover'], lw=3, 
                       mutation_scale=20)
    fig.annotate('', 
                 xy=(0.52, 0.5), xycoords='figure fraction',
                 xytext=(0.48, 0.5), textcoords='figure fraction',
                 arrowprops=arrow_props)
    
    # ========== KEY INSIGHT ANNOTATION BOX ==========
    
    # Get Q3 movement rate
    q3_mover_rate = agg_stats.loc['Q3', 'mover_rate'] * 100
    q3_stayer_success = decomp_stats[(decomp_stats['V_Q'] == 'Q3') & 
                                      (decomp_stats['mover_label'] == 'Stayer')]['success_pct'].values[0]
    
    annotation_text = (f"Q3's high aggregate success is entirely explained by\n"
                       f"its high movement rate ({q3_mover_rate:.0f}%). Among \"Stayers,\" Q3\n"
                       f"actually has the lowest success rate ({q3_stayer_success:.1f}%).")
    
    # Add annotation box at bottom
    ax2.text(0.5, -0.22, annotation_text,
             transform=ax2.transAxes, ha='center', va='top',
             fontsize=10, style='italic',
             bbox=dict(boxstyle='round,pad=0.5', 
                       facecolor=COLORS['annotation'],
                       edgecolor='#c4b7a3',
                       linewidth=1.5))
    
    # ========== MAIN TITLE ==========
    
    fig.suptitle('Solving the Puzzle: Movement Explains Everything',
                 fontsize=16, fontweight='bold', y=1.02)
    
    plt.tight_layout()
    fig.subplots_adjust(wspace=0.15, bottom=0.18)
    
    # Save
    output_path = FIG_DIR / 'M_fig5_mover_stayer.png'
    fig.savefig(output_path, dpi=300)
    plt.close()
    
    print(f"\n✅ Saved: {output_path}")
    
    # Return key statistics for documentation
    return {
        'aggregate': dict(agg_stats['success_pct']),
        'stayer_success': dict(zip(quartiles, stayer_heights)),
        'mover_success': dict(zip(quartiles, mover_heights)),
        'mover_rate': dict(agg_stats['mover_rate'] * 100),
    }

# ============================================================================
# MAIN
# ============================================================================

def main():
    print("="*60)
    print("🐅 M_fig5_mover_stayer.py")
    print("Solving the Puzzle: Movement Explains Everything")
    print("="*60)
    
    cross = load_data()
    stats = plot_mover_stayer_decomposition(cross)
    
    print("\n📊 KEY STATISTICS:")
    print(f"   Q3 Aggregate: {stats['aggregate']['Q3']:.1f}%")
    print(f"   Q3 Movers:    {stats['mover_success']['Q3']:.1f}%")
    print(f"   Q3 Stayers:   {stats['stayer_success']['Q3']:.1f}%")
    print(f"   Q3 Move Rate: {stats['mover_rate']['Q3']:.1f}%")
    
    # Movement ratio
    overall_mover = sum(stats['mover_success'].values()) / 4
    overall_stayer = sum(stats['stayer_success'].values()) / 4
    print(f"\n   Overall Mover Success:  {overall_mover:.1f}%")
    print(f"   Overall Stayer Success: {overall_stayer:.1f}%")
    print(f"   Movement Advantage:     {overall_mover/overall_stayer:.1f}×")

if __name__ == "__main__":
    main()
