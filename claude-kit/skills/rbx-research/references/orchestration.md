# Orchestration: three modes (chosen automatically, shown in the plan)

`rt.py init --agent-tool yes|no` records whether THIS session has the Agent/subagent tool; `--mode A|B|C` forces a mode. Auto: Agent tool present -> A; else `claude` command found -> B; else C. `orch.py mode --out OUT` prints the choice.

| Mode | Who does the model work | Concurrency | Cost shape |
|---|---|---|---|
| A manager | Agent-tool workers briefed by this session | up to the cap, in waves | full agents (haiku for extraction), more overhead than B; batches via `--per-worker` |
| B headless | `claude -p` calls with no tools from the scripts (`process.py run`, `cred.py judge`, `trust.py verify`) | pool = cap | cheapest, fully scripted, can run in the background |
| C sequential | this session, following the same briefs one at a time | 1 | no extra processes; slowest |

Hard rules in every mode: workers never spawn workers; at most `cap` workers alive; small tool output; no polling loops; stop on any usage-limit message and report; state is on disk, so every command resumes.

## Mode A protocol (the session is the manager)
1. Size the job: `rt.py plan` shows items, cap, time. `orch.py wave` sizes each worker's batch (extract 8 ids, credibility 3 creators, verify 1 theme; change with `--per-worker`).
2. Brief: `orch.py wave --out OUT --stage extract|cred|verify` claims work, writes one brief per worker (`OUT/.cache/briefs/`) and prints `W<k> model=<m> ids=<n> brief=<path>`. Each brief is AI to AI: role and no-spawn rule, exact scope (ids), step commands, DONE WHEN, budget, STOP RULE, REPORT FORMAT (one line, at most 40 words, never the extraction itself). Exit 2 = `STOP <reason>` (time, budget, usage limit): launch nothing. Exit 3 = previous wave not reported yet: finish it first.
3. Launch ALL printed workers in ONE message with the Agent tool (concurrently), `model` as printed, prompt = `Read and follow the brief at <path>.` Add no more workers than printed. Wait once.
4. Verify each report with cheap independent checks, not trust: `orch.py report --out OUT --stage S --worker K --text "<report>"`. Extract: the file exists, parses, matches the id, and its numeric claims occur in the cached source text (catches fabricated numbers). Credibility: result schema and claim count. Verify: every theme item got a label. `FAIL` re-queues the ids with ONE retry (second failure marks them failed and names them in the gaps). `LIMIT` (exit 2) = a worker saw a usage limit: stop, tell the user, resume later.
5. Track: `orch.py status --out OUT` (mode, cap, workers per wave, spend vs budget, time left, stop reason). Repeat from step 2 until `NOTHING_LEFT`.
6. Saved state: manifest statuses, `.cache/orch.json` (waves, claims, tries), `costs.csv`. A new session resumes by running `wave` again; claims older than 30 minutes expire. Worker spend is logged from reported token counts (rows `extract-subagent`, `cred-subagent`, `trust-verify-subagent`), estimates.

## Mode B
`process.py run --out OUT` (background, pool = cap, waits on limits, one retry per item), then `synth.py themes`, `cred.py judge`, `trust.py verify` (one call at a time), `synth.py final`.

## Mode C
The same `wave` loop with one worker; read the brief and do it yourself. Same prep/save scripts, same report checks.

## Try it without spending anything
`PY SKILL_DIR/scripts/selftest.py` runs mode A offline (`DTR_STUB=1`, tests only). [cold:rbx-research/selftest-detail.md] read only to understand what the offline self-test simulates.
