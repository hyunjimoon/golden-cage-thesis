# CHANGELOG v4.0.0 (2025-12-28)

> **Source**: thesis_v3_to_v4_summary.txt (User voice memo)
> **Type**: MAJOR (Structural reorganization)

---

## Summary: Module Restructuring

### v3 → v4 Module Changes

```
v3:  I ─ M(1,2,3,4,5) ─ T(1,2,3,4) ─ E(1,2,3,4) ─ C(1,2,3)
            │               │            │
            ▼               ▼            ▼
v4:  I ─ M(MG,MF) ───── V(VM,VD) ── E(Motional) ─ C
        dG/dM dM/dF    dM/dV dD/dV   Prescription
```

### Key Changes

| Aspect | v3 | v4 |
|--------|-----|-----|
| T module | T (Trap) | **V (Vagueness)** |
| M subagents | M1-M5 (5개) | **MG, MF** (2개) |
| V subagents | T1-T4 (4개) | **VM, VD** (2개) |
| E focus | Cases (E1-E4) | **Motional 처방** |
| Variables | E, M, G | **F, M, G, V, D** (5개) |

---

## New Variable System

| Variable | Definition | Measurement |
|:--------:|:-----------|:------------|
| **F** | Funding | External capital raised |
| **M** | Movement | \|ΔV\| (absolute vagueness change) |
| **G** | Growth | Later Stage VC (C/D+) |
| **V** | Vagueness | Strategic position breadth |
| **D** | Direction | Sign of ΔV (zoom-in vs zoom-out) |

---

## New Module Structure

### I — Introduction (Funding Paradox)
- Introduces 5 variables: F, M, G, V, D
- Core equation: dG/dF = (dG/dM)(dM/dF) < 0

### M — Movement ("What" happens)

| Subagent | Focus | Equation | Target Scholars |
|:--------:|:------|:---------|:----------------|
| **MG** | Movement Principle | dG/dM > 0 | Porter, Ghemawat, Van den Steen |
| **MF** | Golden Cage | dM/dF < 0 | Camuffo, Nanda |

**Content Mapping**:
- MG ← M1 (Strategy Gospel) + M2 (Empirics: dG/dM)
- MF ← M4 (Bayesian Gospel) + M5 (Empirics: dM/dF)
- M3 (Bridge) → Integrated into I or removed

### V — Vagueness ("Why" traps form)

| Subagent | Focus | Equation | Target Scholars |
|:--------:|:------|:---------|:----------------|
| **VM** | Vagueness → Movement | dM/dV | Stern (precision → testing) |
| **VD** | Vagueness → Direction | dD/dV | Zoom-in/out analysis |

**Content Mapping**:
- VM ← T1 (Coords) + T2 (High-V Trap) + T3 (Low-V Trap)
- VD ← T4 (Synthesis) + direction analysis

### E — Escape ("How" to escape)

**Focus**: Motional Case Study + 3 Prescriptions

| Prescription | Description |
|:-------------|:------------|
| **Platformize** | Expand beyond OEM (HMG) to manufacturers, network players |
| **Acculturate** | Dynamic coordination protocol, provisional commitment |
| **Evaluate** | Dashboard for common knowledge, coordinated action |

**Content Mapping**:
- Motional situation (Low-V, High-F, Low-M state)
- Aurora Model as contrast/template
- E1-E4 content consolidated

### C — Commit (Conclusion)
- Summary of contributions
- Boundary conditions
- Future research

---

## File Structure Changes

### Before (v3):
```
1_I_introduction/I1.md
2_M_movement_matters/M1.md, M2.md, M3.md, M4.md, M5.md
3_T_funding_traps/T1.md, T2.md, T3.md, T4.md
4_E_escape/E1.md, E2.md, E3.md, E4.md
5_C_commit/C1.md, C2.md, C3.md
```

### After (v4):
```
1_I_introduction/I1.md
2_M_movement/MG.md, MF.md
3_V_vagueness/VM.md, VD.md
4_E_escape/E_motional.md
5_C_commit/C1.md
```

---

## Paper ↔ Module Mapping (NEW)

| Paper | v3 | v4 | 🧙‍♂️ Syntax Master |
|:------|:---|:---|:------------------|
| Paper A | M1, M2 | **MG** | M_Empirics_zgk25.pdf |
| Paper B | M4, M5 | **MF** | M_Empirics_zgk25.pdf |
| Paper C | T1-T4 | **VM, VD** | T_Theory_GKSS21.pdf |
| Paper D | E1-E4 | **E_motional** | E_Solution_Motional.pdf |

---

## Migration Plan

1. ✅ Create CHANGELOG_v4.0.0
2. ⏳ Rename 3_T_funding_traps → 3_V_vagueness
3. ⏳ Create MG.md, MF.md from M1-M5
4. ⏳ Create VM.md, VD.md from T1-T4
5. ⏳ Consolidate E1-E4 → E_motional.md
6. ⏳ Update dashboard structure
7. ⏳ Update obi-wan.md with new mapping
8. ⏳ Apply Gemini's syntax master recommendations

---

## Version Rule

```
vMAJOR.MINOR.PATCH_YYMMDD

v4.0.0_251228:
- MAJOR=4: 모듈 구조 대폭 변경 (T→V, subagent 통합)
- MINOR=0: 새 버전 시작
- PATCH=0: 초기
- DATE=251228: 오늘
```

---

*必死卽生, 必生卽死*
*Commit to ADAPTATION, direction first and speed second.*
