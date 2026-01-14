\hypertarget{ch:mechanism}{%
\chapter{The Golden Cage Mechanism}\label{ch:mechanism}}

\begin{quote}
\emph{"Why does it happen?"} \textbf{Key Insight}: Founders \emph{cannot} pivot, not that they \emph{will not}, because governance lacks advocates for alternatives.
\end{quote}

\hypertarget{introduction}{%
\section{Introduction}\label{introduction}}

Strategic flexibility enables ventures to operationalize the Freedom Axiom \citep{stern2023}: the capacity to pursue the ``best available alternative'' requires maintaining multiple viable paths. New ventures possess this capacity naturally---their ``blank slate'' status \citep{christensen1997innovators} permits strategic repositioning unconstrained by legacy commitments. Yet the funding process systematically \textbf{erodes} this flexibility precisely when ventures need it most to navigate uncertainty---a paradox this chapter resolves.

\textbf{Flexibility as Latent Capability.} I define strategic flexibility as the \textbf{latent capability} to pursue multiple paths within constrained resource spaces. This capability remains unobserved directly; I proxy it through \textbf{repositioning}---the observable behavioral manifestation of latent flexibility. Ventures that reposition demonstrate they possessed flexibility; those that remain static may lack the capability or choose not to exercise it. Critically, the data reveal that staying is rarely strategic: \textbf{Movers outperform Stayers by 2.60\ensuremath{\times}} (18.1\% vs.~7.0\% later-stage success, p < 0.001). This suggests that in early-stage ventures, lack of movement predominantly signals rigidity rather than perfection.

\textbf{The Funding-Growth Paradox.} Funding correlates negatively with growth (\ensuremath{\rho} = -0.196, p < 0.001). The paradox resolves through decomposition:

\begin{equation}
\frac{dG}{dE} = \underbrace{\frac{dG}{dR}}_{\text{Flexibility Premium }(+)} \times \underbrace{\frac{dR}{dE}}_{\text{Commitment Trap }(-)} = (+) \times (-) = (-)
\end{equation}

Funding \textbf{erodes} flexibility precisely when ventures need it most. \citet{camuffo2020a} document that scientific experimentation improves pivot quality, yet securing capital to fund experimentation requires commitments that attract homogeneous believers. The paradox is structural: acquiring resources to learn reduces the governance diversity necessary to act on learning.

\textbf{Why Compare Manufacturing and Ventures?} The concept of strategic flexibility originates in manufacturing, where \citet{jordan1995principles} demonstrated that process flexibility hedges against demand uncertainty. I import this concept to venture governance---but the \textbf{mechanism} differs fundamentally. Understanding this difference clarifies why funding can erode flexibility in ventures while enhancing it in manufacturing.

\begin{longtable}[]{@{}
  >{\raggedright\arraybackslash}p{0.22\columnwidth}
  >{\raggedright\arraybackslash}p{0.35\columnwidth}
  >{\raggedright\arraybackslash}p{0.35\columnwidth}@{}}
\toprule
\textbf{Dimension} & \textbf{Manufacturing} & \textbf{Ventures} \\
\midrule
\endhead
Execution Agent & Central planner (deterministic) & Distributed governance (stochastic) \\
Flexibility Creation & Equipment investment & Strategic ambiguity \\
Configuration Mode & Ex-ante design & Emergent through selection \\
Adaptation Trigger & Demand signal (automatic) & Market feedback + \textbf{governance advocacy} \\
\bottomrule
\end{longtable}

\textbf{Table 2.0: Manufacturing vs.~Venture Flexibility.} The critical difference lies in the adaptation trigger. In manufacturing, sensors detect demand shifts and systems adjust automatically. In ventures, adaptation requires \textbf{political consensus}---the board must advocate for change. This ``governance friction'' is the cage's essence: founders cannot pivot without board support, and homogeneous boards lack advocates for alternatives.

\textbf{The Core Asymmetry.} In manufacturing, capital \textbf{buys} flexibility (more equipment investment = more production options). In ventures, capital can \textbf{erode} flexibility (more funding = more governance homogeneity = fewer pivot advocates). This asymmetry explains the Funding-Growth Paradox.

\textbf{Figure 3a: Process Flexibility vs.~Venture Flexibility.} Governance composition \textbf{mediates} flexibility emergence. In manufacturing, central planners configure flexibility deterministically through equipment investment. In ventures, flexibility emerges stochastically through the sorting process that determines who joins governance. The board's belief distribution---not the founder's intention---determines which pivots receive advocacy when market signals arrive.

\citeauthor{eisenberg1984ambiguity}'s \citeyearpar{eisenberg1984ambiguity} ``strategic ambiguity'' functions as a \textbf{stochastic enabler} of flexibility. Founders who \textbf{orchestrate} ambiguous positioning attract diverse stakeholders who project their own interpretations onto capacious visions. This diversity \textbf{unlocks} future pivot capacity: when market signals suggest changing direction, at least some governance voices advocate for the alternative. Strategic ambiguity does not guarantee flexibility---it increases the \emph{probability} that flexibility survives the funding process.

\begin{longtable}[]{@{}
  >{\raggedright\arraybackslash}p{(\columnwidth - 6\tabcolsep) * \real{0.1351}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 6\tabcolsep) * \real{0.2568}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 6\tabcolsep) * \real{0.3108}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 6\tabcolsep) * \real{0.2973}}@{}}
\toprule
\begin{minipage}[b]{\linewidth}\raggedright
Industry
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedright
Example Platforms
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedright
Flexibility Mechanism
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedright
Constraint Mechanism
\end{minipage} \\
\midrule
\endhead
Mobility & Tesla, Better Place & Vision vs.~operational commitment & Board composition \\
Software & Slack, Flickr & Product pivot capacity & Investor thesis alignment \\
Hardware & Nest, Dropcam & Technology redeployment & Sunk cost in manufacturing \\
\bottomrule
\end{longtable}

\textbf{Table 2.1: Examples of ventures that face flexibility constraints through governance.} These constraints arise when operational commitments attract like-minded investors who filter skeptics from governance.

The examples illustrate that flexibility constraints can simultaneously arise from multiple sources, which raises the question of how governance composition interacts with commitment type. Specifically, what commitment structure is best for survival? Is it more effective to commit at the vision level (preserving pivot options), or is it better to commit at the operational level (attracting aligned investors)? Despite the significant capital through which founders make commitments on both technology and market sides, the interaction of commitment type and governance composition is not well-understood. Indeed, we know of no work in the literature that examines the interaction of these two flexibility mechanisms in venture governance. And, in practice, founders usually make commitment decisions without visibility into how those commitments shape board composition, a one-sided approach that neither reveals nor exploits the interaction of different flexibility levers, and we will show that it can come at a great cost.

This chapter studies how funding creates a \emph{golden cage}, a structural trap that prevents founders from adapting, no matter how much they want to. We focus on governance, not moral hazard or resource constraints, and on how they interact. Table 2.1 shows that governance-based flexibility constraints arise in many settings, so we highlight general effects relevant to any venture. We develop a simple model showing how commitment type shapes who joins the board. Specific commitments (operational) attract narrow coalitions; vague commitments (vision-level) attract diverse coalitions. The venture maximizes survival, which depends on both resources and pivot capacity. We study how founders should structure commitment, and when they should commit at the vision versus operational level.

Our results show that the choice of commitment level has a significant impact on venture survival. Even with fixed commitment credibility, the pivot capacity (and consequently the survival probability) can vary significantly depending on how commitment is structured (see Figure 3). Moreover, by comparing two natural commitment strategies: (1) the operational commitment, which specifies technology and market, and (2) the vision commitment, which specifies direction but not destination, we find that either strategy can improve survival by more than 2\ensuremath{\times} compared to the other, depending on industry and stage. Hence, founders who optimize their commitment level but not its structure may pay a high price.

Despite the impact of commitment structure, optimizing it poses nontrivial difficulties. Even in a simple and symmetric governance model, the geometry of pivot capacity (as a function of commitment structure) reveals traps in which a venture might get stuck. In particular, the current practice of many founders, wherein commitments are made to secure near-term funding without considering long-term governance implications, might converge to such traps. Near these traps, founders mistakenly perceive themselves to be optimally positioned, as commitment should neither be increased nor decreased; however, the venture would benefit from restructuring commitment from operational to vision level or vice versa. These structural insights are unique to our study of commitment-governance interaction, and our empirical results show that they generalize beyond our particular model.

\hypertarget{contributions}{%
\subsection{Contributions}\label{contributions}}

This chapter examines how commitment shapes governance. I characterize how funding constrains flexibility and identify optimal commitment structures.

\textbf{Optimal commitment structures.} Either vision-level or operational commitment can dominate the other. Sections 2.3 and 2.4 introduce two key effects: \emph{belief homogenization} and \emph{signal diversity loss}. Belief homogenization follows from operational commitment. Specific commitments attract like-minded investors, so governance diversity falls while shared conviction rises. But this conviction becomes wasteful when the committed direction proves wrong. Signal diversity loss arises under extreme operational commitment: board members who might champion alternatives never join governance. The venture ignores disconfirming signals and cannot recognize when it should pivot. Sections 2.3 and 2.4 characterize when these effects bind tightest; Section 2.5 identifies the dominant commitment structure across industry contexts.

\textbf{Synthesis of sorting and ambiguity theories.} Our main theoretical contribution: we synthesize \citeauthor{vandensteen2010interpersonal}'s \citeyearpar{vandensteen2010interpersonal} sorting equilibrium with \citeauthor{eisenberg1984ambiguity}'s \citeyearpar{eisenberg1984ambiguity} strategic ambiguity into a unified mechanism. Scholars have long struggled to characterize how commitment shapes governance. We develop three analytical approaches. Section 2.3 maps commitment type to governance composition and shows that belief homogenization lowers survival for operational commitment. Section 2.4 applies the flexibility premium analysis when strategic ambiguity produces high governance diversity. Section 2.5 formalizes Caged Learning (Theorem 1) to characterize when organizational learning ceases.

\textbf{Ruling out moral hazard.} The critical distinction is "cannot pivot" versus "will not pivot." If founders \emph{will not} pivot due to reduced incentives (moral hazard), the prescription is intensified monitoring. If founders \emph{cannot} pivot due to governance constraints (the cage), the prescription is governance redesign---preserving skeptical voices before funding eliminates them. My evidence favors the structural explanation.

\hypertarget{analytic-structure-patterns-vs.-mechanisms}{%
\subsection{Analytic Structure: Patterns vs.~Mechanisms}\label{analytic-structure-patterns-vs.-mechanisms}}

This thesis distinguishes between \textbf{observed correlational patterns} (measurable) and \textbf{theoretical mechanisms} (latent). The distinction is critical for interpreting the evidence and follows the Layers of Theoretical Explanation (LTE) framework developed by \citet{kozlowski2025advancing}, which identifies three levels of theoretical depth:

\begin{longtable}[]{@{}
  >{\centering\arraybackslash}p{(\columnwidth - 6\tabcolsep) * \real{0.1892}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 6\tabcolsep) * \real{0.2703}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 6\tabcolsep) * \real{0.1892}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 6\tabcolsep) * \real{0.3514}}@{}}
\toprule
\begin{minipage}[b]{\linewidth}\centering
Layer
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedright
Question
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedright
Focus
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedright
This Thesis
\end{minipage} \\
\midrule
\endhead
\textbf{Layer 1: Construct} & \emph{What} relationships exist? & Observable covariation & \ensuremath{\rho}(E,G) = -0.196, \ensuremath{\rho}(E,R) = -0.087, Mover Advantage = 2.60\ensuremath{\times} \\
\textbf{Layer 2: Process} & \emph{How} do actions unfold? & Action sequences in context & Commit \ensuremath{\rightarrow} Fund \ensuremath{\rightarrow} Filter \ensuremath{\rightarrow} Homogenize \ensuremath{\rightarrow} Cage \\
\textbf{Layer 3: Mechanism} & \emph{Why} do actors behave this way? & Generative drivers & \ensuremath{\mu}(1-\ensuremath{\mu}) \textless{} \ensuremath{\epsilon}/B (Theorem 1: Caged Learning) \\
\bottomrule
\end{longtable}

The LTE framework clarifies that construct-level findings (Layer 1) predict but do not explain. Layer 2 describes the \emph{sequence} through which the golden cage forms: operational commitment attracts like-minded investors, who filter skeptics from governance, producing belief homogeneity that eliminates learning capacity. Layer 3 specifies the \emph{generative mechanism} that drives this sequence: \citeauthor{vandensteen2010interpersonal}'s \citeyearpar{vandensteen2010interpersonal} sorting equilibrium produces high \ensuremath{\mu} (shared optimism), while operational commitment produces low B (narrow strategic breadth), satisfying the Caged Learning condition.

\textbf{Observed Patterns (Layer 1 ,  Measured Variables):} - \textbf{H1 (Commitment Trap):} \ensuremath{\rho}(Funding, Repositioning) \textless{} 0 ,  Funding suppresses repositioning - \textbf{H2 (Flexibility Premium):} \ensuremath{\rho}(Repositioning, Growth) \textgreater{} 0 ,  Repositioning enables growth - \textbf{H3 (Funding Paradox):} \ensuremath{\rho}(Funding, Growth) \textless{} 0 ,  Net negative effect (H1 \ensuremath{\times} H2)

\textbf{Process Sequence (Layer 2 ,  Action Flow):} - Commit \ensuremath{\rightarrow} Fund \ensuremath{\rightarrow} Filter \ensuremath{\rightarrow} Homogenize \ensuremath{\rightarrow} Signal Loss \ensuremath{\rightarrow} Cage

\textbf{Theoretical Mechanisms (Layer 3 ,  Generative Drivers):} - \textbf{CEF Mechanism:} Commitment \ensuremath{\rightarrow} Funding \ensuremath{\rightarrow} Flexibility\ensuremath{\downarrow} (how funding suppresses adaptation capacity) - \textbf{FG Mechanism:} Flexibility \ensuremath{\rightarrow} Growth (why adaptation capacity enables growth) - \textbf{Caged Learning:} \ensuremath{\mu}(1-\ensuremath{\mu}) \textless{} \ensuremath{\epsilon}/B formalizes when learning ceases endogenously

The patterns are directly testable from data. The mechanisms are theoretical constructs that \emph{explain} the patterns but require inference from observed variables. Specifically: - \textbf{Flexibility (F)} is latent; we proxy it through Repositioning (R) - \textbf{Commitment (C)} is latent; we proxy it through Strategic Breadth (B)

This chapter develops the theoretical mechanisms (Layers 2-3). Chapter 4 tests whether the observed patterns (Layer 1) are consistent with these mechanisms.

\hypertarget{related-work}{%
\subsection{Related Work}\label{related-work}}

\textbf{Commitment in strategy.} Commitment has a long history in strategy with early works focusing on the value of irreversible choices \citep{ghemawat1991commitment}. Most early works in this literature have focused on determining the optimal \emph{level} of commitment \citep{porter1996what, ghemawat1991commitment}, thus optimizing over a single dimension. In contrast, our decision also involves commitment \emph{structure}, vision versus operational. More importantly, we identify not just the optimal commitment level, but also structural properties that arise from the interplay of commitment type and governance composition and can cause potential pitfalls in practice.

In our focus on structural insights, our study relates more closely to those works in flexibility that aim to identify the optimal commitment \emph{design} rather than the optimal \emph{amount} of commitment. The seminal work of \citet{sanchez1995strategic} first introduced "strategic flexibility," which enables a small amount of uncommitted resources to yield almost all the benefits of a perfectly flexible system. Since then, a vast literature has studied commitment-flexibility trade-offs \citep{adner2004what, mcgrath1999falling, dixit1994investment}. A key distinction between our work and this stream lies in the \emph{structure} of our flexibility mechanism: as venture governance involves stochastically formed coalitions that connect founders with investors, we cannot model flexibility as a fixed strategic design. Instead, founders use commitment choices to shape the \emph{probability} of attracting diverse governance voices.

\textbf{Organizational learning.} Our work also relates to papers that study flexibility in organizational adaptation, though they focus on flexibility within a single organization. Prior works study exploration-exploitation trade-offs \citep{march1991exploration}, competency traps \citep{levinthal1993the}, and Bayesian entrepreneurship \citep{gans2019foundations}. More explicitly focused on venture adaptation, some works study pivoting \citep{ries2011the, camuffo2020a} and strategic experimentation \citep{kirtley2023what}. Our work differs from all of these in that we focus on the interplay of two different flexibility mechanisms, commitment structure and governance composition.

\textbf{Governance and venture capital.} A reasonable interpretation of our structural results is that founders are unlikely to find the optimal commitment structure if they optimize without considering governance implications (see Section 2.4). This relates to a stream of literature that identifies conflicts between founder and investor incentives \citep{jensen1976theory, hellmann2002venture}. There, ventures may face inefficiencies due to moral hazard. In our work, the inefficiency arises not from misaligned incentives but from \emph{structural constraints}, without governance diversity, founders cannot pivot even when they want to.

\hypertarget{commitment-as-double-edged-sword}{%
\section{Commitment as Double-Edged Sword}\label{commitment-as-double-edged-sword}}

Strategy orthodoxy favors commitment. \citet{porter1996what} argues that competitive advantage requires choosing a unique position and making trade-offs that competitors cannot easily imitate. \citet{ghemawat1991commitment} provides the definitive treatment: commitment creates value through four mechanisms, lock-in (sunk costs), lock-out (competitor exclusion), lags (time advantages), and inertia (organizational momentum). The prescription follows: choose a defensible position, then commit.

But Ghemawat also identifies the flip side: commitment forecloses alternatives. Every dollar sunk into battery-swapping infrastructure is a dollar unavailable for charging infrastructure. Every milestone promised to investors is a constraint on strategic pivots. Commitment is a double-edged sword, valuable for credibility, costly for flexibility.

The tension intensifies in nascent markets. Under technological and demand uncertainty, commitment becomes a bet on incomplete information. \citet{dixit1994investment} formalize this through real options reasoning: when uncertainty is high (\ensuremath{\sigma}\ensuremath{\uparrow}), waiting becomes more valuable because the option to learn dominates the benefit of early commitment. \citet{sanchez1995strategic} extends this to strategic flexibility: firms facing environmental uncertainty should maintain "strategic flexibility", the capacity to respond to unforeseen contingencies.

\hypertarget{the-golden-cage-mechanism}{%
\section{The Golden Cage Mechanism}\label{the-golden-cage-mechanism}}

The \emph{golden cage} forms through a four-step sequence. The mechanism builds on a key insight: confident founders attract like-minded investors, producing belief homogeneity without any party behaving irrationally.

\textbf{Step 1: Commitment Attracts Believers.} Securing capital requires operational commitments, production architecture choices, go-to-market sequences, milestone definitions \citep{gompers2001the, hellmann2002venture}. Investors who fund a venture believe these specific commitments will succeed.

\textbf{Step 2: Believers Filter Skeptics.} \citeauthor{vandensteen2010interpersonal}'s \citeyearpar{vandensteen2010interpersonal} sorting equilibrium explains why: entrepreneurs who pursue a venture are more optimistic about it, a selection effect, not bias. Investors who choose to fund also share this optimism, because pessimistic investors self-select out. The result is belief homogeneity without any party behaving irrationally. The board contains no skeptics, not because skeptics were expelled, but because they never joined.

\textbf{Step 3: Homogeneity Eliminates Signals.} Without skeptics, disconfirming signals lack advocates \citep{cyert1963a}. Market feedback indicating problems with the committed approach has no champion in governance discussions. \citet{march1991exploration} identifies this tension: belief convergence is efficient for exploitation (executing a known strategy) but destructive for exploration (discovering whether the strategy is correct).

\textbf{Step 4: Signal Loss Prevents Learning.} The venture cannot recognize when it should pivot. Learning stops, not because founders lack motivation, but because the structure prevents it. The cage is structural: founders want to pivot but lack governance support.

\citet{eisenberg1984ambiguity} completes the mechanism through "strategic ambiguity." Early-stage ventures necessarily communicate with some vagueness, the future is genuinely uncertain. This ambiguity enables "unified diversity": stakeholders project their own interpretations onto vague visions. Tesla's "accelerating sustainable transport" attracted believers in electrification, autonomy, and energy transition, each projecting their thesis onto the same vision. But this same mechanism traps the venture later: any pivot threatens \emph{someone's} projected interpretation, and that someone now sits on the board.

The causal chain is:

\[C \rightarrow E \rightarrow F\downarrow \rightarrow R\downarrow \rightarrow G\downarrow\]

Where C = Commitment, E = Early funding, F = Flexibility, R = Repositioning, G = Growth. See Glossary for definitions.

\textbf{Which arrows are tested?} Chapter 4 tests three specific relationships:
\begin{itemize}
\item \textbf{H1: E \ensuremath{\rightarrow} R} (\ensuremath{\rho} = -0.087***) --- Funding suppresses repositioning (TESTED)
\item \textbf{H2: R \ensuremath{\rightarrow} G} (2.60\ensuremath{\times} Mover Advantage) --- Repositioning enables growth (TESTED)
\item \textbf{H3: E \ensuremath{\rightarrow} G} (\ensuremath{\rho} = -0.196***) --- Net negative effect of funding on growth (TESTED)
\end{itemize}
The arrows C \ensuremath{\rightarrow} E (commitment attracts capital) and E \ensuremath{\rightarrow} F (funding reduces flexibility) are assumed from theory, not directly tested.

\begin{figure}
\hypertarget{fig:b-trajectories}{%
\centering
\includegraphics[width=0.85\textwidth,]{img/Ch2_Fig1_B_trajectories.png}
\caption{Strategic breadth (\(B\)) trajectories by archetype across financing rounds: zoom-out (expand), stayer (constant), and zoom-in (focus).}\label{fig:b-trajectories}
}
\end{figure}

\begin{figure}
\hypertarget{fig:golden-cage}{%
\centering
\includegraphics[width=0.8\textwidth]{img/Ch2_Fig2_golden_cage.png}
\caption{The golden cage mechanism: higher early capital (\(E\), log scale) predicts lower repositioning (\(R\)).}\label{fig:golden-cage}
}
\end{figure}

\hypertarget{formal-condition-for-caged-learning}{%
\subsection{Formal Condition for Caged Learning}\label{formal-condition-for-caged-learning}}

Building on \citeauthor{levinthal1993the}'s \citeyearpar{levinthal1993the} insight that successful organizations become "myopic" through competency traps, I formalize when learning ceases:

\textbf{Theorem 1 (Caged Learning).} \emph{Learning ceases when}

\[\mu(1 - \mu) < \frac{\varepsilon}{B}\]

\emph{where \ensuremath{\mu} = belief probability, \ensuremath{\epsilon} = expected belief shift from a signal, and B = strategic breadth. (Proof: Appendix D.)}

Van den Steen's sorting equilibrium produces high \ensuremath{\mu} (shared optimism); operational commitments narrow B (strategic focus). Both forces push the inequality toward satisfaction, caged learning becomes \emph{endogenous} to the funding process itself.

\hypertarget{real-options-foundation}{%
\section{Real Options Foundation}\label{real-options-foundation}}

The cage mechanism operates against the backdrop of real options theory. \citet{mcgrath1999falling} articulates the entrepreneurial implications: initiatives are options, not commitments. Failure enables "falling forward", learning that informs subsequent attempts.

But real options have boundaries. \citet{adner2004what} caution against treating all strategic decisions as options: options require defined exercise conditions and limited downside. The cage violates both conditions, founders cannot define when to pivot (no skeptics to signal), and commitment creates unlimited downside (sunk costs in wrong direction).

\citet{huchzermeier2001project} distinguish uncertainty types: market uncertainty (what customers want) differs from budget uncertainty (whether we can deliver). The cage binds tighter when both uncertainty types are high, the venture needs flexibility for market learning \emph{and} operational learning, yet governance permits neither.

\hypertarget{hypotheses}{%
\section{Hypotheses}\label{hypotheses}}

From the golden cage mechanism, I derive three testable hypotheses:

\textbf{Hypothesis 1 (Funding-Growth):} \emph{Early-stage funding correlates negatively with later-stage growth.}

\[H_1: \frac{dG}{dE} < 0\]

\textbf{Hypothesis 2 (Funding-Repositioning):} \emph{Early-stage funding correlates negatively with repositioning.}

\[H_2: \frac{dR}{dE} < 0\]

\textbf{Hypothesis 3 (Repositioning-Growth):} \emph{Strategic repositioning correlates positively with growth.}

\[H_3: \frac{dG}{dR} > 0\]

Together, these hypotheses complete the decomposition:

\[\frac{dG}{dE} = \frac{dG}{dR} \times \frac{dR}{dE} = (+) \times (-) = (-)\]
