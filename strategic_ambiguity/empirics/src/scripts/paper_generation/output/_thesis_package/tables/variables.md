---
modified:
  - 2025-12-10T12:57:07-05:00
  - 2025-12-11T10:49:31-05:00
---

| **Variable Symbol** | **Variable Name**      | **Definition**                                                                           | **Unit / Type**                 | **Range**    | **Time**          |
| ------------------- | ---------------------- | ---------------------------------------------------------------------------------------- | ------------------------------- | ------------ | ----------------- |
| **$L$**             | **Long-term Success**  | Probability of later-stage funding                                                       | Probability                     | $\in [0, 1]$ | $T$ (End)         |
| $F_t$               | Later Capital          | Amount of later-stage funding raised.                                                    | Currency ($M)                   | Continuous   | $t$ (Interval)    |
| **$E$**             | **Early Capital**      | Amount of early-stage funding raised.                                                    | Currency ($M)                   | Continuous   | $0$ (Start)       |
| **$G_t$**           | **Growth Ratio**       | Momentum of value creation: $\frac{F_t - E}{E}$<br>$G_t$ is proportional to L when t = T | Ratio                           | Continuous   | $t$ (Interval)    |
| **$V$**             | **Vagueness**          | Vagueness of early-stage positioning/promise.                                            | Score                           | $[0, 100]$   | $0$ (Start)       |
| **$D_t$**           | **Directional Change** | The raw change of position (vector).                                                     | Score                           | $[-M, +M]$   | $t$ (Interval)    |
| **$A_t$**           | **Adaptive Capacity**  | The absolute change of position: $\\D_t$.                                                | Represents "Movement."<br>Score | $[0, M]$     | $t$<br>(Interval) |
