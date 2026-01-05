# RG. Repositioning-Growth (9 paragraphs)

> **Core Question**: Why dG/dR > 0?

---

## Task Tool Commands

### 🟠c: GPS 구조 (para 7-10)
```
Task(subagent_type="general-purpose", prompt="""
RG module GPS 작성:

Gospel: Porter's "commit to sustainable position" 통념
Puzzle: dG/dR > 0, Movers 1.82× Stayers (18.0% vs 9.9%)
Solution: Partial commitment + Perceive ⇄ Act feedback loop

Output: 4개 단락 (각 150 words)
Numbers: 1.82×, 18.0%, 9.9% 정확히 사용
""")
```

### 🟡g: TF 초안 (para 11-14)
```
Task(subagent_type="general-purpose", prompt="""
RG module TF 작성:

Table: Stayer vs Mover 비교 (N, survival rate, examples)
Figure: R-G positive correlation 설명

Output: 4개 단락 + 표 1개
Key examples: Sky Engine (dR=+60.7, G=216×)
""")
```

### 🔴a: ME + 검증 (para 15)
```
Task(subagent_type="general-purpose", prompt="""
RG module ME 작성 + 전체 검증:

Map: Tesla vs Better Place (mission vs product commitment)
Exit: Limitations (selection bias, hindsight bias)

검증:
1. 1.82× = 18.0/9.9 계산 확인
2. Mover/Stayer 정의 일관성
3. Tesla case 정확성

Output: 1개 단락 + 검증 리포트
""")
```

---

## Content

### Para 7-8: Gospel + Puzzle (🟠c)

**Gospel (G)**:
> [TODO] Porter: "Choose a sustainable position and defend it."

**Puzzle (P)**:
> [TODO] dG/dR > 0 — Movers outperform Stayers by 1.82× (18.0% vs 9.9%)

---

### Para 9-10: Solution (🟠c)

**Solution (S)**:
> [TODO] Partial commitment + Perceive ⇄ Act feedback loop

---

### Para 11-12: Table (🟡g)

| Archetype | Definition | N | Survival | Example |
|:----------|:-----------|--:|:--------:|:--------|
| **Stayer** | R ≈ 0 | 142,847 | 9.9% | Surestar |
| **Mover** | R > 0 | 38,147 | 18.0% | Sky Engine |

**Key stat**: 1.82× = 18.0 / 9.9

---

### Para 13-14: Figure (🟡g)

**F1(RG): R-G Positive Correlation**

[TODO] Description:
- X-axis: Repositioning (R)
- Y-axis: Growth (G)
- Pattern: Upward trend, movers in upper-right

---

### Para 15: Map + Exit (🔴a)

**Map: Tesla vs Better Place**

| Pattern | Company | Promise Type | Commitment | Outcome |
|:--------|:--------|:-------------|:-----------|:--------|
| Success | Tesla | Mission ("Sustainable energy") | Staged | Global leader |
| Trap | Better Place | Product ("Battery swap") | Full upfront | Liquidation 2013 |

**Exit: Limitations**
1. Selection bias: 성공 사례 과대대표
2. Hindsight bias: 사후적 해석 위험

---

## Status

| Para | Role | Task | Status |
|:----:|:----:|:-----|:------:|
| 7-8 | 🟠c | GPS: Gospel+Puzzle | ⬜ |
| 9-10 | 🟠c | GPS: Solution | ⬜ |
| 11-12 | 🟡g | Table: Archetypes | ⬜ |
| 13-14 | 🟡g | Figure: RG correlation | ⬜ |
| 15 | 🔴a | ME + Verify | ⬜ |
