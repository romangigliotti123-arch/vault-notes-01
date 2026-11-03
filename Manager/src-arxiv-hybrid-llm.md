---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2404.14618
type: paper
author: Ding et al. (Microsoft)
published: 2024-04-22
accessed: 2026-10-29
reliability: high (abstract read via arXiv API)
---
# Hybrid LLM: Cost-Efficient and Quality-Aware Query Routing
## Key claims
- A router predicts query difficulty and sends the query to the small or the large model; the quality threshold is tunable at test time. "up to 40% fewer calls to the large model, with no drop in response quality."
- Difficulty prediction is the crux; savings depend on how many queries are easy.
## Quotable
> "up to 40% fewer calls to the large model, with no drop in response quality"

## Used by
[[topic-model-effort-routing-cost]]
