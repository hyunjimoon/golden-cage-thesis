# Table 5 구조 평가 Prompt

> ChatGPT/Gemini에게 복사-붙여넣기 하세요

---

**MIT PhD 논문 Table 구조 평가 요청**

벤처 성장 연구에서 "Mover vs Stayer" 분류 테이블을 어떻게 제시할지 두 가지 옵션이 있습니다. 학술적 명확성과 독자 설득력 관점에서 평가해주세요.

---

**옵션 A: 단일 테이블 (기존)**

| Archetype | Criteria | N | % | Success Rate |
|:----------|:---------|--:|--:|:------------:|
| Stayer | R ≤ 0.5 | 144,605 | 79.9% | 9.9% |
| Zoom-in | ΔB < 0, R > 0.5 | 15,902 | 8.8% | 17.1% |
| Zoom-out | ΔB > 0, R > 0.5 | 20,487 | 11.3% | 18.4% |
| **All Movers** | R > 0.5 | 36,389 | 20.1% | **17.8%** |

---

**옵션 B: 분리 테이블 (신규)**

**Table 5a: Binary Classification (Primary)**

| Archetype | Criteria | N | % | Success Rate |
|:----------|:---------|--:|--:|:------------:|
| Stayer | R ≤ τ | 144,605 | 79.9% | 9.9% |
| Mover | R > τ | 36,389 | 20.1% | **17.8%** |

*Note: τ = median(R | R > 0)*

**Table 5b: Directional Decomposition (Secondary)**

| Direction | Criteria | N | % | Success Rate |
|:----------|:---------|--:|--:|:------------:|
| Zoom-in | ΔB < 0, R > τ | 15,902 | 8.8% | 17.1% |
| Zoom-out | ΔB > 0, R > τ | 20,487 | 11.3% | 18.4% |

---

**평가 기준:**
1. **인과적 명확성**: 어느 구조가 "binary가 main, 3-way가 보조"임을 더 명확히 전달하는가?
2. **Canon 숫자 강조**: 1.81× (17.8% vs 9.9%) 핵심 발견이 어디서 더 돋보이는가?
3. **MIT 위원회 방어**: "왜 3-way를 main으로 안 썼나?" 공격에 어느 구조가 더 방어적인가?
4. **독자 인지부하**: 첫 독서에서 어느 것이 이해하기 쉬운가?

**최종 추천과 근거를 알려주세요.**

---

## 대안 질문 (저자가 이미 옵션 B 선택 시)

> 저자는 옵션 B를 선택했는데 옵션 A로 돌아가야 할까요?

---

*Created: 2026-01-12*
*Issue: #024 Mover Taxonomy Decision*
