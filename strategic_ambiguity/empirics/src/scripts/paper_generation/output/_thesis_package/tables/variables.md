---
modified:
  - 2025-12-10T12:57:07-05:00
  - 2025-12-11T10:49:31-05:00
  - 2025-12-12T14:00:00-05:00
---

# Variable Definitions (Paper M/C/T)

## Primary Variables

| **Variable Symbol** | **Variable Name**      | **Definition**                                                                           | **Unit / Type**                 | **Range**    | **Time**          |
| ------------------- | ---------------------- | ---------------------------------------------------------------------------------------- | ------------------------------- | ------------ | ----------------- |
| **$G_t$**           | **Growth (DV)**        | Funding growth rate: $G_t = F_t / E$<br>Primary dependent variable for Paper M          | Ratio                           | Continuous   | $t$ (Interval)    |
| **$E$**             | **Early Capital**      | Amount of early-stage funding raised.                                                    | Currency ($M)                   | Continuous   | $0$ (Start)       |
| $F_t$               | Later Capital          | Amount of later-stage funding raised.                                                    | Currency ($M)                   | Continuous   | $t$ (Interval)    |
| **$V$**             | **Vagueness**          | Vagueness of early-stage positioning/promise.                                            | Score                           | $[0, 100]$   | $0$ (Start)       |
| **$D_t$**           | **Directional Change** | The raw change of position (vector): $D_t = V_T - V_0$                                   | Score                           | $[-M, +M]$   | $t$ (Interval)    |
| **$A_t$**           | **Adaptive Capacity**  | The absolute change of position: $A_t = |D_t|$<br>Represents "Movement"                  | Score                           | $[0, M]$     | $t$ (Interval)    |

## Deprecated Variables

| **Variable Symbol** | **Variable Name**      | **Definition**                                                                           | **Status**                      |
| ------------------- | ---------------------- | ---------------------------------------------------------------------------------------- | ------------------------------- |
| $L$                 | Long-term Success      | Binary: 1 if LastFinancingDealType == 'Later Stage VC'                                   | **Deprecated** → Use $G$ instead |

## Notes

- **Paper M**: Uses $G$ (Growth = $F_t/E$) as continuous DV
- **Paper C**: Uses $G$ for Golden Cage mechanism analysis
- **Paper T**: Uses $G$ in simulation models
- $L$ (binary) was used in earlier Paper U drafts but replaced by continuous $G$ for better statistical power
