---
tags: [manager-kb, source]
url: https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration
type: official-doc
author: Anthropic (Claude Managed Agents docs)
published: undated (beta; multiagent_20261001)
accessed: 2026-10-29
reliability: high (official; partial read of a 71 KB page)
---
# Managed Agents: Multiagent orchestration
## Key claims
- Three ways to hand off work: subagents (agent delegates and reads reports; each in a persistent, context-isolated "session thread" it can follow up with; one level deep, max 25 child threads), dynamic workflows (agent writes a program that runs many agents in the background; main thread stays free to talk to the user and check progress; cannot message the run's threads), and an advisor (primary thread consults a stronger model mid-turn for planning or final review while it does the work itself; billed at the advisor's rate; only the primary thread can consult).
- Patterns that "work well": parallelization, specialization (domain system prompts and tools instead of one agent with every capability), escalation (consult a more capable model for a subset of hard subtasks).
- The agent decides when to start a run; guide it in the system prompt: "When you're asked to review more than a few contracts, start a workflow run... Review one or two contracts yourself, without a run." Other prompt examples: one agent per item then a second agent that reviews EVERY item (not only those the first flagged) and redoes failures; "One agent failing must not fail the run... list that contract as not covered... tell me which weren't covered"; time limit; "Before you start a run, describe its phases and how many agents each one runs. Then wait for my go-ahead" (docs note: nothing enforces this, no approval step exists).
- "Keep runs to the tasks that need them, because every agent in a run uses tokens"; set a session budget to cap total spend.
- All agents share the same sandbox/filesystem/credentials but have separate conversation histories.
## Quotable
> "Keep runs to the tasks that need them, because every agent in a run uses tokens."

## Used by
[[topic-anthropic-agent-guidance]], [[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
