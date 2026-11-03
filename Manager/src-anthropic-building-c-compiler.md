---
tags: [manager-kb, source]
url: https://www.anthropic.com/engineering/building-c-compiler
type: eng-blog
author: Nicholas Carlini (Anthropic Safeguards)
published: 2026-02-05
accessed: 2026-10-29
reliability: high (primary; extreme-scale API-billed case study)
---
# Building a C compiler with a team of parallel Claudes
## Key claims
- Setup: bash loop re-launching Claude Code with a prompt file in containers; 16 agents, each in its own Docker container, shared bare git repo; tasks claimed by writing a lock file in `current_tasks/` (git sync prevents double claims); NO orchestrator, no inter-agent chat; each agent picks the "next most obvious" task. Specialised roles emerged: dedupe, performance, codegen, design critique, docs.
- Scale: ~2,000 sessions, ~2 weeks, ~2B input / 140M output tokens, just under $20,000 API cost; ~100k-line Rust compiler that builds Linux 6.9 on x86/ARM/RISC-V, ~99% pass on most suites.
- Lessons for autonomous-agent test design: "the task verifier is nearly perfect, otherwise Claude will solve the wrong problem"; add CI so new commits cannot break old code; keep test output small ("should not print thousands of useless bytes"), log details to files, tag errors for grep, precompute summaries (context pollution); "Claude can't tell time" -> `--fast` deterministic sample mode; when the task is one monolith (Linux kernel) all agents hit the same bug -> use a known-good oracle (GCC) to split work.
- Limits: Claude "cheats" (calls GCC for 16-bit real-mode phase); no own assembler/linker; inefficient output; new features often broke old ones.
## Quotable
> "With agent teams, multiple Claude instances work in parallel on a shared codebase without active human intervention."
> "Claude can't tell time and, left alone, will happily spend hours running tests instead of making progress."

## Used by
[[topic-anthropic-agent-guidance]], [[topic-context-engineering]], [[topic-llm-judge-and-adversarial-verification]], [[topic-long-running-always-on-agents]], [[topic-multi-agent-failure-modes]], [[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
