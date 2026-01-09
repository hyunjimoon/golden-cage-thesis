# Canonical Registry (CR.GLOSSARY) - v6.1 (Option B Aligned)

> **Purpose:** Translation Dictionary between Python code and Thesis text
> **Last Updated:** 2026-01-09

---

## 1. Variable Mapping (Code ↔ Text)

| Thesis Variable | Definition | Code Variable (Legacy) | Measurement Method (Updated) |
|:---:|:---|:---|:---|
| **F** | **Funding** (Early-stage Capital) | `log_raised_usd` / `funding_total` / `E` | Log(Total Raised USD up to Series A) |
| **R** | **Repositioning** (Strategic Shift) | `pivot_magnitude` / `sim_score` / `M` | $1 - \text{CosineSim}(\text{SBERT}(D_t), \text{SBERT}(D_0))$ |
| **B** | **Strategic Breadth** | `breadth_score` / `specificity` / `V` | $100 \times (1 - \text{AvgCosineSim}(\text{Keywords}, \text{Lexicon}))$ |
| **G** | **Growth** (Performance) | `late_stage_success` / `L` / `GrowthRate` | Survival to Series C+ OR IPO/M&A |
| **C** | **Commitment** | `commitment_level` | (Qualitative/Dummy) Operational Lock-in |
| **A** | **Adaptability** | N/A (Latent) | Latent capacity suppressed by Governance |

### Legacy Code → Thesis Translation

| Code (01_raw_to_processed.py) | Thesis Symbol | Notes |
|:------------------------------|:-------------:|:------|
| `V`, `V_0`, `V_T` | **B**, **B₀**, **B_T** | Strategic Breadth (0-100 scale) |
| `D` = V_T - V_0 | **ΔB** | Direction of breadth change |
| `M` = \|D\| | **R** | Repositioning magnitude |
| `E` (first_financing_size) | **F** | Early-stage funding |
| `L` (Later Stage VC) | **G** | Growth/Success outcome |
| `mover_type` | Archetype | zoom_in / zoom_out / stayer |

---

## 2. Core Claims & Logic

| ID | Statement | Math | Section |
|:---|:---|:---|:---|
| **CLAIM.PARADOX** | Funding suppresses Growth (Total Effect) | $dG/dF < 0$ ($\rho \approx -0.174$) | Sec II (¶8) |
| **CLAIM.CAGE** | Funding suppresses Repositioning | $dR/dF < 0$ | Sec II (¶14) |
| **CLAIM.ARG** | Repositioning drives Growth | $dG/dR > 0$ (Movers > Stayers) | Sec III (¶21) |
| **CLAIM.TRAP** | Learning Cessation Condition | $\mu(1-\mu) < \epsilon/B$ | Sec II (¶12) |

---

## 3. Thresholds (Strict Definition)

| Category | Code Condition | Thesis Condition | Interpretation |
|:---------|:---------------|:-----------------|:---------------|
| **Stayers** | `M < 5` or horizontal | R < 5 | Strategic breadth within noise |
| **Movers** | `D < -10` or `D > 10` AND `M >= 5` | R ≥ 15 | Significant semantic shift (≥1 SD) |
| **Zoom-in** | `D < -10` AND `M >= 5` | ΔB < -10, R ≥ 5 | Focus narrowing |
| **Zoom-out** | `D > 10` AND `M >= 5` | ΔB > 10, R ≥ 5 | Scope broadening |
| **Golden Cage** | High E + Low M | High F + Low R | Well-funded Stayers |

---

## 4. Data Sources

| Variable | Source File | Pipeline Step |
|:---------|:------------|:--------------|
| B (V) | `vagueness_timeseries.parquet` | 01_raw_to_processed.py |
| F (E) | `features_all.parquet` | 01_raw_to_processed.py |
| G (L) | `features_all.parquet` | 01_raw_to_processed.py |
| Panel | `thesis_panel_v3.nc` | Final output |

---

*When writing thesis text, ALWAYS use Thesis Variable names (F, R, B, G, C, A).*
*When reading code, translate using this registry.*
