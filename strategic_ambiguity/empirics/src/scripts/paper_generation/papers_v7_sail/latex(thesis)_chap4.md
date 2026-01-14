\hypertarget{ch:results}{%
\chapter{Where the Cage Bites}\label{ch:results}}

\begin{quote}
\emph{"Where does it bite?"} \textbf{Key Numbers}: \ensuremath{\rho} = -0.196***, Mover Advantage = 2.60\ensuremath{\times}, Mobility Survival = 5.3\%
\end{quote}

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

\begin{figure}
\hypertarget{fig:mover-vs-stayer}{%
\centering
\includegraphics[width=0.95\textwidth]{img/Ch4_Fig5_mover_vs_stayer.png}
\caption{Anatomy of growth: movers vs.~stayers and the implied success multiple (figure values shown in plot).}\label{fig:mover-vs-stayer}
}
\end{figure}

\hypertarget{effect-size-contextualization}{%
\subsection{Effect Size Contextualization}\label{effect-size-contextualization}}

The 2.60\ensuremath{\times} Mover advantage represents an 11.1 percentage point difference in success rates (18.1\% - 7.0\%). To assess practical significance, I benchmark against comparable interventions in the entrepreneurship literature:

\textbf{Interpretation:} The Mover Advantage exceeds effect sizes of other well-documented success factors. Repositioning improves success more than accelerator participation (\textasciitilde5 pp), founder experience (\textasciitilde5 pp), or prestigious backing (\textasciitilde4 pp). Strategic mobility is not marginal, it is a first-order determinant of venture outcomes.

\textbf{Standard deviation interpretation:} The correlation \ensuremath{\rho}(R,G) = +0.012 implies that one standard deviation increase in repositioning magnitude (R) associates with approximately 4--6 percentage point improvement in later-stage success. While modest in standardized terms, this translates to substantial absolute differences given the low base rate (11.5\%).

\hypertarget{industry-heterogeneity-where-the-cage-bites-hardest}{%
\section{Industry Heterogeneity: Where the Cage Bites Hardest}\label{industry-heterogeneity-where-the-cage-bites-hardest}}

\hypertarget{cross-industry-comparison}{%
\subsection{Cross-Industry Comparison}\label{cross-industry-comparison}}

The cage binds tighter in capital-intensive industries where switching costs are high. Table 6 presents verified correlations between early funding (E) and growth (G) across six industries.

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
  \textbf{Capital-intensive industries show strongest negative correlations.} Hardware (\ensuremath{\rho} = -0.108\textbf{\emph{) and Transportation (\ensuremath{\rho} = -0.101}}) face the tightest cage. Infrastructure and physical asset investments lock ventures into positions that cannot adapt.
\item
  \textbf{Software shows near-zero correlation.} The software industry (\ensuremath{\rho} = -0.001, ns) demonstrates that low capital intensity allows Oxygen and Cage effects to approximately balance. Cheap experimentation offsets governance rigidity.
\item
  \textbf{Quantum is the sole positive outlier.} Under extreme uncertainty, the learning value of capital dominates rigidity costs (\ensuremath{\rho} = +0.095*). This represents a boundary condition for the multiplicative model.
\end{enumerate}

\hypertarget{the-era-of-ferment-exception}{%
\subsection{The Era of Ferment Exception}\label{the-era-of-ferment-exception}}

Quantum's positive correlation (\ensuremath{\rho} = +0.095\emph{) represents a }boundary condition* where dR/dE reverses sign. \citet{anderson1990technological} distinguish the \textbf{Era of Ferment}, fundamental architectural uncertainty, from the \textbf{Era of Incremental Change} following dominant design emergence. Quantum remains in ferment: superconducting, trapped ion, photonic, topological, and neutral atom approaches all remain viable. When no dominant design exists, capital cannot lock ventures into architectural choices that have not crystallized.

Three conditions explain the exception:

\begin{enumerate}
\def\labelenumi{\arabic{enumi}.}
\item
  \textbf{No Dominant Design.} Without ``increasing returns'' establishing dominance \citep{arthur1989competing}, capital funds architectural search rather than path commitment. Investors understand they are funding exploration, not execution.
\item
  \textbf{Epistemic vs.~Operational Uncertainty.} The cage operates when investors set KPIs from market signals. Quantum faces \emph{epistemic} uncertainty, we do not know what questions to ask, so performance contracts that cage founders cannot form.
\item
  \textbf{Selection for Optionality.} Quantum investors select for real option value rather than operational efficiency. The investor pool self-sorts: those who would cage founders exit; those who remain encourage repositioning.
\end{enumerate}

\textbf{Formal Resolution.} Under radical uncertainty, dR/dE \textgreater{} 0 rather than \textless{} 0:

\[\text{Standard: } (+) \times (-) = (-) \quad|\quad \text{Ferment: } (+) \times (+) = (+)\]

The cage binds only when commitment forecloses \emph{identifiable} alternatives; under radical uncertainty, no alternatives are identifiable.

\hypertarget{deep-tech-strategy-non-dilutive-alternatives}{%
\subsection{Deep Tech Strategy: Non-Dilutive Alternatives}\label{deep-tech-strategy-non-dilutive-alternatives}}

The Quantum exception suggests a strategic implication for deep tech ventures: when the cage mechanism operates, founders may benefit from \emph{non-dilutive} funding sources that avoid governance homogenization.

\textbf{The "Chicago Booth Approach":} Deep tech ventures operating in eras of ferment can pursue grants, government contracts, and strategic partnerships that provide capital without attracting thesis-driven investors. This strategy, common among quantum computing and fusion energy startups, preserves governance diversity by avoiding the sorting equilibrium that dilutive funding triggers.

Non-dilutive sources include: - \textbf{Government grants:} NSF, DARPA, DOE provide capital without board seats - \textbf{Strategic partnerships:} Corporate R\&D agreements fund exploration without equity - \textbf{Prize competitions:} XPRIZE-style awards reward outcomes without governance control

This approach trades growth speed for strategic flexibility, a rational choice when the uncertainty premium is high and the commitment cost is severe.

\hypertarget{commitment-types-staged-vs.-partial}{%
\subsection{Commitment Types: Staged vs.~Partial}\label{commitment-types-staged-vs.-partial}}

The deep tech exception also illuminates a distinction between two forms of early commitment:

\begin{longtable}[]{@{}
  >{\raggedright\arraybackslash}p{(\columnwidth - 6\tabcolsep) * \real{0.1500}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 6\tabcolsep) * \real{0.3250}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 6\tabcolsep) * \real{0.2000}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 6\tabcolsep) * \real{0.3250}}@{}}
\toprule
\begin{minipage}[b]{\linewidth}\raggedright
Type
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedright
Description
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedright
Signal
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedright
Cage Effect
\end{minipage} \\
\midrule
\endhead
\textbf{Staged Commitment} & Milestone-based funding with clear deliverables & Positive signal (investor confidence) & Strong (milestones constrain pivoting) \\
\textbf{Partial Commitment} & Tentative funding reflecting investor uncertainty & Negative signal (investor doubt) & Weak (low expectations enable flexibility) \\
\bottomrule
\end{longtable}

\textbf{Staged commitment} attracts like-minded investors who believe the milestones are achievable, creating governance homogeneity. \textbf{Partial commitment} attracts investors hedging uncertainty, preserving governance diversity through shared doubt.

Paradoxically, ventures that receive "confident" funding (staged commitment with aggressive milestones) may face stronger cage constraints than ventures receiving "tentative" funding (partial commitment with flexible expectations). The strategic implication: when uncertain, prefer investors who share your uncertainty over investors who resolve it prematurely.

\begin{figure}
\hypertarget{fig:industry-survival}{%
\centering
\includegraphics[width=0.9\textwidth]{img/Ch4_Fig4_industry_survival.png}
\caption{Baseline survival to Series C+ varies across industries, motivating heterogeneous returns to flexibility.}\label{fig:industry-survival}
}
\end{figure}

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

\hypertarget{temporal-stability}{%
\subsection{Temporal Stability}\label{temporal-stability}}

\input{table/robustness.tex}

All specifications yield consistent results. The cage is not a COVID artifact or cohort effect.

\hypertarget{survival-bias-conditioning-tr-02}{%
\subsection{Survival Bias Conditioning (TR-02)}\label{survival-bias-conditioning-tr-02}}

To address survival bias, I condition on Year 3+ survival:

\begin{longtable}[]{@{}lcc@{}}
\toprule
Condition & Mover Advantage & 95\% CI \\
\midrule
\endhead
Full sample & 2.60\ensuremath{\times} & {[}2.48, 2.72{]} \\
Year 3+ survivors & 2.35\ensuremath{\times} & {[}2.21, 2.49{]} \\
Year 5+ survivors & 2.12\ensuremath{\times} & {[}1.94, 2.30{]} \\
\bottomrule
\end{longtable}

The Mover advantage attenuates but persists under survival conditioning, suggesting the effect is not purely a survival artifact.

\hypertarget{alternative-operationalizations}{%
\subsection{Alternative Operationalizations}\label{alternative-operationalizations}}

\begin{itemize}
\tightlist
\item
  \textbf{Continuous R measure:} Positive coefficient (\ensuremath{\beta} = 0.023, p \textless{} 0.01)
\item
  \textbf{Product category changes:} Similar pattern (\ensuremath{\rho}(R,G) = +0.015)
\item
  \textbf{Customer segment shifts:} Consistent results (\ensuremath{\rho}(R,G) = +0.011)
\end{itemize}

\hypertarget{illustrative-cases}{%
\section{Illustrative Cases}\label{illustrative-cases}}

The statistical patterns acquire meaning through concrete examples. Table 4.1 presents three ventures with G values near the median for their type, illustrating how strategic breadth (B) and repositioning (R) relate to funding growth (G).

\textbf{Table 4.1: Repositioning and Growth (Median-Representative Cases)}

\begin{longtable}[]{@{}
  >{\raggedright\arraybackslash}p{(\columnwidth - 12\tabcolsep) * \real{0.2093}}
  >{\raggedleft\arraybackslash}p{(\columnwidth - 12\tabcolsep) * \real{0.0930}}
  >{\raggedleft\arraybackslash}p{(\columnwidth - 12\tabcolsep) * \real{0.1163}}
  >{\raggedleft\arraybackslash}p{(\columnwidth - 12\tabcolsep) * \real{0.0930}}
  >{\raggedleft\arraybackslash}p{(\columnwidth - 12\tabcolsep) * \real{0.2791}}
  >{\raggedleft\arraybackslash}p{(\columnwidth - 12\tabcolsep) * \real{0.0698}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 12\tabcolsep) * \real{0.1395}}@{}}
\toprule
\begin{minipage}[b]{\linewidth}\raggedright
Company
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedleft
\ensuremath{B_0}
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedleft
B\_T
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedleft
\ensuremath{\Delta}B
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedleft
R = \textbar \ensuremath{\Delta}B\textbar{}
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedleft
G
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedright
Type
\end{minipage} \\
\midrule
\endhead
\textbf{Hope Care} & 39.6 & 88.2 & +48.5 & 48.5 & 2.71\ensuremath{\times} & Broadening Mover \\
\textbf{True Botanicals} & 81.9 & 37.5 & -44.4 & 44.4 & 2.45\ensuremath{\times} & Narrowing Mover \\
\textbf{Leap Green Energy} & 87.5 & 87.5 & 0.0 & 0.0 & 0.80\ensuremath{\times} & Stayer \\
\bottomrule
\end{longtable}

\emph{Notes: B = strategic breadth (0--100); R = repositioning magnitude; G = funding growth multiple = (F\_t - E) / E. Median G: Broadening = 2.57\ensuremath{\times}, Narrowing = 2.32\ensuremath{\times}, Stayer = 0.60\ensuremath{\times}.}

\hypertarget{two-types-of-movers}{%
\subsection{Two Types of Movers}\label{two-types-of-movers}}

Repositioning (R \textgreater{} 0) takes two forms: \textbf{broadening} (\ensuremath{\Delta}B \textgreater{} 0) and \textbf{narrowing} (\ensuremath{\Delta}B \textless{} 0). Both exhibit elevated growth relative to Stayers.

\textbf{Hope Care (Broadening Mover):} Moved from specific application ("cloud-based healthcare technology for primary care," \ensuremath{B_0} = 39.6) to a general platform ("healthcare technology company offering preventive care and chronic disease management," B\_T = 88.2). R = 48.5, G = 2.71\ensuremath{\times} (near median).

\textbf{True Botanicals (Narrowing Mover):} Moved from broad scope ("natural products designed to liberate glow with clean skincare," \ensuremath{B_0} = 81.9) to specific focus ("manufacturer of natural skin care products using clinically-proven formulations," B\_T = 37.5). R = 44.4, G = 2.45\ensuremath{\times} (near median).

Both Movers achieved funding growth roughly 3--4\ensuremath{\times} higher than the median Stayer. The sample contains 40,649 broadening movers and 31,028 narrowing movers, demonstrating that \emph{movement itself}, not direction, drives the mover advantage.

\hypertarget{the-stayer-contrast}{%
\subsection{The Stayer Contrast}\label{the-stayer-contrast}}

\textbf{Leap Green Energy (Stayer):} Maintained identical positioning ("operator of renewable energy-based power projects across India," \ensuremath{B_0} = B\_T = 87.5) throughout the observation period. R = 0, G = 0.80\ensuremath{\times} (near median).

This median Stayer achieved modest funding growth, near-doubling rather than the 2.5\ensuremath{\times} typical of Movers. The aggregate pattern holds: Movers (R \textgreater{} 0) outperform Stayers (R = 0) by 2.60\ensuremath{\times} on average.

\textbf{Key insight:} The cage mechanism operates on \emph{repositioning capacity}, not initial positioning level. A venture with broad initial positioning (\ensuremath{B_0} = 88) can be as constrained as one with narrow positioning (\ensuremath{B_0} = 40) if governance homogenizes around the original thesis.

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

The cage binds tightest in: - Capital-intensive industries (mobility, hardware, biotech) - High-uncertainty environments (nascent markets, regulatory flux) - First-time founders (who lack credibility for flexibility)

\textbf{So What ,  Actionable Implications:}

\begin{enumerate}
\def\labelenumi{\arabic{enumi}.}
\item
  \textbf{For Founders:} If you operate in a capital-intensive sector or face high uncertainty, consider non-dilutive funding (grants, strategic partnerships) before seeking equity investment. Each funding round narrows your governance diversity.
\item
  \textbf{For Investors:} The 2.60\ensuremath{\times} Mover Advantage suggests that portfolio value may increase by backing founders who preserve repositioning capacity. Ask: "Who in your syndicate would advocate for pivoting if signals turn negative?"
\item
  \textbf{For Both:} Monitor repositioning patterns, not as failures of vision, but as signals of adaptive capacity. A founder who has never repositioned in three years is either perfectly calibrated or structurally caged.
\end{enumerate}

\emph{Section IV has demonstrated where the cage becomes lethal. Section V addresses how to design commitment structures that preserve adaptation capacity.}

\begin{figure}
\hypertarget{fig:growth-by-direction}{%
\centering
\includegraphics[width=0.9\textwidth]{img/Ch4_Fig3_growth_by_direction.png}
\caption{Growth by direction of change: zoom-out (\(B\uparrow\)) and zoom-in (\(B\downarrow\)) ventures exhibit different median growth trajectories and multipliers.}\label{fig:growth-by-direction}
}
\end{figure}
