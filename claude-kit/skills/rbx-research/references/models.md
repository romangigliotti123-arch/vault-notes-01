# Model choice per stage (automatic; the user can override)

Default rule: haiku for scouting, listing, triage and per-item extraction; sonnet for synthesis and most judgement work; opus ONLY for the single final cross-source synthesis, ONLY in the Heavy tier, ONLY if the user allowed it at the limits question.

Use the aliases `haiku`, `sonnet`, `opus` (scripts pass them to `claude -p --model <alias>`; the Agent tool accepts the same). Do not hard-code dated model ids; if the environment names concrete current ids, mention them in the plan but keep passing aliases.

| Stage | Light (<= ~$2) | Moderate (<= ~$8) | Heavy (> ~$8) | Effort |
|---|---|---|---|---|
| Scout, list, dedupe | scripts only | scripts only | scripts only | n/a |
| Creator judging (ratings 0-5, batches of 10) | haiku | sonnet | sonnet | low / medium |
| Per-item extraction (video, post, README, thread) | haiku | haiku | haiku | low |
| Dense technical items (docs with code, papers, long high-relevance pages) | haiku | sonnet, at most 20% of items | sonnet, at most 30% of items | medium |
| Theme synthesis + contradiction check (one call per theme) | sonnet | sonnet | sonnet | medium |
| Trust layer: label + fact-check claims (one call per theme) | haiku | sonnet | sonnet | medium |
| Creator credibility judging (one call per creator, optional) | haiku | sonnet (haiku beyond 10 creators) | sonnet | low |
| Final playbook + open questions + 10 recall Q&A | sonnet | sonnet | opus if allowed, else sonnet | medium / high |

Overrides: "all sonnet" (raise `limits.sonnet_share` in `state.json`), "haiku only" (set it to 0), "no opus" (default). `rt.py init --force` with the flags also resets them. `--synth-model haiku` makes synthesis about 4x cheaper at lower quality. Mode A workers are full agents: somewhat more overhead per item than mode B.

## Cost estimates (ranges, not quotes)
Per-call estimates: haiku extraction $0.002-0.008/item, sonnet theme synthesis $0.05-0.20, final synthesis $0.10-0.40 (opus $0.50-2.00); real spend comes from the CLI `total_cost_usd` in `costs.csv`, else `scripts/prices.json`. [cold:rbx-research/incident-and-costs.md] read only to see the incident behind the caps or to estimate per-call costs.
Budget split used by the plan: about 5% ranking, 50% extraction (57% when credibility is off), 25% synthesis, 8% trust layer, 7% credibility, 5% reserve. Extraction stops at 75% of the budget so synthesis always has room.
Subscription users: dollars are API-equivalent value, not a bill; the plan's window share (about 5% of a 5-hour window per dollar) is a rough guide, check `/usage`.
