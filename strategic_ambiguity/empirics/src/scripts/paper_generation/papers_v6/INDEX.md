# papers_v6: Sail Edition

> **Phase**: Sail (속전속결) | **Structure**: I-RG-FR-P-C | **Date**: 2025-01-04

---

## Core Thesis

> **"Commitment attracts believers; believers provide funding; funding solidifies the echo chamber; echo chambers block learning."**

### Decomposition
$$\frac{dG}{dF} = \underbrace{\frac{dG}{dR}}_{\text{(+)}} \times \underbrace{\frac{dR}{dF}}_{\text{(-)}} = (-)$$

### Canonical Numbers
| Finding | Value |
|:--------|:------|
| Funding-Growth correlation | ρ = −0.196*** |
| Sample size | N = 180,994 |
| Mover advantage | 1.82× (18.0% vs 9.9%) |

---

## Folder Structure

```
papers_v6/
├── INDEX.md                    # 이 파일
├── GLOSSARY.md                 # 용어 정의
├── CORE_CONTRIBUTION.md        # 핵심 기여
├── IMAGE_PROMPT_gemini.md      # 이미지 생성 프롬프트
│
├── 1_I/I.md                    # Introduction (6 para) + Task commands
├── 2_RG/RG.md                  # Repositioning-Growth (9 para) + Task commands
├── 3_FR/FR.md                  # Funding-Repositioning (9 para) + Task commands
├── 4_P/P.md                    # Prescribe (3 para) + Task commands
├── 5_C/C.md                    # Conclusion (2 para) + Task commands
│
└── figures/                    # Python figure scripts
    ├── fig_I_stayer_vs_mover.py
    ├── fig_BM_motional_strategy.py
    └── C_fig1_prescription.py
```

---

## Task Tool Workflow

각 module 파일에 Task tool 명령어가 내장되어 있음:

```
🟠c Task → GPS 구조 작성 (13 para)
    ↓
🟡g Task → TF 초안 생성 (11 para)
    ↓
🔴a Task → ME 작성 + 전체 검증 (5 para + verify)
    ↓
⚓d → 승인/수정
```

### 병렬 실행 예시

```python
# I, RG module 동시 작성
Task(subagent_type="general-purpose", prompt="I module GPS...")
Task(subagent_type="general-purpose", prompt="RG module GPS...")
# → 자동 병렬 실행
```

---

## Module Overview (29 Paragraphs)

| Module | Para | Core Question | 🟠c | 🟡g | 🔴a |
|:------:|:----:|:--------------|:---:|:---:|:---:|
| **I** | 6 | Why dG/dF < 0? | 1-4 | 5-6 | verify |
| **RG** | 9 | Why dG/dR > 0? | 7-10 | 11-14 | 15+verify |
| **FR** | 9 | Why dR/dF < 0? | 16-20 | 21-23 | 24+verify |
| **P** | 3 | When to commit? | 27 | — | 25-26+verify |
| **C** | 2 | So what? | — | 28 | 29+verify |

---

## Agent Roles (Task tool로 실행)

| Agent | Role | subagent_type | Paragraphs |
|:-----:|:-----|:--------------|:----------:|
| 🟠c | GPS 구조 설계 | general-purpose | 13 |
| 🟡g | TF 초안 생성 | general-purpose | 11 |
| 🔴a | ME + 검증 | general-purpose | 5 + all verify |
| ⚓d | 방향 결정 | Human | 승인 |

---

## Quality Gates

| Check | Standard |
|:------|:---------|
| Causal chain | Commitment → Believers → Funding → Echo Chamber |
| Numbers | ρ=−0.196***, N=180,994, 1.82× |
| One-sentence | 모든 module에서 동일 |
| Can't not won't | Governance lock-in (not moral hazard) |

---

## Execution Order

```
Phase 1: 🟠c GPS (병렬)
├── Task: I module GPS (para 1-4)
├── Task: RG module GPS (para 7-10)
├── Task: FR module GPS (para 16-20)
└── Task: P module Balance (para 27)

Phase 2: 🟡g TF (병렬)
├── Task: I module TF (para 5-6)
├── Task: RG module TF (para 11-14)
├── Task: FR module TF (para 21-23)
└── Task: C module Implications (para 28)

Phase 3: 🔴a ME + Verify (병렬)
├── Task: RG module ME (para 15)
├── Task: FR module ME (para 24)
├── Task: P module Prescription (para 25-26)
├── Task: C module Summary (para 29)
└── Task: 전체 검증

Phase 4: ⚓d 승인
└── Human review & approval
```

---

*필사즉생 — 속도와 정밀함이 우리를 살린다.*
