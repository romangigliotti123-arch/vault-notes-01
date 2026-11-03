---
tags: [manager-kb, source]
url: https://officechai.com/ai/claude-researcher-explains-how-agentic-search-performed-better-than-rag-for-code-generation/
type: practitioner-blog
author: OfficeChai quoting Boris Cherny (Anthropic)
published: 2025-05-27
accessed: 2026-10-29
reliability: med: secondary report of a talk, verbatim lines
---
# Cherny on why Claude Code uses agentic search not RAG
## Key claims
- Early Claude Code used RAG with a local vector DB, then "landed on just agentic search".
- Reasons: it "outperformed everything else by a lot"; code "drifts out of sync" with an index; agent search sidesteps security, privacy and staleness problems.
- Evidence base is weak by his own account: "There are some internal benchmarks also, but mostly vibes."
- Named trade-off: costs latency and tokens ("trading time for intelligence").
- Original video youtube.com/watch?v=zDmW5hJPsvQ was not opened.
## Quotable
> "Eventually, we landed on just agentic search as the way to do things."

## Used by
[[topic-knowledge-management-rag]]
