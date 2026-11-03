---
tags: [manager-kb, source]
url: https://claude.com/blog/multi-agent-coordination-patterns
type: eng-blog
author: Cara Phillips (+ Eugene Yan, Jiri De Jonghe, Samuel Weller, Erik S.)
published: 2026-04-10
accessed: 2026-10-29
reliability: high (official Anthropic guidance; no quantitative data)
---
# Multi-agent coordination patterns: five approaches and when to use them
## Key claims
- Five patterns: (1) generator-verifier, (2) orchestrator-subagent (Claude Code uses this), (3) agent teams (persistent workers claiming from a shared queue), (4) message bus (event pub/sub), (5) shared state (no coordinator, shared store).
- Default: "For most use cases, we recommend starting with orchestrator-subagent"; "start with the simplest pattern that could work, watching where it struggles, and evolving from there"; production systems often combine patterns.
- Generator-verifier limits: "The verifier is only as good as its criteria"; a vague-criteria verifier approves nearly everything; assumes generation and evaluation are separable; loops stall -> cap + fallback (human escalation).
- Orchestrator-subagent limits: "The orchestrator becomes an information bottleneck"; details lost across handoffs; without parallel running you pay multi-agent token cost without speed gain.
- Agent teams: "Independence is the critical requirement"; teammates can't easily share findings; conflicting edits on shared resources; use when workers need sustained context across steps ("When subagents need to retain state across invocations, agent teams are the better fit").
- Message bus: silent failure ("the system fails silently, handling nothing but never crashing"); tracing hard. Shared state: duplicated/contradictory work, reactive loops need explicit termination (time budget, convergence threshold, designated decider).
## Quotable
> "We recommend starting with the simplest pattern that could work, watching where it struggles, and evolving from there."
> "The verifier is only as good as its criteria."

## Used by
[[topic-anthropic-agent-guidance]], [[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
