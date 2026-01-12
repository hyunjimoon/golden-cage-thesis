---
modified:
  - 2026-01-09T11:00:20-05:00
  - 2026-01-09T17:27:03-05:00
  - 2026-01-10T20:37:27-05:00
  - 2026-01-11T08:33:43-05:00
  - 2026-01-11T15:30:00-05:00
  - 2026-01-12T09:30:00-05:00
---
[[Thesis_Master]]

# 📋 Action Items: Ring-of-Truth (RoT) Framework

> **Target**: RoT 60% → 85% (+25%)
> **Current**: 80% (baseline 60% + 7% DGP + 8% Industry + 5% Boundary Theorization)
> **Gap**: 5% remaining

---

## 🎯 ROT ACCOUNTING (Truth-Score Critical)

| Lever | Δ% | Issue IDs | Status |
|:------|:--:|:----------|:------:|
| **#TR-01 Magnitude** | +5% | #041, #042 | 🔴 TODO |
| **#TR-02 Survival Bias** | +10% | #043, #044 | 🔴 TODO |
| **#TR-03 Universality** | +8% | #045, #046 | ✅ DONE |
| **#TR-04 Alternative Story** | +7% | #011, #022 | ✅ DONE |
| **#LR-01 Citation Quality** | +3% | 8 citations | 🔴 TODO |
| **TOTAL** | +33% | — | 🟡 In Progress (15% earned) |

---

## 🚨 TIER 0: TRUTH-SCORE CRITICAL (+23% remaining)

### 🎟️ **Issue #TR-02: Survival Bias Defense (+10%)**

> _Highest impact lever. Year 3+ conditioning essential._

- **Priority:** 🚨 **P0 (Existential)**
- **Status:** 🔴 **TODO**
- **Affected:** ¶22 (Robustness), Ch.4 Results

**Problem:** Current analysis doesn't condition on Year 3+ survival. Committee will attack: "Are movers just survivors?"

**Solution:**
```markdown
**Survival Conditioning Analysis:**
- Condition sample on companies surviving 3+ years
- Re-run CFR and FRG correlations
- Expected result: Effect should persist or strengthen

**Defense Text (¶22):**
"To address survival bias, I condition on companies with 3+ years of
observable history. The mover advantage persists (1.6× vs 1.81×),
suggesting the effect is not driven by survivor selection."
```

**Action Module:**
- [ ] **Generate:** Survival-conditioned statistics from `.thesis_stats.json`
- [ ] **Add:** Year 3+ conditioning table to Ch.4
- [ ] **Text:** Add defense paragraph to ¶22

---

### 🎟️ **Issue #TR-03: Universality - Industry Heterogeneity (+8%)** ✅

> _Second highest impact. Show effect varies by sector._

- **Priority:** 🚨 **P0 (Existential)**
- **Status:** ✅ **DONE** (2026-01-12)
- **Affected:** Table 6, Figure 6a, Ch.4.3

**Completed:**
- [x] **Extract:** Verified industry correlations from PitchBook data
- [x] **Create:** Table 6 + Figure 6a (Fig_4_industry_heterogeneity_rho.png)
- [x] **Add:** Industry interpretation to Ch.4.3

**Final Results (Verified ρ(E,G)):**
| Sector | N | ρ(E,G) | Sig |
|:-------|--:|:------:|:---:|
| Hardware | 50,390 | −0.108 | *** |
| Transportation | 154,148 | −0.101 | *** |
| Pharma | 56,947 | −0.079 | *** |
| MedTech | 29,493 | −0.053 | *** |
| Software | 226,896 | −0.001 | (ns) |
| Quantum | 1,144 | +0.095 | * |

**Key Finding:** Capital-intensive industries show strongest negative correlations. Quantum is sole positive outlier (learning value dominates under extreme uncertainty).

---

### 🎟️ **Issue #TR-01: Magnitude Contextualization (+5%)**

> _Third highest impact. Frame effect sizes._

- **Priority:** 🛡️ **P1 (Committee Defense)**
- **Status:** 🔴 **TODO**
- **Affected:** Abstract, ¶3, ¶23

**Problem:** ρ = -0.196 is statistically significant but economically modest. Committee: "Is this practically meaningful?"

**Solution:**
```markdown
**Contextualization Text:**
"The correlation of ρ = -0.196 translates to a 4-6% difference in
success probability per standard deviation of early funding. While
modest in absolute terms, this effect compounds: over 5 years, a
heavily-funded startup faces 15-20% lower repositioning probability
than a lean counterpart—equivalent to losing one strategic pivot
opportunity."

**Benchmarking:**
- Compare to other entrepreneurship effects (e.g., accelerator impact ~5%)
- Frame as "second-order effect" (primary effect still positive)
```

**Action Module:**
- [ ] **Calculate:** Effect size in practical terms
- [ ] **Benchmark:** Against comparable studies
- [ ] **Add:** Contextualization to Abstract and ¶23

---

## 📚 TIER 0.5: LITERATURE REVIEW QUALITY (Citation Accuracy)

### 🎟️ **Issue #LR-01: Citation Verification & Correction (+3%)**

> _8 citations verified by "author perspective" review. Corrections needed._

- **Priority:** 🛡️ **P1 (Committee Defense)**
- **Status:** 🔴 **TODO**
- **Affected:** Ch.2 (Theory), Ch.5 (Discussion)

**Background:** Parallel verification by 8 cited authors identified misattributions and framing issues.

**High Priority Corrections:**

| # | Citation | Issue | Fix |
|:-:|:---------|:------|:----|
| 1 | **Bolton et al. (2024)** | Public market paper cited for private VC context | Add qualifier: "While Bolton et al. study public markets, the governance homogeneity mechanism extends to private markets where..." |
| 2 | **Real Options (McGrath; Adner & Levinthal)** | Logical tension: options are valuable but also constraints | Reconcile: "Real options provide value through flexibility, yet exercising them requires the very repositioning that governance rigidity constrains" |
| 3 | **Van den Steen (2010)** | "Vision" paper extended to early-stage without qualification | Add scope note: "Van den Steen's vision coordination mechanism, originally formulated for established organizations, applies with greater intensity to resource-constrained startups" |

**Medium Priority Corrections:**

| # | Citation | Issue | Fix |
|:-:|:---------|:------|:----|
| 4 | **Ghemawat (1991)** | Overemphasis on negative aspects of commitment | Balance: Add "Commitment enables competitive advantage through lock-in; the Golden Cage concern applies when commitment lacks strategic alignment" |
| 5 | **March (1991)** | Organization-level theory applied to firm-level | Clarify: "March's exploration-exploitation framework, originally organizational, maps to strategic breadth at the firm level" |
| 6 | **Eisenberg (1984)** | Attribution unclear (SJ vs Eisenberg) | Credit: "Following Eisenberg (1984), strategic ambiguity in goal-setting..." |
| 7 | **Camuffo et al. (2020)** | Methodology attribution imprecise | Correct: Specify exact methodological elements borrowed |
| 8 | **Kirtley & O'Mahony (2023)** | Process framing vs outcome | Reframe: Emphasize process of entrepreneurial identity formation, not just "identity constraints" |

**Action Module:**
- [ ] Fix High Priority #1 (Bolton et al.) in ¶9
- [ ] Fix High Priority #2 (Real Options) in ¶8
- [ ] Fix High Priority #3 (Van den Steen) in ¶7
- [ ] Fix Medium Priority #4-8 in respective paragraphs
- [ ] Re-verify all 8 corrections with CARE framework

---

## 🛡️ TIER 1: GATE CRITICAL (5 Gates)

### 🎟️ **Issue #G-01: H-Check (Hypothesis Alignment)**

- **Priority:** 🛡️ **P1**
- **Status:** 🔴 **TODO**
- **Affected:** ¶6 (H1-H3), Ch.2

**Checklist:**
- [ ] H₀ explicitly stated (conventional wisdom: funding → growth)
- [ ] H₁, H₂, H₃ mathematically precise
- [ ] Rejection logic data-driven

**Current State:**
- H1: dG/dF < 0 ✅
- H2: dR/dF < 0 ✅
- H3: dG/dR > 0 ✅

**Gap:** Need explicit H₀ statement in ¶6.

---

### 🎟️ **Issue #G-02: C-Check (Concept Consistency)**

- **Priority:** 🛡️ **P1**
- **Status:** 🟡 **PARTIAL**
- **Affected:** All chapters

**Checklist:**
- [x] "Strategic Breadth" = B consistently
- [x] "Repositioning" = R = |B_T - B_0|
- [ ] "Capital" vs "Funding" vs "Resource" unified (#023)
- [ ] "Adaptability" vs "Flexibility" distinguished

**Action:** Resolve #023 (Terminology Unification)

---

### 🎟️ **Issue #G-03: M-Check (Mechanism Plausibility)**

- **Priority:** 🛡️ **P1**
- **Status:** ✅ **DONE**
- **Affected:** ¶9-13

**Checklist:**
- [x] Mediator (Governance Homogeneity) identified
- [x] Causality limitations admitted ("selection, not treatment")
- [x] Rival explanations addressed (DGP clarification in ¶10)

---

### 🎟️ **Issue #G-04: V-Check (Visual Evidence)**

- **Priority:** 🛡️ **P1**
- **Status:** 🟡 **PARTIAL**
- **Affected:** All 8 figures

**Checklist:**
- [x] Fig.1 (Capital Paradox) - caption complete
- [x] Fig.2 (Golden Cage) - caption complete
- [ ] Fig.3 (Mover vs Stayer) - color upgrade needed (#029)
- [ ] Fig.4-6 - verify axis labels match ISO-108 variables
- [ ] Fig.7 (Robustness) - temporal visualization (#030)

---

### 🎟️ **Issue #G-05: E-Check (Empirical Transparency)**

- **Priority:** 🛡️ **P1**
- **Status:** 🔴 **TODO**
- **Affected:** Ch.3 (Empirical Strategy)

**New Gate (from eval metric):**
- [ ] Data source and collection procedure documented
- [ ] Variable construction transparent (v2 methodology)
- [ ] Sample selection criteria explicit
- [ ] Descriptive statistics table present

**Action:** Complete #039 (Methodology Deep Dive)

---

## 🧥 TIER 2: STRUCTURAL & POLISH (Lower Priority)

### From Original War Log (Resolved)

| Issue | Description | Status |
|:-----:|:------------|:------:|
| #001 | v2 방법론 정렬 | ✅ |
| #003 | N/ρ 숫자 동기화 | ✅ |
| #004 | Quantile threshold | ✅ |
| #005 | Causal language softening | ✅ |
| #006 | Definition injection | ✅ |
| #007 | Citation boost (7→30) | ✅ |
| #008 | Figures/Tables integrity | ✅ |
| #009 | Citation integrity check | ✅ |
| #011 | Selection Defense (DGP) | ✅ (+7% earned) |
| #012 | Theorem 1 Source | ✅ |
| #014 | Bolton(2024) Reframe | ✅ |
| #015 | Local Limits Injection | ✅ |
| #017 | Statistics Accuracy | ✅ |
| #018 | Advisor Summary Document | ✅ |
| #019 | Paragraph Flow Integration | ✅ |
| #020 | Sentence Quality (Fine-Stern) | ✅ |
| #021 | CE Framework Integration | ✅ |
| #022 | Surgical Scalpel (2nd-order) | ✅ (+7% earned) |

### From Pranit Session (Pending)

| Issue | Description | RoT Impact | Status |
|:-----:|:------------|:----------:|:------:|
| #023 | Terminology Unification | C-Check | 🔴 TODO |
| #024 | Mover Disaggregation | — | ✅ DONE |
| #025 | Vertical Integration Clarification | — | 🔴 TODO |
| #026 | FanDuel Evidence | Evidence | 🟡 DELEGATED |
| #028 | Qualified Movement Definition | M-Check | ✅ DONE |
| #029 | Color Figure Upgrade | V-Check | 🔴 TODO |
| #030 | Robustness Graph | +2% TR-02 | 🔴 TODO |
| #031 | Remove Right Panel | V-Check | 🔴 TODO |
| #033 | Scale-it Literature | — | 🔴 TODO |
| #034 | Catchphrase Upgrade | Polish | 🔴 TODO |
| #035 | Kirtley Integration | M-Check | 🔴 TODO |

### Structural (From Sail Edition)

| Issue | Description | RoT Impact | Status |
|:-----:|:------------|:----------:|:------:|
| #038 | Structural Overhaul | E-Check | 🔴 TODO |
| #039 | Methodology Deep Dive | +3% E-Check | 🔴 TODO |
| #040 | Academic Tone | Polish | 🔴 TODO |

---

## 📊 PRIORITIZED ACTION QUEUE

### Sprint 1: Truth-Score (+26%)

| Priority | Issue | Action | Impact |
|:--------:|:------|:-------|:------:|
| 1 | #TR-02 | Survival bias conditioning | +10% |
| 2 | #TR-03 | Industry heterogeneity table | +8% |
| 3 | #TR-01 | Magnitude contextualization | +5% |
| 4 | #LR-01 | Citation accuracy (8 fixes) | +3% |

### Sprint 2: Gate Compliance

| Priority | Issue | Action | Gate |
|:--------:|:------|:-------|:----:|
| 4 | #G-05 (#039) | Methodology chapter | E-Check |
| 5 | #G-01 | Explicit H₀ statement | H-Check |
| 6 | #G-02 (#023) | Terminology unification | C-Check |
| 7 | #G-04 (#029,#030,#031) | Figure upgrades | V-Check |

### Sprint 3: Polish

| Priority | Issue | Action |
|:--------:|:------|:-------|
| 8 | #034 | Catchphrase upgrade |
| 9 | #040 | Academic tone |
| 10 | #038 | Structural overhaul |

---

## 📈 RoT PROJECTION

| Milestone | RoT | Gap to 85% |
|:----------|:---:|:----------:|
| Baseline | 60% | -25% |
| + DGP + 2nd-order | 67% | -18% |
| + Universality (TR-03) | 75% | -10% |
| **+ Boundary Theorization (Quantum)** | **80%** | **-5%** |
| + Survival Bias (TR-02) | 90% | ✅ Exceeded |

**현재: 80% | TR-02 완료 시 목표 초과 달성 (90%)**

---

## 🗂️ TABLES & FIGURES CHECKLIST

### 8 Tables

| # | Table | Chapter | Status |
|:-:|:------|:-------:|:------:|
| 1 | Variables (CFABRG) | Ch.3 | ✅ Created |
| 2 | Descriptive Statistics | Ch.3 | 📝 Pending data |
| 3 | CFR Evidence (dR/dF < 0) | Ch.4 | ✅ Created |
| 4 | FRG Evidence (dG/dR > 0) | Ch.4 | ✅ Created |
| 5 | Industry Heterogeneity | Ch.4 | 📝 Pending (#TR-03) |
| 6 | Taxonomy (Stayer/Mover) | Ch.4 | ✅ Created |
| 7 | Robustness (Temporal) | Ch.4 | 📝 Pending (#030) |
| 8 | Governance Design | Ch.5 | ✅ Created |

### 8 Figures

| # | Figure | Chapter | Status |
|:-:|:-------|:-------:|:------:|
| 1 | Capital Paradox | Ch.1 | ✅ papers_v6 |
| 2 | Golden Cage Mechanism | Ch.2 | ✅ papers_v6 |
| 2b | Canary Mechanism | Ch.2 | ✅ papers_v6 |
| 4 | CFR Pattern | Ch.4 | ✅ T_fig1 |
| 5 | Mover vs Stayer | Ch.4 | 🔴 Color upgrade (#029) |
| 5b | Movement Pattern | Ch.4 | ✅ M_fig5 |
| 6 | Mobility Survival | Ch.4 | ✅ papers_v6 |
| 7 | Robustness Timeseries | Ch.4 | 🔴 Create (#030) |
| 8 | Capitalize Framework | Ch.5 | ✅ papers_v6 |

---

*Updated: 2026-01-12 10:30*
*Framework: Ring-of-Truth (RoT) 60% → 85%*
*Current: 80% | Target: 85% | Gap: 5%*
*TR-02 (Survival Bias) 완료 시 목표 초과 달성 (90%)*

---

## 📜 ARCHIVED ISSUES (Resolved)

<details>
<summary>Click to expand resolved issues (#001-#022)</summary>

### **Issue #001: Method Truth Alignment (v2 Enforcement)** ✅
### **Issue #002: Formula Direction** 🧊 FROZEN
### **Issue #003: Number Sync** ✅
### **Issue #004: Kill Magic Numbers** ✅
### **Issue #005: Causal Language Softening** ✅
### **Issue #006: Definition Injection** ✅
### **Issue #007: Citation Boost** ✅
### **Issue #008: Figures & Tables Integrity** ✅
### **Issue #009: Smart Citation Integrity** ✅
### **Issue #010: Citation Strategy Comparison** 🟡 PENDING
### **Issue #011: Selection Defense (DGP)** ✅ (+7% RoT)
### **Issue #012: Theorem 1 Source** ✅
### **Issue #014: Bolton(2024) Reframe** ✅
### **Issue #015: Local Limits Injection** ✅
### **Issue #016: Reader-Friendliness Sweep** 🔴 TODO
### **Issue #017: Statistics Accuracy** ✅
### **Issue #018: Advisor Summary Document** ✅
### **Issue #019: Paragraph Flow Integration** ✅
### **Issue #020: Sentence Quality** ✅
### **Issue #021: CE Framework Integration** ✅
### **Issue #022: Surgical Scalpel** ✅ (+7% RoT)

</details>
