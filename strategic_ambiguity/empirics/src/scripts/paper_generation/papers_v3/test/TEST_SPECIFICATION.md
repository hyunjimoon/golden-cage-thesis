# Data Validation Test Specification

## Philosophy: Simulation-Based Calibration Mindset

Given your expertise in SBC, these tests follow the principle:
**"If the data generation process is correct, the posterior should recover the prior."**

Translated to our context:
**"If the raw-to-processed pipeline is correct, derived statistics should match source truth."**

---

## Test Categories

### 1. **Identity Tests** (Raw → Processed Consistency)
Verify that processed data exactly matches raw data for unchanged fields.

| Test ID | Description | Expected |
|---------|-------------|----------|
| `T1.1` | Company count: raw vs processed | Exact match |
| `T1.2` | E values match first_financing_size | Exact match |
| `T1.3` | V values match vagueness scores | Exact match |
| `T1.4` | Year filtering preserves correct companies | Set equality |

### 2. **Transformation Tests** (Algebraic Correctness)
Verify computed variables follow their definitions.

| Test ID | Description | Formula | Tolerance |
|---------|-------------|---------|-----------|
| `T2.1` | D = V_T - V_0 | ∀i: D[i] = V_T[i] - V_0[i] | ε = 1e-10 |
| `T2.2` | A = |D| | ∀i: A[i] = |D[i]| | ε = 1e-10 |
| `T2.3` | G = total_raised / E | ∀i: G[i] = F_t[i] / E[i] | ε = 1e-6 |
| `T2.4` | L = "Later Stage VC" indicator | Boolean match | Exact |

### 3. **Classification Tests** (Archetype Correctness)
Verify mover classification follows exact rules.

| Test ID | Description | Rule |
|---------|-------------|------|
| `T3.1` | Stayer classification | A < 5 → stayer |
| `T3.2` | Zoom-in classification | A ≥ 5 AND D < -10 → zoom_in |
| `T3.3` | Zoom-out classification | A ≥ 5 AND D > 10 → zoom_out |
| `T3.4` | Horizontal classification | A ≥ 5 AND -10 ≤ D ≤ 10 → horizontal |
| `T3.5` | Partition completeness | All companies classified exactly once |

### 4. **Statistical Invariance Tests** (Reproducibility)
Verify key statistics are reproducible from raw data.

| Test ID | Description | Expected | Tolerance |
|---------|-------------|----------|-----------|
| `T4.1` | N after E filter | 180,860 ± 500 | 0.3% |
| `T4.2` | L base rate | 11.5% ± 0.5% | 0.5pp |
| `T4.3` | ρ(G, E) | -0.196 ± 0.02 | 0.02 |
| `T4.4` | ρ(G, A) | +0.209 ± 0.02 | 0.02 |
| `T4.5` | ρ(A, E) | -0.117 ± 0.02 | 0.02 |

### 5. **Distributional Tests** (Shape Preservation)
Verify distributions haven't been distorted.

| Test ID | Description | Test |
|---------|-------------|------|
| `T5.1` | V_0 range | [0, 100] |
| `T5.2` | V_T range | [0, 100] |
| `T5.3` | D range | [-100, 100] |
| `T5.4` | A range | [0, 100] |
| `T5.5` | G positivity | G ≥ 0 (or NaN) |
| `T5.6` | L binary | L ∈ {0, 1} |

### 6. **Merge Integrity Tests** (Join Correctness)
Verify data merges preserve information correctly.

| Test ID | Description | Check |
|---------|-------------|-------|
| `T6.1` | No duplicate company_ids | unique(company_id) = n_rows |
| `T6.2` | All V_0 companies have V_T | inner join completeness |
| `T6.3` | Feature merge doesn't inflate N | post-merge N ≤ pre-merge N |
| `T6.4` | No orphan records | all rows have valid company_id |

### 7. **Temporal Consistency Tests** (Year Logic)
Verify year-based filtering is correct.

| Test ID | Description | Check |
|---------|-------------|-------|
| `T7.1` | V_0 from 2021 only | all V_0 rows have year=2021 |
| `T7.2` | V_T from 2025 only | all V_T rows have year=2025 |
| `T7.3` | No 2022 data (known gap) | year ≠ 2022 |
| `T7.4` | Timeline makes sense | V_T measured after V_0 |

### 8. **Edge Case Tests** (Boundary Conditions)
Verify handling of edge cases.

| Test ID | Description | Check |
|---------|-------------|-------|
| `T8.1` | E = 0 handling | G = NaN when E = 0 |
| `T8.2` | Missing total_raised | G = 1.0 when total_raised is NaN but E exists |
| `T8.3` | NaN propagation | NaN in input → NaN in output (not 0) |
| `T8.4` | Inf prevention | No infinite values in G |

### 9. **Cross-Validation Tests** (Multiple Sources)
Verify consistency across data sources.

| Test ID | Description | Check |
|---------|-------------|-------|
| `T9.1` | E in vagueness_ts matches E in features | Same values |
| `T9.2` | Company IDs consistent | Same format/type |
| `T9.3` | total_raised in features_all | Non-negative |

### 10. **Regression Tests** (Backward Compatibility)
Verify key results haven't changed unexpectedly.

| Test ID | Description | Baseline |
|---------|-------------|----------|
| `T10.1` | Mover success rate | ~17.7% |
| `T10.2` | Stayer success rate | ~10.8% |
| `T10.3` | Movement advantage | ~1.6x |
| `T10.4` | Stayer proportion | ~91% |

---

## Test Severity Levels

| Level | Description | Action |
|-------|-------------|--------|
| **CRITICAL** | Data integrity compromised | Block all analysis |
| **ERROR** | Results may be incorrect | Investigate immediately |
| **WARNING** | Unexpected but not fatal | Log for review |
| **INFO** | Informational check | Note in report |

---

## Implementation Notes

### SBC-Inspired Rank Statistics
For continuous variables, we can compute:
```python
def rank_test(computed, expected, n_bins=20):
    """
    SBC-style uniformity test.
    If transformation is correct, ranks should be uniform.
    """
    ranks = (computed < expected).mean()  # Should be ~0.5
    return abs(ranks - 0.5) < 0.1  # Tolerance
```

### Coverage Tests
For interval estimates:
```python
def coverage_test(ci_low, ci_high, true_value, target=0.95):
    """
    CI should cover true value ~95% of time.
    """
    covered = (ci_low <= true_value) & (true_value <= ci_high)
    return covered.mean() >= target - 0.05
```

---

## Output Format

```
================================================================================
DATA VALIDATION REPORT
================================================================================
Timestamp: 2025-12-18 18:00:00
Data Version: thesis_panel_v3.nc

CRITICAL TESTS: 0 FAILED / 10 PASSED
ERROR TESTS:    0 FAILED / 15 PASSED
WARNING TESTS:  2 FLAGGED / 8 PASSED
INFO TESTS:     10 PASSED

--------------------------------------------------------------------------------
DETAILED RESULTS
--------------------------------------------------------------------------------
[PASS] T1.1 Company count consistency: 180,994 == 180,994
[PASS] T2.1 D = V_T - V_0: max_error = 0.0
[PASS] T4.3 ρ(G, E) = -0.196: actual = -0.196
[WARN] T5.5 G positivity: 134 negative values (0.07%)
...

================================================================================
OVERALL STATUS: PASS (with warnings)
================================================================================
```
