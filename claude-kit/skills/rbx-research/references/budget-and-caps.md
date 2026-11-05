# Limits, caps and why they are strict

## What happened (so it is not repeated)
Eleven parallel high-effort research workers, several spawning their own helpers, used a whole 5-hour usage window in about 30 minutes and stopped the other jobs too. The cost is almost entirely in workers (hundreds of millions of cache-read tokens), not in the orchestrating session. Hence: bounded fan-out, no nested workers, small tool output, no polling loops.

## Rules enforced by this skill
- Questions first (usage budget, time, worker cap, depth/sources). Nothing runs before they are answered.
- Worker cap = number of model-calling workers alive at once, counting Agent-tool subagents and the script's headless `claude -p` calls together. `orch.py wave` never briefs more than the cap and refuses a new wave until the previous one was reported. `process.py run` creates exactly that many threads. Synthesis calls run one at a time.
- Workers have no tools in script mode (`--tools ""`), so they cannot spawn anything. In subagent mode (see `subagent-mode.md`) the subagents are told not to spawn subagents.
- The main session only orchestrates. It never reads whole transcripts or notes; scripts print summaries.
- Wait, do not poll: start `process.py run` in the background and wait for the completion notice.
- Limits are checked before every dispatch (`check_limits` in `scripts/common.py`). Extraction ends at 80% of the time window and 75% of the budget; synthesis may use the remainder. Stop reasons: `time-limit`, `budget`, `usage-limit`, `exhausted`, `max-items`.
- On a usage-limit or 429/overloaded response the run stops cleanly (no retry storm). State is saved after every item, so the same command resumes.
- Before a Heavy or long run on a subscription, glance at `/usage`: if the 5-hour window is already above about 70%, suggest Light or waiting.

## Resume semantics
`manifest.json` holds every item with `status` (pending, done, skipped, failed, claimed). Extractions live in `.cache/extracts/<id>.json`; a present file means done. Transcripts and fetched text are cached in `.cache/`. `process.py run` re-queues interrupted items, skips done ones and dedupes identical content by hash. `costs.csv` is the source of truth for spend and is summed on every check. `rt.py extend --budget-usd TOTAL --minutes M` sets new limits for a resumed run.

## Failure handling
One retry per failing item (status `failed` after the second try, with the reason). Network blocks are recorded in `.cache/unreachable.json` and listed in `00-README.md`; the run continues with the other sources.
