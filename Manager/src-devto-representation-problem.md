---
tags: [manager-kb, source]
url: https://dev.to/chen115y/the-representation-problem-why-rag-vs-agentic-search-is-the-wrong-debate-4j8f
type: practitioner-blog
author: Yaohua Chen
published: May (year not shown on page)
accessed: 2026-10-29
reliability: low-med: opinion essay
---
# The Representation Problem: RAG vs agentic search is the wrong debate
## Key claims
- Thesis: pick retrieval by data structure; "similarity does not equal relevance".
- Agentic search burns more tokens and time; fine for coding agents (users accept multi-second), poor for high-throughput serving of thousands of queries per second.
- Vector RAG fits "unstructured text corpora with relatively stable content and straightforward information needs" (support wikis, FAQ).
- Structural questions (call chains, change impact) need graph structure; vector similarity cannot answer them.
- Indexes go stale; fill the gap by agentic search on recently changed files (hybrid).
## Quotable
> "similarity does not equal relevance"

## Used by
[[topic-knowledge-management-rag]]
