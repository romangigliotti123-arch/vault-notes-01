---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2212.10496
type: paper
author: Gao et al.
published: 2022-12-20
accessed: 2026-10-29
reliability: high: foundational
---
# HyDE: Precise Zero-Shot Dense Retrieval without Relevance Labels
## Key claims
- An LLM writes a hypothetical answer document for the query; its embedding retrieves real documents; false details are filtered by the encoder.
- Beats Contriever, comparable to fine-tuned retrievers across web search, QA, fact verification.
- Costs one LLM call per query and needs a capable instruction model.
## Quotable
> "unreal and may contain false details" (abstract wording on generated documents)

## Used by
[[topic-knowledge-management-rag]], [[topic-skill-library-retrieval]]
