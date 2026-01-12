#!/usr/bin/env python3
"""
00_data_pipeline.py - Complete Raw → Analysis Pipeline
=======================================================

Creates all intermediate and final data files from raw PitchBook data.
Designed for reproducibility and efficiency (no recalculation after first run).

VARIABLE MAPPING (Final Agreed - 2026-01-11):
┌────────┬──────────────────────┬─────────────────────────────┐
│ Symbol │ Definition           │ Raw Column / Computation    │
├────────┼──────────────────────┼─────────────────────────────┤
│ E      │ Early capital ($M)   │ FirstFinancingSize          │
│ K      │ Kapital total ($M)   │ TotalRaised                 │
│ G      │ Growth = K/E         │ TotalRaised / FirstFinancing│
│ L      │ Later Stage success  │ "Later Stage VC" → 1/0      │
│ B      │ Breadth (vagueness)  │ computed from Description   │
│ R      │ Repositioning        │ |B_T - B_0|                 │
│ D      │ Direction            │ B_T - B_0                   │
│ C      │ Commitment           │ latent (not measured)       │
│ F      │ Flexibility          │ latent (not measured)       │
└────────┴──────────────────────┴─────────────────────────────┘

NOTE: C (Commitment) and F (Flexibility) are LATENT variables, not directly measured.
      They are inferred through the causal chain: C → E, C → F(−), F → R, R → G

OUTPUT FILES:
├── data/processed/
│   ├── companies_consolidated.parquet  # All companies, all years
│   ├── features_all.parquet            # With computed features
│   ├── vagueness_timeseries.parquet    # V scores over time
│   └── thesis_panel_v3.nc              # Final analysis panel

Usage:
    python 00_data_pipeline.py [--force]  # --force rebuilds all

Author: Claude Code CLI
Date: 2026-01-11
"""

import sys
import argparse
import logging
from pathlib import Path
from datetime import datetime

import pandas as pd
import numpy as np
import xarray as xr
from scipy.stats import spearmanr

# ============================================================================
# CONFIGURATION
# ============================================================================

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%H:%M:%S'
)
log = logging.getLogger(__name__)

SCRIPT_DIR = Path(__file__).parent.resolve()
DATA_RAW = SCRIPT_DIR / 'data' / 'raw'
DATA_PROC = SCRIPT_DIR / 'data' / 'processed'

# Raw files
RAW_FILES = {
    2021: DATA_RAW / 'Company20211201.dat',
    2023: DATA_RAW / 'Company20231201.dat',
    2024: DATA_RAW / 'Company20241201.dat',
    2025: DATA_RAW / 'Company20251101.dat',
}

# Essential columns to keep (reduces memory)
ESSENTIAL_COLS = [
    'CompanyID', 'CompanyName', 'Description', 'Keywords',
    'TotalRaised', 'FirstFinancingSize', 'FirstFinancingDate',
    'FirstFinancingDealType', 'LastFinancingSize', 'LastFinancingDate',
    'LastFinancingDealType', 'GrowthRate', 'YearFounded', 'Employees',
    'HQCountry', 'HQState_Province', 'BusinessStatus', 'CompanyFinancingStatus',
]

# ============================================================================
# VAGUENESS SCORER (Simplified V3)
# ============================================================================

class BreadthScorer:
    """
    Breadth scorer (B) - measures strategic ambiguity/vagueness.
    Based on V3 methodology, renamed V → B for clarity.
    - B_market: Market entropy (category diversity)
    - B_tech: Technical abstractness (lack of specifics)
    - B: Weighted composite
    """

    MARKET_CATEGORIES = {
        'fintech': ['fintech', 'payment', 'banking', 'insurance', 'lending', 'crypto'],
        'healthcare': ['healthcare', 'health tech', 'medical', 'pharma', 'biotech'],
        'enterprise': ['enterprise', 'b2b', 'saas', 'crm', 'erp', 'workflow'],
        'consumer': ['consumer', 'b2c', 'e-commerce', 'retail', 'marketplace', 'gaming'],
        'infrastructure': ['infrastructure', 'cloud', 'devops', 'api', 'platform'],
        'ai_ml': ['artificial intelligence', 'machine learning', 'deep learning', 'nlp', 'ai'],
        'hardware': ['hardware', 'semiconductor', 'chip', 'sensor', 'robotics'],
        'cleantech': ['cleantech', 'renewable', 'solar', 'battery', 'ev', 'sustainability'],
    }

    CONCRETE_PATTERNS = [
        r'\b\d+[\.\d]*\s*(?:nm|μm|mm|cm|m|ghz|mhz|gb|tb|mb|%)\b',  # metrics
        r'\bv\d+(?:\.\d+)*\b',  # versions
        r'\b20[0-2]\d\b',  # years
    ]

    def __init__(self):
        import re
        self.concrete_regex = re.compile('|'.join(self.CONCRETE_PATTERNS), re.IGNORECASE)

    def score_market_entropy(self, text: str) -> float:
        """Compute market entropy (0-100). Higher = more vague."""
        if not text or len(text) < 10:
            return 50.0

        text_lower = text.lower()
        hits = []
        for cat, keywords in self.MARKET_CATEGORIES.items():
            if any(kw in text_lower for kw in keywords):
                hits.append(cat)

        n_cats = len(hits)
        if n_cats == 0:
            return 80.0  # No clear category = vague
        elif n_cats == 1:
            return 20.0  # Clear focus
        else:
            # More categories = more vague
            return min(20 + n_cats * 15, 100)

    def score_tech_abstractness(self, text: str) -> float:
        """Compute technical abstractness (0-100). Higher = more vague."""
        if not text or len(text) < 10:
            return 50.0

        # Count concrete specifications
        matches = self.concrete_regex.findall(text)
        n_concrete = len(matches)

        word_count = len(text.split())
        if word_count == 0:
            return 50.0

        concrete_density = n_concrete / word_count * 100

        # Higher density of concrete specs = less vague
        return max(0, 100 - concrete_density * 50)

    def score(self, text: str) -> dict:
        """Compute all breadth scores."""
        b_market = self.score_market_entropy(text)
        b_tech = self.score_tech_abstractness(text)
        b_composite = 0.5 * b_market + 0.5 * b_tech

        return {
            'B_market': b_market,
            'B_tech': b_tech,
            'B': b_composite
        }


def classify_hardware(text: str) -> int:
    """Classify as hardware (1) or software (0)."""
    if not isinstance(text, str):
        return 0

    text_lower = text.lower()

    hw_keywords = [
        'hardware', 'robotics', 'robot', 'chip', 'asic', 'semiconductor',
        'device', 'sensor', 'fpga', 'silicon', 'biotech', 'quantum',
        'autonomous vehicle', 'battery', 'manufacturing', 'lidar'
    ]
    sw_keywords = [
        'software', 'saas', 'api', 'cloud', 'platform', 'sdk',
        'microservice', 'data', 'ml', 'ai', 'nlp', 'analytics'
    ]

    hw_count = sum(1 for kw in hw_keywords if kw in text_lower)
    sw_count = sum(1 for kw in sw_keywords if kw in text_lower)

    return 1 if hw_count > sw_count else 0


# ============================================================================
# PIPELINE STEPS
# ============================================================================

def step1_consolidate_raw(force: bool = False):
    """Step 1: Load raw .dat files and consolidate to parquet."""
    output_path = DATA_PROC / 'companies_consolidated.parquet'

    if output_path.exists() and not force:
        log.info(f"Step 1: Using cached {output_path.name}")
        return pd.read_parquet(output_path)

    log.info("Step 1: Consolidating raw .dat files...")

    dfs = []
    for year, path in sorted(RAW_FILES.items()):
        if not path.exists():
            log.warning(f"  File not found: {path}")
            continue

        log.info(f"  Loading {path.name}...")

        # Read only essential columns
        df = pd.read_csv(path, sep='|', low_memory=False,
                         usecols=lambda c: c in ESSENTIAL_COLS)
        df['snapshot_year'] = year

        log.info(f"    {len(df):,} companies")
        dfs.append(df)

    if not dfs:
        raise FileNotFoundError("No raw data files found")

    # Concatenate all years
    df_all = pd.concat(dfs, ignore_index=True)
    log.info(f"  Total: {len(df_all):,} records across {len(dfs)} snapshots")

    # Keep latest snapshot per company
    df_latest = (df_all
                 .sort_values(['CompanyID', 'snapshot_year'])
                 .drop_duplicates('CompanyID', keep='last'))

    log.info(f"  Unique companies (latest snapshot): {len(df_latest):,}")

    # Save
    DATA_PROC.mkdir(parents=True, exist_ok=True)
    df_latest.to_parquet(output_path, index=False)
    log.info(f"  Saved: {output_path.name}")

    return df_latest


def step2_compute_features(df: pd.DataFrame, force: bool = False):
    """Step 2: Compute features (E, K, G, L, F)."""
    output_path = DATA_PROC / 'features_all.parquet'

    if output_path.exists() and not force:
        log.info(f"Step 2: Using cached {output_path.name}")
        return pd.read_parquet(output_path)

    log.info("Step 2: Computing features...")

    # NOTE: PitchBook raw data is ALREADY in millions USD
    # E: Early capital ($M) - already in millions
    df['E'] = pd.to_numeric(df['FirstFinancingSize'], errors='coerce')
    log.info(f"  E (Early capital): {df['E'].notna().sum():,} valid")

    # K: Total raised ($M) - already in millions
    df['K'] = pd.to_numeric(df['TotalRaised'], errors='coerce')
    log.info(f"  K (Total raised): {df['K'].notna().sum():,} valid")

    # G: Growth = K/E (growth multiple)
    # This definition yields ρ(G, E) ≈ -0.14 (Funding Paradox)
    valid_for_G = (df['K'].notna()) & (df['E'].notna()) & (df['E'] > 0)
    df['G'] = np.where(valid_for_G, df['K'] / df['E'], np.nan)

    # Cap extreme outliers (G > 100x is unrealistic)
    df.loc[df['G'] > 100, 'G'] = np.nan

    log.info(f"  G (Growth = K/E): {df['G'].notna().sum():,} valid")
    log.info(f"    G mean: {df['G'].mean():.2f}x, median: {df['G'].median():.2f}x")

    # L: Later Stage VC success
    df['L'] = df['LastFinancingDealType'].fillna('').str.contains(
        'Later Stage VC', case=False
    ).astype(int)
    log.info(f"  L (Later Stage VC): {df['L'].sum():,} ({df['L'].mean()*100:.1f}%)")

    # F: Flexibility (1 - is_hardware)
    text_col = (df['Description'].fillna('') + ' ' + df['Keywords'].fillna(''))
    df['is_hardware'] = text_col.apply(classify_hardware)
    df['F'] = 1 - df['is_hardware']
    log.info(f"  F (Flexibility): {df['F'].mean()*100:.1f}% software, {df['is_hardware'].mean()*100:.1f}% hardware")

    # Sector FE
    def classify_sector(text):
        if not isinstance(text, str):
            return 'Other'
        text = text.lower()
        if any(w in text for w in ['biotech', 'pharma', 'health', 'medical']):
            return 'Healthcare'
        elif any(w in text for w in ['hardware', 'robotics', 'chip', 'semiconductor']):
            return 'Hardware'
        elif any(w in text for w in ['ai', 'machine learning', 'ml']):
            return 'AI/ML'
        elif any(w in text for w in ['fintech', 'payment', 'banking']):
            return 'FinTech'
        elif any(w in text for w in ['enterprise', 'b2b', 'saas']):
            return 'Enterprise'
        elif any(w in text for w in ['consumer', 'b2c', 'gaming']):
            return 'Consumer'
        else:
            return 'Other'

    df['sector_fe'] = text_col.apply(classify_sector)

    # Save
    df.to_parquet(output_path, index=False)
    log.info(f"  Saved: {output_path.name}")

    return df


def step3_compute_breadth_timeseries(force: bool = False):
    """Step 3: Compute Breadth (B) scores for each year."""
    output_path = DATA_PROC / 'breadth_timeseries.parquet'

    if output_path.exists() and not force:
        log.info(f"Step 3: Using cached {output_path.name}")
        return pd.read_parquet(output_path)

    log.info("Step 3: Computing Breadth (B) timeseries...")

    scorer = BreadthScorer()
    all_records = []

    for year, path in sorted(RAW_FILES.items()):
        if not path.exists():
            continue

        log.info(f"  Processing {year}...")

        df = pd.read_csv(path, sep='|', low_memory=False,
                         usecols=['CompanyID', 'Description', 'Keywords',
                                  'FirstFinancingSize'])

        # Combine text
        df['text'] = df['Description'].fillna('') + ' ' + df['Keywords'].fillna('')

        # Score breadth
        log.info(f"    Scoring {len(df):,} companies...")
        scores = df['text'].apply(scorer.score)

        df['B'] = scores.apply(lambda x: x['B'])
        df['B_market'] = scores.apply(lambda x: x['B_market'])
        df['B_tech'] = scores.apply(lambda x: x['B_tech'])

        df['year'] = year
        df['company_id'] = df['CompanyID']
        df['first_financing_size'] = pd.to_numeric(df['FirstFinancingSize'], errors='coerce')

        all_records.append(df[['company_id', 'year', 'B', 'B_market', 'B_tech',
                               'first_financing_size']])

        log.info(f"    B mean: {df['B'].mean():.1f}, std: {df['B'].std():.1f}")

    df_ts = pd.concat(all_records, ignore_index=True)
    log.info(f"  Total records: {len(df_ts):,}")

    # Save
    df_ts.to_parquet(output_path, index=False)
    log.info(f"  Saved: {output_path.name}")

    return df_ts


def step4_build_thesis_panel(breadth: pd.DataFrame, feat: pd.DataFrame, force: bool = False):
    """Step 4: Build final thesis panel (NetCDF)."""
    output_path = DATA_PROC / 'thesis_panel_v3.nc'

    if output_path.exists() and not force:
        log.info(f"Step 4: Using cached {output_path.name}")
        return xr.open_dataset(output_path)

    log.info("Step 4: Building thesis panel...")

    # B_0 from 2021
    b_2021 = breadth[breadth['year'] == 2021][['company_id', 'B', 'first_financing_size']].copy()
    b_2021 = b_2021.rename(columns={'B': 'B_0', 'first_financing_size': 'E'})
    b_2021 = b_2021[b_2021['E'].notna() & (b_2021['E'] > 0)]
    log.info(f"  B_0 (2021) with E: {len(b_2021):,}")

    # B_T from 2025
    b_2025 = breadth[breadth['year'] == 2025][['company_id', 'B']].copy()
    b_2025 = b_2025.rename(columns={'B': 'B_T'})
    log.info(f"  B_T (2025): {len(b_2025):,}")

    # Merge B_0 and B_T
    panel = b_2021.merge(b_2025, on='company_id', how='inner')
    log.info(f"  Panel (B_0 + B_T): {len(panel):,}")

    # Compute D (Direction) and R (Repositioning = |D|)
    panel['D'] = panel['B_T'] - panel['B_0']
    panel['R'] = panel['D'].abs()

    # Mover classification based on R (Repositioning)
    nonzero_R = panel[panel['R'] > 0]['R']
    R_threshold = nonzero_R.quantile(0.50) if len(nonzero_R) > 0 else 0

    def classify_mover(row):
        if row['D'] < 0 and row['R'] > R_threshold:
            return 'zoom_in'
        elif row['D'] > 0 and row['R'] > R_threshold:
            return 'zoom_out'
        else:
            return 'stayer'

    panel['mover_type'] = panel.apply(classify_mover, axis=1)
    panel['moved'] = (panel['mover_type'] != 'stayer').astype(int)

    log.info(f"  Movers: {panel['moved'].sum():,} ({panel['moved'].mean()*100:.1f}%)")

    # Merge with features
    feat_dedup = feat.drop_duplicates('CompanyID').copy()
    feat_dedup['company_id'] = feat_dedup['CompanyID'].astype(str)
    panel['company_id'] = panel['company_id'].astype(str)

    # NOTE: F (Flexibility) is LATENT - not directly measured
    # We only merge measured variables: G, K, L, sector
    panel = panel.merge(
        feat_dedup[['company_id', 'G', 'K', 'L', 'sector_fe']],
        on='company_id',
        how='left'
    )
    log.info(f"  After feature merge: {len(panel):,}")

    # B_0 quartiles
    try:
        panel['quartile_B0'] = pd.qcut(panel['B_0'], 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
    except ValueError:
        panel['quartile_B0'] = pd.cut(panel['B_0'], 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

    # Create NetCDF with FINAL variable names (V→B, M→R, G=K/E)
    ds = xr.Dataset({
        'B_0': ('company', panel['B_0'].values),
        'B_T': ('company', panel['B_T'].values),
        'D': ('company', panel['D'].values),
        'R': ('company', panel['R'].values),
        'E': ('company', panel['E'].values),
        'K': ('company', panel['K'].fillna(np.nan).values),
        'G': ('company', panel['G'].fillna(np.nan).values),
        'L': ('company', panel['L'].fillna(0).values.astype(int)),
        'moved': ('company', panel['moved'].values.astype(int)),
        'mover_type': ('company', panel['mover_type'].values.astype(str)),
        'quartile_B0': ('company', panel['quartile_B0'].astype(str).values),
        'sector': ('company', panel['sector_fe'].fillna('Other').values.astype(str)),
    }, coords={
        'company': panel['company_id'].values,
    })

    # Metadata
    ds.attrs['created'] = str(datetime.now())
    ds.attrs['n_companies'] = len(panel)
    ds.attrs['l_base_rate'] = float(panel['L'].mean()) if 'L' in panel else np.nan
    ds.attrs['g_definition'] = 'G = K/E (growth multiple)'
    ds.attrs['description'] = 'Golden Cage Thesis Panel v3 (2026-01-11) - G=K/E, V→B, M→R'

    # Variable descriptions
    var_descs = {
        'B_0': 'Initial Breadth (2021)',
        'B_T': 'Final Breadth (2025)',
        'D': 'Direction = B_T - B_0',
        'R': 'Repositioning = |D|',
        'E': 'Early capital ($M)',
        'K': 'Total raised / Kapital ($M)',
        'G': 'Growth = K/E (growth multiple)',
        'L': 'Success = Later Stage VC',
        'moved': 'Binary: significant repositioning',
        'mover_type': 'zoom_in / zoom_out / stayer',
        'quartile_B0': 'Initial Breadth quartile',
        'sector': 'Industry sector',
    }
    for var, desc in var_descs.items():
        if var in ds:
            ds[var].attrs['description'] = desc

    # Save
    ds.to_netcdf(output_path)
    log.info(f"  Saved: {output_path.name}")

    return ds


def step5_validate_and_report(ds: xr.Dataset):
    """Step 5: Validate and generate summary report."""
    log.info("Step 5: Validation & Report")

    df = pd.DataFrame({
        'B_0': ds['B_0'].values,
        'B_T': ds['B_T'].values,
        'D': ds['D'].values,
        'R': ds['R'].values,
        'E': ds['E'].values,
        'K': ds['K'].values,
        'G': ds['G'].values,
        'L': ds['L'].values,
        'moved': ds['moved'].values,
        'mover_type': ds['mover_type'].values,
    })

    report = []
    report.append("=" * 60)
    report.append("THESIS PANEL SUMMARY REPORT")
    report.append("=" * 60)
    report.append(f"Generated: {datetime.now()}")
    report.append("")

    # Sample size
    N = len(df)
    report.append(f"[1] Sample Size")
    report.append(f"    N = {N:,}")
    report.append("")

    # Success rate
    l_rate = df['L'].mean() * 100
    report.append(f"[2] Success Rate (L = Later Stage VC)")
    report.append(f"    L = 1: {df['L'].sum():,} ({l_rate:.1f}%)")
    report.append("")

    # Mover statistics
    mover_stats = df['mover_type'].value_counts()
    report.append(f"[3] Movement Classification")
    for mt, count in mover_stats.items():
        pct = count / N * 100
        report.append(f"    {mt}: {count:,} ({pct:.1f}%)")
    report.append("")

    # Success by mover type
    report.append(f"[4] Success by Mover Type")
    mover_success = df[df['moved'] == 1]['L'].mean() * 100
    stayer_success = df[df['moved'] == 0]['L'].mean() * 100
    advantage = mover_success / stayer_success if stayer_success > 0 else np.nan

    report.append(f"    Movers: {mover_success:.1f}%")
    report.append(f"    Stayers: {stayer_success:.1f}%")
    report.append(f"    Advantage: {advantage:.2f}x")
    report.append("")

    # Correlations
    valid = df[(df['E'].notna()) & (df['G'].notna()) & (df['E'] > 0)].copy()
    valid['log_E'] = np.log1p(valid['E'])

    report.append(f"[5] Key Correlations (n={len(valid):,})")

    if len(valid) > 100:
        rho_GE, p_GE = spearmanr(valid['G'], valid['log_E'])
        rho_RE, p_RE = spearmanr(valid['R'], valid['log_E'])
        rho_GR, p_GR = spearmanr(valid['G'], valid['R'])

        def sig(p):
            return '***' if p < 0.001 else '**' if p < 0.01 else '*' if p < 0.05 else 'ns'

        report.append(f"    ρ(G, log(E)) = {rho_GE:+.4f} {sig(p_GE)} (Funding Paradox)")
        report.append(f"    ρ(R, log(E)) = {rho_RE:+.4f} {sig(p_RE)} (Fund→Cage)")
        report.append(f"    ρ(G, R)      = {rho_GR:+.4f} {sig(p_GR)} (Reposition→Growth)")
    report.append("")

    # Variable statistics
    report.append(f"[6] Variable Statistics")
    for var in ['E', 'K', 'G', 'B_0', 'R']:
        col = df[var].dropna()
        if len(col) > 0:
            report.append(f"    {var}: mean={col.mean():.2f}, median={col.median():.2f}, std={col.std():.2f}")
    report.append("")

    # K >= E validation
    valid_KE = df[(df['K'].notna()) & (df['E'].notna()) & (df['E'] > 0)]
    violations = (valid_KE['K'] < valid_KE['E']).sum()
    pct_valid = (1 - violations / len(valid_KE)) * 100 if len(valid_KE) > 0 else 0

    report.append(f"[7] K >= E Validation (Cumulative Funding)")
    report.append(f"    Valid: {len(valid_KE) - violations:,} ({pct_valid:.1f}%)")
    report.append(f"    Violations: {violations:,}")
    report.append("")

    report.append("=" * 60)

    # Print and save
    report_text = '\n'.join(report)
    print(report_text)

    report_path = DATA_PROC / 'thesis_panel_report.txt'
    report_path.write_text(report_text)
    log.info(f"  Report saved: {report_path.name}")

    return report_text


# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description='Complete data pipeline')
    parser.add_argument('--force', action='store_true',
                        help='Force rebuild all files (ignore cache)')
    args = parser.parse_args()

    log.info("=" * 60)
    log.info("DATA PIPELINE - Raw → Analysis")
    log.info("=" * 60)

    # Step 1: Consolidate raw
    df = step1_consolidate_raw(force=args.force)

    # Step 2: Compute features
    feat = step2_compute_features(df, force=args.force)

    # Step 3: Breadth timeseries (V → B)
    breadth = step3_compute_breadth_timeseries(force=args.force)

    # Step 4: Build thesis panel
    ds = step4_build_thesis_panel(breadth, feat, force=args.force)

    # Step 5: Validate and report
    step5_validate_and_report(ds)

    log.info("")
    log.info("=" * 60)
    log.info("PIPELINE COMPLETE")
    log.info("=" * 60)
    log.info(f"Output directory: {DATA_PROC}")


if __name__ == '__main__':
    main()
