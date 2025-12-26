# 🌱 Discussion Module - Table of Contents

## Module D (Lines 105-113) = 9 paragraphs

*Musical Tempo: Allegro vivace — CODA*

---

## 🎼 D as Coda

```
┌─────────────────────────────────────────────────────────────┐
│  SONATA FORM OF THESIS                                      │
│                                                             │
│  M (Exposition)      → Introduce themes                     │
│  C (Development)     → Vary themes                          │
│  T (Recapitulation)  → Return with deeper meaning           │
│  D (CODA)            → Conclude + Synthesize                │
│                                                             │
│  D(112) is where LTE Theory contribution goes               │
└─────────────────────────────────────────────────────────────┘
```

### Structure

```
┌────────────────────────────────────────────────────────────┐
│  🌐 ALL (105)               │  1 paragraph   │ Meta-level │
├────────────────────────────────────────────────────────────┤
│  👤 ENTREPRENEUR (106)      │  1 paragraph   │ ENT advice │
├────────────────────────────────────────────────────────────┤
│  💰 INVESTOR (107)          │  1 paragraph   │ INV advice │
├────────────────────────────────────────────────────────────┤
│  ⚠️ LIMITATIONS (108-110)   │  3 paragraphs  │ Boundaries │
├────────────────────────────────────────────────────────────┤
│  🔗 LINKED [M][C][T] (111-112)│ 2 paragraphs │ Contributions│
├────────────────────────────────────────────────────────────┤
│  🏁 CONCLUDE (113)          │  1 paragraph   │ Final      │
└────────────────────────────────────────────────────────────┘
```

---

## 🌐 Line 105: ALL — Meta-Level Insight

**Content**: Multiple ways to grow

| Path | Start | Direction | Works? |
|:-----|:-----:|:---------:|:------:|
| 🔴 Zoom In | High V₀ | Focus | ✅ (with capacity) |
| 🔵 Zoom Out | Low V₀ | Expand | ✅ |
| 🟢 Horizontal | Any | Lateral | ⚠️ OK |
| ⚫ Stayer | Any | None | ❌ Worst |

---

## 👤 Line 106: ENTREPRENEUR — Commit to Adaptation

| DO | DON'T |
|:---|:------|
| ✅ **Commit to adaptation** | ❌ Commit to specific outcome |
| ✅ Practice **Bayesian hygiene** | ❌ Surround with believers only |
| ✅ Include DOUBTERS deliberately | ❌ Create echo chambers |

---

## 💰 Line 107: INVESTOR — Open to Adaptation

| DO | DON'T |
|:---|:------|
| ✅ **Open to adaptation** | ❌ Lock founders into thesis |
| ✅ Fund trajectories | ❌ Over-index on positioning |

---

## ⚠️ Lines 108-110: LIMITATIONS

| Line | Content |
|:----:|:--------|
| 108 | Data quality, G7 misalignment |
| 109 | Validity: G₁ (financial) vs G₂ (operational) |
| 110 | (continues) |

---

## 🔗 Lines 111-112: LINKED Contributions

### Line 111: [M][C] Industry & Time Heterogeneity

- Results differ by **industry** and **time**
- **Hype industries** (AI, Crypto) → dG/dE shifts more negative

---

### Line 112: [T] LTE Theory Contribution

**⚠️ THIS IS THE METHODOLOGICAL CONTRIBUTION**

Based on Cronin et al. (2025) "Layers of Theoretical Explanation" framework:

```
┌─────────────────────────────────────────────────────────────┐
│  LAYERS OF THEORETICAL EXPLANATION (LTE)                    │
│  ═══════════════════════════════════════                    │
│                                                             │
│  LAYER 1: CONSTRUCT (What relationships exist?)             │
│  ──────────────────────────────────────────────             │
│  Module M: Observable construct relationships               │
│  • τ → Funding (α₁ < 0)                                     │
│  • τ → Success (β₁ > 0)                                     │
│  • dG/dA > 0 (Movement Principle)                           │
│  Method: Covariance, regression on N=488,381 ventures       │
│                                                             │
│  LAYER 2: PROCESS (How do actions unfold over time?)        │
│  ──────────────────────────────────────────────             │
│  Module C: Action/event sequences in context                │
│  • Vague promise → Multiple interpretations                 │
│  • Diverse interpretations → Diverse stakeholders join      │
│  • Diverse coalition → Learning opportunities               │
│  • Learning → Adaptation → Success                          │
│  Method: Case studies (4 variations), E×E matrix            │
│                                                             │
│  LAYER 3: MECHANISM (Why do actors behave this way?)        │
│  ──────────────────────────────────────────────             │
│  Module T: GENERATIVE MECHANISMS that cause Layer 2         │
│  • Learning trap equation: μ(1−μ) < ε/(V+1)                 │
│  • Optimist's echo chamber mechanism                        │
│  • Doubter prescription as intervention                     │
│  Method: Formal equation + Computational simulation         │
└─────────────────────────────────────────────────────────────┘
```

### LTE Contribution to Organization Science

| Traditional Org Science | This Dissertation (LTE Approach) |
|:------------------------|:---------------------------------|
| Verbal theory | Formal equation: μ(1−μ) < ε/(V+1) |
| Case studies only | Case + Large-N (488K ventures) |
| Static analysis | Computational simulation |
| Explanation focus | Prediction + Intervention design |
| "Increase X to improve Y" | Specific actions for specific actors |

### What-How-Why Framework

| Question | Module | Layer | Contribution |
|:---------|:------:|:-----:|:-------------|
| **WHAT** | M | 1 (Construct) | Movement Principle: dG/dA > 0 |
| **HOW** | C | 2 (Process) | Fund2Cage: Funding → Commitment → Rigidity |
| **WHY/WHEN** | T | 3 (Mechanism) | Learning trap: μ(1−μ) < ε/(V+1) |

### Computational Simulation as Layer 3 Validation

```
PURPOSE: Validate generative mechanism under controlled conditions

SIMULATION DESIGN:
├── Generate N ventures with varying V, μ, τ
├── For each venture:
│   ├── Stakeholder coalition forms based on θ* = μ + kσ
│   ├── Belief updating occurs based on P(join|τ, θᵢ)
│   └── Check if trap condition satisfied
├── Track which combinations trigger trap
└── Compare predicted vs. observed Q patterns

VALIDATION RESULTS:
┌──────────┬─────────────┬─────────────┬─────────┐
│ Quartile │ Predicted   │ Observed    │ Match?  │
│          │ (Simulation)│ (Data)      │         │
├──────────┼─────────────┼─────────────┼─────────┤
│ Q1       │ High trap   │ 12.3%       │ ✅      │
│ Q2       │ Medium trap │ 8.9%        │ ✅      │
│ Q3       │ Low trap    │ 16.0%       │ ✅      │
│ Q4       │ Medium      │ 12.9%       │ ✅      │
└──────────┴─────────────┴─────────────┴─────────┘
```

### Why This Matters (Cronin et al. 2025)

> "Process theorizing provides improved causal inference that better specifies the **who, what, where, when, why and how** of organizational behavior and, hence, provides **more precise specification for the design of organizational interventions**."

**For Entrepreneurs**: Not just "be more flexible" → Specific actions:
- IF high-μ founder, THEN deliberately recruit doubters
- IF precise promise, THEN monitor belief variance
- IF low movement rate, THEN check for echo chamber

**For Investors**: Not just "fund good teams" → Specific signals:
- Evaluate adaptation CAPACITY, not just current position
- Value teams with belief diversity
- Monitor for commitment trap indicators

---

## 🏁 Line 113: CONCLUDE

| What We Know | Confidence | Layer |
|:-------------|:-----------|:-----:|
| Movement > Position | HIGH | 1 |
| Fund2Cage exists | MEDIUM | 2 |
| Q3 optimality | MEDIUM | 1-2 |
| LTE mechanism | MEDIUM | 3 |

> Certainty is expensive; honesty is cheap.
> 必死卽生, 必生卽死

---

## 📊 Summary Table

| Line | Content | Module Link | LTE Layer |
|:----:|:--------|:------------|:---------:|
| 105 | **ALL**: Multiple ways to grow | I, M, C | — |
| 106 | **ENT**: Commit to adaptation | T | 3 |
| 107 | **INV**: Open to adaptation | M, C | 2 |
| 108-110 | Limitations | — | — |
| 111 | **[M][C]**: Industry/time heterogeneity | M, C | 1-2 |
| 112 | **[T]**: LTE contribution | T | **1-2-3** |
| 113 | **Conclude** | ALL | — |

---

## 🔗 T Empirics vs D(112) — Clear Separation

```
T EMPIRICS (93-100)                    D(112)
────────────────────                   ─────────────────────
SUBSTANTIVE FINDING                    METHODOLOGICAL CONTRIBUTION
(Why Q3 wins)                          (How we built/validated theory)

Part A: 😊 Benefit of vague            Layer 1: Construct (M)
        (high mover proportion)              → What relationships?
                                       
Part B: 😭 Cost of precise             Layer 2: Process (C)
        (Optimist's echo chamber)            → How do actions unfold?
                                       
                                       Layer 3: Mechanism (T)
                                             → Why? (formal equation)
                                             → Computational simulation
                                       
────────────────────                   ─────────────────────
"Q3 works because..."                  "Our theory works because..."
```

---

## Navigation

| Module | Lines | Link |
|--------|-------|------|
| I Introduction | 1-11 | [toc(i).md](../1_I_introduction/toc(i).md) |
| M Movement | 12-48 | [toc(m).md](../2_M_movement/toc(m).md) |
| C Fund2Growth | 49-80 | [toc(c).md](../3_C_cash2growth/toc(c).md) |
| T Commit2Trap | 81-104 | [toc(t).md](../4_T_commit2trap/toc(t).md) |
| **D Discussion** | 105-113 | *You are here* |

---

*必死卽生, 必生卽死*

**Commitment and Flexibility in Entrepreneurship**
Hyunji Moon, MIT Sloan
Advisors: Charlie Fine (Operations) & Scott Stern (Strategy)
