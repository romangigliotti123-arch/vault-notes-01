---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/workflows.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated
accessed: 2026-10-29
reliability: high (official; full page read)
---
# Dynamic workflows: resume, stall and usage-limit behaviour
## Key claims
- A workflow is a JS script run in an isolated runtime; intermediate results stay in script variables. `Date.now()`, `Math.random()`, no-arg `new Date()` THROW inside the script "so that a relaunched run repeats the same agent() calls" (determinism for replay, same idea as Temporal/DBOS).
- Resume: completed agents return saved results on relaunch; first agent whose prompt differs, or any failed agent, and everything after it, reruns ("a failure in the middle of a fan-out reruns work that already finished"). If the session exits the run does not continue on its own; saved results live under the session dir in `~/.claude/projects/`; `claude --resume` then ask Claude to relaunch; fresh session => `nothing to resume`.
- Stalls: an agent whose output stops arriving restarts from the same prompt (max 5 restarts, 6 attempts) then the `agent()` call fails (`agent stalled on all 6 attempts`); `stallMs` per call or `CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS` globally; results become `null` inside pipeline()/parallel().
- Usage limit: run pauses and resumes at reset (v2.1.271+) BUT NOT in `claude -p`, background sessions, Remote Control or teammate sessions; max two waits then agent fails.
- Caps: 16 concurrent agents default, 1,000 agents per run, Large-workflow warning >25 agents or >1.5M tokens. No mid-run user input (use one workflow per stage for sign-off).

## Used by
[[topic-long-running-always-on-agents]]
