# Dissertation Abstracts (Production-Ready)
## Aligned with LTE Framework (Cronin et al., 2025)

**Author**: Hyunji Moon  
**Program**: MIT Sloan PhD, Operations Management & Entrepreneurship  
**Advisors**: Charlie Fine (Operations), Scott Stern (Strategy)  
**Date**: December 2025

---

## Dissertation Abstract (The Overarching Strategy)

**Title**: Strategic Ambiguity in Entrepreneurship: Linking Promise Vagueness, Adaptive Capacity, and Investor Sorting through the Layers of Theoretical Explanation

### Abstract

New ventures face a fundamental tension between the need for specific commitments to secure resources and the need for flexibility to navigate uncertainty. This dissertation investigates this tension by adopting the Layers of Theoretical Explanation (LTE) typology to integrate descriptive construct evidence with generative process mechanisms.

**Paper M (Descriptive Construct Theorizing)** documents an empirical anomaly ("The What"): analyzing 180,860 technology ventures (2021–2025), we find that the relationship between initial promise vagueness (V₀) and long-term success (L) is **non-monotonic**, rejecting signaling theory's monotonic prediction (Spearman ρ = +0.024***). Success rates vary across vagueness quartiles (Q1=12.3%, Q2=8.9%, Q3=16.0%, Q4=12.9%) in a pattern driven by **movement**: ventures that repositioned (A > 0) succeed 2.6× more than those that stayed fixed (18.1% vs 7.0%). The Q3 anomaly (highest success) is explained entirely by Q3's highest movement rate (68%); among non-movers, Q3 shows the *lowest* success (6.6%).

**Paper C (Causal Identification)** traces the temporal process ("The How"): early capital (E) is associated with reduced adaptive capacity (ρ(A,E) = −0.009***), while adaptation significantly predicts growth (ρ(G,A) = +0.044***). The mediation pathway—dG/dE = (dG/dA) × (dA/dE) = (+) × (−) < 0—contributes to the negative capital-growth correlation (ρ(G,E) = −0.211***). We interpret this as suggestive evidence of a capital-flexibility friction, noting the small effect size of E→A.

**Paper T (Explanatory Process Theorizing)** provides generative sufficiency ("The Why") through agent-based simulation. We formalize the Analyst/Believer matching mechanism: specific promises (V→0) attract Analyst-type investors who impose high learning resistance and pivot costs, while vague promises (V→1) attract Believer-type investors who enable adaptation. The simulation reproduces the empirical patterns—non-monotonic V-L relationship, movement-driven success, and mediated capital effects—from this single mechanism, establishing generative sufficiency.

Collectively, this multi-method approach advances organizational science by bridging the gap between population-level construct relationships and the unit-level generative mechanisms that drive them. The practical implication: **vagueness buys options; success requires using them**.

---

## Paper M Abstract (Layer 1: Descriptive Construct Theorizing)

**Title**: When Vagueness Pays: Non-Monotonic Promise Precision and the Movement Principle

**Label**: Descriptive Construct Theorizing (The Variance)

### Abstract

Does a clear, specific value proposition always predict venture success? While conventional signaling theory suggests specificity facilitates resource acquisition by reducing information asymmetry, this paper documents a striking empirical anomaly that rejects this monotonic prediction.

Using a longitudinal dataset of **180,860 technology ventures** (2021–2025), we analyze the relationship between initial promise vagueness (V₀) and long-term success (L = Later Stage VC achieved). We find:

1. **Non-monotonic pattern**: Spearman ρ(V,L) = +0.024*** rejects monotonic decrease. Success varies across quartiles: Q1 (Precise) = 12.3%, Q2 = 8.9%, Q3 = 16.0%, Q4 (Vague) = 12.9%.

2. **Movement Principle**: The dominant finding is not about initial positioning but **adaptation**. Ventures that repositioned (A = |V_T − V₀| > 0) achieve 18.1% success versus 7.0% for those that stayed fixed—a **2.6× advantage**. Direction matters less than movement: Focusing (17.6%) ≈ Broadening (18.6%).

3. **Q3 Anomaly Explained**: Q3's highest success (16.0%) comes from Q3's highest movement rate (68%). Among stayers only, Q3 shows the *lowest* success (6.6%), confirming that movement—not initial vagueness—drives outcomes.

This descriptive construct theory establishes the "What" of the phenomenon: while initial positioning correlates with success non-monotonically, the deeper pattern is that **vagueness buys options; success requires using them**. These findings challenge linear strategic models and motivate process-level investigation into *how* capital affects the ability to exercise strategic options (Paper C) and *why* investor matching creates these patterns (Paper T).

**Keywords**: Strategic Ambiguity, Non-Monotonic Pattern, Movement Principle, Signaling Theory Boundary Conditions

---

## Paper C Abstract (Layer 2: Causal Identification)

**Title**: The Capital-Flexibility Tradeoff: How Early Funding Constrains Adaptive Capacity

**Label**: Causal Identification (The Process Sequence)

### Abstract

Startups are often advised to raise capital to "fuel" growth, but does capital also constrain the flexibility to adapt? Moving beyond the descriptive patterns documented in Paper M, this paper focuses on **tracing the temporal process** linking early capital (E), adaptive capacity (A), and growth (G).

Addressing the mediation structure through correlational analysis of the same **180,860 ventures**, we examine three relationships:

1. **H1: Capital → Adaptation (−)**: ρ(A,E) = −0.009*** confirms a statistically significant capital-flexibility friction. However, the effect size is small (R² < 0.01%), suggesting capital is not a deterministic "cage."

2. **H2: Adaptation → Growth (+)**: ρ(G,A) = +0.044*** confirms that adaptive capacity predicts growth, consistent with Paper M's Movement Principle.

3. **H3: Capital → Growth (−)**: ρ(G,E) = −0.211*** reveals a negative capital-growth correlation—the "Capital Paradox."

The mediation pathway—**dG/dE = (dG/dA) × (dA/dE) = (+) × (−) < 0**—provides one explanation: capital may create commitment costs (sunk resources, stakeholder expectations) that raise the psychological and material cost of strategic change.

**Important caveats**: We cannot distinguish commitment costs from selection effects (well-funded ventures may have less *need* to pivot). The E→A effect, while significant, explains minimal variance. The strong G-E correlation likely reflects multiple mechanisms beyond flexibility alone.

This paper contributes to Layer 2 of the LTE framework by tracing *how* the capital-flexibility-growth process unfolds temporally, setting the stage for Paper T's formal mechanism specification.

**Keywords**: Capital-Flexibility Tradeoff, Mediation Analysis, Commitment Costs, Adaptive Capacity

---

## Paper T Abstract (Layer 3: Explanatory Process Theorizing)

**Title**: The Learning Trap: Generative Sufficiency through Investor-Type Matching

**Label**: Explanatory Process Theorizing (The Generative Mechanism)

### Abstract

Why do specific promises constrain adaptation while vague promises enable growth? Paper M documented *what* patterns exist (non-monotonic V-L, Movement Principle), and Paper C traced *how* capital relates to adaptation temporally. This paper completes the LTE framework by demonstrating *why* through **generative sufficiency**: we formalize the Analyst/Believer matching mechanism and show that a computational simulation based on this mechanism reproduces the precise empirical patterns.

**The Core Mechanism—Investor-Type Matching**:

- **Matching Function**: P(Analyst | V) = 1 − V; P(Believer | V) = V

- **Analyst Characteristics** (attracted to V → 0): High learning resistance (0.9), low variance tolerance (0.1), high pivot cost (2.0). They expect commitment to stated strategy and resist strategic evolution.

- **Believer Characteristics** (attracted to V → 1): Low learning resistance (0.1), high variance tolerance (0.9), low pivot cost (0.5). They invest in founder vision and embrace adaptation.

**Simulation Design**: N = 2,000 ventures, T = 100 periods. Each venture is matched to investor type via the matching function. Growth accumulates based on adaptability net of change costs imposed by investor type.

**Generative Sufficiency Established**: The simulation reproduces:
1. Non-monotonic V-G relationship (G(V=1) > G(V=0))
2. Bimodal growth distribution (Mover/Stayer decomposition)
3. Mediation structure (investor type mediates V → A → G)

The **Learning Trap**: Specific promises attract Analysts who lock ventures into their initial strategy, suppressing the learning and adaptation that Paper M showed drives success. The trap is not capital per se, but the *type* of stakeholder that promise specificity attracts.

**Contribution**: We complete the LTE triad—WHAT (Paper M), HOW (Paper C), WHY (Paper T)—providing the "precise specification of who does what, when, and how" (Cronin et al., 2025) that enables targeted entrepreneurial guidance: choose your investor audience deliberately, because it determines your adaptive capacity.

**Keywords**: Generative Sufficiency, Agent-Based Simulation, Analyst/Believer Matching, Learning Trap, LTE Layer 3

---

## Summary Table: LTE Integration

| Layer | Paper | Question | Method | Key Finding |
|:-----:|:------|:---------|:-------|:------------|
| **1** | M | WHAT patterns exist? | Spearman ρ, Quartile decomposition | Non-monotonic; Movement Principle (2.6×) |
| **2** | C | HOW do processes unfold? | Correlational mediation | E→A(−), A→G(+), dG/dE < 0 |
| **3** | T | WHY do mechanisms generate? | Agent-based simulation | Analyst/Believer matching → Learning Trap |

---

## Key Statistics Reference

| Metric | Value | Paper |
|:-------|:------|:------|
| N | 180,860 | All |
| L base rate | 11.5% | M |
| Spearman ρ(V,L) | +0.024*** | M |
| Q1 (Precise) | 12.3% | M |
| Q2 (Low-Mid) | 8.9% | M |
| Q3 (High-Mid) | 16.0% | M |
| Q4 (Vague) | 12.9% | M |
| Stayed (A=0) | 7.0% | M |
| Moved (A>0) | 18.1% | M |
| Move ratio | **2.6×** | M |
| ρ(A,E) | −0.009*** | C |
| ρ(G,A) | +0.044*** | C |
| ρ(G,E) | −0.211*** | C |

---

## The Three Principles (For Discussion Chapter)

1. **Movement Principle**: Vagueness buys options—USE THEM (2.6× advantage)
2. **Capital-Flexibility Friction**: Money may buy commitment, not flexibility (small but significant)
3. **Investor Matching**: Choose your audience—Analysts lock, Believers enable

---

*必死卽生, 必生卽死*  
*"반드시 죽고자 하면 살고, 반드시 살고자 하면 죽는다."*

---

**Version**: 2.0 (LTE-Aligned)  
**Last Updated**: 2025-12-11  
**Status**: Production-Ready for Advisor Review
