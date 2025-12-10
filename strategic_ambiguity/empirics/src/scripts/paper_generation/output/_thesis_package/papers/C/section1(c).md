---
title: When Commitment Becomes a Cage
version: 6.0 (Data correction: 8.8× → 2.7×)
core_hypothesis: H_cost (Cost of Commitment = 2.7×)
core_mechanism: dY/dE = dY/d|ΔV| × d|ΔV|/dE = (+) × (-) < 0
modified:
  - 2025-12-09T12:00:00-05:00
---

# Chapter 1: Introduction

## Abstract

The prevailing wisdom—"more funding is better"—underlies nearly all entrepreneurial advice. Yet among **123,906 technology ventures** tracked from 2021-2025, we find a striking anomaly: companies with less early funding that stayed strategically flexible achieved **2.7× better funding growth** than well-funded companies that stayed the course.

We explain this through a mechanism chain:
$$\frac{dY}{dE} = \underbrace{\frac{dY}{d|\Delta V|}}_{(+)} \times \underbrace{\frac{d|\Delta V|}{dE}}_{(-)} < 0$$

Capital demands commitment. Commitment homogenizes teams. Homogeneity blocks learning. Using a counterfactual framework conditioning on early funding level, we estimate the **Cost of Commitment** at **2.7×** forgone funding growth (Escape Velocity Y=2.16× vs Golden Cage Y=0.80×). The strategic implication: **deprivation breeds flexibility, and flexibility breeds success**.

---

## Core Narrative (Gospel → Puzzle → Answer)

| | Gospel → Puzzle → Answer |
|:---|:---|
| **Gospel** | More 💰capital = more 🧪experiment = better 🧠learning |
| **Puzzle** | Startups with higher E changed strategy less (|ΔV|↓) and grew less (Y↓) |
| **Answer** | Capital requests commitment → commitment homogenizes team → homogeneity blocks learning |

---

## ¶1 The Resource Advantage Prescription

> **H₀ (Null):** More early funding → Better outcomes

The Resource-Based View (Barney 1991) and entrepreneurial finance literature prescribe a clear path: secure resources early. Early funding provides runway, signals quality, attracts talent, and enables competitive moves. Founders celebrate mega-rounds; VCs compete for deals; success stories are told through capital accumulation.

This gospel is so deeply embedded that questioning it seems heretical.

---

## ¶2 The Golden Cage Anomaly

Yet among 123,906 ventures in our panel, we observe a counterintuitive pattern:

| Profile | Early Funding (E) | Flexibility |ΔV| | Y = L/E |
|:--------|:-----------------:|:-----------:|:-------:|
| **Escape Velocity** | Low (≤ median) | High (> median) | **2.16×** |
| **Golden Cage** | High (> median) | Low (≤ median) | **0.80×** |
| **Ratio** | - | - | **2.7×** |

Companies with **less** early funding and **more** strategic flexibility achieved **2.7× better outcomes** than those with abundant resources who stayed locked in.

**Notation** (money as flow, not stock):
- **E** = Early funding (first_financing_size)
- **L** = Later funding (Total_2025 - E)
- **Y** = L/E (funding growth ratio)
- **|ΔV|** = |V_L - V_E| (strategic flexibility)

See [[fig3_cohort_analysis.png]] for the visual.

---

## ¶3 Research Question

> **RQ:** What is the cost of commitment—the forgone outcome from being locked into a strategy?

We ask: holding early funding constant, how much do locked-in companies underperform flexible ones?

---

## ¶4 Counterfactual Cost Framework

We introduce a **Counterfactual Cost of Commitment** estimator:

$$\text{Cost} = E[Y | \text{Locked}, E] - E[Y | \text{Flexible}, E]$$

By conditioning on **same early funding level** (E), we isolate the effect of lock-in. This is not "late bloomers succeed" (대기만성)—it's "**deprivation → flexibility → success**" (결핍 → 유연성 → 성공).

The mechanism is a **chain effect**:
```
E↑ → Promise → σ↓ → |ΔV|↓ → Y↓
```

---

## ¶5 Key Finding: 2.7× Cost of Commitment

Our main result (**H_cost**):

> **H_cost**: Escape Velocity (2.16×) vs Golden Cage (0.80×) = **2.7× gap**

This holds across all funding deciles (see [[fig2_cost_by_decile.png]]). Lock-in hurts at every funding level.

**Supporting evidence** (H_supporting): Lock-in correlation ρ = **-0.117*** between early funding and |ΔV|.

---

## ¶6 Contributions (Three Parents)

| Parent Literature | Gap | Our Contribution |
|:------------------|:----|:-----------------|
| **Entrepreneurial Finance** | Funding assumed unambiguously positive | Identify conditions where funding hurts |
| **Real Options Theory** | Option value assumed but not measured | Provide measure (|ΔV|) and cost estimate |
| **Organizational Learning** | Focus on what is learned, not capacity | Show how resources reduce learning capacity |

---

## ¶7 Paper Roadmap

| Section | Content |
|:--------|:--------|
| [[chap2_theory]] | Mechanism chain: dY/dE = (+)(−), H_cost derivation |
| [[chap3_empirics]] | Panel data, cohort design, 3-panel mechanism test |
| [[chap4_discussion]] | Implications, limitations, Bayesian hygiene |

---

*"What got you funded prevents your growth. 결핍 → 유연성 → 성공."*
