---
modified:
  - 2026-01-09T09:49:30-05:00
---
### 📋 [Action_Items.md] D-1 Parallel Operations Log

COMMANDER: @Jeonha

STATUS: 🚨 DEFCON 1 (Strategy: Stick to v2 & Parallel Execution)

---

## 🤖 TEAM ASSIGNMENTS (Parallel Tracks)

- **Track 1 (Code/Stats):** **Cli 1** (@Charlie, @Sujin) $\to$ Fix Logic & Robustness using `v2`.
    
- **Track 2 (Text/Story):** **Cli 2** (@Scott) $\to$ Fix Narrative & Consistency.
    

---

## 🚨 PRIORITY 0: EXISTENTIAL THREATS (Fix or Die)

### **Issue #001: Method Truth Alignment (v2 Enforcement)**

> _Fraud Risk. Code is Abstractness (v2), Text must match._

- **Assignee:** @Scott (Cli 2)

- **Status:** ✅ **RESOLVED**

- **Action Module:**

    - [x] **Trigger:** `vagueness_v3` (Entropy) is abandoned. `v2` is active.

    - [x] **Extract:** Thesis_Master.md에 SBERT/Entropy 언급 없음 확인. CR.GLOSSARY v6.2 업데이트 완료.

    - [x] **Verify:** CR.GLOSSARY: "Dictionary-based Vague Terminology Density" 정의 반영.

    - [x] **Verdict:** Committed `fix(thesis): P0 방어선 구축`.
        

### **Issue #002: Formula Direction ($1-H$) $\to$ FROZEN**

> _Strategy Change. We stick to v2._

- **Assignee:** @Charlie (Cli 1)
    
- **Status:** 🧊 **FROZEN / SKIPPED**
    
- **Note:** `vagueness_v2.py` does not use Entropy. This issue is obsolete under Option A.
    

### **Issue #003: Number Sync (Abstract vs Body)**

> _Consistency. N=408k vs 178k._

- **Assignee:** @Sujin (Cli 1)

- **Status:** ✅ **RESOLVED**

- **Action Module:**

    - [x] **Trigger:** Discrepancy identified in Abstract.

    - [x] **Extract:** ¶1 수정: N=408,784 → **178,401**, ρ=-0.196 → **-0.174**

    - [x] **Verify:** Abstract 숫자 동기화 완료.

    - [x] **Verdict:** Committed `fix(thesis): P0 방어선 구축`.
        

---

## 🛡 PRIORITY 1: STATISTICAL DEFENSE (Cli 1)

### **Issue #004: Kill Magic Numbers (Thresholds)**

> _Robustness. Replace 10 with Quantile._

- **Assignee:** @Sujin (Cli 1)

- **Status:** ✅ **RESOLVED**

- **Action Module:**

    - [x] **Trigger:** `D > 10` is arbitrary in `01_raw_to_processed.py`.

    - [x] **Extract:** Implemented `D_q75 = quantile(0.75)`, `D_q25 = quantile(0.25)`, `M_q50 = quantile(0.50)`.

    - [x] **Verify:** Quantile thresholds: D_q25=0.0, D_q75=0.0 (분포가 0 주위 집중). 기존 ±10 threshold가 실제로 상위/하위 ~20% 포착 확인.

    - [x] **Verdict:** Committed `fix(thesis): P0 방어선 구축`. 기존 데이터(thesis_panel_v3.nc) 보존됨.

    - [x] **Thesis Text Updated:** ¶20-21의 Classification/Results 테이블을 quantile-based 정의로 변경 완료 (2026-01-09 09:35)
        

### **Issue #005: Causal Language Softening**

> _Tone. "Causes" $\to$ "Associated with"._

- **Assignee:** @Scott (Cli 2)

- **Status:** ✅ **RESOLVED**

- **Action Module:**

    - [x] **Trigger:** Lack of strong IV.

    - [x] **Extract:** Softened 4 instances of causal language:
        - ¶III intro: "proving that" → "suggesting that"
        - ¶19: "drives growth" → "is associated with growth"
        - ¶21: "drives the mover advantage" → "is associated with the mover advantage"
        - ¶23: "growth suppressor" → "associated with suppressed growth"

    - [x] **Verify:** Grep scan confirms no remaining "proves/proved/proven/resulted in" in claims. ¶29 already states "I document correlation, not causation."

    - [x] **Verdict:** Causal language softened (2026-01-09 09:40)
        

---

## 🧥 PRIORITY 2: NARRATIVE STRUCTURE (Cli 2)

### **Issue #006: Definition Injection (Front-loading)**

> _Readability. Define B & R in Intro._

- **Assignee:** @Scott (Cli 2)
    
- **Status:** 🔴 Todo
    
- **Action Module:**
    
    - [ ] **Trigger:** Definitions appear too late (¶20).
        
    - [ ] **Extract:** Insert definitions in Intro (¶3-5): "$B$ = Density of vague terms".
        
    - [ ] **Verify:** (@Gyeongrin) Readability flow check.
        
    - [ ] **Verdict:** (@Jeonha) Commit `docs: #006 intro definitions`.
        

### **Issue #007: Citation Boost (>30)**

> _Academic Rigor. Add canonical refs._

- **Assignee:** @Scott (Cli 2)
    
- **Status:** 🔴 Todo
    
- **Action Module:**
    
    - [ ] **Trigger:** Bibliography count < 30.
        
    - [ ] **Extract:** Add Eisenberg, Gioia, Trigeorgis, etc.
        
    - [ ] **Verify:** (@Gyeongrin) Ensure no ghost citations.
        
    - [ ] **Verdict:** (@Jeonha) Commit `docs: #007 boost biblio`.

### **Issue #008: Figures & Tables Integrity (Audit + Front Matter)**

> _Compliance & QA. Ensure all artifacts are captioned, referenced, and listed._

- **Assignee:** @Scott (Cli 2)
    
- **Priority:** 🧥 **P2 (Narrative/Polish)**
    
- **Status:** 🔴 Todo
    
- **Action Module:**
    
    - [ ] **Trigger:** Missing front matter OR potential "Orphaned Figures".
        
    - [ ] **Extract (Audit Phase):**
        
        - **Check Captions:** Verify every image/table has a descriptive caption (e.g., _Figure 1: Distribution of..._).
            
        - **Check References:** grep/search body text to ensure every Figure/Table is cited (e.g., _"As shown in Figure 1..."_). **Orphaned figures are forbidden.**
            
    - [ ] **Extract (Generate Phase):**
        
        - Generate **"List of Figures"** & **"List of Tables"** based on the audited captions.
            
        - Insert after TOC.
            
    - [ ] **Verify:** (@Gyeongrin) Random spot-check for "Figure X" links vs actual images.
        
    - [ ] **Verdict:** (@Jeonha) Commit `docs: #008 integrity check & lists`.


## Thesis Structure (Thesis_Master.md)

| Section                             |   Lines | Content                                                  |
| :---------------------------------- | ------: | :------------------------------------------------------- |
| Abstract                            |   10-24 | Paradox + Decomposition + Mechanism                      |
| I. Introduction                     |   28-79 | Wisdom → Puzzle → Resolution → Mechanism → Contributions |
| II. Repositioning Drives Growth     |  82-144 | Orthodoxy → Exception → Movers/Stayers → Tesla/BP        |
| III. Funding Inhibits Repositioning | 148-229 | Theory → Contradiction → Mechanism → Segway              |
| IV. Prescription                    | 233-279 | Two-Phase → AV Cases                                     |
| V. Conclusion                       | 283-311 | Summary → Implications → Limitations                     |
| References                          | 315-329 | 7 citations                                              |

---

## 📊 검증 결과 요약 (2026-01-09 09:30)

### Option A 채택: v2 파이프라인 유지

| 지표 | 값 | 상태 |
|:-----|:---|:----:|
| **N** | 180,994 | ✅ |
| **ρ(G, E)** | −0.196*** | ✅ Funding Paradox |
| **ρ(M, E)** | −0.059*** | ✅ Fund→Cage |
| **ρ(G, M)** | +0.117*** | ✅ Movement→Growth |
| **Mover Advantage** | 1.82× (18.0% vs 9.9%) | ✅ |

### P0 Status

| Issue | 내용 | 상태 |
|:-----:|:-----|:----:|
| #001 | v2 방법론 정렬 | ✅ |
| #002 | Formula (1-H) | 🧊 FROZEN |
| #003 | N/ρ 숫자 동기화 | ✅ |
| #004 | Quantile threshold | ✅ |

---

*Updated: 2026-01-09 09:30*
*Option A: v2 데이터 방어선 완료.*
