---
tags: [manager-kb, source]
url: https://openclawdc.com/blog/do-claude-code-subagents-burn-your-limit/
type: practitioner-blog
author: OpenClaw DC (guide)
published: 2026-08-19
accessed: 2026-10-29
reliability: low (no original measurements; restates Anthropic docs; read via WebFetch summary)
---
# Do Claude Code subagents burn your limit?
## Key claims
- "Parallel agents buy you wall-clock time. They do not buy you tokens." "A subagent is cheaper than the main thread only when the work generates far more intermediate output than final answer."
- Agent teams ~7x tokens in plan mode (attributed to the Anthropic costs page, confirmed in [[src-ccdocs-costs]]).
- "Anthropic does not publish how plan limits convert token usage into your 5-hour and weekly allowance"; whether cache reads count toward plan limits is not stated. Recommends testing `CLAUDE_CODE_SUBAGENT_MODEL=haiku`, explicit `model:` per agent, narrowing tools, avoiding forks for small tasks, `/usage` subagent share.
- Takeaway: the open question "do cache reads count at full rate against subscription limits" is unresolved in public sources; conflicting community reports exist (snippet-only: a March-2026 report of cache reads consuming ~99.9% of a quota; a later telemetry analysis fitting cache_read ~0x).

## Used by
[[topic-model-effort-routing-cost]]
