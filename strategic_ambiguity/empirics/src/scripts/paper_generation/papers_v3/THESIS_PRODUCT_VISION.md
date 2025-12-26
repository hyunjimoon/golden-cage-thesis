# 📐 Thesis Product Vision: I-M-C-T-D Exhibits Interface Specification

> **For LLM 연합함대**: This document specifies the exact format and content of each figure and table.
>
> **생산 일정**:
> - **Phase 1-2 (오늘)**: 8 exhibits (CRITICAL + HIGH)
> - **Phase 3-4 (내일)**: 10 exhibits (MEDIUM + LOWER)

---

## 🎯 Core Thesis Reminder

$$\frac{dG}{dE} = \underbrace{\frac{dG}{dA}}_{\text{Movement Principle (+)}} \times \underbrace{\frac{dA}{dE}}_{\text{Cage Effect (−)}} < 0$$

---

# PHASE 1: CRITICAL (4 exhibits) 🔴

## 1️⃣ Fig M.3: Cash2Cage Mechanism Chain (KILLER FIGURE)

### Purpose
한 장의 그림으로 전체 논문을 설명

### Format
**3-Panel Figure** (horizontal layout, 1200×400 px)

```
┌─────────────────┬─────────────────┬─────────────────┐
│    PANEL A      │    PANEL B      │    PANEL C      │
│                 │                 │                 │
│   Cage Effect   │    Movement     │  Cash Paradox   │
│                 │   Principle     │   (Combined)    │
│                 │                 │                 │
│  Scatter plot   │  Scatter plot   │   Arrow diagram │
│   E vs A        │   A vs G        │   or equation   │
│                 │                 │                 │
│ ρ = -0.052***   │ ρ = +0.159***   │ (+)(−) = (−)    │
└─────────────────┴─────────────────┴─────────────────┘
```

### Data Requirements
```python
# From correlation_panel.nc
Panel A: E (early funding) vs A (adaptation)
         - Scatter with regression line
         - ρ(E,A) = -0.052, p < 0.001
         - Color by quartile_V0

Panel B: A (adaptation) vs G (growth)
         - Scatter with regression line
         - ρ(A,G) = +0.159, p < 0.001
         - Highlight movers vs stayers

Panel C: Mechanism chain diagram
         - E →(-) A →(+) G
         - Net effect: dG/dE < 0
```

### Output
- `fig_M3_killer_mechanism.png` (300 DPI)
- `fig_M3_killer_mechanism.svg` (vector)

---

## 2️⃣ Fig M.2: Movers vs Stayers (2.6×)

### Purpose
Movement Principle의 핵심 증거: dG/dA > 0

### Format
**Grouped Bar Chart** (800×500 px)

```
Success Rate (%)
     │
 20% ┤                    ████████
     │                    ████████ 18.1%
 15% ┤                    ████████
     │                    ████████
 10% ┤                    ████████
     │    ████            ████████
  5% ┤    ████ 7.0%       ████████
     │    ████            ████████
  0% ┼────────────────────────────────
          Stayed           Moved
          (A=0)            (A>0)

     N=108,516           N=72,344

     *** p < 0.001, RR = 2.59 [2.42, 2.77]
```

### Data Requirements
```python
# From movement_stats.nc
group: ['stayed', 'moved']
success_rate: [0.070, 0.181]
ci_low: [0.066, 0.175]
ci_high: [0.074, 0.187]
n_ventures: [108516, 72344]
relative_risk: 2.59
```

### Annotations
- Error bars (95% CI)
- "2.6×" annotation with arrow
- Chi-squared test result
- NNT = 9 in caption

### Output
- `fig_M2_movers_vs_stayers.png`

---

## 3️⃣ Fig C.1: V₀ × ΔV Typology (4 Archetypes)

### Purpose
4가지 Archetype 시각화

### Format
**Scatter Plot with Quadrants** (800×800 px)

```
         ΔV (Direction)
          │
    +60   │   Zoom-out
          │     ●●●
          │   ●●●●●●
    +30   │ ●●●●●●●●●    Sky Engine ★
          │
     0  ──┼────────────────────── V₀
          │  Stayer    Move-around
   -30    │ ●●●●●●●●●●●●●●●●●
          │   ●●●●●●●●●●●
          │     Zoom-in    Linpowave ★
   -60    │
          └────────────────────────
              25    50    75   100
                 Initial V₀
```

### Data Requirements
```python
# From mover_typology.nc
For each venture:
  - V_0: initial vagueness (x-axis)
  - delta_V: V_T - V_0 (y-axis)
  - type_label: 'zoom_in'|'stayer'|'move_around'|'zoom_out'
  - G: growth (for color intensity)

Highlight examples:
  - Sky Engine: (28.4, +60.7) → Zoom-out
  - Linpowave: (88.1, -56.3) → Zoom-in
  - Rubedos: (81.9, 0) → Stayer
```

### Quadrant Labels
| Quadrant | V₀ | ΔV | Label | Color |
|----------|----|----|-------|-------|
| Top-Left | Low | + | Zoom-out | 🟢 Green |
| Top-Right | High | + | (rare) | 🟢 Light |
| Bottom-Left | Low | - | (rare) | 🔵 Light |
| Bottom-Right | High | - | Zoom-in | 🔵 Blue |
| Center | Any | ≈0 | Stayer/Move-around | 🔴 Red |

### Output
- `fig_C1_typology_quadrant.png`

---

## 4️⃣ Tab M.1: Hypothesis Results H1-H3

### Purpose
통계적 검증 결과 요약

### Format
**LaTeX/Markdown Table**

```markdown
| Hypothesis | Statement | Test | ρ | 95% CI | p-value | Result |
|:-----------|:----------|:-----|--:|:------:|:-------:|:------:|
| H₀ | ρ(V,L) < 0 (Signaling) | Spearman | +0.024 | [0.019, 0.029] | <0.001 | ❌ Rejected |
| H₁ | dG/dA > 0 (Movement) | Spearman | +0.159 | [0.153, 0.165] | <0.001 | ✓ Supported |
| H₂ | dA/dE < 0 (Cage) | Spearman | −0.052 | [−0.058, −0.046] | <0.001 | ✓ Supported |
| H₃ | Heterogeneous by Type | ANOVA | F=156.3 | - | <0.001 | ✓ Supported |
```

### Data Requirements
```python
# From hypothesis_results.nc
hypothesis: ['H0', 'H1', 'H2', 'H3']
rho: [0.024, 0.159, -0.052, None]
ci_low: [0.019, 0.153, -0.058, None]
ci_high: [0.029, 0.165, -0.046, None]
p_value: [0.001, 0.001, 0.001, 0.001]
test_statistic: [None, None, None, 156.3]
result: ['rejected', 'supported', 'supported', 'supported']
```

### Output
- `tab_M1_hypothesis_results.md`
- `tab_M1_hypothesis_results.tex`

---

# PHASE 2: HIGH (4 exhibits) 🟡

## 5️⃣ Fig M.1: Success by Vagueness Quartile

### Purpose
Q3 Peak 패턴 시각화 (Non-monotonic)

### Format
**Bar Chart with Error Bars** (800×500 px)

```
Success Rate (%)
     │
 18% ┤              ████
 16% ┤              ████ 16.0%
 14% ┤              ████
 12% ┤  ████        ████        ████
 10% ┤  ████ 12.3%  ████        ████ 12.9%
  8% ┤  ████        ████  ████  ████
  6% ┤  ████        ████  ████  ████
  4% ┤  ████        ████  ████  ████
     │  ████        ████  ████  ████
  0% ┼──────────────────────────────────
       Q1          Q2    Q3    Q4
     (Precise)                (Vague)

     *** Q3 > Q1: p < 0.001
     *** Q3 > Q4: p < 0.001
```

### Data Requirements
```python
# From vagueness_quartile_stats.nc
quartile: ['Q1', 'Q2', 'Q3', 'Q4']
success_rate: [0.123, 0.089, 0.160, 0.129]
ci_low: [0.118, 0.085, 0.154, 0.124]
ci_high: [0.128, 0.093, 0.166, 0.134]
n_ventures: [45215, 45215, 45215, 45215]
```

### Annotations
- Peak at Q3 highlighted
- Significance brackets between Q3 and others
- "Non-monotonic" label

### Output
- `fig_M1_quartile_success.png`

---

## 6️⃣ Fig C.2: dG/dA by Type (Effectiveness)

### Purpose
Archetype별 Movement Effectiveness 비교

### Format
**Coefficient Plot / Forest Plot** (800×400 px)

```
dG/dA (Movement Effectiveness)
                    │
    Zoom-out   ────●────────  +0.18 ***
                    │
    Zoom-in    ───●─────────  +0.15 ***
                    │
    Move-around ──●──────────  +0.08 *
                    │
    Stayer     ●────────────  −0.05 **  ← 🔴 TRAP!
                    │
               ────┼────────────────
              -0.1  0   +0.1  +0.2

    *** Stayer is the ONLY negative type
```

### Data Requirements
```python
# From effectiveness_by_type.nc
type: ['zoom_out', 'zoom_in', 'move_around', 'stayer']
dG_dA: [0.18, 0.15, 0.08, -0.05]
ci_low: [0.15, 0.12, 0.03, -0.09]
ci_high: [0.21, 0.18, 0.13, -0.01]
p_value: [0.001, 0.001, 0.05, 0.01]
n_ventures: [36000, 38000, 12000, 94000]
```

### Key Message
- Stayer is the **only type with negative dG/dA**
- This is the "TRAP" condition

### Output
- `fig_C2_effectiveness_by_type.png`

---

## 7️⃣ Tab C.1: Company Examples (Table 2.2)

### Purpose
4 Archetype을 실제 회사로 예시

### Format
**Markdown/LaTeX Table**

```markdown
| Company | V₀ | V_T | ΔV | Type | Growth | Key Insight |
|:--------|---:|----:|---:|:-----|-------:|:------------|
| **Stripe** | 75.2 | 32.1 | −43.1 | Zoom-in | 89.3× | Vague → PMF found |
| **Amazon** | 28.4 | 89.1 | +60.7 | Zoom-out | 215.9× | Books → Everything |
| **Airbnb** | 65.3 | 71.2 | +5.9 | Move-around | 45.2× | Pivoted multiple times |
| **Quibi** | 82.1 | 81.9 | −0.2 | Stayer | 0.0× | 💀 "Entitled to grow" |
```

### Data Requirements
```python
# From company_examples.nc (or manual curation)
company: ['Stripe', 'Amazon', 'Airbnb', 'Quibi']
V_0: [75.2, 28.4, 65.3, 82.1]
V_T: [32.1, 89.1, 71.2, 81.9]
delta_V: [-43.1, 60.7, 5.9, -0.2]
type_label: ['zoom_in', 'zoom_out', 'move_around', 'stayer']
growth: [89.3, 215.9, 45.2, 0.0]
insight: ['Vague → PMF', 'Books → Everything', 'Pivoted', 'Entitled trap']
```

### Output
- `tab_C1_company_examples.md`
- `tab_C1_company_examples.tex`

---

## 8️⃣ Tab T.1: Precision Paradox (Q3 > Q1)

### Purpose
Precision Paradox 통계적 증거

### Format
**Comparison Table**

```markdown
| Metric | Q1 (Precise) | Q3 (Moderate) | Difference | p-value |
|:-------|-------------:|--------------:|-----------:|:-------:|
| Success Rate | 12.3% | 16.0% | +3.7 pp | <0.001 |
| Movement Rate | 42% | 68% | +26 pp | <0.001 |
| Success (Stayers) | 7.1% | 6.6% | −0.5 pp | 0.23 |
| Success (Movers) | 18.2% | 20.4% | +2.2 pp | <0.01 |
| Avg Growth (G) | 2.1× | 3.4× | +1.3× | <0.001 |

**Interpretation**: Q3 wins because of higher movement rate, not inherently better positioning.
```

### Data Requirements
```python
# From precision_paradox.nc
metric: ['success_rate', 'movement_rate', 'success_stayers',
         'success_movers', 'avg_growth']
Q1: [0.123, 0.42, 0.071, 0.182, 2.1]
Q3: [0.160, 0.68, 0.066, 0.204, 3.4]
difference: [0.037, 0.26, -0.005, 0.022, 1.3]
p_value: [0.001, 0.001, 0.23, 0.01, 0.001]
```

### Output
- `tab_T1_precision_paradox.md`
- `tab_T1_precision_paradox.tex`

---

# PHASE 3: MEDIUM (5 exhibits) 🟢

## 9️⃣ Fig M.4: Temporal Stability 2023-2025

### Format
**Line Plot with Confidence Bands** (800×400 px)

```python
# From temporal_stability.nc
year: [2023, 2024, 2025]
relationships: ['ρ(A,E)', 'ρ(G,A)', 'ρ(G,E)']
# Each relationship has rho, ci_low, ci_high per year
```

### Key Message
- Patterns stable across market regimes
- Not artifact of specific year

---

## 🔟 Fig C.3: dA/dE by Type (Efficiency)

### Format
**Coefficient Plot** (same style as Fig C.2)

```python
# From efficiency_by_type.nc
type: ['zoom_out', 'zoom_in', 'move_around', 'stayer']
dA_dE: [+0.05, +0.03, -0.02, +0.08]  # Stayer paradox: gets money but doesn't move
```

---

## 1️⃣1️⃣ Tab C.2: Type-Specific Statistics

### Format
**Detailed breakdown table**

```markdown
| Type | N | % | Success | Growth | dG/dA | dA/dE | dG/dE |
|:-----|--:|--:|--------:|-------:|------:|------:|------:|
| Zoom-out | 36K | 20% | 19.2% | 4.2× | +0.18 | +0.05 | + |
| Zoom-in | 38K | 21% | 18.1% | 3.1× | +0.15 | +0.03 | + |
| Move-around | 12K | 7% | 15.3% | 2.5× | +0.08 | −0.02 | ≈0 |
| Stayer | 94K | 52% | 7.0% | 1.2× | −0.05 | +0.08 | − |
```

---

## 1️⃣2️⃣ Tab M.2: Direction Irrelevance

### Format
```markdown
| Direction | Success Rate | 95% CI | vs Stayer |
|:----------|-------------:|:------:|:---------:|
| Zoom-in (D<0) | 17.6% | [16.8%, 18.4%] | 2.5× |
| Zoom-out (D>0) | 18.6% | [17.8%, 19.4%] | 2.7× |
| **Difference** | 1.0 pp | Cohen's h=0.027 | Negligible |
```

---

## 1️⃣3️⃣ Fig T.1: Learning Capacity by V

### Format
**Heatmap or Contour Plot** (800×600 px)

```python
# From learning_capacity.nc
# μ(1-μ) / (V+1) surface
V: 0-100 (x-axis)
mu: 0-1 (y-axis)
capacity: 2D array

# Show trap region where capacity < epsilon
```

---

# PHASE 4: LOWER (5 exhibits) ⚪

## 1️⃣4️⃣ Fig T.2: Tesla vs Better Place
- Timeline comparison
- Can be prose description instead

## 1️⃣5️⃣ Fig T.3: Belief Updating Surface
- 3D theoretical visualization
- Can show equation instead

## 1️⃣6️⃣ Tab I.1: Notation Reference
- V, D, A, E, G definitions
- Can be inline in Introduction

## 1️⃣7️⃣ Tab I.2: Key Statistics Summary
- N=488,381, success rates
- Can be in abstract

## 1️⃣8️⃣ Tab D.1/D.2: Discussion tables
- Contributions and Limitations
- Usually prose in dissertations

---

# 📋 LLM Fleet Interface Checklist

## For Data Generation Agent (데이터 생성)
```
□ thesis_panel_v3.nc (master panel, N=488,381)
□ correlation_panel.nc (for Fig M.3)
□ movement_stats.nc (for Fig M.2)
□ mover_typology.nc (for Fig C.1)
□ hypothesis_results.nc (for Tab M.1)
□ vagueness_quartile_stats.nc (for Fig M.1)
□ effectiveness_by_type.nc (for Fig C.2)
□ company_examples.nc (for Tab C.1)
□ precision_paradox.nc (for Tab T.1)
```

## For Visualization Agent (시각화)
```
Phase 1 (오늘):
□ fig_M3_killer_mechanism.png
□ fig_M2_movers_vs_stayers.png
□ fig_C1_typology_quadrant.png
□ tab_M1_hypothesis_results.md

Phase 2 (오늘):
□ fig_M1_quartile_success.png
□ fig_C2_effectiveness_by_type.png
□ tab_C1_company_examples.md
□ tab_T1_precision_paradox.md
```

## For LaTeX Agent (조판)
```
□ All figures at 300 DPI
□ All tables in .tex format
□ Consistent styling (fonts, colors)
□ Caption templates provided
```

---

# 🎯 Success Criteria

| Phase | Exhibits | Deadline | Validator |
|:------|:--------:|:--------:|:---------:|
| Phase 1 | 4 | 오늘 오후 | 🐅권준 |
| Phase 2 | 4 | 오늘 저녁 | 🐢정운 |
| Phase 3 | 5 | 내일 오전 | 🐙김완 |
| Phase 4 | 5 | 내일 오후 | (optional) |

**Definition of Done**:
- [ ] Data file (.nc) exists and loads correctly
- [ ] Figure/Table matches specification above
- [ ] Annotations and labels are correct
- [ ] Statistical values match `_shared/statistics.md`

---

*必死卽生, 必生卽死 - 오늘 Phase 1-2 완료!*
