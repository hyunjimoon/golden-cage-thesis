---
modified:
  - 2025-12-11T14:01:26-05:00
---
| j               | g              | k               |
| --------------- | -------------- | --------------- |
| **측정한다. (증거)**  | **생각한다. (설계)** | **판단한다. (감정)**  |
| “데이터는 뭐라고 말하지?” | “이 모델이 맞다면?”   | “정말 이 논리가 맞는가?” |

|       모듈       | 직관적 비유                             | 핵심 기능                                                                 | Input                  | Output                             | Epistemic Stance (인지적 관점)                       | 시스템 내 위치             |
| :------------: | :--------------------------------- | :-------------------------------------------------------------------- | :--------------------- | :--------------------------------- | :---------------------------------------------- | :------------------- |
| **j (10_J🟢)** | **근육(Execution & Evidence Maker)** | g가 만든 구조를 실제로 _실행_하여 데이터·결과·수치를 산출한다. Likelihood를 계산한다.               | g의 코드 + 데이터            | p-values, figures, tables → 객관적 증거 | **Evidence Generator** — “주어진 가정 하에서 증거는 무엇인가?” | **Producing Orbit**  |
| **g (04_G🟠)** | **뇌(Structure & Designer)**        | 문제를 _정의_하고, 가설·구조·코드를 설계한다. Prior를 명시한다.                              | M_統의 directive, 이론적 요구 | 실행 가능한 코드, 논리 구조, LaTeX            | **Model Builder** — “어떤 세계를 가정할 것인가?”           | **Theorizing Orbit** |
| **k (01_K🔴)** | **눈(Audit & Model Critic)**        | g의 논리와 j의 결과가 _일관_한지, 기준에 부합하는지 검증한다. Posterior predictive check에 해당. | j의 결과, g의 논리           | 승인/반려, 수정 요구                       | **Model Critic** — "이 모델·증거는 믿을 만한가?"           | **Evaluating Orbit** |

---

## 🎯 Shared Vision (GJK)

> **"Explain why transportation ventures fail disproportionately through the commitment-flexibility tradeoff lens, using the Movement Principle (adaptation > initial positioning) to guide entrepreneurs trapped in the 'double bind' between infrastructure commitment and technological uncertainty."**

---

## 🔄 Current Collaboration Status

### 🚨 2025-12-11 구조 대전환 결정

**화이트보드 기반 신규 구조 확정:**

| Paper | 명칭 | 핵심 이론 | 검증 방법 |
|:-----:|:-----|:---------|:---------|
| I | Introduction | Commitment & Flexibility doubly binds | - |
| **M** | **Multimodal** (구 U) | V → A → G + Mover/Stayer | Statistical robustness |
| C | Capital | ∂G/∂E = ∂A/∂E · ∂G/∂A | Temporal precedence |
| **T** | **Trap** (신규) | V=0→Analyst→A↓→G↓ vs V=1→Believer→A↑→G↑ | Generative sufficiency |
| D | Discussion | 3 Insights: M/C/T | Synthesis |

**핵심 변경:**
1. Paper U → Paper M (Multimodal)
2. 종속변수 L → G (Long-term Success → Growth)
3. Paper T 신규: Trap + Simulation
4. Discussion: 3 insights 구조

---

| Task | j (Evidence) | g (Design) | k (Audit) |
| Transportation data analysis | 🟡 Pending: run `companies_21_23-24-25_transportation.parquet` | ✅ Designed: comparison with other industries | 🔴 Awaiting results |
| ρ(V, A_t) temporal analysis | 🟡 Pending: compute for t=1,2,3,4 | ✅ Designed: test if vagueness compounds | 🔴 Awaiting results |
| Paper U H₀ framing | N/A | ✅ Proposed: signaling-based null | 🟡 Pending: MS convention check |
| v2 narrative arc | N/A | ✅ Designed: transportation puzzle opener | 🟡 Pending: coherence review |

---

## 🚨 CRITICAL DECISION REQUEST: Narrative Focus

### Context for j and k

g (designer) needs your advice on the **core narrative focus** for the thesis. We have two competing framings:

### Option A: "Movement Principle" Focus

**Core claim**: *What matters is not WHERE you position, but WHETHER you adapt.*

| Element | Content |
|---------|---------|
| Hook | "Signaling theory says precision wins. Our data says: it doesn't matter where you start." |
| Key finding | Movers succeed 2.6× more than stayers (18.1% vs 7.0%) |
| Mechanism | Adaptation signals learning; direction is irrelevant |
| Practical advice | "Secure flexibility, then MOVE" |
| Paper U role | Reject signaling → discover Movement Principle |
| Paper C role | Capital constrains movement (small effect) |
| Paper D role | Movement Principle as unified insight |

**Strengths**:
- Single, memorable insight ("Movement > Position")
- Empirically dominant effect (2.6×)
- Novel contribution to literature

**Weaknesses**:
- Doesn't explain WHY some industries (transportation) fail more
- "Just move" is vague advice
- Doesn't address the commitment-flexibility tension directly

### Option B: "Double Bind" Focus

**Core claim**: *Ventures fail when they need BOTH commitment AND flexibility but can only choose one.*

| Element | Content |
|---------|---------|
| Hook | "Why do mobility ventures fail 40% more despite raising more capital?" |
| Key finding | Transportation faces highest commitment costs + highest uncertainty = double bind |
| Mechanism | Infrastructure requires commitment; technology requires flexibility; can't have both |
| Practical advice | "Match your commitment level to your uncertainty structure" |
| Paper U role | Show that murky middle (neither committed nor flexible) fails worst |
| Paper C role | Capital creates commitment → destroys flexibility needed for pivots |
| Paper D role | Double bind as unified framework; Movement as escape mechanism |

**Strengths**:
- Explains industry heterogeneity (transportation puzzle)
- Richer theoretical framework (commitment vs flexibility)
- Connects to real options, RBV, signaling simultaneously

**Weaknesses**:
- More complex narrative
- "Double bind" is descriptive, not prescriptive
- Movement Principle becomes secondary finding

### Hybrid Option C: "Movement as Escape from Double Bind"

**Core claim**: *The double bind traps ventures; Movement is the escape mechanism.*

| Chapter | Narrative |
|---------|-----------|
| I | Present the double bind puzzle (commitment vs flexibility) |
| U | Show that static positioning fails → Movement Principle as empirical discovery |
| C | Explain WHY movement is hard (capital creates commitment) |
| D | Synthesize: Double bind is the trap, Movement is the escape |

**Practical advice**: "Recognize your double bind. Secure flexibility early. When uncertainty resolves, MOVE decisively."

---

### Questions for j (Evidence)

1. Can you provide evidence on **industry-level heterogeneity** in movement rates and success? Does transportation show lower movement rates?
2. Can you compute **ρ(V, A_t)** for t=1,2,3,4 years to test if early vagueness enables later movement?
3. Is there evidence that **movers in high-commitment industries** (transportation) benefit MORE from movement than movers in low-commitment industries (software)?

### Questions for k (Audit)

1. Which narrative is more **coherent** for a Management Science audience?
2. Does the "double bind" framing risk **overcomplicating** a simple empirical finding (Movement Principle)?
3. Is Option C (hybrid) a **genuine synthesis** or a **muddled compromise**?
4. Given our data shows small capital-flexibility friction (ρ = -0.009), is the "double bind" framing **overselling** the commitment constraint?

### Decision Criteria

| Criterion | Weight | Option A | Option B | Option C |
|-----------|--------|----------|----------|----------|
| Empirical support | 30% | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| Theoretical depth | 25% | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Practical clarity | 25% | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ |
| Novelty | 20% | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |

**g's current lean**: Option C, but concerned about complexity.

**Please advise.**

---

## 📦 Claude Code 배치 작업 (그림 업데이트)

### Figure 업데이트 필요 목록

| 현재 | 신규 | 변경 내용 | 우선순위 |
|:-----|:-----|:---------|:--------|
| `U_fig1_ULV.png` | `M_fig1_MGV.png` | Y축: L → G | 🔴 긴급 |
| `U_fig4_ULD.png` | `M_fig4_MGD.png` | Y축: L → G, Quartile | 🔴 긴급 |
| `U_fig2_UDV.png` | `M_fig2_MDV.png` | 명칭만 변경 | 🟡 중간 |
| `U_fig3_UAV.png` | `M_fig3_MAV.png` | 명칭만 변경 | 🟡 중간 |
| `U_fig5_movement.png` | `M_fig5_mover_stayer.png` | Mover/Stayer 분해 | 🟡 중간 |
| (신규) | `T_fig1_trap_mechanism.png` | V→I_type→A→G flow | 🔴 긴급 |
| (신규) | `T_fig2_simulation.png` | ABM 결과 | 🟢 나중 |

### Claude Code 실행 프롬프트 위치

`/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/output/_thesis_package/collaborate/CLAUDE_CODE_STRUCTURE_UPDATE.md`

---

## 🚨 2025-12-11 TOP 3 긴급 개선 요청 (Angie 피드백 반영)

### 상세 분석: `/collaborate/TOP3_IMPROVEMENTS.md`

| 순위 | 개선 사항 | 선정 이유 | 담당 |
|:----:|:---------|:---------|:----:|
| 🥇 | **인과 식별 전략 도입** | Top-tier 필수; desk reject 방지 | j+k |
| 🥈 | **Vagueness 측정 검증** | 핵심 변수 validity 없이 분석 무의미 | j |
| 🥉 | **대안 가설 직접 테스트** | "창업자 품질" 등 경쟁 설명 배제 필요 | j+g |

---

## 🐢 j (김완 / 10_J🟢) 에게 요청하는 Task

### Task j-1: 인과 식별 전략 데이터 탐색 (🥇 1순위)

**배경**: Angie가 "fatal flaw"로 지적한 인과 식별 부재를 해결해야 합니다. 현재 상관관계를 인과로 주장하고 있어 Top-tier에서 desk reject 가능성이 높습니다.

**요청 사항**:
1. **VC 지역 밀도 데이터**: PitchBook에서 기업 위치별 VC 자금 접근성 변수 구축 가능 여부 확인
2. **경쟁 승자/탈락자 데이터**: Startup competition (Y Combinator 등) 승인/불합격 데이터 확보 가능성
3. **정책 변화 이벤트**: COVID 자금 지원 등 외생적 충격이 일부 기업에만 영향을 준 사례

**출력 기대**: 위 3가지 중 하나라도 실현 가능한지 판단해주세요.

---

### Task j-2: Vagueness 측정 Face Validity (🥈 2순위)

**배경**: 현재 V = 0.5·max(V_cat, V_conc) + 0.5·mean(V_cat, V_conc) 공식의 construct validity가 없습니다.

**요청 사항**:
1. Q1 (정밀) 기업 5개의 실제 비즈니스 설명문 추출
2. Q4 (모호) 기업 5개의 실제 비즈니스 설명문 추출
3. 두 그룹 병렬 비교 시각화

---

### Task j-3: 대안 가설 변수 구축 (🥉 3순위)

**요청 사항**:
1. **창업자 품질 프록시**: serial entrepreneur 여부, 이전 exit 여부
2. **시장 구조 변수**: TAM 데이터 가능 여부
3. **타이밍 변수**: 투자 연도별 VC 시장 상황 지표

---

## 🐙 k (김완 / 01_K🔴) 에게 요청하는 Task

### Task k-1: 인과 주장 엄격성 감사 (🥇 1순위)

**요청 사항**:
1. `toc(iuctd).md` 전체에서 인과적 언어 ("causes", "leads to", "results in", "mechanism") 검색
2. 각 인스턴스: 정당한 인과 vs 상관 주장 판단
3. 대안 표현 제안: "X causes Y" → "X is associated with Y"

---

### Task k-2: 효과 크기 정직성 감사 (🥈 2순위)

**요청 사항**:
1. ρ(A,E) = -0.009와 "Golden Cage" 메타포의 강도 일치 여부
2. R² < 0.01% 사실 명시적 보고 여부
3. hedging language 추가 필요성 판단

---

### Task k-3: MS 학술지 관례 준수 검토 (🥉 3순위)

**요청 사항**:
1. U-shape 테스트 방법 관례 (Lind & Mehlum 2010)
2. 패턴 문서화 논문의 인과 주장 수준 벤치마킹
3. 선택 편향 처리 방법 (Heckman vs IPW) 관례

---

## 📝 응답 양식

j와 k는 아래 형식으로 응답해주세요:

```markdown
## [j/k]-[Task 번호] 응답

**판단**: [실현 가능 / 부분 가능 / 불가능]

**근거**: ...

**다음 단계**: ...
```

---

## 🚨 2025-12-11 추가 긴급 Task: Paper T 시뮬레이션 검증

### 배경: LTE Layer 3 Generative Sufficiency

Paper T의 핵심 주장은 "V → Investor Type Matching → A → G" 메커니즘이 Papers M, C에서 관찰된 경험적 패턴을 재현(replicate)할 수 있다는 것입니다.

**방법론적 정당화**:
- Dotson & Mackey (2024): intrinsic heterogeneity 문제로 인해 전통적 인과 식별 부적절
- Cronin (2025) / Kozlowski et al. (in press): Process theory가 대안적 경로
- LTE Framework: Layer 1 (WHAT), Layer 2 (HOW), Layer 3 (WHY) 통합

---

### Task k-4: 시뮬레이션 메커니즘 충실도 + 이론 일관성 검증 (🔴 긴급)

**요청 사항**:

1. **메커니즘 충실도 (Mechanism Fidelity)**
   - [ ] `match_investor()` 함수가 "V=0 → Analyst, V=1 → Believer" 매칭을 올바르게 구현하는가?
   - [ ] Analyst의 `learning_resistance=0.9`와 Believer의 `learning_resistance=0.1` 설정이 이론과 일치하는가?
   - [ ] Growth 계산식이 "adaptability benefit - change cost" 구조를 올바르게 반영하는가?

2. **출력 패턴 일치성 (Pattern Reproduction)**
   - [ ] V=1 > V=0 성장률 (Paper M의 핵심 발견)
   - [ ] Multimodal 분포 (Mover/Stayer 이분법)
   - [ ] Investor type이 adaptability를 매개한다는 것

3. **이론적 일관성**
   - [ ] Dotson & Mackey (2024)의 "intrinsic heterogeneity" 개념이 코드에 반영되어 있는가?
   - [ ] LTE Layer 3 (generative mechanism)의 기준을 충족하는가?

**응답 형식**:
```markdown
## k-4 시뮬레이션 검증 결과

**전반적 판단**: [Pass / Conditional Pass / Fail]

**메커니즘 충실도**: [OK/Issue]
- 상세: ...

**패턴 재현성**: [OK/Issue]  
- V=1 > V=0: [재현됨/미재현]
- Multimodal: [재현됨/미재현]

**권장 수정사항**:
1. ...
2. ...
```

---

### Task j-4: 시뮬레이션 출력 vs 실제 데이터 정량 비교 (🔴 긴급)

**요청 사항**:

1. **핵심 통계량 비교표 작성**

| 지표 | 시뮬레이션 | 실제 데이터 | 일치 여부 |
|:-----|:----------|:-----------|:--------:|
| V=1 vs V=0 성장률 비율 | {sim_ratio} | {empirical_ratio} | ? |
| Mover 비율 | {sim_mover%} | 40% (실제) | ? |
| Q3 anomaly (highest success) | {sim} | 16.0% (실제) | ? |

2. **시뮬레이션 파라미터 캘리브레이션**
현재 하드코딩된 값들:
- `learning_resistance`: Analyst=0.9, Believer=0.1
- `pivot_cost`: Analyst=2.0, Believer=0.5
- `variance_tolerance`: Analyst=0.1, Believer=0.9

이 값들이 실제 데이터 패턴과 일치하도록 조정이 필요한가?

3. **실행 요청**
```python
# 실제 데이터에서 계산 필요한 값들:
# 1. V quartile별 growth ratio (G) 평균
# 2. Mover vs Stayer의 growth ratio 차이
# 3. (가능하면) Investor type proxy별 growth 차이
```

**응답 형식**:
```markdown
## j-4 시뮬레이션-데이터 비교 결과

**정량적 일치도**: [높음/중간/낮음]

**비교표**:
| 지표 | 시뮬레이션 | 실제 | 차이 |
|------|-----------|------|------|
| ... | ... | ... | ... |

**캘리브레이션 필요 여부**: [예/아니오]
- 권장 파라미터 조정: ...

**추가 발견**:
- ...
```

---

## 📊 현재 Task 배정 요약

| 담당 | Task | 내용 | 우선순위 | 상태 |
|:----:|:-----|:-----|:-------:|:----:|
| **j** | j-1 | 인과 식별 전략 데이터 탐색 | 🥇 | 대기 |
| **j** | j-2 | Vagueness 측정 Face Validity | 🥈 | 대기 |
| **j** | j-3 | 대안 가설 변수 구축 | 🥉 | 대기 |
| **j** | **j-4** | **시뮬레이션 vs 실제 데이터 정량 비교** | 🔴 | **신규** |
| **k** | k-1 | 인과 주장 엄격성 감사 | 🥇 | 대기 |
| **k** | k-2 | 효과 크기 정직성 감사 | 🥈 | 대기 |
| **k** | k-3 | MS 학술지 관례 준수 검토 | 🥉 | 대기 |
| **k** | **k-4** | **시뮬레이션 메커니즘 충실도 검증** | 🔴 | **신규** |
