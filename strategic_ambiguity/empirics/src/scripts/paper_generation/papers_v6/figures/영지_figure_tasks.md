# 영지 Figure Tasks (見 See)

> 덕목: 見 (Observe/See) — 본질을 포착하여 시각화
> 업데이트: 2026-01-08

---

## 📊 Figure 총괄표 (10개)

| Figure | 제목 | 위치 | 상태 | 이미지 파일 |
|:------:|:-----|:----:|:----:|:------------|
| **Fig-GC** | Golden Cage (Canary) | Cover/¶5 | ✅ selected | `versionA.png` |
| **Fig-I** | Funding Paradox | ¶9 | ✅ exists | `Fig-I_funding_paradox.png` |
| **Fig-CFR1** | Golden Cage Mechanism | ¶21 | ✅ exists | `Fig-FR1_golden_cage.png` |
| **Fig-CFR2** | Learning Trap / Selection | ¶22 | ✅ exists | `Fig-FR2_learning_trap.png` |
| **Fig-ARG** | Mover vs Stayer Trajectories | ¶14 | ✅ exists | `Fig-RG_mover_vs_stayer.png` |
| **Fig-P1** | Doubly-Binded Effect | ¶27 | ⏳ NEW | (생성 필요) |
| **Fig-P2** | Capitalize (B↑→G↑) | ¶26 | ⏳ NEW | (생성 필요) |
| **Fig-Causal** | 인과 다이어그램 | ¶5 | ⚠️ text only | (본문 ASCII로 충분) |
| **Fig-GB** | Strategic Ambiguity | ¶14 | ⏳ pending | (미생성) |
| **Fig-Rob** | 3-Panel Robustness | ¶23 | ⏳ pending | (미생성) |

---

## 🐦 Fig-GC: The Golden Cage (Thesis Cover)

| Spec | Value |
|:-----|:------|
| **Type** | Metaphor Illustration |
| **Subject** | Blue canary in gilded cage |
| **Structural Constraint** | Wings bound (손이 묶임) |
| **Cognitive Constraint** | Eyes veiled (눈이 가려짐) |
| **Color** | 🟡 Gold (#d4a84b) + 🔵 Blue (#4dabf7) |
| **Status** | ✅ versionA selected |
| **Image** | `day5_thesis(IAPC)/.../versionA.png` |

**Caption** ✅ SELECTED:
> **"Wings bound, eyes veiled."**

- 4단어, 대구(parallelism) 구조
- 구조적 제약 (wings) + 인지적 제약 (eyes) 암시

---

## 📊 Fig-I: Funding Paradox (¶9)

| Spec | Value |
|:-----|:------|
| **X-axis** | F (Funding) - log scale |
| **Y-axis** | G (Growth) |
| **Slope** | **Negative** (ρ = −0.196***) |
| **Color** | 🔴 Red (#ff6b6b) |
| **Message** | "More funding → Less growth" |
| **N** | 408,784 ventures |
| **Image** | `Fig-I_funding_paradox.png` |

**Caption**: Stayer (9.9%) vs Mover (17.9%) — Movement predicts growth (N=180,994)

---

## 📊 Fig-CFR1: Golden Cage Mechanism (¶21)

| Spec | Value |
|:-----|:------|
| **X-axis** | Early Capital E ($M, log scale) |
| **Y-axis** | Adaptive Capacity A = |D_t| |
| **Slope** | λ = −0.102*** (one-tailed) |
| **Color** | 🟡 Gold (#d4a84b) |
| **Message** | "Money buys commitment, not flexibility" |
| **N** | 180,860 |
| **Image** | `Fig-FR1_golden_cage.png` |

**Caption**: Golden Cage confirmed: +1SD funding → −0.4SD adaptive capacity

---

## 📊 Fig-CFR2: Learning Trap / Endogenous Selection (¶22)

| Spec | Value |
|:-----|:------|
| **X-axis** | Vagueness (Ambiguity, 0-1) |
| **Y-axis** | Final Valuation (Growth) |
| **Type** | Scatter with zones |
| **Colors** | 🔵 Analyst-Backed (Precise) / 🟡 Believer-Backed (Vague) |
| **Key Zones** | "Trapped Success" (low V) vs "Generative Sufficiency" (high V) |
| **Formula** | μ(1−μ) < ε/B |
| **Image** | `Fig-FR2_learning_trap.png` |

**Caption**: Endogenous Selection — Vagueness unlocks scale, precision traps

---

## 📊 Fig-ARG: V Trajectories by Archetype (¶14)

| Spec | Value |
|:-----|:------|
| **Type** | 3-panel time series |
| **Panels** | zoom_in (N=8,521) / zoom_out (N=13,222) / stayer (N=376,515) |
| **X-axis** | Year (2021-2025) |
| **Y-axis** | V (Vagueness) |
| **Key Insight** | Movers change V dramatically; Stayers remain flat |
| **Image** | `Fig-RG_mover_vs_stayer.png` |

**Caption**: Movers (R≥10) vs Stayers (R<10) — Movement direction doesn't matter, magnitude does

---

## 📊 Fig-P1: Doubly-Binded Effect (¶27) — NEW

| Spec | Value |
|:-----|:------|
| **Type** | Line chart with zones |
| **X-axis** | C (Commitment Level) |
| **Y-axis** | G (Growth) |
| **Lines** | High A (완만 ↘) vs Low A (급격 ↘) |
| **Key Zone** | "Stuck in middle" — C와 A 모두 제약 → 최저 G |
| **Example** | Waymo: high C (massive funding) + low A (policy constraints) → 성장 정체 |
| **Color** | 🔴 Red zone for doubly-binded |
| **Status** | ⏳ NEW — 생성 필요 |

**Problem**: Mobility ventures = CFR(Commitment 제약) + ARG(Flexibility 제약) 이중 구속
- Waymo: blackouts, customer perception↓, EV subsidy 축소
- 정치적/규제적 불확실성이 adaptability 제약

**Caption**: Doubly-binded ventures (high C, low A) show lowest growth rates

---

## 📊 Fig-P2: Capitalize via Strategic Ambiguity (¶26) — NEW

| Spec | Value |
|:-----|:------|
| **Type** | Scatter/Line chart |
| **X-axis** | B (Breadth/Vagueness, 0-100) |
| **Y-axis** | G (Growth) |
| **Shape** | Monotonic ↗ — B↑ → G↑ |
| **Key Insight** | precise(B≈0)보다 broad(B↑)가 성장↑ |
| **Mechanism** | 모호함 → 투자자/고객이 각자 optimism 투영 가능 |
| **Color** | 🟠 Orange (#ffa502) |
| **Status** | ⏳ NEW — 생성 필요 |

**Solution**: CSCE 4 Tools
- **C**apitalize: Strategic Ambiguity (B↑→G↑)
- **S**egment: Robotaxi / B2B Fleet / Adjacent markets
- **C**ollaborate: Ops 역량 파트너십
- **E**valuate: Market∥Ops 균형점

**Caption**: Strategic Ambiguity enables growth — broader positioning attracts diverse believers

---

## 📊 Fig-Causal: 인과 다이어그램 (¶5)

| Spec | Value |
|:-----|:------|
| **Type** | DAG (Directed Acyclic Graph) |
| **Chain** | C → A → R → G |
| **Observed** | F ··· R (ρ = −0.196) |
| **Mechanism** | C decreases A, A increases R |
| **Status** | ⚠️ Text only — visualization needed |

**Current Text Version**:
```
C ──decreases──▶ A ──increases──▶ R ──increases──▶ G
                                    ▲
F ·········observed (ρ=−0.196)·····┘
```

---

## 📊 Fig-GB: Strategic Ambiguity (¶14) — PENDING

| Spec | Value |
|:-----|:------|
| **X-axis** | B (Breadth/Vagueness, 0-100) |
| **Y-axis** | G (Growth) |
| **Key Insight** | 방향 무관 — |ΔB| (movement magnitude) matters |
| **Examples** | Sky Engine (+60.7), Linpowave (−56.3) — both Movers |
| **Color** | 🟠 Orange (#ffa502) |
| **Status** | ⏳ pending |

---

## 📊 Fig-Rob: 3-Panel Robustness (¶23) — PENDING

| Panel | X-axis | Y-axis | Expected Slope |
|:------|:-------|:-------|:---------------|
| **Panel A** | F | G | Negative (−) |
| **Panel B** | F | R | Negative (−) |
| **Panel C** | R | G | Positive (+) |

**Layout**: 1 row × 3 columns
**Caption**: Decomposition holds: dG/dF = (dG/dR)(dR/dF) = (+)(−) = (−)

---

## 🎨 Color Semantic (Thesis-wide)

| Variable | Color | Hex | Meaning |
|:---------|:------|:----|:--------|
| C (Commitment) | 🟡 Gold | #d4a84b | Trap, constraint |
| F (Funding) | 🔵 Blue | #4dabf7 | Input, neutral |
| A (Adaptability) | 🟢 Teal | #2ed573 | Capacity |
| B (Breadth) | 🟠 Orange | #ffa502 | Cognitive scope |
| R (Repositioning) | 🟣 Purple | #a855f7 | Movement, change |
| G (Growth) | 🟢 Green | #69db7c | Positive outcome |
| I (Introduction) | 🔴 Red | #ff6b6b | Problem, alert |

---

## ✅ CARE Checklist for Figures

- [ ] **C**risp: One figure = one message
- [ ] **A**ccessible: Colorblind-safe, readable at 50% zoom
- [ ] **R**eader-loving: Main insight obvious in 3 seconds
- [ ] **E**arned: Every element justifies its existence

---

## 🎨 톤 통일 과제

현재 이미지 톤 불일치:
- Dark theme: Fig-I, Fig-CFR2
- Light theme: Fig-ARG, Fig-CFR1, Fig-P
- Artistic: Fig-GC (독자적 유지)

**권장**: 데이터 차트들 → Dark theme로 통일 (Fig-I 스타일)

---

## 📁 이미지 파일 위치

**로컬 (papers_v6/figures/images/):**
```
papers_v6/figures/images/
├── Fig-GC_golden_cage_canary.png   (972 KB) - 🐦 Thesis cover
├── Fig-I_funding_paradox.png        (56 KB)  - ¶9
├── Fig-ARG_mover_vs_stayer.png      (1.0 MB) - ¶14
├── Fig-CFR1_golden_cage.png         (289 KB) - ¶21
├── Fig-CFR2_learning_trap.png       (493 KB) - ¶22
└── Fig-P_CSCE.png                   (85 KB)  - ¶26
```

**원본 (Dropbox):**
```
/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/Tool4Ops4Entrep/acculturate/
└── w9_acculturate(thesis)/day4_IAPC/angie_prior2post/prior/figures/
```

---

## 📋 Status Summary

| Status | Count | Figures |
|:-------|:-----:|:--------|
| ✅ Selected | 1 | Fig-GC |
| ✅ Exists | 5 | Fig-I, Fig-CFR1, Fig-CFR2, Fig-ARG |
| ⏳ NEW | 2 | **Fig-P1** (Doubly-Binded), **Fig-P2** (Capitalize B↑→G↑) |
| ⚠️ Text only | 1 | Fig-Causal (본문 ASCII로 충분) |
| ⏳ Pending | 2 | Fig-GB, Fig-Rob |

**우선순위**: Fig-P1, Fig-P2 → Fig-GB → Fig-Rob

---

## 🔗 Dependencies

```
수진 (data) → 영지 (figure)
```

영지 figures depend on 수진's empirical results:
- ¶2 (수진): ρ(F,G) = −0.196 data
- ¶10-13 (수진): CFR theory variables
- ¶19-21 (수진): ARG theory variables

---

*Last updated: 2026-01-08*
