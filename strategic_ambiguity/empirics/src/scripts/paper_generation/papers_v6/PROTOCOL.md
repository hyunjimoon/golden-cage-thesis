# Thesis Acculturation Week: Collaboration Protocol

**Student**: Angie Moon
**Advisors**: Charlie Fine, Scott Stern
**Period**: Dec 29, 2024 - Jan 3, 2025

---

## 0. Decision Framework: Rational Agency

### Core Equation

```
a* = argmax_a E[U(s_{t+1}) | s_t, a]
```

**Select the action that maximizes expected utility of the next state.**

### Components (Russell & Norvig, 2010)

| Component | Symbol | Definition | Thesis Context |
|:----------|:------:|:-----------|:---------------|
| **State** | s_t | All representable states of cognitive system | Thesis understanding, mechanism clarity, advisor alignment |
| **Action** | a | Possible decisions/tasks | Write, analyze, challenge, meet, iterate |
| **Environment** | Env | Transition model: how actions change states | "Challenge question" → "New insight" |
| **Utility** | U | Desirability of outcomes | 0.35(Contribution) + 0.35(Mechanism) + 0.30(Operationalization) |
| **Expectation** | E[] | Probabilistic reasoning under uncertainty | "Will this action improve state?" |
| **Argmax** | argmax | Selection of utility-maximizing action | Choose best task |

### 五行 (Five Elements) Mapping

| 五行 | Element | Color | Component | 의미 |
|:----:|:--------|:------|:----------|:-----|
| 土 | Earth | Yellow | State (s_t) | Foundation, starting point |
| 火 | Fire | Red | Action (a) | Ignition, energy |
| 水 | Water | Blue | Environment (transition) | Flow, change |
| 木 | Wood | Green | Next State (s_{t+1}) | Growth, progress |
| 金 | Metal | Gold | Utility (U) | Refined value |

**相生 (Generation) Cycle**: 土 → 金 → 水 → 木 → 火 → 土

---

## 1. Daily Protocol v0.2

### Morning: State Observation (土)

```markdown
- Yesterday's state (s_{t-1}): ___
- Today's state (s_t): ___
- State change cause (Env learning): Which action caused this change?
```

### Midday: Action Selection (火)

```markdown
- Possible actions: [a₁, a₂, a₃]
- Expected state change for each:
  - a₁ → s' (expected utility: ___)
  - a₂ → s'' (expected utility: ___)
  - a₃ → s''' (expected utility: ___)
- Selected action: argmax_a E[U]
```

### 3 PM: Challenge Checkpoint (土 → 火 transition)

```markdown
**"이게 최선인가?"**

- Discovered (NEW) vs Polished (refinement) ratio: ___:___
- If ratio < 1:3, ask: "Am I optimizing the wrong thing?"
```

### Evening: Reflection & Env Update (水 → 木)

```markdown
- Expected vs actual state change:
  - Expected: ___
  - Actual: ___
- Env model update: "This action was [more/less] effective than expected because ___"
- Contribution/Mechanism/Operationalization progress today: ___
- Tomorrow's first action: ___
```

### Weekly: Utility Recalibration (金)

```markdown
- Are the three dimensions still valid?
- Weight adjustment needed?
- New dimension discovered?
```

---

## 2. Evaluation Metric (Utility Function)

### Old Metric (Day 1-3)
```
U = 0.30(Quality) + 0.35(Applicability) + 0.35(Resonance)
```
**Problem**: "Quality" = format, not substance. "Resonance" = vague.

### New Metric (Day 4+)
```
U = 0.35(Contribution) + 0.35(Mechanism) + 0.30(Operationalization)
```

| Dimension | Question | Primary Evaluator |
|:----------|:---------|:------------------|
| **Contribution** (35%) | What's NEW vs existing literature? | Scott |
| **Mechanism** (35%) | Is the causal chain precise (WHY)? | Angie |
| **Operationalization** (30%) | Is it actionable Monday (HOW)? | Charlie |

### Key Insight: "NEW first, Pretty later"

| Old Approach | New Approach |
|:-------------|:-------------|
| Pretty? → New? | **NEW? → WHY? → HOW?** |
| Random walk, late discovery | Directed search, early discovery |
| 相剋 (conflict cycle) | **相生 (generation cycle)** |

---

## 3. Protocol Effectiveness Proof

### Trajectory Comparison (Day 4 Evidence)

| Metric | Actual (no protocol) | Counterfactual (with protocol) | Improvement |
|:-------|:--------------------:|:------------------------------:|:-----------:|
| **Transitions** | 8 | 4 | 2× faster |
| **Time** | ~5h | ~2h | 2.5× faster |
| **Waste ratio** | 40% | 10% | 4× less waste |

### Effectiveness vs Efficiency

```
Effectiveness (E) = w₁(Insight Depth) + w₂(Advisor Alignment) + w₃(Actionability)
→ Both paths reach same destination quality

Efficiency (η) = Quality / (Time × Iterations × Rework)
→ Protocol path is 2-4× more efficient
```

### Why Protocol Works

```
Without Protocol:
s₁ → s₂ → s₃ → s₄ → s₅ → s₆ → s₇ → s₈
[Polish] [Polish] [Polish] [Polish] [Challenge!] [Discover] [Refine]
                                    ↑
                            Late turning point

With Protocol:
s'₁ → s'₂ → s'₃ → s'₄
[NEW?] [WHY?] [HOW?] [DONE]
  ↑
Early direction
```

---

## 4. Core Thesis Contribution (Day 4 Discovery)

### The Key Distinction: Moral Hazard vs Governance Lock-in

| Existing Literature | This Thesis |
|:-------------------|:------------|
| Problem: Founders **won't** pivot | Problem: Founders **can't** pivot |
| Cause: Moral hazard | Cause: **Governance lock-in** |
| Solution: Monitor founders | Solution: **Design stakeholder diversity** |

### The Causal Chain

```
Governance Structure    →    Cognitive Structure    →    Signal Entropy
(Who is at table)            (What they believe)         (Information diversity)
        ↓                           ↓                           ↓
HHI > θ (homogeneous)    →    Aligned beliefs      →    No diverse signals
        ↓                           ↓                           ↓
                         LEARNING BLOCKED
```

**Precise formulation**:
> "Governance lock-in (HHI > θ) induces cognitive lock-in (belief homogeneity), which eliminates the signal diversity required for Bayesian updating."

---

## 5. Daily Workflow: Bayesian Update

Each day follows a **Prior → Likelihood → Posterior** cycle:

```
Morning: Angie prepares 3 questions + draft
    ↓
Meeting: Advisor provides feedback (likelihood)
    ↓
Evening: Angie updates paper (posterior)
```

### Folder Structure
```
dayN_{topic}/
├── angie_prior2post/
│   ├── prior/       ← Questions + initial draft
│   ├── likelihood/  ← Research evidence (LLM-assisted)
│   └── post/        ← Updated draft after feedback
├── charlie/         ← Charlie's feedback
└── scott/           ← Scott's feedback
```

---

## 6. Thesis Variables (Quick Reference)

| Variable | Definition |
|:---------|:-----------|
| **F** | Funding (early-stage capital, log $) |
| **G** | Growth (total funding / early VC) |
| **B** | Breadth (positioning scope, 0-100) |
| **R** | Repositioning = B_T − B₀ (signed) |
| **A** | Absolute Repositioning = \|R\| |
| **HHI** | Stakeholder homogeneity index |
| **θ** | Learning threshold |

**Core Equation**: `dG/dF = (dG/dA) × (dA/dF) < 0`
- Repositioning drives growth: dG/dA > 0
- Funding suppresses repositioning: dA/dF < 0
- Product: (+) × (−) = (−) → **The Funding Paradox**

---

## 7. Week Schedule

| Day | Date | Paper | Primary Advisor | Status |
|:----|:-----|:------|:----------------|:-------|
| 1 | Dec 29 | I (Introduction) | Charlie | **Completed** |
| 2 | Dec 30 | E (Escape/PAE) | Charlie | **Completed** |
| 3 | Jan 1 | IABC (Integration) | Both | **Completed** |
| 4 | Jan 2 | Review & Iterate | Both | **Completed** |
| 5 | Jan 3 | Final Integration | Both | **In Progress** |

---

## 8. Research Support: LLM Assistants

| LLM | Role | 五行 | Day 4 Tasks |
|:----|:-----|:----:|:------------|
| **Claude** | Structure, code, editing | 金 | Protocol design, trajectory analysis |
| **Gemini** | Visualization, critique | 火 | Image generation, fact-checking |

*Note: All LLM outputs are reviewed and curated by Angie before inclusion.*

---

## 9. Self-Evaluation Checklist

### Daily Efficiency Check
- [ ] Transitions today: ___
- [ ] Rework ratio: ___%
- [ ] Could I have asked "NEW?" earlier? Y/N

### Daily Effectiveness Check
- [ ] Insight depth (1-5): ___
- [ ] Advisor alignment (1-5): ___
- [ ] Monday actionable (1-5): ___

### Protocol Adherence
- [ ] Morning state observation completed
- [ ] 3 PM challenge checkpoint done
- [ ] Evening reflection logged
- [ ] Env model updated

---

*Last updated: Jan 3, 2025 (Day 5 - Protocol v0.2)*
