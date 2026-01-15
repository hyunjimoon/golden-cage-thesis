\hypertarget{ch:data}{%
\chapter{Data and Identification}\label{ch:data}}

\hypertarget{introduction}{%
\section{Introduction}\label{introduction}}

\textbf{This chapter describes the data and identification strategy for the golden cage hypotheses.} I analyze 180,994 U.S. ventures from PitchBook (2021--2025), measure repositioning through text analysis, and address selection concerns through a multi-layer identification strategy.

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

The sample construction retained 37.1\% of the initial universe: non-US exclusions (36\%), late-stage (14\%), insufficient observation window (10\%), and missing data (4\%).

\hypertarget{variable-operationalization}{%
\section{Variable Operationalization}\label{variable-operationalization}}

\input{table/variable.tex}

\hypertarget{strategic-breadth-b}{%
\subsection{Strategic Breadth (B)}\label{strategic-breadth-b}}

I operationalize \textbf{Strategic Breadth (B)} using dictionary-based text analysis of company descriptions. Drawing on category spanning research \citep{zuckerman1999the, pontikes2012two} and linguistic concreteness research \citep{pan2018corporate}, I construct a continuous measure (0--100) that captures the degree of vagueness in a venture's positioning.

The measure combines two validated components:
\begin{itemize}
\tightlist
\item \textbf{Categorical Vagueness}: The prevalence of superordinate terms (e.g., ``platform,'' ``ecosystem'') that span multiple market categories.
\item \textbf{Concreteness Deficit}: The absence of specific binding markers, such as precise quantitative targets or narrow technical specifications.
\end{itemize}

B = 0 indicates maximally specific positioning; B = 100 indicates maximally vague positioning. The sample mean is B = 52.3 (SD = 18.4). \emph{Full variable construction details, including keyword dictionaries and scoring formulas, are provided in Appendix C.}

\textbf{Illustrative Examples.} Table~\ref{tab:breadth-examples} demonstrates how the vagueness measure (B) captures strategic positioning breadth. Movers (Hope Care, True Botanicals) repositioned substantially between 2021--2025; Stayers (Leap Green Energy) maintained consistent positioning.

\begin{table}[h]
\centering
\caption{Vagueness Measure: Illustrative Examples from Sample}
\label{tab:breadth-examples}
\small
\begin{tabular}{p{2.5cm}p{4.5cm}p{4.5cm}cc}
\toprule
\textbf{Company} & \textbf{2021 Description} & \textbf{2025 Description} & $\Delta B$ & \textbf{G} \\
\midrule
\multicolumn{5}{l}{\emph{Panel A: Movers}} \\
\addlinespace
\textbf{Hope Care} & ``Cloud-based healthcare technology for primary care'' & ``Healthcare technology company offering preventive care and chronic disease management'' & +48.5 & \\
 & (Specific: named segment) & (Broad: platform for multiple conditions) & & \\
 & $B_0 = 39.6$ (precise) & $B_T = 88.2$ (vague) & & $G = 2.71\times$ \\
\addlinespace
\textbf{True Botanicals} & ``Natural products designed to liberate glow with clean skincare'' & ``Manufacturer of natural skin care products using clinically-proven formulations'' & $-44.4$ & \\
 & (Broad: abstract benefits) & (Specific: defined product category) & & \\
 & $B_0 = 81.9$ (vague) & $B_T = 37.5$ (precise) & & $G = 2.45\times$ \\
\midrule
\multicolumn{5}{l}{\emph{Panel B: Stayers}} \\
\addlinespace
\textbf{Leap Green Energy} & ``Operator of renewable energy-based power projects across India'' & ``Operator of renewable energy-based power projects across India'' & 0.0 & \\
 & (Nearly identical positioning) & & & \\
 & $B_0 = 87.5$ & $B_T = 87.5$ & & $G = 0.80\times$ \\
\bottomrule
\end{tabular}
\end{table}

\emph{Notes: B = vagueness score (0--100 scale); $\Delta B = B_T - B_0$; $G = F_t/E$ (total subsequent funding / early funding). Hope Care exemplifies successful broadening: pivoting from specific primary care to a general preventive health platform. True Botanicals exemplifies focusing: narrowing from broad wellness aspirations to specific skincare formulations. Both Movers achieved repositioning; direction differed but movement itself distinguished them from Stayers.}

\hypertarget{repositioning-r}{%
\subsection{Repositioning (R)}\label{repositioning-r}}

\textbf{Repositioning (R).} Repositioning magnitude measures the absolute change in strategic breadth: R\_i = \textbar B\_T - B\_0\textbar, where B\_0 is breadth at baseline (2021) and B\_T at endpoint (2025). The distribution exhibits zero-inflation: 59.7\% of ventures show R = 0 (Stayers), while 40.3\% show R \textgreater{} 0 (Movers).

\textbf{Growth (G).}

I operationalize growth as a \textbf{binary indicator}: G = 1 if the venture reached Later Stage VC (Series C or beyond) by the end of the observation window, G = 0 otherwise. This binary measure captures whether ventures successfully progressed through the funding lifecycle. The base success rate is 11.5\%. \emph{Robustness checks using the continuous funding growth multiple are provided in Appendix D.}

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

\textbf{Key distributional features} (full descriptive statistics in Appendix C):

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

Key sample characteristics: 40.3\% of ventures qualify as "Movers" (R \textgreater{} 0), while 59.7\% are "Stayers" (R = 0) (see Section~3.3.2 for definition rationale). The base success rate (reaching Later Stage VC) is 11.5\%. Chapter 4 presents the empirical results.
