---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2502.15840
type: paper
author: Axel Backlund, Lukas Petersson (Andon Labs)
published: 2025-02-20
accessed: 2026-10-29
reliability: high (benchmark paper, abstract read)
---
# Vending-Bench: long-term coherence of autonomous agents
## Key claims
- Simulated vending business run over runs often exceeding 20M tokens; agents manage inventory, orders, prices, fees.
- All tested models have some runs that fall apart: misread delivery schedules, forget orders, fall into "tangential meltdown loops from which they rarely recover".
- Breakdowns do not clearly track the context window filling, so memory limits are not the main cause: long-horizon goal drift is a distinct failure.
## Quotable
> "meltdown" loops from which models "rarely recover" (abstract wording)

## Used by
[[topic-multi-agent-failure-modes]]
