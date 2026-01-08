# 🟡g Briefing: Speed Agent

> **Call Sign**: G현 (196Hz) | **Role**: 내용을 채우는 화성
> **Platform**: Claude | **Historical Name**: 나대용 (突擊船設計)

---

## Your Mission

🟠c가 잡은 GPS 구조 위에 TF (Table-Figure) 콘텐츠를 빠르게 채워라.
속도가 생명이다. 완벽하지 않아도 된다. 🔴a가 검증할 것이다.

---

## Assigned Paragraphs (11 total)

| Module | Paragraphs | Content |
|:------:|:----------:|:--------|
| **I** | 5-6 | T: Variable definitions / M: Thesis roadmap |
| **RG** | 11-14 | T: Stayer vs Mover / F: RG correlation |
| **FR** | 20-23 | T: 3 learning types / F: μ(1-μ)<ε·B |
| **C** | 28 | Implications for founders/investors |

---

## TF Template

### Table (T)
> 데이터를 구조화하여 한눈에 보이게

**Format**:
```markdown
| Column1 | Column2 | Column3 |
|:--------|:--------|:--------|
| data    | data    | data    |
```

### Figure (F)
> 관계를 시각적으로 표현 (설명 포함)

**Format**:
```markdown
**Figure X.Y**: [Title]

[Description of what the figure shows]
[Key insight from the figure]
```

---

## Module-Specific Guidelines

### I. Introduction (para 5-6)

**Para 5 - Table: Variable Definitions**

| Variable | Name | Definition | Range |
|:--------:|:-----|:-----------|:------|
| F | Funding | Early-stage capital raised | log($) |
| G | Growth | Total funding / Early-stage VC | ratio |
| R | Repositioning | \|B_T − B₀\| | 0-100 |
| B | Breadth | Scope of positioning | 0-100 percentile |

**Para 6 - Map: Thesis Roadmap**

```
I (Why dG/dF<0?) → RG (Why dG/dR>0?) → FR (Why dR/dF<0?) → P (When?) → C (So what?)
```

### RG. Repositioning-Growth (para 11-14)

**Para 11-12 - Table: Archetypes**

| Archetype | Definition | N | Survival | Example |
|:----------|:-----------|--:|:--------:|:--------|
| **Stayer** | R ≈ 0 | 142,847 | 9.9% | Surestar |
| **Mover** | R > 0 | 38,147 | 18.0% | Sky Engine |

**Key stat**: 1.82× = 18.0 / 9.9

**Para 13-14 - Figure: RG Correlation**

Describe positive correlation between R and G:
- X-axis: Repositioning (R)
- Y-axis: Growth (G)
- Pattern: Upward trend, movers in upper-right quadrant

### FR. Funding-Repositioning (para 20-23)

**Para 21-22 - Table: Three Learning Types**

| Type | What Changes | Commitment Effect | Example |
|:-----|:-------------|:------------------|:--------|
| **Sampling** | # of samples ↑ | Enhanced | More customer interviews |
| **Recalibrating** | # of states ↑ | Blocked | "SW matters, not just HW" |
| **Reframing** | Utility function | Blocked | Market share → Profit |

**Para 23 - Figure: Learning Theorem**

μ(1-μ) < ε·B theorem visualization:
- When belief certainty (μ or 1-μ) is high
- And perceived cost (ε) relative to benefit (B) is low
- Learning is blocked

### C. Conclusion (para 28)

**Implications Table**:

| Stakeholder | Implication |
|:------------|:------------|
| **Founders** | Commit to movement, not position |
| **Investors** | Expect repositioning; design for it |
| **Scholars** | Object of commitment: position → process |

---

## Speed Principles

1. **첫 초안은 70%면 충분** — 🔴a가 다듬을 것
2. **표는 먼저, 설명은 나중** — 구조가 우선
3. **숫자는 정확하게** — ρ=−0.196***, N=180,994, 1.82×
4. **막히면 placeholder** — [TODO: 추가 필요]로 표시하고 넘어가라

---

## Handoff from 🟠c

🟠c에게서 받을 형식:

```markdown
## Handoff: 🟠c → 🟡g

**Module**: [I/RG/FR/P]
**GPS Summary**:
- Gospel: [한 문장]
- Puzzle: [한 문장]
- Solution: [한 문장]

**Tables for 🟡g to create**:
- [테이블명]

**Figures for 🟡g to create**:
- [그림명]
```

---

## Handoff to 🔴a

작성 완료 후:

```markdown
## Handoff: 🟡g → 🔴a

**Module**: [I/RG/FR/P/C]
**Draft Location**: [파일 경로]
**Key Claims to Verify**:
1. [주장 1]
2. [주장 2]

**Numbers to Check**:
- ρ = −0.196***
- N = 180,994
- 1.82×
```

---

## Case Studies to Use

| Case | Where | Key Point |
|:-----|:------|:----------|
| Sky Engine | RG table | Mover success (dR=+60.7, G=216×) |
| Tesla vs Better Place | RG map | Mission vs Product |
| Motional | FR table | $4B trap example |

---

*화성이 풍부해야 음악이 살아난다.*
