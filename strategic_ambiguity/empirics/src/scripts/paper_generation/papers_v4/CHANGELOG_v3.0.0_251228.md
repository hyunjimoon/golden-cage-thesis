# CHANGELOG v3.0.0 (2025-12-28)

> **Source**: Causal Direction Fix (User feedback on 2025-12-27)
> **Type**: MAJOR (Breaking conceptual change)
> **Gaps Closed**: G6~G8

---

## Summary: The Causal Fix

### Before (v2.x) — WRONG
```
Capital → Commitment → Trap
"펀딩이 몰입을 만든다"
```

### After (v3.0) — CORRECT
```
Commitment → Capital → Lock-in → Trap
   (Stage 1)    (Stage 2)
   Selection    Reinforcement
"몰입해야 펀딩받고, 펀딩이 고착시킨다"
```

---

## Why This Matters

| v2 해석 | v3 해석 |
|---------|---------|
| "돈 받으면 갇힌다" | "갇힐 사람만 돈 받는다" |
| 자본의 인과적 효과 | **Selection Effect + Reinforcement** |
| 펀딩이 원인 | 펀딩은 결과이자 증폭기 |

**핵심 통찰**: dM/dE < 0는 자본의 인과적 효과가 아니라, committed된 창업자만 선택되는 **Selection Effect**가 주 원인.

---

## Gaps Closed

| Gap | Description | Affected Files | Status |
|:---:|:------------|:---------------|:------:|
| G6 | I module causal language fix | I1.md ¶01, THESIS.html | ✅ |
| G7 | M4 selection effect 명시 | M4.md ¶34-35 | ✅ |
| G8 | T3 echo chamber two-stage | T3.md ¶66-67 | ✅ |

---

## Detailed Changes by Paragraph

### I1 ¶01 — Causal Direction Fix

**BEFORE:**
> Strategy theory and investment practice share an implicit assumption: **capital enables commitment**, commitment enables coordination, coordination enables growth.

**AFTER:**
> Strategy theory and investment practice share an implicit assumption: **commitment attracts capital**, capital enables coordination, coordination enables growth.

---

### M4 ¶34-35 — Selection Effect Added

**BEFORE:**
> This is not Camuffo-Nanda being wrong. It is Camuffo-Nanda being incomplete. Capital enables experimentation. But to obtain capital, founders must commit.
>
> **Capital creates commitment** through three channels...

**AFTER:**
> This is not Camuffo-Nanda being wrong. It is Camuffo-Nanda being incomplete. Capital enables experimentation. But to *obtain* capital, founders must first commit—precisely. **This is the selection effect**: investors fund confident visions, not acknowledged uncertainty.
>
> The mechanism operates in **two stages**. **Stage 1 (Selection)**: Commitment → Capital. Founders commit precisely to attract funding. **Stage 2 (Lock-in)**: Capital → Reinforcement. Once funded, commitment intensifies through three channels...

---

### T3 ¶66-67 — Two-Stage Echo Chamber

**BEFORE:**
> Staw's (1976) escalation research explains the mechanism...
>
> The echo chamber forms naturally. Precise visions attract investors who believe that exact thesis.

**AFTER:**
> The mechanism operates in **two stages**. **Stage 1 (Selection)**: Commitment attracts capital—founders who articulate precise visions attract investors who believe that exact thesis. **Stage 2 (Lock-in)**: Capital reinforces commitment. Staw's (1976) escalation research explains why...
>
> The echo chamber forms through both stages: **selection filters for believers, lock-in silences doubters**.

---

### Abstract — Two-Stage Mechanism

**BEFORE:**
> **The Mechanism:** Capital creates commitment through psychological, structural, and social channels.

**AFTER:**
> **The Mechanism:** The process operates in two stages. *Stage 1 (Selection)*: Commitment attracts capital—investors fund confident visions. *Stage 2 (Lock-in)*: Capital reinforces commitment through psychological, structural, and social channels.

---

## Files Updated

| File | Change |
|:-----|:-------|
| `1_I_introduction/I1.md` | ¶01 causal fix |
| `2_M_movement_matters/M4.md` | ¶34-35 selection effect |
| `3_T_funding_traps/T3.md` | ¶66-67 two-stage echo chamber |
| `🎓THESIS_v3.0.0_251228_MIT.html` | Abstract, I.1, T.3 |
| `dashboard_v4.html` | Consistency tracker + I1, M4, T3 borders |

---

## Structural Changes

| Change | Details |
|:-------|:--------|
| Folder rename | `1_P_paradox/` → `1_I_introduction/` |
| File rename | `P1.md` → `I1.md` |
| obi-wan.md | Paper structure updated (📿-🧩-🔍 framework) |

---

## Version Rule

```
vMAJOR.MINOR.PATCH_YYMMDD

v3.0.0_251228:
- MAJOR=3: 인과 방향 수정 (Breaking conceptual change)
- MINOR=0: 새 버전 시작
- PATCH=0: 초기
- DATE=251228: 오늘
```

---

## Next: v4.0.0 Preview

v4에서 예정된 구조 변경:
- T module → V module (Vagueness)
- M subagents: MG (dG/dM) + MF (dM/dF)
- V subagents: VM (dM/dV) + VD (dD/dV)
- E module: Motional 처방 (Platformize → Acculturate → Evaluate)

---

*必死卽生, 必生卽死*
*Commit to ADAPTATION, direction first and speed second.*
