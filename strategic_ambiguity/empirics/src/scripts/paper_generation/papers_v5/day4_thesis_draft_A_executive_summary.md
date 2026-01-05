# The Commitment Trap: Strategic Repositioning Under Capital Lock-in

## Executive Summary for Advisor Review

**Author:** Hyunji Moon | **Advisors:** Scott Stern, Charles Fine | **January 2025**

---

## Abstract

This dissertation addresses a fundamental paradox: early funding success correlates with diminished strategic flexibility (dG/dF < 0), yet strategic movement predicts growth (dG/dA > 0). I explain this through the **Commitment Trap model**, showing that when investor concentration exceeds a threshold (HHI > θ), startups lose the optionality needed for evidence-based pivoting.

The framework integrates Ghemawat's (1991) commitment theory with Gans et al.'s (2021) "Test Two, Choose One" strategy, operationalized through Fine's 10 Tools. Validation comes from 488,381 startups (quantitative) and mobility venture cases including Motional and Ford/GM's $19B EV write-off (qualitative).

**Core Proposition:** Scott's "Test Two, Choose One" is implemented through Charlie's modular operations design, enabling escape from the commitment trap in capital-intensive ventures.

---

## 1. The Puzzle

### 1.1 Empirical Anomaly

| Relationship | Finding | Implication |
|:-------------|:--------|:------------|
| dG/dF < 0 | More early funding → lower growth | Capital constrains |
| dG/dA > 0 | More repositioning → higher growth (1.82×) | Movement enables |
| dA/dF < 0 | More funding → less repositioning | Capital blocks movement |

**Decomposition:** dG/dF = (dG/dA) × (dA/dF) = (+) × (−) = (−)

### 1.2 The Paradox Stated

Capital should expand options. Why does it constrain them?

---

## 2. Theoretical Framework: Ghemawat + Gans

### 2.1 Ghemawat (1991): When Flexibility Beats Commitment

Commitment creates value, but flexibility dominates when three conditions hold:

| Condition | Definition | Mobility Sector |
|:----------|:-----------|:----------------|
| **(1) High Irreversibility** | Sunk costs cannot be recovered | Factory investment, sensor architecture |
| **(2) High Ambiguity** | Outcomes uncertain | Regulatory timeline, consumer adoption |
| **(3) Learning Possible** | Information reveals over time | Technology validation, market feedback |

**All three conditions hold for AV startups** → Flexibility should dominate, yet ventures commit early.

### 2.2 Ghemawat's Four Lock-in Mechanisms

| Mechanism | Definition | Motional Application |
|:----------|:-----------|:--------------------|
| **Lock-in** | Sunk investments create expectations | $4B → stakeholder expectations |
| **Lock-out** | Closing off alternatives | L4 robotaxi → trucking path blocked |
| **Lags** | Long lead times | 2027-2030 plans already locked |
| **Inertia** | Organizational resistance | Hyundai/Aptiv resist pivot |

### 2.3 Gans et al. (2021): Two Patterns

| Dimension | Tesla (Success) | Better Place (Failure) | Motional (At Risk) |
|:----------|:----------------|:----------------------|:-------------------|
| **Promise** | Broad ("sustainable energy") | Narrow ("swappable battery") | Narrow ("L4 robotaxi") |
| **Strategy** | Extended exploration | Early exploitation | Early exploitation |
| **Commitment** | Partial, staged | Full, early | Full, early |
| **Result** | Global leader | Liquidated 2013 | Stuck in L4 |

**Insight:** Motional exhibits the Better Place pattern—narrow promise + early exploitation + full commitment.

---

## 3. The Golden Cage Mechanism

### 3.1 Three-Stage Process

```
Stage 1: Capital requires commitment
         └── Investors demand specific promises ("L4 robotaxi by 2027")
                    ↓
Stage 2: Commitment attracts believers
         └── Investors who share the vision join; skeptics exit
         └── Stakeholder homogeneity increases (HHI ↑)
                    ↓
Stage 3: Homogeneity blocks learning
         └── No champion for alternatives
         └── Disconfirming evidence dismissed
         └── TRAP
```

### 3.2 Formal Condition

**Trap Condition:** HHI > θ (investor concentration exceeds threshold)

When HHI > θ:
- Bayesian updating fails: μ(1−μ) < ε/(V+1)
- No stakeholder advocates for pivot
- Commitment escalates despite negative signals

**Empirical estimate:** θ ≈ 0.27 for mobility sector

---

## 4. Empirical Validation

### 4.1 Large-Sample Evidence (N = 488,381)

| Funding Quartile | Movement Rate | Growth Multiple |
|:-----------------|:--------------|:----------------|
| Q1 (Lowest) | 23% | 1.0× (baseline) |
| Q2 | 19% | 1.2× |
| Q3 | 14% | 1.1× |
| Q4 (Highest) | 9% | 0.8× |

**Pattern:** Highest-funded startups move least and grow least.

### 4.2 Ford/GM Natural Experiment

**Setup:** Full EV commitment under Ghemawat's three conditions
- High irreversibility: Factory retooling ($B)
- High ambiguity: Consumer adoption, charging infrastructure
- Learning possible: Hybrid alternatives existed

**Shock:** Biden → Trump policy shift (2024-2025)

**Result:** Ford $19B+ write-off; GM similar losses

**Interpretation:** Premature full commitment under uncertainty destroys value. The commitment trap operates at scale.

### 4.3 Motional Case

| Dimension | Status | Risk Level |
|:----------|:-------|:-----------|
| Promise narrowness | "L4 robotaxi" only | High |
| Commitment level | $4B invested | High |
| Stakeholder HHI | Hyundai + Aptiv dominant | High |
| Learning activity | "Stuck without testing strategies" | Critical |

**Diagnosis confirmed by Motional:** Company acknowledged being "stuck in L4 without testing strategies."

---

## 5. Prescription: Partial Commitment Framework

### 5.1 Why Partial Commitment? Two Paradoxes, One Solution

Entrepreneurs face two interrelated paradoxes. Partial commitment resolves both.

| Aspect | Paradox of Entrepreneurship (Gans et al.) | Explorer's Paradox |
|:-------|:------------------------------------------|:-------------------|
| **Core Tension** | Ranking alternatives requires experimentation, but experimentation creates commitments that eliminate alternatives | Better information requires more commitment, but commitment reduces ability to act on that information |
| **Key Trade-off** | Optimization vs. Choice | Information gathering vs. Strategic flexibility |
| **Resource Focus** | Limited ability to pursue multiple alternatives simultaneously | Limited resources (time/money) deplete as you move closer to either path |
| **Learning Mechanism** | Learning through experimentation requires partial commitment | Signal precision increases with proximity/commitment |
| **Decision Challenge** | When to stop optimizing and make a choice? | How far to move down a path before committing or switching? |
| **Resolution** | "Test Two, Choose One" | Partial commitments and staged learning |
| **Time Dimension** | Sequential (optimization then choice) | Present vs. Future (current learning vs. future flexibility) |
| **Main Insight** | You can't fully evaluate options without some commitment | Getting better information inherently reduces optionality |

**Synthesis:** Both paradoxes share a common resolution—**partial commitment**. Sufficient commitment generates learning signals; insufficient commitment preserves the ability to act on what is learned.

### 5.2 Scott's "Test Two, Choose One" → Charlie's Operations

| Scott (Strategy) | Charlie (Operations) |
|:-----------------|:--------------------|
| Keep two paths open | Build shared platform (80%) + differentiated apps (20%) |
| Gather signals | Measure same KPIs across both paths |
| Choose based on evidence | Decision gate with operational criteria |
| Commit to winner | Redeploy shared infrastructure |

**Key Insight:** The operational translation of "Test Two" is modular architecture—shared infrastructure that supports multiple paths without full commitment to either.

### 5.3 The Q2 → Q3 → Q1 Sequence

| Phase | Question | Commitment | Tools (Fine) |
|:------|:---------|:-----------|:-------------|
| **Q2** | How to build? | 20% (explore) | Evaluate, Automate, Collaborate |
| **Q3** | Where to play? | 50% (focus) | Segment, Replicate |
| **Q1** | How to scale? | 80% (commit) | Platformize, Capitalize |

**Common Error:** Starting with Q1 (Capitalize) before Q2 (Evaluate)

**Prescription:** Validate before you capitalize

### 5.4 Application to Motional

**Current state:** Q1 position (high capital, narrow promise)

**Recommended sequence:**
1. **Return to Q2:** Test L2/L3 ADAS alongside L4
2. **Execute Q3:** Choose market (robotaxi vs trucking vs ADAS licensing)
3. **Re-enter Q1:** Scale chosen path with remaining capital

---

## 6. Contribution Summary

| Layer | Question | Contribution |
|:------|:---------|:-------------|
| **L1 (What)** | What relationships exist? | dG/dA > 0, dA/dF < 0, dG/dF < 0 |
| **L2 (How)** | How do they unfold? | Golden Cage: 3-stage mechanism |
| **L3 (Why)** | Why do agents behave this way? | HHI > θ blocks Bayesian updating |
| **Rx** | What should be done? | Q2→Q3→Q1 via partial commitment |

### Theoretical Integration

| Scholar | Framework | This Thesis Extends |
|:--------|:----------|:-------------------|
| **Ghemawat (1991)** | Lock-in mechanisms | + Lock-out via stakeholder governance |
| **Gans et al. (2021)** | Test Two, Choose One | + Operational implementation |
| **Van den Steen (2017)** | Commitment's object | + Commitment's scope condition |
| **Fine (2022)** | 10 Tools | + Sequencing for flexibility |

---

## 7. Limitations and Future Work

| Limitation | Implication | Future Direction |
|:-----------|:------------|:-----------------|
| Selection bias | Successful movers exit early | Survival analysis |
| Generalizability | Mobility-specific | Replication in biotech, hardware |
| Measurement | HHI threshold estimated | Direct governance measurement |

---

## References (Selected)

- Fine, C. H. (2022). *Operations for Entrepreneurs*. MIT Sloan.
- Gans, J., Scott, E., & Stern, S. (2021). *Entrepreneurial Strategy*. MIT Press.
- Ghemawat, P. (1991). *Commitment: The Dynamic of Strategy*. Free Press.
- Van den Steen, E. (2017). A Formal Theory of Strategy. *Management Science*, 63(8).

---

*Executive Summary: 8 pages | Full thesis available upon request*
