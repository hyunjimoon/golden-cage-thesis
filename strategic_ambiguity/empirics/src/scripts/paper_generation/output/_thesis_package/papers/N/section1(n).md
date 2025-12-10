# 🤹N: Promise Vendor — Optimal Number of Options
## Chapter 1: Introduction

**Version:** 3.0 (D Redefined: Demand → Distribution of Viable Paths)
**Core Contribution:** Reinterpretation of Newsvendor D for strategic context
**R&R #4:** FATAL — 수학 기반 없으면 k* 공식 붕괴

---

## Abstract

The newsvendor model optimizes inventory against a **demand distribution** D. But for startups, "demand" has no meaning — there are no customers yet. We propose a **strategic reinterpretation**: D is not customer demand but the **Distribution of Viable Paths** — the probability distribution over how many strategic paths will prove viable ex post.

This reinterpretation preserves the mathematical structure while gaining strategic meaning:
- **C_u** (underage cost) becomes **FOMO cost** — the penalty for missing a viable path
- **C_o** (overage cost) becomes **Burn cost** — the waste from maintaining a dead-end option
- **k*** (optimal inventory) becomes **optimal number of strategic options**

$$k^* = F_D^{-1}\left(\frac{C_u}{C_u + C_o}\right)$$

Where D ~ Poisson(λ) represents the distribution of viable paths, estimated from industry-level revealed viability data.

---

## ¶1. Gospel (H₀): News Vendor — "D = Demand"

> **The Newsvendor Gospel**: Given demand distribution D, find optimal inventory q* = F_D⁻¹(C_u/(C_u+C_o)).

This model is elegant. But it assumes D is **customer demand** — how many units customers will buy.

**For startups, this assumption fails.** There are no customers yet. What is "demand"?

---

## ¶2. Puzzle: 스타트업은 "수요"가 없다

In the AV industry (2016):
- **Waymo**: Hedged across LiDAR, Vision, L2, L4 (k=5 options)
- **Tesla**: Bet on Vision + Battery (k=2 options)
- **Comma.ai**: Vision-only (k=1 option)

Which k is optimal? The newsvendor can't answer because we don't know what "D" means for them.

**The puzzle**: What should D represent when there's no demand data?

---

## ¶3. RQ: D를 어떻게 재해석할 수 있는가?

> **Research Question**: Can we reinterpret the newsvendor's D to have strategic meaning for ventures with no past demand?

From classical operations:
- D = "how many customers will come?"
- q* = "how much inventory to hold?"

**Our reinterpretation**:
- D = "how many strategic paths will prove viable?"
- k* = "how many options to hold?"

---

## ¶4. Lens: D = Distribution of Viable Paths

We propose the **Promise Vendor** model — a reinterpretation of newsvendor:

| | Classical Newsvendor | Promise Vendor (Ours) |
|:---|:---|:---|
| **D means** | Customer demand | **Viable strategic paths** |
| **Decision** | Inventory quantity q | **Option count k** |
| **C_u (underage)** | Lost sale | **FOMO cost** (missed viable path) |
| **C_o (overage)** | Unsold stock | **Burn cost** (wasted option) |

This is a **mathematical isomorphism** — same formula, different interpretation:
$$k^* = F_D^{-1}(CR) \quad \text{where } D = \text{Distribution of Viable Paths}$$

---

## ¶5. Solution: The Promise Vendor Formula

**Core Result**:

$$k^* = F_D^{-1}\left(\frac{C_u}{C_u + C_o}\right)$$

Where:
- **D** ~ Poisson(λ) = Distribution of viable paths (from industry data)
- **C_u** = FOMO cost = penalty for missing a viable path
- **C_o** = Burn cost = waste from maintaining dead-end option

### FOMO as Bayesian C_u Signal

```
FOMO 발동: "저것도 해야 할 것 같아"
    ↓
= High perceived C_u (cost of missing that path)
    ↓
= Bayesian update: λ might be higher
    ↓
CR ↑ → k* ↑
```

**Insight**: FOMO is not irrational. It's a **Bayesian signal that C_u is high**.

| Industry | λ | CR | k* | FOMO Level |
|:---|:---:|:---:|:---:|:---|
| **SaaS** | 0.9 | 0.25 | 1 | Low ("one path wins") |
| **Hardware** | 1.1 | 0.50 | 1-2 | Moderate |
| **Biotech** | 1.4 | 0.60 | 2 | High ("multiple modalities") |
| **Deep-tech** | 1.8 | 0.85 | 3-4 | Very High ("nobody knows") |

---

## ¶6. Positioning: Closest Papers

| Paper | Focus | Gap We Fill |
|:---|:---|:---|
| Arrow (1958) | Newsvendor: optimal q* given D | **What is D for startups?** |
| McGrath (1999) | Real options thinking | **No optimal k* formula** |
| Adner (2002) | Option exercise timing | **How many options, not when** |
| Kogut & Kulatilaka (2001) | Platform options | **Assumes known D** |

**Our contribution**: Reinterpret D as Distribution of Viable Paths — mathematical validity preserved, strategic meaning gained.

---

## ¶7. Roadmap

| Chapter | Content | Key Output |
|:---|:---|:---|
| [[chap2_theory]] | D reinterpretation + k* derivation | D = Viable Paths, k* = F_D⁻¹(CR) |
| [[chap3_empirics]] | λ estimation by industry | Poisson λ from revealed viability |
| [[chap4_discussion]] | Three-paper integration | V→D, E→C_u/C_o, k* synthesis |

---

## Connection to Trilogy

```
✌️U: V → D (Vagueness shapes the distribution of viable paths)
      ↓
🦾C: E → C_u/C_o (Capital affects FOMO/Burn cost structure)
      ↓
🤹N: k* = F_D⁻¹(C_u/(C_u+C_o)) (Optimal options from D and costs)
```

**Punchline**: *"D is not demand — it's the distribution of viable paths. The newsvendor formula works; the meaning is transformed."*

---

*Ready for Theory development (¶8-17).*
