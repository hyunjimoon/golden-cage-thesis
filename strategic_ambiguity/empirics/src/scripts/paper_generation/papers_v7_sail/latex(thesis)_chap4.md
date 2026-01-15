---
modified:
  - 2026-01-15T06:35:50-05:00
---
\hypertarget{ch:results}{%
\chapter{Where the Cage Binds}\label{ch:results}}

\hypertarget{introduction}{%
\section{Introduction}\label{sec:ch4-introduction}}

Chapter~\ref{ch:theory} theorized that funding creates a golden cage through governance homogenization. Chapter~\ref{ch:data} described how I measure repositioning from company descriptions. This chapter tests whether the patterns exist in the data.

I test three hypotheses. First, the Commitment Cage (H1): does funding suppress repositioning? Second, the Flexibility Flex (H2): does repositioning predict success? Third, the Funding-Growth Paradox (H3): does early funding correlate negatively with later success? The theory predicts that H3 arises because H1 and H2 combine: funding suppresses the very mechanism (repositioning) that drives success.

The results confirm all three hypotheses. Funding suppresses repositioning ($\rho = -0.087$, p \textless{} 0.001). Repositioning predicts success---Movers outperform Stayers by 2.60$\times$. And the overall funding-growth correlation is negative ($\rho = -0.196$, p \textless{} 0.001). I also document industry heterogeneity: the cage binds tightest in capital-intensive sectors like Hardware and Transportation, but loosens in pre-paradigmatic sectors like Quantum where no dominant design has emerged.

\begin{figure}
\hypertarget{fig:mover-advantage}{%
\centering
\includegraphics[width=0.9\textwidth,]{img/Ch4_Fig1_G_by_R.png}
\caption{The Mover Advantage. Ventures that reposition (Movers) achieve 18.1\% success rates; those that hold position (Stayers) achieve only 7.0\%. This 2.60$\times$ difference is the Flexibility Flex.}\label{fig:mover-advantage}
}
\end{figure}

\hypertarget{h1-funding-growth-the-funding-growth-paradox}{%
\section{H1: Funding \ensuremath{\rightarrow} Growth (The Funding-Growth Paradox)}\label{h1-funding-growth-the-funding-growth-paradox}}

The data confirm H1: early-stage funding correlates negatively with later-stage success ($\rho(E,G) = -0.196^{***}$, $N = 180{,}994$). This is the aggregate paradox introduced in Chapter~\ref{ch:introduction}. Chapters~\ref{ch:data}--\ref{ch:results} unpack the paradox by testing two component relationships: funding suppresses repositioning ($E \rightarrow R$) and repositioning predicts growth ($R \rightarrow G$).

\hypertarget{h2-funding-repositioning-the-commitment-trap}{%
\section{H2: Funding \ensuremath{\rightarrow} Repositioning (\cage{Commitment Cage})}\label{sec:h2-commitment-cage}}

As theorized in Chapter~\ref{ch:theory}, funding should suppress repositioning through governance homogenization. The data confirm H2: funding suppresses repositioning (\ensuremath{\rho} = -0.087***, N = 180,994). The correlation is robust to industry FE (-0.082), cohort FE (-0.079), and founder controls (-0.075). Well-funded ventures reposition less, consistent with the cage mechanism where higher funding correlates with more specific commitments and more homogeneous governance.

\hypertarget{h3-repositioning-growth-the-flexibility-premium}{%
\section{H3: Repositioning \ensuremath{\rightarrow} Growth (\flex{Flexibility Flex})}\label{sec:h3-flexibility-flex}}

\hypertarget{main-finding}{%
\subsection{Main Finding}\label{main-finding}}

The data confirm H3: repositioning enables growth.

\input{table/frg_analysis.tex}

The positive correlation is consistent: ventures that reposition succeed more often.

\hypertarget{the-mover-advantage-2.60}{%
\subsection{The Mover Advantage: 2.60\ensuremath{\times}}\label{the-mover-advantage-2.60}}

To operationalize this relationship, I classify ventures as Movers or Stayers (primary), with a secondary directional breakdown for interpretation.

\input{table/mover_taxonomy.tex}

\emph{Note: R \textgreater{} 0 = any repositioning. See Section~3.3.3 for definition rationale.}

\textbf{The core finding:} Movers outperform Stayers by \textbf{2.60\ensuremath{\times}} in success rate ($P(L=1)$: 18.1\% vs.~7.0\%, p \textless{} 0.001, \ensuremath{\chi^2} = 5,322). This binary classification is the primary taxonomy used throughout subsequent analyses.

\emph{Note: \ensuremath{\Delta}B = B\_T - \ensuremath{B_0}. Zoom-in = narrowing (\ensuremath{\Delta}B \textless{} 0); Zoom-out = expanding (\ensuremath{\Delta}B \textgreater{} 0). Remaining Movers (36,554) have minimal directional change.}

\textbf{Interpretive insight:} Both directions show elevated success rates (17.1\% and 18.4\%). This suggests that \emph{moving clearly}, not which direction you move, explains the mover advantage. The binary Mover/Stayer distinction carries the primary identification.

\emph{See Appendix C for detailed mover vs. stayer anatomy visualization.}

\hypertarget{illustrative-cases-h3}{%
\subsection{Illustrative Cases}\label{illustrative-cases-h3}}

Three median-representative cases illustrate the pattern: Hope Care (broadening mover, G = 2.71\ensuremath{\times}), True Botanicals (narrowing mover, G = 2.45\ensuremath{\times}), and Leap Green Energy (stayer, G = 0.80\ensuremath{\times}). Both mover types outperform stayers, demonstrating that \emph{movement itself}, not direction, drives the advantage.

\hypertarget{robustness-h3}{%
\subsection{Robustness}\label{robustness-h3}}

Results are robust to: (1) temporal stability across cohort years, (2) survival conditioning (Year 3+ survivors: 2.35\ensuremath{\times}, Year 5+: 2.12\ensuremath{\times}), and (3) alternative operationalizations of R. \emph{Full robustness tables are provided in Appendix C.}

\hypertarget{industry-heterogeneity-where-the-cage-binds-tightest}{%
\section{Industry Heterogeneity: Where the Cage Binds Tightest}\label{sec:industry-heterogeneity}}

The funding-growth paradox introduced in Section~\ref{sec:funding-growth-paradox} is not uniform---it varies systematically across industries. This section unpacks that heterogeneity.

\hypertarget{cross-industry-comparison}{%
\subsection{Cross-Industry Comparison}\label{cross-industry-comparison}}

The cage binds tighter in capital-intensive industries where switching costs are high. The following table presents verified correlations between early funding (E) and growth (G) across six industries.

\input{table/industry.tex}

\emph{Note: E = first\_financing\_size (M USD), G = growth (binary: reached Later Stage VC). Data verified from PitchBook (2021-2025).}

\begin{figure}
\hypertarget{fig:industry-rho}{%
\centering
\includegraphics[width=0.9\textwidth,]{img/Ch4_Fig2_industry_rho.png}
\caption{Industry heterogeneity in the early funding--growth correlation \$ ho(E,G)\$ (bars show correlation by industry; \(N\) by industry shown in plot).}\label{fig:industry-rho}
}
\end{figure}

Three patterns emerge. Capital-intensive industries show the strongest negative correlations: Hardware (\ensuremath{\rho} = -0.108) and Transportation (\ensuremath{\rho} = -0.101) face the tightest cage because infrastructure and physical asset investments lock ventures into positions that cannot adapt. Software shows near-zero correlation (\ensuremath{\rho} = -0.001, ns), demonstrating that low capital intensity allows the Oxygen and Cage effects to approximately balance---cheap experimentation offsets governance rigidity. Quantum is the sole positive outlier (\ensuremath{\rho} = +0.095*): under extreme uncertainty, the learning value of capital dominates rigidity costs, representing a boundary condition for the multiplicative model.

\hypertarget{the-era-of-ferment-exception}{%
\subsection{The Quantum Exception}\label{the-era-of-ferment-exception}}

Quantum computing shows a positive correlation ($\rho = +0.095$*)---the only industry where more funding associates with more success. Why? In technology evolution, industries pass through an ``era of ferment'' \citep{anderson1990technological} before a dominant design emerges. During this phase, multiple technical approaches compete and no architecture has proven superior. Quantum computing is in this phase: superconducting qubits, trapped ions, photonic approaches, and topological qubits all remain viable.

When no dominant design exists, capital cannot lock ventures into specific architectural choices because those choices have not yet crystallized. The learning value of capital (experimentation) dominates its rigidity cost (governance homogenization). This is a boundary condition for the golden cage theory: the cage mechanism assumes that commitment narrows options, but in pre-paradigmatic industries, there may be no options to narrow.

\emph{See Appendix C for industry survival baseline visualization.}

\hypertarget{the-triple-vulnerability}{%
\subsection{The Triple Vulnerability}\label{the-triple-vulnerability}}

The mobility sector exemplifies the cage mechanism through three vulnerabilities. Capital intensity requires massive upfront infrastructure investment. Regulatory uncertainty means policy landscapes shift unpredictably. Technology path uncertainty means multiple viable architectures compete. These vulnerabilities interact: capital intensity demands commitment, but uncertainty types multiply the cost of wrong commitment.

\hypertarget{conclusion}{%
\section{Conclusion}\label{conclusion}}

The evidence supports all three hypotheses. The Commitment Cage (H1) is confirmed: funding suppresses repositioning ($\rho = -0.087$***). The Flexibility Flex (H2) is confirmed: Movers achieve 2.60$\times$ higher success rates than Stayers (18.1\% vs 7.0\%). The Funding-Growth Paradox (H3) is confirmed: early funding correlates negatively with later success ($\rho = -0.196$***).

The cage does not bind uniformly. It is tightest in capital-intensive industries like Hardware and Transportation, where infrastructure investments create switching costs. It loosens in pre-paradigmatic sectors like Quantum, where no dominant design constrains architectural choices. This heterogeneity is consistent with the theory: the cage forms through commitment, and commitment matters more when switching costs are high.

These findings raise a question: if the cage is structural, can founders escape it? Chapter~\ref{ch:design} addresses this by developing design principles for commitment structures that preserve flexibility.