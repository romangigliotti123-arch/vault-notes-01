---
tags: [manager-kb, source]
url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
type: official-doc
author: Anthropic (Claude Developer Platform docs)
published: undated (GA; tool type memory_20250818)
accessed: 2026-10-29
reliability: high (official)
---
# Memory tool
## Key claims
- Client-side directory `/memories` of files Claude can view/create/str_replace/insert/delete/rename; supports just-in-time retrieval: record what you learn, read back on demand, keep active context focused.
- Auto-injected protocol: "ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE... record status / progress / thoughts... ASSUME INTERRUPTION: Your context window might be reset at any moment, so you risk losing any progress that is not recorded."
- Housekeeping prompt: "keep its content up-to-date, coherent and organized. You can rename or delete files that are no longer relevant. Do not create new files unless necessary."
- Pair with compaction: "compaction keeps the active context small without client-side bookkeeping, and memory preserves the information that must survive summarization." Pair with context editing (clears specific tool results).
- Multisession pattern: initializer session creates progress log + feature checklist + startup script reference; each later session reads them first, works one feature at a time, marks complete only after end-to-end verification, updates log before ending.
- Security: path traversal validation, cap file size, expire stale memory, strip sensitive data.
## Quotable
> "Mark a feature complete only after end-to-end verification confirms it works, not when the code is written."

## Used by
[[topic-anthropic-agent-guidance]], [[topic-context-engineering]], [[topic-context-window-management]]
