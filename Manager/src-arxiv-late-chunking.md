---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2409.04701
type: paper
author: Gunther et al. (Jina)
published: 2024-09-07
accessed: 2026-10-29
reliability: med: only abstract read, no metrics
---
# Late Chunking: Contextual Chunk Embeddings Using Long-Context Embedding Models
## Key claims
- Embed the whole long text with a long-context model, then pool token embeddings per chunk after the transformer (before mean pooling) so each chunk vector carries document context. No extra training required.
- Alternative to Anthropic's LLM-written chunk context: cheaper (no LLM calls per chunk) but needs a long-context embedding model.
## Quotable
> (paraphrase only)

## Used by
[[topic-knowledge-management-rag]]
