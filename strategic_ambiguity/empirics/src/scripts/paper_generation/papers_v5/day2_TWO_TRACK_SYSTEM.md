# Two-Track Update System

## Overview

| Track | Location | Audience | Strategy |
|:------|:---------|:---------|:---------|
| **Advisor-facing** | `w9_acculturate(thesis)/` | Charlie, Scott | Sequential reveal, minimal complexity |
| **Personal** | `papers_v5/` | Angie | Full simulation, all 7 modules |

---

## Rationale

### 1. Foreshadowing Effect
Day 1 피드백이 전체 7 모듈에 미치는 영향을 미리 시뮬레이션:
- V → B 변경 → MG, MF, VM, VD, E 모든 모듈 용어 업데이트
- "Contingent qualification" → I, M 모듈 Van den Steen 프레이밍 일관성

### 2. Dynamic Optimization
피드백에 따른 빠른 대응:
- Personal track: 전체 영향 즉시 반영
- Advisor track: 해당 day 모듈만 reveal

### 3. Cognitive Load Management
교수님들께 과부하 방지:
- 하루에 1개 모듈 + 3개 질문
- Dashboard는 해당 day 모듈만 강조

---

## Folder Structure

```
Advisor-facing (Dropbox)
w9_acculturate(thesis)/
├── PROTOCOL.md              ← 전체 프로토콜 (공개)
├── day1_intro/
│   └── I, QUESTIONS_FOR_ADVISORS
├── day2_paperE/             ← TODAY
│   └── E.md, QUESTIONS_FOR_ADVISORS2
├── day3_paperM/
├── day4_paperV/
└── day5_integration/

Personal (tolzul)
papers_v5/
├── paper(thesis)_v5_prior.md    ← 전체 thesis 현황
├── TWO_TRACK_SYSTEM.md          ← 이 문서
├── 1_I_introduction/
├── 2_M_movement/
├── 3_V_vagueness/
├── 4_E_escape/
├── 5_C_conclusion/
├── dashboard_v5_prior_minimal.html   ← Advisor용 (오늘 생성)
└── dashboard_v5_prior_full.html      ← Personal용
```

---

## Dashboard Evolution Strategy

### Day-by-Day Minimal Dashboards

| Day | Advisor Dashboard | Focus |
|:----|:-----------------|:------|
| Day 1 | I only | Core equation, 5 variables |
| Day 2 | I + E | PAE Framework, Motional |
| Day 3 | I + E + M | Repositioning Principle |
| Day 4 | I + E + M + V | Learning Traps |
| Day 5 | Full | Integration |

### Complexity Levels

```
Level 0 (Minimal): Core equation + 5 variables only
    ↓
Level 1 (Day view): + Current day's module expanded
    ↓
Level 2 (Week view): + All modules collapsed
    ↓
Level 3 (Full): + All paragraphs, prompts, bottlenecks
```

---

## Sync Protocol

### After Each Advisor Meeting:
1. **Personal track**: Incorporate feedback → all 7 modules
2. **Advisor track**: Update only current day's `post/` folder
3. **Dashboard**: Regenerate minimal version for next day

### Before Each Day:
1. **Personal track**: Simulate today's feedback impact
2. **Advisor track**: Prepare `prior/` folder with E.md, QUESTIONS

---

## Today's Implementation (Day 2)

### Advisor Track (w9_acculturate)
```
day2_paperE/
├── EMAIL_BODY.md           ✓
├── angie_prior2post/
│   ├── prior/
│   │   ├── E.md            ✓
│   │   └── QUESTIONS_FOR_ADVISORS2.md  ✓
│   ├── likelihood/         (after meeting)
│   └── post/               (tonight)
├── charlie/                (Charlie's feedback)
└── scott/                  (Scott's feedback)
```

### Personal Track (papers_v5)
```
papers_v5/
├── paper(thesis)_v5_prior.md           ✓
├── TWO_TRACK_SYSTEM.md                 ✓ (this file)
└── dashboard_v5_prior_minimal.html     (next)
```

---

## Next Steps

1. Create `dashboard_v5_prior_minimal.html` for advisors
   - Core equation + 5 variables
   - I module: completed (Day 1 feedback)
   - E module: in progress (Day 2 focus)
   - M, V, C: pending (grayed out)

2. After Motional meeting (#4):
   - Update E.md with project scoping details
   - Update dashboard with Motional status

3. After advisor meeting:
   - Personal: propagate feedback to all modules
   - Advisor: update day2 post/ folder

---

*Last updated: Dec 30, 2024*
