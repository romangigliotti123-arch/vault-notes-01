---
tags: [manager-kb, source]
url: https://www.anthropic.com/engineering/advanced-tool-use
type: eng-blog
author: Bin Wu (+ Claude Developer Platform team)
published: 2025-11-24
accessed: 2026-10-29
reliability: high (primary; internal evals)
---
# Introducing advanced tool use on the Claude Developer Platform
## Key claims
- Tool Search Tool: discover tools on demand (`defer_loading: true`); ~85% token reduction in the article's example; MCP eval accuracy Opus 4 49%->74%, Opus 4.5 79.5%->88.1%. Use when tool definitions >~10K tokens or 10+ tools; little value under 10 tools.
- Programmatic Tool Calling: Claude writes Python that calls tools in a sandbox so intermediate results stay out of context; 37% fewer tokens on complex research (43,588 -> 27,297). Use for large datasets, 3+ dependent calls, parallel ops.
- Tool Use Examples (`input_examples`, 1-5 per tool): complex-parameter accuracy 72% -> 90%.
- Principle: "Agents should discover and load tools on-demand, keeping only what's relevant for the current task."
## Quotable
> "Agents should discover and load tools on-demand, keeping only what's relevant for the current task."

## Used by
[[topic-agent-security]], [[topic-anthropic-agent-guidance]], [[topic-context-engineering]], [[topic-skill-library-retrieval]], [[topic-tool-and-mcp-design]]
