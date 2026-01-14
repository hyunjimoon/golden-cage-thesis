\hypertarget{ch:data}{%
\chapter{Data and Identification}\label{ch:data}}

\begin{quote}
\emph{"How do we test it?"} \textbf{Key Numbers}: N = 180,994, Mover Rate = 40.3\%, Base Success Rate = 11.5\%
\end{quote}

\hypertarget{introduction}{%
\section{Introduction}\label{introduction}}

\textbf{This chapter tests the golden cage hypotheses.} I analyze 180,994 U.S. ventures from PitchBook (2021--2025), measure repositioning through text analysis, and address selection concerns through a multi-layer identification strategy.

\hypertarget{data-sources-and-sample-construction}{%
\section{Data Sources and Sample Construction}\label{data-sources-and-sample-construction}}

I construct a panel of 180,994 ventures from PitchBook, covering the period 2021--2025. PitchBook provides comprehensive coverage of U.S. venture-backed companies, including funding rounds, company descriptions, and outcome data.

\textbf{Sample Construction.} The initial universe contains 488,381 ventures. I apply the following filters:

\begin{enumerate}
\def\labelenumi{\arabic{enumi}.}
\tightlist
\item
  \textbf{Geography:} U.S.-headquartered ventures (reduces to 312,456)
\item
  \textbf{Stage:} Early-stage (Seed, Series A, Series B) at baseline (reduces to 245,892)
\item
  \textbf{Observation window:} Minimum 24 months observable history (reduces to 198,234)
\item
  \textbf{Data completeness:} Non-missing values for core variables (reduces to 180,994)
\end{enumerate}

\textbf{Figure 4: Sample Construction}

\begin{verbatim}
488,381 \ensuremath{\rightarrow} [US only] \ensuremath{\rightarrow} 312,456 \ensuremath{\rightarrow} [Early-stage] \ensuremath{\rightarrow} 245,892 \ensuremath{\rightarrow} [24mo+] \ensuremath{\rightarrow} 198,234 \ensuremath{\rightarrow} [Complete] \ensuremath{\rightarrow} 180,994
  All      (-36%)       US        (-14%)       Seed/A/B    (-10%)    Window     (-4%)      Final
\end{verbatim}

\emph{Retention: 37.1\%. Primary exclusions: non-US (36\%), late-stage (14\%), insufficient window (10\%), missing data (4\%).}

\hypertarget{variable-operationalization}{%
\section{Variable Operationalization}\label{variable-operationalization}}

\input{table/variable.tex}

\hypertarget{strategic-breadth-b}{%
\subsection{Strategic Breadth (B)}\label{strategic-breadth-b}}

Strategic breadth measures how vaguely a venture positions itself in public communications. High B means the venture positions broadly and ambiguously; low B means it positions specifically. I construct a 0--100 vagueness score from two components: \textbf{Categorical Vagueness} and \textbf{Concreteness Deficit}.

\hypertarget{theoretical-foundation}{%
\subsubsection{Theoretical Foundation}\label{theoretical-foundation}}

I draw on three literatures. First, \textbf{category spanning research} \citep{zuckerman1999the, hannan2007logics, pontikes2012two} shows that ventures using abstract category labels ("platform," "ecosystem") signal broader scope than those using concrete labels ("restaurant," "delivery app"). \citet{hsu2006jacks} shows that category breadth affects how audiences evaluate ventures, spanning multiple categories reduces legitimacy but preserves strategic options.

Second, \textbf{linguistic concreteness research} \citep{pan2018corporate, chen2015a} shows that specific text, quantitative markers, temporal references, technical acronyms, signals that ventures have committed to particular outcomes. Ventures that avoid specificity preserve flexibility by not anchoring stakeholder expectations to measurable targets.

Third, \textbf{symbolic differentiation research} \citep{barlow2025it} examines how quality-signaling resources interact with narrative distinctiveness. Their analysis of 31,270 UK ventures demonstrates that patent-rich ventures strategically modulate narrative distinctiveness based on industry conditions, a finding consistent with the golden cage mechanism where resource acquisition shapes symbolic positioning.

\hypertarget{component-1-categorical-vagueness}{%
\subsubsection{Component 1: Categorical Vagueness}\label{component-1-categorical-vagueness}}

Following \citet{zuckerman1999the} and \citet{hannan2007logics}, I measure categorical vagueness through the prevalence of \textbf{abstract keywords} in company descriptions and PitchBook keyword fields.

\textbf{Abstraction keywords} (superordinate category terms): - \emph{High abstraction}: "platform," "solution," "ecosystem," "technology," "approach," "service," "advanced," "next-generation," "sustainable," "AI," "data," "analytics" - \emph{Low abstraction}: "device," "application," "tool," "product," "restaurant," "clinic," "factory"

The categorical vagueness score combines two sub-measures:

\begin{enumerate}
\def\labelenumi{(\alph{enumi})}
\item
  \emph{Abstraction Ratio}: Proportion of keywords belonging to the abstract category. \[\text{Abstraction}_i = \frac{\text{Abstract keywords}}{\text{Total keywords}}\]
\item
  \emph{Category Diversity}: Following \citet{pontikes2012two}, ventures spanning multiple distinct categories exhibit higher strategic ambiguity. I measure uniqueness ratio: \[\text{Diversity}_i = \frac{\text{Unique keywords}}{\text{Total keywords}}\]
\end{enumerate}

The categorical vagueness component averages these sub-measures: \[\text{CategoricalVagueness}_i = 50 \times (\text{Abstraction}_i + \text{Diversity}_i)\]

\hypertarget{component-2-concreteness-deficit}{%
\subsubsection{Component 2: Concreteness Deficit}\label{component-2-concreteness-deficit}}

Following \citet{pan2018corporate} and \citet{chen2015a}, I measure the \emph{absence} of concrete markers in company descriptions. Ventures that avoid specific commitments, quantitative targets, temporal milestones, technical specifications, preserve strategic flexibility.

\textbf{Concreteness markers} (specificity indicators): - \emph{Temporal specificity}: "Q3 2024," "by 2025," "within 18 months" - \emph{Quantitative specificity}: "95\%," "100x faster," "6x stronger," "\$50M revenue" - \emph{Technical specificity}: "Level 4 autonomy," "510(k) clearance," "LPBF," "DLS"

I count concrete markers per 100 words of description text: \[\text{ConcretenessDensity}_i = \frac{\text{Concrete markers} \times 100}{\text{Total words}}\]

The concreteness deficit (vagueness component) inverts this measure: \[\text{ConcreteDeficit}_i = 100 - \min(\text{ConcretenessDensity}_i \times 5, 100)\]

\hypertarget{composite-score}{%
\subsubsection{Composite Score}\label{composite-score}}

The final strategic breadth score averages both components: \[B_i = \frac{\text{CategoricalVagueness}_i + \text{ConcreteDeficit}_i}{2}\]

\textbf{Interpretation}: B = 0 indicates maximally specific positioning (narrow breadth); B = 100 indicates maximally vague positioning (broad breadth). The sample mean is B = 52.3 (SD = 18.4), indicating moderate strategic ambiguity on average.

\hypertarget{validation}{%
\subsubsection{Validation}\label{validation}}

The measure exhibits expected correlations: - \textbf{Convergent validity}: B correlates positively with industry uncertainty (\ensuremath{\rho} = +0.18, p \textless{} 0.001), ventures in nascent markets position more broadly. - \textbf{Discriminant validity}: B correlates near-zero with funding amount (\ensuremath{\rho} = -0.03, ns) at baseline, breadth is a strategic choice, not a resource constraint. - \textbf{Predictive validity}: Initial breadth (\ensuremath{B_0}) predicts repositioning magnitude (\ensuremath{\rho}(\ensuremath{B_0}, R) = +0.11, p \textless{} 0.001), broader initial positioning enables larger subsequent movements.

\hypertarget{repositioning-r}{%
\subsection{Repositioning (R)}\label{repositioning-r}}

\textbf{Repositioning (R).} Repositioning magnitude measures the absolute change in strategic breadth: R\_i = \textbar B\_T - B\_0\textbar, where B\_0 is breadth at baseline (2021) and B\_T at endpoint (2025). The distribution exhibits zero-inflation: 59.7\% of ventures show R = 0 (Stayers), while 40.3\% show R \textgreater{} 0 (Movers).

\textbf{Growth (G).}

I operationalize growth as the funding growth multiple: G = (F\_t - E) / E, where F\_t is total funding raised and E is early-stage funding. This continuous measure captures the magnitude of capital accumulation subsequent to initial financing. The median G is 0.9\ensuremath{\times} (near-doubling); the distribution is right-skewed with mean 0.67\ensuremath{\times}.

\textbf{Commitment (C).}

Commitment (C) is the first variable in the causal chain (C \ensuremath{\rightarrow} E \ensuremath{\rightarrow} R \ensuremath{\rightarrow} G) and is operationalized as \textbf{initial strategic specificity}, the degree to which a venture's early positioning forecloses alternative paths. I construct a 0--100 commitment index from three components:

\begin{enumerate}
\def\labelenumi{(\alph{enumi})}
\item
  \emph{Product Category Count.} Fewer initial product categories indicate higher commitment. A venture targeting "enterprise SaaS for healthcare compliance" (1 category) exhibits higher C than one targeting "AI-powered solutions for enterprise" (3+ categories). I invert the category count: C\_a = 100 \ensuremath{\times} (1 / categories).
\item
  \emph{Milestone Granularity.} More specific milestones in early pitch materials indicate higher commitment. I code milestone specificity from company descriptions and funding announcements: vague milestones ("achieve product-market fit") score low; specific milestones ("FDA 510(k) clearance by Q3 2024") score high. C\_b = 0--100 based on milestone specificity.
\item
  \emph{Investor Agreement Terms.} Staged milestone-based funding structures indicate higher commitment than unconditional tranches. I proxy this through funding round structure: ventures with milestone-triggered tranches score higher than those with single-tranche rounds. C\_c = 100 if staged, 50 if mixed, 0 if unconditional.
\end{enumerate}

The composite index averages the three components: \textbf{C = (C\_a + C\_b + C\_c) / 3}.

\emph{Validation.} Commitment correlates positively with early funding (\ensuremath{\rho}(C,E) = +0.23, p \textless{} 0.001), confirming that specific commitments attract capital. Commitment also moderates the E \ensuremath{\rightarrow} R relationship: the negative correlation between funding and repositioning strengthens at high C (interaction \ensuremath{\beta} = -0.04, p \textless{} 0.01), consistent with the cage mechanism.

\hypertarget{descriptive-statistics}{%
\section{Descriptive Statistics}\label{descriptive-statistics}}

\input{table/descriptive.tex}

\emph{Note: R is reported in standardized units for cross-venture comparability; raw R = \textbar B\_T - \ensuremath{B_0}\textbar{} ranges 0--100. G is the funding growth multiple. See Section~4.6 for illustrative cases.}

\textbf{Key distributional features:}

\begin{itemize}
\tightlist
\item
  \textbf{Stayers:} 107,917 ventures (59.7\%) show no strategic movement (R = 0)
\item
  \textbf{Movers:} 72,943 ventures (40.3\%) exhibit repositioning (R \textgreater{} 0)
\end{itemize}

\hypertarget{identification-strategy}{%
\section{Identification Strategy}\label{identification-strategy}}

The central challenge: distinguishing selection from treatment effects. \citeauthor{vandensteen2010interpersonal}'s \citeyearpar{vandensteen2010interpersonal} sorting equilibrium predicts that high-conviction founders match with high-conviction investors, producing correlation between funding and rigidity without funding \emph{causing} rigidity. I document robust correlational patterns consistent with a theoretical mechanism, not causal effects.

\textbf{Multi-Layer Defense.} (1) \emph{Selection as Mechanism}: I contend this selection \emph{is} part of the mechanism, not a confound. The golden cage forms through selection \emph{and} subsequent contractual reinforcement. (2) \emph{Fixed-Horizon Conditioning}: I condition on survival to Year 3 before comparing Movers and Stayers, all ventures had equal opportunity to reposition. Among these equal-survival-opportunity firms, Movers still achieve 2.60\ensuremath{\times} higher success rates. (3) \emph{Observable Controls}: I control for founder characteristics, industry fixed effects, cohort timing, and initial positioning. (4) \emph{Future Work}: Quasi-experimental approaches (VC fund vintage effects, geographic shocks) could disentangle selection from treatment.

\hypertarget{conclusion}{%
\section{Conclusion}\label{conclusion}}

This chapter described how I test the cage hypotheses. The sample comprises 180,994 U.S. ventures from PitchBook (2021--2025), with repositioning measured through dictionary-based text analysis.

I defend against identification threats in four ways: (1) treating selection as mechanism rather than confound, (2) conditioning on fixed horizons to mitigate survival bias, comparing repositioners and non-repositioners among ventures that survived equally long (Year 3+), (3) conditioning on observables, and (4) proposing future quasi-experimental approaches for causal identification.

Key sample characteristics: 40.3\% of ventures qualify as "Movers" (R \textgreater{} 0), while 59.7\% are "Stayers" (R = 0) (see Section~3.3.3 for definition rationale). The base success rate (reaching Later Stage VC) is 11.5\%. Chapter 4 presents the empirical results.
