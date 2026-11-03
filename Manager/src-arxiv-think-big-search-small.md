---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2607.07548
type: paper
author: (authors not extracted)
published: 2026-07-08
accessed: 2026-10-29
reliability: med (abstract opened only; small-model QA search agents, not coding; single study)
---
# Think Big, Search Small: Where Capacity Matters in Hierarchical Search Agents?
## Key claims
- Factorises a hierarchical search agent into a delegation role (task decomposition), an execution role (retrieval/evidence extraction) and a fixed answer role; runs controlled capacity sweeps on five multi-hop QA benchmarks.
- Role factorisation beats a single-agent baseline by 4.5 to 8.6 exact-match points across six model scales.
- **Asymmetric sensitivity**: scaling the delegation backbone improves EM by ~11 points; scaling the execution sub-agent moves EM by only ~2.6. "identifying decomposition as the capability bottleneck." Recipe: "concentrate capacity at delegation and downsize execution without sacrificing accuracy." A 1.7B distilled executor matched a frontier sub-agent with 37% fewer sub-agent tokens.
- Direct relevance to us: our manager runs on Haiku while workers are Sonnet/Opus - the inverse of this recipe. Caveat: the manager here does routing/briefing, not search decomposition from scratch; but briefs ARE the decomposition.

## Used by
[[topic-orchestration-patterns]]
