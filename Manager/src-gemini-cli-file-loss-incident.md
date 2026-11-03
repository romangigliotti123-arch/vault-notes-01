---
tags: [manager-kb, source]
url: https://incidentdatabase.ai/entities/gemini-cli/
type: news
author: AI Incident Database + press (search snippets only)
published: 2025-07
accessed: 2026-10-29
reliability: low-med (snippet only; Ars Technica fetch blocked)
---
# Gemini CLI file-loss incident (July 2025)
## Key claims
- SNIPPET ONLY. GitHub issue by user anuraag2601 (Jul 21 2025): Gemini CLI 0.1.13 on Windows without sandbox lost files while reorganising a folder. Reports say the mkdir step failed silently, and later move commands ran as if the folder existed, overwriting files. The agent output said "I have failed you completely and catastrophically."
- Disputed scope; no Google postmortem found. Pattern: a failed precondition was not checked before dependent destructive steps (silent partial failure, non-idempotent action).
## Quotable
> (none; snippet only)
## Note
Do not cite details beyond the pattern without opening a primary source.

## Used by
[[topic-multi-agent-failure-modes]]
