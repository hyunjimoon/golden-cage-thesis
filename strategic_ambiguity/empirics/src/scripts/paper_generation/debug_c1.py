
import pandas as pd
import numpy as np
from scipy import stats
from pathlib import Path

# Paths
ROOT = Path("/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics")
DATA_PATH = ROOT / "data/processed/vagueness_timeseries.parquet"
COMPANY_PATH = ROOT / "data/processed/Company20251101.parquet"

def load_data():
    print("📂 Loading data...")
    panel = pd.read_parquet(DATA_PATH)
    
    company_cols = ['CompanyID', 'TotalRaised', 'BusinessStatus', 'LastFinancingDealType']
    company_df = pd.read_parquet(COMPANY_PATH, columns=company_cols)
    company_df.columns = ['company_id', 'TotalRaised_2025', 'BusinessStatus', 'LastFinancingDealType']
    company_df['company_id'] = company_df['company_id'].astype(str)

    df_0 = panel[panel['year'] == 2021][['company_id', 'V', 'first_financing_size']].copy()
    df_0.columns = ['company_id', 'V', 'E']
    df_0['company_id'] = df_0['company_id'].astype(str)

    df_T = panel[panel['year'] == 2025][['company_id', 'V', 'total_delta_V']].copy()
    df_T.columns = ['company_id', 'V_T', 'D']
    df_T['company_id'] = df_T['company_id'].astype(str)

    cross = df_0.merge(df_T, on='company_id', how='inner')
    cross = cross.merge(company_df, on='company_id', how='left')

    cross['A'] = cross['D'].abs()
    cross['E_log'] = np.log10(cross['E'].clip(lower=0.01))
    
    cross['F_t'] = cross['TotalRaised_2025'] - cross['E']
    cross['F_t'] = cross['F_t'].clip(lower=0)
    cross['G'] = cross['F_t'] / (cross['E'] + 0.001)
    g_cap = cross['G'].quantile(0.99)
    cross['G'] = cross['G'].clip(upper=g_cap)

    # Filter valid
    valid = cross[['E', 'A', 'G']].notna().all(axis=1) & (cross['E'] > 0) & np.isfinite(cross['G'])
    return cross[valid].copy()

def analyze():
    df = load_data()
    print(f"Data Loaded: N={len(df)}")
    
    print("\n--- Variable A Distribution ---")
    print(df['A'].describe())
    
    print("\n--- Panel A (A vs E) Analysis ---")
    # Correlation
    slope, intercept, r, p, se = stats.linregress(df['E_log'], df['A'])
    print(f"Correlation (A, E_log): r={r:.4f}, p={p:.4f}, slope={slope:.4f}")
    
    # Deciles
    df['E_bin'] = pd.qcut(df['E_log'], 10, labels=False, duplicates='drop')
    binned_A = df.groupby('E_bin').agg({'E_log': 'median', 'A': ['mean', 'median', 'min', 'max']})
    print("\nBinned by E (Top/Bottom 3):")
    print(binned_A.head(3))
    print(binned_A.tail(3))
    
    print("\n--- Panel B (G vs A) Analysis ---")
    df['A_bin'] = pd.qcut(df['A'], 10, labels=False, duplicates='drop')
    binned_B = df.groupby('A_bin').agg({'A': ['mean', 'median', 'min', 'max'], 'G': 'mean'})
    print("\nBinned by A (Top/Bottom 3):")
    print(binned_B.head(3))
    print(binned_B.tail(3))

if __name__ == "__main__":
    analyze()
