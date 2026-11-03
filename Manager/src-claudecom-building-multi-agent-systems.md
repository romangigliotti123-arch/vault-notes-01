---
tags: [manager-kb, source]
url: https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them
type: eng-blog
author: Cara Phillips (+ Paul Chen, Andy Schumeister, Brad Abrams, Theo Chu)
published: 2026-01-23
accessed: 2026-10-29
reliability: high (official; cost numbers are approximate)
---
# Building multi-agent systems: when and how to use them
## Key claims
- Multi-agent consistently beats single agent in three situations only: context protection (clean isolated contexts), parallelization (benefit is "thoroughness rather than speed"), specialization (conflicting tool sets/prompts).
- Single agent first: teams that spent months on elaborate multi-agent designs found better prompting of one agent matched their results. "Start with the simplest approach that works, and add complexity only when evidence supports it."
- Cost: "multi-agent implementations typically use 3-10x more tokens than single-agent approaches for equivalent tasks"; wall-clock often still longer than one agent.
- Decompose by context boundary, not by work type: splitting planning/implementation/testing creates a "telephone game"; "an agent handling a feature should also handle its tests."
- Verification subagents: "The most significant failure mode for verification subagents is marking outputs as passing without thorough testing"; mitigate with concrete criteria, negative tests, explicit instruction to run comprehensive checks - "Without explicit requirements for comprehensive validation, verification agents take shortcuts."
- Before adding agents for many tools, consider Tool Search or compaction.
## Quotable
> "Start with the simplest approach that works, and add complexity only when evidence supports it."
> "The most significant failure mode for verification subagents is marking outputs as passing without thorough testing."

## Used by
[[topic-anthropic-agent-guidance]], [[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
