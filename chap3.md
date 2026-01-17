::: {#ch:data}
# Data and Identification {#ch:data}
:::

::: {#introduction}
## Introduction {#sec:ch3-introduction}
:::

Chapter [\[ch:theory\]](#ch:theory){reference-type="ref"
reference="ch:theory"} argued that funding creates a golden cage by
homogenizing governance beliefs. This chapter describes how I test that
theory. The core challenge is measuring flexibility--a latent capability
that cannot be directly observed. My solution is to measure its
behavioral manifestation: repositioning, the observable shift in a
venture's strategic positioning over time. Ventures that reposition
reveal they had flexibility; ventures that hold position may lack it.

I analyze 168,011 U.S. ventures from PitchBook (2021--2025). To measure
repositioning, I use dictionary-based text analysis of company
descriptions, computing how much each venture's strategic breadth
changed between funding rounds. The method draws on established research
in category spanning [@zuckerman1999the] and linguistic concreteness
[@pan2018corporate].

A key identification concern is selection: high-conviction founders may
both raise more capital and resist pivoting, producing correlation
without causation. I address this in
Section [1.5](#identification-strategy){reference-type="ref"
reference="identification-strategy"}, arguing that selection is part of
the mechanism (not a confound) and conditioning on observable
characteristics.

## Data Sources and Sample Construction

I construct a panel of 168,011 ventures from PitchBook, covering the
period 2021--2025. PitchBook provides comprehensive coverage of U.S.
venture-backed companies, including funding rounds, company
descriptions, and outcome data.

**Sample Construction.** The initial universe contains 488,381 ventures.
I filter to U.S.-headquartered ventures at early stage (Seed through
Series B) with at least 24 months of observable history and complete
data on core variables, yielding 168,011 ventures (34.4% retention).

## Variable Operationalization

::: {#tab:variables}
+--------------+-------------------+--------------+------------------------+
| ::: minipage | ::: minipage      | ::: minipage | ::: minipage           |
| Symbol       | Variable          | Type         | Operationalization     |
| :::          | :::               | :::          | :::                    |
+:=============+:==================+:=============+:=======================+
| ::: minipage | ::: minipage      | ::: minipage | ::: minipage           |
| Symbol       | Variable          | Type         | Operationalization     |
| :::          | :::               | :::          | :::                    |
+--------------+-------------------+--------------+------------------------+
| **C**        | Commitment        | Choice       | Initial strategic      |
|              |                   |              | specificity index      |
|              |                   |              | (0--100): product      |
|              |                   |              | category count,        |
|              |                   |              | milestone granularity, |
|              |                   |              | funding structure      |
+--------------+-------------------+--------------+------------------------+
| **E**        | Early Funding     | Outcome      | Early-stage capital    |
|              |                   |              | secured                |
|              |                   |              | (first_financing_size, |
|              |                   |              | M USD,                 |
|              |                   |              | log-transformed)       |
+--------------+-------------------+--------------+------------------------+
| **F**        | Flexibility       | Capacity     | Governance-permitted   |
|              |                   |              | change capacity        |
|              |                   |              | (inferred from R)      |
+--------------+-------------------+--------------+------------------------+
| **B**        | Strategic Breadth | State        | Market positioning     |
|              |                   |              | specificity (0--100    |
|              |                   |              | scale via              |
|              |                   |              | dictionary-based       |
|              |                   |              | vagueness)             |
+--------------+-------------------+--------------+------------------------+
| **R**        | Repositioning     | Action       | $|B_T - B_0|$,         |
|              |                   |              | magnitude of strategic |
|              |                   |              | change                 |
+--------------+-------------------+--------------+------------------------+
| **G**        | Growth            | Outcome      | Binary: $G = 1$ if     |
|              |                   |              | reached Later Stage VC |
|              |                   |              | (Series C+); base rate |
|              |                   |              | 11.5%                  |
+--------------+-------------------+--------------+------------------------+

: Variable Definitions and Causal Structure
:::

**From latent flexibility to observable repositioning.** The theory
chapter treats strategic flexibility ($F$) as a *latent* capability: the
ability to keep multiple viable paths live under uncertainty. Because
$F$ is unobserved in administrative venture data, I proxy it with
**repositioning** ($R$), the observable behavioral manifestation of
latent flexibility. Ventures that reposition reveal that they retained
(and were permitted by governance to exercise) flexibility; ventures
that remain static may lack the capability or may be structurally caged.
This proxy motivates the empirical focus on $E \rightarrow R$ and
$R \rightarrow G$ in
Chapter [\[ch:results\]](#ch:results){reference-type="ref"
reference="ch:results"}.

**Limitations of this proxy approach.** Three caveats apply. First,
repositioning captures *revealed* flexibility, not *latent*
flexibility---a venture that could pivot but chose not to appears
identical to one that was structurally caged. Second, text-based
measures of strategic breadth may miss repositioning that occurs within
a fixed description (e.g., a "platform" company pivoting between
applications). Third, the measure cannot distinguish *voluntary*
repositioning (strategic adaptation) from *forced* repositioning
(responding to failure). These limitations are addressed further in
Chapter [\[ch:conclusion\]](#ch:conclusion){reference-type="ref"
reference="ch:conclusion"},
Section [\[limitations\]](#limitations){reference-type="ref"
reference="limitations"}.

::: {#strategic-breadth-b}
### Strategic Breadth (B)
:::

I operationalize **Strategic Breadth (B)** using dictionary-based text
analysis of company descriptions. Drawing on category spanning research
[@zuckerman1999the; @pontikes2012two] and linguistic concreteness
research [@pan2018corporate], I construct a continuous measure (0--100)
that captures the degree of vagueness in a venture's positioning.

The measure combines two components. The first is *Categorical
Vagueness*: how much a description uses broad, umbrella terms
("platform," "ecosystem," "solution") rather than specific market
categories ("mobile payments," "enterprise SaaS"). A company describing
itself as a "technology platform" spans many categories; one describing
itself as "inventory management software for small retailers" does not.
The second component is *Concreteness Deficit*: whether the description
lacks specific binding markers such as quantitative targets ("10,000
users") or narrow technical specifications ("HIPAA-compliant cloud
storage").

The resulting score ranges from 0 to 100. A score of 0 means maximally
specific positioning--the company has committed to a narrow path. A
score of 100 means maximally vague positioning--the company retains many
possible directions. The sample mean is B = 45.2 (SD = 12.6). Full
construction details appear in
Appendix [\[app:a\]](#app:a){reference-type="ref" reference="app:a"};
the bimodal distribution of $B$ is visualized in
Appendix [\[app:c\]](#app:c){reference-type="ref" reference="app:c"},
Figure [\[fig:bimodal\]](#fig:bimodal){reference-type="ref"
reference="fig:bimodal"}.

**Illustrative Examples.**
Table [1.2](#tab:breadth-examples){reference-type="ref"
reference="tab:breadth-examples"} demonstrates how the breadth measure
(B) captures strategic positioning using examples from the autonomous
vehicle (AV) industry--a capital-intensive sector where the golden cage
mechanism binds tightly. Movers repositioned substantially between
2021--2025; Stayers maintained consistent positioning.

::: {#tab:breadth-examples}
+-------------+---------------+---------------+------------+---------------+
| **Company** | **2021        | **2025        | $\Delta B$ | **Growth      |
|             | Description** | Description** |            | Mult.**       |
+:============+:==============+:==============+:==========:+:=============:+
| *Panel A: Movers (Zoom-Out)*                                             |
+-------------+---------------+---------------+------------+---------------+
| **Aurora**  | "Developer of | "Autonomous   | +38.2      |               |
|             | autonomous    | driving       |            |               |
|             | trucks for    | platform      |            |               |
|             | freight       | powering      |            |               |
|             | logistics"    | trucking,     |            |               |
|             |               | ride-hailing, |            |               |
|             |               | and delivery" |            |               |
+-------------+---------------+---------------+------------+---------------+
|             | (Specific:    | (Broad:       |            |               |
|             | trucking      | multi-modal   |            |               |
|             | focus)        | platform)     |            |               |
+-------------+---------------+---------------+------------+---------------+
|             | $B_0 = 42.1$  | $B_T = 80.3$  |            | $3.2\times$   |
|             | (precise)     | (vague)       |            |               |
+-------------+---------------+---------------+------------+---------------+
| *Panel B: Movers (Zoom-In)*                                              |
+-------------+---------------+---------------+------------+---------------+
| **Cruise**  | "Developer of | "Provider of  | $-35.6$    |               |
|             | self-driving  | personal      |            |               |
|             | vehicles for  | autonomous    |            |               |
|             | urban         | vehicle       |            |               |
|             | mobility"     | technology    |            |               |
|             |               | for OEMs"     |            |               |
+-------------+---------------+---------------+------------+---------------+
|             | (Broad: urban | (Specific:    |            |               |
|             | mobility)     | OEM           |            |               |
|             |               | licensing)    |            |               |
+-------------+---------------+---------------+------------+---------------+
|             | $B_0 = 76.4$  | $B_T = 40.8$  |            | $2.9\times$   |
|             | (vague)       | (precise)     |            |               |
+-------------+---------------+---------------+------------+---------------+
| *Panel C: Stayers*                                                       |
+-------------+---------------+---------------+------------+---------------+
| **Argo AI** | "Developer of | "Developer of | 0.0        |               |
|             | Level 4       | Level 4       |            |               |
|             | autonomous    | autonomous    |            |               |
|             | driving       | driving       |            |               |
|             | technology    | technology    |            |               |
|             | for           | for           |            |               |
|             | robotaxis"    | robotaxis"    |            |               |
+-------------+---------------+---------------+------------+---------------+
|             | (Unchanged    |               |            |               |
|             | positioning   |               |            |               |
|             | despite       |               |            |               |
|             | market        |               |            |               |
|             | signals)      |               |            |               |
+-------------+---------------+---------------+------------+---------------+
|             | $B_0 = 58.2$  | $B_T = 58.2$  |            | $1.0\times$\* |
+-------------+---------------+---------------+------------+---------------+

: Breadth Measure: Illustrative Examples from AV Industry
:::

*Notes: B = vagueness score (0--100 scale); $\Delta B = B_T - B_0$;
Growth Multiple $= F_t/E$ (total subsequent funding / early funding).
\*Argo AI shut down in October 2022; growth multiple reflects capital
consumed before shutdown. Breadth scores are illustrative, computed by
applying the breadth algorithm to publicly available company
descriptions; these specific companies may not appear in the filtered
PitchBook sample ($N = 168{,}011$).*

**Why AV?** The autonomous vehicle industry provides a natural
laboratory for the golden cage mechanism because it combines three
conditions that amplify the cage: (1) high capital intensity--\$100M+
funding rounds create strong sunk costs, (2) regulatory
uncertainty--policy landscapes shift unpredictably across jurisdictions,
and (3) technology path uncertainty--viable architectures compete (lidar
vs. camera-only, robotaxi vs. personal AV, trucking vs. passenger).
These conditions create strong investor sorting: VCs who fund AV
ventures hold firm beliefs about which approach will win.

**Aurora (Zoom-Out, $3.2\times$):** Aurora began in 2021 as a
trucking-focused company: "autonomous trucks for freight logistics." By
2025, Aurora had broadened to a multi-modal "Aurora Driver" platform
powering trucking, ride-hailing, and delivery. This repositioning--from
specific application to general platform--attracted new partners
(PACCAR, Volvo, Uber Freight) and enabled \$820M+ in additional funding.
The zoom-out preserved optionality: if trucking unit economics proved
unfavorable, the platform could pivot to other applications without
abandoning the core technical asset.

**Cruise (Zoom-In, $2.9\times$):** Cruise took the opposite path. In
2021, Cruise positioned broadly as an "urban mobility" company operating
robotaxis in San Francisco. By 2025, GM's "Cruise 2.0" strategy narrowed
focus: exiting the robotaxi business to license autonomous technology to
OEMs for personal vehicles. This zoom-in responded to market signals
that robotaxi unit economics were challenging. The repositioning freed
Cruise from fleet operations costs while monetizing its core technical
capability through licensing.

**Argo AI (Stayer, $1.0\times$):** Argo AI maintained identical
positioning from 2021 through its October 2022 shutdown: "Level 4
autonomous driving technology for robotaxis." Despite \$3.6B in funding
from Ford and Volkswagen, Argo failed to attract new investors when both
backers reduced commitment. The company's inability to reposition
illustrates the cage mechanism: Ford and VW, as thesis-driven investors,
had funded a specific technical approach (robotaxis). When that approach
encountered headwinds, Argo's board--populated solely by believers in
robotaxis--lacked advocates for alternatives like trucking or OEM
licensing. The cage was structural, not motivational.

**The Key Pattern:** Both Movers achieved
$\sim$3$\times$ growth multiples; the Stayer achieved
$1.0\times$ (capital consumed without subsequent growth). The
*direction* of repositioning differed--Aurora zoomed out, Cruise zoomed
in--but *movement itself* distinguished survivors from the caged. This
pattern motivates the binary Mover/Stayer classification used throughout
the empirical analysis.

::: {#repositioning-r}
### Repositioning (R)
:::

**Repositioning (R).** Following @kirtley2023pivot's definition of
strategic change in entrepreneurial firms, repositioning magnitude
measures the absolute change in strategic breadth: $R_i = |B_T - B_0|$,
where $B_0$ is breadth at baseline (2021) and $B_T$ at endpoint (2025).
Importantly, most ventures do not reposition at all: 61.2% show R = 0
(I call these "Stayers"), while only 38.8% show R \> 0 ("Movers"). This pattern (most
ventures holding position) is consistent with the golden cage theory:
governance constraints make repositioning difficult.

**Growth (G) and Growth Multiple.**

I use two outcome measures. **Growth (G)** is a binary indicator:
$G = 1$ if the venture reached Later Stage VC (Series C or beyond) by
the end of the observation window, $G = 0$ otherwise. The base growth
rate is 11.0%. The **Mover Advantage** (2.60$\times$) compares growth
rates: $P(G=1|\text{Mover}) / P(G=1|\text{Stayer})$ = 17.6% / 6.7%.
Separately, the **Growth Multiple** $= F_t/E$ measures continuous
funding scale for illustrative cases. *Robustness checks using
alternative threshold definitions are provided in Appendix C.*

## Descriptive Statistics

::: {#tab:descriptive}
  Variable                              Mean      SD   Min   Median   Max
  ----------------------------------- ------ ------- ----- -------- -----
  Variable                              Mean      SD   Min   Median   Max
  Early Funding (E, M USD)              40.2   376.7   0.0      1.0   ---
  Strategic Breadth ($B_0$)             45.2    12.6     0     44.7   100
  Repositioning (R = $|B_T - B_0|$)      4.0     7.8     0     0.06    62
  Growth (G, binary)                    0.11    0.31     0        0     1

  : Descriptive Statistics ($N = 168{,}011$)
:::

<figure id="fig:distributions-E-B0" data-latex-placement="htbp">
<img src="img/Ch3_Fig1_distributions_E_B0.png" style="width:90.0%" />
<figcaption>Distributions of Early Funding (<span
class="math inline"><em>E</em></span>) and Baseline Strategic Breadth
(<span class="math inline"><em>B</em><sub>0</sub></span>). Early funding
is right-skewed with median $1.5M; strategic breadth shows bimodal
distribution concentrated at high values.</figcaption>
</figure>

<figure id="fig:distributions-R-G" data-latex-placement="htbp">
<img src="img/Ch3_Fig2_distributions_R_G.png" style="width:90.0%" />
<figcaption>Distributions of Repositioning (<span
class="math inline"><em>R</em></span>) and Growth (<span
class="math inline"><em>G</em></span>). 61.2% of ventures show no
repositioning (Stayers); 11.0% reach Later Stage VC (Growth =
1).</figcaption>
</figure>

The sample divides into Stayers (102,742 ventures, 61.2%) who show no
strategic movement, and Movers (65,269 ventures, 38.8%) who shifted
their strategic breadth by a measurable amount. Overall, 11.0% of
ventures reach Later Stage VC by the end of the observation window, with
average strategic breadth at baseline of B = 45.2 (SD = 12.6).

## Identification Strategy

The central challenge is distinguishing selection from treatment
effects. High-conviction founders may both raise more capital and resist
pivoting--not because funding caused rigidity, but because conviction
drove both outcomes. This concern is valid, and I do not claim causal
identification.

However, I argue that selection is part of the mechanism, not a confound
to be eliminated. The golden cage theory predicts that funding and
rigidity correlate *because* committed founders attract committed
investors through sorting. The selection concern is precisely what the
theory describes. The question is not whether selection exists--it
does--but whether the pattern is consistent with the theoretical
mechanism.

I address identification in three ways. First, I conduct bounds analysis
for survival bias: the sample requires $B_T$ (2025 breadth) to compute
repositioning, which conditions on survival. If excluded firms died
because they were caged and couldn't reposition, they are "extreme
Stayers" ($R=0$) with $G=0$. Assigning $R=0$ to all excluded firms
yields $\rho(E,R) = -0.131$ (vs. $-0.133$ baseline)---the correlation is
stable (see Appendix [\[app:c\]](#app:c){reference-type="ref"
reference="app:c"},
Table [\[tab:attenuation\]](#tab:attenuation){reference-type="ref"
reference="tab:attenuation"}). Furthermore, only 3% of excluded firms
are "Out of Business"; 70% are "Generating Revenue," indicating data
coverage rather than survival bias. Second, the Mover advantage persists
under survival conditioning: 2.60$\times$ (full sample), 2.35$\times$
(Year 3+ survivors), 2.12$\times$ (Year 5+ survivors). Attenuation is
expected---longer survival windows select for higher-quality firms---but
the advantage remains economically meaningful
(Appendix [\[app:c\]](#app:c){reference-type="ref" reference="app:c"},
Table [\[tab:threshold\]](#tab:threshold){reference-type="ref"
reference="tab:threshold"}). Third, I interpret results as robust
correlational patterns consistent with theory, not as causal effects.
Future work could exploit quasi-experimental variation (VC fund vintage
effects, geographic funding shocks) to strengthen causal claims. *Note:
H3 is sensitive to M&A coding; when M&A is coded as success, $\rho(E,G)$
reverses from $-0.04$ to $+0.15$. H1 and H2 are robust across all coding
approaches (Appendix [\[app:c\]](#app:c){reference-type="ref"
reference="app:c"},
Table [\[tab:ma-sensitivity\]](#tab:ma-sensitivity){reference-type="ref"
reference="tab:ma-sensitivity"}).*

## Conclusion

This chapter described how I test the cage hypotheses using 168,011 U.S.
ventures from PitchBook (2021--2025), with repositioning measured
through dictionary-based text analysis. The key finding is that
repositioning is rare---only 38.8% of ventures change their strategic
positioning, consistent with the golden cage theory that governance
constraints make movement difficult. The base success rate is 11.0%, but
this masks substantial heterogeneity between Movers and Stayers.
Chapter [\[ch:results\]](#ch:results){reference-type="ref"
reference="ch:results"} tests whether funding suppresses repositioning
(H1), whether repositioning predicts success (H2), and where these
patterns vary across industries.
