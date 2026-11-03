# Model choice per stage (automatic; the user can override)

Default rule: haiku for scouting, listing, triage and per-item extraction; sonnet for synthesis and most judgement work; opus ONLY for the single final cross-source synthesis, ONLY in the Heavy tier, ONLY if the user allowed it at the limits question.

Use the aliases `haiku`, `sonnet`, `opus` (the scripts pass them to `claude -p --model <alias>` and the Agent tool accepts the same aliases). Do not hard-code dated model ids: the alias resolves to the newest model the user's installation offers. If the environment or system prompt names concrete current model ids, mention them in the plan for transparency, but keep passing aliases.

| Stage | Light (<= ~$2) | Moderate (<= ~$8) | Heavy (> ~$8) | Effort |
|---|---|---|---|---|
| Scout, list, dedupe | scripts only (no model) | scripts only | scripts only | n/a |
| Creator judging (ratings 0-5, batches of 10) | haiku | sonnet | sonnet | low / medium |
| Per-item extraction (video, post, README, thread) | haiku | haiku | haiku | low |
| Dense technical items (docs with code, papers, long high-relevance pages) | haiku | sonnet, at most 20% of items | sonnet, at most 30% of items | medium |
| Theme synthesis + contradiction check (one call per theme) | sonnet | sonnet | sonnet | medium |
| Trust layer: label + fact-check claims (one call per theme) | haiku | sonnet | sonnet | medium |
| Creator credibility judging (one call per creator, optional) | haiku | sonnet (haiku beyond 10 creators) | sonnet | low |
| Final playbook + open questions + 10 recall Q&A | sonnet | sonnet | opus if allowed, else sonnet | medium / high |

Why: extraction is high-volume reading comprehension (haiku is accurate enough and the cheapest place to spend); synthesis is low-volume and where quality shows (sonnet); the final cross-source call is a single call, so opus there costs a few dollars at most while improving the part the user reads first.

Overrides the user may ask for: "all sonnet" (raise `limits.sonnet_share` in `state.json`), "haiku only" (set it to 0), "no opus" (the default). `rt.py init --force` with the flags also resets them.

## Cost estimates (ranges, not quotes)
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

Budget split used by the plan: about 5% ranking, 50% extraction (57% when credibility is off), 25% synthesis, 8% trust layer, 7% credibility, 5% reserve. Extraction stops at 75% of the budget so synthesis always has room.

Subscription users: the dollar figures are API-equivalent value, not a bill. The plan prints a rough window share using about 5% of a 5-hour window per dollar (one measured Light run); real shares differ a lot by plan, model and load, so treat it as a guide and check `/usage`. `--synth-model haiku` makes synthesis about 4x cheaper at lower quality. In manager mode A the workers are full agents, so expect somewhat more overhead per item than mode B.
