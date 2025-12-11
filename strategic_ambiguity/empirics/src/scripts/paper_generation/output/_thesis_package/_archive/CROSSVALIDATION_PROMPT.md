# 🔍 Cross-Validation Prompt for LLM Verification
> **Purpose**: Verify interpretation of handwritten research sketches
> **Method**: Ask another LLM to independently interpret the same images
> **Author**: Hyunji Moon (MIT PhD Candidate)

---

## Instructions for Verification LLM

I am writing a PhD thesis on "Flexibility and Commitment in Entrepreneurship" with two empirical papers:
- **Paper U**: Examines how initial Vagueness (V) affects Long-term Success (L)
- **Paper C**: Examines how Early Capital (E) affects Growth (G) through Adaptive Capacity (|ΔV|)

I have two handwritten sketches showing my expected relationships between variables. Please analyze each sketch independently and tell me:

1. **What variables and relationships do you see?**
2. **What are the expected signs (+, -, 0, U-shape, etc.) for each relationship?**
3. **How do the two sketches relate to each other (if at all)?**

---

## Context: Variable Definitions

| Symbol | Name | Definition |
|--------|------|------------|
| V | Vagueness | Initial positioning vagueness score (0-100) |
| L | Long-term Success | Probability of reaching Series B+ funding |
| E | Early Capital | First-round funding amount ($M) |
| D | Directional Change | V_final - V_initial (signed) |
| |ΔV| or A | Adaptive Capacity | Absolute value of D |
| G | Growth | (Total funding - E) / E |

---

## Sketch 1 Analysis Request

[ATTACH IMAGE: 1765383083065_image.png]

Please identify:

### Top Row (appears to be Paper U relationships)
- What is the first plot showing? (appears to be L vs V with bar chart)
- What is the second plot showing? (appears to be a cone/funnel shape)
- What is the third plot showing? (appears to be L vs |ΔV|)

### Bottom Row (appears to be Paper C relationships)
- What is the first plot showing? (appears to be G vs E)
- What is the second plot showing? (appears to be |ΔV| vs E)
- What is the third plot showing? (appears to be G vs |ΔV|)

### Questions:
1. For each relationship, what sign or shape is expected?
2. Are there any mathematical notations visible (derivatives, inequalities)?
3. What is the causal chain implied by the bottom row?

---

## Sketch 2 Analysis Request

[ATTACH IMAGE: 1765383092618_image.png]

This appears to be a 2×2 or 3×2 matrix framework. Please identify:

### Structure
- What are the row labels? (appears to be A, M, B)
- What are the column headers?
- What framework is being depicted?

### Content
- What signs (+, -, 0) appear in each cell?
- What text annotations are visible?
- What do the row labels likely stand for?

### Interpretation
- Does this represent different "types" of entrepreneurs or investors?
- How do the signs in each cell relate to the plots in Sketch 1?

---

## Verification Questions

After analyzing both sketches, please answer:

1. **Consistency Check**: Are the expected signs in Sketch 2's matrix consistent with the graph shapes in Sketch 1?

2. **Paper U Interpretation**: What does Sketch 1's top row suggest about the relationship between V and L? Is it:
   - Monotonic negative (more V → less L)?
   - Monotonic positive (more V → more L)?
   - U-shaped (extremes outperform middle)?
   - Something else?

3. **Paper C Interpretation**: What does Sketch 1's bottom row suggest about the causal chain E → |ΔV| → G? Specifically:
   - Sign of d|ΔV|/dE (does capital increase or decrease flexibility)?
   - Sign of dG/d|ΔV| (does flexibility increase or decrease growth)?
   - Net sign of dG/dE?

4. **Framework Interpretation**: What do you think the A/M/B rows in Sketch 2 represent? Some possibilities:
   - Analyst / Mixed / Believer (investor types)
   - Alpha / Middle / Beta (venture types)
   - Something else?

5. **Key Insight**: What is the main theoretical insight these sketches are trying to convey?

---

## Expected Output Format

Please provide your analysis in this format:

```
## Sketch 1 Analysis

### Top Row (Paper U)
| Plot | X-axis | Y-axis | Expected Shape/Sign | Interpretation |
|------|--------|--------|---------------------|----------------|
| 1    |        |        |                     |                |
| 2    |        |        |                     |                |
| 3    |        |        |                     |                |

### Bottom Row (Paper C)
| Plot | X-axis | Y-axis | Expected Shape/Sign | Interpretation |
|------|--------|--------|---------------------|----------------|
| 1    |        |        |                     |                |
| 2    |        |        |                     |                |
| 3    |        |        |                     |                |

## Sketch 2 Analysis

### Matrix Structure
| Row | Paper U Signs | Paper C Signs | Interpretation |
|-----|---------------|---------------|----------------|
|     |               |               |                |

## Synthesis

[Your interpretation of how the two sketches relate and what theoretical framework they represent]
```

---

## My Preliminary Interpretation (for comparison)

After you provide your independent analysis, I will share my interpretation so we can compare:

- Sketch 1 top row: I believe this shows Paper U plots (ULV, UDV/UAV, ULD)
- Sketch 1 bottom row: I believe this shows Paper C plots (CGE, CAE, CGA)
- Sketch 2: I believe this shows an Analyst/Mixed/Believer framework with different expected signs for each type

Please provide your interpretation BEFORE seeing mine, so we can have genuine cross-validation.

---

**END OF PROMPT**
