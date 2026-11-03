---
tags: [manager-kb, source]
url: https://raw.githubusercontent.com/tobi/qmd/main/README.md
type: repo
author: Tobi Lutke (tobi/qmd)
published: undated (v2.x, 2026)
accessed: 2026-10-29
reliability: med-high: primary README, own fixture benchmark
---
# qmd: on-device hybrid search for markdown (README)
## Key claims
- Local hybrid search over markdown: SQLite FTS5 BM25 + vector (embeddinggemma-300M Q8, ~300MB) + LLM rerank (qwen3-reranker-0.6b, ~640MB) + query expansion model (1.7B, ~1.1GB); runs through node-llama-cpp/GGUF, no API keys.
- Fusion: Reciprocal Rank Fusion k=60, original query weighted x2, top-ranked bonus; rerank top 30 and blend by rank (75/25 for ranks 1-3, 60/40 for 4-10, 40/60 for 11+). Typed sub-queries lex / vec / hyde.
- Chunking: ~900 tokens with 15% overlap, split on scored markdown break points (headings 100..50, code fences 80); markdown uses regex chunking.
- MCP tools: query, get, multi_get, status, metadata. Commands: search (BM25), vsearch, query (hybrid, "best quality").
- Own fixture quality: BM25 ~0.50, vector ~0.70, hybrid/full ~1.00 (tiny fixture, not independent). No latency or RAM numbers published. Directly usable over the Obsidian vault and the library.
## Quotable
> (paraphrase; README figures only)

## Used by
[[topic-knowledge-management-rag]], [[topic-skill-library-retrieval]]
