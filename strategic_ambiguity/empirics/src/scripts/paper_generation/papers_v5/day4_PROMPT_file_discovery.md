# Self-Explanatory Prompt: File Discovery for Thesis Optimization

## Task

Search `/Users/hyunjimoon/tolzul` vault and identify files that can improve the thesis according to the evaluation metric below. Sort by relevance and recommend top 10-15 files.

---

## Evaluation Metric

```
Thesis Success = 0.30(Quality) + 0.35(Applicability) + 0.35(Resonance)
```

| Dimension | Weight | Definition | Current Gap |
|:----------|:------:|:-----------|:------------|
| **Quality** | 30% | Looks, thinks, acts like a thesis | Structure needs Johannes-style formatting |
| **Applicability** | 35% | Actionable for AV/Motional | Motional case needs more specifics |
| **Resonance** | 35% | Integrates Scott + Charlie frameworks | Partial commitment operationalization |

---

## Current Thesis State

### Core Argument
- **Puzzle**: dG/dF < 0 (more funding → less growth)
- **Mechanism**: HHI > θ creates commitment trap
- **Solution**: Partial commitment via "Test Two, Choose One" operationalized through modular operations

### Theoretical Backbone
- Ghemawat (1991): 3 conditions for flexibility, 4 lock-in mechanisms
- Gans et al. (2021): Tesla vs Better Place pattern, "Test Two, Choose One"
- Fine (2022): 10 Tools for operations
- Van den Steen (2017): Commitment theory

### Empirical Cases
- **Primary**: Motional (AV startup, $4B, stuck in L4)
- **Validation**: Ford/GM $19B EV write-off
- **Comparison**: Tesla, Better Place, Waymo, Cruise, Aurora

### Deliverables Created
- `thesis_draft_A_executive_summary.docx` (9 pages)
- `thesis_draft_B_executive_summary.docx` (9 pages)
- `3questions_to_advisors.docx`
- `email_body.docx`

---

## Files to Search For

### Priority 1: Advisor Resonance (35%)

| Need | Search Keywords | File Types |
|:-----|:---------------|:-----------|
| Scott Stern's frameworks | `stern`, `test two`, `entrepreneurial strategy`, `bayesian` | .md, .pdf |
| Charlie Fine's frameworks | `fine`, `10 tools`, `clockspeed`, `operations`, `NSS` | .md, .pdf |
| Jinhua Zhao's frameworks | `zhao`, `mobility`, `transportation` | .md, .pdf |
| Integration examples | `scott-charlie`, `strategy-operations` | .md |

### Priority 2: Applicability (35%)

| Need | Search Keywords | File Types |
|:-----|:---------------|:-----------|
| Motional specifics | `motional`, `aptiv`, `hyundai`, `nutonomy`, `robotaxi` | .md, .pdf, .docx |
| AV industry data | `autonomous vehicle`, `AV`, `L4`, `waymo`, `cruise` | .md, .pdf |
| Ford/GM EV case | `ford`, `GM`, `EV`, `electric vehicle`, `write-off` | .md, .pdf |
| Mobility ventures | `mobility`, `transportation startup` | .md |

### Priority 3: Quality (30%)

| Need | Search Keywords | File Types |
|:-----|:---------------|:-----------|
| Thesis structure examples | `thesis`, `dissertation`, `johannes` | .md, .pdf |
| Academic writing | `CARE`, `writing`, `syntax` | .md |
| LTE framework | `LTE`, `layer`, `theory`, `evidence` | .md, .pdf |
| Ghemawat/Gans papers | `ghemawat`, `commitment`, `gans`, `better place` | .md, .pdf |

---

## Search Locations (Priority Order)

### Tier 0: Critical Network Hub Files (읽기 필수 - 네트워크 중심 노드)

These files are high-connectivity nodes that link multiple thesis components:

| File | Role | Key Content | Metric |
|:-----|:-----|:------------|:-------|
| `🗄️🧠scott.md` | Scott mental model | 4 Axioms, Test Two Choose One, Bayesian Entrepreneurship, Low/High bar testing | Resonance |
| `🗄️🧠charlie.md` | Charlie mental model | 10 Tools, Clockspeed, Nail-Scale-Sail, Process Architecture, SW vs HW startups | Resonance |
| `🗄️🧠jinhua.md` | Jinhua mental model | Mobility venture survival, M3S, regulatory barriers | Applicability |
| `M3_🥚Evol ops growth/` | Evolution framework | Adaptation patterns, clockspeed dynamics, strategy evolution | Quality |

**Full Paths:**
```
/Users/hyunjimoon/tolzul/Front/Simmering/베이즈창업/spandrel/ops4entrep/📐method/recycled_analysis/evaluators/🗄️🧠scott.md
/Users/hyunjimoon/tolzul/Balance/🎵 Weekly_Melody/3_승수전문_찰리/🗄️🧠charlie.md
/Users/hyunjimoon/tolzul/Front/Simmering/베이즈창업/spandrel/ops4entrep/📐method/recycled_analysis/evaluators/🗄️🧠jinhua.md
/Users/hyunjimoon/tolzul/Front/Simmering/베이즈창업/spandrel/ops4entrep/📐method/recycled_analysis/🗄️3_practical_imp/M3_🥚Evol ops growth/
```

### Tier 1: Thesis Core
1. `/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/` — thesis work

### Tier 2: Supporting Content
2. `/Users/hyunjimoon/tolzul/Space/Library/1논문용/` — paper notes (📜 prefix files)
3. `/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/Tool4Ops4Entrep/` — NSS/operations content
4. `/Users/hyunjimoon/tolzul/Balance/🎵 Weekly_Melody/` — advisor-related notes
5. `/Users/hyunjimoon/tolzul/.claude/` — prompts and skills

---

## Key Conceptual Patterns to Extract

### From 🗄️🧠scott.md:
- Table 6-7: "Test Two, Choose One" examples and rationale
- Low bar (lenient) vs High bar (strict) testing distinction
- Entrepreneurial Strategy Compass (IP/Disruptor/Value Chain/Architectural)
- 4 Axioms: Freedom, Constraint, Uncertainty, Noisy Learning

### From 🗄️🧠charlie.md:
- Nail-Scale-Sail stage model
- 10 Tools: Processify, Professionalize, Segment, Evaluate, Automate, Platformize, Replicate, Collaborate, Acculturate, Capitalize
- Clockspeed amplification (product vs process innovation)
- SW vs HW startup comparison (experiment cost c, pivot cost k)
- "Premature automation" warning

### From 🗄️🧠jinhua.md:
- Mobility venture low survival causes:
  - Regulatory & Compliance Barriers
  - High Capital Requirements
  - Slow Adoption Cycles
  - Technology & Reality Gap
  - Operational Complexity
  - Large Incumbents

### Integration Pattern: Perceive-to-Act vs Act-to-Perceive
```
Scott (🧭 Perceive to Act): Form beliefs → Test → Choose
Charlie (🧬 Act to Perceive): Commit → Learn → Adapt
Thesis Resolution: Partial Commitment bridges both directions
```

---

## Output Format

Return a sorted table:

| Rank | File Path | Relevance to Metric | Specific Use | Priority |
|:----:|:----------|:--------------------|:-------------|:--------:|
| 1 | `/path/to/file.md` | Resonance: Scott framework | Add to Section 5.2 | High |
| 2 | ... | ... | ... | ... |

**For each recommended file, explain:**
1. Which metric dimension it serves (Quality/Applicability/Resonance)
2. Which thesis section it improves
3. What specific content to extract

---

## Exclusion Criteria

- Skip files already incorporated (listed in "Deliverables Created")
- Skip personal notes unrelated to thesis
- Skip duplicate versions (prefer most recent)
- Skip files > 50MB (likely data/images)

---

## Example Good Finds

| File Type | Why Valuable |
|:----------|:-------------|
| `📜Ghemawat91_Commitment.md` | Direct theoretical backbone |
| `motional_meeting_notes.md` | Primary case specifics |
| `NSS_10tools_sequencing.md` | Charlie's framework application |
| `stern_test_two_lecture.pdf` | Scott's framework details |

---

## Execute

1. Use `Glob` to find candidate files by pattern
2. Use `Grep` to search content for keywords
3. Use `Read` to verify relevance
4. Sort by evaluation metric contribution
5. Return top 10-15 with explanations

Start searching.
