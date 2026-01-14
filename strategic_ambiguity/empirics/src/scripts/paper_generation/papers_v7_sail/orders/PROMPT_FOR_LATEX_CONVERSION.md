# 🐢 정운에게: LaTeX 변환 요청

**Last Updated: 2026-01-14 v2.0**

## 📋 Mission
`Thesis_Master.md`의 콘텐츠를 **기존 MIT thesis LaTeX 템플릿**에 맞춰 변환해주세요.
템플릿 구조를 유지하면서 콘텐츠만 교체하고, **컴파일 가능한 업데이트된 zip 파일**을 반환해주세요.

---

## 📁 전달 파일 목록

### 1. 필수 파일
| 파일 | 용도 | 상태 |
|------|------|------|
| `Thesis_Master.md` | **원본 콘텐츠** (6개 Chapter, v7.1) | ✅ 최신 |
| `Thesis_LaTeX_Format/` 폴더 | **기존 MIT thesis 템플릿** | ✅ 구조 유지 |
| `figures/*.png` (12개) | **Figure 파일들** | ✅ Grayscale 적용 완료 |

---

## 📂 기존 템플릿 구조 (Thesis_LaTeX_Format/)

```
Thesis_LaTeX_Format/
├── MIT-Thesis.pdf              # 기존 출력 결과 (참조용)
├── mitthesis.cls               # MIT class 파일 (유지)
├── README.md
├── MIT-thesis-template/        # ⭐ 작업 대상 폴더
│   ├── MIT-Thesis.tex          # Main file (수정)
│   ├── abstract.tex            # Abstract (교체)
│   ├── introduction.tex        # Chapter 1 (교체)
│   ├── paper_M.tex             # → chapter2_mechanism.tex로 교체
│   ├── paper_V.tex             # → chapter3_data.tex로 교체
│   ├── paper_E.tex             # → chapter4_results.tex로 교체
│   ├── discussion.tex          # → chapter5_design.tex로 교체
│   ├── conclusion.tex          # Chapter 6 (교체)
│   ├── statistics_summary.tex  # 통계 요약 (업데이트)
│   ├── mydesign.tex            # 디자인 설정 (유지)
│   ├── mitthesis-sample.bib    # 참고문헌 (교체)
│   ├── bib/
│   │   └── bib(U).bib          # 추가 참고문헌
│   ├── img/                    # ⭐ Figure 폴더 (교체)
│   │   └── (기존 이미지들)
│   ├── table/                  # Table 정의
│   │   ├── variable.tex        # 변수 정의 테이블 (교체)
│   │   └── litrev.tex          # 문헌 리뷰 테이블
│   ├── fontsets/               # 폰트 설정 (유지)
│   └── spandrel/               # 예시 챕터 (삭제 가능)
├── examples/                   # 예시 파일들 (유지)
└── mitthesis-doc/              # 문서 (유지)
```

---

## 🎯 변환 요구사항

### A. Chapter 매핑 (Thesis_Master.md → LaTeX)

| Thesis_Master.md | LaTeX 파일 | 비고 |
|------------------|------------|------|
| Abstract (¶1-3) | `abstract.tex` | 교체 |
| Chapter 1: Introduction | `introduction.tex` | 교체 |
| Chapter 2: Golden Cage Mechanism | `chapter2_mechanism.tex` | **새 파일** |
| Chapter 3: Data and Identification | `chapter3_data.tex` | **새 파일** |
| Chapter 4: Where the Cage Bites | `chapter4_results.tex` | **새 파일** |
| Chapter 5: Designing for Flexibility | `chapter5_design.tex` | **새 파일** |
| Chapter 6: Conclusion | `conclusion.tex` | 교체 |
| References | `golden_cage.bib` | **새 파일** |

### B. Figure 교체 (figures/ → img/)

**⚠️ 중요: 모든 Figure는 GRAYSCALE 기반 (총 11개)**

| # | 파일명 | Chapter | 내용 | 색상 |
|:--|:-------|:--------|:-----|:-----|
| 1 | `Ch1_Fig1_capital_paradox.png` | Ch.1 | E vs G negative correlation | Grayscale |
| 2 | `Ch1_Fig2_mediation_dag.png` | Ch.1 | E → R → G mediation DAG | B&W with labels |
| 3 | `Ch2_Fig1_B_trajectories.png` | Ch.2 | B evolution by archetype | Grayscale + accent |
| 4 | `Ch2_Fig2_golden_cage.png` | Ch.2 | E vs R negative correlation | Grayscale |
| 5 | `Ch4_Fig1_mover_advantage.png` | Ch.4 | Mover vs Stayer success (2.02×) | Grayscale ✅ |
| 6 | `Ch4_Fig2_industry_rho.png` | Ch.4 | ρ(E,G) by industry | Grayscale ✅ |
| 7 | `Ch4_Fig3_growth_by_direction.png` | Ch.4 | B Trajectories + Growth by direction | Grayscale ✅ |
| 8 | `Ch4_Fig4_industry_survival.png` | Ch.4 | Survival by industry | Grayscale |
| 9 | `Ch4_Fig5_mover_vs_stayer.png` | Ch.4 | Mover taxonomy | Grayscale |
| 10 | `Ch5_Fig1_sweet_spot.png` | Ch.5 | B quartile analysis | Grayscale |
| 11 | `Ch6_Fig1_growth_diagnostics.png` | Ch.6 | Growth Diagnostics (Fine-Hausmann) | Grayscale |

**Figure 복사 매핑 (그대로 복사):**
```
papers_v7_sail/figures/              →  MIT-thesis-template/img/
├── Ch1_Fig1_capital_paradox.png     →  Ch1_Fig1_capital_paradox.png
├── Ch1_Fig2_mediation_dag.png       →  Ch1_Fig2_mediation_dag.png
├── Ch2_Fig1_B_trajectories.png      →  Ch2_Fig1_B_trajectories.png
├── Ch2_Fig2_golden_cage.png         →  Ch2_Fig2_golden_cage.png
├── Ch4_Fig1_mover_advantage.png     →  Ch4_Fig1_mover_advantage.png
├── Ch4_Fig2_industry_rho.png        →  Ch4_Fig2_industry_rho.png
├── Ch4_Fig3_growth_by_direction.png →  Ch4_Fig3_growth_by_direction.png
├── Ch4_Fig4_industry_survival.png   →  Ch4_Fig4_industry_survival.png
├── Ch4_Fig5_mover_vs_stayer.png     →  Ch4_Fig5_mover_vs_stayer.png
├── Ch5_Fig1_sweet_spot.png          →  Ch5_Fig1_sweet_spot.png
└── Ch6_Fig1_growth_diagnostics.png  →  Ch6_Fig1_growth_diagnostics.png
```

### C. Table 처리 (11개)

Thesis_Master.md의 Markdown 테이블들을 `table/` 폴더에 LaTeX로 변환:

| Table # | 내용 | 파일명 |
|---------|------|--------|
| Table 1 | Variable Definitions | `table/variable.tex` (교체) |
| Table 2 | Descriptive Statistics | `table/descriptive.tex` |
| Table 4 | FRG Analysis | `table/frg_analysis.tex` |
| Table 5a-c | Mover Taxonomy | `table/mover_taxonomy.tex` |
| Table 6 | Industry Breakdown | `table/industry.tex` |
| Table 7 | Robustness Tests | `table/robustness.tex` |
| Table 8-9 | Governance Design | `table/governance.tex` |
| Table 10 | Alternative Explanations | `table/alternatives.tex` |

### D. MIT-Thesis.tex 수정사항

```latex
% 기존 include 구문을 새 챕터 파일로 교체
\include{introduction}           % Chapter 1
\include{chapter2_mechanism}     % Chapter 2 (NEW)
\include{chapter3_data}          % Chapter 3 (NEW)
\include{chapter4_results}       % Chapter 4 (NEW)
\include{chapter5_design}        % Chapter 5 (NEW)
\include{conclusion}             % Chapter 6

% Bibliography 설정
\addbibresource{golden_cage.bib} % NEW
```

### E. BibTeX 변환

Thesis_Master.md의 REFERENCES 섹션(약 40개)을 `golden_cage.bib`로 변환:
```bibtex
@article{jensen1976theory,
  author  = {Jensen, Michael C. and Meckling, William H.},
  title   = {Theory of the firm: Managerial behavior, agency costs and ownership structure},
  journal = {Journal of Financial Economics},
  year    = {1976},
  volume  = {3},
  number  = {4},
  pages   = {305--360}
}
```

---

## 🔢 Canonical Numbers (변경 금지)

| Variable | Value | LaTeX |
|----------|-------|-------|
| ρ(E,G) | −0.196*** | `$\rho = -0.196^{***}$` |
| N | 180,994 | `$N = 180{,}994$` |
| Mover Advantage | 2.60× | `$2.60\times$` |
| ρ(E,R) | −0.087*** | `$\rho = -0.087^{***}$` |

---

## 📐 LaTeX 스타일 가이드

### Figure 형식

**Ch1_Fig1 Capital Paradox:**
```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.85\textwidth]{img/Ch1_Fig1_capital_paradox.png}
    \caption{The Funding-Growth Paradox. Higher early funding correlates with
    lower later-stage success ($N = 180{,}994$, $\rho = -0.196$, $p < 0.001$).}
    \label{fig:capital-paradox}
\end{figure}
```

**Ch1_Fig2 Mediation DAG:**
```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.9\textwidth]{img/Ch1_Fig2_mediation_dag.png}
    \caption{The Mediation Structure (DAG). \textbf{Upper path (measured):}
    Early Funding $\rightarrow$ Reposition $\rightarrow$ Growth.
    H1 (Commitment Trap, $-$): Funding suppresses repositioning.
    H2 (Flexibility Premium, $+$): Repositioning enables growth.
    H3 (Funding Paradox, $-$): Net effect shown by dashed arc.
    \textbf{Lower path (latent):} Commitment enables funding ($+$) but destroys Flexibility ($-$).}
    \label{fig:mediation-dag}
\end{figure}
```

**Ch4_Fig1 Mover Advantage (GRAYSCALE):**
```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.75\textwidth]{img/Ch4_Fig1_mover_advantage.png}
    \caption{Growth by Repositioning: ``Move to Grow.'' Movers ($R > 0$) achieve
    $2.02\times$ higher success rates than Stayers ($R = 0$). $N = 168{,}011$,
    $\chi^2 = 2{,}622^{***}$.}
    \label{fig:mover-advantage}
\end{figure}
```

**Ch4_Fig3 Growth by Direction:**
```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=\textwidth]{img/Ch4_Fig3_growth_by_direction.png}
    \caption{Growth by Strategic Direction. \textbf{Upper:} B trajectories by archetype
    (2021--2025). Narrowing movers ($B\downarrow$, $n=24{,}159$, 21\%) focus;
    stayers ($B=$, $n=62{,}567$, 53\%) maintain; broadening movers ($B\uparrow$,
    $n=30{,}277$, 26\%) expand. \textbf{Lower:} Both directions achieve higher
    median growth ($\sim 2.8\times$) than stayers ($\sim 0.6\times$).}
    \label{fig:growth-direction}
\end{figure}
```

**Ch6_Fig1 Growth Diagnostics (Fine-Hausmann):**
```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=\textwidth]{img/Ch6_Fig1_growth_diagnostics.png}
    \caption{Startup Growth Diagnostics. \textbf{Panel A:} The Anatomy of Growth
    (Fine's Scale-it Framework). $G = \text{Market} \times \text{Ops}$---only filled
    area represents true value. Type A: Operational Trap; Type B: Market Mirage;
    Type C: Balanced Engine. \textbf{Panel B:} Growth Diagnostics Tree (Hausmann adaptation).
    Golden Cage identified as supply-side resource constraint where $E\uparrow \rightarrow R\downarrow$.}
    \label{fig:growth-diagnostics}
\end{figure}
```

### Table 형식
```latex
\begin{table}[htbp]
    \centering
    \caption{Variable Definitions and Causal Structure}
    \label{tab:variables}
    \begin{tabular}{@{}clll@{}}
        \toprule
        Symbol & Variable & Type & Operationalization \\
        \midrule
        C & Commitment & Choice & Initial strategic specificity index \\
        E & Early Funding & Outcome & First financing size (M USD) \\
        \bottomrule
    \end{tabular}
\end{table}
```

### Cross-reference
```latex
Figure~\ref{fig:capital-paradox}
Table~\ref{tab:variables}
Chapter~\ref{ch:mechanism}
```

---

## ✅ 반환 요청

1. **업데이트된 zip 파일** (`Thesis_LaTeX_Format_Updated.zip`)
   - 기존 템플릿 구조 유지
   - 콘텐츠만 교체/추가

2. **컴파일 명령어**:
   ```bash
   cd MIT-thesis-template
   pdflatex MIT-Thesis.tex
   biber MIT-Thesis
   pdflatex MIT-Thesis.tex
   pdflatex MIT-Thesis.tex
   ```

3. **변환 노트**: 수동 확인이 필요한 부분 목록

---

## ⚠️ 주의사항

1. **mitthesis.cls 유지**: MIT 공식 클래스 파일 수정 금지
2. **fontsets/ 유지**: 폰트 설정 파일들 유지
3. **기존 img/ 정리**: 사용하지 않는 기존 이미지 삭제
4. **spandrel/ 삭제 가능**: 예시 챕터 폴더는 삭제해도 됨
5. **Grayscale 우선**: 모든 Figure는 grayscale 기반, 색상 최소화

---

## 📊 2026-01-14 업데이트 사항

| 항목 | 변경 내용 |
|:-----|:---------|
| Fig4_growth_by_R.png | → `Ch4_Fig1_mover_advantage.png` (Grayscale, 노란색 제거) |
| Fig5_industry_rho.png | → `Ch4_Fig2_industry_rho.png` (Grayscale only) |
| growth_mover_stayer.png | → `Ch4_Fig3_growth_by_direction.png` (NEW, 본문 삽입) |
| Fig1b_mediation_dag.png | Caption 업데이트 (H1/H2/H3 명확화) |
| Fig9_balanced_growth.png | Fine-Hausmann 프레임워크 적용 |

---

감사합니다! 🐢
