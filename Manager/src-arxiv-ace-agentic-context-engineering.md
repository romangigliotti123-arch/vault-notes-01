---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2510.04618
type: paper
author: Zhang et al. (Stanford, SambaNova, Berkeley; Zou and Olukotun last authors)
published: 2025-10-06
accessed: 2026-10-29
reliability: med-high: ICLR 2026, abstract numbers only
---
# Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models (ACE)
## Key claims
- Treats context as an evolving playbook built by generation, reflection, curation; structured incremental (delta) updates to avoid losing detail.
- Names two failure modes of prior methods: brevity bias ("drops domain insights for concise summaries") and context collapse ("iterative rewriting erodes details over time").
- Gains over strong baselines: +10.6% on agent benchmarks, +8.6% on finance; matches the top production agent on the AppWorld leaderboard with a smaller open model. Works without labels using execution feedback.
- Search snippets (not verified in abstract): three roles Generator/Reflector/Curator, non-LLM merging of deltas, 86.9% lower adaptation latency.
- Direct design rule for a lessons log: append small dated deltas, never ask an LLM to rewrite the whole file.
## Quotable
> "iterative rewriting erodes details over time"

## Used by
[[topic-knowledge-management-rag]]
