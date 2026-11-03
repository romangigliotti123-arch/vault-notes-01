---
tags: [manager-kb, source]
url: https://www.anthropic.com/news/contextual-retrieval
type: eng-blog
author: Anthropic
published: 2024-09-19
accessed: 2026-10-29
reliability: high: primary, numbers measured
---
# Introducing Contextual Retrieval
## Key claims
- Chunks usually no more than a few hundred tokens; contextual retrieval prepends chunk-specific explanatory context (LLM-generated) to each chunk before embedding AND before building the BM25 index.
- Top-20-chunk retrieval failure rate: baseline 5.7%; Contextual Embeddings 3.7% (35% reduction); + Contextual BM25 2.9% (49%); + reranking 1.9% (67%).
- One-time cost to generate contextualized chunks with prompt caching: $1.02 per million document tokens (800-token chunks, 8k-token docs, 100 tokens of context per chunk).
- If knowledge base is under 200,000 tokens (about 500 pages) just put the whole thing in the prompt instead of RAG.
- Hybrid embeddings + BM25 recommended because BM25 catches exact identifiers/error codes embeddings miss.
## Quotable
> "the one-time cost to generate contextualized chunks is $1.02 per million document tokens"

## Used by
[[topic-context-engineering]], [[topic-knowledge-management-rag]], [[topic-skill-library-retrieval]]
