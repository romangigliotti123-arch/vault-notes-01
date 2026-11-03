---
tags: [manager-kb, source]
url: https://github.com/ruvnet/ruflo (formerly ruvnet/claude-flow)
type: repo
author: Reuven Cohen (rUv)
published: undated (README read 2026-10-29; first commit June 2, 2025 per README)
accessed: 2026-10-29
reliability: low (marketing-heavy README, self-reported counts; code not read)
---
# Ruflo / Claude Flow (agent meta-harness)
## Key claims
- Positioning: "Agent = Model + Harness ... Ruflo is the harness": 100+ specialised agents, swarms, "self-learning memory", federation between machines, "314 MCP tools / 26 CLI commands". Two install paths with very different surface: Claude Code plugins (slash commands, a few skills, agent defs; zero files in workspace; only `ruflo-core` registers an MCP server) vs `npx ruflo init` (98 agents, 60+ commands, 30 skills, MCP server, hooks, daemon, writes `.claude/`, `.claude-flow/`, `CLAUDE.md`, settings).
- Uses Claude Code "mods" (2.1.287+): `ruflo-mods` "routes prompts and enforces policy in-process"; README warns "mods run with your account's permissions and are not sandboxed, so read the code first". `ruflo-console` = cockpit showing workflows, agents, models, tokens, cost; "Claude control" setting with levels read/write/manage/full and ask/auto approval, default read+ask; "network, spending and destructive actions require confirmation even in auto".
- Plugin catalogue (35) includes autopilot (agents run autonomously in a loop), loop-workers (background tasks on a timer), goals, federation (agents on different machines), aidefence (prompt-injection/PII scan), rag-memory/agentdb/ruvector memory stores. No benchmark evidence for orchestration gains in the README; the demo section itself says the recorded session is "not evidence of completed swarm work or memory recall".
- Relevance: shows the opposite design philosophy to HumanLayer's "start simple, add config only on failure": a large always-on hook/daemon/MCP surface. Treat as a source of ideas (cost cockpit, control levels with ask/auto, federation) not as something to install: it would add hooks, daemon and 300+ tools to a box that already runs a lean manager, and the manager-setup research already found ambient plugin context to be the biggest waste.
## Quotable
> "Mods run with your account's permissions; review their code before installing."

## Used by
[[topic-claude-code-features]], [[topic-multi-agent-frameworks]]
