---
tags: [manager-kb, source]
url: https://docs.langchain.com/langsmith/trace-claude-code.md
type: official-doc
author: LangChain
published: undated
accessed: 2026-10-29
reliability: high (vendor doc)
---
# LangSmith: trace Claude Code
## Key claims
- Plugin `langsmith-tracing` (marketplace `langchain-ai/langsmith-claude-code-plugins`), hook-based, env `TRACE_TO_LANGSMITH=true`, `CC_LANGSMITH_API_KEY`, `CC_LANGSMITH_PROJECT`, `CC_LANGSMITH_METADATA`, `CC_LANGSMITH_REDACT` (redaction ON by default; "a safety net, not a guarantee").
- Captures user messages, tool calls, compaction, subagent runs, assistant responses; NOT system prompts. "Subagents are only traced upon completion" - an interrupted subagent's child runs are lost. Turns share a `thread_id`. Hook log at `~/.claude/state/hook.log`.
- Sends transcripts to a SaaS (privacy: Roman's chats; do not use without confirm-first).

## Used by
[[topic-observability]]
