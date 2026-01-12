---
collection:
  - "[[Space/Lab/Papers]]"
author_ids:
  - ChatGPT
  - Gemini Deep Research
field:
  - entrepreneurship
  - strategy
  - methodology
year: 2026
created: 2026-01-11
modified:
  - 2026-01-11T15:38:01-05:00
journal: LLM Research Report
---

## 📍 Provenance (출처 기록)

> **Source Prompts**: [[롤모델논문_현상수배]]
> **경로**: `/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/output/_🩸I/[[롤모델논문_현상수배.md`
> **생성일**: 2026-01-11
>
> 이 문서는 `롤모델논문_현상수배.md`의 **Charles Fine 관점 프롬프트**를 ChatGPT와 Gemini에게 전달하여 생성된 결과물입니다.
> - ChatGPT 프롬프트: Semantic/Structural Focus (competing mechanisms, engagement techniques)
> - Gemini 프롬프트: Syntax/Flow Focus (sentence-level craft, paragraph transitions)

---

## 🔬 Intro 해부 (Posen-Cachon Framework)

### 📌 Prior 설정 (X): "논문 템플릿 선정은 직관적으로"
> "Researchers typically select template papers based on familiarity, advisor recommendations, or citation counts, without systematic evaluation."

### 📌 Puzzle 제시 (Y): 어떤 템플릿이 Golden Cage thesis에 최적인가?
> "With hundreds of potential templates in entrepreneurship, strategy, and VC governance literature, how do we identify papers that best match our specific theoretical mechanism and empirical approach?"

### 📌 새 렌즈 제시 (Z): 다차원 평가 프레임워크
> "We apply a 4-criterion evaluation (structural clarity, methodological rigor, Golden Cage connection, feasibility) across ChatGPT and Gemini recommendations to identify Top 3 templates."

---

## 📊 핵심 Framework

### Evaluation Criteria (5-point scale)

| 기준 | 정의 | 가중치 |
|:----|:----|:------:|
| **구조적 명확성** | 서론 훅, H0 vs H1, 결과 제시의 논리 흐름 | 25% |
| **방법론적 엄밀성** | 인과 식별, 대안 설명 방어, 강건성 검증 | 25% |
| **Golden Cage 연결성** | thesis 핵심 메커니즘과의 직접 관련성 | 30% |
| **실행 가능성** | 데이터/방법론 모방 가능성 | 20% |

### ChatGPT vs Gemini 비교

```
ChatGPT 특성:
├── 실용적 프레이밍: "What to extract and emulate"
├── 중간 깊이 (~300단어/논문)
├── 직접 매칭: 각 논문 → thesis chapter 연결
└── 약점: Paper C(텍스트 분석) 추천 부재

Gemini 특성:
├── 이론적 프레이밍: Charles Fine's Clockspeed 적용
├── 깊은 분석 (~1000단어/논문)
├── 방법론 상세: 코사인 유사도 공식, LLM 사전 구축
├── 진화적 서사: 1세대(린) → 2세대(과학적 창업)
└── 약점: 과도한 분량, 실행 지침 상대적 부족
```

---

## 📐 Top 3 Template Papers 선정

### 🥇 1위: Ewens, Nanda, & Rhodes-Kropf (2018)

**"Cost of Experimentation and the Evolution of Venture Capital"** — JFE

| 기준 | 점수 | 근거 |
|:----|:----:|:----|
| 구조적 명확성 | 5 | 기술 충격 → 비용 변화 → 거버넌스 변화 |
| 방법론적 엄밀성 | 5 | Diff-in-Diff, AWS 충격 활용 |
| Golden Cage 연결성 | 5 | **직접 연결**: 실험 비용 ↔ 거버넌스 경직성 |
| 실행 가능성 | 4 | PitchBook 데이터로 재현 가능 |
| **총점** | **4.75** | |

**선정 이유:**
1. Golden Cage 메커니즘과 **직접 연결**: 실험 비용 ↔ 거버넌스 경직성
2. Diff-in-Diff 설계가 PitchBook 분석에 직접 적용 가능
3. "기술 충격 → 조직 행동 변화"의 논리가 연구와 동형

### 🥈 2위: Jin & McElheran (2025)

**"Economies Before Scale: IT Strategy and Performance Dynamics"** — ManSci

| 기준 | 점수 | 근거 |
|:----|:----:|:----|
| 구조적 명확성 | 5 | Commitment vs Flexibility 직접 프레이밍 |
| 방법론적 엄밀성 | 5 | 100,000+ 기업 패널, 다중 강건성 검증 |
| Golden Cage 연결성 | 5 | **직접 연결**: "조기 헌신이 성장 억제" |
| 실행 가능성 | 4 | 대규모 데이터 필요 |
| **총점** | **4.75** | |

**선정 이유:**
1. Commitment vs Flexibility를 **정확히** Golden Cage 프레이밍으로 분석
2. "조기 헌신이 초기 5년간 생존을 해친다" = Golden Cage 실증
3. N=100,000+ ≈ thesis N=180,994와 유사 규모

### 🥉 3위: Valentine, Novelli, & Agarwal (2024)

**"The Theory-Based View and Strategic Pivots"** — Strategy Science

| 기준 | 점수 | 근거 |
|:----|:----:|:----|
| 구조적 명확성 | 5 | 이론화 + 실험 = 성과 |
| 방법론적 엄밀성 | 5 | LLM 기반 사전, 코사인 유사도 |
| Golden Cage 연결성 | 4 | 피벗의 인지적 차원 — 간접 연결 |
| 실행 가능성 | 4 | 최신 기법, 구현 복잡 |
| **총점** | **4.50** | |

**선정 이유:**
1. 피벗을 "인지적 신념 수정"으로 재정의 — repositioning 측정 이론적 근거
2. LLM 기반 텍스트 분석 방법론 = 최신 표준
3. 이론화(Theorization) + 실험(Experimentation) 분리 ↔ A(Flexibility)와 R(Repositioning) 구분

---

## 🎯 For Your Thesis: Chapter별 템플릿 매핑

| Chapter | 1순위 템플릿 | 2순위 템플릿 |
|:--------|:-----------|:-----------|
| **Ch.1 Introduction** | Guzman & Stern (2020) | Jin & McElheran (2025) |
| **Ch.2 Theory & Hypotheses** | Jin & McElheran (2025) | Valentine et al. (2024) |
| **Ch.3 Empirical Strategy** | Ewens et al. (2018) | Menon et al. (2021) |
| **Ch.4 Results** | Ewens et al. (2018) | Camuffo et al. (2020) |
| **Ch.5 Discussion** | Jin & McElheran (2025) | Nanda & Rhodes-Kropf (2017) |

---

## 📐 종합 평가

| 차원 | ChatGPT | Gemini | 승자 |
|:----|:-------|:-------|:----:|
| 실용성 | ⭐⭐⭐⭐ | ⭐⭐⭐ | ChatGPT |
| 이론적 깊이 | ⭐⭐ | ⭐⭐⭐⭐⭐ | Gemini |
| 방법론 상세 | ⭐⭐ | ⭐⭐⭐⭐⭐ | Gemini |
| Golden Cage 연결 | ⭐⭐⭐ | ⭐⭐⭐⭐ | Gemini |
| **종합** | — | — | **Gemini** |

**결론:** Gemini가 이론적 통합과 방법론 상세에서 우위. 실행 시 ChatGPT의 "extract and emulate" 접근법 결합이 최적.

---

## 🔗 Key Literature Links

- [[📜ewens18_cost(experimentation, vc)]] — Cost of experimentation
- [[📜jin24_economies(scale, IT)]] — Economies before scale
- [[📜valentine24_tbv(pivot, theorization)]] — Theory-based view of pivots
- [[📜guzman20_entrepreneurship(quality, quantity)]] — Entrepreneurial quality
- [[📜camuffo20_scientific(entrepreneurship)]] — Scientific approach

---

## 📖 Citation

> ChatGPT & Gemini Deep Research. (2026). Synthesis Report: Template Paper Recommendations for Golden Cage Thesis. *LLM Research Report*.

**Methodology:**
- ChatGPT: Practical extraction framework
- Gemini: Charles Fine's Clockspeed + Methodological depth
- Synthesis: 4-criterion weighted evaluation
