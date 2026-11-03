---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/costs
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (page mentions v2.1.305)
accessed: 2026-11-01
reliability: high (official; full page read). Supplements src-ccdocs-costs.
---
# Manage costs: 2026 additions
## Key claims
- Enterprise average about $13 per developer per active day, $150-250 per month, under $30 per active day for 90% of users (API-billed context; we are on a subscription).
- `/usage` on subscriptions attributes recent usage to skills, subagents, plugins and individual MCP servers as a % of total, lists recommendations (rows covering >=10% of usage) and a Loops table for heavy `/loop` tasks; `f` applies fixable rows (not while Remote Control is connected).
- The Session block shows a prompt-cache line (requests, % input from cache, misses with likely cause, expected rebuilds after compaction, warm/cold with TTL); main conversation only, NOT subagents.
- Agent teams use "approximately 7x more tokens than standard sessions" when teammates run in plan mode; use Sonnet for teammates, keep teams small, shut teammates down when done (each active teammate keeps consuming).
- Why a long session burns limits: full history re-sent each request; cache misses after idle gaps; session-scoped scheduled tasks, cross-session messages, goal check-ins (max 3 idle per goal) and subagents/workflows each add full-context requests while idle.
- Thinking cannot be disabled on Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable models: use effort. Keep CLAUDE.md under about 200 lines, move workflow detail into skills; delegate verbose output (tests, logs) to subagents and choose a smaller subagent model; `autoContinueAtUsageLimit` waits and continues after a usage-limit reset.
## Used by
[[topic-model-effort-routing-cost]], [[topic-context-window-management]], [[topic-observability]]
