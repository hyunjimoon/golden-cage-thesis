# I: The Funding Paradox
## Introduction (v5)

**¶1-10 | Keystone | Locks: F, R, A, G, B, core equation, LTE + Cronin**

---

**¶01** The strategy literature debates commitment versus flexibility. Van den Steen (2017) formalizes why strategy creates value because commitment is costly—irreversibility signals credibility. Ghemawat (1991): "commitment is the essence of strategy." Another tradition emphasizes flexibility: Mintzberg (1987), Teece et al. (1997). This dissertation asks: when does each matter most? The answer has stakes: $330B in VC funded committed founders. But what if early-stage capital is an anchor, not rocket fuel?

**¶02** The empirical evidence: ventures that raise more early-stage funding show *lower* subsequent growth. ρ(G,F) = −0.196 (p < 0.001, N = 408,697). I call this the **Funding Paradox**.

**¶03** This dissertation explains why. The answer lies in **repositioning**—the strategic change a venture undertakes. Repositioning = realized option. Sky Engine repositioned ("AI for autonomous vehicles" → "synthetic data cloud for vision AI")—grew 216×. Surestar stayed—grew 27×. Firms that reposition outperform stayers by 1.82× (18.0% vs 9.9% survival). **Repositioning predicts growth (dG/dA > 0), but funding suppresses repositioning (dA/dF < 0).**

**¶04** Five variables structure the analysis:
- **F** = Funding (log early-stage capital)
- **G** = Growth (total funding / early VC)
- **B** = Breadth (0-100 percentile, scope of positioning)
- **R** = Repositioning (B_T − B₀), signed
- **A** = Absolute Repositioning (|R|)

**¶05** The Funding Paradox resolves through decomposition:
```
dG/dF = (dG/dA) × (dA/dF) < 0
```
- dG/dA > 0: repositioning → growth
- dA/dF < 0: funding → stakeholder lock-in → less repositioning
- Product of positive and negative = negative

**¶06** Reconceptualization: commitment is liability in nascent environments. Prescription: **"Nail it with flexibility, then scale it with commitment."** Van den Steen's commitment-creates-value requires scope condition: in high uncertainty, object of commitment must shift from position to repositioning capability.

**¶07** This dissertation proceeds in three sections. Following this introduction, **Section A** (AG+FA) establishes the Repositioning Principle: firms that reposition outperform stayers, but funding suppresses repositioning. **Section B** (BT) explains heterogeneous outcomes through the learning trap mechanism: μ(1−μ) < ε×B. **Section C** (C1-C4) demonstrates intervention design via the NFSC framework and Fine22 extension.

The dissertation employs the **Layer-Theory-Evidence (LTE)** structure (Cronin et al., 2025, *Organization Science*):

> "Construct theories tell us WHAT relationships exist ('funding correlates with failure'), but process theories tell us WHO does WHAT, WHEN, and WHY—enabling precise intervention design."

| Section | LTE Layer | 질문 | 기여 |
|:-------:|:---------:|:-----|:-----|
| A | Layer 2 (HOW) | 어떤 순서로? | 자금→약속→lock-in→재포지셔닝억제 |
| B | Layer 3 (WHY) | 왜 작동? | μ(1−μ) < ε×B 학습 함정 메커니즘 |
| C | Intervention | 그래서 뭘? | NFSC + Fine22 10 Tools 체계적 적용 |

**왜 이 구조가 기여인가:**

| 비평 | 반박 (LTE 기반) |
|:-----|:----------------|
| "인과 없으면 기여 부족" | Layer 1이 현상의 존재(What)를 입증했기에 Layer 2(How)가 가치를 가짐. 본 논문은 Layer 1을 전제로 Layer 2+3을 추가 |
| "상관관계만으로 부족" | 동의함. 상관관계는 증상을 보여주고, 과정이론은 치료법을 제시함. 둘 다 필요하며 상호보완적 |
| "실천적 함의 약함" | Layer 1은 "무엇이 문제인지", Layer 2는 "어떻게 개입할지" 답함. Process Theory = actor-level 처방 가능 |
| "왜 저널이 받아야?" | Cronin et al. (2025): Layer 1(Construct)과 Layer 2(Process)는 상호보완적이며, intervention design에는 둘 다 필요 |

**¶08** Traps occur at both extremes of B₀:
- **High-B₀ trap**: Too vague → can't falsify (Mobility: B₀=78, 5% survival)
- **Low-B₀ trap**: Too specific → can't pivot (Motional: echo chamber)

**¶09** Prescription: commit to repositioning capability, not fixed positions. Design structures that preserve flexibility even as capital flows.

**¶10** The contribution is not causal identification (Layer 1), but mechanism decomposition (Layer 2+3)—enabling founders and investors to design interventions that escape the funding trap.

---

## I Output Interface

```yaml
I_OUTPUT:
  locks:
    - F: "early-stage funding (log $)"
    - G: "growth (total funding / early VC)"
    - B: "breadth (0-100 percentile)"
    - R: "repositioning (B_T - B_0), signed"
    - A: "|R| = |B_T - B_0|, magnitude"
  core_equation: "dG/dF = (dG/dA)(dA/dF) < 0"
  types: [stayer, zoom_in, zoom_out]
  key_stats:
    - "ρ(G,F) = -0.196 (p < 0.001, N = 408,697)"
    - "Repositioners: 18.0% survival, Stayers: 9.9% survival"
    - "Repositioning advantage: 1.82×"
```

---

*v5 Update: V→B, M→R/A terminology (Dec 29 Charlie feedback)*
