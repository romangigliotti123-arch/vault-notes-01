---
tags: [manager-kb, source]
url: https://www.anthropic.com/engineering/writing-tools-for-agents
type: eng-blog
author: Ken Aizawa (+ Anthropic teams)
published: 2025-09-11
accessed: 2026-10-29
reliability: high (primary)
---
# Writing effective tools for AI agents
## Key claims
- Tools are "a contract between deterministic systems and non-deterministic agents"; design for agents, not developers.
- Process: prototype (local MCP server), evaluate with dozens of realistic tasks each with a verifiable outcome (track accuracy, runtime, tool calls, tokens, errors), then paste transcripts into Claude Code to refactor tools; use a held-out test set.
- Principles: few targeted high-impact tools, not API wrappers (e.g. one schedule_event); namespace tools by prefix; return meaningful context (names over ids; response_format concise vs detailed: 72 vs 206 tokens); token efficiency (pagination, filters, truncation; Claude Code caps tool responses at 25,000 tokens); error messages that tell the agent how to fix the call; descriptions written like for a new hire; small description refinements gave big gains (SWE-bench SOTA for Sonnet 3.5).
## Quotable
> "More tools don't always lead to better outcomes."
> "Even small refinements to tool descriptions can yield dramatic improvements."

## Used by
[[topic-agent-security]], [[topic-anthropic-agent-guidance]], [[topic-context-engineering]], [[topic-knowledge-management-rag]], [[topic-skill-library-retrieval]], [[topic-tool-and-mcp-design]]
