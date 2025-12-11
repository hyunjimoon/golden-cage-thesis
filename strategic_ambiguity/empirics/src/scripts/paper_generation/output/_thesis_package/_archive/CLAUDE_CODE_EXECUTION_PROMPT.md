# 🎯 CLAUDE CODE MASTER EXECUTION PROMPT
## End-to-End: Data → Figures → Thesis Text

> **Mission**: Generate 7 publication-ready figures and write empirical module paragraphs
> **Quality**: Production-ready for advisors (Charlie Fine, Scott Stern)
> **Output**: Figures (.png) + Thesis text (.md) for ✌️U ¶25-32 and 🦾C ¶57-64

---

## 📁 FILE PATHS

```python
# Root
ROOT = "/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics"

# Input
DATA = f"{ROOT}/data/processed/vagueness_timeseries.parquet"

# Output
FIG_DIR = f"{ROOT}/src/scripts/paper_generation/output/_thesis_package/figures"
TEXT_DIR = f"{ROOT}/src/scripts/paper_generation/output/_thesis_package/text"
```

---

## 📊 DATA STRUCTURE

### Source: `vagueness_timeseries.parquet` (Panel format)
| Column | Type | Description |
|--------|------|-------------|
| `company_id` | str | Unique identifier |
| `year` | int | 2021, 2023, 2024, 2025 |
| `V` | float | Vagueness score [7.46, 97.08] |
| `delta_V` | float | Year-over-year ΔV |
| `total_delta_V` | float | Cumulative D = V_t - V_0 |
| `first_financing_size` | float | E (Early Capital, $M) |

### Transform: Panel → Cross-sectional
```python
# Extract t=0 (2021)
df_0 = df[df['year'] == 2021][['company_id', 'V', 'first_financing_size']]
df_0.columns = ['company_id', 'V', 'E']

# Extract t=T (2025)
df_T = df[df['year'] == 2025][['company_id', 'V', 'total_delta_V']]
df_T.columns = ['company_id', 'V_T', 'D']

# Merge
cross = df_0.merge(df_T, on='company_id')

# Derived variables
cross['A'] = cross['D'].abs()  # A = |D| = |V_T - V_0|
```

---

## 🔬 VARIABLE DEFINITIONS (CRITICAL)

| Symbol | Name | Formula | Type |
|--------|------|---------|------|
| **V** | Vagueness | V at t=0 (2021) | Continuous [0,100] |
| **E** | Early Capital | first_financing_size | Continuous ($M) |
| **D** | Directional Change | V_T - V_0 = total_delta_V | **Signed** (+/-) |
| **A** | Adaptive Capacity | \|D\| = \|V_T - V_0\| | **Unsigned** (≥0) |
| **L** | Long-term Success | Survival to 2025 | Binary (proxy) |
| **G** | Growth Ratio | Proxy from A, E | Continuous |

⚠️ **CRITICAL**: D is SIGNED (directional), A is UNSIGNED (magnitude only)

---

## 📈 SEVEN PLOTS SPECIFICATION

### Paper ✌️U (¶25-32): Vagueness & Survival

#### Plot U1: ULV — L vs V (U-Shape Test) [¶25-26]
```
Method: Quartile + χ² (NOT quadratic regression)
X-axis: V Quartile (Q1=Precise, Q4=Vague)
Y-axis: Survival Rate (%)

Key Metric: Δ = (Q1+Q4)/2 - (Q2+Q3)/2
Expected: Δ > 0, χ² > 300, p < 0.001

Visualization:
- Bar chart with 4 bars (Q1-Q4)
- Horizontal lines showing (Q1+Q4)/2 and (Q2+Q3)/2
- Annotation: "Δ = X.XX pp, χ² = XXX, p < 0.001"
- Color: Q1,Q4 = green (extremes), Q2,Q3 = red (middle)
```

#### Plot U2: UDV — D vs V [¶27]
```
X-axis: V (Initial Vagueness)
Y-axis: D (Directional Change = V_T - V_0, SIGNED)

Expected: V↑ → D range expands (cone shape)
- Low V: D constrained near 0
- High V: D spreads to both + and -

Visualization:
- Scatter plot with transparency
- Show that High-V companies have wider D spread
- NOT a simple linear correlation
```

#### Plot U3: UAV — A vs V [¶28]
```
X-axis: V (Initial Vagueness)
Y-axis: A = |D| (Adaptive Capacity, UNSIGNED)

Expected: ρ > 0 (positive correlation)
- Vagueness enables larger absolute movement

Visualization:
- Binned scatter + regression line + 95% CI
- Annotation: "ρ = X.XX***, N = XXX,XXX"
```

#### Plot U4: ULD — L vs A [¶29-30]
```
X-axis: A = |ΔV| (Adaptive Capacity)
Y-axis: L (Survival Rate)

Expected: dL/d|ΔV| > 0 (positive slope)
- More movement → better survival

Visualization:
- Binned scatter + logistic-style curve
- Annotation: "dL/dA > 0***"
```

### Paper 🦾C (¶57-64): Capital & Flexibility

#### Plot C1: CGE — G vs E [¶57-58]
```
X-axis: E (Early Capital, LOG SCALE)
Y-axis: G (Growth proxy)

Expected: ρ < 0 (negative correlation)
- Capital curse: more E → less G

Visualization:
- Log-scale X-axis
- Binned scatter + regression
```

#### Plot C2: CAE — A vs E (GOLDEN CAGE ⭐) [¶59-60]
```
X-axis: E (Early Capital, LOG SCALE)
Y-axis: A = |ΔV| (Adaptive Capacity)

Expected: d|ΔV|/dE < 0 (NEGATIVE)
- THE KEY FINDING: Money reduces flexibility

Visualization:
- Log-scale X-axis
- Decile binning with error bars
- Regression with 95% CI band
- Annotation: "💰 → 🔒 Golden Cage: λ = X.XX***"
```

#### Plot C3: CGA — G vs A [¶61-62]
```
X-axis: A = |ΔV| (Adaptive Capacity)
Y-axis: G (Growth)

Expected: dG/d|ΔV| > 0 (positive)
- Flexibility drives growth

Visualization:
- Scatter + regression
- Annotation: "ρ = X.XX***"
```

#### Plot C4: Mechanism Summary [¶63-64]
```
3-Panel showing the causal chain:
dG/dE = dG/dA × dA/dE = (+) × (-) < 0

Panel A: A vs E (−)
Panel B: G vs A (+)
Panel C: G vs E (−) = Combined effect
```

---

## 📝 THESIS TEXT TEMPLATE

### Paper ✌️U Section 3 (Empirics): ¶25-32

```markdown
## ¶25: U-Shape Introduction
We test the U-shape hypothesis using quartile analysis. Figure U1 displays 
survival rates by vagueness quartile for N = [N] technology ventures.

[INSERT FIGURE: U_fig1_ULV.png]

## ¶26: U-Shape Results
The data reveal a clear U-shape pattern. Ventures with the most precise 
positioning (Q1) survive at [Q1]%, while those with the most vague positioning 
(Q4) survive at [Q4]%. Critically, the intermediate quartiles (Q2, Q3) show 
the lowest survival rates at [Q2]% and [Q3]% respectively. 

The murky middle penalty Δ = ([Q1]+[Q4])/2 - ([Q2]+[Q3])/2 = [Δ] percentage 
points (χ² = [χ²], p < 0.001), confirming that both extremes outperform 
the middle.

## ¶27: Movement Analysis (UDV)
Figure U2 examines how initial vagueness affects subsequent repositioning. 
Ventures with high initial V exhibit a wider range of directional changes D, 
suggesting that vagueness creates "room to move" in positioning space.

[INSERT FIGURE: U_fig2_UDV.png]

## ¶28: Adaptive Capacity (UAV)
Figure U3 shows the relationship between V and adaptive capacity A = |ΔV|. 
We find a positive correlation (ρ = [ρ], p < [p]), indicating that vague 
initial positioning enables larger absolute strategic pivots.

[INSERT FIGURE: U_fig3_UAV.png]

## ¶29-30: Movement and Survival (ULD)
Figure U4 tests whether adaptive capacity predicts survival. The positive 
relationship (dL/d|ΔV| = [β], p < [p]) suggests that ventures capable of 
larger repositioning are more likely to reach late-stage funding.

[INSERT FIGURE: U_fig4_ULD.png]

## ¶31-32: Summary and Robustness
Table U1 summarizes our hypothesis tests. The U-shape pattern holds across 
all four industries (Software, Transportation, Hardware, Pharmaceuticals), 
with Δ > 0 in each case.

[INSERT TABLE: U_table1_summary.png]
```

### Paper 🦾C Section 3 (Empirics): ¶57-64

```markdown
## ¶57-58: The Causal Mechanism
We propose that early capital affects growth through its impact on adaptive 
capacity. Figure C1 illustrates the three-step mechanism:

dG/dE = (dG/d|ΔV|) × (d|ΔV|/dE) = (+) × (−) < 0

[INSERT FIGURE: C_fig1_mechanism.png]

## ¶59-60: The Golden Cage (Key Finding)
Figure C2 presents our central empirical finding. We observe a significant 
negative relationship between early capital and adaptive capacity 
(λ = [λ], p < [p]). 

[INSERT FIGURE: C_fig2_CAE_golden_cage.png]

This "Golden Cage" effect suggests that well-funded ventures become locked 
into their initial positioning, unable or unwilling to pivot even when 
market conditions change.

## ¶61-62: Flexibility and Growth
Figure C3 confirms the second link in our causal chain. Adaptive capacity 
positively predicts growth (ρ = [ρ], p < [p]), indicating that flexibility 
enables value creation.

[INSERT FIGURE: C_fig3_CGA.png]

## ¶63-64: The Capital Paradox
Combining these effects, Figure C4 shows the net relationship between early 
capital and growth. Despite conventional wisdom that more funding enables 
growth, we find a negative relationship: ventures with larger early rounds 
exhibit lower growth multiples.

The mechanism: Money buys commitment, not flexibility. And in uncertain 
environments, flexibility—not resources—drives growth.

[INSERT FIGURE: C_fig4_summary.png]
```

---

## ⚙️ EXECUTION STEPS

### Step 1: Setup
```bash
cd /Users/hyunjimoon/tolzul/Front/On/love\(cs\)/strategic_ambiguity/empirics
mkdir -p src/scripts/paper_generation/output/_thesis_package/figures
mkdir -p src/scripts/paper_generation/output/_thesis_package/text
```

### Step 2: Generate Figures
```python
# Run the master script (create this file)
python src/scripts/paper_generation/output/_thesis_package/seven_plots_v2.py
```

### Step 3: Generate Thesis Text
```python
# The script should also output:
# - text/paper_U_sec3.md (¶25-32)
# - text/paper_C_sec3.md (¶57-64)
# with placeholders filled with actual statistics
```

### Step 4: Verify
```bash
ls -la src/scripts/paper_generation/output/_thesis_package/figures/
# Expected: U_fig1_ULV.png, U_fig2_UDV.png, ... C_fig4_summary.png

ls -la src/scripts/paper_generation/output/_thesis_package/text/
# Expected: paper_U_sec3.md, paper_C_sec3.md
```

---

## 🎨 VISUALIZATION STANDARDS

```python
# Figure settings
plt.rcParams.update({
    'figure.dpi': 300,
    'figure.figsize': (10, 6),
    'font.size': 11,
    'font.family': 'DejaVu Sans',
    'savefig.bbox': 'tight',
    'savefig.facecolor': 'white',
})

# Colors
COLORS = {
    'extreme': '#27ae60',     # Green for Q1, Q4
    'middle': '#e74c3c',      # Red for Q2, Q3
    'positive': '#27ae60',    # Green for positive effects
    'negative': '#e74c3c',    # Red for negative effects
    'primary': '#3498db',     # Blue for data points
}

# Significance stars
def stars(p):
    if p < 0.001: return '***'
    if p < 0.01: return '**'
    if p < 0.05: return '*'
    return ''
```

---

## ✅ DELIVERABLES CHECKLIST

### Figures (7 total)
```
□ U_fig1_ULV.png      - Quartile bar chart + Δ
□ U_fig2_UDV.png      - D vs V scatter (cone)
□ U_fig3_UAV.png      - A vs V with regression
□ U_fig4_ULD.png      - L vs A 
□ C_fig1_mechanism.png - 3-panel causal chain
□ C_fig2_CAE_golden_cage.png - THE KEY FIGURE ⭐
□ C_fig3_CGA.png      - G vs A
```

### Text (2 files)
```
□ paper_U_sec3.md     - ¶25-32 with statistics filled
□ paper_C_sec3.md     - ¶57-64 with statistics filled
```

### Statistics to Report
```
□ N (sample size)
□ Q1, Q2, Q3, Q4 survival rates
□ Δ (murky middle penalty)
□ χ² statistic and p-value
□ Correlation coefficients (ρ) for each relationship
□ Regression slopes with standard errors
□ All p-values and significance stars
```

---

## 🔑 CRITICAL REMINDERS

1. **D vs A**: D is SIGNED (V_T - V_0), A is UNSIGNED (|D|)

2. **ULV Method**: Use Quartile + χ², NOT quadratic regression
   - Δ = (Q1+Q4)/2 - (Q2+Q3)/2 is the key metric

3. **L is proxied**: Since we don't have actual survival data, proxy L based on:
   - Companies present in 2025 = survived
   - Use U-shape + A effect for logistic model

4. **G is proxied**: Estimate from A and E relationships

5. **Log scale for E**: Always use log10(E) for funding variables

6. **Golden Cage is THE key finding**: C_fig2 should be publication-quality

---

## 📤 EXPECTED OUTPUT SUMMARY

After execution:
```
_thesis_package/
├── figures/
│   ├── U_fig1_ULV.png
│   ├── U_fig2_UDV.png
│   ├── U_fig3_UAV.png
│   ├── U_fig4_ULD.png
│   ├── C_fig1_mechanism.png
│   ├── C_fig2_CAE_golden_cage.png
│   └── C_fig3_CGA.png
├── text/
│   ├── paper_U_sec3.md  (¶25-32, ~800 words)
│   └── paper_C_sec3.md  (¶57-64, ~800 words)
└── stats/
    └── summary_statistics.json
```

---

**END OF PROMPT**

Execute this end-to-end to generate all figures and thesis text.
