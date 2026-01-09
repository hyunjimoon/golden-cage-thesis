---
modified:
  - 2026-01-09T09:18:13-05:00
---
### 📋 [Action_Items.md] D-1 Operations Log (Issue Tracked)

COMMANDER: @Jeonha

STATUS: 🚨 DEFCON 1

CURRENT FOCUS: fix: #001 (In Progress)

---

## 🚨 PRIORITY 0: EXISTENTIAL THREATS (Must Fix)

### **Issue #001: Method Truth Alignment (SBERT $\to$ Entropy)**

> _Fraud Risk Removal. Code must match Text._

- **Assignee:** @Charlie
    
- **Status:** 🟡 In Progress (Glossary updated, checking Thesis text...)
    
- **Action Module:**
    
    - [x] **Trigger:** `CR.GLOSSARY.md` mismatch found.
        
    - [ ] **Extract:** Replace "SBERT/Cosine" with "Shannon Entropy" in `Thesis_Master.md`.
        
    - [ ] **Verify:** (@Gyeongrin) Ensure no "embedding" keywords remain.
        
    - [ ] **Verdict:** (@Jeonha) Commit `fix: #001 text alignment`.
        

### **Issue #002: Formula Direction Flip ($1-H \to H$)**

> _Logic Repair. Narrow Market $\neq$ High Vagueness._

- **Assignee:** @Charlie
    
- **Status:** 🔴 Todo
    
- **Action Module:**
    
    - [ ] **Trigger:** `vagueness_v3.py` logic error identified.
        
    - [ ] **Extract:** Change code to `vagueness = 0.5 * H_norm`.
        
    - [ ] **Verify:** (@Gyeongrin) Sign Flip Test (Correlation direction check).
        
    - [ ] **Verdict:** (@Jeonha) Commit `fix: #002 flip formula`.
        

### **Issue #003: Number Sync (Abstract vs Body)**

> _Consistency. N=408k vs 178k._

- **Assignee:** @Sujin
    
- **Status:** 🔴 Todo
    
- **Action Module:**
    
    - [ ] **Trigger:** Claude reported discrepancy.
        
    - [ ] **Extract:** Update Abstract to use Analytical Sample ($N=178,401$).
        
    - [ ] **Verify:** (@Gyeongrin) Check Abstract, Table 1, and Conclusion match.
        
    - [ ] **Verdict:** (@Jeonha) Commit `fix: #003 number sync`.
        

---

## 🛡 PRIORITY 1: STATISTICAL DEFENSE (Methodology)

### **Issue #004: Kill Magic Numbers (Thresholds)**

> _Robustness. Why 10? Why 5?_

- **Assignee:** @Sujin
    
- **Status:** 🔴 Todo
    
- **Action Module:**
    
    - [ ] **Trigger:** Arbitrary thresholds in `01_raw_to_processed.py`.
        
    - [ ] **Extract:** Implement `quantile(0.75)` dynamic threshold.
        
    - [ ] **Verify:** (@Gyeongrin) Check if Mover/Stayer ratio remains reasonable.
        
    - [ ] **Verdict:** (@Jeonha) Commit `feat: #004 dynamic thresholds`.
        

### **Issue #005: Causal Language Softening**

> _Tone. "Causes" $\to$ "Associated with"._

- **Assignee:** @Scott
    
- **Status:** 🔴 Todo
    
- **Action Module:**
    
    - [ ] **Trigger:** Lack of strong IV (Instrumental Variable).
        
    - [ ] **Extract:** Rewrite ¶22 and Conclusion.
        
    - [ ] **Verify:** (@Gyeongrin) Scan for forbidden words ("proves", "causes").
        
    - [ ] **Verdict:** (@Jeonha) Commit `docs: #005 soften claims`.
        

---

## 🧥 PRIORITY 2: NARRATIVE STRUCTURE

### **Issue #006: Definition Injection (Front-loading)**

> _Readability. Define B & R in Intro._

- **Assignee:** @Scott
    
- **Status:** 🔴 Todo
    
- **Action Module:**
    
    - [ ] **Trigger:** Definitions appear too late (¶20).
        
    - [ ] **Extract:** Add clear definitions to Introduction (¶3-5).
        
    - [ ] **Verify:** (@Gyeongrin) Readability flow check.
        
    - [ ] **Verdict:** (@Jeonha) Commit `docs: #006 intro definitions`.
---




---

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

*Updated: 2026-01-09*
*MERGE & PURGE complete. Thesis_Master.md is now the manuscript.*
