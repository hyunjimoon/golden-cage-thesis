# Canonical Registry (CR.GLOSSARY) — v5

**Last updated**: Dec 31, 2024 (Day 3)
**Terminology shifts**: V→B, M→R/A, PAE→NFSC, E+C→C (merged)

---

## Core Construct (Locked)

| Construct | Definition | Version |
|:----------|:-----------|:-------:|
| **Nail with Flexibility, Scale with Commitment (NFSC)** | Ventures operationalize ambiguity during Nail phase (low-cost learning), then operationalize precision during Scale phase (high-volume execution). Transition occurs when dominant design is confirmed. | v5 |

**Theoretical foundation**: Fine (Evolutionary Entrepreneurship) + Stern (Bayesian Entrepreneurship)

---

## Variables (Locked v5)

| Var | Name | Definition | Operationalization | Owner |
|:---:|:-----|:-----------|:-------------------|:-----:|
| **F** | Funding | Early-stage capital | log($) raised at Seed/A | I |
| **G** | Growth | Scaling success | Total funding / Early VC | I |
| **B** | Breadth | Positioning scope | 0-100 percentile (higher = broader) | I |
| **R** | Repositioning | Directional change | B_T − B₀ (signed) | A |
| **A** | Absolute Repositioning | Change magnitude | \|R\| = \|B_T − B₀\| | A |

### Variable Evolution

| v4 | v5 | Reason |
|:---|:---|:-------|
| V (Vagueness) | **B (Breadth)** | Neutral framing (Charlie) |
| M (Movement) | **R (Repositioning)** | Precise terminology |
| D (Direction) | **R (signed)** | Merged into R |
| \|M\| | **A (Absolute)** | Clearer notation |

---

## Types (Locked)

| Type | Condition | Survival | Description |
|:-----|:----------|:--------:|:------------|
| **Stayer** | A ≈ 0 | 9.9% | No repositioning |
| **Zoom-in** | R < 0 (A > 0) | 17.5% | Increasing precision |
| **Zoom-out** | R > 0 (A > 0) | 18.4% | Increasing flexibility |

---

## Core Equations (Locked)

| ID | Equation | Meaning |
|:---|:---------|:--------|
| **EQ.PARADOX** | dG/dF = (dG/dA) × (dA/dF) < 0 | The Funding Paradox |
| **EQ.AG** | dG/dA > 0 | Repositioning Principle |
| **EQ.FA** | dA/dF < 0 | Funding Anchor |
| **EQ.TRAP** | μ(1−μ) < ε × B | Learning Trap Condition |

---

## Claims Registry

| ID | Statement | Module | Version | Dependents |
|:---|:----------|:------:|:-------:|:-----------|
| CLAIM.PARADOX | dG/dF < 0 | I | v2 | All |
| CLAIM.AG | dG/dA > 0 (Repositioners outperform stayers 1.82×) | AG | v2 | FA, B, C |
| CLAIM.FA | dA/dF < 0 (1-SD funding → 0.4 SD less repositioning) | FA | v2 | B, C |
| CLAIM.TRAP | μ(1−μ) < ε×B defines learning trap | B | v2 | C |
| CLAIM.LOCKIN | Funding triggers premature lock-in/lock-out | A | v5 | C |

---

## Module Structure (I-A-B-C) — Day 3 Update

| Module | Name | Role | Sub-modules | Key Scholar |
|:------:|:-----|:-----|:------------|:------------|
| **🔴I** | Introduction | The Puzzle | — | Ghemawat |
| **🟡A** | Absolute Repositioning | The "What" | AG (dG/dA), FA (dA/dF) | Van den Steen, Real Options |
| **⚪️B** | Breadth | The "Why" | BT (Trap), BD (Direction) | Bayesian Learning |
| **🔵C** | Conclusion | The "How" + Synthesis | C1, C2, C3, C4 | Fine + Stern |

### C Module Subsections (E+C Merged)

| Sub | Name | Paragraphs | Content |
|:---:|:-----|:-----------|:--------|
| **C1** | NFSC Definition | ¶81-84 | "Nail with Flexibility, Scale with Commitment" framework |
| **C2** | Q×Tools Mapping | ¶85-91 | Q1/Q2/Q3 × 10 Scaling Tools matrix |
| **C3** | Integrative Case | ¶92-95 | Motional case applying NFSC |
| **C4** | Closure | ¶96-98 | Contributions, limitations, coda |

### Module Dependencies

```
I (Introduction)
├── establishes F, G, B, R, A, core equation
│
├── A (Absolute Repositioning)
│   ├── AG: dG/dA > 0 (Van den Steen + Real Options)
│   └── FA: dA/dF < 0 (Camuffo-Nanda + Lock-in/Lock-out)  ← F→A naming
│
├── B (Breadth)
│   ├── BT: Learning trap μ(1−μ) < ε×B
│   └── BD: Direction effects (zoom-in vs zoom-out)
│
└── C (Conclusion) — E+C Merged
    ├── C1: NFSC Definition (¶81-84)
    ├── C2: Q×Tools Mapping (¶85-91)
    ├── C3: Integrative Case (¶92-95)
    └── C4: Closure (¶96-98)
```

---

## Theoretical Extensions

| Original Theory | Extension | Module |
|:----------------|:----------|:------:|
| Van den Steen (2017) | Object of commitment: position → process | AG |
| Ghemawat (1991) | Lock-in/Lock-out explains dA/dF < 0 | FA |
| Real Options | Funding violates "delay until uncertainty drops" | FA |
| Camuffo-Nanda | Selection effect precedes learning | FA |

---

## Key Statistics (Locked)

| Stat | Value | Source |
|:-----|:------|:-------|
| ρ(G,F) | −0.196 (p < 0.001, N = 408,697) | I |
| Repositioner survival | 18.0% | AG |
| Stayer survival | 9.9% | AG |
| Advantage ratio | 1.82× | AG |
| Funding → Repositioning | 1-SD F → 0.4 SD less A | FA |

---

## Terminology Do's and Don'ts

| DO use | DON'T use | Reason |
|:-------|:----------|:-------|
| Breadth (B) | Vagueness (V) | Neutral framing |
| Repositioning (R) | Movement (M) | Precise |
| Absolute Repositioning (A) | Adaptation | A ≠ fitness-improving |
| NFSC | PAE Framework | Day 3 update |
| Lock-in/Lock-out | Stakeholder constraint | Ghemawat terminology |

---

## File Naming Convention (v5 Day 3)

```
papers_v5/
├── 1_I_introduction/
│   └── I.md
├── 2_A_repositioning/       # Note: folder name, not "adaptation"
│   ├── AG.md
│   └── FA.md                # FA = F→A (cause→effect naming)
├── 3_B_breadth/
│   ├── BT.md (Trap)
│   └── BD.md (Direction)
├── 4_C_conclusion/          # E+C Merged
│   ├── C1.md (NFSC Definition, ¶81-84)
│   ├── C2.md (Q×Tools Mapping, ¶85-91)
│   ├── C3.md (Integrative Case, ¶92-95)
│   └── C4.md (Closure, ¶96-98)
├── CR.GLOSSARY.md           # This file
└── paper(thesis)_v5_prior.md
```

---

*Canonical Registry v5 Day 3 — Single source of truth for terminology*
