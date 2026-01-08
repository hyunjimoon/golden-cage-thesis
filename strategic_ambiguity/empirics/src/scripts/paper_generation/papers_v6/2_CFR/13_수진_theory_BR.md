# ¶13 수진_theory(BR): Learning Trap Formula

> **Agent**: 수진 (見 Observe)
> **Row**: Table (T) + Figure (F) — Theorem
> **Status**: 📝 Draft

---

## Content

**Theorem 1 (Learning Trap).** *Learning ceases when:*

$$\mu(1-\mu) < \frac{\varepsilon}{B}$$

where:
- μ = probability of success (belief)
- ε = belief mean shift from new signal
- B = breadth (inverse precision)

---

## Interpretation

| Condition | Effect |
|:----------|:-------|
| **High certainty** (μ → 1) | LHS → 0, trap triggered |
| **Narrow focus** (small B) | RHS increases, trap triggered |
| **Both conditions** | Learning cessation guaranteed |

Both conditions—high certainty and narrow focus—are characteristic of well-funded ventures with specific commitments.

---

## Figure Reference

![Fig-FR2: Learning Trap](../../figures/Fig-FR2_learning_trap.png)

The venture *cannot* update even when updating would be optimal.

---

## Dependencies

- **Upstream**: ¶12 (수진_theory_R)
- **Downstream**: ¶14 (스캇_empirics_BR)
