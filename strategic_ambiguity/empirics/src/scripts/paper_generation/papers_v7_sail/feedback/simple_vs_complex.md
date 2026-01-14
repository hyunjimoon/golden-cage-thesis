# Simple vs Complex Version: Advisor Choice

**Core Principle**: LESS IS MORE (Miaomiao feedback)

---

## The Problem

Current thesis has **too many statistics**:
- ρ(E,G) = -0.196
- ρ(E,R) = -0.087
- 2.60× Mover Advantage
- χ² = 5,322
- 18.1% vs 7.0%
- +11.1 pp effect size
- N = 180,994
- Industry-specific correlations (Hardware: -0.108, Transportation: -0.101, Quantum: +0.095)
- Sweet Spot: 16.0% survival
- Case studies: Hope Care 2.71×, Leap Green 0.80×

**Reader cognitive load**: Too high. Key message gets lost.

---

## Proposed Hierarchy

### Tier 1: THE ONE NUMBER (Hammer this)
| Stat | Value | Plain English |
|:-----|:------|:--------------|
| **Mover Advantage** | **2.60×** | "Ventures that reposition are 2.6× more likely to succeed" |

This is THE headline. Everything else supports it.

### Tier 2: The Mechanism (3 stats)
| Stat | Value | Role |
|:-----|:------|:-----|
| ρ(E,R) = -0.087*** | Funding suppresses repositioning | Why movers are rare |
| 18.1% vs 7.0% | Success rates | Unpacks the 2.60× |
| N = 180,994 | Sample size | Credibility |

### Tier 3: Depth (for appendix/robustness)
- ρ(E,G) = -0.196 (net effect)
- χ² = 5,322 (significance)
- Industry heterogeneity
- Case studies

---

## Two Versions for Advisors

### SIMPLE VERSION (Recommended for Defense)

**One slide, one number:**

> "Ventures that reposition are **2.60× more likely to succeed**—but funding suppresses repositioning."

**Supporting evidence** (footnote level):
- N = 180,994 ventures
- p < 0.001

**Causal chain** (visual only):
```
Funding → Less Repositioning → Lower Growth
   ↓            ↓                  ↓
 (E↑)     (ρ = -0.087***)      (2.60× gap)
```

**Figures**: 2-3 max
1. Fig 1: The Funding-Growth Paradox (scatter)
2. Fig 2: Mover vs Stayer Success Rate (bar chart)
3. Fig 3: The Golden Cage Mechanism (DAG)

---

### COMPLEX VERSION (For Written Thesis)

Keep all current statistics, but:
1. Move Tier 3 stats to appendix
2. Present Tier 1 first, then unpack with Tier 2
3. Industry heterogeneity → separate results subsection

**Chapter structure**:
- §4.1: The Headline (2.60×)
- §4.2: Unpacking the Mechanism (Tier 2)
- §4.3: Robustness & Heterogeneity (Tier 3 summary, detail in appendix)

---

## Recommendation for Advisors

| Audience | Version | Rationale |
|:---------|:--------|:----------|
| **Defense presentation** | Simple | 15-20 min, need clarity |
| **Written thesis** | Complex | Comprehensive record |
| **Paper submission** | Simple | Journal reviewers value clarity |
| **Technical appendix** | Complex | Methodological rigor |

**Question for advisors**:
> "For the defense, should I present the Simple version (2.60× headline + 2 supporting stats) or the Complex version (full decomposition)?"

---

## Action Items if Simple Chosen

1. **Ch1**: Keep only 2.60× and N = 180,994
2. **Ch2**: Remove all statistics except mechanism description
3. **Ch4**: Lead with 2.60×, move decomposition to §4.2
4. **Figures**: Reduce from 10+ to 5 core figures

## What Gets Cut (Simple Version)

| Current | Action |
|:--------|:-------|
| ρ(E,G) = -0.196 | Move to appendix |
| χ² = 5,322 | Footnote only |
| Industry-specific ρ | Appendix table |
| Case study ratios | Keep 1 example (Tesla vs Better Place narrative) |
| Sweet Spot 16.0% | Ch5 only, not intro |

---

## One-Liner for Each Version

**Simple**: "Funding cages startups. Movers succeed 2.6× more—but funding suppresses movement."

**Complex**: "Early funding correlates negatively with growth (ρ = -0.196) because it suppresses repositioning (ρ = -0.087), and repositioning drives success (2.60× Mover Advantage, p < 0.001, N = 180,994)."

---

*Created: 2026-01-14*
*Purpose: Advisor decision on thesis presentation style*
