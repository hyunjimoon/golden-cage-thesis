---
modified:
  - 2026-01-15T09:00:00-05:00
version: claude_restructure_v1
---
\hypertarget{ch:theory}{%
\chapter{Theory}\label{ch:theory}}

\hypertarget{sec:ch2-introduction}{%
\section{Introduction}\label{sec:ch2-introduction}}

Strategic flexibility enables ventures to operationalize the Freedom Axiom \citep{stern2023}: the capacity to pursue the ``best available alternative'' requires maintaining multiple viable paths. New ventures possess this capacity naturally. Their ``blank slate'' status \citep{christensen1997innovators} permits strategic repositioning unconstrained by legacy commitments. Yet the funding process systematically \textbf{erodes} this flexibility precisely when ventures need it most to navigate uncertainty---a paradox this chapter resolves.

\textbf{The Funding-Growth Paradox.} Funding correlates negatively with later-stage success ($\rho = -0.196$, $p < 0.001$). This paradox resolves through mediation: funding suppresses repositioning (\S\ref{sec:commitment-cage}), yet repositioning drives success (\S\ref{sec:flexibility-flex}). The product of a negative and a positive is negative.

\textbf{Key Definitions.} I define \emph{strategic flexibility} ($F$) as the latent capacity to keep multiple paths viable under uncertainty. Because $F$ is not directly observable, the empirical chapters proxy it with \textbf{repositioning} ($R$): observable changes in strategic breadth over time (Chapter~\ref{ch:data}). Throughout, $F$ denotes latent flexibility; $R$ denotes its behavioral manifestation.

\textbf{The Core Asymmetry.} Traditional operations management views flexibility as a purchased asset \citep{jordan1995principles}. Venture governance presents a fundamental asymmetry: capital does not ``buy'' flexibility; it often \textbf{erodes} it. As founders trade equity for resources, they import a governance sorting effect that homogenizes beliefs. Unlike a machine that remains flexible regardless of usage, a board loses its capacity to advocate for alternatives as it becomes populated solely by believers.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.5\textwidth]{img/Ch2_Fig1_full_puzzle.png}
\caption{The Full Puzzle (Preview). Causal structure: $C \rightarrow E \rightarrow F \rightarrow G$. Gray nodes indicate components detailed in \S\ref{sec:commitment-cage}--\ref{sec:conclusion-hypotheses}.}
\label{fig:full-puzzle}
\end{figure}

\textbf{Chapter Roadmap.} Section~\ref{sec:commitment-cage} develops the \emph{Commitment Cage}: how funding suppresses flexibility through belief homogenization (H1: $dF/dE < 0$). Section~\ref{sec:flexibility-flex} establishes the \emph{Flexibility Flex}: why flexibility enables growth (H2: $dG/dF > 0$). Section~\ref{sec:conclusion-hypotheses} synthesizes these into testable hypotheses, showing that the Funding-Growth Paradox (H3) emerges as their product.

%% ============================================================
\hypertarget{sec:commitment-cage}{%
\section{Commitment Cage}\label{sec:commitment-cage}}

This section explains \textbf{how funding suppresses flexibility}. The mechanism operates through belief-based sorting: funding requires commitment, commitment attracts believers, and believers filter out skeptics. The result is governance homogeneity that prevents learning.

\subsection{Commitment as Double-Edged Sword}

Strategy orthodoxy favors commitment. \citet{porter1996what} argues that competitive advantage requires choosing a unique position and making trade-offs that competitors cannot easily imitate. \citet{ghemawat1991commitment} provides the definitive treatment: commitment creates value through four mechanisms---lock-in (sunk costs), lock-out (competitor exclusion), lags (time advantages), and inertia (organizational momentum). The prescription follows: choose a defensible position, then commit.

But Ghemawat also identifies the flip side: commitment forecloses alternatives. Every dollar sunk into battery-swapping infrastructure is a dollar unavailable for charging infrastructure. Every milestone promised to investors is a constraint on strategic pivots. Commitment is a double-edged sword---valuable for credibility, costly for flexibility.

The tension intensifies in nascent markets. Under technological and demand uncertainty, commitment becomes a bet on incomplete information. \citet{dixit1994investment} formalize this through real options reasoning: when uncertainty is high ($\sigma\uparrow$), waiting becomes more valuable because the option to learn dominates the benefit of early commitment. \citet{sanchez1995strategic} extends this to strategic flexibility: firms facing environmental uncertainty should maintain the capacity to respond to unforeseen contingencies.

\subsection{The Four-Step Cage Formation}

The \emph{golden cage} forms through a four-step sequence. The mechanism builds on a key insight: confident founders attract like-minded investors, producing belief homogeneity without any party behaving irrationally.

\textbf{Step 1: Commitment Attracts Believers.} Securing capital requires operational commitments---production architecture choices, go-to-market sequences, milestone definitions \citep{gompers2001the, hellmann2002venture}. Investors who fund a venture believe these specific commitments will succeed.

\textbf{Step 2: Believers Filter Skeptics.} People with different beliefs naturally sort into different organizations: optimists join ventures led by optimists, while skeptics stay away. \citeauthor{vandensteen2010interpersonal}'s \citeyearpar{vandensteen2010interpersonal} sorting equilibrium formalizes this: entrepreneurs who pursue a venture are more optimistic about it (selection, not bias), and investors who fund also share this optimism because pessimists self-select out. The result is belief homogeneity without any party behaving irrationally. The board contains no skeptics---not because skeptics were expelled, but because they never joined.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.45\textwidth]{img/Ch2_Fig2_commitment_cage.png}
\caption{Commitment Cage (Tile 1). The $C \rightarrow E \rightarrow F$ path: funding suppresses flexibility. H1: $\rho(E,F) < 0$.}
\label{fig:commitment-cage}
\end{figure}

\textbf{Step 3: Homogeneity Eliminates Signals.} Without skeptics, disconfirming signals lack advocates \citep{cyert1963a}. Market feedback indicating problems with the committed approach has no champion in governance discussions. \citet{march1991exploration} identifies this tension: belief convergence is efficient for exploitation (executing a known strategy) but destructive for exploration (discovering whether the strategy is correct).

\textbf{Step 4: Signal Loss Prevents Learning.} The venture cannot recognize when it should pivot. Learning stops---not because founders lack motivation, but because the structure prevents it. The cage is structural: founders want to pivot but lack governance support.

\subsection{Hypothesis 1: The Commitment Cage}

From this mechanism, I derive:

\textbf{Hypothesis 1 (Commitment Cage):} \emph{Early-stage funding correlates negatively with repositioning.}

\[H_1: \frac{dR}{dE} < 0\]

The empirical test appears in Chapter~\ref{ch:results}, Section~\ref{sec:h2-commitment-cage}. Preview: $\rho(E,R) = -0.087^{***}$ ($N = 180{,}994$).

%% ============================================================
\hypertarget{sec:flexibility-flex}{%
\section{Flexibility Flex}\label{sec:flexibility-flex}}

This section explains \textbf{why flexibility enables growth}. While Section~\ref{sec:commitment-cage} established that funding suppresses flexibility, this section establishes that flexibility matters: ventures that reposition outperform those that do not.

\subsection{Strategic Ambiguity as Flexibility Enabler}

\citeauthor{eisenberg1984ambiguity}'s \citeyearpar{eisenberg1984ambiguity} ``strategic ambiguity'' functions as a \textbf{stochastic enabler} of flexibility. Founders who orchestrate ambiguous positioning attract diverse stakeholders who project their own interpretations onto capacious visions. This diversity unlocks future pivot capacity: when market signals suggest changing direction, at least some governance voices advocate for the alternative.

Tesla's ``accelerating sustainable transport'' attracted believers in electrification, autonomy, and energy transition---each projecting their thesis onto the same vision. This coalition diversity preserved Tesla's capacity to pivot across segments (Roadster $\rightarrow$ Model S $\rightarrow$ Model 3) without losing governance support. In contrast, Better Place's commitment to ``battery swapping infrastructure'' attracted only believers in that specific mechanism. When market feedback favored charging over swapping, no governance voice advocated pivoting.

\subsection{The Causal Chain}

The complete causal chain is:

\[C \rightarrow E \rightarrow F\downarrow \rightarrow R\downarrow \rightarrow G\downarrow\]

Where $C$ = Commitment, $E$ = Early funding, $F$ = Flexibility (latent), $R$ = Repositioning (observed), $G$ = Growth. The arrows $C \rightarrow E$ (commitment attracts capital) and $E \rightarrow F$ (funding reduces flexibility) derive from Section~\ref{sec:commitment-cage}. This section establishes $F \rightarrow G$: flexibility enables growth.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.45\textwidth]{img/Ch2_Fig3_flexibility_flex.png}
\caption{Flexibility Flex (Tile 2). The $F \rightarrow G$ path: repositioning enables growth. H2: $\rho(F,G) > 0$.}
\label{fig:flexibility-flex}
\end{figure}

\subsection{Theorem 1: Caged Learning}

Building on \citeauthor{levinthal1993the}'s \citeyearpar{levinthal1993the} insight that successful organizations become ``myopic'' through competency traps, I formalize when learning ceases:

\textbf{Theorem 1 (Caged Learning).} \emph{Learning ceases when}

\[\mu(1 - \mu) < \frac{\varepsilon}{B}\]

\emph{where $\mu$ = belief probability, $\varepsilon$ = expected belief shift from a signal, and $B$ = strategic breadth. (Proof: Appendix~\ref{app:b}.)}

Van den Steen's sorting equilibrium produces high $\mu$ (shared optimism); operational commitments narrow $B$ (strategic focus). Both forces push the inequality toward satisfaction---caged learning becomes \emph{endogenous} to the funding process itself.

\subsection{Hypothesis 2: The Flexibility Flex}

From this analysis, I derive:

\textbf{Hypothesis 2 (Flexibility Flex):} \emph{Strategic repositioning correlates positively with later-stage success.}

\[H_2: \frac{dL}{dR} > 0\]

where $L$ denotes binary success (reaching Later Stage VC). The empirical test appears in Chapter~\ref{ch:results}, Section~\ref{sec:h3-flexibility-flex}. Preview: Movers outperform Stayers by $2.60\times$ ($P(L=1)$: 18.1\% vs.\ 7.0\%).

%% ============================================================
\hypertarget{sec:conclusion-hypotheses}{%
\section{Conclusion: Hypotheses}\label{sec:conclusion-hypotheses}}

The preceding sections established two relationships:
\begin{itemize}
\item \textbf{H1 (Commitment Cage):} $dR/dE < 0$ --- funding suppresses repositioning
\item \textbf{H2 (Flexibility Flex):} $dL/dR > 0$ --- repositioning enables success
\end{itemize}

\subsection{The Funding-Growth Paradox (H3)}

Together, these hypotheses explain the Funding-Growth Paradox:

\textbf{Hypothesis 3 (Funding-Growth Paradox):} \emph{Early-stage funding correlates negatively with later-stage growth.}

\[H_3: \frac{dG}{dE} < 0\]

The decomposition makes the paradox transparent:

\[\frac{dG}{dE} = \underbrace{\frac{dL}{dR}}_{\text{H2: }(+)} \times \underbrace{\frac{dR}{dE}}_{\text{H1: }(-)} = (+) \times (-) = (-)\]

Funding suppresses the very mechanism (repositioning) required for survival. The paradox is not that capital is harmful, but that the governance structures attached to capital constrain adaptation.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.45\textwidth]{img/Ch2_Fig4_paradox.png}
\caption{The Paradox (Tile 3). The net effect $E \rightarrow G$: H3 $=$ H1 $\times$ H2 $= (-) \times (+) = (-)$. The Funding-Growth Paradox emerges from the product.}
\label{fig:paradox}
\end{figure}

\subsection{Complete Model}

Figure~\ref{fig:complete-model} integrates all three hypotheses into the complete theoretical model.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.65\textwidth]{img/Ch2_Fig5_complete_model.png}
\caption{Complete Model. The Golden Cage mechanism: $C \rightarrow E \rightarrow F\downarrow \rightarrow R\downarrow \rightarrow G\downarrow$. Red path (H1): Commitment Cage. Blue path (H2): Flexibility Flex. Dashed path (H3): Net paradox.}
\label{fig:complete-model}
\end{figure}

\subsection{Structural vs.\ Motivational Constraint}

A key distinction: I argue founders \emph{cannot} pivot (structural constraint), not that they \emph{will not} pivot (moral hazard). This distinction has implications for intervention design. If founders will not pivot due to reduced incentives, the prescription is intensified monitoring. If founders cannot pivot due to structural constraints (the cage), the prescription is governance redesign---preserving skeptical voices before funding eliminates them.

\subsection{Preview of Empirical Tests}

Chapters~\ref{ch:data}--\ref{ch:results} test these hypotheses using 180,994 ventures from PitchBook (2021--2025):

\begin{itemize}
\item \textbf{H1 (Commitment Cage):} $\rho(E,R) = -0.087^{***}$ --- confirmed
\item \textbf{H2 (Flexibility Flex):} Mover advantage $= 2.60\times$ --- confirmed
\item \textbf{H3 (Funding-Growth Paradox):} $\rho(E,G) = -0.196^{***}$ --- confirmed
\end{itemize}

Industry heterogeneity reveals boundary conditions: the cage binds tightest in capital-intensive sectors (Hardware: $\rho = -0.108$, Transportation: $\rho = -0.101$) but releases under extreme uncertainty (Quantum: $\rho = +0.095$).
