# Gemini Image Generation Prompt: Thesis Protocol Visualization

**Purpose**: Visualize the rational agency framework and trajectory comparison using 五行 (Five Elements) color symbolism.

---

## Prompt (English)

```
Create an academic diagram showing rational agency in thesis development, using 五行 (Five Elements) color symbolism.

=== COLOR LEGEND (五行) ===
- 火 Fire Red (#C62828): Action, Discovery, Creation — "NEW?"
- 水 Water Blue (#1976D2): Flow, Transition, Understanding — "WHY?"
- 木 Wood Green (#2E7D32): Growth, Progress, Implementation — "HOW?"
- 金 Metal Gold (#FFD700): Refinement, Value, Quality — Output
- 土 Earth Yellow (#FFC107): Foundation, State, Turning Point — Start

=== LAYOUT: Three Sections ===

--- TOP SECTION: Rational Agency Flow (五行 Cycle) ---

Circular flow showing generative cycle (相生):

        [s_t] 土 Yellow
           ↓ generates
    [Action] 火 Red ──→ [Environment] 水 Blue
                              ↓ generates
                        [s_{t+1}] 木 Green
                              ↓ generates
                        [Utility] 金 Gold
                              ↓ generates
                        [argmax] → back to 土

Center formula: "a* = argmax_a E[U(s_{t+1}) | s_t, a]"

Show 相生 (generating) cycle arrows connecting the elements in proper order.

--- MIDDLE SECTION: Two Parallel Trajectories ---

LEFT PATH "Actual: Pretty → New" (실제):
- 8 nodes in a winding, inefficient path: s₁ → s₂ → s₃ → s₄ → s₅ → s₆ → s₇ → s₈
- Nodes s₁-s₅: Faded GRAY with small red X marks (wasted polish cycles)
- Labels under s₁-s₅: "Polish" in gray text
- Node s₆: 土 YELLOW burst with star shape — "이게 최선?" (turning point)
- Node s₇: 火 RED — "Discover"
- Node s₈: 木 GREEN — "Refine"
- Path style: Curved, meandering, with some backtracking
- Below path: "8 transitions | 5h | 40% waste | 相剋 (conflict)"

RIGHT PATH "Counterfactual: New → Why → How" (반사실):
- 4 nodes in a straight diagonal ascending line: s'₁ → s'₂ → s'₃ → s'₄
- Node s'₁: 火 RED circle — "NEW?" with lightbulb icon
- Node s'₂: 水 BLUE circle — "WHY?" with chain link icon
- Node s'₃: 木 GREEN circle — "HOW?" with wrench icon
- Node s'₄: 金 GOLD circle — "DONE" with checkmark icon
- Path style: Straight, efficient diagonal line going up-right
- Arrows between nodes: Solid, confident, with "E[Δs]=high" labels
- Below path: "4 transitions | 2h | 10% waste | 相生 (generation)"

CENTER between paths:
- Large curved arrow pointing from left path to right path
- Label: "2-4× efficiency gain"
- Small text: "Same destination, better path"

--- BOTTOM SECTION: Evaluation Formula ---

Three interlocking circles (Venn diagram style):

     火 RED circle
    "NEW?" (35%)
   Contribution
        ∩
水 BLUE      木 GREEN
"WHY?"  ∩   "HOW?"
(35%)       (30%)
Mechanism   Operation

Center intersection (where all three meet): 金 GOLD — "Thesis Quality"

Formula below the Venn diagram:
"U = 0.35(火 Contribution) + 0.35(水 Mechanism) + 0.30(木 Operationalization)"

--- BOTTOM BANNER ---

Two lines showing the key insight:

Line 1 (crossed out with strikethrough, gray color):
"OLD: 土 → ? → ? → ? → 土 → 火 → 木"
"Pretty first, New later — Random walk, late discovery"

Line 2 (bold, highlighted):
"NEW: 土 → 火 → 水 → 木 → 金"
"New first, Pretty follows — Directed search, early discovery"

=== STYLE SPECIFICATIONS ===

Overall:
- Clean academic diagram style (inspired by Russell & Norvig AI textbook)
- White background
- Slight shadow on main elements for depth
- Professional, minimalist aesthetic

Colors (use exact hex codes):
- 火 Fire Red: #C62828
- 水 Water Blue: #1976D2
- 木 Wood Green: #2E7D32
- 金 Metal Gold: #FFD700
- 土 Earth Yellow: #FFC107
- Gray (waste): #9E9E9E
- Black (text): #212121
- White (background): #FFFFFF

Typography:
- Main labels: Sans-serif bold (Helvetica Neue or similar)
- Formula text: Monospace or italic serif
- Chinese characters (五行): Slightly larger, can be decorative
- Korean text: Clean sans-serif

Shapes:
- State nodes: Circles with thick borders (3-4px)
- Component boxes: Rounded rectangles
- Arrows: Solid black lines with arrowheads, 2px thickness
- Dotted arrows for uncertain/wasteful transitions

Icons (optional but nice):
- Lightbulb for "NEW?"
- Chain links for "WHY?" (causation)
- Wrench/gear for "HOW?"
- Star/trophy for "DONE"

Layout:
- Aspect ratio: 16:9 or 4:3
- Top section: 25% of height
- Middle section: 50% of height
- Bottom section: 25% of height
- Generous margins and spacing

=== OPTIONAL ELEMENTS ===

- Subtle 太極 (yin-yang) watermark in corner (very light, 10% opacity)
- Small 五行 symbols next to element names
- Gradient transitions between elements following 相生 cycle
```

---

## Prompt (한글 버전)

```
위와 동일하되 라벨 변경:

TOP SECTION:
- "Current State" → "현재 상태"
- "Action" → "행동"
- "Environment" → "환경/전이"
- "Next State" → "다음 상태"
- "Utility" → "효용"

MIDDLE SECTION:
- "Actual: Pretty → New" → "실제: 예쁘게 → 새롭게"
- "Counterfactual: New → Why → How" → "반사실: 새롭게 → 왜 → 어떻게"
- "Polish" → "다듬기"
- "Discover" → "발견"
- "Refine" → "정제"
- "DONE" → "완료"
- "waste" → "낭비"
- "efficiency gain" → "효율 개선"

BOTTOM BANNER:
- "Pretty first, New later" → "예쁘게 먼저, 새롭게 나중에"
- "New first, Pretty follows" → "새롭게 먼저, 예쁨은 따라온다"
- "Random walk, late discovery" → "무작위 탐색, 늦은 발견"
- "Directed search, early discovery" → "방향성 탐색, 빠른 발견"
```

---

## Simple Version (for quick generation)

```
Create a simple diagram comparing two learning paths:

LEFT: Winding gray path with 8 nodes, labeled "Polish → Polish → Challenge! → Discover"
- Colors: Gray nodes (waste) → Yellow burst (turning point) → Green (success)
- Caption: "5 hours, 40% waste"

RIGHT: Straight diagonal path with 4 nodes, labeled "NEW? → WHY? → HOW? → DONE"
- Colors: Red → Blue → Green → Gold (following 五行 cycle)
- Caption: "2 hours, 10% waste"

Bottom: Three overlapping circles (red "NEW", blue "WHY", green "HOW") = gold center "Quality"

Style: Clean, academic, white background, bold colors
```

---

## Usage Notes

1. **For Gemini**: Copy the full prompt above
2. **For other image generators**: Use the "Simple Version"
3. **Color codes are exact** — use hex values for consistency
4. **五行 ordering matters** — follow 相生 (generation) not 相剋 (conflict)

---

*Created: January 3, 2025*
