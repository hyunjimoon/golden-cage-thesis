# Figure and Table Inventory

## Summary Statistics (from actual data)

| Statistic | Value | Source |
|-----------|-------|--------|
| Total ventures | **180,994** | thesis_stats.json |
| Moved success rate | **17.7%** | thesis_stats.json |
| Stayed success rate | **10.8%** | thesis_stats.json |
| Movement advantage | **1.6×** | 17.7% / 10.8% |
| ρ(G, E) | **−0.196*** | Funding Paradox |
| ρ(A, E) | **−0.117*** | Fund2Cage |
| ρ(G, A) | **+0.209*** | Movement → Growth |
| ρ(V, L) | **+0.024*** | Vagueness → Success |

---

## Figures

### Module I: Introduction
| Figure | File | Description | Referenced In |
|--------|------|-------------|---------------|
| Fig I.1 | `1_I_introduction/fig_i_cash_paradox.png` | Funding Paradox visualization | content.md ¶3 |

### Module M: Movement Principle
| Figure | File | Description | Referenced In |
|--------|------|-------------|---------------|
| Fig M.1 | `2_M_movement/fig_m_mover_advantage.png` | Mover vs Stayer comparison | s4_results.md ¶21 |
| Fig M.2 | `2_M_movement/paper_m2/fig_decomposition.png` | Three-panel decomposition | s6_empirics.md ¶42 |

### Module C: Fund2Growth / Cash2Cage
| Figure | File | Description | Referenced In |
|--------|------|-------------|---------------|
| Fig C.1 | `3_C_cash2growth/fig_c_typology.png` | 4-archetype typology | s1_theme.md ¶52 |

### Module T: Commit2Trap
| Figure | File | Description | Referenced In |
|--------|------|-------------|---------------|
| Fig T.1 | `4_T_commit2trap/fig_decomposition_real.png` | Decomposition (all data) | s3_learning_trap.md |
| Fig T.2 | `4_T_commit2trap/fig_decomposition_real_2023.png` | Decomposition 2023 | Temporal stability |
| Fig T.3 | `4_T_commit2trap/fig_decomposition_real_2024.png` | Decomposition 2024 | Temporal stability |
| Fig T.4 | `4_T_commit2trap/fig_decomposition_real_2025.png` | Decomposition 2025 | Temporal stability |
| Fig T.5 | `4_T_commit2trap/fig_V_trajectories_by_archetype.png` | Vagueness trajectories | s2_precision_paradox.md |
| Fig T.6 | `4_T_commit2trap/fig_success_by_archetype_real.png` | Success by archetype | s3_learning_trap.md |
| Fig T.7 | `4_T_commit2trap/fig_V_efficiency_real.png` | V-efficiency relationship | s3_learning_trap.md |
| Fig T.8 | `4_T_commit2trap/fig_archetype_dG_dE_real.png` | dG/dE by archetype | s3_learning_trap.md |

### Module D: Discussion
| Figure | File | Description | Referenced In |
|--------|------|-------------|---------------|
| Fig D.1 | `5_D_discussion/fig_d_synthesis.png` | Synthesis diagram | content.md ¶108 |

### Diagnostic Figures (not for publication)
| Figure | File | Description |
|--------|------|-------------|
| - | `_shared/fig_eyeball_growthrate_comparison.png` | GrowthRate validation |
| - | `_shared/fig_eyeball_success_by_archetype.png` | Success rate check |
| - | `4_T_commit2trap/diagnostic_*.png` | Various diagnostics |
| - | `test/diagnostic_*.png` | Test diagnostics |

### Transportation Industry Figures (supplementary)
| Figure | File | Description |
|--------|------|-------------|
| - | `4_T_commit2trap/fig_*_transportation.png` | Transportation sector analysis |

---

## Tables

### Module I: Introduction
| Table | Description | Location | Key Values |
|-------|-------------|----------|------------|
| - | Summary statistics | content.md ¶3 | N=180,994, ρ(G,E)=−0.196 |

### Module M: Movement Principle
| Table | Description | Location | Key Values |
|-------|-------------|----------|------------|
| Tab 1 | Variable definitions | s3_litrev_variables.md ¶16-19 | V, D, A, E, G |
| Tab 2 | Movement Principle | s4_results.md ¶21 | 17.7% vs 10.8% = 1.6× |
| Tab 3 | Success by quartile | s4_results.md ¶22 | Q3=16.0% highest |
| Tab 4 | Direction comparison | s4_results.md ¶23 | 17.6% ≈ 18.6% |
| Tab 5 | Effect size interpretation | s5_implication.md ¶24 | NNT=14, RR=1.64 |

### Module C: Fund2Growth
| Table | Description | Location | Key Values |
|-------|-------------|----------|------------|
| Tab C.1 | 4 archetype typology | s1_theme.md ¶52 | Stayer/Horiz/ZoomIn/ZoomOut |
| Tab C.2 | Company examples | s1_theme.md ¶53 | Sky Engine, Linpowave, etc. |
| Tab C.3 | Stayer statistics | s2_var1_stayer.md ¶58 | 91%, 10.8% |
| Tab C.4 | Success by archetype | s2_var1_stayer.md ¶60 | Comparison table |

### Module T: Commit2Trap
| Table | Description | Location | Key Values |
|-------|-------------|----------|------------|
| Tab T.1 | Q1-Q4 expected vs observed | s1_revisit.md ¶82 | Q3 wins unexpectedly |
| Tab T.2 | Composition analysis | s3_learning_trap.md ¶94 | Movement rate → success |
| Tab T.3 | Trap risk by μ | s3_learning_trap.md ¶96 | High μ → need doubters |
| Tab T.4 | V level → stakeholder type | s3_learning_trap.md ¶97 | Echo chamber mechanism |

### Module D: Discussion
| Table | Description | Location | Key Values |
|-------|-------------|----------|------------|
| Tab D.1 | Confidence assessment | limitations.md ¶113 | High/Medium/Low |

---

## Key Equations

| Equation | Description | Location |
|----------|-------------|----------|
| dG/dE = (dG/dA)(dA/dE) | Chain rule decomposition | content.md ¶6 |
| μ(1−μ) < ε/(V+1) | Learning trap condition | content.md ¶8 |
| AOC = Sunk + Resistance + Identity | Adjustment cost | s5_theory.md ¶39 |

---

## Data Sources

| Source | Description | N |
|--------|-------------|---|
| thesis_panel_v3.nc | Main analysis dataset | 180,994 |
| thesis_stats.json | Computed statistics | - |

---

*Generated: 2025-12-21*
*Statistics verified from actual data via compute_thesis_stats.py*
