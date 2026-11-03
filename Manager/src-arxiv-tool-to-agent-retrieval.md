---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2511.01854
type: paper
author: Lumer et al.
published: 2025-11-03
accessed: 2026-10-29
reliability: med: preprint, LiveMCPBench
---
# Tool-to-Agent Retrieval
## Key claims
- Problem: matching queries only to coarse agent-level descriptions hides what individual tools do.
- Fix: embed tools AND parent agents in one vector space linked by metadata, retrieve at either level.
- +19.4% Recall@5 and +17.7% nDCG@5 over prior agent retrievers across eight embedding models on LiveMCPBench.
- Directly relevant: our library mixes agents (coarse) and skills (fine); index both granularities and link them.
## Quotable
> (paraphrase only; abstract longer than quote limit)

## Used by
[[topic-skill-library-retrieval]]
