# ¶5 수진_table(I): Variable Definitions

> **Agent**: 수진 (見 Observe)
> **Row**: Table (T)
> **Status**: 📝 Draft

---

## Content

We operationalize three primary constructs:

**Tab-I2: Variable Definitions**

| Variable | Name | Definition | Measurement | Example |
|:--------:|:-----|:-----------|:------------|:--------|
| **F** | Funding | Early-stage capital | Log(Seed + Series A) | $5M → 6.7 |
| **R** | Repositioning | Strategic change | \|B_T − B_0\| | 60 pts change |
| **G** | Growth | Funding multiplier | Total ÷ Early | 200× |

---

## Operationalization Detail

### F (Funding)
- **Source**: PitchBook
- **Range**: $100K - $100M (log scale)
- **Period**: Seed + Series A rounds

### R (Repositioning)
- **Source**: Company description keywords
- **B scale**: 0 (narrow/specific) to 100 (broad/vague)
- **Threshold**: R ≥ 10 = Mover, R < 10 = Stayer

### G (Growth)
- **Numerator**: Total funding (all rounds)
- **Denominator**: Early-stage funding
- **Interpretation**: How much initial investment multiplied

---

## Dependencies

- **Upstream**: ¶3 (찰리_sol) — decomposition equation
- **Downstream**: ¶5 (영지_fig) — visualization
