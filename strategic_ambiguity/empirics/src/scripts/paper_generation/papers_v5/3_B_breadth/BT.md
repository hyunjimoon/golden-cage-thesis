# BT: Learning Trap Condition

**¶49-72 | "Why" — How Breadth affects Repositioning | Target: Stern, GKSS, Bayesian Learning**

---

## The Learning Trap Condition

**¶49** The Funding Anchor (dA/dF < 0) operates through two mechanisms. Both explain why capital, intended to enable learning, instead suppresses repositioning.

**¶50** Traps are process failures, not outcome failures. A trap is a state where **learning halts**—new evidence no longer updates beliefs or actions.

**¶51** Traps occur at both extremes of breadth:
- **High-B₀ traps**: venture stays too vague, unable to zoom in
- **Low-B₀ traps**: venture stays too specific, unable to zoom out

**¶52** The learning condition formalizes this:

```
Trap ≡ [μ(1−μ) < ε × B] ∨ [B < B* ∧ HHI(belief) > 0.5]
```

Where:
- μ(1−μ) = belief variance (capacity to update)
- ε = learning threshold
- B = breadth (inversely related to precision τ)
- HHI(belief) = Herfindahl index of stakeholder belief concentration
- B* = critical breadth threshold

**Two distinct trap mechanisms**:

| Trap Type | Condition | Mechanism |
|:----------|:----------|:----------|
| **High-B Trap** | μ(1−μ) < ε×B | Threshold too high to cross |
| **Low-B Trap** | B < B* ∧ HHI > 0.5 | Echo chamber collapses variance |

For High-B: Large B raises the threshold ε×B, making it hard to satisfy.

For Low-B: Small B lowers the threshold, but **selection mechanism forces μ → 0 or 1**. Precise promises attract only believers; doubters are filtered out. Result: HHI(belief) → 1, and μ(1−μ) → 0 regardless of threshold.

---

## High-B₀ Trap (Flexibility Paradox)

**¶57** **Mechanism: 옵션 유지 → 학습 불능.** When ventures stay too vague, they preserve optionality but cannot learn. Hypotheses cannot be rejected—nothing specific enough to test.

**¶58** High B raises the threshold ε×B. Without specificity, founders cannot identify *what* to reject. Learning requires surprise; surprise requires prediction.

**¶59** High-B₀ founders attract believers who share their grand vision. Agreement is easy when definitions are loose.

**¶60** **Mobility exemplifies: B₀=78, 91% stayer ratio, 5% survival.**

**¶64** **Escape requires forcing specificity before funding.** Convert vague promises into testable hypotheses that can fail.

---

## Low-B₀ Trap (Commitment Paradox)

**¶65** **Mechanism: 몰입 고착 → pivot 불능.** Precise promises attract believers who expect exactly that outcome. Pivoting betrays the people who funded you.

**¶66** **Two stages**:
- **Stage 1 (Selection)**: Commitment attracts capital. Precise visions attract investors who believe that exact thesis. Doubt gets filtered out before the check clears.
- **Stage 2 (Lock-in)**: Capital reinforces commitment. Escalation of commitment (Staw, 1976).

**¶67** **Echo chamber** forms. Selection filters for believers. Lock-in silences doubters. Result: homogeneous stakeholders who share founder's thesis—agreement makes learning impossible.

**¶68** Low B raises threshold. But real problem: belief homogenization. When everyone agrees, variance μ(1−μ) → 0. No evidence can update unanimous prior.

**¶71** The trap is dangerous because **it looks like success**. Hitting milestones feels like progress. The venture wins its defined game while losing the real one.

**¶72** **Escape requires belief diversity before funding.** Add a doubter—investor or advisor who challenges the thesis. Disagreement preserves variance needed for learning.

---

## BT Output Interface

```yaml
BT_OUTPUT:
  equation: "μ(1−μ) < ε × B"
  traps:
    high_B0:
      mechanism: "Too vague → can't falsify"
      example: "Mobility (B₀=78, 5% survival)"
      escape: "Force specificity (zoom in)"
    low_B0:
      mechanism: "Too specific → echo chamber"
      example: "Motional ($4B, stayer)"
      escape: "Force diversity (zoom out)"
  connection_to_AF: "Lock-in/Lock-out reinforces both traps"
  target_scholars: ["Stern", "GKSS", "Bayesian Learning"]
```

---

*v5 Update: BL→BT, added connection to AF Lock-in (Dec 31 Day 3)*
