# Validation Report: V=87.5 Investigation

**Date**: 2025-12-20
**Status**: VALIDATED - Not a Bug
**Investigator**: Claude Code

---

## Executive Summary

User raised critical concern about 43% of V scores being exactly 87.5. After thorough investigation:

**V=87.5 is VALID expected behavior**, not a bug. It represents the "baseline vagueness" for typical company descriptions that are:
- Neither buzzword-heavy (low S_cat)
- Nor data-rich (high S_concdef)

---

## Investigation Results

### 1. Formula Verification

```
V=87.5 = 0.5 * V_raw + 0.5 * concrete_score
       = 0.5 * 75 + 0.5 * 100
       = 87.5
```

Where:
- **V_raw = 75** comes from:
  - S_cat = 0 (no abstract buzzwords like "platform", "solution", "ecosystem")
  - S_concdef = 100 (no numbers, dates, units, benchmarks)
  - V_raw = 0.5 * max(0, 100) + 0.5 * mean(0, 100) = 75

- **concrete_score = 100** comes from:
  - No numerical metrics (%, numbers)
  - No years (2020, 2021, etc.)
  - No technical units (MHz, GB, fps)

### 2. Sample V=87.5 Descriptions

These are REAL descriptions from the data that score V=87.5:

| Description | V Score | Why 87.5? |
|:------------|:-------:|:----------|
| "Provider of cellular telecommunication service. The company offers mobile phone services." | 87.5 | Plain descriptive, no buzzwords, no metrics |
| "Distributor of liquid propane for home, residential, business and agricultural use." | 87.5 | Factual, no abstract terms, no numbers |
| "Publisher of mobile games intended to offer entertainment options." | 87.5 | Generic, lacks specific metrics |
| "The company is currently operating in stealth mode." | 87.5 | Minimal info, nothing concrete |

### 3. Data Distribution

```
Total rows: 1,635,136
V=87.5 rows: 708,337 (43.3%)

Companies with V=87.5 in ALL 4 years: 158,851
(These are consistently "baseline vague" companies)

V Statistics:
  Mean: 78.54
  Median: 87.50
  Std: 20.06
```

### 4. Scorer Differentiation Test

The scorer CAN differentiate between vague and concrete texts:

| Type | Mean V | Examples |
|:-----|:------:|:---------|
| Concrete | 22.4 | "7nm chip achieving 10 TFLOPS at 45W", "99.99% uptime" |
| Vague | 100.0 | "AI-powered platform", "next-generation solutions" |
| Baseline | 87.5 | "Provider of services", "Developer of technology" |

---

## Interpretation for Thesis

### What V=87.5 Means

V=87.5 represents companies with **"informationless" descriptions**:
- Not trying to sound impressive (no buzzwords)
- Not sharing specific metrics (no data)
- Just stating what they do in plain terms

### Implications for Archetype Analysis

For companies stuck at V=87.5 across years:
- They are **stayers** by definition (D ≈ 0)
- Their "strategic commitment" measurement is uninformative
- Consider treating them as a separate "baseline" category

### Recommendations

1. **Document clearly** in thesis that 43% have baseline vagueness
2. **Sensitivity analysis**: Run decomposition excluding V=87.5 companies
3. **Consider alternative interpretation**: V=87.5 may indicate:
   - Very early stage (no story to tell yet)
   - Traditional business (not trying to attract VC attention)
   - Data limitation (PitchBook lacks detailed description)

---

## Test File Created

`test_vagueness_validation.py` can be run by another LLM for independent verification:

```bash
python3.11 src/scripts/paper_generation/papers_v3/4_T_commit2trap/test_vagueness_validation.py
```

All 5 tests pass:
- ✓ Formula verification
- ✓ Text differentiation
- ✓ Data distribution
- ✓ Source text analysis
- ✓ Expected range test

---

## Conclusion

**The data is valid.** V=87.5 is the natural score for 43% of company descriptions because PitchBook descriptions for many companies are:
- Factual but not data-rich
- Descriptive but not marketing-heavy
- "We do X" rather than "We revolutionize X with 99% efficiency"

This is a feature of the real-world data, not a bug in the scorer.

---

**Signed**: Claude Code
**Reviewed by**: 다른 LLM으로 검증 가능 (test_vagueness_validation.py)
