# Variable System: Notation Reference

## Core Variables (Use V, not τ)

| Symbol | Name | Definition | Range | Unit |
|--------|------|------------|-------|------|
| **V** | Vagueness | Initial positioning ambiguity (breadth of market positioning) | 0-100 | Dimensionless (High V = vague) |
| **V₀** | Initial Vagueness | Vagueness at first observation | 0-100 | Dimensionless |
| **V_T** | Terminal Vagueness | Vagueness at final observation | 0-100 | Dimensionless |
| **D** | Direction | V_T - V₀ (signed change) | Any | Dimensionless (+ = zoom out, - = zoom in) |
| **A** | Realized Adaptation | \|D\| = \|V_T - V₀\| (actual movement) | ≥ 0 | Dimensionless |
| **E** | Early Funding | Seed/Series A funding amount | Continuous | log(USD) |
| **G** | Growth | Funding multiple: F_t / E | Continuous | Multiple |
| **L** | Later-stage Success | Binary: reached Later Stage VC = 1 | 0, 1 | Binary |

## Derived Measures

| Symbol | Definition | Interpretation |
|--------|------------|----------------|
| **ρ(X,Y)** | Spearman rank correlation | Non-parametric monotonic association |
| **dG/dA** | Marginal effect of adaptation on growth | Movement Principle (+) |
| **dA/dE** | Marginal effect of capital on adaptation | Cash2Cage mechanism (−) |
| **dG/dE** | Total effect of capital on growth | Cash Paradox (compound) |

## Core Equations

```
MOVEMENT PRINCIPLE:     dG/dA > 0      (movement helps growth)
CASH2CAGE:              dA/dE < 0      (capital constrains movement)
CASH PARADOX:           dG/dE = (dG/dA)(dA/dE) = (+)(−) < 0

LEARNING TRAP (🪤T):    μ(1−μ) < ε/(V+1)
                        Low V → Low learning capacity → TRAP
```

## Bayesian Updating (from mechanism_calling_simulation.pdf)

**Equation 3.1 (Posterior Update)**:
$$\mu_{posterior} = \frac{\tau \cdot \mu_{prior} + n \cdot \bar{x}}{\tau + n}$$

Where:
- μ = Aspiration level (boldness)
- τ = Precision (note: V = 1/τ for vagueness)
- n = Operational complexity / sample size
- x̄ = Observed mean

**Equation 3.2 (Adjustment-of-Commitment Cost)**:
$$AOC = Sunk + Stakeholder\ Resistance + Identity\ Disruption$$

**Equation 3.6 (Mechanism Chain)**:
$$\frac{dY}{dE} = \frac{\partial Y}{\partial |ΔV|} \cdot \frac{\partial |ΔV|}{\partial E} = (+)(−) < 0$$

## Mover Classification

| Type | Condition | V₀ → V_T | Direction |
|------|-----------|----------|-----------|
| **Zoom In** | D < 0 | Vague → Precise | Focusing |
| **Stayer** | D ≈ 0 | No change | Static |
| **Horizontal** | D ≈ 0* | Keywords change | Thrashing |
| **Zoom Out** | D > 0 | Precise → Vague | Broadening |

*Note: Keywords change but V level similar

---

*Variable definitions consistent across all modules. See angie_golden_cage_draft.pdf Table 2.2 for company examples.*
