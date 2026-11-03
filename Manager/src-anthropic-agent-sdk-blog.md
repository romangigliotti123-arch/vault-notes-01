---
tags: [manager-kb, source]
url: https://claude.com/blog/building-agents-with-the-claude-agent-sdk
type: eng-blog
author: Thariq Shihipar (+ editors)
published: 2025-09-29
accessed: 2026-10-29
reliability: high (primary; moved from anthropic.com/engineering via 308 redirect)
---
# Building agents with the Claude Agent SDK
## Key claims
- SDK = general-purpose agent harness; principle: give the agent a computer. Loop: gather context -> take action -> verify work -> repeat.
- Gather: agentic search / filesystem layout is context engineering; start with agentic search (grep/tail) over semantic search (faster but less accurate, harder to maintain, less transparent); subagents for parallelism and context isolation (return only relevant results to the orchestrator); compaction.
- Act: tools (context-efficiency matters), bash/scripts, code generation for precise reusable operations, MCP for integrations.
- Verify: defined rules (lint, validation) are "the best form of feedback"; visual feedback (screenshots/Playwright); LLM-as-judge for fuzzy criteria (less robust, adds latency and cost).
- Improve: read failures, ask whether the agent has the right tools/info, add rules, build evals from real usage.
## Quotable
> "Agents that can check and improve their own output are fundamentally more reliable"
> "The best way to improve an agent is to look carefully at its output, especially the cases where it fails"

## Used by
[[topic-anthropic-agent-guidance]], [[topic-context-engineering]]
