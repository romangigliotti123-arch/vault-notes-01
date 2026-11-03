---
tags: [manager-kb, source]
url: https://claude.com/blog/building-agents-when-to-fold-subagents-into-your-main-agent-loop
type: eng-blog
author: Diane Sarkis (Claude blog, best practices)
published: 2026-10-22
accessed: 2026-10-29
reliability: med-high (official blog, vendor-customer anecdotes, no public data)
---
# Building agents: When to fold subagents into your main agent loop
## Key claims
- Thesis: for many enterprise agents, a single main loop with progressively disclosed skills/tools can beat orchestrator + subagent designs on quality, cost and latency; one customer reported ~2x runtime speed.
- Subagents still make sense when: (1) a single loop shows measurable degradation from context bloat; (2) parallel tasks need fresh context windows that can be discarded; (3) a single agent struggles to choose tools or the system prompt holds conflicting instructions.
- Context-isolation trade-off: subagent results return as lossy summaries and each handoff degrades fidelity; a single loop keeps every step's result so the agent "can connect them", at the cost of growing context.
- Decision rules: merge specialists that chain on each other's output, touch the same data, or are called together; prefer calling a subagent as a tool over a full handoff; fold in one subagent at a time and compare evals with and without; check which tasks changed, not just the aggregate; run tasks more than once (intermittent failures); split by context needs, not by org chart.
- Overhead of many subagents: duplicated prompts, overlapping subagents, fragmented evals.
## Quotable
> "A single agent loop hits measurable performance degradation from context bloat"
> "passing information back and forth with each handoff degrading fidelity"

## Used by
[[topic-anthropic-agent-guidance]], [[topic-context-engineering]], [[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
