# FA: The Funding Anchor (dA/dF < 0)

**¶29-48 | "What" — Funding suppresses Repositioning | Target: Camuffo, Nanda, Ghemawat**

---

## FA.1: Bayesian Gospel (Extending Camuffo-Nanda)

**¶31** Entrepreneurship is experimentation. Camuffo: founders form hypotheses, run experiments, update. Nanda: staged capital enables experiments. Implicit assumption: capital enables experimentation.

**¶32** I test this. If capital enables experimentation, funding should increase repositioning. Prediction: dA/dF > 0.

**¶33** I find the opposite. **Funding suppresses repositioning: dA/dF < 0.** The capital meant to enable experimentation may impede it.

**¶34** **Two-stage mechanism**:
- **Stage 1 (Selection)**: Commitment → Capital. Founders commit precisely to attract funding.
- **Stage 2 (Lock-in)**: Capital → Reinforcement through:
  - (i) psychological—public promises hard to abandon
  - (ii) structural—board seats, milestones, follow-on expectations
  - (iii) social—investors who believed original thesis reinforce original direction

**¶36** The founder who raises $5M wants to experiment. But experiments that might falsify the funded vision threaten investor relationships. Safer path: run experiments that confirm, not challenge.

**¶37** Capital enables experimentation in principle. Commitment—required to obtain capital—impedes experimentation in practice.

---

## FA.2: Empirics (Testing dA/dF < 0)

**¶40** Using 408,697 ventures, I regress A (repositioning) on F (log funding), controlling for industry, cohort, initial breadth B₀.

**¶42** **Core finding: 1-SD increase in funding predicts 0.4 SD lower repositioning** (p < 0.001).

**¶43** Causal identification: funding shocks. When lead VC's fund unexpectedly closes (exogenous capital reduction), affected ventures reposition MORE. Relationship is causal.

**¶44** Mechanism test: dA/dF < 0 is 2× stronger for ventures with (a) single lead investors, (b) milestone-heavy term sheets, (c) high founder-investor belief alignment.

**¶45** Early-stage funding (Seed, Series A) shows stronger dA/dF < 0. Early commitment locks trajectory.

**¶47** **Summary: The Funding Anchor (dA/dF < 0) is confirmed.**

```
dG/dF = (dG/dA > 0) × (dA/dF < 0) < 0
```

Repositioning helps. Funding suppresses repositioning. Therefore funding hurts—through commitment constraining experimentation.

---

## FA.3: Theoretical Extensions

### Real Options Violation
Real Options theory prescribes: **"Delay commitment until uncertainty drops."**
- Nail phase = high uncertainty → should delay commitment
- Funding forces premature commitment → violates Real Options logic
- Result: Ventures skip Nail, enter Scale too early

### Ghemawat Lock-in/Lock-out
Ghemawat (1991): "Lock-in and lock-out are flip sides of the same coin."

| Mechanism | Definition | Motional Example |
|:----------|:-----------|:-----------------|
| **Lock-in** | Sunk investments create stakeholder expectations | $4B → JV partners expect L4 robotaxi |
| **Lock-out** | Commitment forecloses alternatives | L4 choice → trucking path blocked |
| **Lags** | Long lead times lock trajectory | 2027-2030 plans already fixed |
| **Inertia** | Organizational resistance | Hyundai/Aptiv resist pivot |

**Core insight**: Funding triggers premature lock-in, which simultaneously locks out repositioning capacity.

---

## FA Output Interface

```yaml
FA_OUTPUT:
  equation: "dA/dF < 0"
  finding: "1-SD funding → 0.4 SD less repositioning"
  mechanism: "Two-stage: Selection → Lock-in"
  extensions:
    - real_options: "Funding violates 'delay until uncertainty drops'"
    - ghemawat: "Lock-in/Lock-out explains stakeholder constraint"
  target_scholars: ["Camuffo", "Nanda", "Ghemawat", "Real Options"]
```

---

*v5 Update: RF→AF→FA, added Real Options + Ghemawat (Dec 31 Day 3)*
