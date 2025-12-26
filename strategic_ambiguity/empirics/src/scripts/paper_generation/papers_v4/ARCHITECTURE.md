---
modified:
  - 2025-12-22T15:36:05-05:00
  - 2025-12-23T10:07:48-05:00
---
# Commit to Movement

## Thesis Architecture (5m × 17sm × 113¶)

*必死卽生, 必生卽死*

---

## Title Structure

| Module | Subtitle | LTE Role | Core Question |
|:------:|:---------|:---------|:--------------|
| **I** | The Funding Paradox | Puzzle | Why dG/dE < 0? |
| **M** | What Moves, Grows | L1: WHAT | Statistical association |
| **T** | When Commitment Traps | L2+L3: HOW/WHY | Trap conditions |
| **E** | Who Moved? | Evidence: WHO | Escape paths |
| **C** | Commit to Move | SO WHAT | Prescription |

---

## North Star

**Growth needs movement. Funding can trap it.**

dG/dE < 0 = (dG/dM > 0) × (dM/dE < 0)

---

## Core Equation

$$\underbrace{\frac{dG}{dE} < 0}_{\text{Funding Paradox}} = \underbrace{\frac{dG}{dM} > 0}_{\text{Movement Principle}} \times \underbrace{\frac{dM}{dE} < 0}_{\text{Funding Traps}}$$

---

## Core Construct

**Parallel Experimentation → Strategic Convergence**

> A dynamic strategic process wherein a venture deliberately initiates multiple concurrent resource-allocation paths (Parallel Experimentation) to resolve market uncertainty, followed by a systematic, evidence-based reduction of scope (Strategic Convergence) that concentrates commitment on the highest-potential trajectory.

| 특성 | 설명 |
|:-----|:-----|
| 병렬 실험 (Parallel Experimentation) | 의도적 초기 너비, 복수 경로 동시 탐색 |
| 학습 scaffold로서의 옵션 | 증거 축적 시 제거되는 것이 정상 |
| 증거 기반 수렴 (Strategic Convergence) | 증거에 따른 범위 축소, 규율된 적응 |
| 몰입 (Commitment) | 최고 잠재력 경로에 집중 |

**비특성 (NOT)**:
- ❌ Reactive pivot (사후 반응적 전환)
- ❌ Pure real options holding (순수 옵션 보유)
- ❌ March (1991) exploration→exploitation (개인 학습 수준)

---

## Notation

| Symbol | Meaning |
|:------:|:--------|
| **G** | Growth (성과/성장) |
| **E** | External funding / capital |
| **M** | Movement (strategic adaptation, pivots, reconfiguration) |
| **V** | Vagueness (rank-normalized, 0-100 percentile) |
| **D** | Direction (V_T - V_0, signed change in vagueness rank) |

---

## Methodology Note: Rank Normalization of V

### Problem
Raw vagueness scores (V) cluster at 80-90 on a 0-100 composite scale:
- 80% of companies have V ∈ [80, 90]
- 60% have V_T = V_0 exactly (zero raw movement)
- Raw differences (ΔV) are uninformative due to clustering

### Solution
**Rank-normalize V before computing M:**

1. Convert V_0 to percentile rank within 2021 cohort → V_0 ∈ [0, 100]
2. Convert V_T to percentile rank within 2025 cohort → V_T ∈ [0, 100]
3. Compute D = V_T - V_0 (change in relative position)
4. Compute M = |D| (magnitude of position change)

### Interpretation
- **M = 10**: Company moved 10 percentile points in vagueness ranking
- **D > 0**: Company became relatively MORE vague (Zoom Out)
- **D < 0**: Company became relatively LESS vague (Zoom In)

### Thresholds (Percentile-Based)
- **M ≥ 5**: Meaningful movement (5+ percentile points)
- **|D| > 10**: Meaningful direction (10+ percentile points)

### Data Preservation
- `V_0`, `V_T`: Rank-normalized values (used for analysis)
- `V_0_raw`, `V_T_raw`: Original composite scores (preserved for reference)

---

## 1. Surface Structure: 5 Modules × 113 Paragraphs (IMTEC)

```
THESIS (113 paragraphs) — 5 MODULES (IMTEC)

├── I  (1–11)     The Funding Paradox             [11]  hook + puzzle (dG/dE < 0)
├── M  (12–48)    What Moves, Grows               [37]  movement principle (dG/dM > 0)
├── T  (49–80)    When Commitment Traps           [32]  High-V & Low-V traps
├── E  (81–104)   Who Moved?                      [24]  escape paths
└── C  (105–113)  Commit to Move                   [9]  prescription + coda
```

---

## 2. Submodule Structure: 17 Submodules

### Count Signature
- **I = 11** (1 submodule)
- **M = 9 + 9 + 1 + 9 + 9 = 37** (5 submodules)
- **T = 8 + 8 + 8 + 8 = 32** (4 submodules)
- **E = 6 + 6 + 6 + 6 = 24** (4 submodules)
- **C = 4 + 4 + 1 = 9** (3 submodules)

### I — Introduction: Funding Paradox (1 submodule)

| Submodule | Range | Count | Focus |
|:---------:|:-----:|:-----:|:------|
| **I1** | 1–11 | 11 | The puzzle: dG/dE < 0 |

### M — Movement Matters (5 submodules)

| Submodule | Range | Count | Focus |
|:---------:|:-----:|:-----:|:------|
| **M1** | 12–20 | 9 | Porter's null & construct (WHAT is movement?) |
| **M2** | 21–29 | 9 | Movement principle evidence (dG/dM > 0) |
| **M3** | 30 | 1 | **BRIDGE EQUATION** (the hinge) |
| **M4** | 31–39 | 9 | Fund→Movement first pass (dM/dE < 0) |
| **M5** | 40–48 | 9 | Strengthen, bound, handoff to T |

### T — Funding Traps (4 submodules)

| Submodule | Range | Count | Focus |
|:---------:|:-----:|:-----:|:------|
| **T1** | 49–56 | 8 | **Coords**: What are traps? Process framing + learning condition |
| **T2** | 57–64 | 8 | **High-V Trap**: Too vague → hard to reject/learn (unfalsifiable hypotheses) |
| **T3** | 65–72 | 8 | **Low-V Trap**: Too specific → hard to pivot (commitment lock-in) |
| **T4** | 73–80 | 8 | **Synthesis**: Both extremes trap; explains dM/dE < 0 |

### E — Escape Routes (4 submodules)

| Submodule | Range | Count | Focus |
|:---------:|:-----:|:-----:|:------|
| **E1** | 81–86 | 6 | **Tempo**: Returns to funding paradox with new understanding |
| **E2** | 87–92 | 6 | **Stayer Examples**: Stuck ventures (high failure case studies) |
| **E3** | 93–98 | 6 | **Mover Examples**: Agile (Sky Engine) vs Forced (Nuro) strategies |
| **E4** | 99–104 | 6 | **Synthesis**: Two paths to escape; Agile vs Forced |

### C — Commit to Movement (3 submodules)

| Submodule | Range | Count | Focus |
|:---------:|:-----:|:-----:|:------|
| **C1** | 105–108 | 4 | Implications for entrepreneurs + investors |
| **C2** | 109–112 | 4 | Limitations + new problems |
| **C3** | 113 | 1 | **Coda**: Commit to Movement (returns to I1, M3) |

---

## 3. Three Archetypes

| Archetype | M | D | Description |
|:----------|:-:|:-:|:------------|
| **Stayer** | ≈0 | 0 | Trapped: no movement, 9.9% survival |
| **Mover (Zoom In)** | >0 | <0 | Escapes high-V trap by focusing, 17.5% survival |
| **Mover (Zoom Out)** | >0 | >0 | Escapes low-V trap by expanding, 18.4% survival |

---

## 4. Key Node Dependency Graph

```
TOP / BOOKENDS
  I1  ↔  C3

GOVERNING NODES
  I1 → (M3, E1, C3)

BRIDGE NODE
  M3 : connects
       (M1–M2 = Movement Principle, dG/dM>0)
   with (M4–M5 + T1–T4 = Funding Traps, dM/dE<0)

TEMPO RETURN
  E1 : returns to funding paradox
       with new understanding after T module

SOLUTION BLOCK
  E2–E4 : escape examples + synthesis
    →  (C1 = implications, C2 = limitations)

CODA
  C3 : final synthesis, returns to I1 + M3
```

---

## 5. Deep Structure: 4-Act Rhythm (20-36-42-15)

```
ACT A = 20  : I1 (11) + M1 (9)
ACT B = 36  : M2 (9) + M3 (1) + M4 (9) + M5 (9) + T1 (8)
ACT C = 42  : T2 (8) + T3 (8) + T4 (8) + E1 (6) + E2 (6) + E3 (6)
ACT D = 15  : E4 (6) + C1 (4) + C2 (4) + C3 (1)
```

| Act | Job |
|:---:|:----|
| A | Set puzzle, define movement |
| B | Declare decomposition (M3), enter traps (T1) |
| C | Expand High-V & Low-V traps (T2–T4), tempo return (E1–E3) |
| D | Synthesis (E4) + implications (C1) + contribution (C2–C3) |

---

## 6. LTE Layers → Modules (Cronin et al. 2025)

| Module | LTE Layer | Cronin Question | Mindset |
|:------:|:---------:|:----------------|:--------|
| **I** | — | — | State anomaly |
| **M** | L1 (WHAT) | What relationships exist? | Link variables to predict outcomes |
| **T** | L2+L3 (HOW/WHY) | How unfold + Why behave? | Specify sequence + generative drivers |
| **E** | Evidence (WHO) | — | Document transformation |
| **C** | SO WHAT | — | Enable intervention |

**Key Distinction**:
- L1: Link variables (M→G, E→M) to predict outcomes
- L2+L3: Specify trap sequence + generative mechanism
- SO WHAT: Enable precise intervention design

---

## 7. Audience Design

| Audience | Module Focus | Prior | Target Posterior |
|:---------|:------------:|:------|:-----------------|
| **Strategy scholars** (Porter, Van den Steen) | M | "movement = noise" | "movement = disciplined capability" |
| **Entrepreneurial finance** (Camuffo, Nanda) | T, E | "capital enables learning" | "capital can create learning traps" |
| **Practitioners** (Founders, VCs) | C | "funding = validation" | "commit to movement, not promises" |

---

## 8. Paragraph Rhythm: 4-5-6-3

Internal structure within submodules:
1. **Intro** (hook)
2. **Theory**
3. **Empirics** (evidence)
4. **Discussion** (synthesis)

---

## 9. Learning Trap Mechanism (T2–T3)

### Why Both Extremes Trap

```
HIGH-V TRAP (Too Vague):
  Low specificity → Hypotheses are unfalsifiable
  Cannot reject what you don't precisely define
  μ(1−μ) stays low because you can't tell what's wrong

LOW-V TRAP (Too Specific):
  High specificity → Commitment lock-in
  Precise promise → Attracts believers (high μ)
  Echo chamber forms → Cannot pivot
```

### Learning Trap Equation

$$\text{Trap Condition: } \mu(1-\mu) < \varepsilon/V$$

Where:
- **μ**: Founder's belief (confidence level)
- **μ(1−μ)**: Belief variance (maximized at μ=0.5)
- **V**: Vagueness of promise (higher = more flexibility)
- **ε**: Learning threshold

**High-V interpretation**: Low specificity makes hypotheses unfalsifiable—you can't learn what to reject.

**Low-V interpretation**: High-confidence founders (μ→1) have low belief variance μ(1−μ)→0, making them vulnerable to commitment lock-in.

### μ-Paradox Table

| Founder μ | μ(1−μ) | Trap Risk | Doubter Need |
|----------:|-------:|:----------|:-------------|
| 0.5 | 0.25 | Low | Optional |
| 0.7 | 0.21 | Medium | Recommended |
| 0.9 | 0.09 | **High** | **Critical** |

---

## 10. Multi-Agent Orchestration System

### Chief Architect + 17 Sub-Agents

The thesis is written by a **Chief Architect** orchestrating 17 specialized sub-agents, each responsible for one submodule.

### Non-Negotiable Constraints

**Lexicon Lock (minimize new nouns):**
- Core variables only: **E (funding), M (movement), G (growth), V (vagueness)**
- Trap nouns: **High-V trap / Low-V trap**
- Archetype nouns: **stayer / mover (zoom in) / mover (zoom out)**
- "Tempo" allowed (E1's key concept)
- NO new branded constructs (describe mechanisms generically)

**Provisional Commitment:**
- **BET**: Scaffold is LOCKED for iteration (no mid-run changes)
- **ACTION**: Generate text using explicit Working Assumptions
- **RECALIBRATION**: Only via Candidate Report after drafting; applied next iteration

### Governance Hierarchy (Dependency Graph)

```
[Level 0: Bookends]
  I1 (Alpha) ←→ C3 (Omega)
  Rule: I1 sets context; C3 synthesizes close

[Level 1: Problem Space Governor]
  M3 (Bridge)
  Input: M1+M2 outputs (dG/dM>0 established)
  Output: Authorizes M4, M5, T1–T4

[Level 2: Tempo Return]
  E1 (Tempo)
  Input: Problem block (I+M+T)
  Output: Returns to funding paradox with new understanding

[Level 3: Solution Space Governor]
  E2–E4 + C1
  Input: E1 tempo + C2 boundary memo
  Output: Examples + implications

[Level 4: Boundary Guard]
  C2 (Limitations)
  Defines limitations + "new problem" agenda
  Must publish before C1 finalizes
```

### Sub-Agent Missions

| Agent | ¶ Range | LTE Role | Mission | Mindset |
|:-----:|:-------:|:--------:|:--------|:--------|
| **I1** | 01–11 | Puzzle | State puzzle (dG/dE<0); define E/M/G; lock vocabulary | State anomaly |
| **M1** | 12–20 | L1 | Define Movement as disciplined capability | Link M→G: what predicts growth? |
| **M2** | 21–29 | L1 | Show dG/dM>0 with evidence | Link M→G: evidence |
| **M3** | 30 | Bridge | "Given dG/dM>0, test dM/dE" → Bridge Memo | Decompose the paradox |
| **M4** | 31–39 | L1 | Propose funding→movement mechanisms | Link E→M: what predicts movement? |
| **M5** | 40–48 | L1 | Operationalize dM/dE; handoff to T | Link E→M: evidence |
| **T1** | 49–56 | L2+L3 | Define traps + learning condition μ(1−μ) < ε/V | Sequence: when traps form |
| **T2** | 57–64 | L2+L3 | **High-V trap**: too vague → hard to reject/learn | Driver: why unfalsifiable |
| **T3** | 65–72 | L2+L3 | **Low-V trap**: too specific → hard to pivot | Driver: why lock-in |
| **T4** | 73–80 | L2+L3 | **Synthesis**: both extremes trap; complete dM/dE < 0 | Generative mechanism |
| **E1** | 81–86 | WHO | **Tempo**: return to funding paradox with new lens | Tempo return to I1 |
| **E2** | 87–92 | WHO | **Stayer examples**: stuck ventures, high failure | Document: who stayed? |
| **E3** | 93–98 | WHO | **Mover examples**: Agile (Sky) vs Forced (Nuro) | Document: who moved? |
| **E4** | 99–104 | WHO | **Synthesis**: two escape paths (Agile vs Forced) | Document: how they escaped |
| **C1** | 105–108 | SO WHAT | Implications for founders + investors | Enable intervention |
| **C2** | 109–112 | SO WHAT | Limitations + boundary conditions + new problem | Boundary conditions |
| **C3** | 113 | SO WHAT | Coda: restate paradox and resolution | Commit to Move |

### Execution Order (Strict)

```
1) I1 → Context Memo (definitions + lexicon lock)
2) M1, M2 → Movement established (dG/dM>0)
3) M3 → Bridge Memo (decomposition + test dM/dE)
4) M4, M5, T1–T4 → Trap Memos (High-V and Low-V)
5) C2 → Boundary Memo (limitations first)
6) E1 → Tempo return (funding paradox with new understanding)
7) E2, E3, E4, C1 → Examples + implications
8) C3 → Final synthesis (coda)
```

### Persona Precision

| Module | Voice | Core Stance | Forbidden |
|:------:|:------|:------------|:----------|
| **M** | Porter + Van den Steen | Movement = disciplined capability | Pivot hype |
| **T** | Camuffo + Nanda | Entrepreneurship = experiments | "Capital is fuel" |
| **E** | Mobility sector lens | Tempo + escape mechanisms | New named frameworks |
| **C** | Integrative contribution | Calibrated claims | Overclaiming |

### ITED Rhythm (4-5-6-3)

Within 18-paragraph blocks:
- **Front half (9¶)**: 4 Intro + 5 Theory
- **Back half (9¶)**: 6 Empirics + 3 Discussion

For 8¶ and 6¶ blocks: compress ITED but preserve order.

### Output Format (Per Agent)

Each agent outputs:
1. Labeled paragraphs: **¶57**, **¶58**, ...
2. **MEMO** section:
   - Working Assumptions (≤3 bullets)
   - Falsification conditions (≤2 bullets)
   - Hand-off tokens (≤5 bullets)

**Hard Stop Rule**: Violation of paragraph counts, lexicon lock, persona, or upstream memo → immediate rewrite.

---

## Composition Rules

1. Each module's **first submodule** serves as **connector** to previous module
2. Each submodule's **last paragraph** must **necessarily connect** to next submodule's question

---

## Provisional Commitment Culture

### The Paradox This Thesis Embodies

This thesis argues for **provisional commitment**—and must be written with it.

### Three Principles

| Principle | Description | Implementation |
|:----------|:------------|:---------------|
| **Dynamic over Static** | Movement is a process, not a category | Use verbs: "What moves" not "The mover" |
| **Association over Causation** | M shows correlation; T explains mechanism | M ≠ proof; T = mechanism |
| **Prescription over Description** | C tells actors what to do | C = "Commit to Move" not "Movers succeeded" |

### Language Guidelines

**Preferred**:
- "What moves, grows" (dynamic)
- "When commitment traps" (conditional)
- "Who moved?" (transformation)
- "Commit to move" (prescription)

**Avoid**:
- "Movers are better" (static category)
- "Movement causes growth" (causal overclaim)
- "The trap" (reified noun)

### Mindset Calibration

| Agent Type | LTE Role | Risk | Correction |
|:-----------|:--------:|:-----|:-----------|
| M-agents | L1 (WHAT) | Overclaim causality | Link variables to predict outcomes |
| T-agents | L2+L3 (HOW/WHY) | Abstract mechanism | Specify sequence + generative drivers |
| E-agents | WHO | Hero worship | Document transformation, not hero |
| C-agents | SO WHAT | Preach | Enable intervention, not sermon |

### The D.934 Spirit

Like Schubert's Fantasie:
- **TEMPO** (E1) returns to opening theme with new understanding
- **CODA** (C3) doesn't repeat—it resolves
- Each module **transforms** the puzzle, not just extends it

---

*Commit to Move.*
