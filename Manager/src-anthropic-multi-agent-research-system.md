---
tags: [manager-kb, source]
url: https://www.anthropic.com/engineering/multi-agent-research-system
type: eng-blog
author: Anthropic Engineering
published: 2025-06 (undated in fetch; models Opus 4 / Sonnet 4)
accessed: 2026-10-29
reliability: high (primary vendor, measured; but older models)
---
# How we built our multi-agent research system
## Key claims
- "agents typically use about 4x more tokens than chat interactions"; "multi-agent systems use about 15x more tokens than chats".
- BrowseComp: "three factors explained 95% of the performance variance"; "token usage by itself explains 80% of the variance" (others: number of tool calls, model choice).
- Lead Opus 4 + Sonnet 4 subagents "outperformed single-agent Claude Opus 4 by 90.2%" on internal research eval. Upgrading to a better model gave a bigger gain than doubling the token budget on the older model.
- Effort-scaling rules embedded in prompts: simple fact-finding = 1 agent, 3-10 tool calls; direct comparisons = 2-4 subagents, 10-15 calls each; complex research >10 subagents.
- Economics: "multi-agent systems require tasks where the value of the task is high enough" to pay for the extra tokens; poor fit where all agents share the same context or have many dependencies.
- Memory: lead agent saves its plan to external Memory because context beyond 200,000 tokens is truncated; can "spawn fresh subagents with clean contexts" and retrieve stored context.
- Rainbow deployments: cannot update all running agents at once.
## Quotable
> "multi-agent systems use about 15x more tokens than chats"
> "token usage by itself explains 80% of the variance"

## Used by
[[topic-anthropic-agent-guidance]], [[topic-brief-prompt-engineering]], [[topic-context-engineering]], [[topic-context-window-management]], [[topic-llm-judge-and-adversarial-verification]], [[topic-long-running-always-on-agents]], [[topic-model-effort-routing-cost]], [[topic-multi-agent-failure-modes]], [[topic-multi-agent-frameworks]], [[topic-observability]], [[topic-orchestration-patterns]], [[topic-report-formats-and-verification]]
