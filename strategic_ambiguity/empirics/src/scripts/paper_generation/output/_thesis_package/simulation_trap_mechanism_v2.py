"""
simulation_trap_mechanism_v2.py
Paper T: Generative Sufficiency Simulation

김완(🐙k)의 k-4 피드백 반영:
1. 변수 정의 명확화: learning_resistance → path_flexibility + vision_commitment
2. 생존 편향 추가: H1(초기 자금 패널티) + 초기 사망 메커니즘
3. 확률적 매칭: 결정론적 → P(Believer|V) = 0.3 + 0.4*V (노이즈 포함)

Author: 🐅 g (04_G🟠)
Reviewer: 🐙 k (01_K🔴)
Date: 2025-12-11
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ==============================================================================
# 1. CONFIGURATION
# ==============================================================================
np.random.seed(42)
N = 2000  # Number of ventures
T = 100   # Time periods

# Vagueness: continuous [0, 1] instead of binary
V = np.random.beta(2, 2, N)  # Bell-shaped distribution around 0.5

# ==============================================================================
# 2. INVESTOR MATCHING (김완 지적 #3: 확률적 매칭)
# ==============================================================================
def match_investor(v_value):
    """
    확률적 매칭 (김완 피드백 반영)
    - V=0: P(Believer) = 0.3 (노이즈: 명확해도 Believer 붙을 수 있음)
    - V=1: P(Believer) = 0.7 (노이즈: 모호해도 Analyst 붙을 수 있음)
    - 선형 보간: P(Believer|V) = 0.3 + 0.4 * V
    """
    believer_prob = 0.3 + 0.4 * v_value  # V=0 → 30%, V=1 → 70%
    analyst_prob = 1 - believer_prob
    return np.random.choice(['analyst', 'believer'], p=[analyst_prob, believer_prob])

investor_types = np.array([match_investor(v) for v in V])

# ==============================================================================
# 3. INVESTOR CHARACTERISTICS (김완 지적 #1: 변수 정의 명확화)
# ==============================================================================
def get_investor_characteristics(investor_type):
    """
    김완 피드백 반영: Vision vs Path 분리
    
    Analyst: 
        - High vision_commitment (목표에 집착)
        - Low path_flexibility (방법론 변경 거부)
        - High pivot_cost (피벗 비용 높음)
    
    Believer:
        - High vision_commitment (창업자 비전에 헌신)
        - High path_flexibility (방법론 변경 허용)
        - Low pivot_cost (피벗 비용 낮음)
        
    핵심: 둘 다 vision_commitment는 높음. 차이는 path_flexibility!
    """
    if investor_type == 'analyst':
        return {
            'vision_commitment': 0.9,    # 둘 다 높음 (목표 중시)
            'path_flexibility': 0.2,     # 낮음: 계획 변경 거부
            'pivot_cost': 2.0,           # 높음: 피벗 비용
            'variance_tolerance': 0.1    # 낮음: 불확실성 회피
        }
    else:  # believer
        return {
            'vision_commitment': 0.9,    # 둘 다 높음 (창업자 비전에 헌신)
            'path_flexibility': 0.8,     # 높음: 방법론 변경 허용
            'pivot_cost': 0.5,           # 낮음: 피벗 비용
            'variance_tolerance': 0.9    # 높음: 불확실성 수용
        }

# ==============================================================================
# 4. INITIAL FUNDING (김완 지적 #2: H1 반영 - 초기 자금 패널티)
# ==============================================================================
def calculate_initial_funding(v_value, investor_type):
    """
    H1: Vague → Lower early funding (α₁ < 0)
    
    - 기본 자금: $1M
    - Vagueness 패널티: -0.3 * V (모호할수록 적게 받음)
    - Analyst 프리미엄: +0.2 (Analyst는 더 많이 투자)
    - 노이즈: ±0.1
    """
    base_funding = 1.0  # $1M baseline
    vagueness_penalty = -0.3 * v_value  # H1: vague = less funding
    analyst_premium = 0.2 if investor_type == 'analyst' else 0.0
    noise = np.random.normal(0, 0.1)
    
    initial_funding = max(0.1, base_funding + vagueness_penalty + analyst_premium + noise)
    return initial_funding

initial_funding = np.array([
    calculate_initial_funding(V[i], investor_types[i]) 
    for i in range(N)
])

# ==============================================================================
# 5. SURVIVAL MECHANISM (김완 지적 #2: 초기 사망)
# ==============================================================================
def determine_survival(initial_funding, v_value):
    """
    초기 자금 부족으로 인한 사망 (Death by Starvation)
    
    - 생존 확률 = sigmoid(funding - threshold)
    - threshold = 0.5 (최소 생존 자금)
    - Vague 기업은 funding이 낮으므로 초기 사망률 높음
    """
    threshold = 0.5
    survival_logit = 3 * (initial_funding - threshold)  # steepness = 3
    survival_prob = 1 / (1 + np.exp(-survival_logit))
    return np.random.random() < survival_prob

survived = np.array([
    determine_survival(initial_funding[i], V[i]) 
    for i in range(N)
])

print(f"Initial Survival Rate: {survived.mean()*100:.1f}%")
print(f"  V < 0.5 survival: {survived[V < 0.5].mean()*100:.1f}%")
print(f"  V >= 0.5 survival: {survived[V >= 0.5].mean()*100:.1f}%")

# ==============================================================================
# 6. GROWTH SIMULATION (생존자만)
# ==============================================================================
adaptability = np.zeros(N)
growth = np.zeros(N)
pivot_count = np.zeros(N, dtype=int)

for t in range(T):
    market_shock = np.random.normal(0, 1, N)
    
    for i in range(N):
        if not survived[i]:
            continue  # 사망한 기업은 스킵
            
        characteristics = get_investor_characteristics(investor_types[i])
        
        # Adaptability: path_flexibility가 높을수록 시장 충격에 적응
        adaptation = market_shock[i] * characteristics['path_flexibility'] * 0.3
        adaptability[i] += adaptation
        
        # 피벗 카운트 (adaptation이 threshold 초과 시)
        if abs(adaptation) > 0.1:
            pivot_count[i] += 1
        
        # Growth = adaptability benefit - pivot cost
        adaptability_benefit = abs(adaptability[i]) * 2.0
        change_cost = characteristics['pivot_cost'] * abs(adaptability[i])
        growth[i] += max(0, adaptability_benefit - change_cost)

# ==============================================================================
# 7. RESULTS COMPILATION
# ==============================================================================
results_df = pd.DataFrame({
    'venture_id': range(N),
    'vague': V,
    'vague_quartile': pd.qcut(V, 4, labels=['Q1', 'Q2', 'Q3', 'Q4']),
    'investor_type': investor_types,
    'initial_funding': initial_funding,
    'survived': survived,
    'adaptability': adaptability,
    'pivot_count': pivot_count,
    'final_growth': growth
})

# ==============================================================================
# 8. 김완 검증 프로토콜 실행
# ==============================================================================
def verify_generative_sufficiency(df):
    """
    김완(Gim Wan)의 검증 프로토콜:
    시뮬레이션 결과 데이터가 이론적 기준을 충족하는지 자동 판별
    """
    print("\n" + "="*60)
    print("[🐙 김완] Paper T Generative Sufficiency Check")
    print("="*60)
    
    # 생존자만 필터링 (생존 조건부 분석)
    survivors = df[df['survived'] == True]
    
    # 1. H1 Check: 초기 자금 조달 (Vague가 더 힘들어야 함)
    mean_fund_vague = df[df['vague'] > 0.5]['initial_funding'].mean()
    mean_fund_specific = df[df['vague'] <= 0.5]['initial_funding'].mean()
    h1_pass = mean_fund_vague < mean_fund_specific
    print(f"\n1. H1 (Funding Penalty): {'✅ PASS' if h1_pass else '❌ FAIL'}")
    print(f"   V>0.5: ${mean_fund_vague:.2f}M < V≤0.5: ${mean_fund_specific:.2f}M")
    
    # 2. 초기 사망률 (Vague가 더 높아야 함)
    death_rate_vague = 1 - df[df['vague'] > 0.5]['survived'].mean()
    death_rate_specific = 1 - df[df['vague'] <= 0.5]['survived'].mean()
    survival_bias_pass = death_rate_vague > death_rate_specific
    print(f"\n2. Survival Bias (H1 consequence): {'✅ PASS' if survival_bias_pass else '❌ FAIL'}")
    print(f"   Death rate V>0.5: {death_rate_vague*100:.1f}% > V≤0.5: {death_rate_specific*100:.1f}%")
    
    # 3. H2 Check: 최종 성장 - 생존자 중에서 (Conditional on survival)
    mean_growth_vague = survivors[survivors['vague'] > 0.5]['final_growth'].mean()
    mean_growth_specific = survivors[survivors['vague'] <= 0.5]['final_growth'].mean()
    h2_pass = mean_growth_vague > mean_growth_specific
    print(f"\n3. H2 (Growth Benefit | Survived): {'✅ PASS' if h2_pass else '❌ FAIL'}")
    print(f"   V>0.5: {mean_growth_vague:.2f} > V≤0.5: {mean_growth_specific:.2f}")
    
    # 4. Variance Check: Vague의 결과가 더 극단적이어야 함
    std_growth_vague = survivors[survivors['vague'] > 0.5]['final_growth'].std()
    std_growth_specific = survivors[survivors['vague'] <= 0.5]['final_growth'].std()
    variance_pass = std_growth_vague > std_growth_specific
    print(f"\n4. Variance (Risk Profile): {'✅ PASS' if variance_pass else '❌ FAIL'}")
    print(f"   Std V>0.5: {std_growth_vague:.2f} > V≤0.5: {std_growth_specific:.2f}")
    
    # 5. Mechanism Check: Pivot-Growth 상관관계
    corr_pivot_growth = survivors['pivot_count'].corr(survivors['final_growth'])
    mechanism_pass = corr_pivot_growth > 0.3
    print(f"\n5. Pivot-Growth Link: {'✅ PASS' if mechanism_pass else '⚠️ WEAK'}")
    print(f"   Correlation: {corr_pivot_growth:.3f}")
    
    # 6. Investor Type Mediation
    analyst_growth = survivors[survivors['investor_type'] == 'analyst']['final_growth'].mean()
    believer_growth = survivors[survivors['investor_type'] == 'believer']['final_growth'].mean()
    mediation_pass = believer_growth > analyst_growth
    print(f"\n6. Investor Mediation: {'✅ PASS' if mediation_pass else '❌ FAIL'}")
    print(f"   Believer: {believer_growth:.2f} > Analyst: {analyst_growth:.2f}")
    
    # 7. 확률적 매칭 확인 (결정론적이 아님)
    v_high = df[df['vague'] > 0.7]
    v_low = df[df['vague'] < 0.3]
    believer_rate_high = (v_high['investor_type'] == 'believer').mean()
    believer_rate_low = (v_low['investor_type'] == 'believer').mean()
    stochastic_pass = believer_rate_high < 1.0 and believer_rate_low > 0.0
    print(f"\n7. Stochastic Matching: {'✅ PASS' if stochastic_pass else '❌ FAIL (Deterministic!)'}")
    print(f"   P(Believer|V>0.7): {believer_rate_high*100:.1f}%")
    print(f"   P(Believer|V<0.3): {believer_rate_low*100:.1f}%")
    
    print("\n" + "="*60)
    all_pass = all([h1_pass, survival_bias_pass, h2_pass, variance_pass, mechanism_pass, mediation_pass, stochastic_pass])
    if all_pass:
        print("🎖️ REPORT: General, the strategy is theoretically sound.")
    else:
        print("⚠️ REPORT: General, review failed checks above.")
    print("="*60)
    
    return {
        'H1_funding_penalty': h1_pass,
        'survival_bias': survival_bias_pass,
        'H2_growth_benefit': h2_pass,
        'variance_risk': variance_pass,
        'pivot_growth_link': mechanism_pass,
        'investor_mediation': mediation_pass,
        'stochastic_matching': stochastic_pass
    }

# 검증 실행
verification_results = verify_generative_sufficiency(results_df)

# ==============================================================================
# 9. VISUALIZATION
# ==============================================================================
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Plot 1: Initial Funding by Vagueness (H1)
ax1 = axes[0, 0]
survivors_df = results_df[results_df['survived']]
dead_df = results_df[~results_df['survived']]
ax1.scatter(dead_df['vague'], dead_df['initial_funding'], alpha=0.3, c='red', label='Failed', s=10)
ax1.scatter(survivors_df['vague'], survivors_df['initial_funding'], alpha=0.3, c='green', label='Survived', s=10)
ax1.set_xlabel('Vagueness (V)')
ax1.set_ylabel('Initial Funding ($M)')
ax1.set_title('H1: Vague → Lower Funding → Higher Death')
ax1.legend()

# Plot 2: Survival Rate by Vagueness Quartile
ax2 = axes[0, 1]
survival_by_q = results_df.groupby('vague_quartile')['survived'].mean()
bars = ax2.bar(survival_by_q.index, survival_by_q.values, color=['#d62728', '#ff7f0e', '#2ca02c', '#1f77b4'])
ax2.set_xlabel('Vagueness Quartile')
ax2.set_ylabel('Survival Rate')
ax2.set_title('Survival Bias: Q1 > Q4 (H1 Consequence)')
ax2.set_ylim(0, 1)
for bar, val in zip(bars, survival_by_q.values):
    ax2.text(bar.get_x() + bar.get_width()/2, val + 0.02, f'{val:.1%}', ha='center')

# Plot 3: Growth by Vagueness (Survivors Only) - H2
ax3 = axes[0, 2]
growth_by_q = survivors_df.groupby('vague_quartile')['final_growth'].mean()
bars = ax3.bar(growth_by_q.index, growth_by_q.values, color=['#d62728', '#ff7f0e', '#2ca02c', '#1f77b4'])
ax3.set_xlabel('Vagueness Quartile')
ax3.set_ylabel('Final Growth (Survivors)')
ax3.set_title('H2: Vague → Higher Growth | Survived')
for bar, val in zip(bars, growth_by_q.values):
    ax3.text(bar.get_x() + bar.get_width()/2, val + 0.5, f'{val:.1f}', ha='center')

# Plot 4: Growth by Investor Type
ax4 = axes[1, 0]
growth_by_investor = survivors_df.groupby('investor_type')['final_growth'].mean()
bars = ax4.bar(growth_by_investor.index, growth_by_investor.values, color=['coral', 'steelblue'])
ax4.set_xlabel('Investor Type')
ax4.set_ylabel('Final Growth')
ax4.set_title('Mechanism: Believer > Analyst')
for bar, val in zip(bars, growth_by_investor.values):
    ax4.text(bar.get_x() + bar.get_width()/2, val + 0.5, f'{val:.1f}', ha='center')

# Plot 5: Pivot Count vs Growth (Mechanism)
ax5 = axes[1, 1]
ax5.scatter(survivors_df['pivot_count'], survivors_df['final_growth'], alpha=0.3, c='purple', s=10)
ax5.set_xlabel('Pivot Count')
ax5.set_ylabel('Final Growth')
ax5.set_title(f'Pivot→Growth (r={survivors_df["pivot_count"].corr(survivors_df["final_growth"]):.2f})')

# Plot 6: Overall Growth Distribution (Multimodal)
ax6 = axes[1, 2]
ax6.hist(results_df[results_df['survived']]['final_growth'], bins=50, alpha=0.7, color='green', label='Survivors', density=True)
ax6.axvline(survivors_df[survivors_df['vague'] > 0.5]['final_growth'].median(), color='blue', linestyle='--', label='Median V>0.5')
ax6.axvline(survivors_df[survivors_df['vague'] <= 0.5]['final_growth'].median(), color='red', linestyle='--', label='Median V≤0.5')
ax6.set_xlabel('Final Growth')
ax6.set_ylabel('Density')
ax6.set_title('Growth Distribution (Survivors)')
ax6.legend()

plt.tight_layout()
plt.savefig('/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/output/_thesis_package/figures/T_fig1_trap_mechanism.png', dpi=150, bbox_inches='tight')
plt.show()

# ==============================================================================
# 10. SUMMARY STATISTICS FOR PAPER
# ==============================================================================
print("\n" + "="*60)
print("SUMMARY STATISTICS FOR PAPER T")
print("="*60)
print(f"\nSample Size: N = {N}")
print(f"Survival Rate: {survived.mean()*100:.1f}%")
print(f"  - V < 0.5: {survived[V < 0.5].mean()*100:.1f}%")
print(f"  - V >= 0.5: {survived[V >= 0.5].mean()*100:.1f}%")
print(f"\nInvestor Distribution:")
print(f"  - Analyst: {(investor_types == 'analyst').mean()*100:.1f}%")
print(f"  - Believer: {(investor_types == 'believer').mean()*100:.1f}%")
print(f"\nGrowth (Survivors Only):")
print(f"  - V < 0.5 mean: {survivors_df[survivors_df['vague'] <= 0.5]['final_growth'].mean():.2f}")
print(f"  - V >= 0.5 mean: {survivors_df[survivors_df['vague'] > 0.5]['final_growth'].mean():.2f}")
print(f"  - Ratio: {survivors_df[survivors_df['vague'] > 0.5]['final_growth'].mean() / survivors_df[survivors_df['vague'] <= 0.5]['final_growth'].mean():.2f}x")
