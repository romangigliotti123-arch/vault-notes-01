---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2411.04468
type: paper
author: Microsoft Research (Fourney et al.)
published: 2024-11-07
accessed: 2026-10-29
reliability: med-high (full text HTML read for architecture and ablation; 2024 models GPT-4o/o1)
---
# Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks
## Key claims
- Lead Orchestrator directs four specialists (WebSurfer, FileSurfer, Coder, ComputerTerminal). Statistically competitive with the state of the art on GAIA (38.0-38.9% completion with GPT-4o; per-table figures), AssistantBench, WebArena "without modification to core agent capabilities".
- Two nested loops (full text read, arxiv.org/html/2411.04468). Outer loop keeps a **task ledger** (given facts, facts to look up, facts to derive, educated guesses, plus a natural-language plan that is "a hint ... neither the Orchestrator nor the other agents are required to follow it exactly"). Inner loop writes a **progress ledger** each step by answering five questions: is the request satisfied, is the team looping, is forward progress being made, which agent speaks next, what instruction to give. A **stall counter** increments on loops/no progress; at a threshold (2 in their runs) the Orchestrator exits to the outer loop, reflects on what went wrong, updates the ledger and re-plans. Terminates on completion or max attempts / max time; final step reviews the transcript and reports an answer or "best educated guess".
- Ablation (GAIA validation): replacing the Orchestrator with plain AutoGen GroupChat (who-speaks-next only; no ledgers, planning, progress tracking, loop detection) drops performance by **31%**; removing any one worker agent costs 21% (Coder/Executor) to 39% (FileSurfer). Agents sometimes compensated creatively for a missing capability.
- Modular: agents can be added/removed without re-tuning prompts. AutoGenBench provides repetition and isolation controls for benchmarking agents with side effects.
- Is the reference design for the "supervisor with a ledger" pattern; MAST counts Magentic-One among the 7 frameworks analysed. Magentic-UI (see [[src-magentic-ui-paper]]) is the human-in-the-loop follow-up.

## Used by
[[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
