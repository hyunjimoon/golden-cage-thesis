# The Funding Paradox in Mobility Ventures
## Capital Lock-in and Strategic Repositioning in Nascent Technology Markets

**Author**: Hyunji (Angie) Moon
**Affiliation**: MIT Sloan School of Management
**Date**: January 2025
**Draft Version**: 1.0

---

## Abstract

Why do well-funded mobility ventures struggle to grow? This paper identifies a **Funding Paradox**: capital that enables experimentation simultaneously forecloses it. Using data from 890 ventures across nascent technology sectors, I show that (1) strategic repositioning predicts growth—movers outperform stayers 1.82× in survival rates—but (2) early-stage funding suppresses repositioning. Mobility ventures face this paradox acutely: manufacturing scale, data accumulation, and safety redundancy all require capital, yet capital creates stakeholder lock-in that prevents the flexibility these uncertain markets demand. I propose the PAE Framework (Platformize → Acculturate → Evaluate) as a process-commitment mechanism that preserves repositioning capacity without sacrificing stakeholder coordination.

**Keywords**: Entrepreneurial strategy, strategic ambiguity, autonomous vehicles, venture financing, organizational flexibility

---

## I. Introduction: The Funding Paradox

### ¶1. The Puzzle

Entrepreneurial finance prescribes that staged capital enables experimentation (Kerr, Nanda, & Rhodes-Kropf, 2014). When market outcomes are unknowable—following Knightian uncertainty rather than calculable risk—investors should fund portfolios of experiments, expecting most to fail while few succeed spectacularly. This logic has driven unprecedented capital flows into nascent technology sectors: autonomous vehicles alone attracted over $100 billion in the decade ending 2024.

Yet a puzzle emerges: many of the best-funded ventures have struggled most. Capital-rich autonomous vehicle ventures have delayed commercialization timelines repeatedly, while leaner competitors have pivoted to viable niches. The pattern suggests that funding may not merely enable experimentation but may also constrain it.

### ¶2. The Core Claim

I argue that capital creates a paradox: **obtaining funding requires commitments that foreclose the very experiments funding was meant to enable**. This occurs through three mechanisms:

1. **Selection**: Funding selects for founders with specific, committed visions. The pitch that wins capital becomes difficult to revise.

2. **Allocation**: Capital gets allocated to the funded strategy, creating organizational momentum toward the stated direction.

3. **Constituency**: Each funding round creates stakeholders whose interests become tied to the funded position.

The result is a predictable trap: ventures that succeed in raising capital find themselves locked into positions they may need to abandon.

### ¶3. The Equation

I formalize this as a decomposition:

$$\frac{dG}{dF} = \underbrace{\frac{dG}{dA}}_{\text{Movement Principle}} \times \underbrace{\frac{dA}{dF}}_{\text{Funding Anchor}}$$

Where:
- **G** = Growth (total funding / early-stage VC)
- **F** = Early-stage funding (log $)
- **A** = Absolute repositioning (|B_T − B₀|)
- **B** = Breadth of strategic positioning (0-100 scale)

The first term is positive: repositioning predicts growth. The second term is negative: funding suppresses repositioning. Their product yields the Funding Paradox: **dG/dF < 0** in nascent markets where flexibility matters most.

### ¶4. Contribution

This paper makes three contributions. First, I provide empirical evidence for the Movement Principle—that strategic repositioning, regardless of direction, predicts venture growth (Section A). Second, I identify boundary conditions: the paradox is most severe in mobility ventures, where structural characteristics amplify both the need for capital and its constraining effects (Section B). Third, I propose the PAE Framework as a practical intervention, shifting commitment from positions to processes (Section C).

---

## A. Analysis: The Movement Principle

### ¶5. Empirical Foundation

Using Crunchbase data on 890 ventures across nascent technology sectors (2010-2023), I measure strategic repositioning as the absolute change in positioning breadth between founding and observation: A = |B_T − B₀|. Breadth captures how specifically a venture defines its market scope, ranging from narrow ("L4 robotaxi for urban ridesharing") to broad ("mobility solutions").

### ¶6. Finding 1: Movers Outperform Stayers

Ventures that reposition—whether narrowing (zoom-in) or broadening (zoom-out)—significantly outperform those that maintain their initial positioning:

| Pattern | Survival Rate | Relative Performance |
|:--------|:--------------|:---------------------|
| Stayers (A ≈ 0) | 9.9% | Baseline |
| Zoom-in (R < 0) | 17.5% | 1.77× |
| Zoom-out (R > 0) | 18.4% | 1.86× |
| **All Movers** | **18.0%** | **1.82×** |

The direction of repositioning matters less than the fact of movement itself. This suggests that initial positioning in nascent markets is unlikely to be optimal, and ventures that update their strategies based on market learning outperform those that persist.

### ¶7. Finding 2: Funding Suppresses Movement

A one standard deviation increase in early-stage funding predicts a 0.4 SD decrease in subsequent repositioning (p < 0.01). This relationship holds controlling for sector, founding year, and initial positioning breadth.

The mechanism operates through stakeholder lock-in. Higher funding creates:
- More investors with thesis-specific expectations
- Larger teams hired for the stated strategy
- Public commitments that are costly to reverse

### ¶8. The Trap Configuration

Combining these findings, ventures fall into predictable configurations:

| Configuration | Funding | Repositioning | Growth Trajectory |
|:--------------|:--------|:--------------|:------------------|
| **Agile** | Low F | High A | Favorable |
| **Trapped** | High F | Low A | Unfavorable |
| **Lucky** | High F | High A | Favorable (rare) |
| **Struggling** | Low F | Low A | Unfavorable |

The "Trapped" configuration—high funding, low repositioning—is particularly concerning because it combines resource abundance with strategic rigidity. These ventures have the means to pivot but not the organizational capacity to do so.

---

## B. Boundary: Why Mobility Ventures Are Structurally Trapped

### ¶9. Mobility's Unique Characteristics

The Funding Paradox operates across nascent technology sectors, but mobility ventures face it with particular severity. Four structural characteristics amplify both the need for capital and its constraining effects:

**Manufacturing Integration**: Unlike software ventures, mobility requires physical production—vehicles, sensors, infrastructure. Manufacturing scale demands capital commitments that create sunk costs and supplier dependencies.

**Data Accumulation**: Autonomous systems require massive data for training and validation. Edge cases—unusual road conditions, unexpected pedestrian behavior—occur rarely, requiring fleet-scale deployment to encounter them. Learning requires scale; scale requires capital.

**Safety Redundancy**: Regulatory and ethical requirements demand redundant systems. Unlike "move fast and break things" software culture, mobility ventures cannot iterate through failure—each incident carries reputational and legal consequences. Redundancy is expensive.

**Geographic Lock-in**: Regulatory approval is jurisdiction-specific. A system validated for Las Vegas may require re-certification for Los Angeles. This fragments markets and creates switching costs.

### ¶10. Mobility Sector Statistics

These structural factors produce distinctive sector patterns:

| Metric | Mobility Sector | All Nascent Tech |
|:-------|:----------------|:-----------------|
| Average B₀ (initial breadth) | 78 | 52 |
| Stayer ratio | 91% | 67% |
| Survival to Later Stage | 5% | 14% |
| Average early funding | $47M | $12M |

Mobility ventures start with vague positioning (high B₀), remain stuck (91% stayers), and rarely survive (5%). The combination of high capital requirements and high stayer ratios suggests structural lock-in rather than strategic choice.

### ¶11. The Doubly-Bound Condition

Mobility ventures face a doubly-bound condition:

1. **They need capital** to achieve manufacturing scale, data accumulation, and safety validation
2. **Capital prevents flexibility** through stakeholder lock-in
3. **They need flexibility** because market timing, technology trajectories, and regulatory frameworks remain uncertain
4. **Flexibility prevents capital** because investors require specific theses

This creates a structural trap where the very actions required for survival (raising capital) undermine the capabilities required for survival (strategic flexibility).

### ¶12. Industry Evidence

Recent industry patterns validate this analysis. The World Economic Forum (2025) reports that autonomous vehicle commercialization timelines have been repeatedly delayed, with "predictions tending to be overly optimistic." McKinsey (2024) finds that 96% of mobility executives view partnerships as "crucial or very important"—yet partnerships create the stakeholder dependencies that amplify lock-in.

The ventures that have shown resilience share a common pattern: they repositioned despite capital constraints. Those that pivoted from robotaxi to trucking, or from full autonomy to driver assistance, have outperformed those that maintained their original positioning.

---

## C. Contribution: The PAE Framework

### ¶13. From Position to Process Commitment

Van den Steen (2017) argues that strategy creates value because commitment is costly—irreversibility signals credibility. The Funding Paradox suggests a scope condition: in nascent markets, commitment to fixed positions predicts lower growth.

I propose an alternative: **commit to processes rather than positions**. Rather than promising "we will build X," ventures can commit to "we will evaluate X using these criteria and these decision rules." This preserves the credibility benefits of commitment while maintaining repositioning capacity.

### ¶14. The PAE Framework

The PAE Framework operationalizes process commitment through three sequential stages:

**Stage 1: Platformize** — Create shared decision infrastructure that makes repositioning discussable without threatening stakeholder identities.

- Build integrated dashboards connecting technical and financial metrics
- Ensure joint ownership across functions (engineering, finance, operations)
- Establish common data sources for strategic discussions

*Principle*: The platform must be jointly owned. Siloed metrics perpetuate siloed decisions.

**Stage 2: Acculturate** — Develop shared vocabulary for discussing uncertainty and strategic alternatives.

- Create "legitimate language" for repositioning (adaptation, not abandonment)
- Establish mental models for trade-offs (safety-cost frontiers, flexibility scores)
- Normalize uncertainty acknowledgment in stakeholder communication

*Principle*: Vocabulary must emerge from stakeholders, not be imposed on them.

**Stage 3: Evaluate** — Implement explicit protocols for repositioning decisions, specified before triggering evidence arrives.

- Define probability-based triggers (not calendar-based reviews)
- Establish decision authority and escalation paths
- Pre-commit to evaluation criteria before data collection

*Principle*: Protocols must be committed before evidence arrives to prevent motivated reasoning.

### ¶15. Why Sequence Matters

The PAE sequence addresses the Escape Paradox: you cannot move without stakeholder support, but requesting permission to move signals weakness. Each stage builds on the prior:

1. **Platformize** creates neutral infrastructure *before* repositioning is proposed
2. **Acculturate** normalizes repositioning vocabulary *before* specific moves are discussed
3. **Evaluate** establishes decision rules *before* triggering evidence arrives

By the time repositioning becomes relevant, the organizational infrastructure exists to support it without triggering stakeholder panic.

### ¶16. Theoretical Contribution

This reframing preserves commitment's value-creation mechanism while changing its object:

| Traditional Commitment | Process Commitment |
|:-----------------------|:-------------------|
| Commit to *what* to build | Commit to *how* to decide |
| Irreversibility in position | Irreversibility in process |
| Credibility through stubbornness | Credibility through discipline |

The PAE Framework extends Van den Steen's insight: commitment creates value not because it prevents change, but because it structures change. Ventures that commit to rigorous evaluation processes signal competence more credibly than those that simply persist in failing strategies.

### ¶17. Practical Implications

For mobility ventures facing the Funding Paradox, PAE offers a path forward:

1. **Before raising capital**: Negotiate evaluation protocols into term sheets. Pre-commit to repositioning triggers that all parties accept.

2. **After raising capital**: Build shared decision infrastructure immediately, before strategic disagreements emerge. Invest in common vocabulary.

3. **When evidence suggests repositioning**: Invoke pre-committed protocols rather than requesting permission. Execute the process stakeholders already endorsed.

The core principle: *The more specific your funded vision, the more you need decision processes that permit revision.*

---

## Conclusion

### ¶18. Summary

This paper identifies a Funding Paradox in nascent technology markets: capital that enables experimentation simultaneously forecloses it. Empirically, strategic repositioning predicts growth (movers outperform stayers 1.82×), but funding suppresses repositioning. Mobility ventures face this paradox acutely due to structural characteristics—manufacturing, data, redundancy, regulation—that amplify both capital requirements and lock-in effects.

The PAE Framework offers a resolution: commit to evaluation processes rather than strategic positions. Through Platformize → Acculturate → Evaluate, ventures can build the organizational infrastructure for repositioning before it becomes necessary, preserving flexibility without sacrificing stakeholder coordination.

### ¶19. Limitations and Future Research

This analysis has important limitations. The empirical evidence is correlational; repositioning may reflect founder capabilities rather than causing growth. The PAE Framework awaits systematic testing across multiple ventures. Future research should examine when process commitment succeeds versus fails, and how pre-funding PAE implementation compares to post-funding remediation.

### ¶20. Final Reflection

The Funding Paradox reflects a deeper tension in entrepreneurship: the capabilities required to obtain resources differ from those required to use them well. Pitching requires conviction; adapting requires doubt. The ventures that navigate this tension—maintaining certainty for stakeholders while preserving uncertainty for themselves—may represent a distinct entrepreneurial capability worth cultivating.

*Commit to adaptation. Direction first, speed second.*

---

## References

Ghemawat, P. (1991). *Commitment: The dynamic of strategy*. Free Press.

Gompers, P. A. (1995). Optimal investment, monitoring, and the staging of venture capital. *Journal of Finance*, 50(5), 1461-1489.

Kaplan, S. N., & Strömberg, P. (2003). Financial contracting theory meets the real world: An empirical analysis of venture capital contracts. *Review of Economic Studies*, 70(2), 281-315.

Kerr, W. R., Nanda, R., & Rhodes-Kropf, M. (2014). Entrepreneurship as experimentation. *Journal of Economic Perspectives*, 28(3), 25-48.

McKinsey & Company. (2024). *Autonomous vehicles: Moving forward—Perspectives from industry leaders*.

Van den Steen, E. (2017). A formal theory of strategy. *Management Science*, 63(8), 2616-2636.

World Economic Forum. (2025). *Autonomous Vehicles 2025: Charting the Course Ahead*.

---

## Appendix: Variable Definitions

| Variable | Definition | Measurement |
|:---------|:-----------|:------------|
| G | Growth | Total funding / Early-stage VC |
| F | Funding | log(Early-stage capital in $) |
| B | Breadth | Positioning scope (0-100 percentile) |
| B₀ | Initial Breadth | Breadth at founding |
| B_T | Terminal Breadth | Breadth at observation |
| R | Repositioning (signed) | B_T − B₀ |
| A | Repositioning (absolute) | \|R\| |

---

*Word count: ~2,400*
*Structure: I-A-B-C (Introduction, Analysis, Boundary, Contribution)*
