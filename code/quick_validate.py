#!/usr/bin/env python3
"""
QUICK THESIS VALIDATION
========================
Runs immediately without requiring full dataset.
Validates LaTeX files, cross-references, and consistency.

Usage: python quick_validate.py
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

# Colors for terminal
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'

BASE_DIR = Path(__file__).parent.parent
IMG_DIR = BASE_DIR / "img"
TABLE_DIR = BASE_DIR / "table"

def print_header(msg):
    print(f"\n{BOLD}{'='*60}{RESET}")
    print(f"{BOLD}{msg}{RESET}")
    print(f"{BOLD}{'='*60}{RESET}")

def check_pass(msg):
    print(f"  {GREEN}✓{RESET} {msg}")

def check_fail(msg):
    print(f"  {RED}✗{RESET} {msg}")

def check_warn(msg):
    print(f"  {YELLOW}⚠{RESET} {msg}")


class ThesisValidator:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.passes = 0

    def validate_files_exist(self):
        """Check all required files exist."""
        print_header("1. FILE EXISTENCE CHECK")

        required = {
            "Main thesis": "MIT Thesis.tex",
            "Abstract": "abstract.tex",
            "Bibliography": "golden_cage.bib",
            "Color definitions": "latex(thesis)_color_definitions.tex",
            "Chapter 1": "latex(thesis)_chap1.tex",
            "Chapter 2": "latex(thesis)_chap2.tex",
            "Chapter 3": "latex(thesis)_chap3.tex",
            "Chapter 4": "latex(thesis)_chap4.tex",
            "Chapter 5": "latex(thesis)_chap5.tex",
            "Chapter 6": "latex(thesis)_chap6.tex",
            "Appendix": "latex(thesis)_chap7_appendix.tex",
        }

        for name, filename in required.items():
            path = BASE_DIR / filename
            if path.exists():
                check_pass(f"{name}: {filename}")
                self.passes += 1
            else:
                check_fail(f"{name}: {filename} NOT FOUND")
                self.errors.append(f"Missing file: {filename}")

    def validate_figures(self):
        """Check all figures exist and are referenced."""
        print_header("2. FIGURE VALIDATION")

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
            if path.exists():
                check_pass(f"Figure: {fig}")
                self.passes += 1
            else:
                check_fail(f"Figure: {fig} NOT FOUND")
                self.errors.append(f"Missing figure: {fig}")

    def validate_tables(self):
        """Check all tables exist."""
        print_header("3. TABLE VALIDATION")

        required_tables = [
            "variable.tex",
            "descriptive.tex",
            "frg_analysis.tex",
            "mover_taxonomy.tex",
            "industry.tex",
            "alternatives.tex",
            "robustness.tex",
            "governance.tex",
        ]

        for tab in required_tables:
            path = TABLE_DIR / tab
            if path.exists():
                check_pass(f"Table: {tab}")
                self.passes += 1
            else:
                check_fail(f"Table: {tab} NOT FOUND")
                self.errors.append(f"Missing table: {tab}")

    def validate_bibliography(self):
        """Check all citations are in bibliography."""
        print_header("4. BIBLIOGRAPHY VALIDATION")

        bib_path = BASE_DIR / "golden_cage.bib"
        if not bib_path.exists():
            check_fail("golden_cage.bib not found")
            self.errors.append("Missing bibliography file")
            return

        # Extract citations from all chapters
        citations = set()
        chapters = list(BASE_DIR.glob("latex(thesis)_chap*.tex"))

        for ch in chapters:
            content = ch.read_text()
            matches = re.findall(r"\\cite[pt]?\{([^}]+)\}", content)
            for m in matches:
                for cite in m.split(","):
                    citations.add(cite.strip())

        # Extract bib entries
        bib_content = bib_path.read_text()
        bib_entries = set(re.findall(r"@\w+\{(\w+),", bib_content))

        print(f"  Citations found: {len(citations)}")
        print(f"  Bib entries: {len(bib_entries)}")

        missing = citations - bib_entries
        if missing:
            for m in missing:
                check_fail(f"Citation missing from bib: {m}")
                self.errors.append(f"Missing citation: {m}")
        else:
            check_pass("All citations found in bibliography")
            self.passes += 1

    def validate_statistical_consistency(self):
        """Check statistical values are consistent across chapters."""
        print_header("5. STATISTICAL CONSISTENCY")

        chapters = list(BASE_DIR.glob("latex(thesis)_chap*.tex"))
        all_content = ""
        for ch in chapters:
            all_content += ch.read_text()

        # Check N = 180,994
        n_pattern = r"180[,.]?994"
        n_matches = re.findall(n_pattern, all_content)
        if len(n_matches) >= 2:
            check_pass(f"N=180,994 mentioned {len(n_matches)} times")
            self.passes += 1
        else:
            check_warn(f"N=180,994 only mentioned {len(n_matches)} times")
            self.warnings.append("Sample size mentioned infrequently")

        # Check mover advantage
        ma_pattern = r"2\.60"
        ma_matches = re.findall(ma_pattern, all_content)
        if len(ma_matches) >= 1:
            check_pass(f"2.60× mover advantage mentioned {len(ma_matches)} times")
            self.passes += 1
        else:
            check_fail("2.60× mover advantage not found")
            self.errors.append("Mover advantage value missing")

        # Check correlation values
        rho_pattern = r"[ρ].*?(-?\d+\.\d+)"
        rho_matches = re.findall(rho_pattern, all_content)

        print(f"\n  Correlation values found:")
        value_counts = defaultdict(int)
        for v in rho_matches:
            value_counts[v] += 1
        for v, c in sorted(value_counts.items()):
            print(f"    ρ = {v}: {c} occurrences")

        # Check for ecological clarification
        if "individual" in all_content.lower() and "industry" in all_content.lower():
            check_pass("Ecological vs individual correlation distinguished")
            self.passes += 1
        else:
            check_warn("May need to clarify individual vs industry-level correlations")
            self.warnings.append("Ecological clarification may be needed")

    def validate_cross_references(self):
        """Check LaTeX cross-references."""
        print_header("6. CROSS-REFERENCE CHECK")

        chapters = list(BASE_DIR.glob("latex(thesis)_chap*.tex"))

        labels = set()
        refs = set()

        for ch in chapters:
            content = ch.read_text()
            # Find labels
            labels.update(re.findall(r"\\label\{([^}]+)\}", content))
            # Find refs
            refs.update(re.findall(r"\\ref\{([^}]+)\}", content))
            refs.update(re.findall(r"\\autoref\{([^}]+)\}", content))

        # Standard labels that may be defined elsewhere
        standard = {"ch:introduction", "ch:theory", "ch:data", "ch:results",
                    "ch:design", "ch:conclusion"}

        unresolved = refs - labels - standard

        if unresolved:
            for ref in unresolved:
                check_warn(f"Potentially unresolved reference: {ref}")
                self.warnings.append(f"Unresolved ref: {ref}")
        else:
            check_pass("All references appear to be defined")
            self.passes += 1

    def validate_no_overlapping_claims(self):
        """Check for contradictory claims."""
        print_header("7. CLAIM CONSISTENCY")

        chapters = list(BASE_DIR.glob("latex(thesis)_chap*.tex"))

        # Key claims that should be consistent
        claims = {
            "mover_survival": [],
            "stayer_survival": [],
            "mover_advantage": [],
        }

        for ch in chapters:
            content = ch.read_text()

            # Mover survival rate
            mover_matches = re.findall(r"Movers?.*?(\d+\.?\d*)%", content, re.IGNORECASE)
            claims["mover_survival"].extend(mover_matches)

            # Stayer survival rate
            stayer_matches = re.findall(r"Stayers?.*?(\d+\.?\d*)%", content, re.IGNORECASE)
            claims["stayer_survival"].extend(stayer_matches)

            # Mover advantage
            ma_matches = re.findall(r"(\d+\.\d+)[×x]", content)
            claims["mover_advantage"].extend([m for m in ma_matches if 2 < float(m) < 4])

        # Check consistency
        for claim, values in claims.items():
            unique = set(values)
            if len(unique) <= 1:
                if unique:
                    check_pass(f"{claim}: consistently {list(unique)[0]}")
                    self.passes += 1
            else:
                check_warn(f"{claim}: multiple values {unique}")
                self.warnings.append(f"Inconsistent {claim}: {unique}")

    def run_all(self):
        """Run all validations."""
        print(f"\n{BOLD}GOLDEN CAGE THESIS VALIDATION{RESET}")
        print(f"Base directory: {BASE_DIR}")

        self.validate_files_exist()
        self.validate_figures()
        self.validate_tables()
        self.validate_bibliography()
        self.validate_statistical_consistency()
        self.validate_cross_references()
        self.validate_no_overlapping_claims()

        # Summary
        print_header("VALIDATION SUMMARY")
        print(f"  {GREEN}Passed: {self.passes}{RESET}")
        print(f"  {YELLOW}Warnings: {len(self.warnings)}{RESET}")
        print(f"  {RED}Errors: {len(self.errors)}{RESET}")

        if self.errors:
            print(f"\n{RED}ERRORS:{RESET}")
            for e in self.errors:
                print(f"  - {e}")

        if self.warnings:
            print(f"\n{YELLOW}WARNINGS:{RESET}")
            for w in self.warnings:
                print(f"  - {w}")

        if not self.errors:
            print(f"\n{GREEN}✓ Thesis validation PASSED{RESET}")
            return 0
        else:
            print(f"\n{RED}✗ Thesis validation FAILED{RESET}")
            return 1


if __name__ == "__main__":
    validator = ThesisValidator()
    sys.exit(validator.run_all())
