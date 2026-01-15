---
modified:
  - 2026-01-15T11:11:26-05:00
---
% =========================================================
% APPENDICES
% =========================================================

\chapter{Variable Construction Details}
\label{app:a}

\section{PitchBook Data Fields}

\begin{table}[htbp]
    \centering
    \caption{Primary Data Fields from PitchBook}
    \label{tab:pb-fields}
    \begin{tabular}{@{}llll@{}}
        \toprule
        \textbf{Field Name} & \textbf{Type} & \textbf{Description} & \textbf{Usage} \\
        \midrule
        \texttt{org\_uuid} & String & Unique venture identifier & Primary key \\
        \texttt{company\_description} & Text & Business description & Strategic Breadth ($B$) \\
        \texttt{primary\_industry} & Categorical & Industry classification & Heterogeneity analysis \\
        \texttt{first\_financing\_size} & Numeric & Initial funding (USD) & Early Funding ($E$) \\
        \texttt{last\_financing\_deal\_type} & Categorical & Most recent stage & Growth ($G$) \\
        \texttt{total\_raised} & Numeric & Cumulative funding & Growth Scale ($G$) \\
        \bottomrule
    \end{tabular}
\end{table}

\section{Vagueness Dictionary}

127 terms classified as:
\begin{itemize}
    \item \textbf{Vague (high B):} platform, ecosystem, solutions, enable, transform, optimize, leverage, innovative, next-generation, comprehensive, integrated, scalable
    \item \textbf{Specific (low B):} device, application, tool, product, service, system, manufacturer, operator, provider, developer
\end{itemize}

\section{Variable Definitions}

\subsection*{Strategic Breadth ($B$)}
\begin{equation}
B = 50 \times \frac{\text{vague\_terms}}{\max(\text{vague})} + 50 \times \left(1 - \frac{\text{concrete\_markers}}{\max(\text{concrete})}\right)
\end{equation}

\subsection*{Repositioning ($R$)}
\begin{equation}
R = \lvert B_T - B_0 \rvert
\end{equation}

\subsection*{Outcomes}
\begin{itemize}
    \item \textbf{Growth ($G$)}: Binary = 1 if reached Later Stage VC (Series C+). Base rate: 11.5\%.
    \item \textbf{Growth Multiple}: Continuous funding scale = $F_t / E$ (total subsequent funding / early funding). Used for illustrative cases only.
\end{itemize}


\chapter{Proof of Theorem 1}
\label{app:b}

\textbf{Theorem 1 (Caged Learning).} Learning ceases when $\mu(1 - \mu) < \varepsilon / B$.

\section{Proof}

\textbf{Step 1.} Value of information $\propto$ belief variance: $\mu(1-\mu)$.

\textbf{Step 2.} Signal quality $\propto 1/B$: Low $B \to$ precise; High $B \to$ noisy.

\textbf{Step 3.} Learning ceases when: $\mu(1-\mu) < \varepsilon/B$

\textbf{Step 4.} Early funding triggers both:
\begin{enumerate}
    \item Van den Steen sorting $\to$ high $\mu$
    \item Operational commitment $\to$ low $B$
\end{enumerate}

Combined: $\underbrace{\mu(1-\mu)}_{\downarrow} < \underbrace{\varepsilon/B}_{\uparrow}$ \hfill $\square$


\chapter{Robustness Tests}
\label{app:c}

\section{Strategic Breadth Distribution}

$B_0$ is bimodal:
\begin{itemize}
    \item Low (0--50): 17.9\%
    \item Mid (50--75): 0.0\%
    \item High (75--100): 82.1\%
\end{itemize}

\section{Threshold Sensitivity}

\begin{table}[htbp]
    \centering
    \caption{Mover Advantage by Threshold Definition}
    \label{tab:threshold}
    \begin{tabular}{@{}lrrrr@{}}
        \toprule
        \textbf{Definition} & \textbf{Movers \%} & \textbf{Stayer Succ} & \textbf{Mover Succ} & \textbf{Advantage} \\
        \midrule
        R $>$ 0 (Main) & 40.3\% & 7.0\% & 18.1\% & \textbf{2.60$\times$} \\
        R $>$ 1 & 13.6\% & 10.4\% & 18.0\% & 1.72$\times$ \\
        R $>$ 5 & 9.0\% & 10.8\% & 17.7\% & 1.63$\times$ \\
        R $>$ 10 & 6.3\% & 11.0\% & 17.9\% & 1.62$\times$ \\
        Quartile Cross & 6.4\% & 11.0\% & 17.6\% & 1.60$\times$ \\
        \bottomrule
    \end{tabular}
\end{table}

\textbf{Finding}: Mover Advantage ranges 1.60$\times$--2.60$\times$ across definitions. Core finding is robust.

\section{Rank Normalization}

Under rank normalization:
\begin{itemize}
    \item 100\% become ``Movers'' (each rank unique)
    \item R $>$ 0 definition uninformative
    \item Threshold-based definitions (R $>$ 5, Quartile Cross) remain valid
\end{itemize}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.9\textwidth]{img/AppC_Fig1_bimodal_distribution.png}
    \caption{Bimodal $B_0$ distribution and R thresholds.}
    \label{fig:bimodal}
\end{figure}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.9\textwidth]{img/AppC_Fig2_threshold_robustness.png}
    \caption{Mover Advantage across threshold definitions.}
    \label{fig:threshold}
\end{figure}


\chapter{Glossary}
\label{app:d}

\section{Core Variables}

\begin{itemize}
    \item \textbf{$C$}: Commitment level (latent; operational vs. vision-level)
    \item \textbf{$E$}: Early-stage funding (\$M USD)
    \item \textbf{$F$}: Strategic Flexibility (latent capability to keep multiple paths viable)
    \item \textbf{$B$}: Strategic Breadth (0--100 vagueness scale); $B_0$ = baseline, $B_T$ = endpoint
    \item \textbf{$R$}: Repositioning $= |B_T - B_0|$ (observable proxy for $F$)
    \item \textbf{$G$}: Growth (binary = 1 if reached Later Stage VC, Series C+)
    \item \textbf{$\mu$}: Belief probability (shared optimism in governance)
    \item \textbf{$\varepsilon$}: Expected belief shift from a signal
\end{itemize}

\section{Key Numbers}

\begin{table}[htbp]
    \centering
    \begin{tabular}{@{}ll@{}}
        \toprule
        Metric & Value \\
        \midrule
        $N$ & 180,994 \\
        $\rho(E,G)$ & $-0.196^{***}$ (Funding-Growth Paradox) \\
        $\rho(E,R)$ & $-0.087^{***}$ (Commitment Cage) \\
        Mover Advantage & $2.60\times$ ($P(G=1)$: 18.1\% vs 7.0\%) \\
        Stayers / Movers & 59.7\% / 40.3\% \\
        Base growth rate ($G=1$) & 11.5\% \\
        Sweet Spot (Q3) survival & 15.0\% \\
        \bottomrule
    \end{tabular}
\end{table}

\textbf{Industry Heterogeneity:}
\begin{table}[htbp]
    \centering
    \begin{tabular}{@{}lrl@{}}
        \toprule
        Industry & $\rho(E,G)$ & Interpretation \\
        \midrule
        Hardware & $-0.108^{***}$ & Cage binds tightest \\
        Transportation & $-0.101^{***}$ & Capital-intensive lock-in \\
        Biotech & $-0.085^{***}$ & High switching costs \\
        Software & $-0.001$ (ns) & Cage releases \\
        Quantum & $+0.095^{*}$ & Era of ferment exception \\
        \bottomrule
    \end{tabular}
\end{table}

\section{Mechanism Terms}

\begin{itemize}
    \item \textbf{Golden Cage}: Structural constraint preventing adaptation due to governance homogeneity; forms through $C \rightarrow E \rightarrow F\downarrow \rightarrow R\downarrow \rightarrow G\downarrow$
    \item \textbf{Funding-Growth Paradox (H3)}: $\rho(E,G) < 0$; early funding correlates negatively with later-stage growth
    \item \textbf{Commitment Cage (H1)}: $dR/dE < 0$; funding suppresses repositioning
    \item \textbf{Flexibility Flex (H2)}: $dG/dR > 0$; repositioning predicts growth
    \item \textbf{Decomposition}: $dG/dE = (dG/dR) \times (dR/dE) = (+) \times (-) = (-)$; H3 = H2 $\times$ H1
    \item \textbf{Van den Steen Sorting}: Optimists attract optimists; skeptics self-select out, producing belief homogeneity
    \item \textbf{Strategic Ambiguity}: Precision about direction combined with flexibility about destination; attracts diverse believers
    \item \textbf{Belief Homogeneity}: Convergence of beliefs among governance members through sorting
    \item \textbf{Signal Diversity}: Presence of diverse perspectives to interpret market feedback
    \item \textbf{Caged Learning}: Learning ceases when $\mu(1-\mu) < \varepsilon/B$ (Theorem 1)
    \item \textbf{Era of Ferment}: Pre-paradigmatic phase where no dominant design exists; cage releases
    \item \textbf{Mover}: Venture with $R > 0$ (40.3\% of sample)
    \item \textbf{Stayer}: Venture with $R = 0$ (59.7\% of sample)
\end{itemize}

\section{Commitment Types}

\begin{itemize}
    \item \textbf{Vision-level Commitment}: Direction without destination; preserves flexibility (e.g., Tesla: ``accelerating sustainable transport'')
    \item \textbf{Operational Commitment}: Specific technology/market choice; forecloses alternatives (e.g., Better Place: ``battery swapping infrastructure'')
\end{itemize}

\section{Design Principles (Chapter~\ref{ch:design})}

\begin{itemize}
    \item \textbf{Strategic Ambiguity} (\S\ref{sec:strategic-ambiguity}): Commit to direction, not destination. Vision-level commitment attracts diverse believers; operational commitment attracts homogeneous believers.
    \item \textbf{Balanced Growth} (\S\ref{sec:balanced-growth}): Growth = Market $\times$ Ops. Diagnose which bottleneck threatens and fix it before locking in the other dimension. (Diagonal Principle)
    \item \textbf{Financial Vehicle} (\S\ref{sec:financial-vehicle}): Sequence funding sources. Climb the Funding Ladder (government grants $\rightarrow$ matching grants $\rightarrow$ thesis-driven VCs) so flexibility survives until market signals clarify.
    \item \textbf{Symmetry Principle}: Founders should stage operational commitments as VCs stage financial commitments.
    \item \textbf{Preserving Skeptics}: Actively recruit investors with distinct theses; reserve board seats for independent directors; institute red-team decision rules.
\end{itemize}


\chapter{Supplementary Notes}
\label{app:e}

\section{Non-Dilutive Alternatives}

The Quantum exception suggests deep tech ventures may benefit from non-dilutive funding:
\begin{itemize}
    \item \textbf{Government grants}: NSF, DARPA, DOE
    \item \textbf{Strategic partnerships}: Corporate R\&D agreements
    \item \textbf{Prize competitions}: XPRIZE-style awards
\end{itemize}
