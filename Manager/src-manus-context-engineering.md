---
tags: [manager-kb, source]
url: https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus
type: eng-blog
author: Yichao "Peak" Ji (Manus)
published: 2025-07 (date not shown on fetched page; widely cited as July 2025)
accessed: 2026-10-29
reliability: high (first-party, practitioner; no benchmarks)
---
# Context Engineering for AI Agents: Lessons from Building Manus
## Key claims
- Manus rebuilt its agent framework four times ("Stochastic Graduate Descent"); chose context engineering over training: "ship improvements in hours instead of weeks".
- KV-cache hit rate is "the single most important metric for a production-stage AI agent"; average input:output token ratio ~100:1; cached Sonnet tokens $0.30/MTok vs $3/MTok uncached. Keep prompt prefix stable (no second-precision timestamp at the start), append-only context, deterministic serialisation.
- "Mask, don't remove": do not add/remove tools mid-iteration (invalidates cache, confuses model); constrain via logit masking and consistent tool name prefixes (browser_, shell_).
- File system as context: restorable compression (keep URL/path, drop content); "any irreversible compression carries risk".
- Recitation: ~50 tool calls per task on average; the agent rewrites a todo.md to push the goal into recent attention.
- "Keep the wrong stuff in": leave failed actions and stack traces in context; "error recovery is one of the clearest indicators of true agentic behavior".
- "Don't get few-shotted": uniform repeated action patterns make the agent brittle; add structured variation.
## Quotable
> KV-cache hit rate is the single most important metric for a production-stage AI agent.
> leave the wrong turns in the context.

## Used by
[[topic-anthropic-agent-guidance]], [[topic-brief-prompt-engineering]], [[topic-context-engineering]], [[topic-context-window-management]], [[topic-long-running-always-on-agents]], [[topic-observability]], [[topic-personal-assistant-agents]]
