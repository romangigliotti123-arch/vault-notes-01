# Model and effort routing

| Job | Model | Effort |
|---|---|---|
| Read-only lookup, triage, log reading, extraction, summary, inventory | haiku (`haiku-scout`) | medium |
| Install/setup/script/debug/research/docs/tests with a clear spec | sonnet (`sonnet-worker`) | medium |
| Verification-critical or edge-case heavy: security, data, multi-file edits, remote machines | sonnet | high |
| Whole app/game from scratch, large multi-file build, hard architecture | opus (`opus-builder`) | high |
| Same job after sonnet failed twice with a CORRECT brief | opus | high |

- **Opus only for the hardest work.** Never for installs, setup, lookups, routine scripting or research. In doubt use sonnet.
- xhigh/max effort only with a written reason (heavy against the usage cap).
- Never effort `low` for anything that changes files, systems or accounts.
- A report showing a wrong approach: re-brief or go up one tier; do not re-run the same brief at higher effort. A missing fact is fixed in the brief, not with a bigger model.
- Do not switch your own (manager) model mid-session; delegate (each switch rebuilds the cache).
- Subagents cost more than they look (briefing + report handoff): do trivial checks inline.
- Parallel: independent jobs on disjoint targets, each right-sized; total agents <= the user's cap.
- Dynamic workflow scripts only for the same step repeated over many items (sweeps, folder-wide lint-fix), not for design or sequential judgment.
- Read `/usage` attribution before changing this table. Roblox game work has its own table: `rbx-workflow/references/manager.md` section 10.
