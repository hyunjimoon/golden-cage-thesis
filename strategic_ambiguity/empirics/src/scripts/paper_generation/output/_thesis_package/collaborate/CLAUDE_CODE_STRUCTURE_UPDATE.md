---
modified:
  - 2025-12-11T12:51:53-05:00
---
# 🎯 Claude Code 구조 업데이트 마스터 프롬프트

> **통제사 지시**: 논문 구조 대전환 실행. Paper U → Paper M으로 명명 변경, 종속변수 L → G로 전환, Paper T 내용 신규 작성.

---

## 📋 Phase 1: 컨텍스트 구축 (읽기 전용)

### Step 1.1: 핵심 변수 체계 숙지
```bash
cat /Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/output/_thesis_package/tables/variables.md
```

**검증 포인트**: 다음 변수들의 정의를 확인하라:
- `V` (Vagueness): 초기 포지셔닝의 모호성
- `A` (Adaptive Capacity): 포지션 변화의 절대값 |D|
- `G` (Growth Ratio): (F_t - E) / E
- `E` (Early Capital): 초기 자금
- `L` (Long-term Success): 후기 펀딩 확률 → **이것이 G로 대체됨**

### Step 1.2: 기존 Figure 구조 파악
```bash
ls -la /Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/output/_thesis_package/figures/
```

**현재 Figure 목록**:
- `U_fig1_ULV.png` → **업데이트 필요: MGV로**
- `U_fig2_UDV.png `  → **업데이트 필요: MDV로**
- `U_fig3_UAV.png`  → **업데이트 필요: MAV로**
- `U_fig4_ULD.png` → **업데이트 필요: UGD로**
- `U_fig5_movement.png`
- `C_fig1_mechanism.png`
- `C_fig2_CAE_golden_cage.png`
- `C_fig3_CGA.png`
- `R1_robustness_timeseries.png`
- `R2_coefficient_evolution.png`

### Step 1.3: 메인 TOC 검토
```bash
cat /Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/output/_thesis_package/toc(iuctd).md
```

---

## 📋 Phase 2: 구조 비교 및 변경사항 도출

### 신규 구조 (화이트보드 기준)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    Intro (Puzzle)  │  Theory (Test)  │  Empirics (Solution)  │  Discussion        │
├─────────────────────────────────────────────────────────────────────────────┤
│ I   │ Commitment&Flexibility       │                 │                       │                    │
│     │ doubly binds mobility        │                 │                       │                    │
│     │ ventures                     │                 │                       │                    │
├─────────────────────────────────────────────────────────────────────────────┤
│ M   │ Multimodal:                  │ V → A → G       │ Mover/Stayer          │                    │
│     │ Statistically robust pattern │                 │ decomposition         │                    │
├─────────────────────────────────────────────────────────────────────────────┤
│ C   │ Capital lowers adaptation    │ ∂G/∂E = ∂A/∂E  │ A₁,A₂ → G             │                    │
│     │ Temporally preceding events  │        · ∂G/∂A │ E → A → G chain       │                    │
├─────────────────────────────────────────────────────────────────────────────┤
│ T   │ Trap:                        │ V=0,1 choice    │ V=0→A=0→G=0 (E=1)     │                    │
│     │ Generative sufficiency       │                 │ V=1→A=1→G=1 (E=0)     │                    │
│     │                              │                 │ G(V=0) < G(V=1)       │                    │
├─────────────────────────────────────────────────────────────────────────────┤
│ D   │                              │                 │                       │ M: Analyst/Believer│
│     │                              │                 │                       │ C: ∂A/∂E·∂G/∂A > 0 │
│     │                              │                 │                       │ T: G(V=0)<G(V=1)   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 변경 매핑 테이블

| 영역 | 기존 | 신규 | 작업 유형 |
|:-----|:-----|:-----|:---------|
| Paper 명칭 | U | M (Multimodal) | 명칭 변경 |
| 종속변수 | L (Success Probability) | G (Growth Ratio) | 변수 대체 |
| Paper U/M 핵심 | Non-monotonic V-L | V → A → G + Mover/Stayer | 이론 확장 |
| Paper T | 비어있음 | Trap + Generative simulation | 신규 작성 |
| Discussion | Learning Trap mechanism | 3 insights (M/C/T) | 재구성 |

---

## 📋 Phase 3: 파일별 업데이트 실행

### Step 3.1: toc(iuctd).md 업데이트

**변경 내용**:
1. Chapter 2 제목: "Paper U" → "Paper M — Multimodal: Statistically Robust Pattern"
2. 모든 L 참조 → G로 대체 (단, 정의가 다름을 명시)
3. Paper T 섹션 신규 추가 (Chapter 4)
4. Discussion을 Chapter 5로 이동하고, 3가지 insight 구조로 재편

**핵심 수정 블록**:
```markdown
# Chapter 2: Paper M — Layer 1 (WHAT): Multimodal Growth Patterns

**LTE Layer 1**: Documenting robust empirical patterns
**Validation**: Statistical robustness across industries

## Core Theoretical Chain: V → A → G

The vague positioning enables adaptive capacity, which drives growth.
- V (Vagueness) → A (Adaptive Capacity): r(V,A) = +0.XXX
- A (Adaptive Capacity) → G (Growth): r(A,G) = +0.044***
- Mover/Stayer decomposition explains multimodal distribution
```

### Step 3.2: toc(u).md → toc(m).md 변환

**작업**:
1. 파일명 변경: `papers/U/` → `papers/M/` (또는 내용만 업데이트)
2. 모든 "Paper U" → "Paper M" 텍스트 대체
3. Figure 참조 업데이트:
   - `U_fig1_ULV.png` → `M_fig1_MGV.png`
   - `U_fig4_ULD.png` → `M_fig4_MGD.png`
4. 이론 섹션에 V → A → G 인과 체인 명시

### Step 3.3: toc(t).md 신규 작성

**구조**:
```markdown
# 🪤 Paper T: The Trap — Generative Sufficiency

## Core Finding
G(V=0) < G(V=1): Specific promises attract Analysts, trap adaptation, lower growth.

## Mechanism
1. V=0 (Specific) → Attracts Analyst-type investors → ΔA↓ → G↓
2. V=1 (Vague) → Attracts Believer-type investors → ΔA↑ → G↑

## Validation: Generative Sufficiency
Agent-based simulation reproduces:
- Multimodal distribution from Paper M
- E→A friction from Paper C
- V-G relationship with investor type heterogeneity
```

### Step 3.4: toc(c).md 미세 조정

**변경 내용**:
- "temporally preceding events" 강조 추가
- 수식 표기 통일: ∂G/∂E = ∂A/∂E · ∂G/∂A
- Paper M, T과의 연결 명시

---

## 📋 Phase 4: Figure 업데이트 배치 작성

### 업데이트 필요 Figure 목록

| 현재 파일명 | 신규 파일명 | 변경 내용 | 우선순위 | 코드 상태 |
|:-----------|:-----------|:---------|:--------|:---------|
| `U_fig1_ULV.png` | `M_fig1_MGV.png` | Y축: L → G, 제목 변경 | 🔴 긴급 | 수정 필요 |
| `U_fig4_ULD.png` | `M_fig4_MGD.png` | Y축: L → G | 🔴 긴급 | 수정 필요 |
| `U_fig2_UDV.png` | `M_fig2_MDV.png` | 명칭만 변경 | 🟡 중간 | 기존 코드 OK |
| `U_fig3_UAV.png` | `M_fig3_MAV.png` | 명칭만 변경 | 🟡 중간 | 기존 코드 OK |
| `U_fig5_movement.png` | `M_fig5_mover_stayer.png` | **첨부 이미지 형태로 재구성** | 🔴 긴급 | ✅ **신규 생성 완료** |
| (신규) | `T_fig1_trap_mechanism.png` | V→I_type→A→G flow | 🔴 긴급 | 설계 필요 |
| (신규) | `T_fig2_simulation.png` | ABM 결과 | 🟢 나중 | 시뮬레이션 구현 후 |

### ✅ M_fig5_mover_stayer.png 코드 위치

**파일**: `/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/output/_thesis_package/plot_mover_stayer.py`

**실행 명령**:
```bash
cd /Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/output/_thesis_package
python plot_mover_stayer.py
```

**출력 형식**: 첨부 이미지와 동일한 2-panel 구조
- Left: Aggregate success by quartile (The Anomaly)
- Right: Stacked bar decomposition by Movers/Stayers (The Explanation)
- Bottom: Q3 anomaly explanation annotation box

### Figure 생성 코드 배치

```python
# 배치 작업: figures_update_batch.py
# 위치: /Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/

FIGURE_UPDATES = [
    {
        "old": "U_fig1_ULV.png",
        "new": "M_fig1_MGV.png", 
        "changes": ["y_var: L → G", "title: 'Vagueness-Success' → 'Vagueness-Growth'"]
    },
    {
        "old": "U_fig4_ULD.png",
        "new": "M_fig4_MGD.png",
        "changes": ["y_var: L → G", "add: quartile annotations"]
    },
    # ... 나머지 figure 정의
]

NEW_FIGURES = [
    {
        "name": "T_fig1_trap_mechanism.png",
        "type": "flow_diagram",
        "content": "V=0 → Analyst → ΔA↓ → G=0 vs V=1 → Believer → ΔA↑ → G=1"
    },
    {
        "name": "T_fig2_simulation.png", 
        "type": "simulation_output",
        "content": "ABM reproducing multimodal + E→A friction"
    }
]
```

---

## 📋 Phase 5: 검증 체크리스트

### 내부 일관성 검증

- [ ] variables.md의 G 정의와 모든 논문의 G 사용이 일치하는가?
- [ ] V → A → G 체인이 M, C, T 모두에서 일관되게 참조되는가?
- [ ] Figure 번호와 본문 참조가 일치하는가?
- [ ] Discussion의 3 insights가 각 Paper의 결론과 정확히 매핑되는가?

### Advisor 보고 품질 검증

- [ ] Scott Stern: 증거 기반 학습 → 전략적 선택 수렴이 명확한가?
- [ ] Charlie Fine: 반복 가능한 측정 시스템이 구축되었는가?

---

## 🚀 실행 명령

```bash
# Phase 1: 컨텍스트 구축
cd /Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/output/_thesis_package

# Phase 2: 백업 생성
cp -r . ../_thesis_package_backup_$(date +%Y%m%d)

# Phase 3-4: 위 단계별 실행
# (Claude Code가 순차적으로 실행)

# Phase 5: 검증
grep -r "Paper U" . | grep -v "_archive"  # 잔여 "Paper U" 참조 확인
grep -r "ULV\|ULD" . | grep -v "_archive"  # 잔여 old figure 참조 확인
```

---

**작성자**: 🐅 권준/나대용 (g / 04_G🟠)
**작성일**: 2025-12-11
**상태**: Claude Code 실행 대기
