---
tags: [manager-kb, source]
url: https://ghuntley.com/ralph/
type: practitioner-blog
author: Geoffrey Huntley
published: 2025 (undated in fetch)
accessed: 2026-10-29
reliability: med (single practitioner, anecdotal cost claims)
---
# Ralph Wiggum as a "software engineer" (Ralph loop)
## Key claims
- Simplest form: `while :; do cat PROMPT.md | claude-code ; done`.
- Fresh context window every iteration; state lives in files: `specs/`, `fix_plan.md` (implementation plan), `PROMPT.md`, `AGENT.md` (build/run notes).
- One task per loop, chosen as the most important item in the plan; backpressure from tests/builds/type checkers; commit only when they pass.
- Claimed: a contract that "would have cost $50k" delivered for ~$297 (anecdote). Best for greenfield; pitfalls: non-determinism, duplicate implementations, placeholder code, broken builds, constant prompt tuning.
- Related page https://ghuntley.com/loop/ (opened) says loops need watching: "It's important to watch the loop"; warns against multi-agent complexity.
## Quotable
> `while :; do cat PROMPT.md | claude-code ; done`

## Used by
[[topic-context-window-management]], [[topic-long-running-always-on-agents]], [[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
