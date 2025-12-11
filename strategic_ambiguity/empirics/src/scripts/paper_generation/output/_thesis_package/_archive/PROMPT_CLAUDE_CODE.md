# 🐅 Claude Code Prompt: 7-Plot Generation for Thesis

> **Author**: 권준/나대용 (🐅 중군)  
> **Mission**: Generate 7 publication-ready plots for Papers U and C  
> **Quality Standard**: Production-ready for Charlie Fine & Scott Stern

---

## 📍 Data & Environment Context

### File Paths
```
ROOT = /Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics

Data Sources:
- Panel data: {ROOT}/data/processed/vagueness_timeseries.parquet (or .csv)
- If unavailable: Generate synthetic data following theoretical relationships

Output Locations:
- Paper U figures: {ROOT}/src/scripts/paper_generation/output/✌️U/⚙️process/figures/
- Paper C figures: {ROOT}/src/scripts/paper_generation/output/🦾C/⚙️process/figures/
- Unified figures: {ROOT}/src/scripts/paper_generation/output/_thesis_package/figures/
```

### Actual Data Structure (vagueness_timeseries.parquet)

**File**: `{DATA_DIR}/vagueness_timeseries.parquet`
**Format**: Long (panel) format
**N**: 1,635,136 rows (408,784 companies × 4 years)
**Years**: 2021, 2023, 2024, 2025

| Column | Type | Range | Description |
|--------|------|-------|-------------|
| `company_id` | object | - | Unique identifier |
| `year` | int64 | 2021-2025 | Observation year |
| `V` | float64 | [7.46, 97.08] | Vagueness score |
| `delta_V` | float64 | [-73.93, 80.04] | Year-over-year change |
| `total_delta_V` | float64 | [-74.36, 80.47] | Cumulative change from baseline |
| `first_financing_size` | float64 | [0, 58640] | Early capital ($M), 44% coverage |
| `description` | object | - | Company description |
| `company_name` | object | - | Company name |

### Variable Mapping (Long → Cross-sectional)

| Target Variable | Source | Transformation |
|-----------------|--------|----------------|
| **V** (Initial Vagueness) | `V` where `year=2021` | Direct |
| **V_L** (Late Vagueness) | `V` where `year=2025` | Direct |
| **E** (Early Capital) | `first_financing_size` | Direct |
| **D** (Directional Change) | `total_delta_V` where `year=2025` | Direct |
| **A** (Adaptive Capacity) | `abs(D)` | Computed |
| **L** (Survival) | Exists in 2025 | Proxy (all =1 in this dataset) |
| **G** (Growth) | Estimated from A, E | Proxy |

### Data Preprocessing Code
```python
# Step 1: Load panel data
df = pd.read_parquet('data/processed/vagueness_timeseries.parquet')

# Step 2: Extract cross-sectional features
df_2021 = df[df['year'] == 2021][['company_id', 'V', 'first_financing_size']]
df_2021.columns = ['company_id', 'V', 'E']

df_2025 = df[df['year'] == 2025][['company_id', 'V', 'total_delta_V']]
df_2025.columns = ['company_id', 'V_L', 'D']

# Step 3: Merge
cross_df = df_2021.merge(df_2025, on='company_id', how='inner')

# Step 4: Compute derived variables
cross_df['A'] = cross_df['D'].abs()  # Adaptive Capacity = |ΔV|
cross_df['E_log'] = np.log10(cross_df['E'].clip(lower=0.01))  # Log-transform

# Note: L and G are proxied since actual survival/funding data requires merger with Crunchbase
```

---

## 📊 The 7 Required Plots

### Part 1: Paper ✌️U (Vagueness & Survival)

#### Plot 1: ULV — L vs V (U-Shape Test)
```
Question: Does vagueness have a U-shaped relationship with survival?
X-axis: V (Vagueness Score, 0-100)
Y-axis: L (Survival Probability)

Statistical Requirements:
- Fit: Logistic regression with quadratic term: logit(L) = β₀ + β₁V + β₂V²
- Test: H₀ (linear): β₂ = 0 vs H₁ (U-shape): β₂ > 0
- Visual: Binned scatter + polynomial fit with 95% CI
- Annotation: Report β₂, p-value, and McFadden R²
```

#### Plot 2: UDV — D vs V
```
Question: Does initial vagueness predict directional change?
X-axis: V (Initial Vagueness)
Y-axis: D (Directional Change, signed)

Statistical Requirements:
- Fit: OLS regression: D = α₀ + α₁V + ε
- Test: Direction of α₁
- Visual: Scatter with linear fit + 95% CI
- Annotation: Pearson r, Spearman ρ, p-value
```

#### Plot 3: UAV — A vs V
```
Question: Does starting vague allow for MORE absolute movement?
X-axis: V (Initial Vagueness)
Y-axis: A (Adaptive Capacity = |D|)

Statistical Requirements:
- Fit: OLS or polynomial: A = γ₀ + γ₁V + γ₂V² + ε
- Visual: Binned scatter + fitted curve
- Annotation: Correlation coefficient, p-value
```

#### Plot 4: ULD — L vs D
```
Question: Does directional change predict survival?
X-axis: D (Directional Change)
Y-axis: L (Survival Probability)

Statistical Requirements:
- Fit: Logistic regression
- Visual: Scatter + logistic curve
- Annotation: Odds ratio interpretation
```

### Part 2: Paper 🦾C (Capital-Flexibility-Growth)

#### Plot 5: CGE — G vs E (Capital → Growth)
```
Question: Does early capital predict growth?
X-axis: E (Early Capital, log-scale recommended)
Y-axis: G (Growth Ratio = (F_t - E) / E)

Statistical Requirements:
- Fit: Log-linear: log(G+1) = δ₀ + δ₁·log(E) + ε
- Visual: Log-log scatter with regression line
- Annotation: Elasticity interpretation, R²
```

#### Plot 6: CAE — A vs E (The Golden Cage Plot) ⭐ KEY FIGURE
```
Question: Does early capital REDUCE adaptive capacity?
X-axis: E (Early Capital, log-scale)
Y-axis: A (Adaptive Capacity = |ΔV|)

Theoretical Expectation: HIGH E → LOW A ("Money buys commitment, not flexibility")

Statistical Requirements:
- Fit: Log-linear: A = λ₀ + λ₁·log(E) + ε
- Test: H₀: λ₁ ≥ 0 vs H₁: λ₁ < 0 (one-tailed)
- Visual: Decile binning + regression line with shaded CI
- Annotation: Correlation, p-value, effect size
```

#### Plot 7: CGA — G vs A (Flexibility → Growth)
```
Question: Does adaptive capacity drive growth?
X-axis: A (Adaptive Capacity)
Y-axis: G (Growth Ratio)

Theoretical Expectation: HIGH A → HIGH G ("Flexibility enables value creation")

Statistical Requirements:
- Fit: Linear: G = μ₀ + μ₁·A + ε
- Test: H₀: μ₁ ≤ 0 vs H₁: μ₁ > 0
- Visual: Scatter with linear fit
- Annotation: Correlation, p-value
```

---

## 🎨 Visualization Standards (Production-Ready)

### Figure Quality
```python
# Apply these settings at the TOP of the script
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams.update({
    'figure.figsize': (10, 6),
    'figure.dpi': 300,
    'font.size': 11,
    'font.family': 'DejaVu Sans',
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'axes.titleweight': 'bold',
    'axes.grid': True,
    'grid.alpha': 0.3,
    'legend.fontsize': 10,
    'savefig.bbox': 'tight',
    'savefig.facecolor': 'white',
})
```

### Statistical Annotations
Every plot MUST include:
1. **Correlation coefficient** (Pearson r or Spearman ρ)
2. **P-value** with significance stars: *** p<0.001, ** p<0.01, * p<0.05
3. **Sample size** (N = X)
4. **95% Confidence Interval** (shaded region)

### Color Scheme
```python
COLORS = {
    'primary': '#3498db',      # Blue for data points
    'positive': '#27ae60',     # Green for positive relationships
    'negative': '#e74c3c',     # Red for negative relationships
    'neutral': '#95a5a6',      # Gray for reference
    'highlight': '#f39c12',    # Orange for key findings
}
```

### Handling Large N (N > 100,000)
```python
# Option A: Transparency
ax.scatter(x, y, alpha=0.05, s=5)

# Option B: Hexbin (recommended)
ax.hexbin(x, y, gridsize=30, cmap='Blues', mincnt=1)

# Option C: Decile binning (best for presentation)
df['x_decile'] = pd.qcut(df['x'], 10, labels=False)
binned = df.groupby('x_decile').agg({'x': 'median', 'y': ['mean', 'std', 'count']})
```

---

## 📁 Deliverable: Complete Python Script

Generate a SINGLE Python script that:
1. Loads data from the specified parquet/csv path
2. Computes all derived variables (A, D, G)
3. Creates all 7 figures in sequence
4. Saves each figure to the appropriate output directory
5. Prints a summary of statistical findings

### Expected Output Files
```
✌️U/⚙️process/figures/
├── fig_ULV_survival_vs_vagueness.png
├── fig_UDV_direction_vs_vagueness.png
├── fig_UAV_adaptive_vs_vagueness.png
└── fig_ULD_survival_vs_direction.png

🦾C/⚙️process/figures/
├── fig_CGE_growth_vs_capital.png
├── fig_CAE_adaptive_vs_capital.png    # Golden Cage
└── fig_CGA_growth_vs_adaptive.png
```

---

## ✅ Verification Checklist

Before completing, verify:
- [ ] All 7 plots generated without errors
- [ ] Each plot has proper axis labels (V, E, L, D, A, G)
- [ ] Statistical annotations present on all plots
- [ ] 95% CI bands visible on regression lines
- [ ] Files saved to correct directories
- [ ] Console output summarizes key findings

---

**END OF PROMPT**

*This prompt was structured by 🐅 권준 (Claude) following the 사(思)·조(造) methodology for Scott Stern (strategic convergence) and Charlie Fine (operational rigor).*
