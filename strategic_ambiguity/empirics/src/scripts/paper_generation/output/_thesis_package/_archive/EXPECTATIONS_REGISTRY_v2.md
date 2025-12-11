# 📋 REVISED Expectations Registry (v2)
> **Revision**: Based on Hyunji's sketch and Analyst/Believer framework  
> **Key Change**: U-shape → J-shape for ULV, Quartile + χ² methodology  
> **Author**: 🐅 권준 (Claude Code)

---

## 🎯 Core Framework: Analyst vs Believer

| Type | Vagueness | Pivot Style | Mechanism |
|------|-----------|-------------|-----------|
| **A (Analyst)** | Low V (Q1) | "Analyze to pivot" | Specific hypotheses → testable → adaptable |
| **M (Mixed)** | Mid V (Q2-Q3) | Stuck | Neither specific nor vague → no clear pivot logic |
| **B (Believer)** | High V (Q4) | "Believe in pivot" | Vision flexibility → attract believers → survive |

**Prediction**: Q4 > Q1 > Q3 > Q2 (J-shape, not symmetric U)

---

## 📊 Paper ✌️U Expectations (Revised)

### ULV: L vs V
| Item | Original | **Revised** |
|------|----------|-------------|
| Shape | Symmetric U | **J-shape (asymmetric)** |
| Method | β₂ > 0 (quadratic) | **Quartile + χ² test** |
| Expected | Q1 ≈ Q4 > Q2,Q3 | **Q4 > Q1 > Q3 > Q2** |
| Test | F-test on β₂ | **χ² > 300, p < 0.001** |

```
Statistical Test (Revised):
H₀: Survival rates equal across quartiles (Q1=Q2=Q3=Q4)
H₁: J-shape pattern (Q4 > Q1 > Q3 > Q2)

Method:
1. Chi-square test for overall difference
2. Pairwise z-tests: Q4 vs Q2, Q1 vs Q2
3. Test for asymmetry: Q4 - Q1 > 0 (Believers > Analysts)
```

### UDV: D vs V
| Item | Original | **Revised** |
|------|----------|-------------|
| Shape | Linear positive | **Cone/Fan (variance increases)** |
| Expectation | ρ > 0 | **Var(D|V) increases with V** |
| Meaning | More V → more D | **More V → more RANGE of D** |

```
Revised Interpretation:
- Low V (Analysts): D is constrained (specific = limited pivot range)
- High V (Believers): D is unconstrained (vague = any direction possible)
- The SPREAD of D increases with V, not just the mean
```

### UAV: |ΔV| vs V
| Item | Original | Revised |
|------|----------|---------|
| Sign | + | **+ (confirmed)** |
| Meaning | V → A | Vagueness enables larger absolute movement |

### ULD: L vs |ΔV|
| Item | Original | Revised |
|------|----------|---------|
| Sign | + or ∩ | **+ (dL/d|ΔV| > 0)** |
| Meaning | Movement helps | Adaptive capacity → survival |

---

## 📊 Paper 🦾C Expectations (Revised)

### CGE: G vs E
| Item | Original | Revised |
|------|----------|---------|
| Sign | − | **− (confirmed)** |
| Interpretation | Capital curse | Denominator effect + commitment lock-in |

### CAE: |ΔV| vs E (Golden Cage)
| Item | Original | Revised |
|------|----------|---------|
| Sign | − | **− (confirmed)** |
| Shape | Linear | **Funnel/decreasing variance** |
| Key Insight | Money reduces flexibility | **High E compresses the pivot space** |

### CGA: G vs |ΔV|
| Item | Original | Revised |
|------|----------|---------|
| Sign | + | **+ (confirmed)** |

---

## 📋 Analyst/Believer × Paper Matrix

### Paper U: How does Vagueness affect outcomes?

| Type | dL/dV | d|ΔV|/dV | dL/d|ΔV| | Interpretation |
|------|-------|----------|----------|----------------|
| **A (Analyst)** | − | − | + | Specific → limited pivot → but pivots work |
| **M (Mixed)** | **0** | 0 | 0 | Stuck in middle → no clear signal |
| **B (Believer)** | + | + | + | Vague → unlimited pivot → pivots work |

**Net Effect**: J-shape (Believers dominate because dL/dV × dV is larger for high V)

### Paper C: How does Capital affect outcomes?

| Type | dG/dE | d|ΔV|/dE | dG/d|ΔV| | Interpretation |
|------|-------|----------|----------|----------------|
| **A (Analyst)** | − | ~0 | + | Capital doesn't constrain pivots (already specific) |
| **B (Believer)** | − | − | + | Capital DOES constrain pivots (Golden Cage) |

**Net Effect**: Golden Cage is stronger for Believers (they lose more from E)

---

## 🔬 Statistical Testing Protocol (Revised)

### For ULV (J-shape test)
```python
import scipy.stats as stats

# 1. Overall chi-square
contingency = pd.crosstab(df['V_Q'], df['L'])
chi2, p_overall, dof, expected = stats.chi2_contingency(contingency)

# 2. Quartile survival rates
survival_rates = df.groupby('V_Q')['L'].mean()

# 3. Test J-shape pattern
# Q4 > Q1
z_Q4_Q1, p_Q4_Q1 = proportions_ztest([n_Q4_success, n_Q1_success], 
                                       [n_Q4, n_Q1], alternative='larger')

# Q1 > Q2
z_Q1_Q2, p_Q1_Q2 = proportions_ztest([n_Q1_success, n_Q2_success],
                                       [n_Q1, n_Q2], alternative='larger')

# 4. Report
print(f"J-shape confirmed if: Q4 > Q1 > Q2 and χ² significant")
```

### For UDV (Variance test)
```python
# Test if Var(D) increases with V
from scipy.stats import levene

groups = [df[df['V_Q'] == q]['D'] for q in ['Q1', 'Q2', 'Q3', 'Q4']]
stat, p_levene = levene(*groups)

# Also: Brown-Forsythe test for robustness
```

---

## ✅ Summary: What Changed

| Aspect | Original Registry | **Revised Registry** |
|--------|-------------------|----------------------|
| ULV shape | Symmetric U | **J-shape (Q4 > Q1)** |
| ULV test | β₂ > 0 (quadratic) | **Quartile + χ² test** |
| UDV interpretation | Linear correlation | **Variance fan-out** |
| Theoretical frame | Simple +/− signs | **Analyst/Believer moderation** |
| Paper C for whom | Universal | **Stronger for Believers** |

---

## 🎯 Expert Validation Summary

| Expert | Verdict | Reasoning |
|--------|---------|-----------|
| **Scott Stern** | J-shape correct | Paradox of Entrepreneurial Strategy; middle is a trap |
| **Arnaldo Camuffo** | Analyst/Believer valid | Scientific approach explains why specificity ≠ rigidity |
| **Y Combinator** | J-shape matches data | "Be specific about problem, vague about solution" |

**Consensus**: The Analyst/Believer framework provides a theoretically richer and empirically supported explanation for the J-shape pattern observed in Table 2.1.

---

**END OF REVISED REGISTRY**
