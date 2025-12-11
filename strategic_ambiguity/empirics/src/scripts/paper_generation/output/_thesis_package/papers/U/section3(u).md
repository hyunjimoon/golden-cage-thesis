# Paper U: When Vagueness Pays
## Section 3: Empirics (¶25-32)

### ¶25. Data and Sample Construction

We analyze technology ventures using PitchBook data covering 2021 to 2025. Our sample includes ventures that received early-stage funding (seed or Series A) and for which we can observe positioning descriptions and subsequent funding outcomes. The final sample comprises 180,860 ventures with complete data on initial vagueness scores and later success indicators. This sample represents technology ventures across multiple sectors, providing broad coverage of the startup ecosystem during a period of significant market volatility including the post-COVID recovery and the emergence of generative AI.

### ¶26. Dependent Variable: Long-term Success

Our primary outcome variable, L, captures whether a venture achieves later-stage funding success. We define L = 1 if the venture's last financing deal type equals "Later Stage VC," indicating progression beyond early-stage funding to more substantial institutional investment. The base rate in our sample is L = 11.5%, reflecting that most early-stage ventures do not progress to later stages. This binary measure provides a clear threshold for success while avoiding the complications of continuous funding amounts that vary substantially by sector and time period.

### ¶27. Independent Variable: Initial Vagueness

Our primary explanatory variable, V, measures the vagueness of a venture's initial market positioning using HybridVaguenessScorerV2. The score ranges from 0 (maximally precise) to 100 (maximally vague) and combines two components with equal weight: categorical term density, measuring the presence of vague categorical terms such as "platform," "solutions," and "innovative"; and concreteness deficit, measuring 1 minus average word concreteness based on Brysbaert psycholinguistic norms. This measure captures positioning breadth rather than communication quality, distinguishing it from readability metrics. The correlation between our vagueness score and Flesch-Kincaid readability is r = 0.08, indicating that vagueness and writing quality are largely orthogonal.

### ¶28. Key Variable: Adaptive Capacity

We introduce adaptive capacity, A = |D| = |V_T − V_0|, as our measure of strategic movement. D captures directional change (signed), while A captures absolute change regardless of direction. We classify ventures as "stayed" (A = 0) if their positioning remained fixed, and "moved" (A > 0) if they repositioned over time. In our sample, 60% of ventures show A = 0 (stayed) while 40% repositioned (moved). This measure captures revealed adaptation rather than underlying capacity, as we observe positioning changes but not the ability to change.

### ¶29. Identification Strategy and Temporal Robustness

Our primary identification strategy relies on Spearman rank correlation to test monotonicity, avoiding parametric assumptions about functional form. For the Movement Principle, we compare success rates between movers and stayers using chi-squared tests. We acknowledge that our design is correlational: we document associations between vagueness, movement, and success but cannot establish causation. However, we strengthen causal inference through temporal stability analysis—a quasi-natural experiment exploiting variation across distinct market regimes. If our relationships were driven by omitted variables or spurious correlations, we would expect coefficient instability across the post-COVID recovery (2023), the AI boom (2024), and continued market evolution (2025). Instead, we observe remarkable stability: the capital-flexibility friction (ρ(A,E)) remains negative and significant across all three years (−0.007** in 2023, −0.006* in 2024, −0.009*** in 2025), the flexibility-growth relationship (ρ(G,A)) remains positive and significant (+0.033*** to +0.044***), and the capital paradox (ρ(G,E)) remains strongly negative (−0.225*** to −0.211***). This temporal stability across heterogeneous market conditions provides evidence against the omitted variable and selection explanations that would produce unstable coefficients.

### ¶30. Results: Rejecting Monotonicity

The Spearman rank correlation between initial vagueness (V) and later success (L) is ρ = +0.024 (p < 0.001). This positive correlation directly rejects signaling theory's prediction of monotonic decrease: under H₀, we expected ρ < 0. Success rates by quartile show Q1 (precise) at 12.3%, Q2 at 8.9%, Q3 at 16.0%, and Q4 (vague) at 12.9%. The pattern is non-monotonic rather than U-shaped: Q3 exceeds both Q1 and Q4, contrary to what either pure signaling or pure strategic ambiguity arguments would predict. We therefore reject H₀ in favor of H₁: the relationship between vagueness and success is non-monotonic.

### ¶31. Results: The Movement Principle

Our most striking finding concerns the role of adaptation. Companies that repositioned (A > 0) succeed at 18.1%, compared to 7.0% for those that stayed fixed—a 2.6× advantage (χ² = 4,891.3, p < 0.001). This movement effect dominates any positioning effect. Decomposing by quartile and movement status reveals that Q3's high aggregate success (16.0%) is entirely explained by its high movement rate (68%). Among stayers only, Q3 has the lowest success (6.6%), while Q2 has the highest (7.5%). Among movers, Q3 shows the highest success (20.4%). The aggregate pattern masks fundamentally different dynamics for movers versus stayers.

### ¶32. Results: Direction Irrelevance

Among movers (A > 0), direction matters little. Those who focused (D < 0, moving toward more precision) succeed at 17.6%, while those who broadened (D > 0, moving toward more vagueness) succeed at 18.6%. The chi-squared test yields χ² = 12.4 (p = 0.0004), indicating statistical significance, but the economic magnitude is trivial: a 1.0 percentage point difference versus the 11.1 percentage point difference between movers and stayers. The movement advantage (2.6×) is approximately 25 times larger than the direction effect. This supports the Movement Principle: what matters is whether ventures adapt, not in which direction they move.
