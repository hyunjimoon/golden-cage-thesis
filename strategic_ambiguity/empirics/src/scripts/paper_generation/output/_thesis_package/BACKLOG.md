# 📋 THESIS BACKLOG

## Purpose
이 파일은 논문에 추가해야 할 사항, 개선점, 검증이 필요한 항목들을 기록합니다.

---

## 🔴 HIGH PRIORITY (Must Add)

### 1. A vs D 비교 통계 (¶26에 추가)
**상태:** Pending
**위치:** Paper U ¶26 (Direction Finding)
**내용:**
- A (|D|, magnitude) vs D (signed direction) 비교
- ρ(A,L) = +0.056*** vs ρ(D,L) = +0.017*** → A가 3.3× 강함
- ρ(A,G) = +0.044*** vs ρ(D,G) = -0.0004 (NS) → D는 Growth와 무관
- ρ(E,A) = -0.009*** vs ρ(E,D) = +0.0006 (NS) → Golden Cage는 A에만 적용

**이론적 함의:**
> "It's not which direction you move (focusing vs broadening) that matters—it's how much you move."

---

## 🟡 MEDIUM PRIORITY (Should Add)

### 2. Analyst/Believer 청중 구분 메커니즘
**상태:** Theoretical (no direct data)
**위치:** Paper U ¶12-14
**문제:** 현재 V quartile로만 구분, 실제 청중 데이터 없음
**향후 연구:** Investor type data 확보 필요

### 3. Industry-specific k* 검증
**상태:** Pending
**위치:** Discussion ¶8
**내용:** Deep-tech vs Software의 CR 차이 실증 분석

---

## 🟢 LOW PRIORITY (Nice to Have)

### 4. Robustness checks 확장
- Time-varying effects (2021-2022 vs 2023-2025)
- Industry fixed effects detail
- Alternative L definitions (IPO, M&A)

### 5. Visualization 개선
- 3D surface plot for V × A → L
- Interactive dashboard for exploration

---

## ✅ COMPLETED

(완료된 항목들을 여기로 이동)

---

## 📝 NOTES

### 검증 필요 항목
- [ ] seven_plots_v2.py ↔ paper_U_sec3.md 일치 확인
- [ ] seven_plots_v2.py ↔ paper_C_sec3.md 일치 확인
- [ ] summary_statistics.json ↔ ToC 파일들 통계 일치

### 파일 구조
```
_thesis_package/
├── BACKLOG.md          ← 이 파일
├── papers/
│   ├── I/toc(i).md     ← Introduction (8¶)
│   ├── U/toc(u).md     ← Paper U (32¶)
│   ├── C/toc(c).md     ← Paper C (32¶)
│   └── D/N/toc(n).md   ← Discussion (16¶)
├── text/
│   ├── paper_U_sec3.md
│   └── paper_C_sec3.md
├── stats/
│   └── summary_statistics.json
└── seven_plots_v2.py
```

---

*Last updated: 2025-12-10*
