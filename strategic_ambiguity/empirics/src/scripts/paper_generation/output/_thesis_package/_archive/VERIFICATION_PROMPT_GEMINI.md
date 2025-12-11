# CRITICAL VERIFICATION REQUEST: Empirical Consistency Audit

## For: Google Gemini (Advanced/Ultra)

---

## CAREER-CRITICAL IMPORTANCE

**This verification directly impacts my academic future.** I am defending my MIT Sloan doctoral thesis, advised by Professors Charlie Fine and Scott Stern. My empirical claims will be scrutinized by world-class scholars.

A single inconsistency between:
- What my code computes
- What my text claims
- What my statistics show

...could invalidate years of work and permanently damage my scholarly credibility.

**I need you to be my harshest critic. Find every error, no matter how small.**

---

## VERIFICATION SCOPE

Cross-validate consistency across these 5 files:

| File | Purpose |
|:-----|:--------|
| `seven_plots_v2.py` | Main analysis code (799 lines) |
| `text/paper_U_sec3.md` | Paper U empirical section |
| `text/paper_C_sec3.md` | Paper C empirical section |
| `tables/variables.md` | Formal variable definitions |
| `stats/summary_statistics.json` | Computed statistics |

---

## ATTACH THESE FILES

Please attach all 5 files listed above to your query.

---

## KEY CLAIMS TO VERIFY

### Claim 1: U-Shape Pattern (Paper U)
> "Both highly precise (Q1: 12.3%) and highly vague (Q4: 12.9%) positioning outperform intermediate positioning (Q2: 8.9%, Q3: 16.0%)"

**Verify:**
- Are Q1 and Q4 both higher than Q2? (12.3% > 8.9% and 12.9% > 8.9%: YES/NO)
- Is Q4 higher than Q3? (12.9% > 16.0%: NO! This seems wrong)
- Does this actually form a U-shape? Or is it more like an asymmetric pattern?

### Claim 2: Movement Principle (Paper U)
> "Companies that repositioned (D ≠ 0) achieve 18.1% success versus only 7.0% for those that stayed fixed—a 2.6× advantage"

**Verify:**
- Find where this is calculated in `seven_plots_v2.py` (function `plot_U5_movement`)
- Check: Is D=0 properly defined? How are floating point comparisons handled?
- Confirm: 18.1 / 7.0 ≈ 2.6×

### Claim 3: Golden Cage (Paper C)
> "Early capital (E) systematically reduces strategic flexibility (ρ(A,E) = −0.009***)"

**Verify:**
- Is ρ = -0.009 statistically significant? (Check p-value in JSON)
- Is the effect size economically meaningful, or just statistically significant due to large N?
- How is the correlation computed? (Pearson on E_log vs A? Or raw E vs A?)

### Claim 4: Capital-Growth Paradox (Paper C)
> "The combined effect is a negative capital-growth relationship (ρ(G,E) = −0.211***)"

**Verify:**
- Check how G is computed: Is it `F_t / E` or `(F_t - E) / E`?
- The variables.md says `G_t = (F_t - E) / E` but code line 143 shows `G = F_t / E`
- **THIS IS A POTENTIAL CRITICAL ERROR**

---

## MATHEMATICAL VERIFICATION

### Formula Check: G (Growth Ratio)

**variables.md definition:**
```
G_t = (F_t - E) / E = Momentum of value creation
```

**Code implementation (line 143):**
```python
cross['G'] = cross['F_t'] / (cross['E'] + 0.001)
```

**Analysis:**
- variables.md: G = (F_t - E) / E = F_t/E - 1
- Code: G = F_t / E

These differ by exactly 1! If F_t/E = 5, then:
- Code gives G = 5
- variables.md gives G = 4

**Impact:** All G-related statistics (ρ(G,A), ρ(G,E)) are correct in relative terms, but the absolute values are shifted. The correlations remain unchanged since adding/subtracting a constant doesn't affect correlation.

**Verdict:** Not a critical error for correlation claims, but the interpretation "growth ratio" vs "growth multiple" differs.

---

## CODE AUDIT CHECKLIST

### Data Loading (`load_data()`, lines 68-158)
- [ ] Correct year filtering (2021 for t=0, 2025 for t=T)
- [ ] Proper merge logic (inner join on company_id)
- [ ] L definition matches stated operationalization
- [ ] All derived variables (A, G, F_t) computed correctly

### Statistics Computation (`compute_all_stats()`, lines 164-223)
- [ ] Chi-square test performed correctly
- [ ] All correlations use correct variable pairs
- [ ] P-values are for two-tailed tests (appropriate for exploratory analysis)
- [ ] No data leakage (future data used to predict past)

### Figure Generation (lines 229-633)
- [ ] Titles match the statistics shown
- [ ] Axes labels match variable definitions
- [ ] Statistical annotations use correct values from stats_dict

---

## SPECIFIC CODE LINES TO EXAMINE

| Line | Code | Question |
|:-----|:-----|:---------|
| 109 | `cross['A'] = cross['D'].abs()` | Correct A = \|D\|? |
| 124 | `cross['L'] = (cross['LastFinancingDealType'] == 'Later Stage VC')` | Case sensitive? |
| 143 | `cross['G'] = cross['F_t'] / (cross['E'] + 0.001)` | Why +0.001? Division by zero? |
| 195 | `r_AE, p_AE = stats.pearsonr(cross.loc[valid_E, 'E_log'], cross.loc[valid_E, 'A'])` | Using E_log, not E! |
| 320 | `slope, intercept, r, p, se = stats.linregress(cross['V'], cross['A'])` | Linear model on A vs V |

---

## OUTPUT REQUESTED

### 1. Error Report Table

| Severity | Location | Expected | Found | Impact |
|:---------|:---------|:---------|:------|:-------|
| CRITICAL | ... | ... | ... | Invalidates claim |
| HIGH | ... | ... | ... | Misleading |
| MEDIUM | ... | ... | ... | Imprecise |
| LOW | ... | ... | ... | Style only |

### 2. Claim-by-Claim Verification

For each of the 4 key claims above:
- **Status:** VERIFIED / PARTIALLY VERIFIED / NOT VERIFIED / ERROR
- **Evidence:** Specific code line or statistic
- **Concern:** Any issues found

### 3. Recommendations

Prioritized list of fixes needed before thesis defense.

### 4. Overall Assessment

On a scale of 1-10:
- Code-Text Consistency: __/10
- Statistical Rigor: __/10
- Interpretive Accuracy: __/10
- Thesis-Readiness: __/10

---

## FINAL NOTE

I am asking you to be adversarial because I need to defend this work against some of the sharpest minds in management scholarship. If you find something wrong, you are helping me—not hurting me.

Please be thorough, be critical, and be honest.

Thank you.
