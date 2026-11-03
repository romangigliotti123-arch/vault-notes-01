---
tags: [manager-kb, source]
url: https://learn.microsoft.com/en-us/azure/search/hybrid-search-ranking
type: official-doc
author: Microsoft (Azure AI Search)
published: 2026-06-08 (page date)
accessed: 2026-10-29
reliability: high: vendor doc, standard algorithm
---
# Hybrid search scoring (Reciprocal Rank Fusion), Azure AI Search
## Key claims
- RRF merges ranked lists from parallel queries (BM25 + vector) by summing 1/(rank+k); k=60 "performs best" in their experiments. Needs no score normalisation across methods.
- Semantic (cross-encoder) ranking is applied AFTER RRF; its score is reported separately.
- Fields can be weighted (vector weighting multipliers) - used as precedent for per-field weights.
## Quotable
> "The score is calculated as 1/(rank + k), where rank is the position of the document in the list and k is a constant."

## Used by
[[topic-knowledge-management-rag]], [[topic-skill-library-retrieval]]
