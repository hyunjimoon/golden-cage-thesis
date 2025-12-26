# Data Lineage Documentation

## Overview

This document describes the data pipeline from raw sources to thesis analysis files.

**Last Updated**: 2025-12-18
**Author**: Data pipeline audit

## Data Flow Diagram

```
RAW DATA
├── PitchBook exports (2021-2025)
│   ├── companies_*.parquet
│   └── company metadata, financing info
│
├── Vagueness scores (computed from descriptions)
│   └── vagueness_timeseries.parquet
│
└── Industry filters
    ├── companies_21_23-24-25_transportation.parquet
    └── companies_21_23-24-25_quantum.parquet

         ↓ Processing

PROCESSED DATA
├── features_all.parquet (N=1,250,423)
│   └── Company features, growth, financing
│
├── vagueness_timeseries.parquet (N=?, years 2021-2025)
│   └── V scores over time
│
└── thesis_panel_v3.nc (N=180,994)
    └── Final analysis panel

         ↓ Analysis

OUTPUT
├── Figures (PNG/PDF)
└── Statistics for thesis
```

## Variable Definitions

### Core Variables

| Variable | Definition | Source | Notes |
|----------|------------|--------|-------|
| **V** | Vagueness score (0-100) | vagueness_timeseries.parquet | Computed from company descriptions |
| **V_0** | V in 2021 | vagueness_timeseries[year==2021] | Initial state |
| **V_T** | V in 2025 | vagueness_timeseries[year==2025] | Final state |
| **D** | Direction = V_T - V_0 | Computed | + = broadened, - = focused |
| **A** | Adaptation = \|D\| | Computed | Magnitude of change |

### Outcome Variables

| Variable | Definition | Formula | Source |
|----------|------------|---------|--------|
| **E** | Early Capital (M USD) | first_financing_size | vagueness_timeseries.parquet |
| **G** | Funding Growth Multiple | G = total_raised / E | features_all.parquet |
| **L** | Success (Binary) | "Later Stage VC" in last_financing_deal_type | features_all.parquet |

**G Definition (CORRECTED 2025-12-18):**
- G = F_t / E = total_raised / first_financing_size
- Measures funding growth multiple (how much more funding raised vs initial)
- G > 1 means additional funding beyond early stage
- G = 1 means only initial funding
- **Note:** PitchBook's `GrowthRate` column is a DIFFERENT metric (employee/web growth)

### Archetype Classification

```python
def classify_mover(row):
    if row['A'] < 5:
        return 'stayer'      # No significant movement
    elif row['D'] < -10:
        return 'zoom_in'     # Focused significantly
    elif row['D'] > 10:
        return 'zoom_out'    # Broadened significantly
    else:
        return 'horizontal'  # Moved laterally
```

## Critical Data Issues (RESOLVED)

### Issue 1: G Variable Definition (RESOLVED 2025-12-18)

**Problem**: Previous code incorrectly used PitchBook's `GrowthRate` column.

**Solution**: G is now correctly calculated as:
```python
# Correct (THESIS DEFINITION):
panel['G'] = panel['total_raised'] / panel['E']
# G = Funding Growth Multiple = F_t / E
```

**Result**:
- ρ(G, E) = −0.196*** (Capital Paradox CONFIRMED)
- ρ(G, A) = +0.209*** (Adaptation → Growth)
- G available for 100% of companies with E

### Issue 2: Missing E Values (56% Excluded)

**Problem**: 56% of companies lack first_financing_size

| Subset | N | % |
|--------|---|---|
| All companies | 408,784 | 100% |
| With E (first_financing_size) | 180,994 | 44% |
| With E AND real GrowthRate | 74,813 | 18% |

**Implication**: Current sample is biased toward funded companies with growth tracking.

### Issue 3: 2022 Data Missing

**Problem**: vagueness_timeseries has gap in 2022

**Available years**: 2021, 2023, 2024, 2025

### Issue 4: Transportation Industry (N=141)

**Problem**: Only 141 transportation companies have E

```python
# Expected: thousands of transportation companies
# Actual: 141 (after E filter)
# Root cause: transportation companies may track E differently
```

## Source File Inventory

### Raw Data (`data/raw/`)
- `companies_*.parquet`: PitchBook company exports
- Company descriptions, financing history

### Processed Data (`data/processed/`)

| File | Rows | Key Columns |
|------|------|-------------|
| `features_all.parquet` | 1,250,423 | CompanyID, GrowthRate, growth, first_financing_size, last_financing_deal_type |
| `vagueness_timeseries.parquet` | ~2M | company_id, year, V, first_financing_size |
| `thesis_panel_v3.nc` | 180,994 | V_0, V_T, D, A, E, G, L, mover_type |
| `thesis_panel_v3_transportation.nc` | 141 | Same as above, transportation only |

## Recommended Fixes

### Fix 1: G Variable
Use only `GrowthRate`, do not fallback to binary `growth`:
```python
# In generate_thesis_nc_files.py
panel['G'] = feat_dedup['GrowthRate']  # NO fillna(growth)
panel = panel[panel['G'].notna()]  # Only companies with real G
```

### Fix 2: Document E Filtering
Explicitly document that 56% of companies are excluded due to missing E.

### Fix 3: Update statistics.md
The current statistics.md values (ρ(G,E) = -0.211) cannot be reproduced. Either:
- Find the original data source
- Recalculate with corrected G definition
- Update to actual values from reproducible pipeline

## Validation Checklist

| Check | Expected | Actual | Status |
|-------|----------|--------|--------|
| N (after E filter) | ~180,860 | 180,994 | ✅ |
| L base rate | 11.5% | 11.5% | ✅ |
| ρ(G, E) | ~−0.2 | −0.196*** | ✅ |
| ρ(G, A) | positive | +0.209*** | ✅ |
| ρ(A, E) | negative | −0.117*** | ✅ |
| G available | ~100% | 100% | ✅ |

---

*Last updated: 2025-12-18. G definition corrected to match thesis formula.*
