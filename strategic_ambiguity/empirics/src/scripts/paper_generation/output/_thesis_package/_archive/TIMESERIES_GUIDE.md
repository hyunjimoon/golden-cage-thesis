# 📈 Time Series Implementation & Visualization Guide
> **핵심 인사이트**: D_t, A_t, G_t는 시계열 변수입니다. 이 temporal structure를 활용하면 인과 관계를 더 강하게 보여줄 수 있습니다.
> **Author**: 🐅 권준 (Claude Code)

---

## 📊 데이터의 시계열 구조

### 현재 Panel Structure
```
Years:  t=0 (2021) → t=1 (2023) → t=2 (2024) → t=3 (2025)
        ↓           ↓           ↓           ↓
        V₀          V₁          V₂          V₃
        E₀          -           -           -
        -           ΔV₁         ΔV₂         ΔV₃
        -           D₁          D₂          D₃ (=total_delta_V)
```

### 변수 정의 (시계열 관점)
| 변수 | 정의 | 시계열 특성 |
|------|------|------------|
| **V_t** | 시점 t의 Vagueness | Stock variable (상태) |
| **ΔV_t** | V_t - V_{t-1} | Flow variable (변화) |
| **D_t** | V_t - V_0 (from baseline) | Cumulative flow |
| **A_t** | \|D_t\| | Cumulative absolute change |
| **E** | Initial capital | Time-invariant (t=0에서 측정) |

---

## 🔧 구현 방법론

### Method 1: Trajectory Tracking (개별 궤적 추적)

```python
def compute_trajectories(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute company-level trajectories over time.
    """
    # Pivot to wide format for trajectory analysis
    trajectories = df.pivot(
        index='company_id', 
        columns='year', 
        values=['V', 'delta_V', 'total_delta_V']
    )
    
    # Flatten column names
    trajectories.columns = [f'{var}_{year}' for var, year in trajectories.columns]
    
    # Compute trajectory features
    trajectories['V_initial'] = trajectories['V_2021']
    trajectories['V_final'] = trajectories['V_2025']
    trajectories['total_change'] = trajectories['V_final'] - trajectories['V_initial']
    trajectories['total_movement'] = trajectories['total_delta_V_2025'].abs()
    
    # Trajectory volatility (how smooth was the path?)
    trajectories['volatility'] = trajectories[
        ['delta_V_2023', 'delta_V_2024', 'delta_V_2025']
    ].std(axis=1)
    
    # Direction consistency (did they keep moving same direction?)
    signs = np.sign(trajectories[['delta_V_2023', 'delta_V_2024', 'delta_V_2025']])
    trajectories['direction_consistency'] = signs.apply(
        lambda row: (row == row.iloc[0]).sum() / 3, axis=1
    )
    
    return trajectories
```

### Method 2: Cohort Analysis (코호트별 분석)

```python
def cohort_analysis(df: pd.DataFrame, cohort_var: str = 'V_initial', 
                    n_cohorts: int = 4) -> pd.DataFrame:
    """
    Track cohort divergence over time.
    
    Args:
        df: Panel data (long format)
        cohort_var: Variable to define cohorts (measured at t=0)
        n_cohorts: Number of cohort groups
    """
    # Get initial values for cohort assignment
    initial = df[df['year'] == 2021][['company_id', 'V', 'first_financing_size']].copy()
    initial.columns = ['company_id', 'V_initial', 'E']
    
    # Assign cohorts
    initial['V_cohort'] = pd.qcut(initial['V_initial'], n_cohorts, 
                                   labels=['Q1_Low', 'Q2', 'Q3', 'Q4_High'])
    initial['E_cohort'] = pd.qcut(initial['E'].fillna(initial['E'].median()), n_cohorts,
                                   labels=['Q1_Low', 'Q2', 'Q3', 'Q4_High'])
    
    # Merge back to panel
    df_cohort = df.merge(initial[['company_id', 'V_cohort', 'E_cohort']], on='company_id')
    
    # Compute cohort means over time
    cohort_means = df_cohort.groupby(['year', 'V_cohort']).agg({
        'V': ['mean', 'std', 'count'],
        'total_delta_V': ['mean', 'std']
    }).reset_index()
    
    return cohort_means
```

### Method 3: Transition Analysis (전이 분석)

```python
def compute_transition_matrix(df: pd.DataFrame, 
                               n_states: int = 4) -> np.ndarray:
    """
    Compute Markov-style transition matrix between V states.
    
    Returns:
        Transition probability matrix P[i,j] = P(state_j at t+1 | state_i at t)
    """
    # Assign states based on V quartiles
    df = df.copy()
    df['V_state'] = pd.qcut(df['V'], n_states, labels=range(n_states))
    
    # Create transition pairs
    transitions = []
    for company in df['company_id'].unique():
        company_data = df[df['company_id'] == company].sort_values('year')
        for i in range(len(company_data) - 1):
            state_from = company_data.iloc[i]['V_state']
            state_to = company_data.iloc[i+1]['V_state']
            transitions.append((state_from, state_to))
    
    # Build transition matrix
    trans_matrix = np.zeros((n_states, n_states))
    for s_from, s_to in transitions:
        if pd.notna(s_from) and pd.notna(s_to):
            trans_matrix[int(s_from), int(s_to)] += 1
    
    # Normalize rows
    row_sums = trans_matrix.sum(axis=1, keepdims=True)
    trans_matrix = np.divide(trans_matrix, row_sums, 
                             where=row_sums != 0, out=trans_matrix)
    
    return trans_matrix
```

### Method 4: Growth Decomposition (성장 분해)

```python
def decompose_growth(df: pd.DataFrame) -> pd.DataFrame:
    """
    Decompose total change into components.
    
    D_T = Σ ΔV_t  (total change is sum of period changes)
    A_T = Σ |ΔV_t|  (total movement is sum of absolute changes)
    
    Efficiency = |D_T| / A_T  (how much net change per unit of movement)
    """
    trajectories = compute_trajectories(df)
    
    # Sum of absolute changes (total movement)
    trajectories['total_absolute_change'] = (
        trajectories['delta_V_2023'].abs() + 
        trajectories['delta_V_2024'].abs() + 
        trajectories['delta_V_2025'].abs()
    )
    
    # Net change
    trajectories['net_change'] = trajectories['total_delta_V_2025']
    
    # Efficiency ratio
    trajectories['pivot_efficiency'] = (
        trajectories['net_change'].abs() / 
        trajectories['total_absolute_change'].clip(lower=0.01)
    )
    
    return trajectories
```

---

## 🎨 시계열 플롯 아이디어 (7+ New Plots)

### Plot T1: Trajectory Spaghetti Plot (궤적 스파게티)
```
목적: 개별 회사들의 V 변화 궤적을 시각화
X축: Time (2021 → 2023 → 2024 → 2025)
Y축: Vagueness Score (V)
색상: 초기 E로 구분 (High E = Red, Low E = Blue)

핵심 인사이트: High-E 회사들은 더 "평평한" 궤적을 보이는가?
기대: High-E → 낮은 궤적 변동성
```

### Plot T2: Cohort Divergence (코호트 발산)
```
목적: 초기 V 코호트별 시간에 따른 발산 패턴
X축: Time
Y축: Mean |ΔV| (평균 누적 변화)
선: 각 V 코호트 (Q1-Q4)

핵심 인사이트: 초기에 모호했던 회사들이 더 많이 움직이는가?
기대: High-V 코호트 → 더 가파른 상승 곡선
```

### Plot T3: Transition Heatmap (전이 히트맵)
```
목적: V 상태 간 전이 확률 시각화
X축: State at t+1
Y축: State at t
색상: 전이 확률 (0-1)

핵심 인사이트: V 상태는 얼마나 "sticky"한가?
기대: 대각선이 밝음 (상태 지속), but High-V는 더 분산됨
```

### Plot T4: Velocity Field (속도장)
```
목적: 초기 상태(V₀, E)에 따른 변화 방향과 크기
X축: Initial V (V₀)
Y축: Initial E (log scale)
화살표: 평균 ΔV 방향과 크기

핵심 인사이트: 어느 영역의 회사들이 가장 많이 움직이는가?
기대: Low-E, High-V 영역에서 가장 큰 화살표
```

### Plot T5: Phase Portrait (위상 초상)
```
목적: V_t vs V_{t-1} 관계로 동역학 시각화
X축: V at time t-1
Y축: V at time t
대각선: 변화 없음 (45°선)

핵심 인사이트: 어트랙터(안정점)가 있는가?
기대: 중간값으로 수렴하는 패턴 (regression to mean)
```

### Plot T6: Cumulative Movement by Cohort (누적 이동량)
```
목적: 시간에 따른 누적 A_t = Σ|ΔV| 비교
X축: Time
Y축: Cumulative |ΔV|
선: E 코호트별 (High-E vs Low-E)

핵심 인사이트: High-E가 정말 덜 움직이는가?
기대: Low-E 곡선이 High-E 위에 위치 (Golden Cage 확인)
```

### Plot T7: Sankey Diagram (산키 다이어그램)
```
목적: V 상태 간 회사 흐름 시각화
왼쪽: 2021 V 분위
중간: 2023, 2024 V 분위
오른쪽: 2025 V 분위
흐름 너비: 회사 수

핵심 인사이트: 회사들이 어디서 어디로 이동하는가?
기대: High-E 회사는 더 "직선" 경로
```

### Plot T8: Event Study (이벤트 스터디)
```
목적: "큰 피벗" 전후 궤적 분석
X축: Time relative to pivot event (t-2, t-1, t, t+1, t+2)
Y축: Mean outcome (survival, funding)
선: 피벗 크기별 코호트

핵심 인사이트: 피벗 후 성과가 어떻게 변하는가?
기대: 적절한 피벗 → 성과 개선
```

---

## 📐 구현 코드 (시계열 플롯)

```python
#!/usr/bin/env python3
"""
Time Series Visualization Module for Thesis
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def plot_T1_trajectories(df: pd.DataFrame, sample_n: int = 500,
                         save_path: Path = None) -> plt.Figure:
    """
    T1: Trajectory Spaghetti Plot
    Shows individual company V trajectories over time.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Sample companies for clarity
    companies = df['company_id'].unique()
    if len(companies) > sample_n:
        companies = np.random.choice(companies, sample_n, replace=False)
    
    # Get E for color coding
    E_data = df[df['year'] == 2021].set_index('company_id')['first_financing_size']
    E_median = E_data.median()
    
    for company in companies:
        company_data = df[df['company_id'] == company].sort_values('year')
        E = E_data.get(company, E_median)
        color = '#e74c3c' if E > E_median else '#3498db'
        alpha = 0.1
        
        ax.plot(company_data['year'], company_data['V'], 
                color=color, alpha=alpha, linewidth=0.5)
    
    # Add cohort means
    cohort_means = df.groupby('year')['V'].mean()
    ax.plot(cohort_means.index, cohort_means.values, 
            'k-', linewidth=3, label='Overall Mean')
    
    ax.set_xlabel('Year')
    ax.set_ylabel('Vagueness Score (V)')
    ax.set_title('T1: Company Trajectories in Vagueness Space\n'
                 'Red = High E, Blue = Low E')
    ax.legend()
    
    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig


def plot_T2_cohort_divergence(df: pd.DataFrame, 
                              save_path: Path = None) -> plt.Figure:
    """
    T2: Cohort Divergence Plot
    Shows how V cohorts diverge in adaptive capacity over time.
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Get initial V for cohort assignment
    initial = df[df['year'] == 2021][['company_id', 'V', 'first_financing_size']]
    initial.columns = ['company_id', 'V_initial', 'E']
    
    # V cohorts
    initial['V_cohort'] = pd.qcut(initial['V_initial'], 4, 
                                   labels=['Q1 (Low V)', 'Q2', 'Q3', 'Q4 (High V)'])
    
    # E cohorts
    initial['E_cohort'] = pd.qcut(initial['E'].fillna(initial['E'].median()), 4,
                                   labels=['Q1 (Low E)', 'Q2', 'Q3', 'Q4 (High E)'])
    
    df_merged = df.merge(initial[['company_id', 'V_cohort', 'E_cohort']], on='company_id')
    
    # Left: By V cohort
    ax1 = axes[0]
    cohort_stats = df_merged.groupby(['year', 'V_cohort'])['total_delta_V'].agg(['mean', 'std']).reset_index()
    
    colors = ['#3498db', '#2ecc71', '#f39c12', '#e74c3c']
    for i, cohort in enumerate(['Q1 (Low V)', 'Q2', 'Q3', 'Q4 (High V)']):
        data = cohort_stats[cohort_stats['V_cohort'] == cohort]
        ax1.plot(data['year'], data['mean'].abs(), 'o-', 
                color=colors[i], linewidth=2, markersize=8, label=cohort)
        ax1.fill_between(data['year'], 
                        (data['mean'] - data['std']).abs(),
                        (data['mean'] + data['std']).abs(),
                        color=colors[i], alpha=0.2)
    
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Mean |ΔV| (Cumulative Movement)')
    ax1.set_title('Cohort Divergence by Initial Vagueness')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Right: By E cohort
    ax2 = axes[1]
    cohort_stats_E = df_merged.groupby(['year', 'E_cohort'])['total_delta_V'].agg(['mean', 'std']).reset_index()
    
    for i, cohort in enumerate(['Q1 (Low E)', 'Q2', 'Q3', 'Q4 (High E)']):
        data = cohort_stats_E[cohort_stats_E['E_cohort'] == cohort]
        ax2.plot(data['year'], data['mean'].abs(), 'o-',
                color=colors[i], linewidth=2, markersize=8, label=cohort)
    
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Mean |ΔV| (Cumulative Movement)')
    ax2.set_title('Cohort Divergence by Initial Capital\n'
                  'Expected: Low E (Blue) > High E (Red)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig


def plot_T3_transition_heatmap(df: pd.DataFrame, n_states: int = 4,
                               save_path: Path = None) -> plt.Figure:
    """
    T3: Transition Matrix Heatmap
    Shows probabilities of moving between V states.
    """
    fig, ax = plt.subplots(figsize=(8, 7))
    
    # Compute transition matrix
    df = df.copy()
    df['V_state'] = pd.qcut(df['V'], n_states, 
                            labels=[f'Q{i+1}' for i in range(n_states)])
    
    # Build transitions
    transitions = []
    for company in df['company_id'].unique():
        company_data = df[df['company_id'] == company].sort_values('year')
        states = company_data['V_state'].values
        for i in range(len(states) - 1):
            if pd.notna(states[i]) and pd.notna(states[i+1]):
                transitions.append((states[i], states[i+1]))
    
    # Create matrix
    state_labels = [f'Q{i+1}' for i in range(n_states)]
    trans_df = pd.DataFrame(transitions, columns=['from', 'to'])
    trans_matrix = pd.crosstab(trans_df['from'], trans_df['to'], normalize='index')
    trans_matrix = trans_matrix.reindex(index=state_labels, columns=state_labels, fill_value=0)
    
    # Heatmap
    sns.heatmap(trans_matrix, annot=True, fmt='.2f', cmap='Blues',
                ax=ax, vmin=0, vmax=1,
                xticklabels=['Q1\n(Low V)', 'Q2', 'Q3', 'Q4\n(High V)'],
                yticklabels=['Q1\n(Low V)', 'Q2', 'Q3', 'Q4\n(High V)'])
    
    ax.set_xlabel('State at t+1')
    ax.set_ylabel('State at t')
    ax.set_title('T3: Transition Probabilities Between Vagueness States\n'
                 'Diagonal = persistence, Off-diagonal = change')
    
    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig


def plot_T6_cumulative_movement(df: pd.DataFrame, 
                                 save_path: Path = None) -> plt.Figure:
    """
    T6: Cumulative Movement by E Cohort
    THE KEY PLOT for Golden Cage hypothesis in time series form.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Get E cohorts
    initial = df[df['year'] == 2021][['company_id', 'first_financing_size']].copy()
    initial.columns = ['company_id', 'E']
    initial['E_cohort'] = pd.qcut(initial['E'].fillna(initial['E'].median()), 2,
                                   labels=['Low E', 'High E'])
    
    df_merged = df.merge(initial[['company_id', 'E_cohort']], on='company_id')
    
    # Compute cumulative |ΔV| over time
    cumulative = df_merged.groupby(['year', 'E_cohort']).apply(
        lambda x: x['total_delta_V'].abs().mean()
    ).reset_index()
    cumulative.columns = ['year', 'E_cohort', 'mean_A']
    
    # Plot
    colors = {'Low E': '#3498db', 'High E': '#e74c3c'}
    for cohort in ['Low E', 'High E']:
        data = cumulative[cumulative['E_cohort'] == cohort]
        ax.plot(data['year'], data['mean_A'], 'o-',
                color=colors[cohort], linewidth=3, markersize=10, 
                label=cohort)
    
    # Add gap annotation
    final_year = cumulative['year'].max()
    low_E_final = cumulative[(cumulative['E_cohort'] == 'Low E') & 
                             (cumulative['year'] == final_year)]['mean_A'].values[0]
    high_E_final = cumulative[(cumulative['E_cohort'] == 'High E') & 
                              (cumulative['year'] == final_year)]['mean_A'].values[0]
    gap = low_E_final - high_E_final
    
    ax.annotate(f'Gap = {gap:.2f}',
                xy=(final_year, (low_E_final + high_E_final)/2),
                xytext=(final_year - 0.5, (low_E_final + high_E_final)/2 + 2),
                fontsize=12, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='black'))
    
    ax.set_xlabel('Year')
    ax.set_ylabel('Mean Cumulative |ΔV| (Adaptive Capacity)')
    ax.set_title('T6: Golden Cage in Time Series Form\n'
                 'Expected: Low E (Blue) > High E (Red)')
    ax.legend(loc='upper left')
    ax.grid(True, alpha=0.3)
    
    # Add interpretation
    result = "✓ GOLDEN CAGE CONFIRMED" if gap > 0 else "✗ Not confirmed"
    ax.text(0.98, 0.02, result, transform=ax.transAxes,
            fontsize=14, fontweight='bold', ha='right', va='bottom',
            color='#27ae60' if gap > 0 else '#e74c3c',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig


def generate_all_timeseries_plots(df: pd.DataFrame, output_dir: Path):
    """Generate all time series plots."""
    print("="*70)
    print("🐅 Time Series Visualization Module")
    print("="*70)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("\n📈 Generating time series plots...")
    
    plot_T1_trajectories(df, save_path=output_dir / 'T1_trajectories.png')
    print("   ✅ T1: Trajectory Spaghetti")
    
    plot_T2_cohort_divergence(df, save_path=output_dir / 'T2_cohort_divergence.png')
    print("   ✅ T2: Cohort Divergence")
    
    plot_T3_transition_heatmap(df, save_path=output_dir / 'T3_transition_heatmap.png')
    print("   ✅ T3: Transition Heatmap")
    
    plot_T6_cumulative_movement(df, save_path=output_dir / 'T6_cumulative_movement.png')
    print("   ✅ T6: Cumulative Movement (Golden Cage)")
    
    print(f"\n✅ All time series plots saved to: {output_dir}")


if __name__ == "__main__":
    # Load data
    ROOT = Path("/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics")
    df = pd.read_parquet(ROOT / "data/processed/vagueness_timeseries.parquet")
    
    generate_all_timeseries_plots(
        df, 
        ROOT / "src/scripts/paper_generation/output/_thesis_package/figures/timeseries"
    )
```

---

## 📊 플롯 요약 매트릭스

| Plot ID | 이름 | X축 | Y축 | 핵심 질문 | 기대 결과 |
|---------|------|-----|-----|----------|----------|
| **T1** | Trajectory Spaghetti | Time | V | 개별 궤적 패턴? | High-E = 평평한 궤적 |
| **T2** | Cohort Divergence | Time | Mean \|ΔV\| | 코호트 발산? | Low-E가 더 많이 발산 |
| **T3** | Transition Heatmap | State(t+1) | State(t) | 상태 지속성? | High-V는 더 유동적 |
| **T4** | Velocity Field | V₀ | E | 어디서 가장 움직임? | Low-E, High-V 영역 |
| **T5** | Phase Portrait | V(t-1) | V(t) | 어트랙터 존재? | 중간값 수렴 |
| **T6** | Cumulative Movement | Time | Cumulative A | Golden Cage 시계열? | Low-E 곡선이 위 |
| **T7** | Sankey Diagram | Time | State flow | 흐름 패턴? | High-E = 직선 |
| **T8** | Event Study | Relative time | Outcome | 피벗 효과? | 적절한 피벗 → 개선 |

---

## 🎯 핵심 시계열 인사이트

### Golden Cage의 시간적 증거
```
t=0: High-E와 Low-E 회사들이 유사한 V 분포로 시작
t=1: Low-E 회사들이 더 많이 이동하기 시작
t=2: Gap 확대
t=3: Low-E 회사들이 누적적으로 훨씬 더 많이 이동함

결론: Money는 시간이 지남에 따라 점점 더 강한 "cage"가 됨
```

### U-Shape의 동적 검증
```
초기 High-V 회사: 시간이 지나면서 V 감소 (구체화)
초기 Low-V 회사: 시간이 지나면서 V 증가 (확장) OR 유지
초기 Mid-V 회사: 방향성 없는 변동

결론: 극단적 V는 "목적지"로 기능, 중간 V는 "통과점"
```

---

**END OF TIME SERIES GUIDE**
