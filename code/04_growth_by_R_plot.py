#!/usr/bin/env python3
"""
04_growth_by_R_plot.py - Growth by Repositioning (R > 0 Definition)
=====================================================================

Generates a clear visualization of the Mover Advantage using the
SIMPLE R > 0 definition (any movement = Mover).

Key Result: Movers (R > 0) achieve ~2x higher success rates than Stayers (R = 0)

Author: Claude Code CLI
Date: 2026-01-13
"""

import logging
from pathlib import Path
import pandas as pd
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(message)s', datefmt='%H:%M:%S')
log = logging.getLogger(__name__)

SCRIPT_DIR = Path(__file__).parent.resolve()
DATA_DIR = SCRIPT_DIR / 'data'
FIG_DIR = SCRIPT_DIR / 'figures'
THESIS_FIG_DIR = SCRIPT_DIR.parent / 'figures'
FIG_DIR.mkdir(parents=True, exist_ok=True)

# Colors - Grayscale for thesis consistency
MOVER_COLOR = '#2c3e50'   # Dark gray (Movers)
STAYER_COLOR = '#bdc3c7'  # Light gray (Stayers)

plt.rcParams.update({
    'figure.dpi': 150,
    'font.size': 12,
    'font.family': 'DejaVu Sans',
    'axes.titleweight': 'bold',
    'savefig.bbox': 'tight',
    'savefig.facecolor': 'white',
})


def load_data():
    """Load thesis panel data."""
    nc_path = DATA_DIR / 'thesis_panel_v3.nc'
    if nc_path.exists():
        ds = xr.open_dataset(nc_path)
        df = ds.to_dataframe().reset_index()
        log.info(f"Loaded {len(df):,} rows from thesis_panel_v3.nc")
        return df

    # Fallback to parquet
    parquet_path = DATA_DIR / 'processed' / 'breadth_timeseries.parquet'
    if parquet_path.exists():
        df = pd.read_parquet(parquet_path)
        log.info(f"Loaded {len(df):,} rows from breadth_timeseries.parquet")
        return df

    raise FileNotFoundError("No data file found")


def compute_R_simple(df):
    """
    Compute R using SIMPLE definition: R = |V_T - V_0| (or M if already computed)
    Mover = R > 0 (any movement)
    Stayer = R = 0 (no movement)

    Data columns in thesis_panel_v3.nc:
    - V_0, V_T: breadth at t=0 and t=T
    - D: direction (V_T - V_0)
    - M: magnitude |D| (repositioning)
    - moved: is_mover (0/1 based on current threshold)
    - L: later stage success
    """
    # Use M column if exists (magnitude of repositioning)
    if 'M' in df.columns:
        df['R'] = df['M']
    elif 'D' in df.columns:
        df['R'] = df['D'].abs()
    elif 'V_0' in df.columns and 'V_T' in df.columns:
        df['R'] = (df['V_T'] - df['V_0']).abs()
    elif 'B_0' in df.columns and 'B_T' in df.columns:
        df['R'] = (df['B_T'] - df['B_0']).abs()
    elif 'breadth' in df.columns:
        # From timeseries: pivot to get B_0 and B_T
        pivot = df.pivot_table(index='company_id', columns='year', values='breadth')
        if 2021 in pivot.columns and 2025 in pivot.columns:
            df_r = pd.DataFrame({
                'company_id': pivot.index,
                'B_0': pivot[2021].values,
                'B_T': pivot[2025].values,
            })
            df_r['R'] = (df_r['B_T'] - df_r['B_0']).abs()
            return df_r

    return df


def analyze_growth_by_R(df):
    """
    Analyze growth by repositioning status using R > 0 definition.

    KEY CHANGE: Use simple R > 0 definition instead of R > median
    """
    log.info("\n" + "="*60)
    log.info("GROWTH BY REPOSITIONING (R > 0 Definition)")
    log.info("="*60)

    # Ensure R is computed
    df = compute_R_simple(df)

    # Filter valid R values
    df_valid = df[df['R'].notna()].copy()
    log.info(f"Valid R observations: {len(df_valid):,}")

    # Define Movers (R > 0) and Stayers (R = 0) - SIMPLE DEFINITION
    df_valid['is_mover_simple'] = (df_valid['R'] > 0).astype(int)

    movers = df_valid[df_valid['is_mover_simple'] == 1]
    stayers = df_valid[df_valid['is_mover_simple'] == 0]

    log.info(f"Movers (R > 0): {len(movers):,} ({len(movers)/len(df_valid)*100:.1f}%)")
    log.info(f"Stayers (R = 0): {len(stayers):,} ({len(stayers)/len(df_valid)*100:.1f}%)")

    # Growth outcome (L = later stage success)
    growth_col = 'L' if 'L' in df_valid.columns else None

    results = {
        'n_total': len(df_valid),
        'n_movers': len(movers),
        'n_stayers': len(stayers),
        'mover_pct': len(movers) / len(df_valid) * 100,
    }

    if growth_col and growth_col in df_valid.columns:
        mover_success = movers[growth_col].mean() * 100
        stayer_success = stayers[growth_col].mean() * 100
        advantage = mover_success / stayer_success if stayer_success > 0 else np.nan

        results['mover_success'] = mover_success
        results['stayer_success'] = stayer_success
        results['advantage'] = advantage

        log.info(f"\nSuccess Rates:")
        log.info(f"  Movers (R > 0): {mover_success:.1f}%")
        log.info(f"  Stayers (R = 0): {stayer_success:.1f}%")
        log.info(f"  Mover Advantage: {advantage:.2f}x")

        # Chi-square test
        contingency = pd.crosstab(df_valid['is_mover_simple'], df_valid[growth_col])
        if contingency.shape == (2, 2):
            chi2, p_value, _, _ = chi2_contingency(contingency)
            results['chi2'] = chi2
            results['p_value'] = p_value
            log.info(f"  Chi-square: {chi2:.1f}, p < {p_value:.2e}")

    return df_valid, results


def plot_growth_by_R(df_valid, results, save_path=None):
    """
    Create a clear bar chart showing Mover vs Stayer success rates.
    """
    fig, ax = plt.subplots(figsize=(8, 6))

    categories = ['Stayers\n(R = 0)', 'Movers\n(R > 0)']
    success_rates = [results['stayer_success'], results['mover_success']]
    n_values = [results['n_stayers'], results['n_movers']]
    colors = [STAYER_COLOR, MOVER_COLOR]

    bars = ax.bar(categories, success_rates, color=colors,
                  edgecolor='black', linewidth=2, width=0.6)

    # Value labels
    for i, (bar, rate, n) in enumerate(zip(bars, success_rates, n_values)):
        ax.text(bar.get_x() + bar.get_width()/2, rate + 0.8,
                f'{rate:.1f}%',
                ha='center', fontsize=16, fontweight='bold')
        # Use dark text for light bar, white text for dark bar
        text_color = 'white' if i == 1 else '#2c3e50'
        ax.text(bar.get_x() + bar.get_width()/2, rate/2,
                f'n = {n:,}',
                ha='center', fontsize=11, color=text_color, fontweight='bold')

    # Advantage annotation with arrow
    advantage = results['advantage']
    mid_x = 0.5
    max_y = max(success_rates)

    # Arrow showing advantage
    ax.annotate('', xy=(1, success_rates[1]), xytext=(0, success_rates[0]),
                arrowprops=dict(arrowstyle='->', color='#2c3e50', lw=2,
                              connectionstyle='arc3,rad=0.2'))

    # Advantage text box - simple grayscale
    ax.text(mid_x, max_y * 1.15, f'{advantage:.2f}x',
            ha='center', fontsize=24, fontweight='bold', color='#2c3e50',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                     edgecolor='#2c3e50', linewidth=2))

    ax.text(mid_x, max_y * 1.02, 'Mover Advantage',
            ha='center', fontsize=12, style='italic')

    # Labels and title
    ax.set_ylabel('Success Rate (Later Stage VC) %', fontsize=13)
    ax.set_title('Growth by Repositioning',
                 fontsize=15, fontweight='bold')
    ax.set_ylim(0, max_y * 1.35)

    # Remove top/right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Significance
    if 'p_value' in results:
        sig = '***' if results['p_value'] < 0.001 else '**' if results['p_value'] < 0.01 else '*' if results['p_value'] < 0.05 else ''
        ax.text(0.98, 0.02, f'χ² = {results["chi2"]:.1f}{sig}',
                transform=ax.transAxes, ha='right', fontsize=10, color='gray')

    # Key message at bottom
    fig.text(0.5, -0.02,
             f'N = {results["n_total"]:,} | Mover = R > 0 (any repositioning)',
             ha='center', fontsize=10, color='gray')

    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')
        log.info(f"Figure saved: {save_path}")

    return fig


def main():
    log.info("="*60)
    log.info("GENERATING: Growth by R Plot (R > 0 Definition)")
    log.info("="*60)

    # Load data
    df = load_data()

    # Analyze
    df_valid, results = analyze_growth_by_R(df)

    # Plot
    output_path = FIG_DIR / 'Fig_growth_by_R.png'
    plot_growth_by_R(df_valid, results, save_path=output_path)

    # Also copy to thesis figures
    thesis_path = THESIS_FIG_DIR / 'Fig_growth_by_R.png'
    if THESIS_FIG_DIR.exists():
        import shutil
        shutil.copy(output_path, thesis_path)
        log.info(f"Copied to thesis figures: {thesis_path}")

    log.info("\n" + "="*60)
    log.info("SUMMARY")
    log.info("="*60)
    log.info(f"Stayers (R = 0): {results['stayer_success']:.1f}% success")
    log.info(f"Movers (R > 0):  {results['mover_success']:.1f}% success")
    log.info(f"Mover Advantage: {results['advantage']:.2f}x")
    log.info("="*60)

    return df_valid, results


if __name__ == '__main__':
    df_valid, results = main()
