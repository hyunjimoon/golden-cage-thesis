# 📋 Seven-Plot Expectations Registry
> **Purpose**: Document theoretical expectations BEFORE running empirical analysis  
> **Methodology**: Pre-registration of hypotheses for scientific rigor  
> **Author**: 🐅 권준 (Claude Code)

---

## 🎯 Core Thesis Reminder

**Paper U**: "Strategic vagueness has a U-shaped relationship with venture success"
**Paper C**: "Early capital creates a 'Golden Cage' by reducing adaptive capacity"

**Causal Chain**: 
```
E (Capital) → (-) → A (Flexibility) → (+) → G (Growth)
Therefore: E → (-) → G (The Golden Cage Paradox)
```

---

## 📊 Expectations Table

### Part 1: Paper ✌️U (Vagueness & Survival)

| Plot | X → Y | Expected Sign | Shape | Null Hypothesis (H₀) | Alternative (H₁) | Theoretical Justification |
|------|-------|---------------|-------|---------------------|------------------|---------------------------|
| **ULV** | V → L | **U-shape** | ∪ | β₂ = 0 (linear) | β₂ > 0 (U-shape) | Both extreme clarity (focused execution) and extreme vagueness (maximal optionality) outperform the "murky middle" |
| **UDV** | V → D | **+** | Linear | ρ = 0 | ρ > 0 | High initial vagueness provides more "room to move" in positioning space |
| **UAV** | V → A | **+** | Linear/Convex | ρ = 0 | ρ > 0 | Vague positioning enables larger absolute strategic pivots |
| **ULD** | D → L | **∩ or +** | Inverted-U or Linear | β = 0 | β ≠ 0 | Moderate repositioning signals learning; extreme repositioning may signal desperation |

### Part 2: Paper 🦾C (Capital-Flexibility-Growth)

| Plot | X → Y | Expected Sign | Shape | Null Hypothesis (H₀) | Alternative (H₁) | Theoretical Justification |
|------|-------|---------------|-------|---------------------|------------------|---------------------------|
| **CGE** | E → G | **−** | Log-linear | ρ ≥ 0 | ρ < 0 | High early capital leads to lower growth multiples (denominator effect + commitment lock-in) |
| **CAE** | E → A | **−** ⭐ | Log-linear | ρ ≥ 0 | ρ < 0 | **THE GOLDEN CAGE**: Money buys commitment, not flexibility. Funded startups pivot less. |
| **CGA** | A → G | **+** | Linear | ρ ≤ 0 | ρ > 0 | Flexibility enables value creation. Startups that can adapt grow faster. |

---

## 🔬 Statistical Testing Protocol

### For Each Plot:

```python
# 1. Correlation Test
from scipy import stats

# Pearson (linear relationship)
r_pearson, p_pearson = stats.pearsonr(x, y)

# Spearman (monotonic relationship, robust to outliers)
r_spearman, p_spearman = stats.spearmanr(x, y)

# 2. Regression with Confidence Intervals
import statsmodels.formula.api as smf

# Linear model
model_linear = smf.ols('Y ~ X', data=df).fit()

# Quadratic model (for U-shape test)
model_quad = smf.ols('Y ~ X + I(X**2)', data=df).fit()

# 3. U-Shape Confirmation (for ULV)
# H₀: β₂ = 0 (linear)
# H₁: β₂ > 0 (U-shape)
beta2 = model_quad.params['I(X ** 2)']
p_beta2 = model_quad.pvalues['I(X ** 2)']
is_u_shape = (beta2 > 0) and (p_beta2 < 0.05)
```

---

## ✅ Pre-Registration Checklist

Before running analysis, confirm these expectations:

### Plot 1: ULV (L vs V)
- [ ] Expected: U-shape (β₂ > 0)
- [ ] Mechanism: "Murky middle" underperforms extremes
- [ ] Test: Quadratic term significance
- [ ] Visualization: Polynomial fit with 95% CI

### Plot 2: UDV (D vs V)  
- [ ] Expected: Positive correlation (ρ > 0)
- [ ] Mechanism: Vague positioning = more movement room
- [ ] Test: Pearson/Spearman correlation
- [ ] Visualization: Scatter + linear trend

### Plot 3: UAV (A vs V)
- [ ] Expected: Positive correlation (ρ > 0)
- [ ] Mechanism: Vagueness enables larger pivots
- [ ] Test: Correlation + slope significance
- [ ] Visualization: Binned scatter + regression

### Plot 4: ULD (L vs D)
- [ ] Expected: Inverted-U or positive
- [ ] Mechanism: Learning signal vs desperation signal
- [ ] Test: Linear and quadratic models
- [ ] Visualization: Logistic-style curve

### Plot 5: CGE (G vs E)
- [ ] Expected: Negative correlation (ρ < 0)
- [ ] Mechanism: Denominator effect + commitment
- [ ] Test: Log-log regression
- [ ] Visualization: Log-scale scatter

### Plot 6: CAE (A vs E) ⭐ KEY
- [ ] Expected: **Negative correlation (ρ < 0)**
- [ ] Mechanism: **GOLDEN CAGE** - money reduces flexibility
- [ ] Test: One-tailed test for negative slope
- [ ] Visualization: Decile binning + CI bands

### Plot 7: CGA (G vs A)
- [ ] Expected: Positive correlation (ρ > 0)
- [ ] Mechanism: Flexibility enables growth
- [ ] Test: Correlation + slope significance
- [ ] Visualization: Scatter + linear trend

---

## 📈 Decision Rules

### Confirmation Criteria
| Result | Interpretation | Action |
|--------|----------------|--------|
| Sign matches & p < 0.05 | **Strong support** | Report as main finding |
| Sign matches & 0.05 < p < 0.10 | **Weak support** | Report with caveat |
| Sign matches & p > 0.10 | **Directional support** | Note trend, need more data |
| Sign opposite & p < 0.05 | **Contradiction** | Investigate mechanism |
| No significant relationship | **Null result** | Report honestly |

### Effect Size Thresholds (Cohen's conventions)
| |r| | Interpretation |
|-----|----------------|
| < 0.10 | Negligible |
| 0.10 - 0.30 | Small |
| 0.30 - 0.50 | Medium |
| > 0.50 | Large |

---

## 🎨 Visualization Standards

### Color Coding by Expectation Match
```python
COLORS = {
    'confirmed': '#27ae60',      # Green - matches expectation
    'contradicted': '#e74c3c',   # Red - opposite of expectation
    'inconclusive': '#f39c12',   # Orange - not significant
    'neutral': '#3498db',        # Blue - data points
}
```

### Annotation Template
```python
# On each plot, include:
annotation = f"""
Expected: {expected_sign}
Observed: r = {r:.3f}{stars}
Result: {'✓ CONFIRMED' if matches else '✗ CONTRADICTED'}
"""
```

---

## 📝 Summary Matrix

| Plot | Variable Pair | Expected | If Confirmed | If Contradicted |
|------|--------------|----------|--------------|-----------------|
| ULV | V → L | ∪ U-shape | Murky middle penalty validated | Linear learning model |
| UDV | V → D | + | Vagueness enables movement | Commitment constraints |
| UAV | V → A | + | Optionality theory | Discipline hypothesis |
| ULD | D → L | + or ∩ | Adaptation rewards | Stability rewards |
| CGE | E → G | − | Capital curse | Capital blessing |
| **CAE** | **E → A** | **−** | **Golden Cage confirmed** | **Capital enables pivots** |
| CGA | A → G | + | Flexibility thesis | Commitment thesis |

---

**END OF EXPECTATIONS REGISTRY**

*This document serves as pre-registration for the empirical analysis. All expectations documented BEFORE examining results.*
