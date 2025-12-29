# Commit to Movement: Version 2.1
## 113 First Sentences + Key Figures + Tables

> **Core Equation**: dG/dF = (dG/dM)(dM/dF) < 0
> **North Star**: Growth needs movement. Funding can trap it.
> **Updated**: 2025-12-27

---

## Quick Reference: 10 Key Sentences

1. **¶02**: I find the opposite. Ventures that raise more funding show *lower* growth rates.
2. **¶04**: The decomposition: dG/dF = (dG/dM) × (dM/dF).
3. **¶23**: Movers outperform stayers 1.8×.
4. **¶33**: Funding suppresses movement: dM/dF < 0.
5. **¶34**: This is not Camuffo-Nanda being wrong. It is Camuffo-Nanda being incomplete.
6. **¶52**: The learning condition: μ(1−μ) < ε/V.
7. **¶60**: Vagueness preserves options but prevents learning.
8. **¶71**: The trap is particularly dangerous because it looks like success.
9. **¶97**: The mover's secret: expectation management.
10. **¶113**: Commit to movement, not to the promises that fund it.

---

## Key Figures

### Figure 1: Movement Predicts Growth (M_fig1_MGV)
```
[M Module] The Movement Principle: dG/dM > 0
- Movers outperform stayers 1.8× (18.0% vs 9.9% survival)
- Zoom-in: 17.5%, Zoom-out: 18.4%
```

### Figure 2: Funding Suppresses Movement (C_fig2_CAE_golden_cage)
```
[C Module] The Golden Cage Effect: dM/dF < 0
- +1 SD funding → 0.4 SD lower movement
- Effect 2× stronger for commitment-heavy deals
```

### Figure 3: Learning Trap Mechanism (T_fig1_trap_mechanism)
```
[T Module] Learning Trap Condition: μ(1−μ) < ε/V
- High-V trap: unfalsifiable hypotheses
- Low-V trap: belief variance collapse
```

### Figure 4: Three Archetypes (M_fig5_killer_movement)
```
[E Module] Escape Routes
- Stayer (M≈0): 9.9% survival - TRAPPED
- Zoom-in (ΔV<0): 17.5% survival - ESCAPES High-V trap
- Zoom-out (ΔV>0): 18.4% survival - ESCAPES Low-V trap
```

---

## Key Tables

### Table 1: Variable Definitions

| Symbol | Name | Definition | Operationalization |
|:------:|:-----|:-----------|:-------------------|
| **G** | Growth | Later Stage VC attainment | Series C/D+ reached |
| **F** | Funding | Capital raised | Log(total funding) |
| **M** | Movement | Strategic repositioning | \|ΔV\| = \|V_T - V_0\| |
| **V** | Vagueness | Strategic ambiguity | Rank-normalized (0-100) |

### Table 2: Three Archetypes

| Archetype | M | ΔV | Survival | Mechanism |
|:----------|:-:|:--:|:--------:|:----------|
| **Stayer** | ≈0 | 0 | 9.9% | Trapped: no movement |
| **Zoom-in** | >0 | <0 | 17.5% | Escapes high-V trap by focusing |
| **Zoom-out** | >0 | >0 | 18.4% | Escapes low-V trap by expanding |

### Table 3: Learning Trap Pathways

| Trap Type | V Level | Mechanism | Symptom | Escape Route |
|:----------|:-------:|:----------|:--------|:-------------|
| **High-V** | High | Unfalsifiable hypotheses | Vision alignment, no tests | Force specificity |
| **Low-V** | Low | Belief variance collapse | Echo chamber, no pivots | Add doubters |

### Table 4: E Module Case Studies

| Company | Type | V₀→V_T | E Level | Outcome | Lock-in Type |
|:--------|:-----|:-------|:--------|:--------|:-------------|
| Motional | Stayer | 81.9→81.9 | $4B | 40% layoffs | Corporate JV |
| Rubedos | Stayer | 81.9→81.9 | ~$0.5M | Limited growth | Grant capital |
| TuSimple | Stayer | Low→Low | $1.35B IPO | Collapse | Public market |
| Sky Engine | Mover | 28.4→89.1 | ~$2M | G=215.9× | Agile path |
| Nuro | Mover | Low→High | $2.13B | Pivot | Forced path |

---

## I — The Funding Paradox (¶01-11)

| ¶ | First Sentence |
|:--|:---------------|
| 01 | Strategy theory and investment practice share an implicit assumption: commitment attracts capital, capital enables coordination, coordination enables growth. |
| 02 | **I find the opposite.** Ventures that raise more funding show *lower* growth rates. ρ(G,F) = -0.196 (p < 0.001, N = 180,994). |
| 03 | This paper explains why. The answer lies in movement—the magnitude of strategic repositioning a venture undertakes. |
| 04 | **The decomposition: dG/dF = (dG/dM) × (dM/dF).** A positive times a negative yields the paradox. |
| 05 | I define three variables: E = external funding, M = movement (|ΔV|), G = growth (Later Stage VC). |
| 06 | Movement is not pivoting randomly. It is disciplined repositioning—Parallel Experimentation → Strategic Convergence. |
| 07 | The null hypothesis comes from strategy theory: "strategic positions should have a horizon of a decade or more" (Porter, 1996). |
| 08 | **My finding challenges this implicit assumption.** Movers outperform stayers 1.8×. |
| 09 | Three patterns emerge: stayers (M≈0, 9.9%), zoom-in (M>0, ΔV<0, 17.5%), zoom-out (M>0, ΔV>0, 18.4%). |
| 10 | Traps occur at both extremes. High-V: can't zoom in. Low-V: can't zoom out. |
| 11 | **The prescription: commit to movement, not to the promises that fund it.** |

---

## M — What Moves, Grows (¶12-48)

### M1: Strategy Gospel (¶12-20)

| ¶ | First Sentence |
|:--|:---------------|
| 12 | Van den Steen (2017) formalizes why commitment creates strategic value: "Strategy is the smallest set of choices to optimally guide other choices." |
| 13 | This logic has profound implications. If commitment creates coordination value, repositioning destroys it. |
| 14 | Van den Steen's framework assumes the committed position is correct. |
| 15 | **I propose that Van den Steen's mechanism remains valid, but his scope condition does not hold.** |
| 16 | I define Movement as M = \|ΔV\|, the magnitude of change in strategic vagueness. |
| 17 | Movement is not random pivoting. It is disciplined repositioning—Bayesian updating. |
| 18 | Three movement types emerge: stayers (M≈0), zoom-in (M>0, ΔV<0), zoom-out (M>0, ΔV>0). |
| 19 | **If dG/dM > 0, Van den Steen's framework extends rather than collapses.** |
| 20 | The empirical question is now precise: do ventures that move outperform those that stay? |

### M2: Empirics (¶21-29)

| ¶ | First Sentence |
|:--|:---------------|
| 21 | Van den Steen's framework generates a clear prediction: stayers should outperform movers. |
| 22 | Movement M is computed as \|ΔV\|. Growth G = Later Stage VC (C/D+). |
| 23 | **The core finding: movers outperform stayers 1.8× (18.0% vs 9.9%).** |
| 24 | Regression confirms: +7.3 pp survival per 1 SD movement (p < 0.001). |
| 25 | Direction matters. Zoom-in: 17.5%. Zoom-out: 18.4%. |
| 26 | **The finding challenges Van den Steen's scope, not his mechanism.** |
| 26a | Why extend Van den Steen rather than Porter? Porter addresses *where* to compete; Van den Steen addresses *why* commitment creates value. |
| 27 | Alternative explanation: perhaps movers are simply better founders? Cohort fixed effects and propensity matching confirm: movement premium persists. |
| 28 | Perhaps movement proxies for learning? This is not an alternative—it is the mechanism. |
| 29 | **The Movement Principle (dG/dM > 0) is established.** |

### M3: Bridge (¶30)

| ¶ | First Sentence |
|:--|:---------------|
| 30 | **The funding paradox decomposes into two testable claims.** dG/dM > 0 (M1-M2), dM/dF < 0 (M4-M5, T1-T4). |

### M4: Bayesian Gospel (¶31-39)

| ¶ | First Sentence |
|:--|:---------------|
| 31 | Entrepreneurship is experimentation. Camuffo and colleagues formalized this. |
| 32 | I test this assumption. If capital enables experimentation, then dM/dF > 0. |
| 33 | **I find the opposite. Funding suppresses movement: dM/dF < 0.** |
| 34 | **This is not Camuffo-Nanda being wrong. It is Camuffo-Nanda being incomplete.** This is the selection effect: investors fund confident visions. |
| 35 | The mechanism operates in **two stages**: Stage 1 (Selection): Commitment → Capital. Stage 2 (Lock-in): Capital → Reinforcement. |
| 36 | Consider the founder who raises $5M. She wants to experiment—but experiments that falsify the funded vision threaten investor relationships. |
| 37 | **This extends experimental entrepreneurship.** Capital enables in principle; commitment impedes in practice. |
| 38 | Heterogeneity supports: dM/dF < 0 effect is 2× stronger when commitment is strongest. |
| 39 | Module M5 tests the core claim: dM/dF < 0. |

### M5: Empirics (¶40-48)

| ¶ | First Sentence |
|:--|:---------------|
| 40 | I now test whether funding suppresses strategic movement. |
| 41 | Using 408,697 ventures from PitchBook (2010-2023). |
| 42 | **Core finding: +1 SD funding → 0.4 SD lower movement (p < 0.001).** |
| 43 | Causal identification uses funding shocks: when lead VC's fund closes unexpectedly, affected ventures move MORE. |
| 44 | Mechanism test: dM/dF < 0 effect is 2× stronger for single-lead deals, milestone-heavy terms, high belief alignment. |
| 45 | Timing matters. Early-stage funding shows stronger dM/dF < 0. |
| 46 | Pattern is consistent with commitment constraining experimentation. |
| 47 | **Summary: The Funding Trap is empirically confirmed.** dG/dF = (dG/dM > 0) × (dM/dF < 0) < 0. |
| 48 | The Camuffo-Nanda framework is now extended. Module T explains why: High-V and Low-V traps. |

---

## T — When Commitment Traps (¶49-80)

### T1: Coords (¶49-56)

| ¶ | First Sentence |
|:--|:---------------|
| 49 | The Funding Trap (dM/dF < 0) operates through two mechanisms. |
| 50 | **I frame traps as process failures, not outcome failures.** A trap is where learning halts. |
| 51 | Traps occur at both extremes of vagueness: High-V (too vague) and Low-V (too specific). |
| 52 | **The learning condition formalizes this: μ(1−μ) < ε/V.** |
| 53 | Funding accelerates trap formation through two pathways. |
| 54 | Each mechanism has distinct signature. High-V: unfalsifiable hypotheses. Low-V: belief homogenization. |
| 55 | The E×E matrix maps trap probability. High funding + low diversity = maximum trap. |
| 56 | Modules T2-T3 detail each mechanism. T4 synthesizes. |

### T2: High-V Trap (¶57-64)

| ¶ | First Sentence |
|:--|:---------------|
| 57 | **High-V trap mechanism: options preserved → learning prevented.** |
| 58 | The learning condition: μ(1−μ) < ε/V. High V lowers threshold—but without specificity, nothing to reject. |
| 59 | High-V founders attract believers who share their grand vision. Agreement is easy when definitions are loose. |
| 60 | **The flexibility trap paradox: vagueness preserves options but prevents learning.** |
| 61 | The mechanism has two components: internal (can't design discriminating tests) and external (can't hold accountable). |
| 62 | Data shows: High-V ventures show more vision alignment but less movement. |
| 63 | **High-V ventures need to zoom in. But investors reward vagueness.** |
| 64 | **Escape requires forcing specificity before funding.** |

### T3: Low-V Trap (¶65-72)

| ¶ | First Sentence |
|:--|:---------------|
| 65 | **Low-V trap mechanism: commitment lock-in → pivot impossible.** |
| 66 | Staw's (1976) escalation research: decision-makers "become locked into a course of action." |
| 67 | The echo chamber forms naturally. Precise visions attract investors who believe that exact thesis. |
| 68 | **The learning condition: μ(1−μ) < ε/V. Low V raises threshold; μ→1 collapses variance.** |
| 69 | Data confirms: High investor-founder alignment correlates with lower survival when markets shift. |
| 70 | Examples: Biotech locked into specific indications. Deep tech committed to particular applications. |
| 71 | **The trap is particularly dangerous because it looks like success.** Hitting milestones feels like progress. |
| 72 | **Escape requires belief diversity before funding.** Add a doubter. |

### T4: Synthesis (¶73-80)

| ¶ | First Sentence |
|:--|:---------------|
| 73 | **Both extremes trap ventures.** Too vague: unfalsifiable. Too specific: commitment lock-in. |
| 74 | The unified trap equation: μ(1−μ) < ε/V captures both failures. |
| 75 | **Funding accelerates both traps.** High-V attracts vision investors; Low-V attracts execution investors. |
| 76 | This completes dM/dF < 0 mechanism. Funding selects for stakeholders who resist movement. |
| 77 | Data shows pattern across industries. Mobility (high-V): 91% stayer, 5% survival. |
| 78 | The stayer archetype (M≈0) has two origins: trapped at high-V or trapped at low-V. |
| 79 | **Escape requires different prescriptions.** High-V: specificity. Low-V: diversity. |
| 80 | **The funding paradox is now explained.** dG/dF < 0 because (dG/dM > 0) × (dM/dF < 0). |

---

## E — Who Moved? (¶81-104)

### E1: Tempo (¶81-86)

| ¶ | First Sentence |
|:--|:---------------|
| 81 | **We return to the Funding Paradox with new understanding.** The decomposition is complete. |
| 82 | But explanation is not prescription. Understanding traps doesn't tell how to escape. |
| 83 | Three patterns: Stayer (M≈0, 9.9%), Zoom-in (M>0, ΔV<0, 17.5%), Zoom-out (M>0, ΔV>0, 18.4%). |
| 84 | The escape prescription follows from trap diagnosis. |
| 85 | **The competitive landscape illustrates V-dimension trade-off: Waymo (Low-V) vs Tesla (High-V).** The core battle isn't LiDAR vs. cameras—it's managing the strategic value of ambiguity. |
| 86 | But some ventures escape. E2-E3 examines stayers and movers. |

### E2: Stayer Examples (¶87-92)

| ¶ | First Sentence |
|:--|:---------------|
| 87 | **Stayers and movers face identical uncertainty.** The difference lies in commitment structure. |
| 88 | **Rubedos (Grant lock-in)**: 15+ years, EU funds tied to specific projects. V₀=81.9→V_T=81.9. |
| 89 | **Motional (Corporate lock-in)**: $4B JV = Low-V Trap "Echo Chamber." Three symptoms align with leadership needs: (1) Identity vs Expansion tension, (2) Sequential approach risk, (3) Need for decision-making basis. |
| 90 | **TuSimple (Public market lock-in)**: $1.35B IPO, identity fixed in prospectus. Collapsed. |
| 91 | Three lock-in mechanisms: Grant (legal), Corporate (interdependence), Public (expectations). All suppress M. |
| 92 | **The stayer archetype is not a strategy—it's a symptom.** Funding structures freeze movement. |

### E3: Mover Examples (¶93-98)

| ¶ | First Sentence |
|:--|:---------------|
| 93 | **Movers escape traps through deliberate repositioning.** Two patterns: agile vs forced. |
| 94 | **Sky Engine (Agile)**: V₀=28.4→V_T=89.1, ~$2M seed, G=215.9×. Low E preserved optionality. |
| 95 | **Nuro (Forced)**: $2.13B → crisis → pivot to "Nuro Driver" licensing. High E required failure first. |
| 96 | Both succeed through movement, but mechanisms differ. Agile: voluntary. Forced: crisis-induced. |
| 97 | **The mover's secret: expectation management.** Sky Engine maintained ambiguity; Nuro required visible failure. |
| 98 | Prescription: Delay large capital until identity crystallizes, or manage expectations proactively (Aurora model). |

### E4: Synthesis (¶99-104)

| ¶ | First Sentence |
|:--|:---------------|
| 99 | **Escape requires movement, but two paths exist.** Agile (early, cheap) vs Forced (late, costly). |
| 100 | **Agile Path**: Sky Engine—low early E, freedom to redefine identity, voluntary movement. G=215.9×. |
| 101 | **Forced Path**: Nuro—high E, locked identity, crisis-induced pivot. Movement happened but at enormous cost. |
| 102 | Path depends on funding stage, not preference. Early-stage can choose Agile; late-stage faces Forced. |
| 103 | **Aurora Model for Motional**: Zoom Out to reclaim optionality. Reframe "robotaxi" → "full-stack autonomy provider for HMG." **3-Phase Implementation**: (1) Diagnosis—quantify V,M,trap risk; (2) Simulation—model Zoom Out scenarios; (3) Dashboard Build—E2E strategic planning tool. |
| 104 | **Prescription**: (1) Diagnose E level + V position, (2) Pre-lock-in: delay capital, (3) Post-lock-in Low-V: Aurora model (zoom out), (4) Post-lock-in High-V: zoom in. **E2E Dashboard**: Bayesian control + Adaptive protocol + Dynamic simulation. |

---

## C — Commit to Move (¶105-113)

### C1: Implications (¶105-108)

| ¶ | First Sentence |
|:--|:---------------|
| 105 | **[Founders]** You raised capital to accelerate learning, but the more you raise, the harder it becomes to change course. dG/dF < 0 in early-stage. |
| 106 | **[Founders]** Consider separating internal compass from external pitch. Track |ΔV|. Frame strategy as provisional. |
| 107 | **[Investors]** Your conviction alignment may be a risk factor. When everyone agrees, belief variance collapses. |
| 108 | **[Investors]** Structure terms that permit pivoting. Replace milestone rigidity with learning milestones. |

### C2: Boundary (¶109-112)

| ¶ | First Sentence |
|:--|:---------------|
| 109 | **Limitation—selection bias**: Successful zoom-in ventures "graduate" from dataset early. |
| 110 | **Limitation—generalizability**: Mobility finding (V₀=78, 91% stayer) may not extend everywhere. |
| 111 | **New problem—investor behavior**: VC practices need restructuring. Select for diversity, not alignment. |
| 112 | **New problem—trap detection**: Can we identify traps before they form? Early warning indicators needed. |

### C3: Coda (¶113)

| ¶ | First Sentence |
|:--|:---------------|
| 113 | **Contributions.** Layer 1: M=\|ΔV\|, dG/dM>0, dM/dF<0. Layer 2: Decomposition. Layer 3: μ(1−μ)<ε/V. **必死卽生, 必生卽死.** |

---

## Appendix: Notation Summary

```
Core Equation:
dG/dF = (dG/dM) × (dM/dF) < 0

Where:
- dG/dM > 0 : Movement Principle (M module)
- dM/dF < 0 : Funding Trap (M4-M5, T module)

Learning Trap Condition:
μ(1−μ) < ε/V

Where:
- μ : Believer ratio (confidence level)
- μ(1−μ) : Belief variance (maximized at μ=0.5)
- V : Vagueness (inversely related to precision τ)
- ε : Learning threshold
```

---

*必死卽生, 必生卽死*
*Commit to Movement.*
