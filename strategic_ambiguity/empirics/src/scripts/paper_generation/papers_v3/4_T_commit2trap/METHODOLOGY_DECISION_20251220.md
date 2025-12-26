# Methodology Decision: G Definition & Statistical Approach

**Date**: 2025-12-20
**Decision**: G = raw multiple (배수), Median regression (not mean)

---

## 김정하 교수님의 화소를 빌려

> "세상은 절망적이지만 절망만 하면 안 된다"

통계에서도 마찬가지다.

**Mean(평균)은 이상치에 절망한다.** G = 83,685,704배인 회사 하나가 전체 회귀선을 왜곡한다.

**Median(중앙값)은 절망하지 않는다.** "전형적인" 창업가의 이야기에 집중한다.

---

## 왜 log(G)가 아닌 raw G인가?

> "자기 이익을 바라지 않고 타인에게 충고할 수 있는 관계의 소중함"
> — jungha_kim.md

**Log 변환은 독자에게 충고할 수 없다.**

| G 정의 | 값 | 창업가/투자자에게 |
|:---|:---:|:---|
| G_raw = 10 | "시드 대비 10배 모았어요" | 이해됨 |
| G_log = 2.3 | "로그 지가 2.3이에요" | ??? |

VC의 언어는 "멀티플"이다. 논문이 실무자에게 충고하려면, 그들의 언어를 써야 한다.

---

## 왜 Median인가?

> "현지가 어떤 말을 했을때 어떻게 받아들이실지 모르겠다"
> — jungha_kim.md

**Mean은 이상치의 말을 너무 크게 받아들인다.**

83M배 성장한 회사 1개가 180,000개 회사의 평균을 지배한다.

**Median은 "전형적인 회사"의 이야기를 듣는다.**

| 통계량 | 듣는 대상 | 적합한 질문 |
|:---|:---|:---|
| Mean | 모든 회사 (이상치 포함) | "평균적으로 얼마나?" |
| Median | 전형적인 회사 | "보통 얼마나?" |

Nanda 교수의 Figure 2도 이상치를 제외하고 분포의 중심에 집중한다.

---

## 기술적 구현

### 기존 (폐기)
```python
# G 정의
panel['G'] = np.log1p(panel['total_raised'] / panel['E'])

# 회귀
slope, _, _, p, _ = linregress(x, y)  # OLS (mean 기반)
```

### 새로운 (채택)
```python
# G 정의
panel['G'] = panel['total_raised'] / panel['E']  # raw multiple

# 회귀
from scipy.stats import siegelslopes  # 또는 quantile regression
slope, intercept = siegelslopes(y, x)  # median 기반
```

---

## Nanda 프레임워크와의 일관성

> "To improve readability, firms with greater than 450 million pre-money valuation... are not included in the plots"
> — Nanda, "Priors, Experiments, Learning and Persuasion"

Nanda도 이상치를 제거하고 분포의 중심에 집중한다. Median regression은 이 철학과 일치한다.

---

## 결론

| 항목 | 기존 | 새로운 | 이유 |
|:---|:---|:---|:---|
| G 정의 | log(total/E) | total/E | VC 언어로 소통 |
| 회귀 | OLS (mean) | Median | 이상치 robust |

> "성찰할 수 있다는 것 자체가 성숙함을 보여주는 지표"
> — jungha_kim.md

이 결정도 하나의 성찰이다.

---

**Signed**: Claude & 현지
**Inspired by**: 김정하 교수님의 가르침
