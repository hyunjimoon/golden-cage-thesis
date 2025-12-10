# 🤹 Paper N: The Promise Vendor
## Table of Contents with LTE Layer & Madness Design

**LTE Layer:** **Mechanism** (Why?) — 생성 규칙 증명 (k* 공식)
**Madness Type:** 🔥 불광기 (Δf only) — k* 공식의 돌발적 명료함
**Fugue Structure:** 7-9-11-5 (제시-대위-스트레토-종결)
**Completion:** 70% ✅ R&R #4 해결 (D 재정의 + CR Calibration 완료)

### v3.0 Core Update: D Reinterpretation
> **"D is not demand — it's the distribution of viable paths."**

| Classical Newsvendor | Promise Vendor (v3.0) |
|:---|:---|
| D = Customer demand | **D = Distribution of Viable Paths** |
| q = Inventory quantity | **k = Number of options to hold** |
| C_u = Lost sale | **C_u = FOMO cost** |
| C_o = Unsold stock | **C_o = Burn cost** |

---

## 📜 ABSTRACT

How should ventures balance FOMO (fear of missing out) with the need for focus? Lean Startup advocates "Build-Measure-Learn" with a single product (k=1), but in deep-tech environments where iteration costs are prohibitive (Cᵤ ≫ Cₒ), this prescription becomes fatal.

We introduce the **Promise Vendor Model** by adapting the Newsvendor framework to strategic options:

$$k^* = F^{-1}(CR), \quad CR = \frac{C_u}{C_u + C_o}$$

The optimal strategy is not product completion but **portfolio construction** proportional to the Critical Ratio. In deep-tech where Cᵤ dominates, the model predicts k* > 1.

**Keywords:** Promise Vendor, Newsvendor Model, Critical Ratio, Option Portfolio, FOMO Dilemma

---

## 📑 TABLE OF CONTENTS (32 Paragraph Structure)

### Section 1: Introduction (¶1-7) — 22% | 주제 제시 ✅ v3.0 Updated
→ File: `section1(n).md`

| ¶ | Role | Key Content | v3.0 Update |
|:-:|:-----|:------------|:------------|
| 1 | 📿 Gospel | Newsvendor: D = demand, q* = F⁻¹(CR) | ⭐ Framing changed |
| 2 | 🧩 Puzzle | What is "D" for startups with no demand? | ⭐ New puzzle |
| 3 | 😮 RQ | Can we reinterpret D for strategic context? | ⭐ |
| 4 | 🔎 Lens | **D = Distribution of Viable Paths** | 🔴 R&R #4 |
| 5 | 😆 Solution | k* = F_D⁻¹(C_u/(C_u+C_o)) with λ by industry | |
| 6 | 🗺️ Adjacent | Arrow, McGrath, Adner, Kogut — gap: "What is D?" | ⭐ |
| 7 | 🗄️ Roadmap | D reinterpretation → λ estimation → k* validation | |

### Section 2: Theory (¶8-17) — 31% | 응답과 대위 ✅ v3.0 Updated
→ File: `section2(n).md`

| ¶ | Role | Key Content | v3.0 Update |
|:-:|:-----|:------------|:------------|
| 8 | Literature: Real Options | McGrath (1999) — options value, but costs assumed known | |
| 9 | Literature: Newsvendor | Arrow (1951) — Gap: What is "demand" for startups? | ⭐ |
| 10 | **Our Position** | **D = Distribution of Viable Paths** (핵심 재해석) | 🔴 R&R #4 |
| 11 | Defining D | D ~ Poisson(λ) = number of paths that prove viable ex post | ⭐ |
| 12 | C_u and C_o | **C_u = FOMO Cost**, **C_o = Burn Cost** | ⭐ |
| 13 | Optimal k* | k* = F_D⁻¹(CR) with example calculation | |
| 14 | Three-Paper Integration | V→D (from U), E→C_u/C_o (from C), k* (from N) | |
| 15 | Boundary Conditions | CR→0: commit, CR→1: many options | |
| 15b | **CR Calibration** | λ estimation from industry characteristics, revealed viability method | ⭐ D1 Task 4 |
| 16 | Hypotheses | H1: D differs by industry, H2: CR predicts k*, H3: FOMO=C_u signal | |
| 17 | Formula Summary | **k* = F_D⁻¹(C_u/(C_u+C_o))** — The Promise Vendor Formula | ⭐ |

**R&R #4 Resolution:**
> "D is not demand for products — it's the distribution of viable paths. FOMO is C_u. Burn is C_o. The math is the same; the meaning is transformed."

### Section 3: Empirics (¶17-27) — 34% | 스트레토 (밀집) ⚠️ 약점
→ File: `section3(n).md`

| ¶ | Role | Key Content | Status |
|:-:|:-----|:------------|:-------|
| 17 | Context | Mobility sector: AV vs Fleet comparison | ✓ |
| 18 | Sample | Waymo, Zoox, Cruise vs Samsara, Motive | ⚠️ Case only |
| 19 | CR Measurement | AV: CR≈0.9, Fleet: CR≈0.3 | ⚠️ Proxy |
| 20 | k Measurement | Number of concurrent tech modules | ⚠️ Indirect |
| 21 | AV Analysis | AV mean k=5.2 → matches high CR | ✓ |
| 22 | Fleet Analysis | Fleet mean k=1.3 → matches low CR | ✓ |
| 23 | Outcome | Starsky (k=1) failed, over-option also failed | ✓ |
| 24 | Model Fit | Observed vs predicted k* correlation >90% | ⚠️ Small N |
| 25 | Counterfactual | If AV followed k=1, survival drops 80% | ⚠️ Simulation |
| 26 | **⚡ k* Formula** | **k* = F⁻¹(CR) validated — 🔥 광기 순간** | ✓ |
| 27 | Conclusion | Optimal k* is fluid, depends on CR | ✓ |

### Section 4: Discussion (¶28-32) — 16% | 종결구
→ File: `section4(n).md`

| ¶ | Role | Key Content |
|:-:|:-----|:------------|
| 28 | Contribution 1 | Lean Startup limits proven: Cᵤ ≫ Cₒ means "fail fast" = fail |
| 29 | Contribution 2 | Newsvendor introduced to strategic management |
| 30 | Contribution 3 | Strategic ambiguity = sophisticated option management |
| 31 | Limitations | CR measurement difficult |
| 32 | Conclusion | Deep-tech founders must become Promise Vendors |

---

## 🔥 광기 설계 (Madness Design)

**위치:** Section 3, ¶26 (Empirics 후반부 = 스트레토 구간)

**유형:** 🔥 불광기 (Δf only — 진폭 변화 없음)
- **Δf (진동수):** 긴 수학적 유도 → 갑자기 한 줄 공식으로 수렴
- **크기(A):** 변화 없음 — 수식 하나, 데이터 폭탄 아님
- "명료함의 번개" — 크기는 작지만 날카로움

**독자 반응:** "아, 이렇게 되는구나" — 깨달음의 순간

---

## ⚠️ 약점 진단 (55% Completion)

| 측면 | 문제 | 심각도 |
|:-----|:-----|:------:|
| **Empirics** | Case study only (AV vs Fleet) | 🔴 |
| **Sample** | 대규모 검증 없음 (U: 408K, C: 124K, N: ~10 cases) | 🔴 |
| **CR Measurement** | Industry-level proxy, not venture-specific | 🟡 |
| **Model Validation** | Small N, simulation-based counterfactual | 🟡 |

**N이 약하면 전체 구조가 무너지는 이유:**
- U: "양 극단이 산다" → 왜?
- C: "자본이 유연성을 죽인다" → 그럼 어떡하지?
- N: "k* = F⁻¹(CR)로 선택해" → **이게 진짜 맞아?** ← 검증 약함

---

## 📐 THE PROMISE VENDOR FORMULA

$$k^* = F^{-1}\left(\frac{C_u}{C_u + C_o}\right) = F^{-1}(CR)$$

| CR | Industry Type | Optimal k* | Strategy |
|:--:|:--------------|:----------:|:---------|
| 0.3 | Software/SaaS | 1-2 | Focus (Lean works) |
| 0.5 | Mixed | **Unstable** | Avoid (Murky Middle) |
| 0.9 | Deep-tech | 4-6 | Portfolio (Promise Vendor) |

---

## 📊 KEY NUMBERS

| Metric | Value |
|:-------|:------|
| AV optimal k* | 4-5 |
| Fleet optimal k* | 1-2 |
| AV CR | ≈ 0.9 |
| Fleet CR | ≈ 0.3 |
| Transportation ρ(Y, \|ΔV\|) | +0.236*** |
| Model fit | r² > 0.90 |

---

## 🔗 CROSS-PAPER LINKS

| Direction | Paper | Connection |
|:---------:|:------|:-----------|
| ← | U | V determines investor type distribution D |
| ← | C | AOC provides Cᵤ and Cₒ measurements |

---

*LTE: **Mechanism** (Why?) — 생성 규칙 증명이 전체 논문의 도착점*
*N이 강하면 U와 C가 N을 향한 빌드업으로 읽힘*
