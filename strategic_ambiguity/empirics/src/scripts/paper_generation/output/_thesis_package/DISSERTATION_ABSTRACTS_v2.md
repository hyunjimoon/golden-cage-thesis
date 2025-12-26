# Dissertation Abstracts (Production-Ready v3)
## Aligned with LTE Framework (Cronin et al., 2025)

**Author**: Hyunji Moon
**Program**: MIT Sloan PhD, Operations Management & Entrepreneurship
**Advisors**: Charlie Fine (Operations), Scott Stern (Strategy)
**Date**: December 2025

---

## Overall Dissertation Abstract

**Title**: The Cognitive Cost of Capital: Resolving the Double Bind in Venture Strategy

Startups face a fundamental "Double Bind": they must make specific commitments to attract resources, yet require flexibility to survive in uncertain markets. While the prevailing resource-based view suggests that financial capital facilitates the costly experimentation needed for adaptation, this dissertation proposes a counter-theory: early capital accumulation creates a "Learning Trap" that induces cognitive rigidity. Employing a Levels of Theoretical Explanation (LTE) framework across three studies ($N=180,860$), I demonstrate that capital acts not as fuel for learning, but as a friction against it. Paper M reveals a multimodal survival landscape, establishing the "Movement Principle" where ventures that repositioned their strategy outperform static peers by 1.7× through superior adaptation. Paper C identifies the causal mechanism, showing that early capital ($E$) exerts a subtle but cumulative friction ($\rho \approx -0.01$) on adaptation ($A$), effectively substituting operational flexibility for cognitive lock-in. Paper T uses generative simulation to uncover the micro-foundations: specific promises attract "Analyst" investors who enforce belief homogeneity, thereby disabling the Bayesian updating required for pivots. In contrast, vague promises attract "Believers" who preserve the cognitive variance essential for survival. This research redefines strategic ambiguity not as a lack of direction, but as a sophisticated mechanism for preserving the option to learn.

---

## Paper M Abstract (Layer 1: The WHAT)

**Title**: Promise Precision and Venture Survival: Multimodality and the Movement Principle

**LTE Layer**: Descriptive Construct Theorizing

Does clearer strategic positioning always lead to better venture outcomes? Signaling theory posits that precision reduces information asymmetry and signals quality, implying a linear relationship between specificity and success. I challenge this assumption by analyzing a comprehensive dataset of 180,860 technology ventures (2021-2025). The results reject the linear model, revealing a multimodal distribution of success: ventures succeed either by being highly specific or by maintaining moderate vagueness. Crucially, I find that the success of the ambiguous group is driven by their adaptability. Movers—ventures that repositioned (|D| > 1)—succeeded at a rate of 18.0% compared to 10.4% for static peers (1.7× advantage). This study introduces the "Movement Principle," demonstrating that in high-uncertainty environments, the primary value of an initial position lies not in its optimality, but in the option value it preserves for future movement.

**Key Statistics**:
- N = 180,860 technology ventures (2021-2025)
- Spearman ρ(V,G) = +0.024*** (rejects monotonic decrease)
- Q1=12.3%, Q2=8.9%, Q3=16.0%, Q4=12.9% (non-monotonic)
- Movement advantage: 18.0% vs 10.4% = **1.7×**
- Movement rate by quartile: Q1=26%, Q2=8%, Q3=9%, Q4=11%

**Keywords**: Strategic Ambiguity, Non-Monotonic Pattern, Movement Principle, Adaptive Capacity, LTE Layer 1

---

## Paper C Abstract (Layer 2: The HOW)

**Title**: The Golden Cage: Why Capital Constrains Experimentation

**LTE Layer**: Causal Identification (Process Sequence)

A central tenet of entrepreneurial strategy is that experimentation facilitates learning, and because experimentation is costly, financial capital is required to fuel it (Nanda & Rhodes-Kropf, 2013). Thus, conventional wisdom suggests that early funding should enhance a venture's capacity to adapt. I argue the opposite. While capital provides the operational means to pivot (e.g., buying flexible assets), it simultaneously imposes cognitive constraints that inhibit strategic change. Using longitudinal data, I document a robust negative correlation between early funding ($E$) and subsequent adaptation ($A$). Mediation analysis reveals a statistically significant friction coefficient ($\rho \approx -0.01$), suggesting that capital acts as a "Golden Cage." This friction explains the paradox of why resource-rich ventures often fail to react to market signals—not because they cannot afford to change, but because the implicit contracts and expectations embedded in their capital structure render them cognitively incapable of acknowledging the need to do so.

**Key Statistics**:
- H1: ρ(A,E) = −0.009*** (Capital → Adaptation friction)
- H2: ρ(G,A) = +0.044*** (Adaptation → Growth)
- H3: ρ(G,E) = −0.211*** (Capital Paradox)
- Mediation: dG/dE = (dG/dA) × (dA/dE) = (+) × (−) < 0

**Keywords**: Capital-Flexibility Tradeoff, Golden Cage, Mediation Analysis, Commitment Costs

---

## Paper T Abstract (Layer 3: The WHY)

**Title**: Analysts vs. Believers: A Generative Model of the Learning Trap

**LTE Layer**: Explanatory Process Theorizing (Generative Sufficiency)

Why does capital create cognitive rigidity? I propose that the root cause lies in the endogenous selection of stakeholders. I develop an agent-based simulation to test the "Learning Trap" mechanism, distinguishing between two investor types: "Analysts," who seek to verify specific claims, and "Believers," who invest in broad visions. The model demonstrates that specific promises attract a homogeneous coalition of Analysts, leading to a collapse in belief variance. Without variance, the governance coalition loses its capacity for Bayesian updating, effectively filtering out novel market signals as noise. The simulation demonstrates generative sufficiency by accurately replicating the multimodal survival patterns and capital friction coefficients observed in empirical data. This finding suggests that the strategic value of vagueness lies in its ability to attract "Believer" capital, thereby preserving the cognitive diversity required to escape local optima.

**Key Mechanism**:
```
MECHANISM CHAIN (The Learning Trap):
┌─────────┐    ┌─────────────┐    ┌──────────┐    ┌──────────────┐    ┌─────────────┐
│ Capital │ → │ Homogeneous │ → │ Low Var  │ → │ Weak Update  │ → │ No Movement │
│   E ↑   │    │ Stakeholders│    │ Beliefs  │    │ from Signals │    │   A → 0     │
└─────────┘    └─────────────┘    └──────────┘    └──────────────┘    └─────────────┘

Investor Matching:
- P(Analyst | V) = 1 − V → High learning resistance, low variance tolerance
- P(Believer | V) = V → Low learning resistance, high variance tolerance
```

**Generative Sufficiency**: Simulation reproduces:
1. Non-monotonic V-G relationship
2. Bimodal growth distribution (Mover/Stayer)
3. ρ(A,E) ≈ −0.01 friction coefficient

**Keywords**: Generative Sufficiency, Agent-Based Simulation, Analyst/Believer Matching, Learning Trap, LTE Layer 3

---

## LTE Framework Summary

| Layer | Paper | Question | Method | Core Finding |
|:-----:|:------|:---------|:-------|:-------------|
| **1** | **M** | **WHAT** patterns exist? | Spearman ρ, Quartile decomposition | Movement Principle (1.7×); Non-monotonic V-G |
| **2** | **C** | **HOW** do processes unfold? | Correlational mediation | E → A (−) → G (+); Golden Cage friction |
| **3** | **T** | **WHY** do mechanisms generate? | Agent-based simulation | Analyst/Believer matching → Learning Trap |

---

## The Three Principles

1. **Movement Principle**: Vagueness buys options—USE THEM (1.7× advantage)
2. **Golden Cage Principle**: Capital creates cognitive lock-in, not operational flexibility
3. **Learning Trap Principle**: Specific promises attract Analysts who disable Bayesian updating

---

## Unified Narrative

> **The Cognitive Cost of Capital**
>
> The greatest wealth is not what you have accumulated but what you have preserved the freedom to become—and freedom requires the cognitive diversity to learn when to move.
>
> Strategic ambiguity is not a lack of direction; it is a sophisticated mechanism for preserving the option to learn.

---

*必死卽生, 必生卽死*
*"반드시 죽고자 하면 살고, 반드시 살고자 하면 죽는다."*

---

**Version**: 3.0 (Cognitive Cost of Capital)
**Last Updated**: 2025-12-12
**Status**: Production-Ready for Advisor Review
