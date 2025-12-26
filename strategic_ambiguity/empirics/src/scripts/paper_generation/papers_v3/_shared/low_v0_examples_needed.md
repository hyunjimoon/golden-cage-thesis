# Low V₀ Examples: Data Query Guide

## Missing Examples

| Type | V₀ Level | Direction | Currently Have | Status |
|:-----|:--------:|:---------:|:--------------|:------:|
| ⚫ Stayer | **Low** | None (D ≈ 0) | None | ❌ MISSING |
| 🟢 Horizontal | **Low** | Lateral (keywords change) | None | ❌ MISSING |
| 🔴 Zoom In | High | Focus (D < 0) | Tesla, multiple | ✅ |
| 🔵 Zoom Out | Low | Expand (D > 0) | Amazon | ✅ |

---

## Existing Examples (For Reference)

### High V₀ Examples (Already Available)

| Company | V₀ | V_T | ΔV | Type | Outcome |
|:--------|:--:|:---:|:--:|:-----|:--------|
| **Tesla** | ~85 | ~65 | −20 | 🔴 Zoom In | Success |
| **Quibi** | 82.1 | 81.9 | −0.2 | ⚫ Stayer (High V₀) | Failure |
| **Linpowave** | 88.1 | 31.8 | −56.3 | 🔴 Zoom In | — |
| **Rubedos** | 81.9 | 81.9 | 0 | ⚫ Stayer (High V₀) | — |

### Low V₀ Examples (Already Available)

| Company | V₀ | V_T | ΔV | Type | Outcome |
|:--------|:--:|:---:|:--:|:-----|:--------|
| **Amazon** | 28.4 | 89.1 | +60.7 | 🔵 Zoom Out | Success |
| **Better Place** | ~15 | ~15 | ~0 | ⚫ Stayer (Low V₀) | Failure |
| **Sky Engine** | 28.4 | 89.1 | +60.7 | 🔵 Zoom Out | — |

---

## What's Needed: Low V₀ Stayer and Horizontal

### ⚫ Low V₀ Stayer

**Definition**: Started precise (V₀ < 30) AND stayed precise (|ΔV| < 5)

**Query Logic**:
```python
low_v0_stayers = df[
    (df['V_initial'] < 30) &      # Low V₀ (precise start)
    (abs(df['V_change']) < 5) &   # Stayed (D ≈ 0)
    (df['success'] == True)       # For interesting success case
]
# OR for failure case:
low_v0_stayers_failed = df[
    (df['V_initial'] < 30) &
    (abs(df['V_change']) < 5) &
    (df['success'] == False)
]
```

**Hypothesis**: Should show HIGHEST trap rate (precise + committed = learning blocked)

**Expected Profile**:
- Highly specific initial promise
- Stayed on that promise despite market changes
- Either: survived through niche dominance OR failed due to inability to adapt

### 🟢 Low V₀ Horizontal

**Definition**: Started precise (V₀ < 30) AND keywords changed significantly (lateral pivot) but V stayed similar

**Query Logic**:
```python
low_v0_horizontal = df[
    (df['V_initial'] < 30) &          # Low V₀ (precise start)
    (abs(df['V_change']) < 5) &       # V magnitude stayed similar
    (df['keyword_similarity'] < 0.5)  # But keywords changed (different domain)
]
```

**Hypothesis**: Should show ability to escape trap through domain change

**Expected Profile**:
- Pivoted to adjacent market/technology
- Maintained precision level but shifted focus
- "Lateral movement" at low abstraction level

---

## Data Sources

### Primary Dataset
```
Path: /Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/data/processed/vagueness_timeseries.parquet

Columns:
- company_name
- company_id
- year (2021, 2023, 2024, 2025)
- V (vagueness score 0-100)
- delta_V
- total_delta_V
- description
```

### Outcome Data
```
Path: /Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/data/processed/Company20251101.parquet

Key columns:
- CompanyName
- LastFinancingDealType (Later Stage VC = success)
- BusinessStatus (Out of Business, Bankruptcy = failure)
```

---

## Canonical Examples Candidates (From Literature)

### ⚫ Low V₀ Stayer Candidates

| Company | Hypothesis | Rationale |
|:--------|:-----------|:----------|
| **Waymo** (Alphabet) | Failed Stayer | Committed to specific tech (LiDAR, HD maps, L4) |
| **Cruise** (GM) | Failed Stayer | $10B+ invested, 50% layoffs |
| **Argo AI** | Failed Stayer | Ford + VW backing → complete shutdown |
| **Webvan** | Failed Stayer | Very precise delivery model, couldn't adapt |
| **Kodak** | Failed Stayer | Precise film-based model |

### 🟢 Low V₀ Horizontal Candidates

| Company | Hypothesis | Rationale |
|:--------|:-----------|:----------|
| **Slack** (pre-pivot) | Success Horizontal | Gaming → Enterprise (low V throughout) |
| **PayPal** (pre-pivot) | Success Horizontal | Palm Pilot → Web payments |
| **Stripe Atlas** | Success Horizontal | Precise payments → Precise incorporation |

---

## Action Items

1. **Run Data Query**: Execute the Python queries above on vagueness_timeseries.parquet
2. **Join with Outcomes**: Match companies to success/failure status
3. **Validate Candidates**: Check if literature examples appear in data
4. **Document 2-3 Examples**: For each missing cell (Low V₀ Stayer, Low V₀ Horizontal)

---

## Why This Matters

The thesis currently has strong examples for:
- ✅ High V₀ movers (Tesla, successful zoom-in)
- ✅ Low V₀ movers (Amazon, successful zoom-out)
- ✅ High V₀ stayers (Quibi, failed stayer)

But lacks:
- ❌ Low V₀ stayers (critical for testing learning trap at low V)
- ❌ Low V₀ horizontal movers (critical for testing lateral escape)

These examples would strengthen the empirical narrative by showing the trap operates even at low vagueness levels.

---

*必死卽生, 必生卽死*
