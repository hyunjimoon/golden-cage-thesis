---
modified:
  - 2026-01-09T11:00:20-05:00
  - 2026-01-09T17:27:03-05:00
  - 2026-01-10T20:37:27-05:00
  - 2026-01-11T08:33:43-05:00
  - 2026-01-11T15:30:00-05:00
  - 2026-01-13T08:20:00-05:00
---
[[Thesis_Master]]

# Action Items: Final Integration Plan (v4.0)

> **Goal**: RoT 95% (Peer Review 100% Integration)
> **Sources**: Self Feedback, Lorry & Eze Feedback, Database Examples
> **Status**: Emergency Martial Law - Immediate Execution
> **Current**: RoT 87% (2026-01-13)

---

## 📋 NEW ISSUE TEMPLATE

새 Issue 생성 시 반드시 아래 형식 사용:

```markdown
## Issue #XXX: [제목]

### Original Intent (왜 만드나?)
> [한 문장으로 핵심 문제 — 이게 해결 안 되면 DONE 불가]

### Acceptance Test (언제 DONE인가?)
- [ ] 조건 1: [구체적 확인 항목]
- [ ] 조건 2: [구체적 확인 항목]

### Verification Question (Scott Stern & Charlie Fine의 질문)
> "_____ 가 _____ 되었는가?"
```

**예시:**
```markdown
## Issue #055: Survival Bias Defense

### Original Intent
> "성공한 Mover가 일찍 exit해서 우리 패턴이 편향됐다는 공격 방어"

### Acceptance Test
- [ ] Year 3+ 조건부 분석 결과가 Section 4.5.2에 삽입됨
- [ ] Mover Advantage가 여전히 유의함 (p < 0.05)
- [ ] 2-3 paragraphs 작성 완료

### Verification Question
> "Year 3+ 생존 벤처만 봐도 Mover가 여전히 Stayer보다 유리한가?"
```

---

## CLI DIVISION OF LABOR

| Agent | Role | Issues | Focus |
|:------|:-----|:-------|:------|
| **CLI1** | Logic & Structure | #043-#048 | Theory, Mechanisms, Identification |
| **CLI2** | Narrative & Polish | #049-#054 | Examples, Word Choice, Figures |

### CLI1 Queue (Logic)
1. #043 Pattern vs Mechanism Re-org (Ch.2/Ch.3)
2. #044 Causality Control & H0
3. #045 Alternative Explanations
4. #046 Deep Tech & Commitment Types
5. #047 Measurement Validity (Breadth)
6. #048 Data Transparency (Figure 4)

### CLI2 Queue (Narrative)
1. #049 Example Extraction (Sky Engine, Surestar, Narrowing Mover)
2. #050 Concrete Governance Levers
3. #051 Word Choice Sweep (Paradox restriction)
4. #052 Figure Consistency Check
5. #053 Linpowave Replacement
6. #054 Academic Tone Polish

---

## MASTER ISSUE TRACKER

> **⚠️ 커밋 전 필수 확인**: "Original Intent" 컬럼을 읽고, 이 의도가 해결되었는지 자문하세요.

| # | Issue | Original Intent (왜 만들었나?) | TIER | Status | Owner |
|:--|:------|:------------------------------|:----:|:------:|:-----:|
| #028 | Qualified Movement Definition | "R > median은 arbitrary → R > 0으로 바꿔야" | 0 | DONE | - |
| #030 | Robustness Graph | "2020-2025에도 패턴이 유지되는지 확인" | 0 | DONE | - |
| #041 | Magnitude Contextualization | "ρ=-0.196이 실제로 뭘 의미하는가? 4-6%/SD" | 1 | DONE | CLI1 |
| #042 | Industry Heterogeneity Table | "산업별 차이를 한눈에 보여주는 표" | 0 | DONE | - |
| #043 | Pattern vs Mechanism Re-org | "Ch.2=패턴, Ch.3=메커니즘으로 분리" | 1 | DONE | CLI1 |
| #044 | Causality Control & H0 | "인과 언어 위험 → associative 동사로" | 0 | DONE | CLI1 |
| #045 | Alternative Explanations | "Moral Hazard 등 대안 설명 방어" | 1 | DONE | CLI1 |
| #046 | Deep Tech & Commitment Types | "Quantum 예외 + Staged vs Partial 구분" | 1 | DONE | CLI1 |
| #047 | Measurement Validity | "Breadth(B)가 마케팅 허풍 아닌지 검증" | 0 | DONE | CLI1 |
| #048 | Data Transparency | "Figure 4 플레이스홀더 채우기" | 0 | DONE | CLI1 |
| #049 | Example Extraction | "Sky Engine, Surestar 등 구체적 사례" | 2 | DONE | CLI2 |
| #050 | Concrete Governance Levers | "Preserve Skeptics를 어떻게 실행하나?" | 2 | DONE | CLI2 |
| #051 | Word Choice Sweep | "Movement→Repositioning, Paradox 제한" | 3 | DONE | CLI2 |
| #052 | Figure Consistency | "그래프 스타일 통일 (grayscale)" | 3 | DONE | - |
| #053 | Linpowave Replacement | "G=N/A인 Linpowave 대체 사례 찾기" | 2 | DONE | CLI2 |
| #054 | Academic Tone Polish | "과장된 표현 제거, 학술적 톤" | 3 | DONE | CLI2 |

---

## TIER 0: CRITICAL DEFENSE

### **#044: Causality Control & H0 [P0]**
> *Source: Lorry #1*
- **Gap:** Causal language risk.
- **Owner:** CLI1
- **Action:**
  - **Estimand:** Insert: "I document a robust correlational pattern... consistent with a mechanism."
  - **H0:** Explicitly state Null Hypothesis (Resources -> Growth).
  - **Word Sweep:** Replace `suppresses`/`drives` with associative verbs.

### **#047: Measurement Validity (Breadth) [P0]**
> *Source: Lorry #3*
- **Gap:** Is $B$ just marketing fluff?
- **Owner:** CLI1
- **Action:**
  - **Cross-Validation:** Validate text-based Breadth ($B$) against observable non-text signals (Product Category changes, Tech Tags, Customer Segment shifts).

### **#048: Data Transparency [P0]**
> *Source: Self*
- **Owner:** CLI1
- **Action:**
  - **Figure 4:** Fill the placeholder (Initial DB -> US HQ -> Sample).
  - **Cleanup:** Remove empty 3.2.2. Verify "US Headquartered" filter in code.

---

## TIER 1: LOGIC & STRUCTURE

### **#043: Pattern vs Mechanism Re-org [P1]**
> *Source: User Instruction #5*
- **Owner:** CLI1
- **Action:**
  - **Chapter 2 (Theory):** Focus on Observed Patterns (**EG, ER, RG**).
  - **Chapter 3 (ID):** Focus on Causal Mechanisms (**CEF**: C -> E -> F, **FG**: F -> G).
  - **Figure 2 Update:** Map Latent vs Measured variables to this structure.

### **#045: Alternative Explanations [P1]**
> *Source: Lorry #2*
- **Owner:** CLI1
- **Action:**
  - Compare "Governance Homogeneity" against **Milestone Pressure**, **Burn-rate Discipline**, **Moral Hazard**.
  - Show why data patterns favor Homogeneity.

### **#046: Deep Tech & Commitment Types [P1]**
> *Source: Eze #1, #2, #3, #4*
- **Owner:** CLI1
- **Action:**
  - **Deep Tech:** Add "Chicago Booth Approach" (Non-dilutive funding/Grants) as a survival strategy for Quantum/Deep Tech in Ch.4.
  - **Commitment Distinction:** Contrast **"Staged Commitment"** (Milestone-based, Signal up) vs **"Partial Commitment"** (Low interest, Signal down).

### **#041: Magnitude Contextualization [P1]**
> *Source: TR-01*
- **Owner:** CLI1
- **Action:**
  - Calculate effect size in practical terms (4-6% per SD).
  - Benchmark against comparable studies (accelerator impact ~5%).
  - Add contextualization to Abstract and Ch.4.

---

## TIER 2: EXAMPLES & PRESCRIPTION

### **#049: Illustrative Examples [P2]**
> *Source: Image Analysis + User Instruction #4*
- **Owner:** CLI2
- **Action:**
  - **Broadening Mover:** **Sky Engine** (V: 28 -> 89, G: 215x).
  - **Stayer:** **Surestar** (V: 87 -> 87, G: 26x).
  - **Narrowing Mover:** Find successful "Zoom-in" case in DB.

### **#050: Concrete Governance Levers [P2]**
> *Source: Lorry #5*
- **Owner:** CLI2
- **Action:**
  - Operationalize "Preserve Skeptics": Define via **Syndicate Composition**, **Board Structure**, and **Dissent-friendly Decision Rules**.

### **#053: Linpowave Replacement [P2]**
> *Source: Database check*
- **Owner:** CLI2
- **Action:**
  - Find replacement for Linpowave (G=N/A).
  - Criteria: Successful narrowing mover with G > 10x.

---

## TIER 3: POLISH & TERMINOLOGY

### **#051: Strict Word Choice [P3]**
> *Source: User Instruction #1*
- **Owner:** CLI2
- **Action:**
  - `Movement` -> **`Repositioning`** DONE
  - `Paradox` usage -> Restricted to **"Funding Paradox"** only. TODO
  - `Conviction Paradox` -> **"Caged Learning"** DONE
  - `Theorem 1 (Learning Trap)` -> **"Theorem 1 (Caged Learning)"** DONE

### **#052: Figure Consistency [P3]**
- **Status:** DONE
- Fig_growth_by_R.png updated to grayscale.

### **#054: Academic Tone Polish [P3]**
> *Source: #040*
- **Owner:** CLI2
- **Action:**
  - Remove unearned superlatives.
  - Ensure professional, measured language throughout.

---

## COMPLETED ITEMS

| # | Issue | Description | Completed |
|:--|:------|:------------|:---------:|
| **#028** | Qualified Movement Definition | R > 0 (was R > median) | 2026-01-13 |
| **#030** | Robustness Graph | Temporal stability verified | 2026-01-12 |
| **#042** | Industry Heterogeneity | Table 6 in thesis | 2026-01-12 |
| **#052** | Figure Consistency | Grayscale applied | 2026-01-13 |
| #051a | Movement -> Repositioning | Global replace | 2026-01-13 |
| #051b | Conviction Paradox -> Caged Learning | 2 occurrences | 2026-01-13 |
| #051c | Theorem 1 rename | Caged Learning | 2026-01-13 |
| #TR-02 | Survival Bias Defense | Year 3+ conditioning | 2026-01-13 |
| #TR-03 | Industry Universality | 6 sectors verified | 2026-01-12 |
| #TR-04 | Alternative Story (DGP) | Selection as mechanism | 2026-01-11 |

---

## PRIORITIZED QUEUE

### CLI1 (Logic) - Next Actions
1. **#044** Causality Control (Word sweep for causal language)
2. **#047** Breadth Validity (Cross-validation plan)
3. **#043** Ch.2/Ch.3 Re-org (Pattern vs Mechanism)
4. **#045** Alternative Explanations (vs Moral Hazard)
5. **#046** Deep Tech (Staged vs Partial Commitment)

### CLI2 (Narrative) - Next Actions
1. **#049** Example Extraction (Sky Engine, Surestar)
2. **#053** Linpowave Replacement (find zoom-in success)
3. **#050** Governance Levers (operationalize)
4. **#051** Paradox restriction (remaining items)
5. **#054** Academic Tone (final polish)

---

## KEY STATISTICS (Verified 2026-01-13)

| Metric | Value | Source |
|:-------|:------|:-------|
| N Total | 180,994 | thesis_panel_v3.nc |
| N Movers (R > 0) | 72,943 (40.3%) | test_thesis_consistency.py |
| N Stayers (R = 0) | 107,917 (59.7%) | test_thesis_consistency.py |
| Mover Success | 18.1% | VERIFIED |
| Stayer Success | 7.0% | VERIFIED |
| **Mover Advantage** | **2.60x** | VERIFIED |
| Chi-Square | 5,321.9*** | VERIFIED |

---
*Updated: 2026-01-13 (v4.0 Integration)*
*CLI Division: CLI1 = Logic, CLI2 = Narrative*
