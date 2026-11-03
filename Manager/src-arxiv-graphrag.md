---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2404.16130
type: paper
author: Edge et al. (Microsoft)
published: 2024-04-24
accessed: 2026-10-29
reliability: high: primary, clear scope
---
# From Local to Global: A Graph RAG Approach to Query-Focused Summarization
## Key claims
- Targets GLOBAL sensemaking questions over a whole corpus, which plain RAG handles badly.
- LLM builds an entity knowledge graph, then pregenerates community summaries; at query time each community gives a partial answer, then reduce to a final answer.
- Beats conventional RAG on comprehensiveness and diversity at roughly 1M-token corpora; index build is LLM-expensive (every document processed).
## Quotable
> "What are the main themes in the dataset?" (example global question)

## Used by
[[topic-knowledge-management-rag]]
