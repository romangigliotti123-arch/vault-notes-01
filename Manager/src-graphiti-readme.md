---
tags: [manager-kb, source]
url: https://raw.githubusercontent.com/getzep/graphiti/main/README.md
type: repo
author: Zep (getzep)
published: undated
accessed: 2026-10-29
reliability: med: vendor README, latency claims lack method
---
# Graphiti README (temporal context graphs)
## Key claims
- Open-source framework for temporal context graphs: entities (nodes), facts (edges), episodes (raw source). Facts have validity windows; old facts are invalidated, not deleted.
- Retrieval combines semantic embeddings, BM25 and graph traversal, aiming to avoid LLM summarisation at query time.
- Vs GraphRAG: GraphRAG = static corpus, batch; Graphiti = continuous incremental updates, bi-temporal tracking, custom Pydantic entity types.
- Latency claims ("sub-second" vs GraphRAG "seconds to tens of seconds") are table entries without methodology.
- You must supply the graph DB, LLM and embedder; it is a framework, not a memory product.
## Quotable
> "old facts are invalidated - not deleted"

## Used by
[[topic-knowledge-management-rag]]
