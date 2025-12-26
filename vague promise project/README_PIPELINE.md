# Quantum Startup Theory - End-to-End Pipeline
## 전라좌수군 Production System

> "Vagueness buys options; movement is measurement; capital forces premature collapse."

---

## 🗂️ Directory Structure

```
vague_promise_project/
├── README.md                      # This file
├── run_all.sh                     # 🔥 ONE-CLICK: Analysis → TeX → PDF
│
├── data/
│   ├── raw/                       # PitchBook exports
│   ├── processed/                 # Cleaned datasets
│   └── pitchbook_180k.parquet     # Main dataset (N=180,860)
│
├── analysis/
│   ├── __init__.py
│   ├── config.py                  # SEED=42, paths, constants
│   │
│   ├── layer1_what/               # Layer 1: WHAT patterns exist?
│   │   ├── paper_m/               # Movement Principle
│   │   │   ├── movement_analysis.py
│   │   │   ├── quartile_analysis.py
│   │   │   └── figures/
│   │   │       ├── fig_m1_mover_stayer.png
│   │   │       ├── fig_m2_direction_irrelevance.png
│   │   │       └── fig_m3_quartile_success.png
│   │   │
│   │   └── paper_c/               # Golden Cage
│   │       ├── golden_cage_analysis.py
│   │       ├── temporal_robustness.py
│   │       └── figures/
│   │           ├── fig_c1_capital_vs_adaptation.png
│   │           ├── fig_c2_temporal_stability.png
│   │           └── fig_c3_mediation.png
│   │
│   ├── layer2_how/                # Layer 2: HOW do founders respond?
│   │   ├── process_sequence.py    # Coalition formation process
│   │   ├── case_studies/
│   │   │   ├── tesla_analysis.py
│   │   │   └── better_place_analysis.py
│   │   └── figures/
│   │       ├── fig_l2_process_diagram.png
│   │       └── fig_l2_case_comparison.png
│   │
│   └── layer3_why/                # Layer 3: WHY does this work?
│       ├── oil_model.py           # τ* = √(V/4i) computation
│       ├── agent_simulation.py    # Coalition formation ABM
│       ├── sensitivity.py         # Parameter sensitivity
│       └── figures/
│           ├── fig_l3_oil_surface.png
│           ├── fig_l3_coalition_dynamics.png
│           └── fig_l3_threshold_distribution.png
│
├── papers_v2/                     # Writing modules (existing)
│   ├── _shared/
│   ├── 1_introduction/
│   ├── 2_paper_M/
│   ├── 3_paper_C/
│   ├── 4_discussion/
│   └── 5_statistics/
│
├── latex/
│   ├── main.tex                   # Master document
│   ├── preamble.tex               # Packages & commands
│   ├── chapters/
│   │   ├── ch1_introduction.tex
│   │   ├── ch2_paper_m.tex
│   │   ├── ch3_paper_c.tex
│   │   ├── ch4_discussion.tex
│   │   └── ch5_statistics.tex
│   ├── figures/                   # Symlinks to analysis/*/figures/
│   ├── tables/
│   └── bibliography.bib
│
├── output/
│   ├── thesis.pdf                 # Final output
│   └── thesis_draft_YYYYMMDD.pdf  # Versioned drafts
│
└── scripts/
    ├── generate_figures.py        # Run all figure generation
    ├── compile_latex.py           # LaTeX compilation
    ├── validate_pipeline.py       # Check all dependencies
    └── export_advisor.py          # Generate advisor-ready package
```

---

## 🔥 Quick Start

```bash
# ONE COMMAND: Everything
./run_all.sh

# Or step by step:
./run_all.sh --figures      # Generate all figures
./run_all.sh --latex        # Compile LaTeX only
./run_all.sh --validate     # Check pipeline integrity
./run_all.sh --advisor      # Export advisor package
```

---

## 📊 LTE Layer Mapping

| Layer | Question | Folder | Key Output |
|:-----:|:---------|:-------|:-----------|
| **1** | WHAT patterns? | `analysis/layer1_what/` | Paper M + Paper C figures |
| **2** | HOW do founders respond? | `analysis/layer2_how/` | Process diagram, cases |
| **3** | WHY does it work? | `analysis/layer3_why/` | OIL simulation, ABM |

---

## 🛠️ run_all.sh

```bash
#!/bin/bash
# Quantum Startup Theory: End-to-End Pipeline
# Usage: ./run_all.sh [--figures|--latex|--validate|--advisor]

set -e  # Exit on error

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_ROOT"

echo "🚀 Quantum Startup Theory Pipeline"
echo "=================================="

# Step 1: Generate Figures
if [[ "$1" == "--figures" || "$1" == "" ]]; then
    echo ""
    echo "📊 Step 1: Generating Figures..."
    python analysis/layer1_what/paper_m/movement_analysis.py
    python analysis/layer1_what/paper_c/golden_cage_analysis.py
    python analysis/layer2_how/process_sequence.py
    python analysis/layer3_why/oil_model.py
    echo "✅ Figures complete"
fi

# Step 2: Compile LaTeX
if [[ "$1" == "--latex" || "$1" == "" ]]; then
    echo ""
    echo "📄 Step 2: Compiling LaTeX..."
    cd latex
    pdflatex -interaction=nonstopmode main.tex
    bibtex main
    pdflatex -interaction=nonstopmode main.tex
    pdflatex -interaction=nonstopmode main.tex
    mv main.pdf ../output/thesis.pdf
    cd ..
    echo "✅ PDF generated: output/thesis.pdf"
fi

# Step 3: Validate
if [[ "$1" == "--validate" ]]; then
    echo ""
    echo "🔍 Step 3: Validating Pipeline..."
    python scripts/validate_pipeline.py
fi

# Step 4: Advisor Export
if [[ "$1" == "--advisor" ]]; then
    echo ""
    echo "📦 Step 4: Exporting Advisor Package..."
    python scripts/export_advisor.py
    echo "✅ Advisor package: output/advisor_package_$(date +%Y%m%d).zip"
fi

echo ""
echo "🎉 Pipeline Complete!"
echo "   PDF: output/thesis.pdf"
```

---

## 📈 Figure Registry

| Figure ID | Layer | Description | Script |
|:----------|:-----:|:------------|:-------|
| fig_m1 | 1 | Mover vs Stayer (2.6×) | `paper_m/movement_analysis.py` |
| fig_m2 | 1 | Direction Irrelevance | `paper_m/movement_analysis.py` |
| fig_m3 | 1 | Quartile Success Rates | `paper_m/quartile_analysis.py` |
| fig_c1 | 1 | Capital vs Adaptation | `paper_c/golden_cage_analysis.py` |
| fig_c2 | 1 | Temporal Stability | `paper_c/temporal_robustness.py` |
| fig_c3 | 1 | Mediation Analysis | `paper_c/golden_cage_analysis.py` |
| fig_l2 | 2 | Process Sequence | `layer2_how/process_sequence.py` |
| fig_l3_oil | 3 | OIL Surface τ* | `layer3_why/oil_model.py` |
| fig_l3_abm | 3 | Coalition Dynamics | `layer3_why/agent_simulation.py` |

---

## 🔄 Workflow

```
data/raw/*.csv
     │
     ▼ (clean)
data/processed/*.parquet
     │
     ├──▶ analysis/layer1_what/ ──▶ figures/*.png
     ├──▶ analysis/layer2_how/  ──▶ figures/*.png
     └──▶ analysis/layer3_why/  ──▶ figures/*.png
                                        │
                                        ▼ (symlink)
                                  latex/figures/
                                        │
                                        ▼ (compile)
                                  output/thesis.pdf
```

---

## ✅ Checklist

- [ ] `data/pitchbook_180k.parquet` exists
- [ ] All `analysis/**/figures/*.png` generated
- [ ] `latex/main.tex` compiles without errors
- [ ] `output/thesis.pdf` opens correctly
- [ ] Advisor package exported

---

*통제사: 이순신 문현지 (Moon)*
*Generated: 2025-12-15*
