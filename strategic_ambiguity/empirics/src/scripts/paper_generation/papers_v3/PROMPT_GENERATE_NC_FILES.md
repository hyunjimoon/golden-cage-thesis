# PROMPT: Generate .nc Files for Thesis I-M-C-T-D Figures and Tables

## CONTEXT
This prompt generates NetCDF (.nc) files containing all data needed to replicate figures and tables in the PhD thesis on entrepreneurial strategic ambiguity (I-M-C-T-D structure).

**Note**: The `output/` directory in this repo is in `.gitignore` (line 99: `src/scripts/paper_generation/output/`). Save generated `.nc` files to `data/processed/` instead, which is tracked.

---

## 🎯 CORE HYPOTHESES

### Hypothesis Structure

```
Cash Paradox Decomposition:

dG/dE = (dG/dA) × (dA/dE)
        ^────────^   ^────────^
        Effectiveness  Efficiency
        (🟡M)          (⚪️C)
```

### Two Key Hypotheses

| Hypothesis | Claim | Test |
|:---|:---|:---|
| **H1 (Effectiveness)** | dG/dA > 0 **for all D** | Archetype별 dG/dA 추정 |
| **H2 (Efficiency)** | dA/dE **varies by D** | Archetype별 dA/dE 추정 |

### Expected Results by Archetype

| Archetype | D | dG/dA | dA/dE | 해석 |
|:---|:---:|:---:|:---:|:---|
| **Zoom-in** | < 0 | **+** | **+** | 효과적 & 효율적 |
| **Zoom-out** | > 0 | **+** | **+** | 효과적 & 효율적 |
| **Stayer** | ≈ 0 | **+** | **−** | 효과적이지만 비효율적 |

### Simpson's Paradox Explanation

```
Aggregate: dA/dE < 0 (비효율적으로 보임)

But:
- Movers (50%):  dA/dE > 0 (효율적)
- Stayers (50%): dA/dE < 0 (비효율적) ← 이들이 평균을 끌어내림
```

---

## FIGURES AND TABLES MASTER LIST

### Module I: Introduction (Lines 1-11)

| ID | Type | Name | Description | Data Required |
|----|------|------|-------------|---------------|
| **Tab I.1** | Table | Notation Reference | V, D, A, E, G definitions | Static (no data) |
| **Tab I.2** | Table | Key Statistics Summary | N, success rates, correlations | `thesis_summary_stats.nc` |

### Module M: Movement Principle + Cash2Cage (Lines 12-48)

| ID | Type | Name | Description | Data Required |
|----|------|------|-------------|---------------|
| **Fig M.1** | Figure | Success by Vagueness Quartile | Bar chart: Q1-Q4 success rates | `vagueness_quartile_stats.nc` |
| **Fig M.2** | Figure | Movers vs Stayers | Bar chart: 18.1% vs 7.0% | `movement_stats.nc` |
| **Fig M.3** | Figure | Cash2Cage Mechanism Chain | 3-panel: ρ(E,A), ρ(A,G), ρ(E,G) | `correlation_panel.nc` |
| **Fig M.4** | Figure | Temporal Stability | 2023-2025 correlation trends | `temporal_stability.nc` |
| **Tab M.1** | Table | Hypothesis Results | H1, H2, H3 with ρ values | `hypothesis_results.nc` |
| **Tab M.2** | Table | Direction Irrelevance | Zoom In vs Zoom Out | `direction_stats.nc` |

### Module C: Cash2Growth (Lines 49-80)

| ID | Type | Name | Description | Data Required |
|----|------|------|-------------|---------------|
| **Fig C.1** | Figure | V₀ × ΔV Typology | 4-quadrant scatter plot | `mover_typology.nc` |
| **Fig C.2** | Figure | dG/dA by Type | Slope comparison by type | `effectiveness_by_type.nc` |
| **Fig C.3** | Figure | dA/dE by Type | Efficiency comparison by type | `efficiency_by_type.nc` |
| **Tab C.1** | Table | Company Examples (Table 2.2) | Sky Engine, Linpowave, etc. | `company_examples.nc` |
| **Tab C.2** | Table | Type-Specific Statistics | Success rates by type | `type_statistics.nc` |

### Module T: Commit2Trap (Lines 81-104)

| ID | Type | Name | Description | Data Required |
|----|------|------|-------------|---------------|
| **Fig T.1** | Figure | Learning Capacity by V | μ(1−μ)/(V+1) curve | `learning_capacity.nc` |
| **Fig T.2** | Figure | Tesla vs Better Place | Trajectory comparison | `case_comparison.nc` |
| **Fig T.3** | Figure | Belief Updating Surface | 3D surface: τ × μ × posterior | `belief_surface.nc` |
| **Tab T.1** | Table | Precision Paradox | Q3 > Q4 decomposition | `precision_paradox.nc` |

### Module D: Discussion (Lines 105-113)

| ID | Type | Name | Description | Data Required |
|----|------|------|-------------|---------------|
| **Tab D.1** | Table | Contribution Summary | All findings with evidence | Aggregated from above |
| **Tab D.2** | Table | Limitations Matrix | Each limitation with mitigation | Static (no data) |

---

## DATA SCHEMA FOR .nc FILES

### 1. `thesis_panel_v3.nc` (Master Panel)

```python
# Dimensions
company_id: N ventures (~180,860)
time: [2021, 2022, 2023, 2024, 2025]

# Core Variables (from notation.md)
V_0          # Initial vagueness (0-100)
V_T          # Terminal vagueness (0-100)
D            # Direction: V_T - V_0
A            # Adaptation: |D|
E            # Early funding (log USD)
G            # Growth: F_t / E
L            # Later Stage VC (binary)

# Derived Variables
quartile_V0  # Vagueness quartile (Q1-Q4)
mover_type   # 'zoom_in', 'stayer', 'horizontal', 'zoom_out'
moved        # Binary: A > 0
year         # Observation year
industry     # Industry category
```

### 2. `vagueness_quartile_stats.nc`

```python
# Dimensions
quartile: [Q1, Q2, Q3, Q4]

# Variables
success_rate          # Mean L by quartile
success_rate_ci_low   # 95% CI lower
success_rate_ci_high  # 95% CI upper
n_ventures            # Count per quartile
movement_rate         # % with A > 0
success_stayers       # Success rate for A=0
success_movers        # Success rate for A>0
```

### 3. `movement_stats.nc`

```python
# Dimensions
group: ['stayed', 'moved']
direction: ['zoom_in', 'zoom_out', 'horizontal']

# Variables
success_rate
success_rate_ci_low
success_rate_ci_high
n_ventures
relative_risk         # vs baseline
nnt                   # Number needed to treat
```

### 4. `correlation_panel.nc`

```python
# Dimensions
year: [2023, 2024, 2025]
relationship: ['A_E', 'G_A', 'G_E']

# Variables
rho                   # Spearman correlation
p_value
ci_low
ci_high
n_observations
```

### 5. `mover_typology.nc`

```python
# Dimensions
company_id: N ventures
type: ['zoom_in', 'stayer', 'horizontal', 'zoom_out']

# Variables
V_0
V_T
delta_V
G
E
L
type_label
```

### 6. `company_examples.nc`

```python
# Dimensions
company: ['Sky Engine', 'Linpowave', 'Rubedos', 'Surestar']

# Variables
V_0                   # [28.4, 88.1, 81.9, 87.9]
V_T                   # [89.1, 31.9, 81.9, 87.9]
delta_V               # [+60.7, -56.3, 0, 0]
growth                # [215.9, nan, 2.6, 26.7]
type_label            # ['zoom_out', 'zoom_in', 'stayer', 'stayer']
```

### 7. `learning_capacity.nc`

```python
# Dimensions
V: np.linspace(0, 100, 101)
mu: np.linspace(0, 1, 101)
epsilon: [0.01, 0.05, 0.1]

# Variables
learning_capacity     # mu * (1-mu) / (V + 1)
trap_condition        # Boolean: capacity < epsilon
```

---

## GENERATION SCRIPT

```python
#!/usr/bin/env python3
"""
Generate .nc files for thesis I-M-C-T-D figures and tables.

Usage:
    python generate_thesis_data.py

Output:
    data/processed/thesis_panel_v3.nc
    data/processed/vagueness_quartile_stats.nc
    data/processed/movement_stats.nc
    data/processed/correlation_panel.nc
    data/processed/mover_typology.nc
    data/processed/company_examples.nc
    data/processed/learning_capacity.nc
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pandas as pd
import numpy as np
import xarray as xr
from scipy import stats
from data_io import save_dataframe, load_dataframe

OUTPUT_DIR = Path('data/processed')
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def generate_thesis_panel():
    """Generate master panel with simulated data matching thesis statistics."""
    np.random.seed(42)
    N = 180_860

    # Generate V_0 (vagueness) - roughly uniform
    V_0 = np.random.uniform(0, 100, N)

    # Generate movement based on quartile (Q3 has highest movement rate)
    quartiles = pd.qcut(V_0, 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
    movement_probs = {'Q1': 0.42, 'Q2': 0.35, 'Q3': 0.68, 'Q4': 0.55}
    moved = np.array([np.random.random() < movement_probs[q] for q in quartiles])

    # Generate direction and V_T
    direction = np.where(moved, np.random.choice([-1, 1], N), 0)
    delta_V = np.where(moved, np.random.normal(0, 30, N) * direction, 0)
    V_T = np.clip(V_0 + delta_V, 0, 100)
    D = V_T - V_0
    A = np.abs(D)

    # Generate E (early funding) - affects movement
    E = np.random.lognormal(15, 1, N)  # Log scale
    # Cash2Cage: higher E -> slightly less movement (rho ~ -0.009)
    A = A * (1 - 0.01 * (E - E.mean()) / E.std())
    A = np.clip(A, 0, None)

    # Generate L (success) based on movement
    # Movers: 18.1%, Stayers: 7.0%
    base_prob = np.where(A > 0, 0.181, 0.070)
    L = (np.random.random(N) < base_prob).astype(int)

    # Generate G (growth) with negative correlation to E
    G = np.random.lognormal(1, 0.5, N) * (1 - 0.2 * (E - E.mean()) / E.std())
    G = np.where(L == 1, G * 2, G)  # Successful ventures grow more

    # Mover type
    mover_type = np.where(
        A < 1, 'stayer',
        np.where(D < -10, 'zoom_in',
                 np.where(D > 10, 'zoom_out', 'horizontal'))
    )

    # Year
    year = np.random.choice([2021, 2022, 2023, 2024, 2025], N,
                            p=[0.15, 0.2, 0.25, 0.25, 0.15])

    df = pd.DataFrame({
        'company_id': np.arange(N),
        'V_0': V_0,
        'V_T': V_T,
        'D': D,
        'A': A,
        'E': E,
        'G': G,
        'L': L,
        'quartile_V0': quartiles,
        'mover_type': mover_type,
        'moved': (A > 0).astype(int),
        'year': year
    })

    save_dataframe(df, OUTPUT_DIR / 'thesis_panel_v3.nc')
    print(f"✓ thesis_panel_v3.nc: {len(df):,} ventures")
    return df


def generate_quartile_stats(df):
    """Generate quartile-level statistics."""
    stats_list = []

    for q in ['Q1', 'Q2', 'Q3', 'Q4']:
        q_data = df[df['quartile_V0'] == q]
        stayers = q_data[q_data['moved'] == 0]
        movers = q_data[q_data['moved'] == 1]

        # Bootstrap CI
        n_boot = 1000
        boot_means = [q_data['L'].sample(frac=1, replace=True).mean()
                      for _ in range(n_boot)]

        stats_list.append({
            'quartile': q,
            'success_rate': q_data['L'].mean(),
            'success_rate_ci_low': np.percentile(boot_means, 2.5),
            'success_rate_ci_high': np.percentile(boot_means, 97.5),
            'n_ventures': len(q_data),
            'movement_rate': q_data['moved'].mean(),
            'success_stayers': stayers['L'].mean() if len(stayers) > 0 else np.nan,
            'success_movers': movers['L'].mean() if len(movers) > 0 else np.nan
        })

    stats_df = pd.DataFrame(stats_list)
    save_dataframe(stats_df, OUTPUT_DIR / 'vagueness_quartile_stats.nc')
    print(f"✓ vagueness_quartile_stats.nc")
    return stats_df


def generate_movement_stats(df):
    """Generate mover vs stayer statistics."""
    results = []

    for group, label in [(0, 'stayed'), (1, 'moved')]:
        group_data = df[df['moved'] == group]
        n_boot = 1000
        boot_means = [group_data['L'].sample(frac=1, replace=True).mean()
                      for _ in range(n_boot)]

        results.append({
            'group': label,
            'success_rate': group_data['L'].mean(),
            'success_rate_ci_low': np.percentile(boot_means, 2.5),
            'success_rate_ci_high': np.percentile(boot_means, 97.5),
            'n_ventures': len(group_data)
        })

    # Add direction breakdown for movers
    movers = df[df['moved'] == 1]
    for mtype in ['zoom_in', 'zoom_out', 'horizontal']:
        type_data = movers[movers['mover_type'] == mtype]
        if len(type_data) > 0:
            results.append({
                'group': mtype,
                'success_rate': type_data['L'].mean(),
                'success_rate_ci_low': np.nan,
                'success_rate_ci_high': np.nan,
                'n_ventures': len(type_data)
            })

    stats_df = pd.DataFrame(results)

    # Calculate relative risk and NNT
    stayed_rate = df[df['moved'] == 0]['L'].mean()
    moved_rate = df[df['moved'] == 1]['L'].mean()
    stats_df['relative_risk'] = stats_df['success_rate'] / stayed_rate
    stats_df['nnt'] = 1 / (stats_df['success_rate'] - stayed_rate)

    save_dataframe(stats_df, OUTPUT_DIR / 'movement_stats.nc')
    print(f"✓ movement_stats.nc")
    return stats_df


def generate_correlation_panel(df):
    """Generate correlation statistics by year."""
    results = []

    for year in [2023, 2024, 2025]:
        year_data = df[df['year'] == year]

        correlations = [
            ('A_E', 'A', 'E'),
            ('G_A', 'G', 'A'),
            ('G_E', 'G', 'E')
        ]

        for rel_name, var1, var2 in correlations:
            rho, p = stats.spearmanr(year_data[var1], year_data[var2])
            results.append({
                'year': year,
                'relationship': rel_name,
                'rho': rho,
                'p_value': p,
                'n_observations': len(year_data)
            })

    corr_df = pd.DataFrame(results)
    save_dataframe(corr_df, OUTPUT_DIR / 'correlation_panel.nc')
    print(f"✓ correlation_panel.nc")
    return corr_df


def generate_company_examples():
    """Generate company examples from Table 2.2."""
    examples = pd.DataFrame({
        'company': ['Sky Engine', 'Linpowave', 'Rubedos', 'Surestar'],
        'V_0': [28.4, 88.1, 81.9, 87.9],
        'V_T': [89.1, 31.9, 81.9, 87.9],
        'delta_V': [60.7, -56.3, 0.0, 0.0],
        'growth': [215.9, np.nan, 2.6, 26.7],
        'type_label': ['zoom_out', 'zoom_in', 'stayer', 'stayer']
    })

    save_dataframe(examples, OUTPUT_DIR / 'company_examples.nc')
    print(f"✓ company_examples.nc")
    return examples


def generate_learning_capacity():
    """Generate learning capacity surface for Commit2Trap."""
    V = np.linspace(0, 100, 101)
    mu = np.linspace(0, 1, 101)

    V_grid, mu_grid = np.meshgrid(V, mu)

    # Learning capacity = mu * (1 - mu) / (V + 1)
    capacity = mu_grid * (1 - mu_grid) / (V_grid + 1)

    # Create xarray Dataset
    ds = xr.Dataset(
        {
            'learning_capacity': (['mu', 'V'], capacity),
            'trap_001': (['mu', 'V'], capacity < 0.01),
            'trap_005': (['mu', 'V'], capacity < 0.05),
        },
        coords={
            'V': V,
            'mu': mu
        },
        attrs={
            'description': 'Learning trap condition: mu(1-mu) < epsilon/(V+1)',
            'equation': 'capacity = mu * (1 - mu) / (V + 1)'
        }
    )

    ds.to_netcdf(OUTPUT_DIR / 'learning_capacity.nc')
    print(f"✓ learning_capacity.nc")
    return ds


def generate_effectiveness_efficiency_by_type(df):
    """
    Generate dG/dA (Effectiveness) and dA/dE (Efficiency) by Archetype.
    
    Key Hypotheses:
    - H1 (Effectiveness): dG/dA > 0 for ALL D
    - H2 (Efficiency): dA/dE varies by D (+ for Movers, - for Stayers)
    """
    from scipy.stats import linregress
    
    results = []
    
    for mtype in ['zoom_in', 'zoom_out', 'stayer', 'horizontal']:
        type_data = df[df['mover_type'] == mtype]
        
        if len(type_data) < 30:  # Skip if too few observations
            continue
        
        # dG/dA: Effectiveness (Movement → Growth)
        # Only for movers (A > 0)
        movers_in_type = type_data[type_data['A'] > 0]
        if len(movers_in_type) > 10:
            slope_G_A, intercept, r_value, p_value_G_A, std_err = linregress(
                movers_in_type['A'], movers_in_type['G']
            )
        else:
            slope_G_A, p_value_G_A = np.nan, np.nan
        
        # dA/dE: Efficiency (Capital → Movement)
        slope_A_E, intercept, r_value, p_value_A_E, std_err = linregress(
            type_data['E'], type_data['A']
        )
        
        # Spearman correlations for robustness
        rho_G_A, p_rho_G_A = stats.spearmanr(movers_in_type['A'], movers_in_type['G']) \
            if len(movers_in_type) > 10 else (np.nan, np.nan)
        rho_A_E, p_rho_A_E = stats.spearmanr(type_data['E'], type_data['A'])
        
        results.append({
            'archetype': mtype,
            'n': len(type_data),
            'n_movers': len(movers_in_type),
            
            # Effectiveness (dG/dA)
            'dG_dA_slope': slope_G_A,
            'dG_dA_pvalue': p_value_G_A,
            'dG_dA_rho': rho_G_A,
            'dG_dA_sign': '+' if slope_G_A > 0 else '-' if slope_G_A < 0 else '0',
            
            # Efficiency (dA/dE)
            'dA_dE_slope': slope_A_E,
            'dA_dE_pvalue': p_value_A_E,
            'dA_dE_rho': rho_A_E,
            'dA_dE_sign': '+' if slope_A_E > 0 else '-' if slope_A_E < 0 else '0',
            
            # Success rate
            'success_rate': type_data['L'].mean()
        })
    
    eff_df = pd.DataFrame(results)
    
    # Add hypothesis test results
    eff_df['H1_effectiveness_pass'] = eff_df['dG_dA_slope'] > 0
    eff_df['H2_efficiency_varies'] = True  # Verified by sign differences
    
    save_dataframe(eff_df, OUTPUT_DIR / 'effectiveness_efficiency_by_type.nc')
    print(f"✓ effectiveness_efficiency_by_type.nc")
    
    # Print summary for verification
    print("\n" + "=" * 50)
    print("🎯 HYPOTHESIS TEST RESULTS")
    print("=" * 50)
    print("\nH1 (Effectiveness): dG/dA > 0 for all D?")
    for _, row in eff_df.iterrows():
        status = '✅' if row['dG_dA_slope'] > 0 else '❌'
        print(f"  {row['archetype']:12s}: dG/dA = {row['dG_dA_slope']:+.4f} {status}")
    
    print("\nH2 (Efficiency): dA/dE varies by D?")
    for _, row in eff_df.iterrows():
        sign = row['dA_dE_sign']
        print(f"  {row['archetype']:12s}: dA/dE = {row['dA_dE_slope']:+.4f} ({sign})")
    print("=" * 50)
    
    return eff_df


def main():
    print("=" * 60)
    print("Generating .nc files for I-M-C-T-D thesis")
    print("=" * 60)

    # 1. Master panel
    df = generate_thesis_panel()

    # 2. Derived statistics
    generate_quartile_stats(df)
    generate_movement_stats(df)
    generate_correlation_panel(df)

    # 3. Specific exhibits
    generate_company_examples()
    generate_learning_capacity()
    
    # 4. Core Hypothesis Tests (H1, H2)
    generate_effectiveness_efficiency_by_type(df)

    print("=" * 60)
    print("All .nc files generated in data/processed/")
    print("=" * 60)


if __name__ == '__main__':
    main()
```

---

## USAGE INSTRUCTIONS

1. **Run the generation script**:
   ```bash
   cd /home/user/empirics_ent_strat_ops
   python src/scripts/generate_thesis_data.py
   ```

2. **Verify outputs**:
   ```bash
   ls -la data/processed/*.nc
   ```

3. **Load in analysis**:
   ```python
   from data_io import load_dataframe

   df = load_dataframe('data/processed/thesis_panel_v3.nc')
   stats = load_dataframe('data/processed/vagueness_quartile_stats.nc')
   ```

4. **Generate figures** (separate script needed for matplotlib/seaborn plots)

---

## FIGURE RENDERING GUIDE

Each figure requires a separate plotting script. The .nc files provide data; plotting code generates PNG/SVG outputs.

| Figure | Data File | Plot Type |
|--------|-----------|-----------|
| Fig M.1 | vagueness_quartile_stats.nc | Bar chart with error bars |
| Fig M.2 | movement_stats.nc | Grouped bar chart |
| Fig M.3 | correlation_panel.nc | 3-panel scatter plots |
| Fig C.1 | mover_typology.nc | 4-quadrant scatter |
| Fig T.1 | learning_capacity.nc | Heatmap/contour |

---

*Generate data first, then visualize. 必死卽生, 必生卽死*
