---
tags: [manager-kb, source]
url: https://langfuse.com/integrations/other/claude-code
type: official-doc
author: Langfuse
published: undated
accessed: 2026-10-29
reliability: high (vendor doc)
---
# Langfuse + Claude Code integration
## Key claims
- Uses the Claude Code **Stop hook** (runs after each response), reads the transcript and sends it to Langfuse; NOT Claude Code's OTel export. One trace per conversation turn ("Claude Code - Turn N"), generation span per assistant message, tool spans nested under it; sessions grouped by `session_id`; content truncated at 20,000 chars (`CC_LANGFUSE_MAX_CHARS`). Page does not mention subagents.
- Opt-in per project via `TRACE_TO_LANGFUSE` in `.claude/settings.json`. Plugin: `langfuse/Claude-Observability-Plugin`; needs Python 3.9+ and `langfuse>=4,<5`.
- Langfuse joined ClickHouse (announced 2026-01-16; vendor posts say stays MIT, self-hostable) - see [[src-langfuse-selfhost]].

## Used by
[[topic-observability]]
