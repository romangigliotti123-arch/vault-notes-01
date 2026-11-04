<!-- cold: rbx-research/incident-and-costs.md | read when: read only to see the incident behind the caps or to estimate per-call costs. -->

## From skills/rbx-research/references/budget-and-caps.md :: What happened (so it is not repeated)

Eleven parallel high-effort research workers, several spawning their own helpers, used a whole 5-hour usage window in about 30 minutes and stopped the other jobs too. The cost is almost entirely in workers (hundreds of millions of cache-read tokens), not in the orchestrating session. Hence: bounded fan-out, no nested workers, small tool output, no polling loops.

## From skills/rbx-research/references/models.md :: Why: extraction is high-volume reading comprehension (haiku 

Why: extraction is high-volume reading comprehension (haiku is accurate enough and the cheapest place to spend); synthesis is low-volume and where quality shows (sonnet); the final cross-source call is a single call, so opus there costs a few dollars at most while improving the part the user reads first.

## From skills/rbx-research/references/models.md :: Measured on small runs with the haiku alias (about 4-6k inpu

Measured on small runs with the haiku alias (about 4-6k input tokens and 1.5-2.5k output tokens per item): $0.002-$0.008 per item. The other rows are scaled estimates; real spend is taken from the `total_cost_usd` the CLI reports and logged in `costs.csv`. If it is missing, `scripts/prices.json` supplies rough per-million-token prices; check them against current Anthropic pricing before relying on them.

| Call | Estimated USD |
|---|---|
| Extraction, haiku | 0.002 - 0.008 |
| Extraction, sonnet (dense item) | 0.02 - 0.07 |
| Creator judging batch of 10, haiku / sonnet | 0.003 - 0.01 / 0.015 - 0.05 |
| One theme synthesis, sonnet | 0.05 - 0.20 |
| Final synthesis, sonnet / opus | 0.10 - 0.40 / 0.50 - 2.00 |
| Trust-layer call per theme, haiku / sonnet | 0.01 - 0.04 / 0.04 - 0.15 |
| Credibility call per creator, haiku / sonnet | 0.01 - 0.04 / 0.04 - 0.12 |
