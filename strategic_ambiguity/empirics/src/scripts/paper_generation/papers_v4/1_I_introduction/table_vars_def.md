# 🗄️ Table 1: Variable Definitions

**The Funding Paradox: Core Constructs**

---

## Panel A: Primary Variables

| Variable | Name | Definition | Operationalization | Source |
|:--------:|:-----|:-----------|:-------------------|:-------|
| **F** | Funding | Total external capital raised | log($ raised), cumulative | PitchBook |
| **M** | Movement | Magnitude of strategic repositioning | \|V_T − V_0\| = \|D\| | Computed |
| **G** | Growth | Venture performance/survival | Binary: Later Stage VC (C/D+) | PitchBook |
| **V** | Vagueness | Strategic ambiguity of positioning | Rank-normalized (0-100 percentile) | NLP |
| **D** | Direction | Signed direction of repositioning | V_T − V_0 | Computed |

---

## Panel B: Variable Relationships (Causal Chain)

```
        ┌────────────────────────────────────────┐
        │           F (Funding)                  │
        └──────────────┬─────────────────────────┘
                       │ MF: dM/dF < 0
                       ▼
┌──────────────────────────────────────────────────┐
│                  M (Movement)                     │
│                  M = |D| = |ΔV|                   │
└──────────────┬───────────────────────────────────┘
               │ MG: dG/dM > 0
               ▼
        ┌────────────────────────────────────────┐
        │           G (Growth)                   │
        └────────────────────────────────────────┘

        ┌────────────────────────────────────────┐
        │           V (Vagueness)                │
        └──────┬─────────────────┬───────────────┘
               │ VM: dM/dV       │ VD: dD/dV
               ▼                 ▼
           M (Movement)      D (Direction)
```

**Core Decomposition:**
$$\underbrace{\frac{dG}{dF} < 0}_{\text{Funding Paradox}} = \underbrace{\frac{dG}{dM} > 0}_{\text{MG: Movement Principle}} \times \underbrace{\frac{dM}{dF} < 0}_{\text{MF: Funding Trap}}$$

---

## Panel C: Module Structure (IMVEC)

| Module | Submodule | ¶ Range | Focus | Key Relationship |
|:------:|:----------|:-------:|:------|:-----------------|
| **I** | I1 | 1-11 | Funding Paradox | dG/dF < 0 |
| **M** | MG (M1-M2) | 12-29 | Movement Principle | dG/dM > 0 |
| | M3 (Bridge) | 30 | Decomposition | dG/dF = (dG/dM)(dM/dF) |
| | MF (M4-M5) | 31-48 | Funding Trap | dM/dF < 0 |
| **V** | VM (V1-V2) | 49-64 | Vagueness → Movement | dM/dV |
| | VD (V3-V4) | 65-80 | Vagueness → Direction | dD/dV |
| **E** | E1 | 81-86 | Tempo Return | M vs NM |
| | E2 | 87-92 | Stayer Cases | Non-Movers |
| | E3 | 93-98 | PAE Framework | Platformize→Acculturate→Evaluate |
| | E4 | 99-104 | Synthesis | Escape Paths |
| **C** | C1 | 105-108 | Implications | For founders + investors |
| | C2 | 109-111 | Limitations | Boundary conditions |
| | C3 | 112-113 | Coda | Commit to Move |

---

## Panel D: Movement Archetypes

| Archetype | M | D | Trap Type | Escape | Survival |
|:----------|:-:|:-:|:----------|:-------|:--------:|
| **Stayer** | ≈0 | 0 | Both | — | 9.9% |
| **Zoom In** | >0 | <0 | High-V → | Specificity | 17.5% |
| **Zoom Out** | >0 | >0 | Low-V → | Flexibility | 18.4% |

---

## Panel E: Trap Mechanisms

| Trap | Initial V | Mechanism | Learning Failure | Escape |
|:-----|:----------|:----------|:-----------------|:-------|
| **High-V** | High (vague) | Unfalsifiable hypotheses | Cannot reject | Zoom In (D < 0) |
| **Low-V** | Low (precise) | Echo chamber, μ(1−μ) → 0 | Cannot pivot | Zoom Out (D > 0) |

**Learning Trap Condition:**
$$\mu(1-\mu) < \frac{\varepsilon}{V+1}$$

---

## Panel F: Hypotheses by Module

| H# | Module | Relationship | Gospel (Null) | Surprise |
|:---|:------:|:-------------|:--------------|:---------|
| H1 | I | dG/dF < 0 | "More funding = growth" | Paradox |
| H2 | MG | dG/dM > 0 | Porter: "Stay = win" | Movement wins |
| H3 | MF | dM/dF < 0 | Camuffo/Nanda: "$ = learning" | $ traps |
| H4 | VM | dM/dV (non-monotonic) | Stern: "Precise = good" | Both extremes trap |
| H5 | VD | dD/dV (regime-dependent) | — | Zoom-in vs Zoom-out |

---

## Panel G: PAE Framework (Module E)

| Step | Action | Purpose | Implementation |
|:----:|:-------|:--------|:---------------|
| **P** | Platformize | Expand stakeholder diversity | OEM + Manufacturers + Network |
| **A** | Acculturate | Establish dynamic protocol | Communicate volatility, pre-plan triggers |
| **E** | Evaluate | Build decision dashboard | Bayesian tracking, common knowledge |

---

## Notes

1. **Module Rename**: T (Traps) → V (Vagueness) for clarity
2. **Submodule Convention**: MG = dG/dM, MF = dM/dF, VM = dM/dV, VD = dD/dV
3. **Bridge (M3)**: Single paragraph (¶30) connecting MG and MF
4. **Sample**: N = 408,697 ventures (PitchBook 2021-2025)

---

*Structure Reference: Whiteboard diagram + thesis_v3_to_v4_summary.txt*
