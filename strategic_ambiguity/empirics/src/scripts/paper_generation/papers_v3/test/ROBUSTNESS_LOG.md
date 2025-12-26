# Robustness Testing Log

**Date**: 2025-12-18
**Purpose**: Document all robustness checks and data validation attempts for thesis empirics

---

## 1. G Variable Definition Issue

### Problem Discovered
The original code used:
```python
panel['G'] = panel['GrowthRate'].fillna(panel['growth'])
```

**Issues:**
1. `growth` column is **BINARY** (0 or 1), not continuous
2. `GrowthRate` is PitchBook's employee/web traffic metric, NOT funding growth
3. Fallback to binary corrupted 71% of G values

### Correct Definition (Thesis)
```
G = F_t / E = total_raised / first_financing_size
```

### Validation Results

| Metric | Before Fix | After Fix |
|--------|-----------|-----------|
| G available | 41% (74,857) | 100% (180,994) |
| G = 0 | 71% | 3% |
| ρ(G, E) | +0.025 (n.s.) | **−0.196***|
| ρ(G, A) | +0.012** | **+0.209*** |

---

## 2. Two G Definitions Comparison

### G_funding (Thesis Definition)
- **Formula**: G = total_raised / first_financing_size
- **Interpretation**: Funding growth multiple
- **N**: 180,860

### G_pitchbook (PitchBook's GrowthRate)
- **Formula**: Employee/web traffic growth (proprietary)
- **Interpretation**: Operational growth
- **N**: 74,857 (41% available)

### Thesis Argument Support

| Argument | G_funding | G_pitchbook |
|----------|-----------|-------------|
| Capital Paradox (ρ(G,E) < 0) | ✅ −0.196*** | ❌ +0.025 |
| Adaptation→Growth (ρ(G,A) > 0) | ✅ +0.209*** | ✅ +0.012** |
| Cash2Cage (ρ(A,E) < 0) | ✅ −0.117*** | ✅ −0.087*** |

### dG/dE by Archetype

**G_funding (all negative):**
| Archetype | dG/dE | Sig |
|-----------|-------|-----|
| zoom_in | −0.25 | *** |
| zoom_out | −0.28 | *** |
| stayer | −0.24 | *** |
| horizontal | −0.28 | *** |

**G_pitchbook (all positive):**
| Archetype | dG/dE | Sig |
|-----------|-------|-----|
| zoom_in | +0.05 | * |
| zoom_out | +0.03 | * |
| stayer | +0.03 | *** |
| horizontal | +0.01 | n.s. |

---

## 3. Selection Bias in GrowthRate Data

### Key Finding
Companies with GrowthRate data are **systematically different**:

| Metric | Has GrowthRate | No GrowthRate |
|--------|---------------|---------------|
| N | 74,857 | 106,137 |
| Success Rate (L) | **25.8%** | **1.3%** |
| Stayer % | 85% | 95% |

**Interpretation**: GrowthRate is only tracked for successful, well-monitored companies. This creates survivorship bias that masks the Capital Paradox.

---

## 4. Diagnostic Plots Generated

| Plot | File | Purpose |
|------|------|---------|
| 2x3 Comparison | `diagnostic_growthrate_comparison.png` | Side-by-side thesis tests |
| dG/dE Slopes | `diagnostic_dGdE_by_archetype.png` | Archetype decomposition |
| Selection Bias | `diagnostic_selection_bias.png` | Who has GrowthRate? |

---

## 5. Paradox Resolution

### Original Paradox Question
> If dG/dE by archetype are mostly positive (weighted average), how can rho(G,E) < 0 overall?

### Answer
**No paradox exists.** The original correlations were based on corrupted G data.

With correct G = total_raised / E:
- ρ(G, E) = **−0.196*** (Capital Paradox CONFIRMED)
- All archetypes show negative dG/dE
- No Simpson's Paradox needed

---

## 6. Files Modified

| File | Change |
|------|--------|
| `generate_thesis_nc_files.py` | G = total_raised / E |
| `thesis_panel_v3.nc` | Regenerated with correct G |
| `statistics.md` | Updated correlations |
| `LINEAGE.md` | Documented G definition |

---

## 7. Recommended Robustness Checks for Paper

1. **Primary analysis**: G_funding (correct definition, N=180,860)
2. **Robustness check**: G_pitchbook (report with selection bias caveat)
3. **Subsample analysis**: Restrict to companies with both measures
4. **Temporal stability**: Compute correlations by year (pending)

---

## 8. Key Insight for Theory

**Why G_funding shows Capital Paradox but G_pitchbook doesn't:**

| Measure | What it captures | Capital Paradox? |
|---------|-----------------|------------------|
| G_funding | Investor willingness to provide follow-on capital | ✅ Yes (−0.196) |
| G_pitchbook | Operational growth (employees, web traffic) | ❌ No (+0.025) |

**Interpretation**: The Capital Paradox is specific to **capital allocation dynamics**, not general firm performance. Companies with large early funding:
- Have **lower funding multiples** (investors already committed)
- But may still have **higher operational growth** (more resources)

This distinction strengthens the thesis by showing the paradox is about **investor behavior**, not firm capability.

---

*Last updated: 2025-12-18*
