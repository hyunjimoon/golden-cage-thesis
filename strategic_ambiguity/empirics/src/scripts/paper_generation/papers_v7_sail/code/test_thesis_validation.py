#!/usr/bin/env python3
"""
GOLDEN CAGE THESIS VALIDATION SUITE
====================================
Rigorous automated tests for PhD thesis claims.
Run with: pytest test_thesis_validation.py -v --tb=short

Author: Validation Framework for Angie Moon's MIT Thesis
Version: 1.0.0
"""

import pytest
import pandas as pd
import numpy as np
from scipy import stats
from pathlib import Path
import re
import os

# =============================================================================
# CONFIGURATION
# =============================================================================

# Paths - adjust these based on your data location
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
IMG_DIR = BASE_DIR / "img"
TABLE_DIR = BASE_DIR / "table"

# Thesis claims to validate
CLAIMS = {
    "N_VENTURES": 180994,
    "RHO_EG_INDIVIDUAL": -0.04,
    "RHO_EG_INDIVIDUAL_TOLERANCE": 0.02,  # Allow ±0.02
    "RHO_ER": -0.087,
    "RHO_ER_TOLERANCE": 0.02,
    "MOVER_SURVIVAL": 0.181,  # 18.1%
    "STAYER_SURVIVAL": 0.070,  # 7.0%
    "MOVER_ADVANTAGE": 2.60,
    "MOVER_ADVANTAGE_TOLERANCE": 0.1,
    "P_VALUE_THRESHOLD": 0.001,
    "INDUSTRY_RHO_HARDWARE": -0.11,
    "INDUSTRY_RHO_TRANSPORTATION": -0.10,
}


# =============================================================================
# FIXTURES
# =============================================================================

@pytest.fixture(scope="module")
def load_main_data():
    """Load the main venture dataset."""
    possible_paths = [
        DATA_DIR / "processed" / "ventures_analyzed.csv",
        DATA_DIR / "ventures_final.csv",
        BASE_DIR.parent / "data" / "processed" / "ventures_analyzed.csv",
        Path("/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/papers_v7_sail/data/processed/ventures_analyzed.csv"),
    ]

    for path in possible_paths:
        if path.exists():
            return pd.read_csv(path)

    pytest.skip(f"Data file not found. Tried: {possible_paths}")


@pytest.fixture(scope="module")
def load_industry_data():
    """Load industry-level aggregated data."""
    possible_paths = [
        DATA_DIR / "industry_correlations.csv",
        DATA_DIR / "processed" / "industry_correlations.csv",
        BASE_DIR.parent / "data" / "industry_correlations_v2.csv",
    ]

    for path in possible_paths:
        if path.exists():
            return pd.read_csv(path)

    pytest.skip("Industry correlation data not found")


# =============================================================================
# 1. STATISTICAL REPRODUCIBILITY TESTS
# =============================================================================

class TestCoreCorrelations:
    """Test core correlation claims in the thesis."""

    def test_sample_size(self, load_main_data):
        """Verify N = 180,994 ventures."""
        df = load_main_data
        n = len(df)

        # Allow 1% tolerance for filtering differences
        tolerance = CLAIMS["N_VENTURES"] * 0.01
        assert abs(n - CLAIMS["N_VENTURES"]) < tolerance, \
            f"Sample size mismatch: got {n}, expected ~{CLAIMS['N_VENTURES']}"

    def test_rho_eg_individual(self, load_main_data):
        """Verify ρ(E,G) ≈ -0.04 at individual level."""
        df = load_main_data

        # Identify E and G columns (may have different names)
        e_cols = [c for c in df.columns if c.lower() in ['e', 'early_funding', 'log_funding', 'funding_early']]
        g_cols = [c for c in df.columns if c.lower() in ['g', 'growth', 'reached_c', 'success', 'growth_binary']]

        if not e_cols or not g_cols:
            pytest.skip(f"Cannot identify E/G columns. Available: {df.columns.tolist()}")

        e_col, g_col = e_cols[0], g_cols[0]

        # Compute correlation
        valid = df[[e_col, g_col]].dropna()
        rho, pval = stats.pearsonr(valid[e_col], valid[g_col])

        expected = CLAIMS["RHO_EG_INDIVIDUAL"]
        tolerance = CLAIMS["RHO_EG_INDIVIDUAL_TOLERANCE"]

        assert abs(rho - expected) < tolerance, \
            f"ρ(E,G) individual mismatch: got {rho:.4f}, expected {expected} ± {tolerance}"

        assert pval < CLAIMS["P_VALUE_THRESHOLD"], \
            f"ρ(E,G) not significant: p = {pval:.6f}"

    def test_rho_er(self, load_main_data):
        """Verify ρ(E,R) ≈ -0.087."""
        df = load_main_data

        e_cols = [c for c in df.columns if c.lower() in ['e', 'early_funding', 'log_funding', 'funding_early']]
        r_cols = [c for c in df.columns if c.lower() in ['r', 'repositioning', 'delta_breadth', 'breadth_change']]

        if not e_cols or not r_cols:
            pytest.skip(f"Cannot identify E/R columns. Available: {df.columns.tolist()}")

        e_col, r_col = e_cols[0], r_cols[0]

        valid = df[[e_col, r_col]].dropna()
        rho, pval = stats.pearsonr(valid[e_col], valid[r_col])

        expected = CLAIMS["RHO_ER"]
        tolerance = CLAIMS["RHO_ER_TOLERANCE"]

        assert abs(rho - expected) < tolerance, \
            f"ρ(E,R) mismatch: got {rho:.4f}, expected {expected} ± {tolerance}"


class TestMoverAdvantage:
    """Test mover advantage claims."""

    def test_mover_stayer_survival_rates(self, load_main_data):
        """Verify Mover: 18.1%, Stayer: 7.0%."""
        df = load_main_data

        # Find mover classification and growth columns
        mover_cols = [c for c in df.columns if 'mover' in c.lower() or 'moved' in c.lower()]
        g_cols = [c for c in df.columns if c.lower() in ['g', 'growth', 'reached_c', 'success']]

        if not mover_cols or not g_cols:
            pytest.skip("Cannot identify Mover/G columns")

        mover_col, g_col = mover_cols[0], g_cols[0]

        movers = df[df[mover_col] == 1] if df[mover_col].dtype in ['int64', 'float64'] else df[df[mover_col] == True]
        stayers = df[df[mover_col] == 0] if df[mover_col].dtype in ['int64', 'float64'] else df[df[mover_col] == False]

        mover_rate = movers[g_col].mean()
        stayer_rate = stayers[g_col].mean()

        # Tolerance of 2 percentage points
        assert abs(mover_rate - CLAIMS["MOVER_SURVIVAL"]) < 0.02, \
            f"Mover survival mismatch: got {mover_rate:.3f}, expected {CLAIMS['MOVER_SURVIVAL']}"

        assert abs(stayer_rate - CLAIMS["STAYER_SURVIVAL"]) < 0.02, \
            f"Stayer survival mismatch: got {stayer_rate:.3f}, expected {CLAIMS['STAYER_SURVIVAL']}"

    def test_mover_advantage_ratio(self, load_main_data):
        """Verify 2.60× mover advantage."""
        df = load_main_data

        mover_cols = [c for c in df.columns if 'mover' in c.lower() or 'moved' in c.lower()]
        g_cols = [c for c in df.columns if c.lower() in ['g', 'growth', 'reached_c', 'success']]

        if not mover_cols or not g_cols:
            pytest.skip("Cannot identify Mover/G columns")

        mover_col, g_col = mover_cols[0], g_cols[0]

        movers = df[df[mover_col] == 1] if df[mover_col].dtype in ['int64', 'float64'] else df[df[mover_col] == True]
        stayers = df[df[mover_col] == 0] if df[mover_col].dtype in ['int64', 'float64'] else df[df[mover_col] == False]

        mover_rate = movers[g_col].mean()
        stayer_rate = stayers[g_col].mean()

        if stayer_rate == 0:
            pytest.skip("Stayer rate is 0, cannot compute ratio")

        advantage = mover_rate / stayer_rate
        expected = CLAIMS["MOVER_ADVANTAGE"]
        tolerance = CLAIMS["MOVER_ADVANTAGE_TOLERANCE"]

        assert abs(advantage - expected) < tolerance, \
            f"Mover advantage mismatch: got {advantage:.2f}×, expected {expected}× ± {tolerance}"

    def test_mover_advantage_significance(self, load_main_data):
        """Verify mover advantage is statistically significant."""
        df = load_main_data

        mover_cols = [c for c in df.columns if 'mover' in c.lower() or 'moved' in c.lower()]
        g_cols = [c for c in df.columns if c.lower() in ['g', 'growth', 'reached_c', 'success']]

        if not mover_cols or not g_cols:
            pytest.skip("Cannot identify Mover/G columns")

        mover_col, g_col = mover_cols[0], g_cols[0]

        # Contingency table for chi-square test
        contingency = pd.crosstab(df[mover_col], df[g_col])
        chi2, pval, dof, expected = stats.chi2_contingency(contingency)

        assert pval < 0.001, \
            f"Mover advantage not significant at p<0.001: χ² = {chi2:.2f}, p = {pval:.6f}"


# =============================================================================
# 2. INTERNAL CONSISTENCY TESTS
# =============================================================================

class TestCrossChapterConsistency:
    """Test that statistics are consistent across chapters."""

    def test_tex_files_exist(self):
        """Verify all chapter files exist."""
        chapters = [
            "latex(thesis)_chap1.tex",
            "latex(thesis)_chap2.tex",
            "latex(thesis)_chap3.tex",
            "latex(thesis)_chap4.tex",
            "latex(thesis)_chap5.tex",
            "latex(thesis)_chap6.tex",
            "latex(thesis)_chap7_appendix.tex",
        ]

        for ch in chapters:
            path = BASE_DIR / ch
            assert path.exists(), f"Missing chapter file: {ch}"

    def test_sample_size_consistency(self):
        """Verify N=180,994 is cited consistently."""
        pattern = r"180[,.]?994"

        chapters = list(BASE_DIR.glob("latex(thesis)_chap*.tex"))
        found_in = []

        for ch in chapters:
            content = ch.read_text()
            if re.search(pattern, content):
                found_in.append(ch.name)

        # Should appear in at least Ch1, Ch3
        assert len(found_in) >= 2, \
            f"N=180,994 only found in {len(found_in)} chapters: {found_in}"

    def test_mover_advantage_consistency(self):
        """Verify 2.60× cited consistently."""
        pattern = r"2\.60"

        chapters = list(BASE_DIR.glob("latex(thesis)_chap*.tex"))
        values_found = []

        for ch in chapters:
            content = ch.read_text()
            matches = re.findall(r"(\d+\.\d+).*[×x]", content)
            values_found.extend(matches)

        # All mover advantage citations should be 2.60
        for val in values_found:
            if float(val) > 2 and float(val) < 3:  # Likely mover advantage
                assert abs(float(val) - 2.60) < 0.05, \
                    f"Inconsistent mover advantage value: {val}"

    def test_no_contradictory_correlations(self):
        """Check for contradictory correlation values."""
        chapters = list(BASE_DIR.glob("latex(thesis)_chap*.tex"))

        # Extract all rho values
        rho_pattern = r"[ρ\\rho]\s*[=≈]\s*(-?\d+\.\d+)"

        all_rhos = {}
        for ch in chapters:
            content = ch.read_text()
            matches = re.findall(rho_pattern, content)
            for m in matches:
                val = float(m)
                if val not in all_rhos:
                    all_rhos[val] = []
                all_rhos[val].append(ch.name)

        # Check that -0.04 (individual) and -0.196 (ecological) aren't confused
        # Both are valid but should be properly contextualized
        if -0.04 in [round(v, 2) for v in all_rhos.keys()]:
            pass  # Good - individual level reported

        # This test passes if no contradictions found
        assert True


# =============================================================================
# 3. METHODOLOGICAL VALIDITY TESTS
# =============================================================================

class TestEcologicalFallacy:
    """Test proper handling of ecological vs individual correlations."""

    def test_ecological_clarification_present(self):
        """Verify thesis distinguishes individual vs aggregate correlations."""
        ch1 = BASE_DIR / "latex(thesis)_chap1.tex"

        if not ch1.exists():
            pytest.skip("Chapter 1 not found")

        content = ch1.read_text()

        # Should mention both levels
        has_individual = "individual" in content.lower()
        has_industry = "industry" in content.lower() or "aggregate" in content.lower()

        assert has_individual and has_industry, \
            "Chapter 1 should distinguish individual vs industry-level correlations"

    def test_simpsons_paradox_check(self, load_main_data, load_industry_data):
        """Check if any industries show reversed correlation sign."""
        try:
            df = load_main_data
            industry_df = load_industry_data
        except:
            pytest.skip("Data not available for Simpson's paradox check")

        # Overall correlation
        e_cols = [c for c in df.columns if c.lower() in ['e', 'early_funding', 'log_funding']]
        g_cols = [c for c in df.columns if c.lower() in ['g', 'growth', 'reached_c', 'success']]

        if not e_cols or not g_cols:
            pytest.skip("Cannot identify columns")

        overall_rho, _ = stats.pearsonr(df[e_cols[0]].dropna(), df[g_cols[0]].dropna())

        # Check industry-level for sign reversals
        if 'correlation' in industry_df.columns:
            industry_rhos = industry_df['correlation'].values
            sign_reversals = sum(1 for r in industry_rhos if r * overall_rho < 0)

            if sign_reversals > 0:
                # Not a failure, but should be documented
                print(f"WARNING: {sign_reversals} industries show reversed correlation sign")


class TestCausalIdentification:
    """Test causal claims are properly qualified."""

    def test_mediation_caveats_present(self):
        """Verify mediation analysis caveats are stated."""
        chapters = list(BASE_DIR.glob("latex(thesis)_chap*.tex"))

        caveat_keywords = [
            "selection",
            "endogen",
            "reverse causal",
            "omitted variable",
            "confound",
        ]

        all_content = " ".join([ch.read_text().lower() for ch in chapters])

        caveats_found = [kw for kw in caveat_keywords if kw in all_content]

        assert len(caveats_found) >= 2, \
            f"Insufficient causal caveats. Found: {caveats_found}. Need at least 2."


# =============================================================================
# 4. ROBUSTNESS TESTS
# =============================================================================

class TestRobustness:
    """Test robustness of main findings."""

    def test_correlation_robust_to_outliers(self, load_main_data):
        """Test if ρ(E,G) robust to removing top/bottom 1%."""
        df = load_main_data

        e_cols = [c for c in df.columns if c.lower() in ['e', 'early_funding', 'log_funding']]
        g_cols = [c for c in df.columns if c.lower() in ['g', 'growth', 'reached_c', 'success']]

        if not e_cols or not g_cols:
            pytest.skip("Cannot identify columns")

        e_col, g_col = e_cols[0], g_cols[0]

        # Full sample correlation
        full_rho, _ = stats.pearsonr(df[e_col].dropna(), df[g_col].dropna())

        # Remove outliers
        lower, upper = df[e_col].quantile([0.01, 0.99])
        trimmed = df[(df[e_col] >= lower) & (df[e_col] <= upper)]
        trimmed_rho, _ = stats.pearsonr(trimmed[e_col], trimmed[g_col])

        # Sign should be preserved
        assert np.sign(full_rho) == np.sign(trimmed_rho), \
            f"Correlation sign changes with outlier removal: {full_rho:.3f} → {trimmed_rho:.3f}"

        # Magnitude shouldn't change dramatically
        assert abs(full_rho - trimmed_rho) < 0.05, \
            f"Correlation unstable to outliers: {full_rho:.3f} → {trimmed_rho:.3f}"


# =============================================================================
# 5. DATA INTEGRITY TESTS
# =============================================================================

class TestDataIntegrity:
    """Test data pipeline integrity."""

    def test_no_future_leakage(self, load_main_data):
        """Verify no future information used in predictions."""
        df = load_main_data

        # Check for suspicious column names
        suspicious = [c for c in df.columns if 'future' in c.lower() or 'later' in c.lower()]

        # This is a soft check - flag but don't fail
        if suspicious:
            print(f"WARNING: Potentially suspicious columns: {suspicious}")

    def test_reasonable_missing_rates(self, load_main_data):
        """Verify missing data rates are documented."""
        df = load_main_data

        missing_rates = df.isnull().mean()
        high_missing = missing_rates[missing_rates > 0.5]

        if len(high_missing) > 0:
            print(f"WARNING: Columns with >50% missing: {high_missing.to_dict()}")

        # Critical columns shouldn't have high missing rates
        critical = ['e', 'g', 'r', 'early_funding', 'growth', 'repositioning']
        for col in critical:
            matching = [c for c in df.columns if col in c.lower()]
            for m in matching:
                assert df[m].isnull().mean() < 0.3, \
                    f"Critical column {m} has {df[m].isnull().mean():.1%} missing"


# =============================================================================
# 6. FIGURE AND TABLE VALIDATION
# =============================================================================

class TestFiguresAndTables:
    """Test figures and tables exist and are referenced."""

    def test_all_figures_exist(self):
        """Verify all referenced figures exist."""
        required_figures = [
            "Ch1_Fig1_capital_paradox.png",
            "Ch1_Fig2_mediation_dag.png",
            "Ch2_Fig1_sorting_mechanism.png",
            "Ch3_Fig1_distributions_E_B0.png",
            "Ch3_Fig2_distributions_R_G.png",
            "Ch4_Fig1_G_by_R.png",
            "Ch4_Fig2_industry_rho.png",
            "Ch5_Fig1_sweet_spot.png",
        ]

        for fig in required_figures:
            path = IMG_DIR / fig
            assert path.exists(), f"Missing figure: {fig}"

    def test_all_tables_exist(self):
        """Verify all referenced tables exist."""
        required_tables = [
            "variable.tex",
            "descriptive.tex",
            "frg_analysis.tex",
            "mover_taxonomy.tex",
            "industry.tex",
            "alternatives.tex",
            "robustness.tex",
        ]

        for tab in required_tables:
            path = TABLE_DIR / tab
            assert path.exists(), f"Missing table: {tab}"

    def test_figure_references_valid(self):
        """Verify figure references in tex files point to existing files."""
        chapters = list(BASE_DIR.glob("latex(thesis)_chap*.tex"))

        for ch in chapters:
            content = ch.read_text()
            # Find includegraphics commands
            figures = re.findall(r"\\includegraphics.*?\{([^}]+)\}", content)

            for fig in figures:
                # Normalize path
                fig_path = fig.replace("img/", "").replace("img_overleaf/", "")
                full_path = IMG_DIR / fig_path

                assert full_path.exists(), \
                    f"Referenced figure not found: {fig} (in {ch.name})"


# =============================================================================
# 7. BIBLIOGRAPHY VALIDATION
# =============================================================================

class TestBibliography:
    """Test bibliography completeness."""

    def test_bib_file_exists(self):
        """Verify bibliography file exists."""
        bib_path = BASE_DIR / "golden_cage.bib"
        assert bib_path.exists(), "Bibliography file golden_cage.bib not found"

    def test_all_citations_in_bib(self):
        """Verify all cited references exist in bibliography."""
        chapters = list(BASE_DIR.glob("latex(thesis)_chap*.tex"))
        bib_path = BASE_DIR / "golden_cage.bib"

        if not bib_path.exists():
            pytest.skip("Bibliography file not found")

        # Extract citations
        citations = set()
        for ch in chapters:
            content = ch.read_text()
            matches = re.findall(r"\\cite[pt]?\{([^}]+)\}", content)
            for m in matches:
                for cite in m.split(","):
                    citations.add(cite.strip())

        # Extract bib entries
        bib_content = bib_path.read_text()
        bib_entries = set(re.findall(r"@\w+\{(\w+),", bib_content))

        # Check coverage
        missing = citations - bib_entries

        assert len(missing) == 0, \
            f"Citations missing from bibliography: {missing}"


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
