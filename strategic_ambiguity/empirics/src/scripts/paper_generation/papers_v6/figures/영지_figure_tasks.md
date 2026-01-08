# 영지 Figure Tasks (見 See)

> 덕목: 見 (Observe/See) — 본질을 포착하여 시각화

---

## 4 Required Figures

### Fig-I: Funding Paradox (I Column, ¶5)

| Spec | Value |
|:-----|:------|
| **X-axis** | F (Funding) - log scale |
| **Y-axis** | G (Growth) |
| **Slope** | **Negative** (ρ = −0.196***) |
| **Color** | 🔴 Red (#ff6b6b) |
| **Message** | "More funding → Less growth" |
| **N** | 408,784 ventures |

**Caption**: More funding correlates with less growth (ρ = −0.196, p < 0.001, N = 408,784)

---

### Fig-CFR: Golden Cage Effect (CFR Column)

| Spec | Value |
|:-----|:------|
| **X-axis** | F (Funding) - log scale |
| **Y-axis** | R (Repositioning) |
| **Slope** | **Negative** (−0.4 SD per +1 SD F) |
| **Color** | 🟡 Gold (#d4a84b) |
| **Message** | "More funding → Less repositioning" |

**Caption**: Well-funded ventures adapt less: +1SD funding correlates with −0.4SD repositioning

---

### Fig-FRG: Mover Advantage (FRG Column)

| Spec | Value |
|:-----|:------|
| **X-axis** | R (Repositioning) |
| **Y-axis** | G (Growth) |
| **Slope** | **Positive** |
| **Color** | 🟣 Purple (#a855f7) for R, 🟢 Green (#69db7c) for G |
| **Message** | "More repositioning → More growth" |
| **Highlight** | Movers (R≥10) vs Stayers (R<10) |

**Caption**: Movers outperform Stayers by 1.82× (18.0% vs 9.9% survival)

---

### Fig-Rob: 3-Panel Robustness (FRG Column, ¶23)

| Panel | X-axis | Y-axis | Expected Slope |
|:------|:-------|:-------|:---------------|
| **Panel A** | F | G | Negative (−) |
| **Panel B** | F | R | Negative (−) |
| **Panel C** | R | G | Positive (+) |

**Layout**: 1 row × 3 columns

**Caption**: Decomposition holds across multi-year panels: dG/dF = (dG/dR)(dR/dF) = (+)(−) = (−)

---

## Color Semantic (Thesis-wide)

| Variable | Color | Hex | Meaning |
|:---------|:------|:----|:--------|
| F (Funding) | 🔵 Blue | #4dabf7 | Input, neutral |
| R (Repositioning) | 🟣 Purple | #a855f7 | Movement, change |
| G (Growth) | 🟢 Green | #69db7c | Positive outcome |
| Cage | 🟡 Gold | #d4a84b | Trap, constraint |
| I (Introduction) | 🔴 Red | #ff6b6b | Problem, alert |

---

## CARE Checklist for Figures

- [ ] **C**risp: One figure = one message
- [ ] **A**ccessible: Colorblind-safe, readable at 50% zoom
- [ ] **R**eader-loving: Main insight obvious in 3 seconds
- [ ] **E**arned: Every element justifies its existence

---

## 영지 Invocation Template

```markdown
You are 영지, 덕목 見 (See).
Task: Create Fig-[I/CFR/FRG/Rob]
Upstream: 수진's data analysis
Output:
  - Figure file (PNG/SVG)
  - Caption (1-2 sentences)
  - Status update
```

---

## Dependencies

```
수진 (data) → 영지 (figure)
```

영지 figures depend on 수진's empirical results. Coordinate with:
- ¶2 (수진): ρ(F,G) = −0.196 data
- ¶10-13 (수진): CFR theory variables
- ¶19-21 (수진): FRG theory variables

---

*Status*: ⬜ Fig-I | ⬜ Fig-CFR | ⬜ Fig-FRG | ⬜ Fig-Rob
