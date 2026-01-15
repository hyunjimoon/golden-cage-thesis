---
modified:
  - 2026-01-14T10:48:18-05:00
---
\hypertarget{ch:introduction}{%
\chapter{Introduction}\label{ch:introduction}}

\hypertarget{general-motivation}{%
\section{General Motivation}\label{general-motivation}}

Commitment structures and investor selection \textbf{cage} founders' strategic flexibility. Startups die not for lack of resources, but for lack of mobility. Over the past decade, the U.S. venture capital industry, deploying over \$330 billion globally at its 2021 peak (PitchBook, 2024), has transformed how entrepreneurs build companies in software, mobility, and deep tech. Yet a fundamental tension persists: securing funding requires specific commitments, while uncertain markets reward adaptation. Founders navigate this tension by positioning ambiguously, attracting diverse stakeholders while preserving their ability to pivot.

For instance, Tesla positioned itself early as "accelerating sustainable transport," attracting believers in electrification, autonomy, and energy transition. This let the company pivot across segments (Roadster \ensuremath{\rightarrow} Model S \ensuremath{\rightarrow} Model 3) without losing governance support. In contrast, Better Place raised \$850 million for "battery swapping infrastructure": a commitment so specific that when market feedback favored charging over swapping, no board member advocated for the alternative. The company liquidated in 2013, its assets sold for less than \$1 million (Bradshaw, 2013), a stark illustration of value destruction through operational lock-in.

Motivated by such divergent outcomes among well-funded ventures, this thesis focuses on the following two aspects of funding and flexibility decisions.

\textbf{How funding and flexibility interact.} Capital creates a double bind. It enables experimentation by providing resources for market testing. Yet to secure capital, founders must commit, and commitments attract like-minded investors. Skeptics filter themselves out, reducing signal diversity and impeding learning. Should founders raise substantial early money so they can experiment, or does rigid governance outweigh the resource benefits? Prior studies examine funding effects and pivoting outcomes in isolation rather than as components of a governance system \citep{camuffo2020a, kirtley2023what}. This thesis addresses the gap.

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

The paradox resolves through a \textbf{mediation framework}. I identify two countervailing effects:

\begin{itemize}
\tightlist
\item \textbf{The Commitment Trap:} Early funding negatively predicts repositioning (\ensuremath{\rho} = -0.087, p \textless{} 0.001). Governance structures attached to capital constrain adaptation.
\item \textbf{The Flexibility Premium:} Repositioning positively predicts later-stage success. Ventures that reposition (``Movers'') outperform those that hold position (``Stayers'') by 2.60\ensuremath{\times} (18.1\% vs.~7.0\% reaching Later Stage VC).
\end{itemize}

Thus, funding suppresses the very mechanism (strategic mobility) required for survival. The reason is not that capital is harmful, but that commitment attracts like-minded investors who filter out skeptics.

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
  \textbf{Why does this happen? (Chapter 2):} Securing capital requires specific commitments. Investors who fund a venture believe those commitments will succeed, and skeptics self-select out. The result is governance homogeneity: no one on the board advocates for alternatives when the market signals pivot. I call this the \emph{golden cage}. The main technical contribution is \textbf{Theorem 1 (Caged Learning)}, which formalizes when organizational learning ceases through the funding process itself.
\item
  \textbf{Does the data confirm it? (Chapters 3-4):} Using 180,994 ventures, I measure repositioning through dictionary-based text analysis and document both patterns: funding suppresses repositioning (Funding \ensuremath{\rightarrow} Repositioning\ensuremath{\downarrow}) and repositioning enables growth (Repositioning \ensuremath{\rightarrow} Growth\ensuremath{\uparrow}). Industry heterogeneity reveals boundary conditions: the cage binds tightest in capital-intensive sectors (Hardware: \ensuremath{\rho} = -0.108, Transportation: \ensuremath{\rho} = -0.101) but releases under extreme uncertainty (Quantum: \ensuremath{\rho} = +0.095).
\end{enumerate}

\textbf{Part II: Escaping the Cage (Chapters 5-6)}

\begin{enumerate}
\def\labelenumi{\arabic{enumi}.}
\setcounter{enumi}{2}
\tightlist
\item
  \textbf{What can founders do? (Chapter 5):} I develop a prescriptive framework distinguishing vision-level commitment (which preserves flexibility) from operational commitment (which forecloses it). The \textbf{Strategic Ambiguity Sweet Spot} (Figure~\ref{fig:sweet-spot}) shows that moderate positioning breadth achieves 16.0\% survival, higher than both narrow and maximally broad positioning.
\end{enumerate}

\hypertarget{contribution-preview}{%
\section{Contribution Preview}\label{contribution-preview}}

This thesis makes three contributions to the literature on entrepreneurial strategy and venture governance.

\textbf{First, I document the funding-growth paradox at unprecedented scale.} With N = 180,994 ventures, this study provides population-level evidence of a negative correlation between early-stage funding and later-stage survival. Prior work has examined funding effects in smaller samples \citep[N = 116]{camuffo2020a} or specific contexts \citep{ewens2018cost}. I demonstrate that the paradox generalizes across industries and cohort years, establishing an empirical regularity that demands theoretical explanation.

\textbf{Second, I identify governance homogeneity, not moral hazard, as the binding constraint on venture adaptation.} This distinction carries implications for intervention design. If founders \emph{will not} pivot due to reduced incentives (moral hazard), the prescription is intensified monitoring. If founders \emph{cannot} pivot due to structural constraints (the golden cage), the prescription is governance redesign. My evidence favors the structural explanation: founders of failed well-funded ventures frequently express regret at not pivoting earlier, suggesting motivation was present but governance support was absent.

\textbf{Third, I introduce a theoretical distinction between vision-level and operational commitment.} Vision commitment ("accelerating sustainable transport") preserves flexibility by accommodating multiple implementation paths. Operational commitment ("battery swapping infrastructure") forecloses alternatives by binding resources to specific mechanisms. This distinction explains heterogeneity among well-funded ventures: Tesla's vision commitment enabled pivots across segments and business models, while Better Place's operational commitment prevented adaptation when market feedback favored charging over swapping. The practical implication is that founders can capture commitment's credibility benefits while preserving flexibility, but only by committing at the right level of abstraction.

\begin{center}\rule{0.5\linewidth}{0.5pt}\end{center}
