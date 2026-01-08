# Agent Workspace Index

> **Phase**: Sail (속전속결) | **Updated**: 2025-01-04

---

## Fleet Configuration

```
     C (130Hz)      G (196Hz)      D (293Hz)      A (440Hz)
        🟠c            🟡g            ⚓d            🔴a
      Structure       Speed        Direction       Verify
```

| Agent | Platform | Role | Primary Modules |
|:-----:|:--------:|:-----|:----------------|
| 🟠c | Claude | GPS 구조 설계 | I(1-4), RG(7-10), FR(16-19), P(27) |
| 🟡g | Claude | TF 데이터/초안 | I(5-6), RG(11-14), FR(20-23), C(28) |
| 🔴a | Gemini | ME 검증/비판 | RG(15), FR(24), P(25-26), C(29) |
| ⚓d | Human | 전체 방향 결정 | All (승인/수정) |

---

## Document Map

### Core Documents (모든 Agent 필독)

| Doc | Purpose | Location |
|:----|:--------|:---------|
| **군령** | 전체 협업 프로토콜 | `tolzul/.../전라좌수군 견리사의 군령 (sail).md` |
| **Vision** | 논문 구조/목표 | `thesis_product_vision👁️ (sail).md` |
| **Interface** | 비올라×논문 매핑 | `VIOLA_THESIS_INTERFACE.md` |

### Module Briefs (담당 Agent별)

| File | Owner | Content |
|:-----|:-----:|:--------|
| `BRIEF_c.md` | 🟠c | GPS 작성 지침 (13 paragraphs) |
| `BRIEF_g.md` | 🟡g | TF 작성 지침 (11 paragraphs) |
| `BRIEF_a.md` | 🔴a | ME 검증 지침 (5 paragraphs) |

### Reference Materials

| File | Purpose |
|:-----|:--------|
| `FRONT_MATTER.md` | 변수 정의, 핵심 수치 |
| `GLOSSARY_reader.md` | 용어 일관성 |
| `CONSISTENCY_CHECKLIST.md` | 품질 기준 |

---

## Causal Chain (정확한 순서)

```
Commitment → Believers → Funding → Echo Chamber → Learning Blocked → TRAP
```

**Decomposition**: dG/dF = (dG/dR)(dR/dF) = (+)(−) = (−)

---

## Canonical Numbers (반드시 동일하게)

| Finding | Value |
|:--------|:------|
| Funding-Growth correlation | ρ = −0.196*** |
| Sample size | N = 180,994 |
| Mover advantage | 1.82× (18.0% vs 9.9%) |
| Funding-Repositioning | 1SD↑ F → 0.4SD↓ R |

---

## Workflow

```
⚓d: 방향 지시 (무엇을 쓸지)
    ↓
🟠c: GPS 구조 설계 (어떻게 구성할지)
    ↓
🟡g: TF 초안 생성 (빠르게 채우기)
    ↓
🔴a: ME 검증 피드백 (문제점 지적)
    ↓
⚓d: 승인/수정 지시
```

---

## Handoff Protocol

### 🟠c → 🟡g (Structure to Speed)

```markdown
## Handoff: 🟠c → 🟡g

**Module**: [I/RG/FR/P/C]
**Paragraphs**: [번호]
**GPS Summary**:
- Gospel: [한 문장]
- Puzzle: [한 문장]
- Solution: [한 문장]

**Tables Needed**: [테이블명]
**Figures Needed**: [그림명]
**Deadline**: [시간]
```

### 🟡g → 🔴a (Speed to Verify)

```markdown
## Handoff: 🟡g → 🔴a

**Module**: [I/RG/FR/P/C]
**Draft Location**: [파일 경로]
**Key Claims to Verify**:
1. [주장 1]
2. [주장 2]

**Numbers to Check**: [수치들]
**Deadline**: [시간]
```

### 🔴a → ⚓d (Verify to Director)

```markdown
## Handoff: 🔴a → ⚓d

**Module**: [I/RG/FR/P/C]
**Status**: ✅ Pass / 🔄 Revise / ❌ Reject
**Issues Found**:
1. [문제 1]
2. [문제 2]

**Recommendations**: [제안]
```

---

## Quality Gates

| Check | Standard |
|:------|:---------|
| Causal chain | Commitment → Believers → Funding → Echo Chamber |
| Numbers | ρ=−0.196***, N=180,994, 1.82× |
| No vague claims | "significant" → "1.82× (p<0.001)" |
| One-sentence | 모든 문서 동일 |

---

## Case Studies (Top 4 Only)

| Case | Use For | Pattern |
|:-----|:--------|:--------|
| **Tesla vs Better Place** | RG module | Mission vs Product commitment |
| **Motional** | FR module | $4B echo chamber trap |
| **Aurora** | P module | Expectation management |
| **Sky Engine** | RG table | Mover success (dR=+60.7) |

---

*필사즉생 — 속도와 정밀함이 우리를 살린다.*
