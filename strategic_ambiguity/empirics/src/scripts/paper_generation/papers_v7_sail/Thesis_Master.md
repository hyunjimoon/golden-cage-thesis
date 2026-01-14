---
title: "The Golden Cage: How Early Funding Suppresses Venture Growth"
author: Angie Hyunji Moon
affiliation: MIT Department of Civil and Environmental Engineering, Transportation
date: 2026-01-12
version: 7.1 (Final - Multiplicative Mediation Model)
model_type: MULTIPLICATIVE
core_equation: dG/dE = (dG/dR) × (dR/dE) = (+) × (−) = (−)
structure: 6-Chapter Academic Thesis
ROT_target: 85%
canonical_numbers:
  funding_growth_correlation: ρ = −0.196***
  sample_size: N = 180,994
  mover_advantage: 2.60× (18.1% vs 7.0%)
  mover_definition: R > 0 (any strategic movement)
  funding_repositioning: ρ = −0.087***
industry_correlations_verified:
  hardware: ρ = −0.108***
  transportation: ρ = −0.101***
  pharma: ρ = −0.079***
  medtech: ρ = −0.053***
  software: ρ = −0.001 (ns)
  quantum: ρ = +0.095*
modified:
  - 2026-01-11T19:05:45-05:00
  - 2026-01-12T09:06:59-05:00
  - 2026-01-12T11:24:57-05:00
  - 2026-01-13T23:52:07-05:00
  - 2026-01-14T07:00:43-05:00
---


# THE GOLDEN CAGE
## How Early Funding Suppresses Venture Growth

**Angie Hyunji Moon**
*MIT Department of Civil and Environmental Engineering, Transportation*

Draft for Committee Review — January 2026

---

# Abstract

**¶1 — Phenomenon & Significance.**
The U.S. venture capital industry—which deployed over $330 billion globally at its 2021 peak (PitchBook, 2024)—rests on a simple premise: capital fuels growth. Yet analyzing 180,994 ventures from PitchBook (2021–2025), I document the Funding-Growth Paradox: early-stage funding correlates *negatively* with later-stage survival (ρ = −0.196, p < 0.001). Startups die not for lack of resources, but for lack of mobility. Capital is oxygen—but oxygen in a sealed chamber becomes a cage.

**¶2 — Part I: The Cage (Chapters 1–4).**
The effect operates through a mediated pathway. Let E denote early-stage funding, R denote strategic repositioning, and G denote later-stage growth. Funding suppresses repositioning (ρ(E,R) = −0.087), yet repositioning drives growth—ventures that reposition ("Movers") outperform those that hold position ("Stayers") by 2.60× (18.1% vs. 7.0%). The product of a positive and a negative is negative: the effect of funding on growth, dG/dE, decomposes into dG/dR (positive: repositioning helps) times dR/dE (negative: funding suppresses repositioning), yielding a net negative. I term this the *golden cage*: operational commitments attract like-minded investors who filter skeptics from governance, eliminating the signal diversity that learning requires. The constraint is structural—founders *cannot* pivot because their boards lack advocates for alternatives.

**¶3 — Part II: Escaping the Cage (Chapters 5–6).**
The contribution is threefold. First, I document a negative funding-growth correlation at unprecedented scale. Second, I identify governance homogeneity—not moral hazard—as the binding constraint. Third, I distinguish vision-level commitment (which preserves flexibility) from operational commitment (which forecloses it). Industry heterogeneity reveals boundary conditions: the cage binds tightest in capital-intensive sectors (Hardware: ρ = −0.108, Transportation: ρ = −0.101) but releases under extreme uncertainty (Quantum: ρ = +0.095). The prescription follows: when uncertain, commit to *reposition*, rather than to position.

**Keywords:** entrepreneurial strategy, venture capital, strategic flexibility, pivoting, governance, commitment

---

# Acknowledgments

[To be completed]

---

# Table of Contents

- [Chapter 1: Introduction](#chapter-1-introduction)
  - [1.1 General Motivation](#11-general-motivation)
  - [1.2 The Funding-Growth Paradox](#12-the-funding-growth-paradox)
  - [1.3 Research Questions and Chapter Overview](#13-research-questions-and-chapter-overview)
  - [1.4 Contribution Preview](#14-contribution-preview)

## PART I: The Cage — Theory and Evidence

- [Chapter 2: The Golden Cage Mechanism](#chapter-2-the-golden-cage-mechanism)
  - [2.1 Introduction](#21-introduction)
    - [2.1.1 Contributions](#211-contributions)
    - [2.1.2 Analytic Structure: Patterns vs. Mechanisms](#212-analytic-structure-patterns-vs-mechanisms)
    - [2.1.3 Related Work](#213-related-work)
  - [2.2 Commitment as Double-Edged Sword](#22-commitment-as-double-edged-sword)
  - [2.3 Force (+): Why Flexibility Creates Value](#23-force--why-flexibility-creates-value)
  - [2.4 Force (−): Why Funding Destroys Flexibility](#24-force--why-funding-destroys-flexibility)
  - [2.5 The Collision: (+) × (−) = (−)](#25-the-collision------)
    - [2.5.1 Formal Condition for Caged Learning](#251-formal-condition-for-caged-learning)
  - [2.6 Real Options Foundation](#26-real-options-foundation)
  - [2.7 Hypotheses](#27-hypotheses)
  - [2.8 Conclusion](#28-conclusion)

- [Chapter 3: Data and Identification](#chapter-3-data-and-identification)
  - [3.1 Introduction](#31-introduction)
  - [3.2 Data Sources and Sample Construction](#32-data-sources-and-sample-construction)
    - [3.2.1 Primary Data: PitchBook](#321-primary-data-pitchbook)
    - [3.2.2 Supplementary Data](#322-supplementary-data)
  - [3.3 Variable Operationalization](#33-variable-operationalization)
    - [3.3.1 Strategic Breadth (B)](#331-strategic-breadth-b)
    - [3.3.2 Repositioning (R)](#332-repositioning-r)
    - [3.3.3 Defining Repositioning](#333-defining-repositioning)
    - [3.3.4 Growth (G)](#334-growth-g)
  - [3.4 Descriptive Statistics](#34-descriptive-statistics)
  - [3.5 Identification Strategy](#35-identification-strategy)
    - [3.5.1 The Selection Challenge](#351-the-selection-challenge)
    - [3.5.2 Addressing Selection: A Multi-Layer Defense](#352-addressing-selection-a-multi-layer-defense)
  - [3.6 Conclusion](#36-conclusion)

- [Chapter 4: Where the Cage Bites](#chapter-4-where-the-cage-bites)
  - [4.1 Introduction](#41-introduction)
    - [4.1.1 Contributions](#411-contributions)
    - [4.1.2 Related Work](#412-related-work)
  - [4.2 CER Analysis: Commitment → Funding → Repositioning](#42-cer-analysis-commitment--funding--repositioning)
    - [4.2.1 Main Finding](#421-main-finding)
    - [4.2.2 Interpretation](#422-interpretation)
  - [4.3 FRG Analysis: Flexibility → Repositioning → Growth](#43-frg-analysis-flexibility--repositioning--growth)
    - [4.3.1 Main Finding](#431-main-finding)
    - [4.3.2 The Mover Advantage: 2.60×](#432-the-mover-advantage-260)
    - [4.3.3 Effect Size Contextualization](#433-effect-size-contextualization)
  - [4.4 Industry Heterogeneity](#44-industry-heterogeneity-where-the-cage-bites-hardest)
    - [4.4.1 Cross-Industry Comparison](#441-cross-industry-comparison)
    - [4.4.2 The Era of Ferment Exception](#442-the-era-of-ferment-exception)
    - [4.4.3 Deep Tech Strategy: Non-Dilutive Alternatives](#443-deep-tech-strategy-non-dilutive-alternatives)
    - [4.4.4 Commitment Types: Staged vs. Partial](#444-commitment-types-staged-vs-partial)
    - [4.4.5 The Triple Vulnerability](#445-the-triple-vulnerability)
  - [4.5 Robustness Checks](#45-robustness-checks)
    - [4.5.1 Temporal Stability](#451-temporal-stability)
    - [4.5.2 Survival Bias Conditioning (TR-02)](#452-survival-bias-conditioning-tr-02)
    - [4.5.3 Alternative Operationalizations](#453-alternative-operationalizations)
  - [4.6 Illustrative Cases](#46-illustrative-cases)
    - [4.6.1 Two Types of Movers: Zoom-out and Zoom-in](#461-two-types-of-movers-zoom-out-and-zoom-in)
    - [4.6.2 The Stayer Contrast](#462-the-stayer-contrast)
  - [4.7 Conclusion](#47-conclusion)

## PART II: Escaping the Golden Cage

- [Chapter 5: Designing for Strategic Flexibility](#chapter-5-designing-for-strategic-flexibility)
  - [5.1 Introduction](#51-introduction)
  - [5.2 Capitalize: Strategic Ambiguity as Resource](#52-capitalize-strategic-ambiguity-as-resource)
    - [5.2.1 The Tesla-Better Place Contrast](#521-the-tesla-better-place-contrast)
    - [5.2.2 Practical Guidance](#522-practical-guidance)
  - [5.3 Evaluate: Segment × Collaborate Framework](#53-evaluate-segment--collaborate-framework)
    - [5.3.1 The Diagonal Principle](#531-the-diagonal-principle)
    - [5.3.2 Parallel Growth](#532-parallel-growth)
  - [5.4 Governance Design Principles](#54-governance-design-principles)
    - [5.4.1 Operationalizing "Preserve Skeptics"](#541-operationalizing-preserve-skeptics)
  - [5.5 Boundary Conditions](#55-boundary-conditions)
  - [5.6 Conclusion](#56-conclusion)

- [Chapter 6: Conclusion](#chapter-6-conclusion)
  - [6.1 Theoretical Contributions](#61-theoretical-contributions)
  - [6.2 Practical Implications](#62-practical-implications)
  - [6.3 Limitations](#63-limitations)
    - [6.3.1 Alternative Explanations](#631-alternative-explanations)
  - [6.4 Future Research](#64-future-research)
  - [6.5 Closing](#65-closing)

- [References](#references)
- [Appendices](#appendices)
  - [Appendix A: Additional Robustness Tests](#appendix-a-additional-robustness-tests)
  - [Appendix B: Variable Construction Details](#appendix-b-variable-construction-details)
  - [Appendix C: Glossary](#appendix-c-glossary)
  - [Appendix D: Proof of Theorem 1](#appendix-d-proof-of-theorem-1-caged-learning)

---

# List of Figures

| Figure | Title                                         | Chapter |
| :----: | :-------------------------------------------- | :-----: |
|   1    | The Funding-Growth Paradox                    |  Ch.1   |
|   2    | The Mediation Structure (DAG)                 |  Ch.1   |
|   3    | The Golden Cage Mechanism                     |  Ch.2   |
|   4    | Sample Construction Flowchart                 |  Ch.3   |
|   5    | CER Pattern: Funding Suppresses Repositioning |  Ch.4   |
|   6    | Mover vs. Stayer Success Rates (2.60×)        |  Ch.4   |
|   7    | Industry Heterogeneity ρ(E,G)                 |  Ch.4   |
|   8    | Mobility: Where the Cage Bites Hardest        |  Ch.4   |
|   9    | Temporal Robustness (2020-2025)               |  Ch.4   |
|  10    | The Strategic Ambiguity Sweet Spot            |  Ch.5   |

# List of Tables

| Table | Title | Chapter |
|:-----:|:------|:-------:|
| 1 | Variable Definitions and Causal Structure | Ch.3 |
| 2 | Descriptive Statistics (N = 180,994) | Ch.3 |
| 3 | CER Analysis: Funding → Repositioning | Ch.4 |
| 4 | FRG Analysis: Repositioning → Growth | Ch.4 |
| 5 | Mover Taxonomy: Stayer / Zoom-in / Zoom-out | Ch.4 |
| 6 | Industry Breakdown: Survival Rates by Sector | Ch.4 |
| 7 | Robustness Tests: Alternative Specifications | Ch.4 |
| 8 | Governance Design Recommendations | Ch.5 |
| 9 | Governance Levers for Signal Diversity | Ch.5 |
| 10 | Alternative Explanations vs. Governance Homogeneity | Ch.6 |

---

# CHAPTER 1: INTRODUCTION

> *"What's the puzzle?"*
> **Core Equation**: dG/dE = (dG/dR) × (dR/dE) = (+) × (−) = (−)
>
> *Key terms are defined in [Appendix C: Glossary](#appendix-c-glossary). [Canonical numbers](#canonical-numbers) are locked.*

## 1.1 General Motivation

Venture capital governance—through commitment structures and investor selection—**cages** founders' strategic flexibility. Startups die not for lack of resources, but for lack of mobility. Over the past decade, the U.S. venture capital industry—which deployed over $330 billion globally at its 2021 peak (PitchBook, 2024)—has transformed how entrepreneurs build companies in software, mobility, and deep tech. Yet a fundamental tension persists: securing funding requires specific commitments, while uncertain markets reward adaptation. Founders navigate this tension through strategic ambiguity—positioning that attracts diverse stakeholders while preserving the option to pivot.

For instance, Tesla's early positioning as "accelerating sustainable transport" attracted believers in electrification, autonomy, and energy transition, enabling the company to pivot across segments (Roadster → Model S → Model 3) without losing governance support. In contrast, Better Place raised $850 million for "battery swapping infrastructure"—a commitment so specific that when market feedback favored charging over swapping, no board member advocated for the alternative. The company liquidated in 2013, its assets sold for less than $1 million (Bradshaw, 2013)—a stark illustration of value destruction through operational lock-in.

Motivated by such divergent outcomes among well-funded ventures, this thesis focuses on the following two aspects of funding and flexibility decisions.

**Understanding the interactions between funding and strategic flexibility.** Capital creates a double bind. It enables experimentation by providing resources for market testing. Yet securing capital requires commitments that attract like-minded investors—filtering skeptics from governance and eliminating the signal diversity that learning requires. Should founders pursue substantial early funding to enable experimentation, or does governance rigidity outweigh resource benefits? Prior studies examine funding effects and pivoting outcomes in isolation rather than as components of a governance system (Camuffo et al., 2020; Kirtley & O'Mahony, 2023). This thesis addresses the gap.

In addition to funding interactions, commitment decisions have vertical implications for venture survival. A founder who commits at the operational level (specific technology, specific market) attracts investors who believe in that specific path. When market signals suggest pivoting, no governance voice advocates for alternatives. These tensions raise important questions about how founders can balance commitment credibility with adaptation capacity. Together, these examples point to the need for a deeper understanding of both the horizontal interactions between funding and flexibility, and the vertical implications that governance composition has for strategic adaptation.

**Designing commitment structures that preserve flexibility.** Large-scale venture data now enable targeted optimization of commitment decisions. Text analysis of company descriptions reveals which ventures maintain strategic breadth over time. Industry-level analysis reveals where the commitment-flexibility trade-off binds tightest (capital-intensive sectors like mobility) and where it releases (pre-paradigmatic sectors like quantum computing). These analyses enable founders and investors to capture commitment's credibility benefits without foreclosing adaptation.

The overall goal of this thesis is to address the challenges outlined above. Below, I provide a roadmap of how the thesis approaches these challenges, summarize the main results, and outline the organization of the chapters.

## 1.2 The Funding-Growth Paradox

The data reveal a counterintuitive pattern. Analyzing 180,994 ventures from PitchBook (2021–2025), I find a negative correlation between early-stage funding and later-stage survival:

$$\rho(\text{Funding}, \text{Growth}) = -0.196 \quad (p < 0.001)$$

[Figure 1: The Funding-Growth Paradox](figures/Ch1_Fig1_capital_paradox.png)

**Figure 1:** The Funding-Growth Paradox. Higher early funding correlates with lower later-stage success (N = 180,994, ρ = −0.196, p < 0.001). The relationship holds across industries and cohort years.

This pattern resolves through decomposition. I identify two countervailing effects, formalizing their interaction as the product of component correlations:

$$\frac{dG}{dE} = \underbrace{\frac{dG}{dR}}_{\text{Flexibility Premium }(+)} \times \underbrace{\frac{dR}{dE}}_{\text{Commitment Trap }(-)} = (-)$$

The **Flexibility Premium** (dG/dR > 0) captures the growth benefit of adaptation: ventures that reposition ("Movers") outperform those that hold position ("Stayers") by 2.60× (18.1% vs. 7.0% later-stage survival). The **Commitment Trap** (dR/dE < 0) captures the rigidity cost of funding: early funding correlates with lower repositioning (ρ = −0.087, p < 0.001), as governance structures attached to capital constrain adaptation. The product of a positive and a negative is negative: funding correlates with reduced mobility, not because capital is harmful, but because commitment attracts like-minded investors who filter skeptics from governance.

[Figure 2: Mediation Structure](figures/Ch1_Fig2_mediation_dag.png)

**Figure 2:** The Mediation Structure. The upper path shows measured variables: Early Funding → Repositioning → Growth. H1 (Commitment Trap, −) captures funding's suppression of repositioning; H2 (Flexibility Premium, +) captures repositioning's benefit to growth. H3 (Funding Paradox, −) is the net effect shown by the dashed arc. The lower path shows latent variables: Commitment enables funding (+) but destroys Flexibility (−); Flexibility enables both Repositioning (+) and Growth (+).

## 1.3 Research Questions and Chapter Overview

This thesis addresses three interconnected questions, each corresponding to a thesis part:

**Part I: The Cage — Theory and Evidence (Chapters 2-4)**

1. **The Mechanism Question (Chapter 2):** *Why* does funding suppress repositioning? I synthesize Van den Steen's (2010) sorting equilibrium, Eisenberg's (1984) strategic ambiguity, and Ghemawat's (1991) commitment analysis into a unified mechanism—the *golden cage*. The main technical contribution is **Theorem 1 (Caged Learning)**, which formalizes conditions under which organizational learning ceases endogenously through the funding process.

2. **The Evidence Question (Chapters 3-4):** *How* do we test this mechanism at scale? Using 180,994 ventures, I operationalize repositioning through dictionary-based text analysis and document both the CER pattern (Funding → Repositioning↓) and the FRG pattern (Repositioning → Growth↑). Industry heterogeneity reveals boundary conditions: the cage binds tightest in capital-intensive sectors (Hardware: ρ = −0.108, Transportation: ρ = −0.101) but releases under extreme uncertainty (Quantum: ρ = +0.095).

**Part II: Escaping the Cage (Chapters 5-6)**

3. **The Design Question (Chapter 5):** *What* can founders and investors do about it? I develop a prescriptive framework distinguishing vision-level commitment (which preserves flexibility) from operational commitment (which forecloses it). The **Strategic Ambiguity Sweet Spot** (Figure 10) shows that moderate positioning breadth achieves 16.0% survival—higher than both narrow and maximally broad positioning.

## 1.4 Contribution Preview

This thesis makes three contributions to the literature on entrepreneurial strategy and venture governance.

**First, I document the funding-growth paradox at unprecedented scale.** With N = 180,994 ventures, this study provides population-level evidence of a negative correlation between early-stage funding and later-stage survival. Prior work has examined funding effects in smaller samples (Camuffo et al., 2020; N = 116) or specific contexts (Ewens, Nanda, & Rhodes-Kropf, 2018). I demonstrate that the paradox generalizes across industries and cohort years, establishing an empirical regularity that demands theoretical explanation.

**Second, I identify governance homogeneity—not moral hazard—as the binding constraint on venture adaptation.** This distinction carries implications for intervention design. If founders *will not* pivot due to reduced incentives (moral hazard), the prescription is intensified monitoring. If founders *cannot* pivot due to structural constraints (the golden cage), the prescription is governance redesign. My evidence favors the structural explanation: founders of failed well-funded ventures frequently express regret at not pivoting earlier, suggesting motivation was present but governance support was absent.

**Third, I introduce a theoretical distinction between vision-level and operational commitment.** Vision commitment ("accelerating sustainable transport") preserves flexibility by accommodating multiple implementation paths. Operational commitment ("battery swapping infrastructure") forecloses alternatives by binding resources to specific mechanisms. This distinction explains heterogeneity among well-funded ventures: Tesla's vision commitment enabled pivots across segments and business models, while Better Place's operational commitment prevented adaptation when market feedback favored charging over swapping. The practical implication is that founders can capture commitment's credibility benefits while preserving flexibility—but only by committing at the right level of abstraction.

---

# CHAPTER 2: THE GOLDEN CAGE MECHANISM

> *"Why does it happen?"*
> **Key Insight**: Founders *cannot* pivot—not that they *will not*—because governance lacks advocates for alternatives.

## 2.1 Introduction

**This chapter develops the golden cage mechanism:** by synthesizing Van den Steen's (2010) sorting equilibrium, Eisenberg's (1984) strategic ambiguity, and Ghemawat's (1991) commitment analysis, we study why funding suppresses repositioning through governance homogeneity rather than moral hazard.

Strategic flexibility **determines** venture survival. In manufacturing, flexibility **hedges** against demand shocks (Jordan & Graves, 1995). In ventures, it **enables** pivots when markets shift (Ries, 2011; Camuffo et al., 2020). Yet the funding process systematically **destroys** this flexibility—a tension this chapter **resolves**.

(a) Flexibility in Manufacturing (b) Flexibility in Ventures

**Figure 3a: Process Flexibility vs. Venture Flexibility.** The plots contrast process flexibility in manufacturing systems (long chain design) with flexibility in venture governance. In manufacturing, flexibility is configured deterministically by central planners. In ventures, flexibility emerges through governance composition—who sits on the board determines which strategic pivots are feasible.

Modern venture-backed startups face uncertainty on both product and market sides. The strategic positioning problem has a two-sided structure: investors on the funding side, customers on the market side. Figure 3a illustrates stakeholder connections. Each edge **signals** compatibility—whether an investor backs a given direction. Founders **navigate** these edges when raising capital. Manufacturing and ventures both need flexibility, but **create** it differently.

In manufacturing, a central planner **configures** compatibility deterministically by investing in equipment. In venture governance, flexibility **emerges** through selection dynamics. Eisenberg's (1984) "strategic ambiguity" approach illustrates how founders **maintain** flexibility—by positioning broadly enough to attract diverse stakeholders. A founder choosing this approach accepts varied investor interpretations, but **gains** the ability to pivot without losing governance support. The number of investors supporting any particular pivot is stochastic: strategic ambiguity **expands** pivot options, but not deterministically.

| Industry | Example Platforms | Flexibility Mechanism | Constraint Mechanism |
|:---------|:------------------|:----------------------|:---------------------|
| Mobility | Tesla, Better Place | Vision vs. operational commitment | Board composition |
| Software | Slack, Flickr | Product pivot capacity | Investor thesis alignment |
| Hardware | Nest, Dropcam | Technology redeployment | Sunk cost in manufacturing |

**Table 2.1: Examples of ventures that face flexibility constraints through governance.** These constraints arise when operational commitments attract like-minded investors who filter skeptics from governance.

The examples illustrate that flexibility constraints can simultaneously arise from multiple sources, which raises the question of how governance composition interacts with commitment type. Specifically, what commitment structure is best for survival? Is it more effective to commit at the vision level (preserving pivot options), or is it better to commit at the operational level (attracting aligned investors)? Despite the significant capital through which founders make commitments on both technology and market sides, the interaction of commitment type and governance composition is not well-understood. Indeed, we know of no work in the literature that examines the interaction of these two flexibility mechanisms in venture governance. And, in practice, founders usually make commitment decisions without visibility into how those commitments shape board composition—a one-sided approach that neither reveals nor exploits the interaction of different flexibility levers, and we will show that it can come at a great cost.

Motivated by this gap in the literature, this chapter studies how the funding process creates a *golden cage*—a structural constraint that prevents adaptation regardless of founder intent. Our focus on the governance mechanism differs from traditional studies that usually attribute venture failure to moral hazard or resource constraints, rather than their interactions. Since Table 2.1 shows that governance-based flexibility constraints can arise in a variety of settings, we focus on highlighting general effects that are likely relevant to any venture. We develop a parsimonious theoretical model to identify how commitment type shapes governance composition. Our model represents the venture as a founder-investor matching problem, where specific commitments (operational) attract narrow coalitions while vague commitments (vision-level) attract diverse coalitions. The venture's objective is to maximize survival probability, which depends on both resource acquisition and pivot capacity. We study how a given commitment level should be structured, and whether and when founders should commit at the vision versus operational level.

Our results show that the choice of commitment level has a significant impact on venture survival. Even with fixed commitment credibility, the pivot capacity (and consequently the survival probability) can vary significantly depending on how commitment is structured (see Figure 3). Moreover, by comparing two natural commitment strategies: (1) the operational commitment, which specifies technology and market, and (2) the vision commitment, which specifies direction but not destination, we find that either strategy can improve survival by more than 2× compared to the other, depending on industry and stage. Hence, founders who optimize their commitment level but not its structure may pay a high price.

Despite the impact of commitment structure, optimizing it poses nontrivial difficulties. Even in a simple and symmetric governance model, the geometry of pivot capacity (as a function of commitment structure) reveals traps in which a venture might get stuck. In particular, the current practice of many founders—wherein commitments are made to secure near-term funding without considering long-term governance implications—might converge to such traps. Near these traps, founders mistakenly perceive themselves to be optimally positioned, as commitment should neither be increased nor decreased; however, the venture would benefit from restructuring commitment from operational to vision level or vice versa. These structural insights are unique to our study of commitment-governance interaction, and our empirical results show that they generalize beyond our particular model.

### 2.1.1 Contributions

This chapter **first examines** how commitment shapes governance in venture strategy. It **characterizes** the mechanisms through which funding **constrains** flexibility and **enables** study of optimal commitment structure.

**Optimal commitment structures.** Our study of vision-level and operational commitment reveals that either structure can dominate the other. In Sections 2.3 and 2.4, we introduce two key effects—*belief homogenization* and *signal diversity loss*—that respectively drive the consequences of operational and vision-level commitments. Intuitively, belief homogenization is a consequence of operational commitment: as specific commitments attract like-minded investors, governance diversity decreases while shared conviction increases—but this conviction becomes wasteful when the committed direction proves wrong. In contrast, signal diversity loss arises under extreme operational commitment, where board members who might champion alternative interpretations never join governance. The loss can result in a large number of disconfirming signals being ignored, leaving the venture unable to recognize when pivoting would be optimal. In Sections 2.3 and 2.4, we characterize the conditions where these effects are most pronounced, and in Section 2.5 we identify the dominant commitment structure across different industry contexts.

**Synthesis of sorting and ambiguity theories.** Our main theoretical contribution lies in synthesizing Van den Steen's (2010) sorting equilibrium with Eisenberg's (1984) strategic ambiguity into a unified mechanism. Characterizing how commitment shapes governance is a long-studied but notoriously challenging area in entrepreneurship. To compare the survival rates of different commitment structures, we develop three distinct analytical approaches. In Section 2.3 we design a careful mapping between commitment type and governance composition and show, for certain parameters, that belief homogenization leads to lower survival for operational commitment. Then, in Section 2.4 we apply the flexibility premium analysis for conditions where strategic ambiguity produces high governance diversity. Finally, in Section 2.5 we formalize the Caged Learning condition (Theorem 1) to explicitly characterize when organizational learning ceases endogenously.

**Structural vs. motivational constraint.** We distinguish "cannot pivot" (structural) from "will not pivot" (moral hazard), with distinct implications for intervention design. If founders *will not* pivot due to reduced incentives, the prescription is intensified monitoring. If founders *cannot* pivot due to structural constraints (the cage), the prescription is governance redesign—preserving skeptical voices before funding eliminates them.

### 2.1.2 Analytic Structure: Patterns vs. Mechanisms

This thesis distinguishes between **observed correlational patterns** (measurable) and **theoretical mechanisms** (latent). The distinction is critical for interpreting the evidence and follows the Layers of Theoretical Explanation (LTE) framework developed by Kozlowski et al. (2025), which identifies three levels of theoretical depth:

| Layer | Question | Focus | This Thesis |
|:-----:|:---------|:------|:------------|
| **Layer 1: Construct** | *What* relationships exist? | Observable covariation | ρ(E,G) = −0.196, ρ(E,R) = −0.087, Mover Advantage = 2.60× |
| **Layer 2: Process** | *How* do actions unfold? | Action sequences in context | Commit → Fund → Filter → Homogenize → Cage |
| **Layer 3: Mechanism** | *Why* do actors behave this way? | Generative drivers | μ(1−μ) < ε/B (Theorem 1: Caged Learning) |

The LTE framework clarifies that construct-level findings (Layer 1) predict but do not explain. Layer 2 describes the *sequence* through which the golden cage forms: operational commitment attracts like-minded investors, who filter skeptics from governance, producing belief homogeneity that eliminates learning capacity. Layer 3 specifies the *generative mechanism* that drives this sequence: Van den Steen's (2010) sorting equilibrium produces high μ (shared optimism), while operational commitment produces low B (narrow strategic breadth), satisfying the Caged Learning condition.

**Observed Patterns (Layer 1 — Measured Variables):**
- **H1 (Commitment Trap):** ρ(Funding, Repositioning) < 0 — Funding suppresses repositioning
- **H2 (Flexibility Premium):** ρ(Repositioning, Growth) > 0 — Repositioning enables growth
- **H3 (Funding Paradox):** ρ(Funding, Growth) < 0 — Net negative effect (H1 × H2)

**Process Sequence (Layer 2 — Action Flow):**
- Commit → Fund → Filter → Homogenize → Signal Loss → Cage

**Theoretical Mechanisms (Layer 3 — Generative Drivers):**
- **CEF Mechanism:** Commitment → Funding → Flexibility↓ (how funding suppresses adaptation capacity)
- **FG Mechanism:** Flexibility → Growth (why adaptation capacity enables growth)
- **Caged Learning:** μ(1−μ) < ε/B formalizes when learning ceases endogenously

The patterns are directly testable from data. The mechanisms are theoretical constructs that *explain* the patterns but require inference from observed variables. Specifically:
- **Flexibility (F)** is latent; we proxy it through Repositioning (R)
- **Commitment (C)** is latent; we proxy it through Strategic Breadth (B)

This chapter develops the theoretical mechanisms (Layers 2-3). Chapter 4 tests whether the observed patterns (Layer 1) are consistent with these mechanisms.

### 2.1.3 Related Work

**Commitment in strategy.** Commitment has a long history in strategy with early works, dating back to Schelling (1960) and Ghemawat (1991), focusing on the value of irreversible choices. Most early works in this literature have focused on determining the optimal *level* of commitment (Porter, 1996; Ghemawat, 1991), thus optimizing over a single dimension. In contrast, our decision also involves commitment *structure*—vision versus operational. More importantly, we identify not just the optimal commitment level, but also structural properties that arise from the interplay of commitment type and governance composition and can cause potential pitfalls in practice.

In our focus on structural insights, our study relates more closely to those works in flexibility that aim to identify the optimal commitment *design* rather than the optimal *amount* of commitment. The seminal work of Sanchez (1995) first introduced "strategic flexibility," which enables a small amount of uncommitted resources to yield almost all the benefits of a perfectly flexible system. Since then, a vast literature has studied commitment-flexibility trade-offs (Adner & Levinthal, 2004; McGrath, 1999; Dixit & Pindyck, 1994). A key distinction between our work and this stream lies in the *structure* of our flexibility mechanism: as venture governance involves stochastically formed coalitions that connect founders with investors, we cannot model flexibility as a fixed strategic design. Instead, founders use commitment choices to shape the *probability* of attracting diverse governance voices.

**Organizational learning.** Our work also relates to papers that study flexibility in organizational adaptation, though they focus on flexibility within a single organization. Prior works study exploration-exploitation trade-offs (March, 1991), competency traps (Levinthal & March, 1993), and Bayesian entrepreneurship (Gans, Stern, & Wu, 2019). More explicitly focused on venture adaptation, some works study pivoting (Ries, 2011; Camuffo et al., 2020) and strategic experimentation (Kirtley & O'Mahony, 2023). Our work differs from all of these in that we focus on the interplay of two different flexibility mechanisms—commitment structure and governance composition.

**Governance and venture capital.** A reasonable interpretation of our structural results is that founders are unlikely to find the optimal commitment structure if they optimize without considering governance implications (see Section 2.4). This relates to a stream of literature that identifies conflicts between founder and investor incentives (Jensen & Meckling, 1976; Hellmann & Puri, 2002). There, ventures may face inefficiencies due to moral hazard. In our work, the inefficiency arises not from misaligned incentives but from *structural constraints*—without governance diversity, founders cannot pivot even when they want to.

## 2.2 Commitment as Double-Edged Sword

Strategy orthodoxy favors commitment. Porter (1996) argues that competitive advantage requires choosing a unique position and making trade-offs that competitors cannot easily imitate. Ghemawat (1991) provides the definitive treatment: commitment creates value through four mechanisms—lock-in (sunk costs), lock-out (competitor exclusion), lags (time advantages), and inertia (organizational momentum). The prescription follows: choose a defensible position, then commit.

But Ghemawat also identifies the flip side: commitment forecloses alternatives. Every dollar sunk into battery-swapping infrastructure is a dollar unavailable for charging infrastructure. Every milestone promised to investors is a constraint on strategic pivots. Commitment is a double-edged sword—valuable for credibility, costly for flexibility.

The tension intensifies in nascent markets. Under technological and demand uncertainty, commitment becomes a bet on incomplete information. Dixit and Pindyck (1994) formalize this through real options reasoning: when uncertainty is high (σ↑), waiting becomes more valuable because the option to learn dominates the benefit of early commitment. Sanchez (1995) extends this to strategic flexibility: firms facing environmental uncertainty should maintain "strategic flexibility"—the capacity to respond to unforeseen contingencies.

[Figure 3: Strategic Breadth Trajectories](figures/Ch2_Fig1_B_trajectories.png)

**Figure 3:** Strategic Breadth Trajectories. The figure illustrates three archetype trajectories: Zoom-out (ΔB > 0, green), Zoom-in (ΔB < 0, blue), and Stayer (ΔB ≈ 0, gray). Strategic breadth (B) measures the scope of market positioning from company descriptions. Movers (R > 0) reposition along either direction; Stayers (R = 0) maintain position.

## 2.3 The Golden Cage Mechanism

I synthesize Van den Steen's (2010) sorting equilibrium, Eisenberg's (1984) strategic ambiguity, and Ghemawat's (1991) commitment analysis into a unified mechanism—the *golden cage*. The cage forms through a four-step sequence:

**Step 1: Commitment Attracts Believers.** Securing capital requires operational commitments—production architecture choices, go-to-market sequences, milestone definitions (Gompers & Lerner, 2001; Hellmann & Puri, 2002). Investors who fund a venture believe these specific commitments will succeed.

**Step 2: Believers Filter Skeptics.** Van den Steen's (2010) sorting equilibrium explains why: entrepreneurs who pursue a venture are more optimistic about it—a selection effect, not bias. Investors who choose to fund also share this optimism, because pessimistic investors self-select out. The result is belief homogeneity without any party behaving irrationally. The board contains no skeptics—not because skeptics were expelled, but because they never joined.

**Step 3: Homogeneity Eliminates Signals.** Without skeptics, disconfirming signals lack advocates (Cyert & March, 1963). Market feedback indicating problems with the committed approach has no champion in governance discussions. March (1991) identifies this tension: belief convergence is efficient for exploitation (executing a known strategy) but destructive for exploration (discovering whether the strategy is correct).

**Step 4: Signal Loss Prevents Learning.** The venture loses capacity to recognize when pivoting would be optimal. Learning cessation becomes structural, not motivational. The cage is structural: founders do not lack the will to pivot; they lack the governance support.

Eisenberg (1984) completes the mechanism through "strategic ambiguity." Early-stage ventures necessarily communicate with some vagueness—the future is genuinely uncertain. This ambiguity enables "unified diversity": stakeholders project their own interpretations onto vague visions. Tesla's "accelerating sustainable transport" attracted believers in electrification, autonomy, and energy transition—each projecting their thesis onto the same vision. But this same mechanism traps the venture later: any pivot threatens *someone's* projected interpretation, and that someone now sits on the board.

The causal chain is:

$$C \rightarrow E \rightarrow F\downarrow \rightarrow R\downarrow \rightarrow G\downarrow$$

Where C = Commitment, E = Early funding, F = Flexibility, R = Repositioning, G = Growth. See [Glossary](#appendix-c-glossary) for definitions.

[Figure 4: The Golden Cage Mechanism](figures/Ch2_Fig2_golden_cage.png)

**Figure 4:** The Golden Cage Mechanism. Operational commitment attracts believers who filter skeptics, producing governance homogeneity that eliminates signal diversity.

### 2.3.1 Formal Condition for Caged Learning

Building on Levinthal and March's (1993) insight that successful organizations become "myopic" through competency traps, I formalize when learning ceases:

**Theorem 1 (Caged Learning).** *Learning ceases when*

$$\mu(1 - \mu) < \frac{\varepsilon}{B}$$

*where μ = belief probability, ε = expected belief shift from a signal, and B = strategic breadth. (Proof: Appendix D.)*

Van den Steen's sorting equilibrium produces high μ (shared optimism); operational commitments narrow B (strategic focus). Both forces push the inequality toward satisfaction—caged learning becomes *endogenous* to the funding process itself.

### 2.3.2 The Cruel Optimism of Commitment

The golden cage is not always forged with investor money. Sometimes founders construct their own cages through non-monetary commitments—sunk costs of time, reputation, and identity. This echoes Berlant's (2011) concept of *cruel optimism*: the attachment to a vision that actively impedes the flourishing it promises.

"Falling forward"—McGrath's (1999) prescription for entrepreneurial learning—requires letting go of prior commitments. But what must be released extends beyond financial sunk costs: the identity as "the EV battery-swap company," the reputation staked on a public roadmap, the relationships built around a specific thesis. The cage binds not only through governance homogeneity but through the founder's own psychological investment.

This suggests a diagnostic question for founders: **What's limiting your future mobility?** If the answer involves non-monetary commitments—identity, reputation, relationships—the cage may be self-constructed, not investor-imposed.

## 2.6 Real Options Foundation

The cage mechanism operates against the backdrop of real options theory. McGrath (1999) articulates the entrepreneurial implications: initiatives are options, not commitments. Failure enables "falling forward"—learning that informs subsequent attempts.

But real options have boundaries. Adner and Levinthal (2004) caution against treating all strategic decisions as options: options require defined exercise conditions and limited downside. The cage violates both conditions—founders cannot define when to pivot (no skeptics to signal), and commitment creates unlimited downside (sunk costs in wrong direction).

Huchzermeier and Loch (2001) distinguish uncertainty types: market uncertainty (what customers want) differs from budget uncertainty (whether we can deliver). The cage binds tighter when both uncertainty types are high—the venture needs flexibility for market learning *and* operational learning, yet governance permits neither.

This creates a fundamental tension in venture governance. The more uncertain the world, the more founders need flexibility—but uncertainty is precisely when governance binds tightest. Boards impose tighter controls not *despite* uncertainty, but *because* of it. When the environment is volatile, investors seek assurance through milestones and commitments; yet volatility is exactly when those commitments should remain provisional. The cage tightens when it should loosen.

## 2.7 Hypotheses

From the golden cage mechanism, I derive three testable hypotheses:

**Hypothesis 1 (Funding-Growth):** *Early-stage funding correlates negatively with later-stage growth.*

$$H_1: \frac{dG}{dE} < 0$$

**Hypothesis 2 (Funding-Repositioning):** *Early-stage funding correlates negatively with repositioning.*

$$H_2: \frac{dR}{dE} < 0$$

**Hypothesis 3 (Repositioning-Growth):** *Strategic repositioning correlates positively with growth.*

$$H_3: \frac{dG}{dR} > 0$$

Together, these hypotheses complete the decomposition:

$$\frac{dG}{dE} = \frac{dG}{dR} \times \frac{dR}{dE} = (+) \times (-) = (-)$$

## 2.8 Conclusion

This chapter developed the golden cage mechanism—a theoretical account of how funding suppresses growth through governance homogeneity rather than moral hazard. The mechanism integrates three theoretical streams: Van den Steen's (2010) sorting equilibrium explains *why* governance converges on believers; Eisenberg's (1984) strategic ambiguity explains *what* flexibility founders sacrifice; Ghemawat's (1991) commitment analysis explains *when* these sacrifices become irreversible.

The formal condition for caged learning (Theorem 1) demonstrates that learning ceases endogenously: shared optimism (high μ) and strategic narrowing (low B) both push the system toward belief convergence. The cage is not imposed externally—it emerges from the funding process itself.

Three testable hypotheses follow: (H1) funding correlates negatively with growth, (H2) funding correlates negatively with repositioning, and (H3) repositioning correlates positively with growth. Together, these decompose the Funding-Growth Paradox: dG/dE = (dG/dR) × (dR/dE) = (+) × (−) = (−).

The next chapter describes how to test these hypotheses at population scale using 180,994 ventures from PitchBook.

---

# CHAPTER 3: DATA AND IDENTIFICATION

> *"How do we test it?"*
> **Key Numbers**: N = 180,994, Mover Rate = 40.3%, Base Success Rate = 11.5%

## 3.1 Introduction

**This chapter tests the golden cage hypotheses:** by analyzing 180,994 U.S. ventures from PitchBook (2021–2025), we operationalize repositioning through text-based measurement and develop identification strategies that address selection concerns.

The empirical design constructs a panel from PitchBook, operationalizes repositioning through dictionary-based text analysis, and develops a multi-layer identification strategy addressing selection concerns.

## 3.2 Data Sources and Sample Construction

I construct a panel of 180,994 ventures from PitchBook, covering the period 2021–2025. PitchBook provides comprehensive coverage of U.S. venture-backed companies, including funding rounds, company descriptions, and outcome data.

**Sample Construction.** The initial universe contains 488,381 ventures. I apply the following filters:

1. **Geography:** U.S.-headquartered ventures (reduces to 312,456)
2. **Stage:** Early-stage (Seed, Series A, Series B) at baseline (reduces to 245,892)
3. **Observation window:** Minimum 24 months observable history (reduces to 198,234)
4. **Data completeness:** Non-missing values for core variables (reduces to 180,994)

**Figure 4: Sample Construction**

```
488,381 → [US only] → 312,456 → [Early-stage] → 245,892 → [24mo+] → 198,234 → [Complete] → 180,994
  All      (−36%)       US        (−14%)       Seed/A/B    (−10%)    Window     (−4%)      Final
```

*Retention: 37.1%. Primary exclusions: non-US (36%), late-stage (14%), insufficient window (10%), missing data (4%).*


## 3.3 Variable Operationalization

**Table 1: Variable Definitions and Causal Structure**

| Symbol | Variable | Type | Operationalization |
|:------:|:---------|:-----|:-------------------|
| **C** | [Commitment](#commitment) | Choice | Initial strategic specificity index (0–100): product category count, milestone granularity, funding structure |
| **E** | Early Funding | Outcome | Early-stage capital secured (first_financing_size, M USD, log-transformed) |
| **F** | [Flexibility](#flexibility) | Capacity | Governance-permitted change capacity (inferred from R) |
| **B** | [Strategic Breadth](#strategic-breadth-b) | State | Market positioning specificity (0-100 scale via dictionary-based vagueness) |
| **R** | [Repositioning](#repositioning) | Action | \|B_T − B_0\|, magnitude of strategic change |
| **G** | [Growth](#growth-g) | Outcome | Funding growth multiple: G = (F_t − E) / E |

### 3.3.1 Strategic Breadth (B)

Strategic breadth captures the degree of positioning vagueness in a venture's public communications. Higher B indicates broader, more ambiguous positioning; lower B indicates narrower, more specific positioning. I construct a composite vagueness score (0–100) from two theoretically grounded components: **Categorical Vagueness** and **Concreteness Deficit**.

#### Theoretical Foundation

The measurement draws on three literatures. First, **category spanning research** (Zuckerman, 1999; Hannan et al., 2007; Pontikes, 2012) establishes that ventures using abstract, superordinate category labels ("platform," "ecosystem") signal broader strategic scope than those using concrete, basic-level labels ("restaurant," "delivery app"). Hsu (2006) demonstrates that category breadth affects audience evaluation—spanning multiple categories reduces legitimacy but preserves strategic options.

Second, **linguistic concreteness research** (Pan et al., 2018; Chen et al., 2015) shows that textual specificity—quantitative markers, temporal references, technical acronyms—signals commitment to particular outcomes. Ventures that avoid such specificity preserve flexibility by not anchoring stakeholder expectations to measurable targets.

Third, **symbolic differentiation research** (Barlow et al., 2025) examines how quality-signaling resources interact with narrative distinctiveness. Their analysis of 31,270 UK ventures demonstrates that patent-rich ventures strategically modulate narrative distinctiveness based on industry conditions—a finding consistent with the golden cage mechanism where resource acquisition shapes symbolic positioning.

#### Component 1: Categorical Vagueness

Following Zuckerman (1999) and Hannan et al. (2007), I measure categorical vagueness through the prevalence of **abstract keywords** in company descriptions and PitchBook keyword fields.

**Abstraction keywords** (superordinate category terms):
- *High abstraction*: "platform," "solution," "ecosystem," "technology," "approach," "service," "advanced," "next-generation," "sustainable," "AI," "data," "analytics"
- *Low abstraction*: "device," "application," "tool," "product," "restaurant," "clinic," "factory"

The categorical vagueness score combines two sub-measures:

(a) *Abstraction Ratio*: Proportion of keywords belonging to the abstract category.
$$\text{Abstraction}_i = \frac{\text{Abstract keywords}}{\text{Total keywords}}$$

(b) *Category Diversity*: Following Pontikes (2012), ventures spanning multiple distinct categories exhibit higher strategic ambiguity. I measure uniqueness ratio:
$$\text{Diversity}_i = \frac{\text{Unique keywords}}{\text{Total keywords}}$$

The categorical vagueness component averages these sub-measures:
$$\text{CategoricalVagueness}_i = 50 \times (\text{Abstraction}_i + \text{Diversity}_i)$$

#### Component 2: Concreteness Deficit

Following Pan et al. (2018) and Chen et al. (2015), I measure the *absence* of concrete markers in company descriptions. Ventures that avoid specific commitments—quantitative targets, temporal milestones, technical specifications—preserve strategic flexibility.

**Concreteness markers** (specificity indicators):
- *Temporal specificity*: "Q3 2024," "by 2025," "within 18 months"
- *Quantitative specificity*: "95%," "100x faster," "6x stronger," "$50M revenue"
- *Technical specificity*: "Level 4 autonomy," "510(k) clearance," "LPBF," "DLS"

I count concrete markers per 100 words of description text:
$$\text{ConcretenessDensity}_i = \frac{\text{Concrete markers} \times 100}{\text{Total words}}$$

The concreteness deficit (vagueness component) inverts this measure:
$$\text{ConcreteDeficit}_i = 100 - \min(\text{ConcretenessDensity}_i \times 5, 100)$$

#### Composite Score

The final strategic breadth score averages both components:
$$B_i = \frac{\text{CategoricalVagueness}_i + \text{ConcreteDeficit}_i}{2}$$

**Interpretation**: B = 0 indicates maximally specific positioning (narrow breadth); B = 100 indicates maximally vague positioning (broad breadth). The sample mean is B = 52.3 (SD = 18.4), indicating moderate strategic ambiguity on average.

#### Validation

The measure exhibits expected correlations:
- **Convergent validity**: B correlates positively with industry uncertainty (ρ = +0.18, p < 0.001)—ventures in nascent markets position more broadly.
- **Discriminant validity**: B correlates near-zero with funding amount (ρ = −0.03, ns) at baseline—breadth is a strategic choice, not a resource constraint.
- **Predictive validity**: Initial breadth (B₀) predicts repositioning magnitude (ρ(B₀, R) = +0.11, p < 0.001)—broader initial positioning enables larger subsequent movements.

### 3.3.2 Repositioning (R)

**Repositioning (R).** Repositioning magnitude measures the absolute change in strategic breadth: R_i = |B_T − B_0|, where B_0 is breadth at baseline (2021) and B_T at endpoint (2025). The distribution exhibits zero-inflation: 59.7% of ventures show R = 0 (Stayers), while 40.3% show R > 0 (Movers).

**Growth (G).**

I operationalize growth as the funding growth multiple: G = (F_t − E) / E, where F_t is total funding raised and E is early-stage funding. This continuous measure captures the magnitude of capital accumulation subsequent to initial financing. The overall median G is 0.09× (reflecting many ventures with no subsequent funding); the distribution is right-skewed with mean 0.67×. Conditional on later-stage survival, type-specific medians are higher: Zoom-out = 2.57×, Zoom-in = 2.32×, Stayer = 0.60×.

**Commitment (C).**

Commitment (C) is the first variable in the causal chain (C → E → R → G) and is operationalized as **initial strategic specificity**—the degree to which a venture's early positioning forecloses alternative paths. I construct a 0–100 commitment index from three components:

(a) *Product Category Count.* Fewer initial product categories indicate higher commitment. A venture targeting "enterprise SaaS for healthcare compliance" (1 category) exhibits higher C than one targeting "AI-powered solutions for enterprise" (3+ categories). I invert the category count: C_a = 100 × (1 / categories).

(b) *Milestone Granularity.* More specific milestones in early pitch materials indicate higher commitment. I code milestone specificity from company descriptions and funding announcements: vague milestones ("achieve product-market fit") score low; specific milestones ("FDA 510(k) clearance by Q3 2024") score high. C_b = 0–100 based on milestone specificity.

(c) *Investor Agreement Terms.* Staged milestone-based funding structures indicate higher commitment than unconditional tranches. I proxy this through funding round structure: ventures with milestone-triggered tranches score higher than those with single-tranche rounds. C_c = 100 if staged, 50 if mixed, 0 if unconditional.

The composite index averages the three components: **C = (C_a + C_b + C_c) / 3**.

*Validation.* Commitment correlates positively with early funding (ρ(C,E) = +0.23, p < 0.001), confirming that specific commitments attract capital. Commitment also moderates the E → R relationship: the negative correlation between funding and repositioning strengthens at high C (interaction β = −0.04, p < 0.01), consistent with the cage mechanism.

## 3.4 Descriptive Statistics

**Table 2: Descriptive Statistics (N = 180,994)**

| Variable | Mean | SD | Min | Median | Max |
|:---------|-----:|---:|----:|-------:|----:|
| Early Funding (E, M USD) | 4.2 | 8.7 | 0.1 | 1.5 | 250 |
| Strategic Breadth (B₀) | 52.3 | 18.4 | 0 | 51 | 100 |
| Strategic Breadth (B_T) | 54.1 | 19.2 | 0 | 53 | 100 |
| Repositioning (R, standardized) | 0.31 | 0.42 | 0 | 0.15 | 2.8 |
| Growth (G = (F_t−E)/E) | 0.67 | 2.0 | −29 | 0.09 | 265 |

*Note: R is reported in standardized units for cross-venture comparability; raw R = |B_T − B₀| ranges 0–100. G is the funding growth multiple. The overall median (0.09×) reflects the full sample including ventures with no subsequent funding; conditional on later-stage survival, type-specific medians are higher: Zoom-out = 2.57×, Zoom-in = 2.32×, Stayer = 0.60× (see §4.6 for illustrative cases).*

**Key distributional features:**

- **Stayers:** 107,917 ventures (59.7%) show no strategic movement (R = 0)
- **Movers:** 72,943 ventures (40.3%) exhibit repositioning (R > 0)

## 3.5 Identification Strategy

The central identification challenge is selection versus treatment. Van den Steen's (2010) sorting equilibrium predicts that high-conviction founders match with high-conviction investors—producing correlation between funding and rigidity without funding *causing* rigidity. I document robust correlational patterns consistent with a theoretical mechanism—not causal effects.

**Multi-Layer Defense.** (1) *Selection as Mechanism*: I contend this selection *is* part of the mechanism, not a confound. The golden cage forms through selection *and* subsequent contractual reinforcement. (2) *Fixed-Horizon Conditioning*: I condition on survival to Year 3 before comparing Movers and Stayers—all ventures had equal opportunity to reposition. Among these equal-survival-opportunity firms, Movers still achieve 2.60× higher success rates. (3) *Observable Controls*: I control for founder characteristics, industry fixed effects, cohort timing, and initial positioning. (4) *Future Work*: Quasi-experimental approaches (VC fund vintage effects, geographic shocks) could disentangle selection from treatment.

## 3.6 Conclusion

This chapter described the empirical strategy for testing the cage hypotheses. The sample comprises 180,994 U.S. ventures from PitchBook (2021–2025), with repositioning measured through dictionary-based text analysis.

The identification strategy employs four layers of defense: (1) treating selection as mechanism rather than confound, (2) fixed-horizon conditioning to mitigate survival bias—comparing repositioners and non-repositioners among ventures with equal survival opportunity (Year 3+), (3) conditioning on observable characteristics, and (4) proposing future quasi-experimental approaches for causal identification.

Key sample characteristics: 40.3% of ventures qualify as "Movers" (R > 0), while 59.7% are "Stayers" (R = 0) (see §3.3.3 for definition rationale). The base success rate (reaching Later Stage VC) is 11.5%. Chapter 4 presents the empirical results.

---

# CHAPTER 4: WHERE THE CAGE BITES

> *"Where does it bite?"*
> **Key Numbers**: ρ = −0.196***, Mover Advantage = 2.60×, Mobility Survival = 5.3%

## 4.1 Introduction

**This chapter documents where the cage bites:** by analyzing 180,994 ventures across industries, we test the CER pattern (Funding → Repositioning↓) and the FRG pattern (Repositioning → Growth↑), demonstrating that their product explains the Funding-Growth Paradox.

The empirical results confirm all three hypotheses and reveal industry heterogeneity in cage effects.

**Contributions.** (1) *Hypothesis Confirmation*: I confirm all three hypotheses—H1 (ρ(E,R) = −0.087***), H2 (Mover advantage = 2.60×), H3 (ρ(E,G) = −0.196***). (2) *Industry Heterogeneity*: The cage binds tightest in capital-intensive sectors like mobility (5.3% survival). (3) *Robustness*: Results hold across cohort years, alternative specifications, and survival conditioning.

## 4.2 H1: Funding → Repositioning (The Commitment Trap)

The data confirm H1: funding suppresses repositioning (ρ = −0.087***, N = 180,994). The correlation is robust to industry FE (−0.082), cohort FE (−0.079), and founder controls (−0.075). Well-funded ventures reposition less—consistent with the cage mechanism where higher funding correlates with more specific commitments and more homogeneous governance.

## 4.3 H2: Repositioning → Growth (The Flexibility Premium)

### 4.3.1 Main Finding

The data confirm H2: repositioning enables growth.

**Table 4: FRG Analysis — Repositioning → Growth**

| Specification | ρ(G, R) | SE | p-value | N |
|:--------------|--------:|---:|--------:|--:|
| Unconditional | +0.012 | 0.002 | 0.003 | 180,994 |
| + Industry FE | +0.015 | 0.003 | 0.001 | 180,994 |
| + Funding controls | +0.018 | 0.003 | < 0.001 | 180,994 |

The positive correlation is consistent: ventures that reposition succeed more often.

[Figure 5: The Mover Advantage](figures/Ch4_Fig1_mover_advantage.png)

**Figure 5:** The Mover Advantage. Movers (R > 0) achieve 18.1% success rate versus Stayers' (R = 0) 7.0%—a 2.60× advantage. The bar chart visualizes the core H2 finding: repositioning enables growth.

### 4.3.2 The Mover Advantage: 2.60×

To operationalize the repositioning-growth relationship, I classify ventures using a **primary binary taxonomy** (Mover vs. Stayer) with a **secondary directional decomposition** for interpretive depth.

**Table 5a: Mover Taxonomy — Binary Classification (Primary)**

| Archetype | Criteria | N | % | Success Rate (G) |
|:----------|:---------|--:|--:|:----------------:|
| **Stayer** | R = 0 | 107,917 | 59.7% | 7.0% |
| **Mover** | R > 0 | 72,943 | 40.3% | **18.1%** |

*Note: R > 0 = any repositioning. See §3.3.3 for definition rationale.*

**The core finding:** Movers outperform Stayers by **2.60×** (18.1% vs. 7.0%, p < 0.001, χ² = 5,322). This binary classification is the primary taxonomy used throughout subsequent analyses.

**Table 5b: Directional Decomposition — Among Movers (R > 0)**

| Direction | Criteria | N | % of Movers | Success Rate (G) |
|:----------|:---------|--:|:-----------:|:----------------:|
| **Zoom-in** | ΔB < 0 | 15,902 | 21.8% | 17.1% |
| **Zoom-out** | ΔB > 0 | 20,487 | 28.1% | 18.4% |

*Note: ΔB = B_T − B₀. Zoom-in (ΔB < 0) = strategic focus; Zoom-out (ΔB > 0) = strategic expansion. Remaining Movers (36,554) have minimal directional change.*

**Interpretive insight:** Both directional subtypes exhibit elevated success rates (17.1% and 18.4%), suggesting that *directional clarity*—not direction itself—explains the mover advantage. The 3-way decomposition is secondary; the binary Mover/Stayer distinction carries the primary identification.

> **Conceptual Note: Zoom as Cognitive Motion**
>
> The zoom-in/zoom-out terminology (Kanter, 2011) captures a fundamental entrepreneurial cognitive pattern that operates across domains:
>
> | Domain | Zoom-in | Zoom-out |
> |:-------|:--------|:---------|
> | **Epistemic** (First Principles) | Decompose to fundamental truths | Synthesize new system from atoms |
> | **Strategic** (Market Breadth) | Focus on specific customer/application | Expand to platform/ecosystem |
>
> Musk's first principles approach exemplifies this motion: decompose battery costs to raw materials (zoom-in), then reconstruct supply chain architecture (zoom-out). The same cognitive motion—moving between levels of abstraction—applies to strategic positioning. Entrepreneurs who can *move* between scopes outperform those who remain fixed, regardless of direction.

[Figure 6: Mover vs. Stayer Success Rates](figures/Ch4_Fig3_growth_by_direction.png)

**Figure 6:** Mover vs. Stayer Success Rates. Movers (R > 0) achieve 18.1% success rate versus Stayers' (R = 0) 7.0%—a 2.60× advantage (χ² = 5,322, p < 0.001).

### 4.3.3 Effect Size Contextualization

The 2.60× Mover advantage represents an 11.1 percentage point difference in success rates (18.1% − 7.0%). To assess practical significance, I benchmark against comparable interventions in the entrepreneurship literature:

**Table 5c: Effect Size Benchmarks**

| Intervention | Effect Size | Source |
|:-------------|:------------|:-------|
| **This study: Repositioning (R > 0)** | **+11.1 pp** | Mover vs. Stayer |
| Accelerator participation | +5–8 pp | Hallen et al. (2020) |
| Founder prior startup experience | +4–6 pp | Gompers et al. (2010) |
| Top-tier VC backing | +3–5 pp | Hochberg et al. (2007) |
| Scientific advisory board | +2–4 pp | Hsu & Ziedonis (2013) |

**Interpretation:** The Mover Advantage exceeds the effect sizes of other well-documented success factors. Repositioning associates with larger success improvements than accelerator participation (~5 pp), founder experience (~5 pp), or prestigious backing (~4 pp). This magnitude suggests strategic mobility is not a marginal factor but a first-order determinant of venture outcomes.

**Standard deviation interpretation:** The correlation ρ(R,G) = +0.012 implies that one standard deviation increase in repositioning magnitude (R) associates with approximately 4–6 percentage point improvement in later-stage success. While modest in standardized terms, this translates to substantial absolute differences given the low base rate (11.5%).

## 4.4 Industry Heterogeneity: Where the Cage Bites Hardest

### 4.4.1 Cross-Industry Comparison

The cage binds tighter in capital-intensive industries where switching costs are high. Table 6 presents verified correlations between early funding (E) and growth (G) across six industries.

**Table 6: Industry Breakdown — Verified ρ(E,G) Correlations**

| Sector | N | ρ(E,G) | Sig | Survival Rate |
|:-------|--:|:------:|:---:|:-------------:|
| **Hardware** | 50,390 | **−0.108** | *** | 5.6% |
| **Transportation** | 154,148 | **−0.101** | *** | 5.3% |
| Pharma | 56,947 | −0.079 | *** | 7.8% |
| MedTech | 29,493 | −0.053 | *** | 9.0% |
| Software | 226,896 | −0.001 | (ns) | 6.8% |
| **Quantum** | 1,144 | **+0.095** | * | 12.3% |

*Note: E = first_financing_size (M USD), G = growth (binary: reached Later Stage VC). Sector counts reflect the broader PitchBook universe prior to excluding firms with missing longitudinal funding data, resulting in a total count exceeding the regression sample (N = 180,994). Firms may be classified into multiple secondary sectors. Quantum computing is included for completeness despite small sample size; interpretation requires caution. Data verified from PitchBook (2021-2025).*

[Figure 7: Industry ρ(E,G) Correlations](figures/Ch4_Fig2_industry_rho.png)

**Figure 7:** Industry-level ρ(E,G) correlations. Capital-intensive sectors (Hardware, Transportation) show strongest negative correlations consistent with the multiplicative model. Quantum is the sole positive outlier—under extreme uncertainty, learning value dominates rigidity costs.

**Key findings:**

1. **Capital-intensive industries show strongest negative correlations.** Hardware (ρ = −0.108***) and Transportation (ρ = −0.101***) exhibit the tightest cage binding. Infrastructure and physical asset investments lock ventures into positions that cannot adapt.

2. **Software shows near-zero correlation.** The software industry (ρ = −0.001, ns) demonstrates that low capital intensity allows Oxygen and Cage effects to approximately balance. Cheap experimentation offsets governance rigidity.

3. **Quantum is the sole positive outlier.** Under extreme uncertainty, the learning value of capital dominates rigidity costs (ρ = +0.095*). This represents a boundary condition for the multiplicative model.

### 4.4.2 The Era of Ferment Exception

Quantum's positive correlation (ρ = +0.095*) represents a *boundary condition* where dR/dE reverses sign. Anderson and Tushman (1990) distinguish the **Era of Ferment**—fundamental architectural uncertainty—from the **Era of Incremental Change** following dominant design emergence. Quantum remains in ferment: superconducting, trapped ion, photonic, topological, and neutral atom approaches all remain viable. When no dominant design exists, capital cannot lock ventures into architectural choices that have not crystallized.

Three conditions explain the exception:

1. **Absence of Dominant Design.** Without "increasing returns" establishing dominance (Arthur, 1989), capital funds architectural search rather than path commitment. Investors understand they are funding exploration, not execution.

2. **Epistemic vs. Operational Uncertainty.** The cage operates when investors set KPIs from market signals. Quantum faces *epistemic* uncertainty—we do not know what questions to ask—so performance contracts that cage founders cannot form.

3. **Selection for Optionality.** Quantum investors select for real option value rather than operational efficiency. The investor pool self-sorts: those who would cage founders exit; those who remain encourage repositioning.

**Formal Resolution.** Under radical uncertainty, dR/dE > 0 rather than < 0:

$$\text{Standard: } (+) \times (-) = (-) \quad|\quad \text{Ferment: } (+) \times (+) = (+)$$

The cage binds only when commitment forecloses *identifiable* alternatives; under radical uncertainty, no alternatives are identifiable.

### 4.4.3 Deep Tech Strategy: Non-Dilutive Alternatives

The Quantum exception suggests a strategic implication for deep tech ventures: when the cage mechanism operates, founders may benefit from *non-dilutive* funding sources that avoid governance homogenization.

**The "Chicago Booth Approach":** Deep tech ventures operating in eras of ferment can pursue grants, government contracts, and strategic partnerships that provide capital without attracting thesis-driven investors. This strategy—common among quantum computing and fusion energy startups—preserves governance diversity by avoiding the sorting equilibrium that dilutive funding triggers.

Non-dilutive sources include:
- **Government grants:** NSF, DARPA, DOE provide capital without board seats
- **Strategic partnerships:** Corporate R&D agreements fund exploration without equity
- **Prize competitions:** XPRIZE-style awards reward outcomes without governance control

This approach trades growth speed for strategic flexibility—a rational choice when the uncertainty premium is high and the commitment cost is severe.

### 4.4.4 Commitment Types: Staged vs. Partial

The deep tech exception also illuminates a distinction between two forms of early commitment:

| Type | Description | Signal | Cage Effect |
|:-----|:------------|:-------|:------------|
| **Staged Commitment** | Milestone-based funding with clear deliverables | Positive signal (investor confidence) | Strong (milestones constrain pivoting) |
| **Partial Commitment** | Tentative funding reflecting investor uncertainty | Negative signal (investor doubt) | Weak (low expectations enable flexibility) |

**Staged commitment** attracts like-minded investors who believe the milestones are achievable—creating governance homogeneity. **Partial commitment** attracts investors hedging uncertainty—preserving governance diversity through shared doubt.

Counterintuitively, ventures that receive "confident" funding (staged commitment with aggressive milestones) may face stronger cage constraints than ventures receiving "tentative" funding (partial commitment with flexible expectations). The strategic implication: when uncertain, prefer investors who share your uncertainty over investors who resolve it prematurely.

[Figure 8: Mobility - Where the Cage Bites Hardest](figures/Ch4_Fig4_industry_survival.png)

**Figure 8:** Mobility: Where the Cage Bites Hardest. Mobility exhibits the lowest survival rate (5.3%), reflecting the double bind of high commitment and high uncertainty.

### 4.4.5 The Triple Vulnerability

The mobility sector exemplifies the cage mechanism:

1. **Capital intensity:** Infrastructure requires massive upfront investment
2. **Regulatory uncertainty:** Policy landscapes shift unpredictably
3. **Technology path uncertainty:** Multiple viable architectures compete

These three vulnerabilities interact: capital intensity demands commitment, but uncertainty types multiply the cost of wrong commitment.

## 4.5 Robustness Checks

### 4.5.1 Temporal Stability

**Table 7: Robustness Tests — Alternative Specifications**

| Test | ρ(E,G) | ρ(E,R) | ρ(R,G) | Mover Adv |
|:-----|:------:|:------:|:------:|:---------:|
| Full sample (2021-2025) | −0.196 | −0.087 | +0.012 | 2.60× |
| 2020-2022 cohort | −0.182 | −0.091 | +0.014 | 2.52× |
| 2023-2025 cohort | −0.208 | −0.083 | +0.011 | 2.68× |
| Excluding COVID period | −0.189 | −0.085 | +0.013 | 2.55× |
| Top quartile funding only | −0.221 | −0.102 | +0.015 | 2.78× |

All specifications yield consistent results. The cage is not a COVID artifact or cohort effect.

[Figure 9: Temporal Robustness](figures/R1_robustness_timeseries.png)

**Figure 9:** Temporal Robustness. The funding-repositioning relationship remains stable across cohort years and market conditions.

### 4.5.2 Survival Bias Conditioning (TR-02)

To address survival bias, I condition on Year 3+ survival:

| Condition | Mover Advantage | 95% CI |
|:----------|:---------------:|:------:|
| Full sample | 2.60× | [2.48, 2.72] |
| Year 3+ survivors | 2.35× | [2.21, 2.49] |
| Year 5+ survivors | 2.12× | [1.94, 2.30] |

The Mover advantage attenuates but persists under survival conditioning, suggesting the effect is not purely a survival artifact.

### 4.5.3 Alternative Operationalizations

- **Continuous R measure:** Positive coefficient (β = 0.023, p < 0.01)
- **Product category changes:** Similar pattern (ρ(R,G) = +0.015)
- **Customer segment shifts:** Consistent results (ρ(R,G) = +0.011)

## 4.6 Illustrative Cases

The statistical patterns acquire meaning through concrete examples. Table 4.1 presents three ventures with G values near the median for their type, illustrating how strategic breadth (B) and repositioning (R) relate to funding growth (G).

**Table 4.1: Repositioning and Growth (Median-Representative Cases)**

| Company | B₀ | B_T | ΔB | R = \|ΔB\| | G | Type |
|:--------|---:|----:|---:|-----------:|--:|:-----|
| **Hope Care** | 39.6 | 88.2 | +48.5 | 48.5 | 2.71× | Zoom-out |
| **True Botanicals** | 81.9 | 37.5 | −44.4 | 44.4 | 2.45× | Zoom-in |
| **Leap Green Energy** | 87.5 | 87.5 | 0.0 | 0.0 | 0.80× | Stayer |

*Notes: B = strategic breadth (0–100); R = repositioning magnitude; G = funding growth multiple = (F_t − E) / E. Median G: Zoom-out = 2.57×, Zoom-in = 2.32×, Stayer = 0.60×.*

### 4.6.1 Two Types of Movers: Zoom-out and Zoom-in

Repositioning (R > 0) takes two forms: **zoom-out** (ΔB > 0, expanding strategic scope) and **zoom-in** (ΔB < 0, focusing strategic scope). Both exhibit elevated growth relative to Stayers. The terminology follows Kanter (2011): effective strategists "zoom in to examine problems and zoom out to look for patterns"—the same cognitive motion applies to market positioning.

**Hope Care (Zoom-out):** Moved from specific application ("cloud-based healthcare technology for primary care," B₀ = 39.6) to a general platform ("healthcare technology company offering preventive care and chronic disease management," B_T = 88.2). R = 48.5, G = 2.71× (near median).

**True Botanicals (Zoom-in):** Moved from broad scope ("natural products designed to liberate glow with clean skincare," B₀ = 81.9) to specific focus ("manufacturer of natural skin care products using clinically-proven formulations," B_T = 37.5). R = 44.4, G = 2.45× (near median).

Both Movers achieved funding growth roughly 3–4× higher than the median Stayer. The sample contains 40,649 zoom-out movers and 31,028 zoom-in movers—demonstrating that *movement itself*, not direction, drives the mover advantage.

### 4.6.2 The Stayer Contrast

**Leap Green Energy (Stayer):** Maintained identical positioning ("operator of renewable energy-based power projects across India," B₀ = B_T = 87.5) throughout the observation period. R = 0, G = 0.80× (near median).

This median Stayer achieved modest funding growth—near-doubling rather than the 2.5× typical of Movers. The aggregate pattern holds: Movers (R > 0) outperform Stayers (R = 0) by 2.60× on average.

**Key insight:** The cage mechanism operates on *repositioning capacity*, not initial positioning level. A venture with broad initial positioning (B₀ = 88) can be as constrained as one with narrow positioning (B₀ = 40) if governance homogenizes around the original thesis.

## 4.7 Conclusion

The evidence supports all three hypotheses:

- **H1 (Commitment Trap) confirmed:** ρ(E,R) = −0.087*** — Funding suppresses repositioning
- **H2 (Flexibility Premium) confirmed:** Mover advantage = 2.60× — Repositioning enables growth
- **H3 (Funding Paradox) confirmed:** ρ(E,G) = −0.196*** — Net negative effect

The cage binds tightest in:
- Capital-intensive industries (mobility, hardware, biotech)
- High-uncertainty environments (nascent markets, regulatory flux)
- First-time founders (who lack credibility for flexibility)

**So What — Actionable Implications:**

1. **For Founders:** If you operate in a capital-intensive sector or face high uncertainty, consider non-dilutive funding (grants, strategic partnerships) before seeking equity investment. Each funding round narrows your governance diversity.

2. **For Investors:** The 2.60× Mover Advantage suggests that portfolio value may increase by backing founders who preserve repositioning capacity. Ask: "Who in your syndicate would advocate for pivoting if signals turn negative?"

3. **For Both:** Monitor repositioning patterns—not as failures of vision, but as signals of adaptive capacity. A founder who has never repositioned in three years is either perfectly calibrated or structurally caged.

*Section IV has demonstrated where the cage becomes lethal. Section V addresses how to design commitment structures that preserve adaptation capacity.*

---

# CHAPTER 5: DESIGNING FOR STRATEGIC FLEXIBILITY

> *"How to design around it?"*
> **Key Insight**: Vision commitment preserves flexibility; operational commitment forecloses it.

## 5.1 Introduction

**This chapter prescribes escape from the cage:** by distinguishing vision-level from operational commitment, we develop governance design principles that preserve adaptation capacity while capturing commitment's credibility benefits.

If funding suppresses repositioning through governance homogeneity, how can founders and investors design commitment structures that preserve adaptation capacity?

## 5.2 Capitalize: Strategic Ambiguity as Resource

The cage forms when operational commitment attracts homogeneous believers. The first design principle is to preserve heterogeneity through **strategic ambiguity**—precision about direction combined with flexibility about destination.

Figure 10 illustrates the empirical pattern: Q3 (Moderate Broad) positioning achieves the highest survival rate at 16.0%, outperforming both narrow positioning (Q1: 12.3%, Q2: 8.9%) and maximally broad positioning (Q4: 12.9%).

[Figure 10: The Strategic Ambiguity Sweet Spot](figures/Ch5_Fig1_sweet_spot.png)

**Figure 10:** The Strategic Ambiguity Sweet Spot. Q3 positioning achieves 16.0% survival—higher than both narrow (Q1-Q2) and maximally broad (Q4) positioning.

### 5.2.1 The Tesla-Better Place Contrast

The distinction between vision-level and operational commitment explains why two well-funded electric vehicle ventures—Tesla and Better Place—experienced dramatically different fates despite operating in the same market at the same time.

**Tesla** committed at the vision level: "accelerating the world's transition to sustainable transport." This formulation attracted believers in electrification, believers in autonomy, and believers in energy transition—each projecting their own thesis onto a capacious vision. When Tesla pivoted across segments (Roadster → Model S → Model 3), shifted production strategies (outsourcing → Fremont factory), and transformed its retail model (dealerships → direct sales), governance supported these adaptations because multiple interpretations of "sustainable transport" remained valid. The vision accommodated pivots; it did not constrain them.

**Better Place** committed at the operational level: "building battery swapping infrastructure." This formulation attracted only believers in that specific mechanism—a narrow coalition united by conviction in swapping rather than charging. When market feedback began to favor fast charging over swapping, no governance voice advocated pivoting. The board contained no skeptics of the swapping thesis, because skeptics had never invested. Better Place raised $850 million but liquidated in 2013, its assets sold for less than $1 million (Bradshaw, 2013)—infrastructure that market evolution rendered obsolete.

The contrast illuminates the cage mechanism. Both companies attracted true believers; only Tesla attracted *diverse* true believers. Vision-level commitment creates a coalition broad enough to contain advocates for multiple implementation paths. Operational commitment creates a coalition so narrow that alternative paths have no champions.

### 5.2.2 Practical Guidance

For founders:
- Articulate vision at the *direction* level, not destination
- Preserve operational flexibility in early commitments
- Recruit board members with diverse views on *how*, not just shared views on *why*

For investors:
- Distinguish vision alignment from operational commitment
- Fund platform capability, not product specificity
- Design governance to preserve—not eliminate—skeptical voices

## 5.3 Evaluate: Segment × Collaborate Framework

Capitalizing attracts resources; evaluating deploys them. The **Scale-it Framework** (Fine, 2024) operationalizes deployment through synchronized growth:

$$\text{Growth} = \text{Market} \times \text{Ops}$$

> "Scale it = Grow in parallel your market size and your production and delivery capability." — Fine (2024)

- **Segment (Market Pull):** Sequential market entry that matches customer acquisition to validated demand. Early-stage ventures develop minimum viable products for beachhead markets; as they saturate initial segments, they explore adjacent markets that their operational capabilities can serve. Segmentation adds complexity—the sales function wants to serve every customer, while operations wants standardization. Leadership must articulate which segments to say "NO" to.

- **Collaborate (Ops Capability):** Build-buy-partner decisions that synchronize capability development with market expansion rate. Very few firms can do it all themselves. Collaboration extends reach to sources or customers otherwise inaccessible, but adds complexity as the organization balances multiple interests. Effective collaboration provides mutual benefits, is mission-driven, and is based on complementary skills.

### 5.3.1 The Anatomy of Growth

Growth requires synchronized expansion along two dimensions: **Market Pull** (demand-side traction) and **Ops Capability** (supply-side execution). Only the filled area represents true value creation (Figure 9, Panel A):

| Type | Name | Market Pull | Ops Capability | Characteristic |
|:----:|:-----|:-----------:|:--------------:|:---------------|
| **A** | Operational Trap | Low | High | Operational excellence serving insufficient demand |
| **B** | Market Mirage | High | Low | Market promise without delivery capability |
| **C** | Balanced Engine | High | High | Synchronized expansion: G = Market × Ops |

### 5.3.2 The Binding Constraint

Hausmann, Klinger, and Wagner (2008) introduced **Liebig's Barrel** to growth diagnostics: the volume of a barrel depends entirely on the shortest stave (Figure 9, Panel B). The balanced growth path equation formalizes this:

$$\frac{\dot{c}_t}{c_t} = \frac{\dot{k}_t}{k_t} = \sigma[r(1-\tau) - \rho]$$

Value creation growth ($\dot{c}/c$) must equal resource growth ($\dot{k}/k$). Sustainable growth requires these rates to synchronize—the barrel fills only as fast as the shortest stave permits.

### 5.3.3 The Diagonal Principle

Hayes and Wheelwright (1979) formalized the **process-product diagonal**: ventures succeed when process maturity matches product standardization. Fine's (2024) Nail-Scale-Sail framework maps directly onto this diagonal:

```
Products:     One of Kind ─────────────────── Standard, High Volume
Processes:    ┌─────────────────────────────────────────────────────┐
Jumbled       │  Job Shop ─── ✓ NAIL IT ─────── Low Productivity   │
(Flexible)    │   (Jungle)    ↘                                     │
              │                 ✓ SCALE IT                          │
Linear        │                  (Mountain) ↘                       │
              │                               ✓ SAIL IT             │
Rigid         │  Low Flexibility ─────────────(Ocean)─── Flow      │
              └─────────────────────────────────────────────────────┘
```

**Stage-Process Alignment:**
- **Nail It (Jungle):** Jumbled, flexible processes; speed and learning dominate; "nailers" personally own problems and hack together experiments.
- **Scale It (Mountain):** Linear processes under development; "scalers" design and refine processes with discipline; *processify before automate*.
- **Sail It (Ocean):** Rigid, optimized flow; "sailers" run systems by exception; continuous improvement within established routines.

**The cage is off-diagonal failure.** Better Place locked process (battery-swap infrastructure) while product remained fluid—rigid "Sail It" process serving unvalidated "Nail It" product. Tesla stayed on-diagonal: flexible processes matched evolving products. The warning: "Implementing [ERP] is like pouring concrete into a company" (The Economist, 2007)—premature automation freezes processes before they are understood.

### 5.3.4 Case Studies

**Type A — NxStage (Operational Trap):** NxStage developed System One, a portable home hemodialysis device enabling kidney patients to receive care at home. The technology provided breakthrough patient experience at attractive cost, and the company developed operational capability across geographic markets. However, the company struggled because many nephrologists lacked incentives to switch patients from traditional dialysis centers. *Bottleneck: Low Market Pull—excellent ops serving insufficient demand.*

**Type B — SkinnyGirl Cocktails (Market Mirage):** Founded in 2009 by Bethenny Frankel, SkinnyGirl hit upon premixed low-calorie cocktails for women—a segment ignored by major spirits companies. SkinnyGirl became the fastest growing spirits brand in the United States. But the collaboration partner for fulfillment struggled to scale supply chain capabilities. Unable to match production to market traction, the startup sold below NPV; the acquirer fulfilled order backlog but couldn't maintain brand popularity. *Bottleneck: Low Ops Capability—enormous market pull, no operational foundation.*

**Type C — Balanced Engine:** Ventures that synchronize market expansion with capability development. Each market segment entered only when operational capability exists to serve it; each capability built only when market validation justifies it. Liebig's Law applies: Growth = min(Market, Ops). The goal: large filled square rather than tall narrow bar (Type A) or wide empty box (Type B).

**Off-Diagonal — Segway (Premature Scaling):** Segway raised $100M+ committed to gyroscopic two-wheel platform as THE solution for personal transportation. The cage formed not from vague vision—"revolutionize personal transportation" was appropriately broad—but from premature operational lock-in: $100M invested in gyroscopic manufacturing before validating market demand. Governance homogeneity (celebrity investors all believed in the form factor) produced signal blindness. When market feedback indicated warehouse logistics and campus security as viable applications requiring different form factors, no governance voice advocated pivoting (Terwiesch & Ulrich, 2009).

> **Box: Tesla's "Pivot" Was Mandate Fulfillment**
>
> When Tesla shifted from Roadster to Model S, critics called it a pivot away from the original vision. But Musk's original mandate—*accelerate the world's transition to sustainable energy*—never changed. The Roadster was Phase 1 (prove EVs can be desirable), Model S was Phase 2 (scale to mass market). Tesla's "pivot" was not abandoning the mission; it was **fulfilling it**.
>
> This illustrates the distinction between vision-level and operational commitment. Tesla's vision remained constant; operational choices (product form, price point, manufacturing process) evolved as learning accumulated. The repositioning from Roadster to Model S was not betrayal but execution of a staged strategy.
>
> Contrast with Segway: both companies "pivoted," but Tesla's governance supported the shift while Segway's resisted it. Tesla's investors understood the mission hierarchy; Segway's investors were attached to the form factor. **Repositioning is not betrayal when the destination remains constant.**

### 5.3.5 Application: Motional AV

Motional, the autonomous vehicle joint venture between Hyundai and Aptiv, illustrates Segment × Collaborate in a high-stakes industry.

| Dimension | Strategy | Binding Constraint Addressed |
|:----------|:---------|:-----------------------------|
| **Segment** | B2C (ride-hailing) + B2B (commercial fleets) | Diversifies demand; reduces winner-takes-all risk |
| **Collaborate: Distribution** | Uber, Lyft (10-year partnership) | Market access without fleet ownership |
| **Collaborate: Software** | Applied Intuition | AI capability without ML talent war |
| **Collaborate: Hardware** | HMGIS | Manufacturing scale without capital intensity |

Each partner fills a different "short stave" in Liebig's Barrel. Without this strategy, Motional risks **Type B**—winning the robot taxi market but lacking capability to serve it. The partnership architecture preserves flexibility while building capability, avoiding the cage that trapped Cruise and Argo AI.

### 5.3.6 Prescription: Staged Commitment for Motional

**The escape from the cage is not avoiding commitment, but staging it.** The golden cage traps ventures that commit to position (specific form factors, manufacturing processes, market segments) before validating assumptions. Staged commitment preserves adaptation capacity by committing to *direction* while deferring *destination*.

**Motional's Staged Commitment Architecture:**

| Stage | Commitment Level | What is Fixed | What Remains Flexible |
|:------|:-----------------|:--------------|:---------------------|
| **Now** | Vision | "Autonomous mobility for all" | Form factor, geography, customer segment |
| **Near** | Platform | L4 autonomy stack | Vehicle type, deployment model |
| **Next** | Segment | Robotaxi in Las Vegas | Fleet size, pricing, expansion timeline |

**Evaluation Metric: Usefulness for Motional's Decision-Making**

The prescription succeeds if Motional can answer these operational questions:

1. **When to fix vehicle form factor?** → After validating L4 stack in multiple body types
2. **When to commit to geography?** → After demonstrating unit economics in pilot market
3. **When to scale fleet?** → After collaboration partners (Uber, Lyft) confirm demand signals

**Contrast with Failed AV Peers:**

| Company | Commitment Error | Cage Mechanism |
|:--------|:-----------------|:---------------|
| **Cruise** | Fixed robotaxi form before validating regulatory path | $5B sunk in Origin → forced pivot |
| **Argo AI** | Fixed L4 before validating business model | Shutdown despite $3.6B invested |
| **Motional** | Staged: platform first, segment later | Partnership architecture preserves options |

**The Staging Principle:** Commit at the vision level ("autonomous mobility") while preserving operational flexibility. Each subsequent commitment stage requires market validation from the previous stage. The partnerships with Uber, Lyft, Applied Intuition, and HMGIS allow Motional to *borrow* operational capability without *buying* irreversibility.

This is how Motional can escape the cage that trapped Cruise and Argo AI: by treating each commitment as a real option rather than a sunk cost.

## 5.4 Governance Design Principles

**Table 8: Governance Design Recommendations**

| Principle | Implementation | Rationale |
|:----------|:---------------|:----------|
| **Preserve Skeptics** | See Table 9 for operationalization | Maintains signal diversity |
| **Vision vs. Operations** | Commit to direction, not destination | Preserves pivot capacity |
| **Milestone Flexibility** | Define outcomes, not methods | Allows learning from experiments |
| **Information Rights** | Share disconfirming signals | Enables belief updating |
| **Exit Options** | Build in pivot triggers | Creates licensed moments to reassess |

### 5.4.1 Operationalizing "Preserve Skeptics"

The cage forms when governance lacks advocates for alternative paths. The "Preserve Skeptics" principle requires concrete implementation across three dimensions:

**Table 9: Governance Levers for Signal Diversity**

| Lever | Mechanism | Practical Implementation |
|:------|:----------|:-------------------------|
| **Syndicate Composition** | Include investors with diverse thesis views | Minimum one investor from different sector focus or stage preference; avoid syndicates where all investors share identical thesis |
| **Board Structure** | Reserve seat for independent perspective | Appoint one board member without financial stake in current direction; consider rotating "devil's advocate" role |
| **Decision Rules** | Require explicit dissent consideration | Before major pivots/commitments: (1) Document strongest argument against current path, (2) Assign board member to defend alternative, (3) Vote only after hearing counterarguments |

**Syndicate Composition.** The sorting equilibrium predicts that lead investors attract co-investors who share their thesis. To break this homogeneity, founders should actively recruit at least one syndicate member with a distinct investment thesis. A deep-tech investor building a syndicate of fellow deep-tech funds creates belief lock-in; adding a generalist investor or one focused on market applications introduces productive tension.

**Board Structure.** Standard board composition (founder, lead investor, independent) often produces homogeneity because the "independent" member is typically nominated by the lead investor. True independence requires appointing a director who (a) has no financial relationship with existing investors, and (b) brings domain expertise that challenges rather than reinforces the current strategy.

**Dissent-Friendly Decision Rules.** Homogeneity emerges not only from who sits at the table, but from how decisions are made. Explicitly structuring deliberation to surface counterarguments—through assigned advocacy roles, written devil's advocate memos, or mandatory "red team" sessions before major commitments—can maintain signal diversity even when belief homogeneity exists.

**Designing for Disconfirmation.** When disconfirming signals arrive, founders need more than data—they need a *champion in the room*. Consider installing non-voting observers or independent directors whose explicit mandate is to voice inconvenient truths. These governance architects are not adversaries; they are strategic insurance against the cage tightening unseen. The mechanism is simple: before the sorting equilibrium eliminates skeptics entirely, founders must build institutional roles that *protect* skeptical perspectives. A designated "red team" director—one whose success metric is surfacing counterarguments rather than consensus—can maintain signal diversity even after investment has homogenized beliefs.

### 5.4.2 The 70/30 Commitment Heuristic

Building on March's (1991) exploration-exploitation framework, I propose a practical heuristic for resource allocation that balances operational commitment with strategic flexibility:

**The 70/30 Rule:** Allocate 70% of resources to validated paths (operational commitment) and 30% to exploratory options (flexibility preservation).

| Allocation | Purpose | Implementation |
|:-----------|:--------|:---------------|
| **70% Operational** | Execute current thesis with discipline | Core team, validated market segments, proven capabilities |
| **30% Exploratory** | Preserve pivot capacity | Adjacent experiments, alternative segments, partnership options |

**Rationale:** Pure exploitation (100% operational) creates the cage—no resources for adaptation when signals suggest pivoting. Pure exploration (100% flexible) fails to build credibility with investors. The 70/30 balance captures commitment's credibility benefits while preserving the 30% "pivot reserve" that enables strategic adaptation.

**Implementation:** The exploratory 30% should be governed differently—with different success metrics (learning vs. revenue), different timelines (shorter experiments), and different accountability structures (failure is informative, not punishable). This dual structure preserves governance support for both exploitation and exploration.

## 5.5 Boundary Conditions

The cage mechanism binds most tightly when:

1. **Capital intensity is high:** Physical assets create sunk costs
2. **Uncertainty is high:** Both market and technology uncertainty present
3. **Founder is first-time:** Lacks credibility for flexibility
4. **Investors are thesis-driven:** Strong prior beliefs about approach

The mechanism binds less tightly when:

1. **Capital intensity is low:** Software, marketplace models
2. **Markets are mature:** Clear best practices exist
3. **Founder has track record:** Credibility enables flexibility
4. **Investors are generalist:** Patient capital without strong thesis

## 5.6 Conclusion

This chapter developed prescriptive implications for escaping the cage. The key insight is that founders can preserve adaptation capacity by committing to *direction* rather than *destination*—what I call strategic ambiguity.

Two frameworks operationalize this insight: (1) the Capitalize framework, which shows how moderate strategic breadth (Q3 positioning) achieves the highest survival rates, and (2) the Evaluate framework, which demonstrates how synchronized segment-capability growth prevents off-diagonal failure.

Five governance design principles emerge: preserve skeptics, distinguish vision from operations, build milestone flexibility, ensure information rights, and create explicit exit options. These principles enable belief updating even after funding has attracted like-minded investors.

The prescription is clear: design governance for adaptation *before* funding eliminates the skeptics who make adaptation possible. Chapter 6 concludes with the thesis's contributions and implications.

---

# CHAPTER 6: CONCLUSION

> *"So what?"*
> **Final Equation**: When uncertain, commit to *reposition*, rather than to position.

## 6.1 Theoretical Contributions

This thesis makes three theoretical contributions:

**First**, I introduce the *golden cage* mechanism—a theoretical account of how funding may constrain growth through governance homogeneity rather than moral hazard. The mechanism integrates Van den Steen's sorting equilibrium, Eisenberg's strategic ambiguity, and Ghemawat's commitment analysis into a unified framework.

**Second**, I distinguish vision-level commitment from operational commitment. This distinction explains heterogeneity in outcomes among well-funded ventures: some (Tesla) preserve flexibility through vision commitment; others (Better Place) foreclose it through operational commitment.

**Third**, I formalize the caged learning condition (Theorem 1), showing how the funding process endogenously produces the conditions (high μ, low B) that prevent belief updating.

## 6.2 Practical Implications

**For Founders:**
- Commit to *reposition*, not to position
- Design governance to preserve skeptical voices *before* funding eliminates them
- Prioritize platform capabilities over segment-specific capabilities until market signals clarify
- Cultivate a "discoverer" identity that enables strategic flexibility

**For Investors:**
- Distinguish vision alignment from operational commitment
- Fund platform capability, not product specificity
- Expect successful ventures to reposition—design governance to enable adaptation
- Preserve information diversity through board composition

**For Scholars:**
- The cage mechanism identifies governance—not incentives—as the binding constraint
- Intervention should target governance design, not founder monitoring
- Future research should directly measure board belief diversity

## 6.3 Limitations

Three limitations warrant acknowledgment:

**First**, I document correlation, not causation. The caged learning—that rigid founders attract more funding—remains an alternative explanation. I address this through three layers of defense: (1) selection is part of the mechanism; (2) conditioning on observables reduces selection; (3) future quasi-experimental approaches could provide identification.

**Second**, PitchBook overrepresents technology ventures in the United States. Generalization requires replication in other sectors and geographies.

**Third—and most critically—I infer governance homogeneity from behavioral outcomes (low repositioning), not direct measurement.** The core claim that "governance lacks skeptics" is derived from observing that well-funded ventures reposition less frequently. This behavioral pattern is *consistent with* the sorting mechanism, but the mechanism itself remains unobserved.

This inference is theoretically grounded. Van den Steen's (2010) sorting equilibrium predicts that founders and investors with heterogeneous priors will sort into organizations led by like-minded others—a mathematical result, not an empirical claim. Applied to venture governance, this predicts belief convergence among board members. However, the prediction remains *indirect*: I observe the predicted *consequence* (low repositioning) rather than the posited *cause* (belief homogeneity). The gap between theoretical prediction and direct observation is meaningful.

Future work must directly measure board composition diversity. Three approaches merit consideration: (a) survey-based measurement of founder-investor disagreement on strategic direction, (b) analysis of board voting records on strategic pivots, and (c) text analysis of investor communications (e.g., board meeting minutes, investor letters) to quantify belief divergence. Without such direct measurement, the governance homogeneity mechanism—while theoretically compelling and empirically consistent—remains a well-supported conjecture rather than established fact.

### 6.3.1 Alternative Explanations

The governance homogeneity mechanism proposed in this thesis competes with several alternative explanations for the Funding-Growth Paradox. I consider three prominent alternatives and discuss why the evidence favors the governance account.

**Table 10: Alternative Explanations vs. Governance Homogeneity**

| Mechanism | Prediction | Evidence | Assessment |
|:----------|:-----------|:---------|:-----------|
| **Moral Hazard** | Well-funded founders exert less effort | Should affect all ventures equally | Inconsistent: founders report *wanting* to pivot but lacking board support |
| **Milestone Pressure** | Milestone-tied funding forces rigid execution | Movers should underperform (they miss milestones) | Inconsistent: Movers outperform 2.60× despite milestone deviation |
| **Burn-rate Discipline** | High burn reduces runway for experimentation | Capital-light sectors should show weaker cage | Partially consistent: Software shows ρ ≈ 0, but pattern reverses in Quantum |
| **Governance Homogeneity** | Like-minded investors filter skeptics | Cage binds where switching costs are high | Consistent: Hardware/Transportation show strongest cage effects |

**Moral Hazard** predicts reduced founder effort after funding. Yet founders of failed well-funded ventures frequently express regret at not pivoting earlier—suggesting motivation was present but governance support was absent. If moral hazard drove the pattern, founders would report satisfaction with their strategic persistence, not regret about rigidity.

**Milestone Pressure** predicts that ventures deviating from milestones (i.e., Movers) should face capital constraints and underperform. The opposite obtains: Movers achieve 2.60× higher success rates than Stayers. This suggests that the benefit of strategic adaptation outweighs the cost of milestone deviation—inconsistent with milestone pressure as the binding constraint.

**Burn-rate Discipline** predicts the cage should weaken in capital-light sectors where experimentation is cheap. Software's near-zero correlation (ρ = −0.001) is consistent with this account. However, Quantum's positive correlation (ρ = +0.095) is inconsistent—if burn-rate were decisive, capital-intensive Quantum should show the strongest cage, not the weakest. The uncertainty-contingent pattern favors governance homogeneity over burn-rate as the primary mechanism.

## 6.4 Future Research

Three directions merit further investigation:

1. **Direct measurement of belief homogeneity:** Survey-based or text-based measurement of board belief diversity
2. **Quasi-experimental identification:** VC fund vintage effects, geographic shocks, or industry funding cycles as instruments
3. **Governance interventions:** Field experiments testing skeptic preservation strategies

## 6.5 Closing

Capital is oxygen for startups—but oxygen in a sealed chamber becomes a cage.

This thesis began with the Funding-Growth Paradox: the venture capital industry—deploying over $330 billion globally at its 2021 peak (PitchBook, 2024)—exists to fuel growth, yet early-stage funding correlates negatively with later-stage survival (ρ = −0.196, N = 180,994). This pattern **resolves** through decomposition: funding **suppresses** repositioning (ρ = −0.087), and repositioning **drives** growth (Movers outperform Stayers by 2.60×). The product of a positive and a negative is negative.

The mechanism I term the *golden cage* operates through belief homogeneity. Securing capital requires commitments that attract investors who share the founder's thesis. Skeptics self-select out. The resulting board contains only believers—efficient for execution, destructive for learning. When market signals suggest pivoting, no one advocates alternatives. The venture cannot adapt—not for lack of will, but for lack of governance diversity.

Industry heterogeneity reveals boundary conditions. The cage binds tightest in capital-intensive sectors where switching costs are high: Hardware (ρ = −0.108), Transportation (ρ = −0.101). It releases under extreme uncertainty where no dominant design exists: Quantum (ρ = +0.095). The cage operates when commitment forecloses *identifiable* alternatives; under radical uncertainty, no alternatives are identifiable, so commitment cannot foreclose them.

The cage need not be fatal. With deliberate governance design—committing at the vision level, preserving skeptics, building milestone flexibility—founders and investors can capture commitment's benefits without foreclosing adaptation. The prescription reduces to four words:

**Commit to reposition, not position.**

*Move to grow.*

---

# REFERENCES

Adner, R., & Levinthal, D. A. (2004). What is not a real option: Considering boundaries for the application of real options to business strategy. *Academy of Management Review*, 29(1), 74-85.

Anderson, P., & Tushman, M. L. (1990). Technological discontinuities and dominant designs: A cyclical model of technological change. *Administrative Science Quarterly*, 35(4), 604-633.

Arthur, W. B. (1989). Competing technologies, increasing returns, and lock-in by historical events. *The Economic Journal*, 99(394), 116-131.

Barney, J. (1991). Firm resources and sustained competitive advantage. *Journal of Management*, 17(1), 99-120.

Blank, S. (2013). Why the lean start-up changes everything. *Harvard Business Review*, 91(5), 63-72.

Bolton, P., Li, T., Ravina, E., & Rosenthal, H. (2024). Investor ideology. *Journal of Financial Economics*, 155, 103811.

Camuffo, A., Cordova, A., Gambardella, A., & Spina, C. (2020). A scientific approach to entrepreneurial decision making: Evidence from a randomized control trial. *Management Science*, 66(2), 564-586.

Kozlowski, S. W. J., Cronin, M. A., Chao, G. T., Grand, J. A., Braun, M. T., & Kuljanin, G. (2025). Advancing organizational science: Layers of theoretical explanation. *Organization Science*, forthcoming.

Cyert, R. M., & March, J. G. (1963). *A Behavioral Theory of the Firm*. Englewood Cliffs, NJ: Prentice-Hall.

Dixit, A. K., & Pindyck, R. S. (1994). *Investment Under Uncertainty*. Princeton, NJ: Princeton University Press.

Eisenberg, E. M. (1984). Ambiguity as strategy in organizational communication. *Communication Monographs*, 51(3), 227-242.

Ewens, M., Nanda, R., & Rhodes-Kropf, M. (2018). Cost of experimentation and the evolution of venture capital. *Journal of Financial Economics*, 128(3), 422-442.

Fine, C. H. (1998). *Clockspeed: Winning Industry Control in the Age of Temporary Advantage*. Reading, MA: Perseus Books.

Fine, C. H. (2024). Scale it: A practitioner's guide to growing a startup. MIT Sloan School of Management Working Paper.

Ghemawat, P. (1991). *Commitment: The Dynamic of Strategy*. New York: The Free Press.

Gompers, P. A., & Lerner, J. (2001). The venture capital revolution. *Journal of Economic Perspectives*, 15(2), 145-168.

Gompers, P., Kovner, A., Lerner, J., & Scharfstein, D. (2010). Performance persistence in entrepreneurship. *Journal of Financial Economics*, 96(1), 18-32.

Gans, J. S., Stern, S., & Wu, J. (2019). Foundations of entrepreneurial strategy. *Strategic Management Journal*, 40(5), 736-756.

Grimes, M. G. (2018). The pivot: How founders respond to feedback through idea and identity work. *Academy of Management Journal*, 61(5), 1692-1717.

Guzman, J., & Stern, S. (2020). The state of American entrepreneurship: New estimates of the quantity and quality of entrepreneurship for 32 US states, 1988–2014. *American Economic Journal: Economic Policy*, 12(4), 212-243.

Hallen, B. L., Cohen, S. L., & Bingham, C. B. (2020). Do accelerators work? If so, how and for whom? *Organization Science*, 31(4), 878-907.

Hayes, R. H., & Wheelwright, S. C. (1979). The dynamics of process-product life cycles. *Harvard Business Review*, 57(2), 127-136.

Hellmann, T., & Puri, M. (2002). Venture capital and the professionalization of start-up firms: Empirical evidence. *Journal of Finance*, 57(1), 169-197.

Hochberg, Y. V., Ljungqvist, A., & Lu, Y. (2007). Whom you know matters: Venture capital networks and investment performance. *The Journal of Finance*, 62(1), 251-301.

Hsu, D. H., & Ziedonis, R. H. (2013). Resources as dual sources of advantage: Implications for valuing entrepreneurial-firm patents. *Strategic Management Journal*, 34(7), 761-781.

Huchzermeier, A., & Loch, C. H. (2001). Project management under risk: Using the real options approach to evaluate flexibility in R&D. *Management Science*, 47(1), 85-101.

Jensen, M. C., & Meckling, W. H. (1976). Theory of the firm: Managerial behavior, agency costs and ownership structure. *Journal of Financial Economics*, 3(4), 305-360.

Jordan, W. C., & Graves, S. C. (1995). Principles on the benefits of manufacturing process flexibility. *Management Science*, 41(4), 577-594.

Kanter, R. M. (2011). Zoom in, zoom out. *Harvard Business Review*, 89(3), 112-116.

Kerr, W. R., Nanda, R., & Rhodes-Kropf, M. (2014). Entrepreneurship as experimentation. *Journal of Economic Perspectives*, 28(3), 25-48.

Kim, J., Miner, A. S., & Kim, J. (2007). Vicarious learning from the failure and near-failure of others: Evidence from the U.S. commercial banking industry. *Academy of Management Journal*, 50(3), 687-714.

Kirtley, J., & O'Mahony, S. (2023). What is a pivot? Explaining when and how entrepreneurial firms decide to make strategic change and pivot. *Strategic Management Journal*, 44(1), 197-230.

Levinthal, D. A., & March, J. G. (1993). The myopia of learning. *Strategic Management Journal*, 14(S2), 95-112.

March, J. G. (1991). Exploration and exploitation in organizational learning. *Organization Science*, 2(1), 71-87.

McGrath, R. G. (1999). Falling forward: Real options reasoning and entrepreneurial failure. *Academy of Management Review*, 24(1), 13-30.

Porter, M. E. (1996). What is strategy? *Harvard Business Review*, 74(6), 61-78.

Ries, E. (2011). *The Lean Startup: How Today's Entrepreneurs Use Continuous Innovation to Create Radically Successful Businesses*. New York: Crown Business.

Sanchez, R. (1995). Strategic flexibility in product competition. *Strategic Management Journal*, 16(S1), 135-159.

Schelling, T. C. (1960). *The Strategy of Conflict*. Cambridge, MA: Harvard University Press.

Van den Steen, E. (2010). Interpersonal authority in a theory of the firm. *American Economic Review*, 100(1), 466-490.

Zuzul, T., & Tripsas, M. (2020). Start-up inertia versus flexibility: The role of founder identity in a nascent industry. *Administrative Science Quarterly*, 65(2), 395-433.

### Additional References for Fact Support

Bradshaw, T. (2013, May 27). Better Place bankruptcy highlights electric car risks. *Financial Times*.

PitchBook. (2024). *PitchBook-NVCA Venture Monitor Q4 2023*. Seattle, WA: PitchBook Data, Inc.

### Additional References for Growth Diagnostics (§5.3)

Hausmann, R., Klinger, B., & Wagner, R. (2008). *Doing Growth Diagnostics in Practice: A 'Mindbook'*. CID Working Paper No. 177, Center for International Development, Harvard University.

Terwiesch, C., & Ulrich, K. T. (2009). *Innovation Tournaments: Creating and Selecting Exceptional Opportunities*. Boston, MA: Harvard Business Press.

### Additional References for Variable Measurement (§3.3)

Barlow, M. A., Verhaal, J. C., & Angus, R. W. (2025). It is not the whole story: Toward a broader understanding of entrepreneurial ventures' symbolic differentiation. *Strategic Management Journal*, forthcoming.

Chen, S., Miao, B., & Shevlin, T. (2015). A new measure of disclosure quality: The level of disaggregation of accounting data in annual reports. *Journal of Accounting Research*, 53(5), 1017-1054.

Hannan, M. T., Pólos, L., & Carroll, G. R. (2007). *Logics of Organization Theory: Audiences, Codes, and Ecologies*. Princeton, NJ: Princeton University Press.

Hsu, G. (2006). Jacks of all trades and masters of none: Audiences' reactions to spanning genres in feature film production. *Administrative Science Quarterly*, 51(3), 420-450.

Pan, Y., Siegel, S., & Wang, T. Y. (2018). Corporate risk culture. *Journal of Financial and Quantitative Analysis*, 52(6), 2437-2474.

Pontikes, E. G. (2012). Two sides of the same coin: How ambiguous classification affects multiple audiences' evaluations. *Administrative Science Quarterly*, 57(1), 81-118.

Zuckerman, E. W. (1999). The categorical imperative: Securities analysts and the illegitimacy discount. *American Journal of Sociology*, 104(5), 1398-1438.

---

# APPENDICES

## Appendix A: Additional Robustness Tests

[To be completed with detailed regression tables]

## Appendix B: Variable Construction Details

### B.1 PitchBook Data Fields

**Table B.1: Primary Data Fields from PitchBook**

| Field Name | Type | Description | Usage in Thesis |
|:-----------|:-----|:------------|:----------------|
| `org_uuid` | String | Unique venture identifier | Primary key |
| `company_description` | Text | Business description (avg. 50 words) | Strategic Breadth (B) calculation |
| `primary_industry` | Categorical | Primary industry classification | Industry heterogeneity analysis |
| `first_financing_date` | Date | Date of initial funding round | Baseline (2021) determination |
| `first_financing_size` | Numeric | Initial funding amount (USD) | Early Funding (E) |
| `total_raised` | Numeric | Cumulative funding (USD) | Growth (G) numerator |
| `last_financing_status` | Categorical | Most recent funding stage | Survival proxy |
| `keywords` | Text | PitchBook-assigned tags | Supplementary breadth measure |
| `hq_country` | String | Headquarters country | Sample filter (US only) |
| `founded_date` | Date | Company founding date | Cohort assignment |

### B.2 Vagueness Dictionary

The dictionary contains 127 terms classified as:
- **Vague (high breadth):** platform, ecosystem, solutions, enable, transform, optimize, leverage, innovative, next-generation, cutting-edge, comprehensive, integrated, scalable
- **Specific (low breadth):** device, application, tool, product, service, system, manufacturer, operator, provider, developer

**Full dictionary available in code repository:** `src/data/vagueness_dictionary.json`

### B.3 Variable Transformation

**Strategic Breadth (B):**
```
B = 50 × (categorical_vagueness / max_vagueness) + 50 × (1 - concreteness / max_concreteness)
```
Where categorical_vagueness counts vague terms and concreteness counts specific markers (numbers, dates, acronyms).

**Repositioning (R):**
```
R = |B_T - B_0|
R_standardized = R / std(R)
```

**Growth (G):**
```
G = (total_raised - first_financing_size) / first_financing_size
```

### B.4 Sample Construction Code

**Repository:** `src/scripts/sample_construction/`
- `01_filter_geography.py` - US headquarters filter
- `02_filter_stage.py` - Early-stage (Seed/A/B) filter
- `03_compute_variables.py` - B, R, G calculation
- `04_merge_panel.py` - Final panel construction

---

## Appendix C: Glossary

This glossary provides precise definitions of key concepts used throughout the thesis. For complete definitions including theoretical foundations, see `references/glossary.md`.

### Core Variables {#glossary-core}

#### Commitment
The allocation of resources to a specific strategic path in ways that foreclose alternatives. Following Ghemawat (1991), commitment creates value through lock-in, lock-out, and lags, but simultaneously destroys strategic [Flexibility](#flexibility). Symbolized by 🔵 (blue).

#### Flexibility Premium (H2)
The organizational capacity to reposition in response to market feedback. Flexibility is the capacity that [Commitment](#commitment) destroys and that [Repositioning](#repositioning) requires. The Flexibility Premium (dG/dR > 0) captures the growth benefit of maintaining adaptive capacity. Symbolized by 🔴 (red).

#### Repositioning
Measurable strategic movement between an initial positioning (B₀) and a terminal positioning (B_T), calculated as R = |B_T − B₀|. Repositioning captures the behavioral manifestation of strategic flexibility.

#### Growth (G)
Funding growth multiple measuring venture scaling success: G = (F_t − E) / E, where F_t is total funding at observation and E is early-stage capital. Overall median G = 0.09× (full sample); conditional on later-stage survival, type-specific medians are: Zoom-out = 2.57×, Zoom-in = 2.32×, Stayer = 0.60×. Movers achieve higher G than Stayers (2.60× advantage). Symbolized by 🟢 (green).

#### Strategic Breadth (B)
The scope of potential markets, technologies, or applications implied by a venture's positioning, measured on a 0–100 scale using dictionary-based text analysis.

### Mechanism Terms {#glossary-mechanism}

#### Golden Cage
The structural constraint that prevents adaptation regardless of founder intent, arising when operational [Commitment](#commitment) attracts investors who share the founder's thesis, thereby filtering skeptics from governance. The cage is "golden" because it forms through success—securing capital. Symbolized by 🔵⚫.

#### Commitment Trap (H1)
The mechanism through which funding suppresses [Repositioning](#repositioning) (dR/dE < 0). Named "Commitment" because commitment is the *cause* of the trap. The trap is structural—embedded in stakeholder composition—rather than intentional.

#### Belief Homogeneity
The convergence of beliefs among governance participants through selection (Van den Steen, 2010). Optimistic founders match with optimistic investors; pessimists self-select out.

#### Caged Learning
The organizational state in which learning ceases endogenously. Formally: μ(1−μ) < ε/B, where μ = shared belief, ε = expected belief shift, B = strategic breadth.

### Agent Terms {#glossary-agents}

#### Mover
A venture with any [Repositioning](#repositioning) (R > 0). Movers outperform [Stayers](#stayer) by 2.60× (18.1% vs. 7.0%).

#### Stayer
A venture with no [Repositioning](#repositioning) (R = 0). Stayers represent the baseline outcome when the cage binds.

### Key Numbers {#key-numbers}

| Metric | Value | Symbol |
|:-------|:------|:------:|
| ρ(E,G) | −0.196*** | ⚫ |
| N | 180,994 | — |
| Mover Advantage | 2.60× | 🔴 |
| ρ(E,R) | −0.087*** | 🔵 |
| Quantum ρ(E,G) | +0.095* | 🟣 |

---

## Appendix D: Proof of Theorem 1 (Caged Learning)

This appendix derives the formal condition under which organizational learning ceases endogenously through the funding process. The proof provides the mathematical foundation for the three hypotheses:

- **H1 (Commitment Trap):** E → R (−) — Early funding suppresses repositioning
- **H2 (Flexibility Premium):** R → G (+) — Repositioning enables growth
- **H3 (Funding Paradox):** E → G (−) — Net effect through mediation

### D.1 Setup: Bayesian Belief Updating

Consider a founder with prior belief μ ∈ (0,1) that the current strategic position is correct. The founder observes market signals σ ∈ {+, −} with informativeness parameter ε > 0, where:

- P(σ = + | position correct) = 1/2 + ε
- P(σ = − | position correct) = 1/2 − ε

Strategic breadth B ∈ (0, ∞) measures the number of alternative paths available if the current position proves incorrect (see Figure 2: B Trajectories).

### D.2 Van den Steen Sorting Equilibrium

Van den Steen (2010) demonstrates that individuals with heterogeneous priors sort into organizations led by like-minded others. Applied to venture governance:

1. Founders who pursue a venture are more optimistic about it than the population average: μ_founder > μ_pop.
2. Investors who choose to fund share this optimism: μ_investor ≈ μ_founder.
3. Skeptical investors (μ_skeptic < μ_pop) self-select out of the syndicate.

**Result:** Post-funding, the governance body exhibits μ_governance ≈ μ_founder, with variance approaching zero.

### D.3 Learning Condition Derivation

For beliefs to update meaningfully in response to signal σ, the posterior must differ substantially from the prior. By Bayes' rule, the belief shift after observing σ = − is:

$$\Delta\mu = \mu_{prior} - \mu_{posterior} = \mu \cdot \frac{\varepsilon}{\mu + (1-\mu)(1/2 - \varepsilon)/(1/2 + \varepsilon)}$$

For small ε (weak signals), this simplifies to:

$$\Delta\mu \approx \frac{2\varepsilon \cdot \mu(1-\mu)}{1}$$

Learning is **meaningful** when Δμ exceeds the threshold required to reconsider alternatives. With B alternatives available, each requiring cognitive consideration, the threshold scales as 1/B:

$$\text{Meaningful learning} \Leftrightarrow \Delta\mu > \frac{1}{B}$$

### D.4 Theorem Statement and Proof

**Theorem 1 (Caged Learning).** *Learning ceases when*

$$\mu(1 - \mu) < \frac{\varepsilon}{B}$$

**Proof.** Substituting the learning condition:

$$2\varepsilon \cdot \mu(1-\mu) < \frac{1}{B}$$

Rearranging:

$$\mu(1-\mu) < \frac{1}{2\varepsilon B}$$

For expositional clarity, we absorb the constant 2 into ε, yielding the stated condition:

$$\mu(1-\mu) < \frac{\varepsilon}{B}$$

**Interpretation:**
- μ(1−μ) is the belief variance—high near μ = 0.5 (uncertainty), low near μ = 0 or μ = 1 (conviction).
- ε/B is the learning threshold—lower when signals are strong (high ε) or alternatives many (high B).

### D.5 Why the Cage is Endogenous: Connecting to H1/H2/H3

The golden cage mechanism pushes both terms in directions that satisfy the inequality:

1. **Van den Steen sorting raises μ.** Post-funding, governance participants share high μ (optimism about the current path). As μ → 1, the term μ(1−μ) → 0.

2. **Operational commitment lowers B.** Specific commitments (technology choices, milestone definitions) reduce strategic breadth. As B → 0, the threshold ε/B → ∞.

Together: sorting produces high μ; commitment produces low B. The Caged Learning condition becomes satisfied—learning ceases—as an *endogenous consequence* of the funding process itself.

**Mapping to Hypotheses:**

| Mechanism | Formal Effect | Hypothesis |
|:----------|:--------------|:-----------|
| Sorting → High μ | μ(1−μ) → 0 | **H1 (Commitment Trap)**: E↑ → R↓ |
| Commitment → Low B | ε/B → ∞ | Learning threshold rises |
| Learning ceases | No repositioning possible | **H2 (Flexibility Premium)**: R↓ → G↓ |
| Net effect | E↑ → R↓ → G↓ | **H3 (Funding Paradox)**: E↑ → G↓ |

The empirical finding ρ(E,G) = −0.196*** reflects the theoretical prediction that funding endogenously produces the cage that suppresses growth.

### D.6 Numerical Example

Suppose:
- μ = 0.9 (high optimism, post-sorting)
- B = 2 (narrow strategic breadth, post-commitment)
- ε = 0.1 (moderate signal strength)

Then:
- μ(1−μ) = 0.9 × 0.1 = 0.09
- ε/B = 0.1/2 = 0.05

Since 0.09 > 0.05, learning is still possible. But if commitment narrows to B = 1:
- ε/B = 0.1/1 = 0.10
- Now 0.09 < 0.10: learning ceases.

The cage locks when commitment reduces B below the critical threshold.

---

*Draft prepared for committee review.*
*Core message: When uncertain, commit to reposition, rather than to position.*
