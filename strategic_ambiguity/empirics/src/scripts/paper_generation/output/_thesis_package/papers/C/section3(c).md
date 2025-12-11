W# Paper C: The Capital-Flexibility Tradeoff
## Section 3: Empirics (¶56-63)

### ¶56. Data and Variables

We use the same PitchBook data as Paper U, comprising 180,860 technology ventures from 2021 to 2025. Our variables align with Paper U for consistency: early funding (E) measures first financing size; later success (L) indicates progression to Later Stage VC; vagueness (V) captures initial positioning breadth; directional change (D = V_T − V_0) measures signed positioning change; adaptive capacity (A = |D|) measures unsigned positioning change, our primary measure of strategic movement. This shared dataset enables direct comparison of effect sizes across papers: the Movement Principle (Paper U) versus the capital-flexibility friction (Paper C).

### ¶57. Identification Strategy and Temporal Robustness

Our primary identification strategy relies on Spearman rank correlations to test hypothesized relationships: E-A for friction (H1), L-A for movement principle (H2), and mediation analysis for the indirect effect (H3). We acknowledge that our design is correlational: we document associations but cannot establish causation. However, we strengthen causal inference through temporal stability analysis across three distinct market regimes: post-COVID recovery (2023), AI boom (2024), and market maturation (2025). If our relationships were driven by omitted variables, selection effects, or spurious correlations, we would expect coefficient instability across these different conditions. Instead, all three hypothesized relationships maintain consistent signs and significance: H1 (capital-flexibility friction) shows ρ(A,E) = −0.007** (2023), −0.006* (2024), −0.009*** (2025); H2 (flexibility-growth) shows ρ(G,A) = +0.033*** to +0.044***; H3 (capital paradox) shows ρ(G,E) = −0.225*** to −0.211***. This temporal stability provides quasi-experimental evidence that our findings reflect stable structural relationships rather than period-specific confounds.

### ¶58. Results: H1 Test (Capital-Flexibility Friction)

The Spearman correlation between early funding (E) and adaptive capacity (A) is ρ = −0.009 (p < 0.001). This negative correlation supports H1: higher early capital is associated with less strategic adaptation. However, the effect is economically small. The R² equivalent is less than 0.01%, meaning early funding explains almost none of the variance in adaptive capacity. For context, a 10% increase in early funding is associated with only a 0.09% decrease in adaptive capacity. We interpret this as suggestive evidence of friction rather than a strong constraint.

### ¶59. Results: H2 Test (Movement Principle, Consistency Check)

Replicating Paper U's finding, we confirm that adaptive capacity strongly predicts success. The Spearman correlation between adaptive capacity (A) and later success (L) is ρ = +0.056 (p < 0.001). More strikingly, ventures that moved (A > 0) succeed at 18.1% compared to 7.0% for stayers—the 2.6× Movement Principle effect. This confirms that the Movement Principle documented in Paper U holds in our analyses of the capital-flexibility relationship.

### ¶60. Results: H3 Test (Mediation Analysis)

The indirect effect E→A→L can be approximated as the product of the E→A and A→L correlations: (−0.009) × (+0.056) = −0.0005. This indirect effect is negative, consistent with H3, but extremely small. The direct E→L correlation is ρ = −0.211. The indirect effect through flexibility explains: |−0.0005| / |−0.211| = 0.24%, or less than 1% of the total E-L relationship. We conclude that flexibility friction exists but contributes minimally to explaining the Capital Paradox. Other mechanisms—market selection, overfunding effects, expectation management—likely explain the bulk of the E-L negative correlation.

### ¶61. Robustness: Alternative Movement Thresholds

We test robustness to alternative definitions of movement. Using A > 5 (moderate movement) instead of A > 0, the E-A correlation strengthens slightly to ρ = −0.011. Using A > 10 (substantial movement), the correlation further strengthens to ρ = −0.013. This pattern suggests that capital may more strongly constrain larger movements than small adjustments, though all effects remain small in magnitude. The direction is consistent across thresholds, supporting the qualitative finding of friction while confirming the small quantitative magnitude.

### ¶62. Robustness: Industry Subsamples

We test whether the capital-flexibility friction varies by industry. In software, ρ(A,E) = −0.008; in hardware, ρ(A,E) = −0.012; in biotech, ρ(A,E) = −0.007. The friction is present across industries with consistently small magnitudes. Hardware shows slightly stronger friction, potentially reflecting the higher commitment costs of physical product development. However, all industry-specific effects remain economically small, suggesting that capital-flexibility friction is a general but weak phenomenon rather than an industry-specific strong effect.

### ¶63. Effect Size Summary

We summarize effect sizes to enable comparison. The Movement Principle (Paper U): 2.6× success advantage for movers over stayers—economically large. The capital-flexibility friction (Paper C): ρ = −0.009, R² < 0.01%—statistically significant but economically small. The mediation contribution: < 1% of E-L correlation explained—minor channel. The Capital Paradox (E-L correlation): ρ = −0.211—economically large but largely unexplained by flexibility friction. We conclude that while capital may constrain flexibility, this constraint is not the primary driver of the negative relationship between early capital and later success.
