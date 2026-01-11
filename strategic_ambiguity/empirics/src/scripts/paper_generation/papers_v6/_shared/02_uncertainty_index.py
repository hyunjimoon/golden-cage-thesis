"""
02_uncertainty_index.py
=======================
Task 1: Quantifying Market Uncertainty (U)

Uncertainty Index = f(B, M, T)
- B: Baseline Vagueness (Strategic Ambiguity score)
- M: Market Immaturity (inverse of company age at funding)
- T: Pivot Rate (frequency of repositioning events)

Author: cli1 (Charlie)
Date: 2026-01-11
Thesis Module: CFR (¶7-15), P (¶25-27)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent.parent.parent.parent.parent.parent  # empirics/
DATA_DIR = BASE_DIR / "data" / "processed"
OUTPUT_DIR = Path(__file__).parent / "data"
OUTPUT_DIR.mkdir(exist_ok=True)


def extract_industry(keywords: str) -> str:
    """Extract industry category from Keywords string."""
    if pd.isna(keywords):
        return 'Other'
    keywords_lower = str(keywords).lower()

    industry_mapping = [
        (['software', 'saas', 'tech', 'ai', 'machine learning'], 'Software/AI'),
        (['biotech', 'pharma', 'health', 'medical', 'drug'], 'Healthcare/Biotech'),
        (['fintech', 'financial', 'banking', 'payment'], 'Fintech'),
        (['e-commerce', 'retail', 'consumer'], 'Consumer/Retail'),
        (['transport', 'mobility', 'logistics', 'automotive'], 'Transportation'),
        (['energy', 'cleantech', 'sustainability', 'climate'], 'CleanTech/Energy'),
        (['real estate', 'property'], 'Real Estate'),
        (['manufacturing', 'industrial'], 'Manufacturing'),
    ]

    for keywords_list, category in industry_mapping:
        if any(k in keywords_lower for k in keywords_list):
            return category
    return 'Other'


def normalize_0_1(x: pd.Series) -> pd.Series:
    """Normalize series to 0-1 scale."""
    x_min, x_max = x.min(), x.max()
    if x_max == x_min:
        return pd.Series(0.5, index=x.index)
    return (x - x_min) / (x_max - x_min)


def calculate_uncertainty_index(
    vagueness_path: Path = DATA_DIR / "vagueness_timeseries.parquet",
    companies_path: Path = DATA_DIR / "consolidated_companies.parquet",
    weights: tuple = (1.0, 1.0, 1.0)
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Calculate Uncertainty Index for ventures.

    Parameters
    ----------
    vagueness_path : Path to vagueness timeseries data
    companies_path : Path to consolidated companies data
    weights : (w_B, w_M, w_T) weights for B, M, T components

    Returns
    -------
    df : Company-level dataframe with Uncertainty Index
    industry_summary : Industry-level summary statistics
    """
    print("=" * 60)
    print("Task 1: Quantifying Market Uncertainty (U)")
    print("=" * 60)

    # Load data
    vagueness = pd.read_parquet(vagueness_path)
    companies = pd.read_parquet(companies_path)

    print(f"\n[1] Data loaded:")
    print(f"    Vagueness records: {len(vagueness):,}")
    print(f"    Companies: {len(companies):,}")

    # Merge data
    df = vagueness.merge(
        companies[['CompanyID', 'Keywords', 'YearFounded', 'TotalRaised',
                   'BusinessStatus', 'HQGlobalRegion', 'FirstFinancingDate']],
        left_on='company_id',
        right_on='CompanyID',
        how='left'
    )
    print(f"    Merged records: {len(df):,}")

    # Step 1: Create Industry_Category
    df['Industry_Category'] = df['Keywords'].apply(extract_industry)

    print(f"\n[2] Industry distribution:")
    print(df['Industry_Category'].value_counts())

    # B (Baseline Vagueness)
    df['B'] = df['V']

    # Company Age at first financing
    df['Company_Age'] = pd.to_datetime(df['FirstFinancingDate']).dt.year - df['YearFounded']

    # Step 2: Calculate industry-level uncertainty components
    print("\n" + "=" * 60)
    print("Step 1-2: Data Engineering & Synthesis")
    print("=" * 60)

    industry_stats = df.groupby('Industry_Category').agg({
        'B': lambda x: x.std() / x.mean() if x.mean() != 0 else 0,  # B_volatility
        'Company_Age': 'mean',  # M_immaturity (will invert later)
        'total_delta_V': lambda x: (x != 0).mean()  # T_pivot_rate
    }).reset_index()
    industry_stats.columns = ['Industry_Category', 'B_volatility', 'M_immaturity', 'T_pivot_rate']

    # Normalize components
    industry_stats['B_norm'] = normalize_0_1(industry_stats['B_volatility'])
    industry_stats['M_norm'] = normalize_0_1(1 / (industry_stats['M_immaturity'] + 1))  # Inverse
    industry_stats['T_norm'] = normalize_0_1(industry_stats['T_pivot_rate'])

    # Calculate Uncertainty Index with weights
    w_B, w_M, w_T = weights
    industry_stats['Uncertainty_Index'] = (
        w_B * industry_stats['B_norm'] +
        w_M * industry_stats['M_norm'] +
        w_T * industry_stats['T_norm']
    ) / (w_B + w_M + w_T)

    print("\n[3] Uncertainty Index by Industry:")
    print(industry_stats[['Industry_Category', 'B_norm', 'M_norm', 'T_norm', 'Uncertainty_Index']]
          .sort_values('Uncertainty_Index', ascending=False).to_string())

    # Merge Uncertainty_Index back to main dataframe
    df = df.merge(
        industry_stats[['Industry_Category', 'Uncertainty_Index']],
        on='Industry_Category',
        how='left'
    )

    # Step 3: Segmentation
    print("\n" + "=" * 60)
    print("Step 3: Segmentation & Validation")
    print("=" * 60)

    # Create tiers using cut instead of qcut (avoids duplicate bin edges)
    df['Uncertainty_Tier'] = pd.cut(
        df['Uncertainty_Index'],
        bins=[0, 0.33, 0.66, 1.0],
        labels=['Low', 'Mid', 'High'],
        include_lowest=True
    )

    print("\n[4] Tier distribution:")
    print(df['Uncertainty_Tier'].value_counts())

    # Validation
    tier_validation = df.groupby('Uncertainty_Tier', observed=True).agg({
        'V': ['mean', 'std', 'count'],
        'total_delta_V': ['mean', 'std']
    }).reset_index()
    tier_validation.columns = ['Tier', 'V_mean', 'V_std', 'Count', 'DeltaV_mean', 'DeltaV_std']

    print("\n[5] Validation - V variance by Tier (High U should have higher V variance):")
    print(tier_validation.to_string())

    return df, industry_stats


def create_visualization(df: pd.DataFrame, industry_stats: pd.DataFrame, output_dir: Path):
    """Create visualization of Uncertainty Index distribution."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Plot 1: Industry Uncertainty Index (bar chart)
    ax1 = axes[0]
    sorted_stats = industry_stats.sort_values('Uncertainty_Index', ascending=True)
    colors = plt.cm.RdYlGn_r(sorted_stats['Uncertainty_Index'])
    ax1.barh(sorted_stats['Industry_Category'], sorted_stats['Uncertainty_Index'], color=colors)
    ax1.set_xlabel('Uncertainty Index (U)')
    ax1.set_title('Uncertainty Index by Industry')
    ax1.axvline(x=0.5, color='gray', linestyle='--', alpha=0.5, label='Mid threshold')

    # Plot 2: Uncertainty Tier Distribution
    ax2 = axes[1]
    tier_counts = df['Uncertainty_Tier'].value_counts()
    tier_colors = {'Low': 'green', 'Mid': 'gold', 'High': 'red'}
    ax2.pie(tier_counts, labels=tier_counts.index, autopct='%1.1f%%',
            colors=[tier_colors.get(t, 'gray') for t in tier_counts.index])
    ax2.set_title('Venture Distribution by Uncertainty Tier')

    plt.tight_layout()
    output_path = output_dir / "uncertainty_index_distribution.png"
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\n[6] Visualization saved: {output_path}")


def main():
    """Main execution function."""
    # Calculate Uncertainty Index
    df, industry_stats = calculate_uncertainty_index()

    # Create visualization
    create_visualization(df, industry_stats, OUTPUT_DIR)

    # Save outputs
    print("\n" + "=" * 60)
    print("OUTPUT: Save Results")
    print("=" * 60)

    # Summary table
    print("\n--- Top 5 Industries by Uncertainty ---")
    print(industry_stats.nlargest(5, 'Uncertainty_Index')[
        ['Industry_Category', 'B_volatility', 'M_immaturity', 'T_pivot_rate', 'Uncertainty_Index']
    ].to_string())

    print("\n--- Bottom 5 Industries by Uncertainty ---")
    print(industry_stats.nsmallest(5, 'Uncertainty_Index')[
        ['Industry_Category', 'B_volatility', 'M_immaturity', 'T_pivot_rate', 'Uncertainty_Index']
    ].to_string())

    # Save CSV
    output_cols = ['company_id', 'year', 'V', 'delta_V', 'company_name',
                   'Industry_Category', 'YearFounded', 'B', 'Uncertainty_Index', 'Uncertainty_Tier']
    df_output = df[[c for c in output_cols if c in df.columns]].copy()

    csv_path = OUTPUT_DIR / "venture_data_with_uncertainty.csv"
    df_output.to_csv(csv_path, index=False)
    print(f"\n[7] CSV saved: {csv_path}")
    print(f"    Records: {len(df_output):,}")

    # Save industry summary
    summary_path = OUTPUT_DIR / "industry_uncertainty_summary.csv"
    industry_stats.to_csv(summary_path, index=False)
    print(f"    Industry summary: {summary_path}")

    return df, industry_stats


if __name__ == "__main__":
    df, industry_stats = main()
