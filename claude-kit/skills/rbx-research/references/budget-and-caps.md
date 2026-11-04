# Limits, caps and why they are strict

## What happened (so it is not repeated)
Eleven parallel high-effort workers (some spawning helpers) used a 5-hour usage window in about 30 minutes: hence bounded fan-out, no nested workers, small tool output, no polling. [cold:rbx-research/incident-and-costs.md] read only to see the incident behind the caps or to estimate per-call costs.

## Rules enforced by this skill
- Questions first (budget, time, worker cap, depth/sources); nothing runs before they are answered.
- Worker cap = model-calling workers alive at once (Agent-tool subagents plus headless `claude -p` calls). `orch.py wave` never briefs more than the cap and refuses a new wave until the previous one was reported. `process.py run` creates exactly that many threads. Synthesis calls run one at a time.
- Workers have no tools in script mode (`--tools ""`), so they cannot spawn anything; in subagent mode (`subagent-mode.md`) they are told not to.
- The main session only orchestrates: it never reads whole transcripts or notes. Wait, do not poll: start `process.py run` in the background and wait for the completion notice.
- Limits are checked before every dispatch (`check_limits` in `scripts/common.py`). Extraction ends at 80% of the time window and 75% of the budget; synthesis may use the rest. Stop reasons: `time-limit`, `budget`, `usage-limit`, `exhausted`, `max-items`.
- On a usage-limit or 429/overloaded response the run stops cleanly (no retry storm); state is saved after every item, so the same command resumes.
- Before a Heavy or long run on a subscription, glance at `/usage`: 5-hour window already above about 70% = suggest Light or waiting.

## Resume semantics
`manifest.json` holds every item with `status` (pending, done, skipped, failed, claimed). Extractions live in `.cache/extracts/<id>.json` (present = done); transcripts and fetched text are cached in `.cache/`. `process.py run` re-queues interrupted items, skips done ones, dedupes identical content by hash. `costs.csv` is the source of truth for spend and is summed on every check. `rt.py extend --budget-usd TOTAL --minutes M` sets new limits for a resumed run.

## Failure handling
One retry per failing item (status `failed` after the second try, with the reason). Network blocks go to `.cache/unreachable.json` and `00-README.md`; the run continues with the other sources.
