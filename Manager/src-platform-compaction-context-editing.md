---
tags: [manager-kb, source]
url: https://platform.claude.com/docs/en/build-with-claude/context-editing (+ /compaction overview)
type: official-doc
author: Anthropic (Claude Developer Platform docs)
published: undated (context editing beta header context-management-2025-06-27; on-demand compaction beta header compact-2026-09-04)
accessed: 2026-10-29
reliability: high (official; last ~7k chars of context-editing page unread)
---
# Server-side compaction and context editing
## Key claims
- Compaction replaces older turns with a summary Claude writes on the server. Three modes: on-demand (you decide when; can keep recent turns word-for-word; can run in background), at a token threshold (API decides), or your own client summariser. "Use on-demand compaction wherever it is available." Custom summarisation prompt replaces the default when the default drops something a later turn needs.
- Context editing (finer control): `clear_tool_uses_20250919` clears oldest tool results first once trigger hit (default 100,000 input tokens), `keep` last 3 tool uses, `clear_at_least`, `exclude_tools`, optional `clear_tool_inputs`; cleared results become placeholder text. `clear_thinking_20251015` manages thinking blocks (list first when combined).
- Cache cost: clearing tool results invalidates the cached prefix, so "clear enough tokens to make the cache invalidation worthwhile" (`clear_at_least`).
- Memory tool integration: before clearing threshold Claude "receives an automatic warning to preserve important information".
- Client-side SDK compaction (TS/Ruby tool_runner) deprecated in favour of server-side; Python SDK removed it in v1.0.
- Docs recommend server-side compaction for most long-running conversations; context editing for finer control.
## Quotable
> "To account for this, clear enough tokens to make the cache invalidation worthwhile."

## Used by
[[topic-context-engineering]]
