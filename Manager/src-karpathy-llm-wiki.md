---
tags: [manager-kb, source]
url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
type: practitioner-blog
author: Andrej Karpathy
published: 2026-04-04
accessed: 2026-10-29
reliability: med: influential idea, not benchmarked
---
# LLM Wiki (gist llm-wiki.md)
## Key claims
- Three layers: raw sources (curated, LLM reads never edits); the wiki (LLM-written markdown pages: summaries, entities, concepts; 'The LLM owns this layer entirely'); the schema (CLAUDE.md/AGENTS.md defining structure and workflows).
- Two navigation files: index.md (content catalogue) and log.md (append-only chronological record).
- Operations: ingest (one source can touch 10-15 wiki pages, updates index and log), query (search wiki, cited answer, good answers filed back as new pages), lint (periodic health-check for contradictions, stale claims, orphan pages, missing cross-references).
- Core claim: the wiki is a persistent compounding artifact, instead of re-deriving from raw documents on every query.
- Fetch note: page text is 144k chars (mostly comments, promotional); only first 100k read.
## Quotable
> "the wiki is a persistent, compounding artifact."

## Used by
[[topic-knowledge-management-rag]]
