---
modified:
  - 2026-01-14T10:48:18-05:00
  - 2026-01-15T11:18:27-05:00
---
\hypertarget{ch:introduction}{%
\chapter{Introduction}\label{ch:introduction}}

\hypertarget{general-motivation}{%
\section{General Motivation}\label{general-motivation}}

Startups die not for lack of resources, but for lack of \emph{strategic flexibility}---the capacity to change direction when markets shift. Over the past decade, venture capital has deployed over \$330 billion annually to fuel startup growth. Yet a puzzle emerges from the data: ventures that raise more early funding are \emph{less} likely to succeed later. Why would resources hurt?

The answer lies in governance. To secure funding, founders must commit to specific strategies. These commitments attract investors who believe in those strategies. Skeptics (investors who might advocate for alternatives) never join. The resulting board contains only believers. When market signals suggest pivoting, no one advocates for change. The venture is trapped: not for lack of capital, but for lack of diverse perspectives. I call this the \emph{golden cage}.

Two electric vehicle ventures illustrate the contrast. Tesla positioned itself as ``accelerating sustainable transport''---a vision broad enough to attract believers in electrification, autonomy, and energy storage. When Tesla pivoted from Roadster to Model 3, diverse board perspectives supported the shift. Better Place raised \$850 million for ``battery swapping infrastructure''---a commitment so specific that when charging technology advanced, no governance voice advocated pivoting. Better Place liquidated in 2013; its assets sold for less than \$1 million.

This thesis investigates why funding creates this cage and how founders can escape it.

\textbf{Two Research Questions.} This thesis addresses two questions:

\emph{First, why does funding suppress flexibility?} Capital creates a double bind. It enables experimentation by providing resources. Yet to secure capital, founders must commit, and commitments attract like-minded investors. Skeptics filter themselves out. Prior studies examine funding effects and pivoting outcomes in isolation \citep{camuffo2020a, kirtley2023what}. This thesis treats them as components of a single governance system.

\emph{Second, how can founders commit credibly while preserving flexibility?} The level of commitment matters. A founder who commits at the operational level (``battery swapping infrastructure'') attracts only believers in that mechanism. A founder who commits at the vision level (``sustainable transport'') attracts believers in multiple mechanisms. Large-scale data reveal where the tension is tightest (capital-intensive sectors) and where it releases (pre-paradigmatic sectors like quantum). These patterns help founders design commitment structures that preserve adaptation capacity.

\hypertarget{the-funding-growth-paradox}{%
\section{The Funding-Growth Paradox}\label{sec:funding-growth-paradox}}

Conventional wisdom holds that more resources mean better outcomes---a startup that raises \$10 million should outperform one that raises \$1 million through more runway for experimentation, more capacity for talent acquisition, and more cushion for mistakes. Yet the data tell a different story. Analyzing 180,994 ventures from PitchBook (2021--2025), I find that early-stage funding correlates \emph{negatively} with later-stage success: $\rho = -0.196$ (p \textless{} 0.001). Ventures that raise more money early are less likely to reach Series C or beyond. This is the \textbf{Funding-Growth Paradox}.

\begin{figure}
\hypertarget{fig:capital-paradox}{%
\centering
\includegraphics[width=0.85\textwidth,]{img/Ch1_Fig1_capital_paradox.png}
\caption{The Funding-Growth Paradox. Higher early funding correlates with lower later-stage success (\(N = 180{,}994\), \(\rho = -0.196\), \(p < 0.001\)).}\label{fig:capital-paradox}
}
\end{figure}

The paradox resolves through a mediating variable: \emph{repositioning}---the observable shift in a venture's strategic positioning over time, measured as changes in the breadth of company descriptions between funding rounds. The data reveal two patterns: early funding negatively predicts repositioning ($\rho = -0.087$, p \textless{} 0.001)---the \textbf{Commitment Cage} where governance structures attached to capital constrain adaptation---and repositioning positively predicts later-stage success, with Movers outperforming Stayers by 2.60$\times$ (18.1\% vs.~7.0\%)---the \textbf{Flexibility Flex}. Together, these patterns explain the paradox: funding suppresses the very mechanism (repositioning) required for survival. Capital itself is not harmful; the problem is that commitment attracts like-minded investors who filter out skeptics.

\begin{figure}
\hypertarget{fig:mediation-dag}{%
\centering
\includegraphics[width=0.85\textwidth,]{img/Ch1_Fig2_mediation_dag.png}
\caption{The mediation structure explaining the paradox. Early Funding (\(E\)) suppresses Repositioning (\(R\)), which in turn drives Growth (\(G\)). The negative overall correlation between funding and growth arises because funding blocks the path to adaptation.}\label{fig:mediation-dag}
}
\end{figure}

\hypertarget{chapter-overview}{%
\section{Chapter Overview}\label{chapter-overview}}

The thesis proceeds in two parts. The first part (Chapters 2--4) develops and tests the theory. Chapter~\ref{ch:theory} explains why funding creates the cage: securing capital requires specific commitments, investors who fund believe those commitments will succeed, and skeptics self-select out. The resulting governance homogeneity prevents learning---no one advocates for alternatives when market signals suggest pivoting. I formalize this logic as \textbf{Theorem 1 (Caged Learning)}, which specifies the conditions under which organizational learning ceases. Chapters~\ref{ch:data} and \ref{ch:results} test the theory using 180,994 ventures. The data confirm both patterns: funding suppresses repositioning (the Commitment Cage) and repositioning enables growth (the Flexibility Flex). Industry heterogeneity reveals boundary conditions---the cage binds tightest in capital-intensive sectors like Hardware and Transportation, but releases under extreme uncertainty in pre-paradigmatic sectors like Quantum.

The second part (Chapters 5--6) turns prescriptive. Chapter~\ref{ch:design} addresses what founders can do. The key insight is that the \emph{level} of commitment matters: vision-level commitment (``sustainable transport'') preserves flexibility, while operational commitment (``battery swapping'') forecloses it. Empirically, ventures with moderate positioning breadth achieve 15.0\% survival---higher than both narrow and maximally broad positioning. Chapter~\ref{ch:conclusion} synthesizes contributions, discusses limitations (especially the challenge of directly measuring governance belief diversity), and outlines a research agenda for testing governance interventions.

\hypertarget{contribution-preview}{%
\section{Contribution Preview}\label{sec:contribution-preview}}

This thesis makes three contributions to the literature on entrepreneurial strategy and venture governance.

The first contribution is empirical: I establish the funding-growth paradox as a robust regularity. Using 180,994 ventures from PitchBook (2021--2025), I document that higher early-stage funding correlates with a lower probability of later-stage success. This pattern is surprising because it contradicts the resource-based logic that more funding should enable more experimentation and better outcomes.

The second contribution is theoretical: I explain why the paradox arises. The golden cage mechanism shows how funding induces governance homogeneity through belief-based sorting. Investors who fund a venture believe its current strategy will succeed; skeptics never join. The resulting board lacks the cognitive diversity to advocate for pivots when market signals change. I formalize this logic as Theorem~1 (Caged Learning) and show empirically where the cage binds tightest---in capital-intensive sectors---and where it releases---in pre-paradigmatic sectors like quantum computing.

The third contribution is prescriptive: I provide a framework for founders to commit credibly while preserving flexibility. The key is to distinguish what to commit to (vision vs.~operations), how to grow (diagnosing market vs.~operational bottlenecks), and how to fund (sequencing capital sources to preserve governance diversity). These principles help founders escape the cage without sacrificing the credibility required to attract resources.

Chapter~\ref{ch:theory} begins by developing the theoretical foundations of the golden cage.