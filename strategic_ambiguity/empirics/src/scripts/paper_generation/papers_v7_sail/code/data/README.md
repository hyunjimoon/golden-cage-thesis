# Thesis Data Files

## Final Analysis Panel

| File | Description | Size |
|:-----|:------------|-----:|
| `thesis_panel_v3.nc` | Final analysis panel (NetCDF) | 13MB |

## Source Data (Not Included - Large Files)

Source data is located at `empirics/data/processed/`:

| File | Description | Size | Required |
|:-----|:------------|-----:|:--------:|
| `vagueness_timeseries.parquet` | V, E variables (2021-2025) | 131MB | ✅ |
| `features_all.parquet` | G, L variables | 521MB | ✅ |

## Regeneration

To regenerate `thesis_panel_v3.nc`:

```bash
cd empirics
python src/scripts/paper_generation/papers_v6/_shared/01_raw_to_processed.py --include-missing-G
```

## Variables in thesis_panel_v3.nc

| Variable | Description |
|:---------|:------------|
| `V_0` | Initial vagueness (2021) |
| `V_T` | Final vagueness (2025) |
| `D` | Direction = V_T - V_0 |
| `M` | Movement = \|D\| |
| `E` | Early funding (M USD) |
| `G` | Growth rate (continuous) |
| `L` | Success = Later Stage VC |
| `moved` | Binary mover indicator |
| `mover_type` | zoom_in / zoom_out / stayer |

## Methodology

**Conditional Quantile Thresholds:**
- 59.6% of ventures have M=0 (zero-inflation)
- Threshold = median of non-zero M = 0.5
- Mover: M > 0.5, Stayer: M ≤ 0.5

---
*Generated: 2026-01-09*
