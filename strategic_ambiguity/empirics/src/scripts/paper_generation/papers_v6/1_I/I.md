# I. Introduction (6 paragraphs)

> **Core Question**: Why dG/dF < 0?

---

## Task Tool Commands

### 🟠c: GPS 구조 (para 1-4)
```
Task(subagent_type="general-purpose", prompt="""
I module GPS 작성:

Gospel: "Cash is oxygen" 통념을 학술적으로 서술
Puzzle: ρ = −0.196*** (N=180,994) 발견 제시
Solution: dG/dF = (dG/dR)(dR/dF) = (+)(−) 분해 설명

Output: 4개 단락 (각 150 words)
""")
```

### 🟡g: TF 초안 (para 5-6)
```
Task(subagent_type="general-purpose", prompt="""
I module TF 작성:

Table: Variable definitions (F, G, R, B)
Map: I→RG→FR→P→C thesis roadmap

Output: 2개 단락 + 표 1개
""")
```

### 🔴a: 검증 (double-check)
```
Task(subagent_type="general-purpose", prompt="""
I module 검증:

1. Causal chain: Commitment → Believers → Funding → Echo Chamber 순서 확인
2. Numbers: ρ=−0.196***, N=180,994 정확성
3. Logic: GPS 간 논리 연결 점검

Output: ✅ Pass / 🔄 Revise (수정사항 명시)
""")
```

---

## Content

### Para 1-2: Gospel + Puzzle (🟠c)

**Gospel (G)**:
> [TODO] "Cash is oxygen for startups — more funding enables more growth."

**Puzzle (P)**:
> [TODO] ρ(F,G) = −0.196*** (N=180,994): more early funding correlates with less growth.

---

### Para 3-4: Solution (🟠c)

**Solution (S)**:
> [TODO] Decomposition: dG/dF = (dG/dR)(dR/dF) = (+)(−) = (−)

$$\frac{dG}{dF} = \underbrace{\frac{dG}{dR}}_{\text{RG: (+)}} \times \underbrace{\frac{dR}{dF}}_{\text{FR: (-)}} = (-)$$

---

### Para 5: Table (🟡g)

| Variable | Name | Definition | Range |
|:--------:|:-----|:-----------|:------|
| F | Funding | Early-stage capital raised | log($) |
| G | Growth | Total funding / Early-stage VC | ratio |
| R | Repositioning | \|B_T − B₀\| | 0-100 |
| B | Breadth | Scope of positioning | 0-100 percentile |

---

### Para 6: Map (🟡g)

```
I (Why dG/dF<0?) → RG (dG/dR>0) → FR (dR/dF<0) → P (When?) → C (So what?)
```

---

## Status

| Para | Role | Task | Status |
|:----:|:----:|:-----|:------:|
| 1-2 | 🟠c | GPS: Gospel+Puzzle | ⬜ |
| 3-4 | 🟠c | GPS: Solution | ⬜ |
| 5 | 🟡g | Table: Variables | ⬜ |
| 6 | 🟡g | Map: Roadmap | ⬜ |
| — | 🔴a | Verify all | ⬜ |
