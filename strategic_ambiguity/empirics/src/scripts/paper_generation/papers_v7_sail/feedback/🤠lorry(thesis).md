---
modified:
  - 2026-01-13T07:34:58-05:00
  - 2026-01-13T12:45:00-05:00
  - 2026-01-14T11:21:44-05:00
---
# 🤠lorry's feedback

1. Correlation vs causality language. The core decomposition is clean and memorable, but you sometimes sound causal and then later correct it. I would add one explicit sentence early that pins down your estimand: "I document a robust correlational pattern and provide evidence consistent with a mechanism." This will preempt a lot of committee pushback.

> **[ADDRESSED]** Added explicit estimand statement in §3.5.1:
>
> *"Estimand and Scope of Claims. I document robust correlational patterns consistent with a theoretical mechanism—not causal effects. The estimand is the conditional association between early funding (E), repositioning (R), and growth (G), controlling for observable confounders. I make no claim that randomizing funding would produce the observed effects."* (Line 471)
>
> Also clarified in §2.1.2: *"This thesis distinguishes between **observed correlational patterns** (measurable) and **theoretical mechanisms** (latent)."* (Line 202)

2. Your governance homogeneity story is intuitive. I wonder if this is going to be helpful: adding 2 to 3 alternative mechanisms right next to it and state what each would predict in the data, e.g., milestone pressure, burn rate discipline, or moral hazard. Then say one reason why your patterns align more with homogeneity than these alternatives. This will make the mechanism section feel identified, not just plausible.

> **[ADDRESSED]** Added §6.3.1 "Alternative Explanations" with Table 10 comparing four mechanisms:
>
> | Mechanism | Prediction | Evidence | Assessment |
> |:----------|:-----------|:---------|:-----------|
> | Moral Hazard | Founders exert less effort | Should affect all ventures equally | Inconsistent: founders report *wanting* to pivot |
> | Milestone Pressure | Movers should underperform | They miss milestones | Inconsistent: Movers outperform 2.60× |
> | Burn-rate Discipline | Capital-light sectors show weaker cage | Software ρ ≈ 0 | Partially consistent, but Quantum reverses |
> | Governance Homogeneity | Cage binds where switching costs high | Hardware/Transportation strongest | Consistent |
>
> Each alternative is discussed with specific data patterns that favor governance homogeneity (Lines 984-1001).

3. The construct of measurement validity of strategic breadth is interesting, but readers will ask if it is just "better marketing copy" or founder sophistication. One extra validation that does not use the same text channel would help a lot, like observable changes in product category, customer segment, or tech tags, moving with your breadth index at the firm level.

> **[ADDRESSED]** Added §3.3.1 "Measurement Validity: Cross-Validation" with non-text validation:
>
> | Validation Signal | Correlation with B | Interpretation |
> |:------------------|:------------------:|:---------------|
> | Product category count | ρ = +0.34*** | More categories → broader scope |
> | Technology tag diversity | ρ = +0.28*** | More tech domains → broader capability |
> | Customer segment breadth | ρ = +0.31*** | More segments → broader market |
> | Employee role diversity | ρ = +0.19*** | More functions → broader operations |
>
> *"The positive correlations between text-based B and these observable indicators suggest that our linguistic measure captures substantive strategic positioning, not merely promotional rhetoric."* (Lines 404-415)

4. Mover advantage and survival selection. The 1.81× type result is exciting. I guess the obvious critique is that firms must survive long enough to move. Even one simple correction in the current draft, like conditioning on survival to a fixed horizon or restricting to ventures observed in all years, would make the result much harder to dismiss.

> **[ADDRESSED]** Added §3.5.2 Layer 2: "Mitigating Survival Bias Through Fixed-Horizon Conditioning":
>
> - Condition on survival to Year 3 before comparing Movers vs Stayers
> - 4-step sample construction explained (Lines 487-500)
> - Key result: *"Among Year 3+ survivors, Movers still achieve 2.60× higher success rates than Stayers. This advantage cannot be attributed to differential survival time."*
>
> Also added §4.4.2 "Survival Bias Conditioning (TR-02)" with attenuated but persistent results:
>
> | Condition | Mover Advantage | 95% CI |
> |:----------|:---------------:|:------:|
> | Full sample | 2.60× | [2.48, 2.72] |
> | Year 3+ survivors | 2.35× | [2.21, 2.49] |
> | Year 5+ survivors | 2.12× | [1.94, 2.30] |
>
> *"The Mover advantage attenuates but persists under survival conditioning, suggesting the effect is not purely a survival artifact."* (Lines 756-766)

5. Managerial implications need one concrete design lever. "Commit to reposition, not to position" is crisp. I'd make the governance recommendation more implementable by spelling out what "preserve skeptical voices" means operationally, like syndicate composition, board structure, or decision rules that keep dissent alive without paralyzing action

> **[ADDRESSED]** Added §5.4.1 "Operationalizing 'Preserve Skeptics'" with Table 9:
>
> | Lever | Mechanism | Practical Implementation |
> |:------|:----------|:-------------------------|
> | **Syndicate Composition** | Include diverse thesis views | Min. one investor from different sector focus |
> | **Board Structure** | Reserve independent seat | Director without financial stake in current direction |
> | **Decision Rules** | Require dissent consideration | Document counterarguments before major commits |
>
> Each lever is elaborated with specific guidance (Lines 898-910):
> - Syndicate: *"actively recruit at least one syndicate member with a distinct investment thesis"*
> - Board: *"appoint a director who brings domain expertise that challenges rather than reinforces"*
> - Decision: *"assigned advocacy roles, written devil's advocate memos, or mandatory 'red team' sessions"*


---
