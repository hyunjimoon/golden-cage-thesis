# The Commitment Trap: Why More Funding Correlates with Less Growth

**Hyunji Moon**
MIT Sloan School of Management
*Draft v6.0 — January 4, 2025*

---

> **"Commitment attracts believers; believers provide funding; funding solidifies the echo chamber; echo chambers block learning."**

---

## Abstract

This thesis investigates a puzzling empirical finding: early-stage funding negatively correlates with subsequent growth (ρ = −0.196, p < 0.001, N = 180,994). We decompose this paradox as dG/dF = (dG/dR) × (dR/dF) = (+)(−) = (−), where repositioning drives growth but funding inhibits repositioning. The mechanism operates through echo chamber formation: specific commitments attract like-minded believers, whose funding creates governance structures that block the signal diversity required for learning. We find that "movers" who reposition outperform "stayers" by 1.82× (18.0% vs 9.9% survival). The core contribution shifts the literature from asking why founders *won't* pivot to why they *can't*—from moral hazard to governance lock-in.

---

# I. Introduction

*Core Question: Why dG/dF < 0?*

## ¶1–2: Gospel and Puzzle

**Gospel.** The prevailing wisdom in entrepreneurship holds that "cash is oxygen"—more funding enables more growth. This intuition underlies venture capital as an institution: early capital provides runway for customer discovery, product iteration, and market validation. Scholars from Kerr to Camuffo to Nanda have documented how capital enables experimentation and learning. The logic seems unassailable: startups that raise more can experiment more, learn faster, and scale bigger.

**Puzzle.** Yet the data tell a different story. Analyzing 180,994 ventures from Crunchbase, we find a striking negative correlation between early-stage funding and subsequent growth: ρ(F,G) = −0.196 (p < 0.001). Ventures that raise more early capital grow *less*, not more. This finding contradicts not only practitioner intuition but also the theoretical expectation that capital enables learning. What explains this paradox?

## ¶3–4: Solution

**Solution.** We resolve this paradox through decomposition:

$$\frac{dG}{dF} = \underbrace{\frac{dG}{dR}}_{\text{(+) RG Module}} \times \underbrace{\frac{dR}{dF}}_{\text{(−) FR Module}} = (-)$$

The negative funding-growth relationship emerges from two countervailing forces. First, repositioning drives growth (dG/dR > 0): ventures that adapt their market positioning—"movers"—outperform those that stay fixed—"stayers"—by 1.82×. Second, funding inhibits repositioning (dR/dF < 0): each standard deviation increase in early funding corresponds to 0.4 standard deviations less repositioning.

The mechanism is the **echo chamber trap**. Specific commitments attract believers who share the founder's vision. Skeptics—who might provide valuable disconfirming signals—decline to participate. The believers who do invest create governance structures (board seats, milestone requirements, reporting obligations) that reinforce the original vision. Signal diversity collapses. Learning stops. The venture is trapped.

## ¶5: Variables

| Variable | Name | Definition | Operationalization |
|:--------:|:-----|:-----------|:-------------------|
| **F** | Funding | Early-stage capital | log($) raised at Seed/A |
| **G** | Growth | Scaling success | Total funding / Early VC |
| **R** | Repositioning | Strategic adaptation | \|B_T − B₀\| (absolute change) |
| **B** | Breadth | Positioning scope | 0–100 percentile |

## ¶6: Roadmap

The thesis proceeds as follows. **Section RG** establishes that repositioning drives growth (dG/dR > 0), documenting the 1.82× mover advantage. **Section FR** explains why funding inhibits repositioning (dR/dF < 0), introducing the echo chamber mechanism. **Section P** prescribes when to commit and when to preserve flexibility. **Section C** concludes with implications for founders, investors, and scholars.

---

# RG. Repositioning Drives Growth

*Core Question: Why dG/dR > 0?*

## ¶7–8: Gospel and Puzzle

**Gospel.** Porter's competitive strategy framework counsels that firms should "choose a sustainable position and defend it." Commitment to a well-defined strategy creates barriers to imitation, enables operational optimization, and signals reliability to stakeholders. The implication: strategic stability should predict success.

**Puzzle.** In nascent markets, the opposite appears true. Ventures that reposition—changing their market breadth significantly over time—outperform those that maintain their initial positioning by a factor of 1.82× (18.0% vs 9.9% survival rate). Movement, not stability, predicts growth. How can this be?

## ¶9–10: Solution

**Solution.** Porter's logic assumes a known environment where optimal positions can be identified ex ante. Nascent markets violate this assumption. When the fitness landscape is unknown and shifting, commitment to any specific position risks betting on the wrong horse.

The advantage of movement derives from two sources. First, **partial commitment**: movers commit to *direction* (e.g., "sustainable transportation") rather than *destination* (e.g., "battery swap stations"). This preserves option value while still providing stakeholder coordination. Second, **perceive-act feedback**: movement generates information. Each repositioning attempt reveals market response, enabling Bayesian updating about where value actually lies.

## ¶11–12: Stayer vs Mover Archetypes

| Archetype | Definition | N | Survival | Example |
|:----------|:-----------|--:|:--------:|:--------|
| **Stayer** | R ≈ 0 (no repositioning) | 142,847 | 9.9% | Surestar |
| **Mover** | R > 0 (repositioned) | 38,147 | 18.0% | Sky Engine |

**Key finding**: Movers outperform stayers by 1.82× = 18.0 / 9.9

**Case: Sky Engine.** Founded in 2013 as a consumer drone company (B₀ = 23), Sky Engine pivoted to enterprise industrial inspection (B_T = 84) after discovering that consumer margins couldn't support R&D costs. This repositioning (R = +60.7) led to acquisition at 216× revenue multiple.

## ¶13–14: R-G Positive Correlation

The relationship between repositioning magnitude (R) and growth (G) is robustly positive across specifications. The scatter plot reveals a clear upward trend: ventures in the upper-right quadrant (high R, high G) systematically outperform those in the lower-left (low R, low G).

This pattern holds after controlling for industry, founding year, and initial funding level. The 1.82× advantage is not an artifact of survivor bias—it emerges from comparing outcomes within cohorts matched on observables.

## ¶15: Cases and Limitations

**Tesla vs Better Place: A Tale of Two Commitments**

| Dimension | Tesla | Better Place |
|:----------|:------|:-------------|
| Promise type | Mission ("Sustainable energy") | Product ("Battery swap") |
| Commitment level | Staged (Roadster → Model S → Model 3) | Full upfront ($850M infrastructure) |
| Flexibility | Pivoted from sports car to mass market | Locked into swap station network |
| Outcome | Global leader | Liquidation (2013) |

Tesla committed to a *mission*, allowing product-level flexibility. Better Place committed to a *product*, foreclosing adaptation when the battery swap model failed to gain traction.

**Limitations.** Selection bias may inflate mover advantage if more capable founders are more likely to reposition. Hindsight bias may lead us to rationalize successful pivots as "strategic" while dismissing failed ones as "flailing."

---

# FR. Funding Inhibits Repositioning

*Core Question: Why dR/dF < 0?*

## ¶16–17: Gospel and Puzzle

**Gospel.** Capital enables experimentation. Kerr, Camuffo, and Nanda have documented how funding allows ventures to run more experiments, test more hypotheses, and learn faster. The intuition: more money = more runway = more learning opportunities.

**Puzzle.** Yet we observe dR/dF < 0: a one-standard-deviation increase in early funding corresponds to 0.4 standard deviations *less* repositioning. Ventures with more capital adapt *less*, not more. If capital enables learning, why do well-funded ventures fail to learn?

## ¶18–20: The Echo Chamber Mechanism

**Solution.** The answer lies in the *echo chamber mechanism*:

```
Commitment (specific promises to raise capital)
    ↓ attracts
Believers (skeptics decline to invest)
    ↓ provide
Funding (from like-minded investors)
    ↓ creates
Governance (board seats, milestones, reporting)
    ↓ solidifies
Echo Chamber (everyone agrees on the vision)
    ↓ eliminates
Signal Diversity (no one says "pivot")
    ↓ blocks
Learning → TRAP
```

The mechanism begins with fundraising itself. To attract capital, founders make specific commitments: "We will build a battery swap network for electric vehicles." These commitments attract investors who believe in that specific vision. Skeptics—those who might later say "battery swap won't work, pivot to supercharging"—decline the deal.

The believers who invest don't just provide capital; they create governance structures. Board seats, voting rights, milestone-based tranches, and regular reporting obligations all reinforce the original vision. The more capital raised, the more investors involved, the more complex the governance—and the harder it becomes to change direction.

**The result is an echo chamber.** Everyone around the table agreed to the original plan. No one has an incentive to suggest pivoting. Signal diversity collapses. The venture loses access to the disconfirming information required for genuine learning.

## ¶21–22: Three Types of Learning

Funding affects different types of learning differently:

| Type | What Changes | Commitment Effect | Example |
|:-----|:-------------|:------------------|:--------|
| **Sampling** | Number of samples | Enhanced | More customer interviews |
| **Recalibrating** | State space | Blocked | "Software matters, not just hardware" |
| **Reframing** | Utility function | Blocked | Market share → Profitability |

**Sampling** (running more experiments within a fixed hypothesis space) is enhanced by funding. More capital enables more customer interviews, more A/B tests, more product iterations.

**Recalibrating** (expanding the hypothesis space to include previously unconsidered possibilities) is blocked by funding. When governance is locked into "battery swap will work," the possibility that "battery swap might not work" is structurally excluded.

**Reframing** (questioning the objective function itself) is blocked by funding. When investors expect market share growth, pivoting to profitability requires not just new tactics but new success metrics—a conversation the echo chamber is designed to prevent.

## ¶23: The Learning Trap Theorem

**Theorem.** Learning stops when: μ(1−μ) < ε × B

Where:
- μ = belief certainty (how sure the founder is)
- ε = perceived cost of updating
- B = switching cost barrier (governance complexity)

When belief certainty is high (μ → 1) and governance complexity is high (B is large), the condition is easily satisfied. The venture is trapped: even if disconfirming signals arrive, the cost of acting on them exceeds the expected benefit of updating.

**Motional case.** The Hyundai-Aptiv joint venture raised $4B to pursue L4 robotaxi. With both corporate parents believing in the robotaxi vision, the echo chamber was complete. When the market shifted toward L2+ ADAS, Motional could not pivot: the governance structure locked them into robotaxi. Result: 50% workforce reduction (2024), no pivot, trapped.

## ¶24: LTE Theory and Limitations

**Map to LTE Theory.**
- Layer 1 (What): Repositioning measurement (R = |B_T − B₀|)
- Layer 2 (How): Echo chamber mechanism
- Layer 3 (Why): Bayesian updating with governance constraints

**Limitations.**
1. **Not causal.** The F→R relationship is correlational. Endogeneity is likely: founders who intend to pivot may deliberately raise less.
2. **Sample selection.** Crunchbase overrepresents funded ventures; bootstrapped companies are underrepresented.
3. **Future work.** LTE simulation required to replicate the echo chamber mechanism in silico and test policy interventions.

---

# P. Prescription

*Core Question: When to commit and when to preserve flexibility?*

## ¶25: Test → Choose → Commit

**The T2C1 Framework.** Synthesizing Scott Stern's "partial commitment" with Charlie Fine's "nail with flexibility," we propose a staged approach:

| Stage | Action | Commitment Level | Example |
|:------|:-------|:-----------------|:--------|
| **Test** | Run parallel experiments | Partial | Multiple market segments |
| **Choose** | Select based on evidence | Focused | Winner emerges from data |
| **Commit** | Scale the winner | Full | Operational excellence |

The key insight: **commit to the process, not the position.** Lock in the *how* (a disciplined experimentation system) while keeping the *what* (specific market position) flexible.

## ¶26: Segment → Collaborate → Replicate

**The S-C-R Sequence.** For ventures navigating the autonomous vehicle space:

| Phase | Action | Example |
|:------|:-------|:--------|
| **Segment** | Identify distinct market segments | Robotaxi, Trucking, Ride-hailing |
| **Collaborate** | Partner for missing capabilities | HMG (manufacturing), AI startups (software) |
| **Replicate** | Scale proven model to new markets | California → Texas → Asia |

**Escape paths from the trap:**

| Path | Funding Level | Mechanism | Example |
|:-----|:--------------|:----------|:--------|
| **Agile** | Low (~$2M) | Voluntary pivot | Sky Engine |
| **Forced** | High ($2B+) | Crisis → Pivot | Nuro |
| **Boundary** | High + Expectation mgmt | Preserve options | Aurora |

## ¶27: Balancing Growth and Capability

**The Acculturate-Platformize Balance.** Ventures must balance market growth rate against operational capability development:

- **Acculturate**: Build shared language and evaluation metrics across the organization. This enables rapid coordination when pivots are required.
- **Platformize**: Abstract capabilities into exchangeable modules. When the robotaxi market disappoints, the perception stack can be redeployed to trucking without rebuilding from scratch.

The ventures that escape the trap are those that invest in *meta-capabilities*—the ability to change direction rapidly—even as they execute on their current strategy.

---

# C. Conclusion

*Core Question: So what?*

## ¶28: Implications

**For Founders:**
> "Commit to movement, not to position. Commit to direction, not destination."

The ventures that thrive in nascent markets are those that master the paradox of committed flexibility: signaling enough commitment to attract resources while preserving enough flexibility to adapt. The key is the *object* of commitment. Commit to the mission, not the product. Commit to the process, not the outcome.

**For Investors:**
> "The ventures most likely to succeed may reposition away from the pitch that won your commitment. Design for signal diversity ex ante."

Rather than monitoring founders to prevent pivots (the moral hazard framing), investors should design governance structures that preserve signal diversity. Include skeptics on the board. Build in pivot-friendly milestones. Expect repositioning—and reward it when evidence supports it.

**For Scholars:**
> "In nascent environments, the object of commitment must shift from position to process."

The commitment literature has focused on position-level commitment (to a strategy, a market, a technology). This thesis suggests that in environments of high uncertainty, the valuable form of commitment is process-level: commitment to learning, to experimentation, to adaptation. Van den Steen's (2017) insight that commitment solves coordination problems must be extended: the coordination problem in nascent markets is not "which position?" but "how to update?"

## ¶29: Limitations and Summary

**Limitations.**
1. **Not causal.** This thesis documents correlations, not causes. Endogeneity is pervasive: founders who plan to pivot may raise less; investors may provide more capital to ventures they believe won't need to pivot. Instrumental variable or experimental approaches are needed for causal identification.
2. **Sample.** Crunchbase data underrepresents bootstrapped ventures and non-US companies. The funding-growth paradox may be a specifically VC-backed phenomenon.
3. **Future work.** LTE (Layer-Theory-Evidence) simulation is required to replicate the echo chamber mechanism computationally and test policy interventions (e.g., mandating board diversity, restructuring milestone incentives).

**Summary.**

This thesis began with a puzzle: why does more funding correlate with less growth? The answer lies in a mechanism we call the **commitment trap**:

> **"Commitment attracts believers; believers provide funding; funding solidifies the echo chamber; echo chambers block learning."**

The core contribution is a shift in framing. The existing literature asks why founders *won't* pivot (moral hazard, incentive alignment). This thesis asks why they *can't* pivot (governance lock-in, structural constraint). The implication is profound: the solution is not better monitoring but better governance design—building signal diversity into the funding relationship from the start.

---

## Core Contribution Summary

| Dimension | Existing Literature | This Thesis |
|:----------|:--------------------|:------------|
| **Problem** | Founders **won't** pivot | Founders **can't** pivot |
| **Cause** | Moral hazard (incentive) | Governance lock-in (structure) |
| **Mechanism** | Agency problem | Commitment → Believers → Funding → Echo Chamber |
| **Solution** | Monitor founders | Design signal diversity ex ante |

---

## Canonical Numbers

| Finding | Value | Source |
|:--------|:------|:-------|
| Funding-Growth correlation | ρ = −0.196*** | I |
| Sample size | N = 180,994 | I |
| Mover advantage | 1.82× (18.0% vs 9.9%) | RG |
| Funding → Repositioning | 1 SD F → 0.4 SD less R | FR |

---

*必死卽生 — Commit to ADAPTATION, direction first and speed second.*

---

**References**

[To be added]

---

*Draft generated: January 4, 2025*
*Structure: I-RG-FR-P-C (29 paragraphs)*
*Version: v6.0 Sail Edition*
