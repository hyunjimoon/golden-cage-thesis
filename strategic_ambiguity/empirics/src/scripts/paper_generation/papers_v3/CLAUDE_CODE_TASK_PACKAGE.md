# 🐅 Claude Code Task Package: Thesis Content Restructuring

## Context

You are working on a PhD dissertation "Flexibility and Commitment in Entrepreneurship" for MIT Sloan. The thesis uses a **Sonata musical structure** with modules I-M-C-T-D.

**Critical recent changes** from handwritten notes analysis:
1. M module = **TWO papers** (18+1+18), not 3 sections
2. T module = **5+7+8+4** structure (not 4 equal), with Q3 analysis
3. T empirics = Q3 analysis (NOT simulation)
4. Computational simulation → D(112) as methods contribution
5. Color scheme: ⚫ Stayer, 🟢 Horizontal, 🔴 Zoom In, 🔵 Zoom Out

---

## Task Overview

| Priority | Category | Tasks |
|:--------:|:---------|:------|
| P1 | Structure | Reorganize M into 2 papers + bridge |
| P2 | Content | Rewrite T empirics as Q3 analysis |
| P3 | Content | Add computational simulation to D(112) |
| P4 | Figures | Update all figures with new color scheme |
| P5 | Data | Find Low V₀ examples (Stayer, Horizontal) |

---

## P1: Reorganize M Module (Lines 12-48)

### Current Structure (WRONG)
```
2_M_movement/
├── s1_gospel.md
├── s2_puzzle.md
└── s3_fund2cage.md
```

### Target Structure (CORRECT)
```
2_M_movement/
├── paper_m1/                    # Lines 12-29 (18 paragraphs)
│   ├── s1_gospel.md             # Lines 12-13
│   ├── s2_puzzle.md             # Lines 14-15
│   ├── s3_litrev_variables.md   # Lines 16-19 (V,D,A,E,G definitions)
│   ├── s4_results.md            # Lines 20-23 (dG/dA > 0)
│   ├── s5_implication.md        # Lines 24-26
│   └── s6_conclude.md           # Lines 27-29
├── bridge_line30.md             # Line 30 (Bridge equation)
└── paper_m2/                    # Lines 31-48 (18 paragraphs)
    ├── s1_gospel.md             # Line 31
    ├── s2_puzzle.md             # Line 32
    ├── s3_lens.md               # Line 33
    ├── s4_org.md                # Line 34
    ├── s5_theory.md             # Lines 35-39
    ├── s6_empirics.md           # Lines 40-44
    └── s7_discussion.md         # Lines 45-48
```

### Commands
```bash
cd /Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/papers_v3/2_M_movement

# Create folders
mkdir -p paper_m1 paper_m2

# Bridge equation file
cat > bridge_line30.md << 'EOF'
# Line 30: The Bridge Equation

## The Pivot Point of the Entire Thesis

$$\frac{dG}{dE} = \frac{dG}{dA} \cdot \frac{dA}{dE} = (+)(-) < 0$$

This single paragraph:
- **Receives** from M1: dG/dA > 0 (Movement Principle)
- **Hands off** to M2: Need to explain dA/dE < 0 (Fund2Cage)
- **Explains**: Why the Funding Paradox (dG/dE < 0) emerges

The decomposition transforms the empirical puzzle (negative correlation) into a **causal mechanism** (two separate forces with opposite signs).

---

*Funding builds a golden cage: the resources that secure survival restrict the freedom required for growth.*
EOF
```

---

## P2: Rewrite T Empirics (Lines 93-100)

### Current Content (WRONG)
- Describes simulation + #IP correlation
- Should be in D(112), not here

### Target Content (CORRECT)
T Empirics answers: **Why is Q3 success rate unexpectedly high?**

```markdown
## Part A (Lines 93-96): 😊 Benefit of Vague Promise

**Method**: Indirect proof via movement composition (from Module C)

| Finding | Evidence |
|:--------|:---------|
| Q3 has highest success | 16.0% |
| Q3 has highest movement rate | 68% |
| Movement → Success | 2.6× (from M) |
| **Conclusion** | Q3 success explained by movement composition |

Logic chain:
Q3 (V = 50-75) → High movement rate (68%) → Movement → Success

## Part B (Lines 97-100): 😭 Cost of Precise Promise

**Method**: Learning trap mechanism (μ-doubter relationship)

Mechanism:
1. Precise promise → Attracts believers (high μ stakeholders)
2. Optimistic founder (high μ) → Like-minded gather
3. Low variance in stakeholder beliefs
4. **Cannot update prior** → Learning blocked

The μ-Doubter Insight:
> The more optimistic you are (high μ), the more you NEED doubters.
> High μ → μ(1−μ) is SMALL → Trap condition easier to satisfy
```

### File to Update
```
/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/papers_v3/4_T_commit2trap/s3_learning_trap.md
```

---

## P3: Add Computational Simulation to D(112)

### Target Location
```
/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/papers_v3/5_D_discussion/line112_linked_t.md
```

### Content to Add
```markdown
# Line 112: Linked to [T] — LTE Theory Contribution

## 1. Formal Equation
$$\mu(1-\mu) < \frac{\varepsilon}{V+1}$$

- Testable prediction
- Parameter specification (μ, V, ε measurable)
- Comparative statics (clear directional predictions)

## 2. Computational Simulation (Methods Contribution)

The learning trap equation is validated through computational simulation:

### Simulation Design
- Generate N ventures with varying V, μ, τ
- For each venture, check if trap condition satisfied
- Track which combinations trigger trap
- Compare predicted vs. observed Q patterns

### Validation Results
| Quartile | Predicted (Sim) | Observed (Data) | Match? |
|:---------|:---------------:|:---------------:|:------:|
| Q1 | High trap rate | 12.3% success | ✅ |
| Q2 | Medium trap | 8.9% success | ✅ |
| Q3 | Low trap | 16.0% success | ✅ |
| Q4 | Medium (no focus) | 12.9% success | ✅ |

## 3. Contribution to Organization Science

| Traditional Approach | LTE Approach |
|:---------------------|:-------------|
| Verbal theory | Formal equation |
| Case studies | Large-N empirics |
| Static analysis | Computational simulation |
| Explanation focus | Prediction + intervention |

## 4. What-How-Why Framework

| Question | Module | Contribution |
|:---------|:------:|:-------------|
| **WHAT** | M | Movement Principle |
| **HOW** | C | Fund2Cage mechanism |
| **WHY/WHEN** | T | Learning trap condition |
```

---

## P4: Update Figures with New Color Scheme

### Color Mapping
| Type | Color | Hex Code | RGB |
|:-----|:-----:|:---------|:----|
| ⚫ Stayer | Black | #264653 | (38, 70, 83) |
| 🟢 Horizontal | Green | #2A9D8F | (42, 157, 143) |
| 🔴 Zoom In | Red | #E63946 | (230, 57, 70) |
| 🔵 Zoom Out | Blue | #457B9D | (69, 123, 157) |

### Figures to Update

```python
# Python script to update figure colors
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# New color scheme
COLORS = {
    'stayer': '#264653',      # Black/Dark
    'horizontal': '#2A9D8F',  # Green
    'zoom_in': '#E63946',     # Red
    'zoom_out': '#457B9D',    # Blue
}

# Files to update:
# 1. fig_m_mover_advantage.png - Movement Principle visualization
# 2. fig_c_typology.png - E×E matrix with 4 types
# 3. fig_t_q3_analysis.png - Q3 peak explanation
# 4. Any bar charts comparing types
```

### Figure Locations
```
papers_v3/
├── 2_M_movement/
│   └── figures/
│       └── fig_m_mover_advantage.png    # Update colors
├── 3_C_cash2growth/
│   └── figures/
│       ├── fig_c_typology.png           # Update colors
│       └── fig_c_exe_matrix.png         # Create new
└── 4_T_commit2trap/
    └── figures/
        └── fig_t_q3_analysis.png        # Update colors
```

---

## P5: Find Low V₀ Examples

### Missing Data
| Type | V₀ Level | Currently Have | Need |
|:-----|:--------:|:---------------|:-----|
| ⚫ Stayer | Low | None | Company that started precise and stayed |
| 🟢 Horizontal | Low | None | Company that moved laterally at low V |

### Query to Run on Dataset
```python
# Find Low V₀ Stayer examples
low_v0_stayers = df[
    (df['V_initial'] < 30) &  # Low V₀
    (abs(df['V_change']) < 5) &  # Stayed (D ≈ 0)
    (df['success'] == True)  # Successful for interesting case
]

# Find Low V₀ Horizontal examples
low_v0_horizontal = df[
    (df['V_initial'] < 30) &  # Low V₀
    (abs(df['V_change']) < 5) &  # D ≈ 0
    (df['keyword_change'] > 0.5)  # Keywords changed significantly
]

# Print top candidates with company descriptions
print(low_v0_stayers[['company_name', 'V_initial', 'V_final', 'description_initial', 'description_final']])
```

### Expected Output Format
```
| Company | V₀ | V_T | ΔV | Description Change |
|---------|:--:|:---:|:--:|:-------------------|
| [TBD]   | 25 | 27  | +2 | Stayed precise in X |
| [TBD]   | 30 | 28  | -2 | Lateral move in Y |
```

---

## Execution Order

```
1. [P1] Create M folder structure and bridge file
2. [P2] Rewrite T empirics as Q3 analysis (Part A + Part B)
3. [P3] Create D line112 with computational simulation
4. [P5] Run data query to find Low V₀ examples
5. [P4] Update figures with new colors (after data confirmed)
6. [FINAL] Review all content files for consistency
```

---

## Validation Checklist

After completing all tasks, verify:

- [ ] M has paper_m1/ and paper_m2/ folders with bridge_line30.md
- [ ] T s3_learning_trap.md describes Q3 analysis (😊 + 😭), NOT simulation
- [ ] D has line112_linked_t.md with computational simulation content
- [ ] All figures use ⚫🟢🔴🔵 color scheme
- [ ] Low V₀ examples identified for Stayer and Horizontal
- [ ] toc files (v2/v3) match actual content structure

---

## File Paths Reference

```
BASE = /Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/papers_v3

Architecture:
  ${BASE}/ARCHITECTURE(thesis)_v2.md

M Module:
  ${BASE}/2_M_movement/toc(m)_v2.md
  ${BASE}/2_M_movement/paper_m1/  (CREATE)
  ${BASE}/2_M_movement/paper_m2/  (CREATE)
  ${BASE}/2_M_movement/bridge_line30.md (CREATE)

C Module:
  ${BASE}/3_C_cash2growth/toc(c)_v2.md

T Module:
  ${BASE}/4_T_commit2trap/toc(t)_v3.md
  ${BASE}/4_T_commit2trap/s3_learning_trap.md (REWRITE)

D Module:
  ${BASE}/5_D_discussion/toc(d)_v3.md
  ${BASE}/5_D_discussion/line112_linked_t.md (CREATE)

Data:
  ${BASE}/../data/  (for Low V₀ query)
```

---

*必死卽生, 必生卽死*
