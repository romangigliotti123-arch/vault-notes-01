---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2506.09033
type: paper
author: Zhang et al.
published: 2025-06-10
accessed: 2026-10-29
reliability: med-high (abstract read via arXiv API; QA benchmarks only)
---
# Router-R1: Multi-Round Routing and Aggregation via RL
## Key claims
- The router is itself an LLM that interleaves "think" and "route" actions across rounds, calling several models and integrating responses into its evolving context; reward = format + outcome + **cost reward**. It conditions only on simple model descriptors (pricing, latency, example performance), so it generalises to unseen models.
- Closest published analogue to our setup (an LLM manager choosing among models using price/latency descriptors), but trained with RL on seven QA benchmarks; no coding or ops agents.
- Lesson (my reading): give the manager an explicit descriptor table per worker (price, strengths, latency) in its prompt; that is what the paper conditions on.
## Quotable
> "instantiates the router itself as a capable LLM, leveraging its reasoning ability to interleave 'think' actions ... with 'route' actions"

## Used by
[[topic-model-effort-routing-cost]]
