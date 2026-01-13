---
modified:
  - 2026-01-09T11:00:20-05:00
  - 2026-01-09T17:27:03-05:00
  - 2026-01-10T20:37:27-05:00
  - 2026-01-11T08:33:43-05:00
  - 2026-01-11T15:30:00-05:00
  - 2026-01-12T09:30:00-05:00
  - 2026-01-13T08:10:00-05:00
---
[[Thesis_Master]]

# Action Items: Final Integration Plan (v4.0)

> **Goal**: RoT 95% (Peer Review 100% Integration)
> **Sources**: Self Feedback, Lorry & Eze Feedback, Database Examples
> **Status**: Emergency Martial Law - Immediate Execution

---

## TIER 0: CRITICAL DEFENSE

### **Issue #TR-02: Survival Bias Defense [P0]**
> *Source: Lorry #4*
- **Gap:** "Moved because they survived?" critique.
- **Action:**
  - **Fixed Horizon:** Explicitly condition analysis on "Firms surviving to Year 3+".
  - **Logic:** Argue "Among survivors, those who repositioned grew more."
- **Status:** DONE (test_thesis_consistency.py verifies 2.60x advantage)

### **Issue #TR-04: Measurement Validity (Breadth) [P0]**
> *Source: Lorry #3*
- **Gap:** Is $B$ just marketing fluff?
- **Action:**
  - **Cross-Validation:** Validate text-based Breadth ($B$) against observable non-text signals (Product Category changes, Tech Tags, Customer Segment shifts).

### **Issue #G-01: Causality Control & H0 [P0]**
> *Source: Lorry #1*
- **Gap:** Causal language risk.
- **Action:**
  - **Estimand:** Insert: "I document a robust correlational pattern... consistent with a mechanism."
  - **H0:** Explicitly state Null Hypothesis (Resources -> Growth).
  - **Word Sweep:** Replace `suppresses`/`drives` with associative verbs.

### **Issue #G-05: Data Transparency [P0]**
> *Source: Self*
- **Action:**
  - **Figure 4:** Fill the placeholder (Initial DB -> US HQ -> Sample).
  - **Cleanup:** Remove empty 3.2.2. Verify "US Headquartered" filter in code.

---

## TIER 1: LOGIC & STRUCTURE

### **Issue #S-01: Pattern vs Mechanism Re-org [P1]**
> *Source: User Instruction #5*
- **Action:**
  - **Chapter 2 (Theory):** Focus on Observed Patterns (**EG, ER, RG**).
  - **Chapter 3 (ID):** Focus on Causal Mechanisms (**CEF**: C -> E -> F, **FG**: F -> G).
  - **Figure 2 Update:** Map Latent vs Measured variables to this structure.

### **Issue #T-01: Deep Tech & Commitment Types [P1]**
> *Source: Eze #1, #2, #3, #4*
- **Action:**
  - **Deep Tech:** Add "Chicago Booth Approach" (Non-dilutive funding/Grants) as a survival strategy for Quantum/Deep Tech in Ch.4.
  - **Commitment Distinction:** Contrast **"Staged Commitment"** (Milestone-based, Signal up) vs **"Partial Commitment"** (Low interest, Signal down).

### **Issue #T-02: Alternative Explanations [P1]**
> *Source: Lorry #2*
- **Action:**
  - Compare "Governance Homogeneity" against **Milestone Pressure**, **Burn-rate Discipline**, **Moral Hazard**.
  - Show why data patterns favor Homogeneity.

---

## TIER 2: EXAMPLES & PRESCRIPTION

### **Issue #E-01: Illustrative Examples [P2]**
> *Source: Image Analysis + User Instruction #4*
- **Action:**
  - **Broadening Mover:** **Sky Engine** (V: 28 -> 89, G: 215x).
  - **Stayer:** **Surestar** (V: 87 -> 87, G: 26x).
  - **Narrowing Mover:** **REPLACE Linpowave** (since G=N/A). Find a successful "Zoom-in" case in DB.

### **Issue #P-01: Concrete Governance Levers [P2]**
> *Source: Lorry #5*
- **Action:**
  - Operationalize "Preserve Skeptics": Define via **Syndicate Composition**, **Board Structure**, and **Dissent-friendly Decision Rules**.

---

## TIER 3: POLISH & TERMINOLOGY

### **Issue #W-01: Strict Word Choice [P3]**
> *Source: User Instruction #1*
- **Action:**
  - `Movement` -> **`Repositioning`** (Global Replace). DONE
  - `Paradox` usage -> Restricted to **"Funding Paradox"** only.
  - `Conviction Paradox` -> Renamed to **"Caged Learning"**.
  - `Theorem 1` -> **"Theorem 1 (Caged Learning)"**.

### **Issue #M-01: Methodology Change (R > 0) [P3]**
> *Source: 2026-01-13 Update*
- **Status:** DONE
- **Change:** Mover definition from R > median(R|R>0) to R > 0
- **Result:** 2.60x advantage (18.1% vs 7.0%), verified by test_thesis_consistency.py

---

## PRIORITIZED QUEUE
1. **#TR-04** Measurement Validity (Breadth cross-validation)
2. **#G-01** Causality Control (Word sweep)
3. **#S-01** Ch.2/Ch.3 Structural Re-org
4. **#W-01** Terminology Sweep (remaining items)
5. **#T-01** Deep Tech/Staged Commitment
6. **#E-01** Example Extraction (Find Linpowave Replacement)

---

## COMPLETED ITEMS

| Issue | Description | Completed |
|:------|:------------|:---------:|
| #TR-02 | Survival Bias Defense | 2026-01-13 |
| #M-01 | R > 0 Methodology Change | 2026-01-13 |
| #W-01 (partial) | Movement -> Repositioning | 2026-01-13 |
| #TR-03 | Industry Universality | 2026-01-12 |
| #TR-04 | Alternative Story (DGP) | 2026-01-11 |

---
*Updated: 2026-01-13 (v4.0 Integration)*
