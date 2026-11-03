---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2305.05176
type: paper
author: Chen, Zaharia, Zou (Stanford)
published: 2023-05-09
accessed: 2026-10-29
reliability: high (abstract read via arXiv API; full text not opened)
---
# FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance
## Key claims
- Three strategies: prompt adaptation, LLM approximation, **LLM cascade** (try the cheap model first, escalate based on a learned scorer).
- "FrugalGPT can match the performance of the best individual LLM (e.g. GPT-4) with up to 98% cost reduction or improve the accuracy over GPT-4 by 4% with the same cost."
- API fees differed by two orders of magnitude at the time.
- Caveat (my reading): 2023 classification/QA tasks with a trained scorer; cascades need a reliable "is this answer good" signal.
## Quotable
> "up to 98% cost reduction or improve the accuracy over GPT-4 by 4% with the same cost"

## Used by
[[topic-model-effort-routing-cost]]
