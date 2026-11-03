---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2404.06654
type: paper
author: Hsieh et al. (NVIDIA)
published: 2024-04-09
accessed: 2026-10-29
reliability: high (abstract read via arXiv API; 17 models of early 2024)
---
# RULER: What's the Real Context Size of Your Long-Context Language Models?
## Key claims
- Synthetic benchmark with multi-needle, multi-hop tracing and aggregation tasks at configurable lengths; 17 long-context models. "Despite achieving nearly perfect accuracy in the vanilla NIAH test, almost all models exhibit large performance drops as the context length increases. While these models all claim context sizes of 32K tokens or greater, only half of them can maintain satisfactory performance at the length of 32K."
- Reading for us: claimed window != effective window; tasks needing aggregation or tracing across the transcript (what did each worker report today?) degrade first. Offload aggregation to files/notes.
## Quotable
> "only half of them can maintain satisfactory performance at the length of 32K"

## Used by
[[topic-context-window-management]]
