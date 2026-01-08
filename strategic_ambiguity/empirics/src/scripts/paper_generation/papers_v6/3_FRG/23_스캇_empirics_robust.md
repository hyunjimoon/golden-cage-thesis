# ¶23 스캇_empirics(robust): Robustness Checks

> **Agent**: 스캇 (見 Ground)
> **Row**: Example (E) — Robustness
> **Status**: 📝 Draft

---

## Content

The positive R-G relationship survives multiple robustness checks:

---

## Robustness Panel

| Check | Method | Result |
|:------|:-------|:-------|
| Industry effects | Fixed effects | Robust |
| Alternative R measures | Product category change | Robust |
| Alternative R measures | Customer segment change | Robust |
| Alternative R measures | Technology platform change | Robust |
| Selection effects | Inverse probability weighting | Robust |
| Cohort effects | Year fixed effects | Robust |

---

## Multi-year Panels

Testing across different time windows:

| Period | F-R | R-G | F-G |
|:-------|:---:|:---:|:---:|
| 2021-2022 | − | + | − |
| 2022-2023 | − | + | − |
| 2023-2024 | − | + | − |

Pattern holds consistently: F-R negative, R-G positive, F-G negative.

---

## Limitations

1. **Survivor bias**: Only ventures that survive can reposition
2. **Measurement**: Repositioning relies on text-based breadth scoring
3. **Confound**: Cannot fully rule out founder quality

---

## Dependencies

- **Upstream**: ¶22 (스캇_empirics_RG)
- **Downstream**: ¶24 (스캇_empirics_case_FRG)
