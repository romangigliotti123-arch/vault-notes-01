---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2609.38822
type: paper
author: Yang, Zhang, Shi, Wang
published: 2026-09-30
accessed: 2026-10-29
reliability: med-high: AACL-IJCNLP 2026, single-trial noise noted
---
# SkillSeek: Revisiting Agent Skill Retrieval at Marketplace Scale
## Key claims
- Open skill collections exceed 230,000 entries. Plain BM25 matches or beats an LLM query-rewrite/refine loop in 3 of 4 settings; a small cross-encoder closes the 4th. Per-trial spend $51.30 -> $27.54.
- Recall@5 on a 192-skill pool: BM25 0.546, BGE-base 0.546, BGE+bge-reranker-v2-m3 0.581. On a 34K marketplace pool: BM25 0.391, BGE-base 0.379, +reranker 0.433, +structured "Tool-REX" indexing 0.478.
- Index name + description + a short structured profile; "appending the raw body adds noise" (pass rate -3.2% in ablation). bm25 baseline was rank_bm25, default tokenization, no stemming.
- Top-3 captures essentially all the gain over rank-1; hand 3-5 candidates to the agent. Reranker gains scale with how far stage-1 recall is from ceiling. Higher R@5 need not mean higher pass rate. Differences under ~2% are noise (single trial).
## Quotable
> "the standard IR recipe is a strong default for agent-skill retrieval"

## Used by
[[topic-knowledge-management-rag]], [[topic-skill-library-retrieval]]
