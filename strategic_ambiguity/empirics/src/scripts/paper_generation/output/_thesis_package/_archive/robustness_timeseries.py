#!/usr/bin/env python3
"""
🐅 Time-Series Robustness Check
Verify that key relationships hold across t = 2023, 2024, 2025

Key Hypotheses to Test:
1. ρ(A_t, E) < 0: Golden Cage holds at each time point
2. ρ(G_t, A_t) > 0: Flexibility → Growth at each time point
3. ρ(G_t, E) < 0: Capital curse at each time point

Where:
- D_t = V_t - V_0 (directional change from 2021)
- A_t = |D_t| (adaptive capacity at time t)
- G_t = (TotalRaised_t - E) / E (growth ratio at time t)

Output:
- R1_robustness_timeseries.png: 3×3 panel showing consistency
- robustness_statistics.json: All coefficients with significance

Author: Claude Code
Date: 2025-12-10
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from scipy import stats
import json
import warnings
warnings.filterwarnings('ignore')

# Configuration
SEED = 42
np.random.seed(SEED)

ROOT = Path("/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics")
DATA_PATH = ROOT / "data/processed/vagueness_timeseries.parquet"
FIG_DIR = ROOT / "src/scripts/paper_generation/output/_thesis_package/figures"
STATS_DIR = ROOT / "src/scripts/paper_generation/output/_thesis_package/stats"

# Company files for each year
COMPANY_FILES = {
    2023: ROOT / "data/processed/Company20231201.parquet",
    2024: ROOT / "data/processed/Company20241201.parquet",
    2025: ROOT / "data/processed/Company20251101.parquet",
}

COLORS = {
    'positive': '#27ae60',
    'negative': '#e74c3c',
    'neutral': '#3498db',
    '2023': '#3498db',
    '2024': '#9b59b6',
    '2025': '#e67e22',
}

plt.rcParams.update({
    'figure.dpi': 300,
    'font.size': 10,
    'font.family': 'DejaVu Sans',
    'axes.titleweight': 'bold',
})

def stars(p):
    if p < 0.001: return '***'
    if p < 0.01: return '**'
    if p < 0.05: return '*'
    return ''


def load_timeseries_data():
    """Load and compute D_t, A_t, G_t for each time point."""
    print("📂 Loading time-series data...")

    # Load panel
    panel = pd.read_parquet(DATA_PATH)

    # 2021 baseline
    df_2021 = panel[panel['year'] == 2021][['company_id', 'V', 'first_financing_size']].copy()
    df_2021.columns = ['company_id', 'V_0', 'E']
    df_2021['company_id'] = df_2021['company_id'].astype(str)
    df_2021['E_log'] = np.log10(df_2021['E'].clip(lower=0.01))

    results = {}

    for t in [2023, 2024, 2025]:
        print(f"   Processing t={t}...")

        # Get V_t
        df_t = panel[panel['year'] == t][['company_id', 'V']].copy()
        df_t.columns = ['company_id', 'V_t']
        df_t['company_id'] = df_t['company_id'].astype(str)

        # Merge with baseline
        cross = df_2021.merge(df_t, on='company_id', how='inner')

        # Compute D_t and A_t
        cross['D_t'] = cross['V_t'] - cross['V_0']
        cross['A_t'] = cross['D_t'].abs()

        # Load TotalRaised at time t
        if COMPANY_FILES[t].exists():
            company_df = pd.read_parquet(
                COMPANY_FILES[t],
                columns=['CompanyID', 'TotalRaised', 'BusinessStatus']
            )
            company_df.columns = ['company_id', 'TotalRaised_t', 'BusinessStatus']
            company_df['company_id'] = company_df['company_id'].astype(str)

            cross = cross.merge(company_df, on='company_id', how='left')

            # Compute G_t = (TotalRaised_t - E) / E
            cross['L_funding'] = cross['TotalRaised_t'] - cross['E']
            cross['L_funding'] = cross['L_funding'].clip(lower=0)
            cross['G_t'] = cross['L_funding'] / (cross['E'] + 0.001)

            # Cap outliers
            g_cap = cross['G_t'].quantile(0.99)
            cross['G_t'] = cross['G_t'].clip(upper=g_cap)

            # Survival
            failed = ['Out of Business', 'Bankruptcy: Liquidation', 'Bankruptcy: Admin/Reorg']
            cross['L_t'] = (~cross['BusinessStatus'].isin(failed)).astype(int)
            cross.loc[cross['BusinessStatus'].isna(), 'L_t'] = 1

        # Filter valid
        valid = cross[['V_0', 'E', 'D_t', 'A_t']].notna().all(axis=1) & (cross['E'] > 0)
        cross = cross[valid].copy()

        results[t] = cross
        print(f"      N={len(cross):,}, A_t mean={cross['A_t'].mean():.2f}")

    return results


def compute_robustness_stats(data_dict):
    """Compute key correlations at each time point."""
    stats_results = {}

    for t, df in data_dict.items():
        stats_t = {'year': t, 'N': len(df)}

        # 1. ρ(A_t, E) - Golden Cage
        valid = df['A_t'].notna() & df['E_log'].notna()
        if valid.sum() > 100:
            r, p = stats.pearsonr(df.loc[valid, 'E_log'], df.loc[valid, 'A_t'])
            stats_t['rho_AE'] = r
            stats_t['p_AE'] = p
            stats_t['sign_AE'] = 'negative' if r < 0 else 'positive'

        # 2. ρ(G_t, A_t) - Flexibility → Growth
        valid = df['G_t'].notna() & np.isfinite(df['G_t']) & df['A_t'].notna()
        if valid.sum() > 100:
            r, p = stats.pearsonr(df.loc[valid, 'A_t'], df.loc[valid, 'G_t'])
            stats_t['rho_GA'] = r
            stats_t['p_GA'] = p
            stats_t['sign_GA'] = 'positive' if r > 0 else 'negative'

        # 3. ρ(G_t, E) - Capital Curse
        valid = df['G_t'].notna() & np.isfinite(df['G_t']) & df['E_log'].notna()
        if valid.sum() > 100:
            r, p = stats.pearsonr(df.loc[valid, 'E_log'], df.loc[valid, 'G_t'])
            stats_t['rho_GE'] = r
            stats_t['p_GE'] = p
            stats_t['sign_GE'] = 'negative' if r < 0 else 'positive'

        # 4. ρ(L_t, A_t) - Survival ~ Flexibility
        if 'L_t' in df.columns:
            valid = df['L_t'].notna() & df['A_t'].notna()
            if valid.sum() > 100:
                r, p = stats.pearsonr(df.loc[valid, 'A_t'], df.loc[valid, 'L_t'])
                stats_t['rho_LA'] = r
                stats_t['p_LA'] = p

        # Survival rate
        if 'L_t' in df.columns:
            stats_t['survival_rate'] = df['L_t'].mean() * 100

        stats_results[t] = stats_t

    return stats_results


def plot_robustness_panel(data_dict, stats_dict):
    """
    Create 3×3 panel showing robustness across time.

    Rows: Hypotheses (ρ(A,E), ρ(G,A), ρ(G,E))
    Cols: Time points (2023, 2024, 2025)
    """
    fig, axes = plt.subplots(3, 3, figsize=(15, 12))

    years = [2023, 2024, 2025]

    for col, t in enumerate(years):
        df = data_dict[t]
        st = stats_dict[t]
        color = COLORS[str(t)]

        # --- Row 1: ρ(A_t, E) - Golden Cage ---
        ax = axes[0, col]
        valid = df['A_t'].notna() & df['E_log'].notna() & (df['E'] > 0)
        df_v = df[valid]

        # Binned scatter
        df_v = df_v.copy()
        df_v['E_bin'] = pd.qcut(df_v['E_log'], 10, labels=False, duplicates='drop')
        binned = df_v.groupby('E_bin').agg({'E': 'median', 'A_t': 'mean'})

        ax.scatter(binned['E'], binned['A_t'], s=60, c=color, edgecolors='black', alpha=0.8)

        # Regression line
        slope, intercept, r, p, se = stats.linregress(df_v['E_log'], df_v['A_t'])
        x_fit = np.linspace(df_v['E_log'].min(), df_v['E_log'].max(), 100)
        line_color = COLORS['negative'] if r < 0 else COLORS['positive']
        ax.plot(10**x_fit, slope * x_fit + intercept, '--', color=line_color, lw=2)

        ax.set_xscale('log')
        ax.set_xlabel('E (log)' if col == 1 else '')
        ax.set_ylabel('A_t = |ΔV|' if col == 0 else '')

        sign_check = "✓" if r < 0 else "✗"
        ax.set_title(f't={t}\nρ={r:.3f}{stars(p)} {sign_check}',
                    color=line_color, fontsize=11)
        ax.grid(True, alpha=0.3)

        # --- Row 2: ρ(G_t, A_t) - Flexibility → Growth ---
        ax = axes[1, col]
        valid = df['G_t'].notna() & np.isfinite(df['G_t']) & df['A_t'].notna()
        df_v = df[valid].copy()

        df_v['A_bin'] = pd.qcut(df_v['A_t'], 10, labels=False, duplicates='drop')
        binned = df_v.groupby('A_bin').agg({'A_t': 'median', 'G_t': 'mean'})

        ax.scatter(binned['A_t'], binned['G_t'], s=60, c=color, edgecolors='black', alpha=0.8)

        slope, intercept, r, p, se = stats.linregress(df_v['A_t'], df_v['G_t'])
        x_fit = np.linspace(df_v['A_t'].min(), df_v['A_t'].max(), 100)
        line_color = COLORS['positive'] if r > 0 else COLORS['negative']
        ax.plot(x_fit, slope * x_fit + intercept, '--', color=line_color, lw=2)

        ax.set_xlabel('A_t = |ΔV|' if col == 1 else '')
        ax.set_ylabel('G_t = L/E' if col == 0 else '')

        sign_check = "✓" if r > 0 else "✗"
        ax.set_title(f'ρ={r:.3f}{stars(p)} {sign_check}', color=line_color, fontsize=11)
        ax.grid(True, alpha=0.3)

        # --- Row 3: ρ(G_t, E) - Capital Curse ---
        ax = axes[2, col]
        valid = df['G_t'].notna() & np.isfinite(df['G_t']) & df['E_log'].notna() & (df['E'] > 0)
        df_v = df[valid].copy()

        df_v['E_bin'] = pd.qcut(df_v['E_log'], 10, labels=False, duplicates='drop')
        binned = df_v.groupby('E_bin').agg({'E': 'median', 'G_t': 'mean'})

        ax.scatter(binned['E'], binned['G_t'], s=60, c=color, edgecolors='black', alpha=0.8)

        slope, intercept, r, p, se = stats.linregress(df_v['E_log'], df_v['G_t'])
        x_fit = np.linspace(df_v['E_log'].min(), df_v['E_log'].max(), 100)
        line_color = COLORS['negative'] if r < 0 else COLORS['positive']
        ax.plot(10**x_fit, slope * x_fit + intercept, '--', color=line_color, lw=2)

        ax.set_xscale('log')
        ax.set_xlabel('E (log)' if col == 1 else '')
        ax.set_ylabel('G_t = L/E' if col == 0 else '')

        sign_check = "✓" if r < 0 else "✗"
        ax.set_title(f'ρ={r:.3f}{stars(p)} {sign_check}', color=line_color, fontsize=11)
        ax.grid(True, alpha=0.3)

    # Row labels
    axes[0, 0].annotate('H1: ρ(A,E) < 0\n"Golden Cage"',
                        xy=(-0.35, 0.5), xycoords='axes fraction',
                        fontsize=12, fontweight='bold', rotation=90, va='center')
    axes[1, 0].annotate('H2: ρ(G,A) > 0\n"Flexibility→Growth"',
                        xy=(-0.35, 0.5), xycoords='axes fraction',
                        fontsize=12, fontweight='bold', rotation=90, va='center')
    axes[2, 0].annotate('H3: ρ(G,E) < 0\n"Capital Curse"',
                        xy=(-0.35, 0.5), xycoords='axes fraction',
                        fontsize=12, fontweight='bold', rotation=90, va='center')

    fig.suptitle('Robustness Check: Key Relationships Across Time (t = 2023, 2024, 2025)\n'
                 '✓ = Expected sign confirmed, ✗ = Unexpected sign',
                 fontsize=14, fontweight='bold', y=1.02)

    plt.tight_layout()
    fig.savefig(FIG_DIR / 'R1_robustness_timeseries.png', bbox_inches='tight', facecolor='white')
    plt.close()
    print("   ✅ R1_robustness_timeseries.png")

    return fig


def plot_coefficient_evolution(stats_dict):
    """
    Show how coefficients evolve over time with confidence.
    Single panel with 3 lines showing temporal consistency.
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    years = [2023, 2024, 2025]

    # Extract coefficients
    rho_AE = [stats_dict[t].get('rho_AE', np.nan) for t in years]
    rho_GA = [stats_dict[t].get('rho_GA', np.nan) for t in years]
    rho_GE = [stats_dict[t].get('rho_GE', np.nan) for t in years]

    x = np.arange(len(years))
    width = 0.25

    bars1 = ax.bar(x - width, rho_AE, width, label='ρ(A,E): Golden Cage',
                   color=COLORS['negative'], alpha=0.8, edgecolor='black')
    bars2 = ax.bar(x, rho_GA, width, label='ρ(G,A): Flexibility→Growth',
                   color=COLORS['positive'], alpha=0.8, edgecolor='black')
    bars3 = ax.bar(x + width, rho_GE, width, label='ρ(G,E): Capital Curse',
                   color=COLORS['neutral'], alpha=0.8, edgecolor='black')

    # Add significance stars
    for i, t in enumerate(years):
        st = stats_dict[t]
        if 'p_AE' in st:
            ax.text(i - width, rho_AE[i] + 0.01, stars(st['p_AE']), ha='center', fontsize=10)
        if 'p_GA' in st:
            ax.text(i, rho_GA[i] + 0.01, stars(st['p_GA']), ha='center', fontsize=10)
        if 'p_GE' in st:
            ax.text(i + width, rho_GE[i] - 0.02, stars(st['p_GE']), ha='center', fontsize=10)

    ax.axhline(0, color='black', linewidth=1, linestyle='-')
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Correlation Coefficient (ρ)', fontsize=12)
    ax.set_title('Temporal Stability of Key Relationships\n'
                 'Expected: ρ(A,E) < 0, ρ(G,A) > 0, ρ(G,E) < 0', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3, axis='y')

    # Add expectation annotations
    ax.annotate('Expected < 0', xy=(0.1, -0.15), fontsize=9, color=COLORS['negative'])
    ax.annotate('Expected > 0', xy=(1.1, 0.08), fontsize=9, color=COLORS['positive'])
    ax.annotate('Expected < 0', xy=(2.1, -0.25), fontsize=9, color=COLORS['neutral'])

    plt.tight_layout()
    fig.savefig(FIG_DIR / 'R2_coefficient_evolution.png', bbox_inches='tight', facecolor='white')
    plt.close()
    print("   ✅ R2_coefficient_evolution.png")

    return fig


def create_robustness_table(stats_dict):
    """Create summary table for thesis."""
    rows = []

    for t in [2023, 2024, 2025]:
        st = stats_dict[t]
        row = {
            'Year': t,
            'N': st.get('N', 0),
            'ρ(A,E)': f"{st.get('rho_AE', np.nan):.3f}{stars(st.get('p_AE', 1))}",
            'ρ(G,A)': f"{st.get('rho_GA', np.nan):.3f}{stars(st.get('p_GA', 1))}",
            'ρ(G,E)': f"{st.get('rho_GE', np.nan):.3f}{stars(st.get('p_GE', 1))}",
            'Survival %': f"{st.get('survival_rate', 0):.1f}%",
            'Signs OK': '✓' if (st.get('rho_AE', 1) < 0 and
                                st.get('rho_GA', -1) > 0 and
                                st.get('rho_GE', 1) < 0) else '✗'
        }
        rows.append(row)

    df = pd.DataFrame(rows)
    print("\n📋 Robustness Table:")
    print(df.to_string(index=False))

    # Save
    df.to_csv(STATS_DIR / 'robustness_table.csv', index=False)
    print(f"   ✅ robustness_table.csv")

    return df


def main():
    print("="*70)
    print("🐅 TIME-SERIES ROBUSTNESS CHECK")
    print("Verifying key relationships across t = 2023, 2024, 2025")
    print("="*70)

    # Load data
    data_dict = load_timeseries_data()

    # Compute statistics
    print("\n📊 Computing statistics...")
    stats_dict = compute_robustness_stats(data_dict)

    # Save statistics
    stats_json = {str(k): {kk: (float(vv) if isinstance(vv, (np.floating, np.integer)) else vv)
                           for kk, vv in v.items()}
                  for k, v in stats_dict.items()}
    with open(STATS_DIR / 'robustness_statistics.json', 'w') as f:
        json.dump(stats_json, f, indent=2)
    print("   ✅ robustness_statistics.json")

    # Generate plots
    print("\n📈 Generating robustness plots...")
    plot_robustness_panel(data_dict, stats_dict)
    plot_coefficient_evolution(stats_dict)

    # Create table
    table = create_robustness_table(stats_dict)

    # Summary
    print("\n" + "="*70)
    print("✅ ROBUSTNESS CHECK COMPLETE")
    print("="*70)

    print("\n📊 KEY FINDINGS:")
    all_consistent = True
    for t in [2023, 2024, 2025]:
        st = stats_dict[t]
        ae_ok = st.get('rho_AE', 1) < 0
        ga_ok = st.get('rho_GA', -1) > 0
        ge_ok = st.get('rho_GE', 1) < 0

        status = "✓" if (ae_ok and ga_ok and ge_ok) else "✗"
        all_consistent = all_consistent and (ae_ok and ga_ok and ge_ok)

        print(f"   t={t}: ρ(A,E)={st.get('rho_AE', np.nan):.3f} {'✓' if ae_ok else '✗'}, "
              f"ρ(G,A)={st.get('rho_GA', np.nan):.3f} {'✓' if ga_ok else '✗'}, "
              f"ρ(G,E)={st.get('rho_GE', np.nan):.3f} {'✓' if ge_ok else '✗'} → {status}")

    print(f"\n{'🎉 ALL SIGNS CONSISTENT ACROSS TIME!' if all_consistent else '⚠️ SOME INCONSISTENCIES FOUND'}")

    return data_dict, stats_dict, table


if __name__ == "__main__":
    data_dict, stats_dict, table = main()
