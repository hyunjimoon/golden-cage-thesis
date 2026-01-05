# C. Conclusion (2 paragraphs)

> **Core Question**: So what?

---

## Task Tool Commands

### 🟡g: Implications (para 28)
```
Task(subagent_type="general-purpose", prompt="""
C module para 28 작성:

Implications:
- For Founders: "Commit to movement, not position"
- For Investors: "Expect repositioning; design for signal diversity"
- For Scholars: "Object of commitment: position → process"

Output: 1개 단락 (150 words)
""")
```

### 🔴a: Limitations + Summary (para 29)
```
Task(subagent_type="general-purpose", prompt="""
C module para 29 작성:

Limitations:
1. Not causal (correlation only, endogeneity)
2. Crunchbase data limitations
3. Future: LTE simulation needed

Summary: One-sentence thesis
"Commitment attracts believers; believers provide funding;
funding solidifies the echo chamber; echo chambers block learning."

Output: 1개 단락 (150 words)
""")
```

### 🔴a: 최종 검증
```
Task(subagent_type="general-purpose", prompt="""
전체 논문 최종 검증:

1. One-sentence summary 일관성 (모든 module에서 동일)
2. Canonical numbers 정확성:
   - ρ = −0.196***
   - N = 180,994
   - 1.82× (18.0% vs 9.9%)
3. Causal chain 순서: Commitment → Believers → Funding → Echo Chamber
4. "Can't not won't" 일관성 (governance vs moral hazard)

Output: 최종 검증 리포트
""")
```

---

## Content

### Para 28: Implications (🟡g)

**For Founders**:
> "Commit to movement, not to position."
> "Commit to direction, not destination."

**For Investors**:
> "The ventures most likely to succeed may reposition away from the pitch that won your commitment."
> "Design for signal diversity ex ante."

**For Scholars**:
> "In nascent environments, the object of commitment must shift from position to process."

---

### Para 29: Limitations + Summary (🔴a)

**Limitations**:
1. **Not causal**: Correlation ≠ Causation (endogeneity)
2. **Sample**: Crunchbase data limitations
3. **Future work**: LTE simulation to replicate phenomena

**Summary**:

> **"Commitment attracts believers; believers provide funding; funding solidifies the echo chamber; echo chambers block learning."**

---

## Core Contribution

| Dimension | Existing Literature | This Thesis |
|:----------|:--------------------|:------------|
| **Problem** | Founders **won't** pivot | Founders **can't** pivot |
| **Cause** | Moral hazard (incentive) | Governance lock-in (structure) |
| **Mechanism** | Agency problem | Commitment → Believers → Funding → Echo Chamber |
| **Solution** | Monitor founders | Design signal diversity ex ante |

---

## Status

| Para | Role | Task | Status |
|:----:|:----:|:-----|:------:|
| 28 | 🟡g | Implications | ⬜ |
| 29 | 🔴a | Limitations + Summary | ⬜ |
| — | 🔴a | Final verify | ⬜ |
