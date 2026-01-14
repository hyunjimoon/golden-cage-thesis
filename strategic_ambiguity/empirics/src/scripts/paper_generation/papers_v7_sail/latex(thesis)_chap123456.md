---
modified:
  - 2026-01-14T10:34:55-05:00
---
\hypertarget{ch:introduction}{%
\chapter{Introduction}\label{ch:introduction}}

\begin{quote}
\emph{"What's the puzzle?"} \textbf{Core Equation}: dG/dE = (dG/dR) \ensuremath{\times} (dR/dE) = (+) \ensuremath{\times} (-) = (-)

\emph{Key terms are defined in Appendix C: Glossary. Canonical numbers are locked.}
\end{quote}

\hypertarget{general-motivation}{%
\section{General Motivation}\label{general-motivation}}

Commitment structures and investor selection \textbf{cage} founders' strategic flexibility. Startups die not for lack of resources, but for lack of mobility. Over the past decade, the U.S. venture capital industry, deploying over \$330 billion globally at its 2021 peak (PitchBook, 2024), has transformed how entrepreneurs build companies in software, mobility, and deep tech. Yet a fundamental tension persists: securing funding requires specific commitments, while uncertain markets reward adaptation. Founders navigate this tension by positioning ambiguously, attracting diverse stakeholders while preserving their ability to pivot.

For instance, Tesla positioned itself early as "accelerating sustainable transport," attracting believers in electrification, autonomy, and energy transition. This let the company pivot across segments (Roadster \ensuremath{\rightarrow} Model S \ensuremath{\rightarrow} Model 3) without losing governance support. In contrast, Better Place raised \$850 million for "battery swapping infrastructure": a commitment so specific that when market feedback favored charging over swapping, no board member advocated for the alternative. The company liquidated in 2013, its assets sold for less than \$1 million (Bradshaw, 2013), a stark illustration of value destruction through operational lock-in.

Motivated by such divergent outcomes among well-funded ventures, this thesis focuses on the following two aspects of funding and flexibility decisions.

\textbf{How funding and flexibility interact.} Capital creates a double bind. It enables experimentation by providing resources for market testing. Yet to secure capital, founders must commit, and commitments attract like-minded investors. Skeptics filter themselves out. Signal diversity dies. Learning stops. Should founders raise substantial early money so they can experiment, or does rigid governance outweigh the resource benefits? Prior studies examine funding effects and pivoting outcomes in isolation rather than as components of a governance system \citep{camuffo2020a, kirtley2023what}. This thesis addresses the gap.

Commitment decisions also affect survival vertically. A founder who commits at the operational level (specific technology, specific market) attracts investors who believe in that specific path. When the market signals that the venture should pivot, no board member advocates for alternatives. This raises a question: how can founders commit credibly while preserving their ability to adapt? We need to understand two things: how funding and flexibility interact horizontally, and how governance composition affects strategic adaptation vertically.

\textbf{How to commit while staying flexible.} Large-scale venture data now let founders optimize how they commit. Text analysis of company descriptions reveals which ventures maintain strategic breadth over time. Industry-level analysis shows where the tension between commitment and flexibility is tightest (capital-intensive sectors like mobility) and where it releases (pre-paradigmatic sectors like quantum computing). These analyses help founders and investors capture commitment's credibility benefits without foreclosing adaptation.

This thesis addresses these challenges. Below I explain how each chapter tackles them, summarize the main results, and outline the organization.

\hypertarget{the-funding-growth-paradox}{%
\section{The Funding-Growth Paradox}\label{the-funding-growth-paradox}}

The data reveal a counterintuitive pattern. Analyzing 180,994 ventures from PitchBook (2021\textendash{}2025), I find a negative correlation between early-stage funding and later-stage survival:

\[\rho(\text{Funding}, \text{Growth}) = -0.196 \quad (p < 0.001)\]

\begin{figure}
\hypertarget{fig:capital-paradox}{%
\centering
\includegraphics[width=0.85\textwidth,]{img/Ch1_Fig1_capital_paradox.png}
\caption{The Funding-Growth Paradox. Higher early funding correlates with lower later-stage success (\(N = 180{,}994\), \(\rho = -0.196\), \(p < 0.001\)).}\label{fig:capital-paradox}
}
\end{figure}

Decomposing the pattern resolves it. I identify two countervailing effects and formalize their interaction as the product of component correlations:

\[\frac{dG}{dE} = \underbrace{\frac{dG}{dR}}_{\text{Flexibility Premium }(+)} \times \underbrace{\frac{dR}{dE}}_{\text{Commitment Trap }(-)} = (-)\]

The \textbf{Flexibility Premium} (dG/dR \textgreater{} 0) captures the growth benefit of adaptation: ventures that reposition ("Movers") outperform those that hold position ("Stayers") by 2.60\ensuremath{\times} (18.1\% vs.~7.0\% later-stage survival). The \textbf{Commitment Trap} (dR/dE \textless{} 0) captures the rigidity cost of funding: early funding correlates with lower repositioning (\ensuremath{\rho} = -0.087, p \textless{} 0.001), because governance structures attached to capital constrain adaptation. A positive times a negative is negative: funding correlates with reduced mobility. The reason is not that capital is harmful, but rather that commitment attracts like-minded investors who filter out skeptics.

\begin{figure}
\hypertarget{fig:mediation-dag}{%
\centering
\includegraphics[width=0.85\textwidth,]{img/Ch1_Fig2_mediation_dag.png}
\caption{Mediation structure. \textbf{Upper path (measured):} Early Funding (\(E\)) suppresses Repositioning (\(R\)) (Commitment Trap, \(-\)). \textbf{Lower path (unmeasured):} Commitment both increases funding and reduces flexibility. \textbf{Middle path:} Repositioning increases Growth (Flexibility Premium, \(+\)). Overall, \(E\) negatively correlates with \(G\) (Funding Paradox, \(-\)).}\label{fig:mediation-dag}
}
\end{figure}

\hypertarget{research-questions-and-chapter-overview}{%
\section{Research Questions and Chapter Overview}\label{research-questions-and-chapter-overview}}

This thesis addresses three interconnected questions, each corresponding to a thesis part:

\textbf{Part I: The Cage (Theory and Evidence, Chapters 2-4)}

\begin{enumerate}
\def\labelenumi{\arabic{enumi}.}
\item
  \textbf{Why does this happen? (Chapter 2):} I synthesize \citeauthor{vandensteen2010interpersonal}'s \citeyearpar{vandensteen2010interpersonal} sorting equilibrium, \citeauthor{eisenberg1984ambiguity}'s \citeyearpar{eisenberg1984ambiguity} strategic ambiguity, and \citeauthor{ghemawat1991commitment}'s \citeyearpar{ghemawat1991commitment} commitment analysis into a unified mechanism: the \emph{golden cage}. The main technical contribution is \textbf{Theorem 1 (Caged Learning)}, which formalizes when organizational learning ceases through the funding process itself.
\item
  \textbf{Does the data confirm it? (Chapters 3-4):} Using 180,994 ventures, I measure repositioning through dictionary-based text analysis and document both the CER pattern (Funding \ensuremath{\rightarrow} Repositioning\ensuremath{\downarrow}) and the FRG pattern (Repositioning \ensuremath{\rightarrow} Growth\ensuremath{\uparrow}). Industry heterogeneity reveals boundary conditions: the cage binds tightest in capital-intensive sectors (Hardware: \ensuremath{\rho} = -0.108, Transportation: \ensuremath{\rho} = -0.101) but releases under extreme uncertainty (Quantum: \ensuremath{\rho} = +0.095).
\end{enumerate}

\textbf{Part II: Escaping the Cage (Chapters 5-6)}

\begin{enumerate}
\def\labelenumi{\arabic{enumi}.}
\setcounter{enumi}{2}
\tightlist
\item
  \textbf{What can founders do? (Chapter 5):} I develop a prescriptive framework distinguishing vision-level commitment (which preserves flexibility) from operational commitment (which forecloses it). The \textbf{Strategic Ambiguity Sweet Spot} (Figure 10) shows that moderate positioning breadth achieves 16.0\% survival, higher than both narrow and maximally broad positioning.
\end{enumerate}

\hypertarget{contribution-preview}{%
\section{Contribution Preview}\label{contribution-preview}}

This thesis makes three contributions to the literature on entrepreneurial strategy and venture governance.

\textbf{First, I document the funding-growth paradox at unprecedented scale.} With N = 180,994 ventures, this study provides population-level evidence of a negative correlation between early-stage funding and later-stage survival. Prior work has examined funding effects in smaller samples \citep[N = 116]{camuffo2020a} or specific contexts \citep{ewens2018cost}. I demonstrate that the paradox generalizes across industries and cohort years, establishing an empirical regularity that demands theoretical explanation.

\textbf{Second, I identify governance homogeneity, not moral hazard, as the binding constraint on venture adaptation.} This distinction carries implications for intervention design. If founders \emph{will not} pivot due to reduced incentives (moral hazard), the prescription is intensified monitoring. If founders \emph{cannot} pivot due to structural constraints (the golden cage), the prescription is governance redesign. My evidence favors the structural explanation: founders of failed well-funded ventures frequently express regret at not pivoting earlier, suggesting motivation was present but governance support was absent.

\textbf{Third, I introduce a theoretical distinction between vision-level and operational commitment.} Vision commitment ("accelerating sustainable transport") preserves flexibility by accommodating multiple implementation paths. Operational commitment ("battery swapping infrastructure") forecloses alternatives by binding resources to specific mechanisms. This distinction explains heterogeneity among well-funded ventures: Tesla's vision commitment enabled pivots across segments and business models, while Better Place's operational commitment prevented adaptation when market feedback favored charging over swapping. The practical implication is that founders can capture commitment's credibility benefits while preserving flexibility, but only by committing at the right level of abstraction.

\begin{center}\rule{0.5\linewidth}{0.5pt}\end{center}

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

\textbf{Structural vs.~motivational constraint.} We distinguish "cannot pivot" (structural) from "will not pivot" (moral hazard), with distinct implications for intervention design. If founders \emph{will not} pivot due to reduced incentives, the prescription is intensified monitoring. If founders \emph{cannot} pivot due to structural constraints (the cage), the prescription is governance redesign, preserving skeptical voices before funding eliminates them.

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

I synthesize \citeauthor{vandensteen2010interpersonal}'s \citeyearpar{vandensteen2010interpersonal} sorting equilibrium, \citeauthor{eisenberg1984ambiguity}'s \citeyearpar{eisenberg1984ambiguity} strategic ambiguity, and \citeauthor{ghemawat1991commitment}'s \citeyearpar{ghemawat1991commitment} commitment analysis into a unified mechanism, the \emph{golden cage}. The cage forms through a four-step sequence:

\textbf{Step 1: Commitment Attracts Believers.} Securing capital requires operational commitments, production architecture choices, go-to-market sequences, milestone definitions \citep{gompers2001the, hellmann2002venture}. Investors who fund a venture believe these specific commitments will succeed.

\textbf{Step 2: Believers Filter Skeptics.} \citeauthor{vandensteen2010interpersonal}'s \citeyearpar{vandensteen2010interpersonal} sorting equilibrium explains why: entrepreneurs who pursue a venture are more optimistic about it, a selection effect, not bias. Investors who choose to fund also share this optimism, because pessimistic investors self-select out. The result is belief homogeneity without any party behaving irrationally. The board contains no skeptics, not because skeptics were expelled, but because they never joined.

\textbf{Step 3: Homogeneity Eliminates Signals.} Without skeptics, disconfirming signals lack advocates \citep{cyert1963a}. Market feedback indicating problems with the committed approach has no champion in governance discussions. \citet{march1991exploration} identifies this tension: belief convergence is efficient for exploitation (executing a known strategy) but destructive for exploration (discovering whether the strategy is correct).

\textbf{Step 4: Signal Loss Prevents Learning.} The venture cannot recognize when it should pivot. Learning stops, not because founders lack motivation, but because the structure prevents it. The cage is structural: founders want to pivot but lack governance support.

\citet{eisenberg1984ambiguity} completes the mechanism through "strategic ambiguity." Early-stage ventures necessarily communicate with some vagueness, the future is genuinely uncertain. This ambiguity enables "unified diversity": stakeholders project their own interpretations onto vague visions. Tesla's "accelerating sustainable transport" attracted believers in electrification, autonomy, and energy transition, each projecting their thesis onto the same vision. But this same mechanism traps the venture later: any pivot threatens \emph{someone's} projected interpretation, and that someone now sits on the board.

The causal chain is:

\[C \rightarrow E \rightarrow F\downarrow \rightarrow R\downarrow \rightarrow G\downarrow\]

Where C = Commitment, E = Early funding, F = Flexibility, R = Repositioning, G = Growth. See Glossary for definitions.

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

\hypertarget{ch:conclusion}{%
\chapter{Conclusion}\label{ch:conclusion}}

\begin{quote}
\emph{"So what?"} \textbf{Final Equation}: When uncertain, commit to \emph{reposition}, rather than to position.
\end{quote}

\hypertarget{theoretical-contributions}{%
\section{Theoretical Contributions}\label{theoretical-contributions}}

This thesis makes three theoretical contributions:

\textbf{First}, I introduce the \emph{golden cage} mechanism, explaining how funding constrains growth through governance homogeneity rather than moral hazard. The mechanism integrates \citeauthor{vandensteen2010interpersonal}'s sorting equilibrium, \citeauthor{eisenberg1984ambiguity}'s strategic ambiguity, and \citeauthor{ghemawat1991commitment}'s commitment analysis.

\textbf{Second}, I distinguish vision-level commitment from operational commitment. This explains why well-funded ventures diverge: some (Tesla) preserve flexibility through vision commitment; others (Better Place) foreclose it through operational commitment.

\textbf{Third}, I formalize caged learning (Theorem 1), showing how funding endogenously produces conditions (high \ensuremath{\mu}, low B) that prevent founders from updating their beliefs.

\hypertarget{practical-implications}{%
\section{Practical Implications}\label{practical-implications}}

\textbf{For Founders:}
\begin{itemize}
\tightlist
\item Commit to \emph{reposition}, not to position
\item Design governance to preserve skeptical voices \emph{before} funding eliminates them
\item Prioritize platform capabilities over segment-specific capabilities until the market clarifies what works
\item Cultivate a "discoverer" identity that enables strategic flexibility
\end{itemize}

\textbf{For Investors:}
\begin{itemize}
\tightlist
\item Distinguish vision alignment from operational commitment
\item Fund platform capability, not product specificity
\item Expect successful ventures to reposition, design governance to enable adaptation
\item Preserve diverse information sources on the board
\end{itemize}

\textbf{For Scholars:}
\begin{itemize}
\tightlist
\item The cage mechanism shows governance, not incentives, constrains ventures
\item Interventions should target governance design, not founder monitoring
\item Future research should directly measure board belief diversity
\end{itemize}

\hypertarget{limitations}{%
\section{Limitations}\label{limitations}}

Three limitations warrant acknowledgment:

\textbf{First}, I document correlation, not causation. An alternative explanation remains: rigid founders attract more funding. I address this through three layers of defense: (1) selection is part of the mechanism; (2) conditioning on observables reduces selection; (3) future quasi-experimental approaches could provide identification.

\textbf{Second}, PitchBook overrepresents technology ventures in the United States. Generalization requires replication in other sectors and geographies.

\textbf{Third, and most critically, I infer governance homogeneity from behavioral outcomes (low repositioning), not direct measurement.} I derive the core claim, "governance lacks skeptics", from observing that well-funded ventures reposition less frequently. This behavioral pattern is \emph{consistent with} the sorting mechanism, but the mechanism itself remains unobserved.

Theory grounds this inference. \citeauthor{vandensteen2010interpersonal}'s \citeyearpar{vandensteen2010interpersonal} sorting equilibrium predicts that founders and investors with heterogeneous priors will sort into organizations led by like-minded others, a mathematical result, not an empirical claim. Applied to venture governance, this predicts belief convergence among board members. However, the prediction remains \emph{indirect}: I observe the predicted \emph{consequence} (low repositioning) rather than the posited \emph{cause} (belief homogeneity). The gap matters.

Future work must directly measure board composition diversity. Three approaches merit consideration: (a) survey-based measurement of founder-investor disagreement on strategic direction, (b) analysis of board voting records on strategic pivots, and (c) text analysis of investor communications (e.g., board meeting minutes, investor letters) to quantify belief divergence. Without such direct measurement, the governance homogeneity mechanism, while theoretically compelling and empirically consistent, remains a well-supported conjecture rather than established fact.

\hypertarget{alternative-explanations}{%
\subsection{Alternative Explanations}\label{alternative-explanations}}

The governance homogeneity mechanism proposed in this thesis competes with several alternative explanations for the funding-growth paradox. I consider three prominent alternatives and discuss why the evidence favors the governance account.

\input{table/alternatives.tex}

\textbf{Moral Hazard} predicts reduced founder effort after funding. Yet founders of failed well-funded ventures frequently express regret at not pivoting earlier, suggesting motivation was present but governance support was absent. If moral hazard drove the pattern, founders would report satisfaction with their strategic persistence, not regret about rigidity.

\textbf{Milestone Pressure} predicts that ventures deviating from milestones (i.e., Movers) should face capital constraints and underperform. The opposite obtains: Movers achieve 2.60\ensuremath{\times} higher success rates than Stayers. This suggests that the benefit of strategic adaptation outweighs the cost of milestone deviation, inconsistent with milestone pressure as the binding constraint.

\textbf{Burn-rate Discipline} predicts the cage should weaken in capital-light sectors where experimentation is cheap. Software's near-zero correlation (\ensuremath{\rho} = -0.001) is consistent with this account. However, Quantum's positive correlation (\ensuremath{\rho} = +0.095) is inconsistent, if burn-rate were decisive, capital-intensive Quantum should show the strongest cage, not the weakest. The uncertainty-contingent pattern favors governance homogeneity over burn-rate as the primary mechanism.

\hypertarget{future-research}{%
\section{Future Research}\label{future-research}}

Three directions merit further investigation:

\begin{enumerate}
\def\labelenumi{\arabic{enumi}.}
\tightlist
\item
  \textbf{Direct measurement of belief homogeneity:} Survey-based or text-based measurement of board belief diversity
\item
  \textbf{Quasi-experimental identification:} VC fund vintage effects, geographic shocks, or industry funding cycles as instruments
\item
  \textbf{Governance interventions:} Field experiments testing skeptic preservation strategies
\end{enumerate}

\hypertarget{closing}{%
\section{Closing}\label{closing}}

Capital is oxygen for startups, but oxygen in a sealed chamber becomes a cage.

This thesis began with a paradox: the \$330 billion venture capital industry exists to fuel growth, yet early-stage funding correlates negatively with later-stage survival (\ensuremath{\rho} = -0.196, N = 180,994). The paradox \textbf{resolves} through decomposition: funding \textbf{suppresses} repositioning (\ensuremath{\rho} = -0.087), and repositioning \textbf{drives} growth (Movers outperform Stayers by 2.60\ensuremath{\times}). The product of a positive and a negative is negative.

The mechanism I term the \emph{golden cage} operates through belief homogeneity. Securing capital requires commitments that attract investors who share the founder's thesis. Skeptics self-select out. The resulting board contains only believers, efficient for execution, destructive for learning. When market signals suggest pivoting, no one advocates alternatives. The venture cannot adapt, not for lack of will, but for lack of governance diversity.

Industry heterogeneity reveals boundary conditions. The cage binds tightest in capital-intensive sectors where switching costs are high: Hardware (\ensuremath{\rho} = -0.108), Transportation (\ensuremath{\rho} = -0.101). It releases under extreme uncertainty where no dominant design exists: Quantum (\ensuremath{\rho} = +0.095). The cage operates when commitment forecloses \emph{identifiable} alternatives; under radical uncertainty, no alternatives are identifiable, so commitment cannot foreclose them.

The cage need not be fatal. With deliberate governance design, committing at the vision level, preserving skeptics, building milestone flexibility, founders and investors can capture commitment's benefits without foreclosing adaptation. The prescription reduces to four words:

\textbf{Commit to reposition, not position.}

\emph{Move to grow.}

\begin{figure}
\hypertarget{fig:growth-diagnostics}{%
\centering
\includegraphics[width=0.85\textwidth,height=\textheight]{img/Ch6_Fig1_growth_diagnostics.png}
\caption{Growth diagnostics (placeholder figure; replace with final diagnostic plot when available).}\label{fig:growth-diagnostics}
}
\end{figure}
