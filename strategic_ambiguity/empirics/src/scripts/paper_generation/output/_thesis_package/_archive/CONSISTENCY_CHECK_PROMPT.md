# Consistency Check Prompt for Variable Definitions

## Context
I have a thesis on strategic ambiguity in startups with empirical analysis code. I need to verify that the **variable definitions in theory** match the **code implementation**.

---

## Task
Please compare the theoretical variable definitions (Section A) with the code implementation (Section B) and identify:
1. **Exact matches**: Variables implemented correctly as defined
2. **Semantic matches**: Variables with same meaning but different notation/naming
3. **Mismatches**: Variables where implementation differs from definition
4. **Missing**: Variables defined but not implemented, or vice versa

---

## Section A: Theoretical Variable Definitions

From `variables.md`:

| Symbol | Name | Definition | Unit | Range | Time |
|--------|------|------------|------|-------|------|
| **L** | Long-term Success | Probability of later-stage funding | Probability | [0, 1] | T (End) |
| **F_t** | Later Capital | Amount of later-stage funding raised | Currency ($M) | Continuous | t (Interval) |
| **E** | Early Capital | Amount of early-stage funding raised | Currency ($M) | Continuous | 0 (Start) |
| **G_t** | Growth Ratio | Momentum of value creation: (F_t - E) / E | Ratio | Continuous | t (Interval) |
| **V** | Vagueness | Vagueness of early-stage positioning/promise | Score | [0, 100] | 0 (Start) |
| **D_t** | Directional Change | The raw change of position (vector) | Score | [-M, +M] | t (Interval) |
| **A_t** | Adaptive Capacity | The absolute change of position: \|D_t\| | Score | [0, M] | t (Interval) |

---

## Section B: Code Implementation

### Data Loading (`seven_plots_v2.py`, lines 67-152)

```python
def load_data():
    # Load panel data
    panel = pd.read_parquet(DATA_PATH)

    # t=0 (2021): Extract V and E
    df_0 = panel[panel['year'] == 2021][['company_id', 'V', 'first_financing_size']].copy()
    df_0.columns = ['company_id', 'V', 'E']

    # t=T (2025): Extract V_T and D
    df_T = panel[panel['year'] == 2025][['company_id', 'V', 'total_delta_V']].copy()
    df_T.columns = ['company_id', 'V_T', 'D']

    # Merge
    cross = df_0.merge(df_T, on='company_id', how='inner')
    cross = cross.merge(company_df, on='company_id', how='left')

    # Derived variables
    cross['A'] = cross['D'].abs()  # A = |D|
    cross['E_log'] = np.log10(cross['E'].clip(lower=0.01))

    # L (Survival) - BINARY, not probability
    valid_funding = cross['E'].notna() & (cross['E'] > 0) & cross['TotalRaised_2025'].notna()
    cross['L'] = 0  # Default: not survived
    cross.loc[valid_funding & (cross['TotalRaised_2025'] > cross['E'] * 5), 'L'] = 1

    # G (Growth) = (TotalRaised - E) / E
    cross['L_funding'] = cross['TotalRaised_2025'] - cross['E']
    cross['L_funding'] = cross['L_funding'].clip(lower=0)
    cross['G'] = cross['L_funding'] / (cross['E'] + 0.001)

    return panel, cross
```

### Robustness Check (`robustness_timeseries.py`)

```python
def load_timeseries_data():
    for t in [2023, 2024, 2025]:
        # Get V_t
        df_t = panel[panel['year'] == t][['company_id', 'V']].copy()
        df_t.columns = ['company_id', 'V_t']

        # Compute D_t and A_t
        cross['D_t'] = cross['V_t'] - cross['V_0']
        cross['A_t'] = cross['D_t'].abs()

        # Compute G_t = (TotalRaised_t - E) / E
        cross['L_funding'] = cross['TotalRaised_t'] - cross['E']
        cross['G_t'] = cross['L_funding'] / (cross['E'] + 0.001)
```

---

## Section C: Key Questions

1. **L Definition**: The theory says L is a "probability" [0,1], but code implements it as binary {0,1}. Is this:
   - (a) A bug that needs fixing?
   - (b) An acceptable operationalization that should be documented?
   - (c) A fundamental mismatch requiring theory revision?

2. **F_t vs L_funding**: The code uses `L_funding` instead of `F_t`. Should we:
   - (a) Rename `L_funding` to `F_t` in code?
   - (b) Update the theory document to use `L_funding`?
   - (c) Keep both but add a mapping table?

3. **D_t Computation**: The code uses `total_delta_V` from the data. Is this equivalent to `V_T - V_0`?

4. **Time Subscripts**: The theory uses subscript t for time-varying variables (G_t, D_t, A_t), but the main code computes only T=2025. The robustness code computes for t=2023, 2024, 2025. Is this consistent?

---

## Expected Output Format

Please provide:

1. **Consistency Matrix**
```
| Variable | Theory | Code | Match? | Notes |
|----------|--------|------|--------|-------|
| L        | ...    | ...  | ...    | ...   |
```

2. **Recommended Changes**
- For each mismatch, suggest whether to fix the code or update the theory

3. **Verification Steps**
- Any additional checks needed to ensure full consistency
