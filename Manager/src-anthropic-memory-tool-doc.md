---
tags: [manager-kb, source]
url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
type: official-doc
author: Anthropic
published: undated
accessed: 2026-10-29
reliability: high: official API doc
---
# Memory tool (platform docs)
## Key claims
- Client-side /memories directory with view, create, str_replace, insert, delete, rename; auto-added system prompt: view the memory directory first, "ASSUME INTERRUPTION" so record progress as you go.
- Recommended hygiene line: "always try to keep its content up-to-date, coherent and organized. You can rename or delete files that are no longer relevant. Do not create new files unless necessary."
- Security: validate paths (traversal), cap file sizes, "periodically delete memory files that haven't been accessed in a long time", strip sensitive data before writing.
- Multisession pattern: initializer session creates progress log + feature checklist; each session reads them first and updates at end; mark done only after end-to-end verification.
- Pairs with compaction (summarise) and context editing; memory holds what must survive summarisation.
## Quotable
> "Your application runs every file operation Claude requests"

## Used by
[[topic-knowledge-management-rag]]
