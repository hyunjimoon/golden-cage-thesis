# Canonical Registry (CR.GLOSSARY) - v6.2 (Option A: v2 Pipeline)

> **Purpose:** Translation Dictionary between Python code and Thesis text
> **Last Updated:** 2026-01-09
> **Pipeline:** vagueness_v2.py (HybridVaguenessScorerV2) — **DO NOT CHANGE**

---

## 1. Variable Mapping (Code ↔ Text)

| Thesis Variable | Definition | Code Variable (Legacy) | Measurement Method (v2) |
|:---:|:---|:---|:---|
| **F** | **Funding** (Early-stage Capital) | `log_raised_usd` / `funding_total` / `E` | Log(Total Raised USD up to Series A) |
| **R** | **Repositioning** (Strategic Shift) | `pivot_magnitude` / `M` | $\|B_T - B_0\|$ (Absolute change in Strategic Breadth) |
| **B** | **Strategic Breadth** | `V` / `V_composite` | Dictionary-based Vague Terminology Density (Abstract terms + Concreteness deficit) |
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

## 3. Thresholds (Conditional Quantile Definition)

> **Zero-inflation fix:** 59.6% have M=0, so median calculated from non-zero M only (threshold = 0.5)

| Category | Code Condition | Thesis Condition | Interpretation |
|:---------|:---------------|:-----------------|:---------------|
| **Stayers** | `M <= M_threshold` | R ≤ Median(non-zero M) | No/small movement (incl. ΔB=0) |
| **Movers** | `M > M_threshold` | R > Median(non-zero M) | Significant strategic shift |
| **Zoom-in** | `D < 0` AND `M > M_threshold` | ΔB < 0, R > Median | Focus narrowing |
| **Zoom-out** | `D > 0` AND `M > M_threshold` | ΔB > 0, R > Median | Scope broadening |
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
