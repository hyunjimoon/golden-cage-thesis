---
modified:
  - 2026-01-15T10:42:02-05:00
---
\hypertarget{ch:data}{%
\chapter{Data and Identification}\label{ch:data}}

\hypertarget{introduction}{%
\section{Introduction}\label{sec:ch3-introduction}}

Chapter~\ref{ch:theory} argued that funding creates a golden cage by homogenizing governance beliefs. This chapter describes how I test that theory. The core challenge is measuring flexibility---a latent capability that cannot be directly observed. My solution is to measure its behavioral manifestation: repositioning, the observable shift in a venture's strategic positioning over time. Ventures that reposition reveal they had flexibility; ventures that hold position may lack it.

I analyze 180,994 U.S. ventures from PitchBook (2021--2025). To measure repositioning, I use dictionary-based text analysis of company descriptions, computing how much each venture's strategic breadth changed between funding rounds. The method draws on established research in category spanning \citep{zuckerman1999the} and linguistic concreteness \citep{pan2018corporate}.

A key identification concern is selection: high-conviction founders may both raise more capital and resist pivoting, producing correlation without causation. I address this in Section~\ref{identification-strategy}, arguing that selection is part of the mechanism (not a confound) and conditioning on observable characteristics.

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

\textbf{From latent flexibility to observable repositioning.} The theory chapter treats strategic flexibility ($F$) as a \emph{latent} capability: the ability to keep multiple viable paths live under uncertainty. Because $F$ is unobserved in administrative venture data, I proxy it with \textbf{repositioning} ($R$), the observable behavioral manifestation of latent flexibility. Ventures that reposition reveal that they retained (and were permitted by governance to exercise) flexibility; ventures that remain static may lack the capability or may be structurally caged. This proxy motivates the empirical focus on $E \rightarrow R$ and $R \rightarrow G$ in Chapter~\ref{ch:results}.

\hypertarget{strategic-breadth-b}{%
\subsection{Strategic Breadth (B)}\label{strategic-breadth-b}}

I operationalize \textbf{Strategic Breadth (B)} using dictionary-based text analysis of company descriptions. Drawing on category spanning research \citep{zuckerman1999the, pontikes2012two} and linguistic concreteness research \citep{pan2018corporate}, I construct a continuous measure (0--100) that captures the degree of vagueness in a venture's positioning.

The measure combines two components. The first is \emph{Categorical Vagueness}: how much a description uses broad, umbrella terms (``platform,'' ``ecosystem,'' ``solution'') rather than specific market categories (``mobile payments,'' ``enterprise SaaS''). A company describing itself as a ``technology platform'' spans many categories; one describing itself as ``inventory management software for small retailers'' does not. The second component is \emph{Concreteness Deficit}: whether the description lacks specific binding markers such as quantitative targets (``10,000 users'') or narrow technical specifications (``HIPAA-compliant cloud storage'').

The resulting score ranges from 0 to 100. A score of 0 means maximally specific positioning---the company has committed to a narrow path. A score of 100 means maximally vague positioning---the company retains many possible directions. The sample mean is B = 52.3 (SD = 18.4). Full construction details appear in Appendix A.

\textbf{Illustrative Examples.} Table~\ref{tab:breadth-examples} demonstrates how the vagueness measure (B) captures strategic positioning breadth using examples from the autonomous vehicle (AV) industry---a capital-intensive sector where the golden cage mechanism binds tightly. Movers repositioned substantially between 2021--2025; Stayers maintained consistent positioning.

\begin{table}[h]

\centering
\caption{Vagueness Measure: Illustrative Examples from AV Industry}
\label{tab:breadth-examples}

\small

\begin{tabular}{p{2.2cm}p{4.2cm}p{4.2cm}cc}

\toprule

\textbf{Company} & \textbf{2021 Description} & \textbf{2025 Description} & $\Delta B$ & \textbf{Growth Mult.} \\

\midrule

\multicolumn{5}{l}{\emph{Panel A: Movers (Zoom-Out)}} \\

\addlinespace

\textbf{Aurora} & ``Developer of autonomous trucks for freight logistics'' & ``Autonomous driving platform powering trucking, ride-hailing, and delivery'' & +38.2 & \\

& (Specific: trucking focus) & (Broad: multi-modal platform) & & \\

& $B_0 = 42.1$ (precise) & $B_T = 80.3$ (vague) & & $3.2\times$ \\

\midrule

\multicolumn{5}{l}{\emph{Panel B: Movers (Zoom-In)}} \\

\addlinespace

\textbf{Cruise} & ``Developer of self-driving vehicles for urban mobility'' & ``Provider of personal autonomous vehicle technology for OEMs'' & $-35.6$ & \\

& (Broad: urban mobility) & (Specific: OEM licensing) & & \\

& $B_0 = 76.4$ (vague) & $B_T = 40.8$ (precise) & & $2.9\times$ \\

\midrule

\multicolumn{5}{l}{\emph{Panel C: Stayers}} \\

\addlinespace

\textbf{Argo AI} & ``Developer of Level 4 autonomous driving technology for robotaxis'' & ``Developer of Level 4 autonomous driving technology for robotaxis'' & 0.0 & \\

& (Unchanged positioning despite market signals) & & & \\

& $B_0 = 58.2$ & $B_T = 58.2$ & & $1.0\times$* \\

\bottomrule

\end{tabular}

\end{table}

\emph{Notes: B = vagueness score (0--100 scale); $\Delta B = B_T - B_0$; Growth Multiple $= F_t/E$ (total subsequent funding / early funding). *Argo AI shut down in October 2022; growth multiple reflects capital consumed before shutdown.}

\textbf{Why AV?} The autonomous vehicle industry provides a natural laboratory for the golden cage mechanism because it combines three conditions that amplify the cage: (1) high capital intensity---\$100M+ funding rounds create strong sunk costs, (2) regulatory uncertainty---policy landscapes shift unpredictably across jurisdictions, and (3) technology path uncertainty---viable architectures compete (lidar vs. camera-only, robotaxi vs. personal AV, trucking vs. passenger). These conditions create strong investor sorting: VCs who fund AV ventures hold firm beliefs about which approach will win.

\textbf{Aurora (Zoom-Out, $3.2\times$):} Aurora began in 2021 as a trucking-focused company: ``autonomous trucks for freight logistics.'' By 2025, Aurora had broadened to a multi-modal ``Aurora Driver'' platform powering trucking, ride-hailing, and delivery. This repositioning---from specific application to general platform---attracted new partners (PACCAR, Volvo, Uber Freight) and enabled \$820M+ in additional funding. The zoom-out preserved optionality: if trucking unit economics proved unfavorable, the platform could pivot to other applications without abandoning the core technical asset.

\textbf{Cruise (Zoom-In, $2.9\times$):} Cruise took the opposite path. In 2021, Cruise positioned broadly as an ``urban mobility'' company operating robotaxis in San Francisco. By 2025, GM's ``Cruise 2.0'' strategy narrowed focus: exiting the robotaxi business to license autonomous technology to OEMs for personal vehicles. This zoom-in responded to market signals that robotaxi unit economics were challenging. The repositioning freed Cruise from fleet operations costs while monetizing its core technical capability through licensing.

\textbf{Argo AI (Stayer, $1.0\times$):} Argo AI maintained identical positioning from 2021 through its October 2022 shutdown: ``Level 4 autonomous driving technology for robotaxis.'' Despite \$3.6B in funding from Ford and Volkswagen, Argo failed to attract new investors when both backers reduced commitment. The company's inability to reposition illustrates the cage mechanism: Ford and VW, as thesis-driven investors, had funded a specific technical approach (robotaxis). When that approach encountered headwinds, Argo's board---populated solely by believers in robotaxis---lacked advocates for alternatives like trucking or OEM licensing. The cage was structural, not motivational.

\textbf{The Key Pattern:} Both Movers achieved $\sim$3$\times$ growth multiples; the Stayer achieved $1.0\times$ (capital consumed without subsequent growth). The \emph{direction} of repositioning differed---Aurora zoomed out, Cruise zoomed in---but \emph{movement itself} distinguished survivors from the caged. This pattern motivates the binary Mover/Stayer classification used throughout the empirical analysis.

\hypertarget{repositioning-r}{%
\subsection{Repositioning (R)}\label{repositioning-r}}

\textbf{Repositioning (R).} Repositioning magnitude measures the absolute change in strategic breadth: $R_i = |B_T - B_0|$, where $B_0$ is breadth at baseline (2021) and $B_T$ at endpoint (2025). Importantly, most ventures do not reposition at all: 59.7\% show R = 0 (I call these ``Stayers''), while only 40.3\% show R \textgreater{} 0 (``Movers''). This pattern---most ventures holding position---is consistent with the golden cage theory: governance constraints make repositioning difficult.

\textbf{Success (L) and Growth Multiple.}

I use two outcome measures. \textbf{Success (L)} is a binary indicator: $L = 1$ if the venture reached Later Stage VC (Series C or beyond) by the end of the observation window, $L = 0$ otherwise. The base success rate is 11.5\%. The \textbf{Mover Advantage} (2.60$\times$) compares success rates: $P(L=1|\text{Mover}) / P(L=1|\text{Stayer})$. Separately, the \textbf{Growth Multiple} $= F_t/E$ measures continuous funding scale for illustrative cases. \emph{Robustness checks using alternative threshold definitions are provided in Appendix C.}

\hypertarget{descriptive-statistics}{%
\section{Descriptive Statistics}\label{descriptive-statistics}}

The sample divides into two groups. Stayers (107,917 ventures, 59.7\%) show no strategic movement---their company descriptions remained essentially unchanged over the observation window. Movers (72,943 ventures, 40.3\%) exhibited repositioning, shifting their strategic breadth by a measurable amount.

Overall, 11.5\% of ventures reach Later Stage VC (Series C or beyond) by the end of the observation window. This is the baseline success rate. The average strategic breadth at baseline is B = 52.3 on the 0--100 scale, with substantial variation (SD = 18.4). Full descriptive statistics appear in Appendix A.

\hypertarget{identification-strategy}{%
\section{Identification Strategy}\label{identification-strategy}}

The central challenge is distinguishing selection from treatment effects. High-conviction founders may both raise more capital and resist pivoting---not because funding caused rigidity, but because conviction drove both outcomes. This concern is valid, and I do not claim causal identification.

However, I argue that selection is part of the mechanism, not a confound to be eliminated. The golden cage theory predicts that funding and rigidity correlate \emph{because} committed founders attract committed investors through sorting. The selection concern is precisely what the theory describes. The question is not whether selection exists---it does---but whether the pattern is consistent with the theoretical mechanism.

I address identification in three ways. First, I condition on survival: all ventures in the comparison survived to Year 3, ensuring equal opportunity to reposition. Among these ventures, Movers still achieve 2.60$\times$ higher success rates than Stayers. Second, I control for observable characteristics: founder experience, industry fixed effects, cohort timing, and initial positioning. Third, I interpret results as robust correlational patterns consistent with theory, not as causal effects. Future work could exploit quasi-experimental variation (VC fund vintage effects, geographic funding shocks) to strengthen causal claims.

\hypertarget{conclusion}{%
\section{Conclusion}\label{conclusion}}

This chapter described how I test the cage hypotheses. The sample comprises 180,994 U.S. ventures from PitchBook (2021--2025), with repositioning measured through dictionary-based text analysis.

I defend against identification threats in four ways: (1) treating selection as mechanism rather than confound, (2) conditioning on fixed horizons to mitigate survival bias, comparing repositioners and non-repositioners among ventures that survived equally long (Year 3+), (3) conditioning on observables, and (4) proposing future quasi-experimental approaches for causal identification.

The key finding from this chapter is that repositioning is rare: only 40\% of ventures change their strategic positioning. This is consistent with the golden cage theory---governance constraints make movement difficult. The base success rate is 11.5\%, but this masks substantial heterogeneity between Movers and Stayers.

Chapter~\ref{ch:results} tests whether funding suppresses repositioning (H1), whether repositioning predicts success (H2), and where these patterns vary across industries.