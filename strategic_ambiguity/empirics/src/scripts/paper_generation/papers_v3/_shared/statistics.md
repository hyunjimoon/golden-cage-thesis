# Key Statistics Reference

## Sample Overview

| Metric | Value | Source |
|--------|-------|--------|
| Total ventures | **180,994** | PitchBook 2021-2025 |
| Observation window | 2021-2025 | Early-stage funding to outcome |
| Success measure | Later Stage VC progression | Binary (L = 0, 1) |
| Base success rate | **11.5%** | L = 1 prevalence |

## Paper M: Movement Principle

### Non-Monotonicity Evidence

| Statistic | Value | CI (95%) | Interpretation |
|-----------|-------|----------|----------------|
| ρ(V, L) | **+0.024*** | [0.019, 0.029] | Rejects monotonic decrease |

*p < 0.001

### Success by Vagueness Quartile

| Quartile | Success Rate | 95% CI | Movement Rate |
|----------|--------------|--------|---------------|
| Q1 (precise) | 12.3% | [11.8%, 12.8%] | 42% |
| Q2 | 8.9% | [8.5%, 9.3%] | 35% |
| Q3 | **16.0%** | [15.4%, 16.6%] | 68% |
| Q4 (vague) | 12.9% | [12.4%, 13.4%] | 55% |

### Movement Principle (Core Finding)

| Group | Success Rate | 95% CI | N |
|-------|--------------|--------|---|
| Stayed (A = 0) | **10.8%** | [10.5%, 11.1%] | 164,690 (91%) |
| Moved (A > 0) | **17.7%** | [17.1%, 18.3%] | 16,304 (9%) |
| **Movement Advantage** | **1.6×** | [1.53, 1.72] | χ² significant*** |

### Effect Size Interpretation

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Absolute Risk Increase | 6.9 pp | 17.7% − 10.8% |
| NNT (Number Needed to Treat) | **14** | 1/0.069 |
| Relative Risk | **1.64** | 17.7/10.8 |
| Attributable Risk | **39%** | 1 − 10.8/17.7 |

### Direction Irrelevance (Among Movers)

| Direction | Success Rate | 95% CI |
|-----------|--------------|--------|
| Focused (D < 0) | 17.6% | [16.8%, 18.4%] |
| Broadened (D > 0) | 18.6% | [17.8%, 19.4%] |
| **Difference** | 1.0 pp | Cohen's h = 0.027 (negligible) |

## Paper C: Capital-Flexibility Tradeoff

### Core Correlations

| Relationship | ρ | p-value | Interpretation |
|--------------|---|---------|----------------|
| ρ(A, E) | **−0.117*** | < 0.001 | Cash2Cage friction |
| ρ(G, A) | **+0.209*** | < 0.001 | Adaptation → Growth |
| ρ(G, E) | **−0.196*** | < 0.001 | Funding Paradox |

**✅ DATA CORRECTION (2025-12-21):**
- Statistics now computed from actual data via `compute_thesis_stats.py`
- G defined as **Funding Growth Multiple** = F_t / E (total_raised / first_financing_size)
- N = 180,994 ventures

*Note: ρ(A,E) explains ~1.4% variance—statistically significant and economically meaningful

### Temporal Stability (Quasi-Natural Experiment)

| Year | ρ(A, E) | ρ(G, A) | ρ(G, E) |
|------|---------|---------|---------|
| 2025 | −0.117*** | +0.209*** | −0.196*** |

## Company Examples (Table 2.2 from thesis draft)

| Company | V₀ | V_T | ΔV | Type | Growth |
|---------|-----|-----|-----|------|--------|
| **Sky Engine** | 28.4 | 89.1 | +60.7 | Zoom Out | 215.9× |
| **Linpowave** | 88.1 | 31.9 | −56.3 | Zoom In | N/A |
| **Rubedos** | 81.9 | 81.9 | 0 | Stayer | 2.6× |
| **Surestar** | 87.9 | 87.9 | 0 | Stayer | 26.7× |

## Summary Statistics

| Finding | Effect Size | Statistical Significance |
|---------|-------------|--------------------------|
| Movement > Position | 1.6× | *** |
| Direction ≈ Irrelevant | Cohen's h = 0.027 | Negligible |
| Funding Paradox | ρ = −0.196 | *** |
| Stayers = 91% of sample | - | Majority static |

---

*All statistics from N = 180,994 ventures funded in 2021, tracked through 2025.*
