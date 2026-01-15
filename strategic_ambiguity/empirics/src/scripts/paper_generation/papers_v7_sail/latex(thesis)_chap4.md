\hypertarget{ch:results}{%
\chapter{Where the Cage Bites}\label{ch:results}}

\begin{figure}
\hypertarget{fig:mover-advantage}{%
\centering
\includegraphics[width=0.9\textwidth,]{img/Ch4_Fig1_mover_advantage.png}
\caption{Mover advantage: ventures that reposition exhibit higher success than stayers (figure values shown in plot).}\label{fig:mover-advantage}
}
\end{figure}

\hypertarget{introduction}{%
\section{Introduction}\label{introduction}}

\textbf{This chapter documents where the cage bites.} I analyze 180,994 ventures across industries, test two patterns, Funding \ensuremath{\rightarrow} Repositioning\ensuremath{\downarrow} (CER) and Repositioning \ensuremath{\rightarrow} Growth\ensuremath{\uparrow} (FRG), and show that their product explains the Funding-Growth Paradox. The results confirm all three hypotheses and reveal industry heterogeneity.

\textbf{Contributions.} (1) \emph{I confirm all three hypotheses}, H1 (\ensuremath{\rho}(E,G) = -0.196***), H2 (\ensuremath{\rho}(E,R) = -0.087***), H3 (Mover advantage = 2.60\ensuremath{\times}). (2) \emph{Industry heterogeneity}: The cage binds tightest in capital-intensive sectors like mobility (5.3\% survival). (3) \emph{Robustness}: Results hold across cohort years, alternative specifications, and survival conditioning.

\hypertarget{h2-funding-repositioning-the-commitment-trap}{%
\section{H2: Funding \ensuremath{\rightarrow} Repositioning (The Commitment Trap)}\label{h2-funding-repositioning-the-commitment-trap}}

The data confirm H2: funding suppresses repositioning (\ensuremath{\rho} = -0.087***, N = 180,994). The correlation is robust to industry FE (-0.082), cohort FE (-0.079), and founder controls (-0.075). Well-funded ventures reposition less, consistent with the cage mechanism where higher funding correlates with more specific commitments and more homogeneous governance.

\hypertarget{h3-repositioning-growth-the-flexibility-premium}{%
\section{H3: Repositioning \ensuremath{\rightarrow} Growth (The Flexibility Premium)}\label{h3-repositioning-growth-the-flexibility-premium}}

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

\textbf{The core finding:} Movers outperform Stayers by \textbf{2.60\ensuremath{\times}} (18.1\% vs.~7.0\%, p \textless{} 0.001, \ensuremath{\chi^2} = 5,322). This binary classification is the primary taxonomy used throughout subsequent analyses.

\emph{Note: \ensuremath{\Delta}B = B\_T - \ensuremath{B_0}. Zoom-in = narrowing (\ensuremath{\Delta}B \textless{} 0); Zoom-out = expanding (\ensuremath{\Delta}B \textgreater{} 0). Remaining Movers (36,554) have minimal directional change.}

\textbf{Interpretive insight:} Both directions show elevated success rates (17.1\% and 18.4\%). This suggests that \emph{moving clearly}, not which direction you move, explains the mover advantage. The binary Mover/Stayer distinction carries the primary identification.

\emph{See Appendix E for detailed mover vs. stayer anatomy visualization.}

\hypertarget{effect-size-contextualization}{%
\subsection{Effect Size Contextualization}\label{effect-size-contextualization}}

The 2.60\ensuremath{\times} Mover advantage represents an 11.1 percentage point difference in success rates (18.1\% - 7.0\%). To assess practical significance, I benchmark against comparable interventions in the entrepreneurship literature:

\textbf{Interpretation:} The Mover Advantage exceeds effect sizes of other well-documented success factors. Repositioning improves success more than accelerator participation (\textasciitilde5 pp), founder experience (\textasciitilde5 pp), or prestigious backing (\textasciitilde4 pp). Strategic mobility is not marginal, it is a first-order determinant of venture outcomes.

\textbf{Standard deviation interpretation:} The correlation \ensuremath{\rho}(R,G) = +0.012 implies that one standard deviation increase in repositioning magnitude (R) associates with approximately 4--6 percentage point improvement in later-stage success. While modest in standardized terms, this translates to substantial absolute differences given the low base rate (11.5\%).

\hypertarget{industry-heterogeneity-where-the-cage-bites-hardest}{%
\section{Industry Heterogeneity: Where the Cage Bites Hardest}\label{industry-heterogeneity-where-the-cage-bites-hardest}}

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

\textbf{Key findings:}

\begin{enumerate}
\def\labelenumi{\arabic{enumi}.}
\item
  \textbf{Capital-intensive industries show strongest negative correlations.} Hardware (\ensuremath{\rho} = -0.108) and Transportation (\ensuremath{\rho} = -0.101) face the tightest cage. Infrastructure and physical asset investments lock ventures into positions that cannot adapt.
\item
  \textbf{Software shows near-zero correlation.} The software industry (\ensuremath{\rho} = -0.001, ns) demonstrates that low capital intensity allows Oxygen and Cage effects to approximately balance. Cheap experimentation offsets governance rigidity.
\item
  \textbf{Quantum is the sole positive outlier.} Under extreme uncertainty, the learning value of capital dominates rigidity costs (\ensuremath{\rho} = +0.095*). This represents a boundary condition for the multiplicative model.
\end{enumerate}

\hypertarget{the-era-of-ferment-exception}{%
\subsection{The Era of Ferment Exception}\label{the-era-of-ferment-exception}}

Quantum's positive correlation (\ensuremath{\rho} = +0.095*) represents a boundary condition: when no dominant design exists \citep{anderson1990technological}, capital cannot lock ventures into architectural choices that have not crystallized, so dR/dE reverses sign.

\emph{See Appendix E for industry survival baseline visualization.}

\hypertarget{the-triple-vulnerability}{%
\subsection{The Triple Vulnerability}\label{the-triple-vulnerability}}

The mobility sector exemplifies the cage mechanism:

\begin{enumerate}
\def\labelenumi{\arabic{enumi}.}
\tightlist
\item
  \textbf{Capital intensity:} Infrastructure requires massive upfront investment
\item
  \textbf{Regulatory uncertainty:} Policy landscapes shift unpredictably
\item
  \textbf{Technology path uncertainty:} Multiple viable architectures compete
\end{enumerate}

These three vulnerabilities interact: capital intensity demands commitment, but uncertainty types multiply the cost of wrong commitment.

\hypertarget{robustness-checks}{%
\section{Robustness Checks}\label{robustness-checks}}

Results are robust to: (1) temporal stability across cohort years, (2) survival conditioning (Year 3+ survivors: 2.35\ensuremath{\times}, Year 5+: 2.12\ensuremath{\times}), and (3) alternative operationalizations of R. \emph{Full robustness tables are provided in Appendix E.}

\hypertarget{illustrative-cases}{%
\section{Illustrative Cases}\label{illustrative-cases}}

Three median-representative cases illustrate the pattern: Hope Care (broadening mover, G = 2.71\ensuremath{\times}), True Botanicals (narrowing mover, G = 2.45\ensuremath{\times}), and Leap Green Energy (stayer, G = 0.80\ensuremath{\times}). Both mover types outperform stayers, demonstrating that \emph{movement itself}, not direction, drives the advantage. \emph{Full case descriptions are provided in Appendix F.}

\hypertarget{conclusion}{%
\section{Conclusion}\label{conclusion}}

The evidence supports all three hypotheses:

\begin{itemize}
\tightlist
\item
  \textbf{H1 (Commitment Trap) confirmed:} \ensuremath{\rho}(E,R) = -0.087*** ,  Funding suppresses repositioning
\item
  \textbf{H2 (Flexibility Premium) confirmed:} Mover advantage = 2.60\ensuremath{\times} ,  Repositioning enables growth
\item
  \textbf{H3 (Funding Paradox) confirmed:} \ensuremath{\rho}(E,G) = -0.196*** ,  Net negative effect
\end{itemize}

The cage binds tightest in capital-intensive industries (mobility, hardware, biotech), high-uncertainty environments (nascent markets, regulatory flux), and among first-time founders (who lack credibility for flexibility).

\textbf{Actionable Implications:}

\begin{enumerate}
\def\labelenumi{\arabic{enumi}.}
\item
  \textbf{For Founders:} If you operate in a capital-intensive sector or face high uncertainty, consider non-dilutive funding (grants, strategic partnerships) before seeking equity investment. Each funding round narrows your governance diversity.
\item
  \textbf{For Investors:} The 2.60\ensuremath{\times} Mover Advantage suggests that portfolio value may increase by backing founders who preserve repositioning capacity. Ask: "Who in your syndicate would advocate for pivoting if signals turn negative?"
\item
  \textbf{For Both:} Monitor repositioning patterns, not as failures of vision, but as signals of adaptive capacity. A founder who has never repositioned in three years is either perfectly calibrated or structurally caged.
\end{enumerate}

\emph{Section IV has demonstrated where the cage becomes lethal. Section V addresses how to design commitment structures that preserve adaptation capacity. See Appendix E for growth-by-direction visualization.}
