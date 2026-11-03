---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2310.12963
type: paper
author: Aggarwal et al.
published: 2023-10-19
accessed: 2026-10-29
reliability: high (abstract read via arXiv API)
---
# AutoMix: Automatically Mixing Language Models
## Key claims
- A small model answers first and **self-verifies** (few-shot); a POMDP router escalates to a larger model when confidence is low. "reducing computational cost by over 50% for comparable performance" over five models and five datasets.
- Self-verification is noisy, so the router is built to cope with it. Lesson (my reading): "cheap worker first, escalate on a weak report" only works if the report carries checkable evidence (the VERIFIED field), not a bare "success".
## Quotable
> "reducing computational cost by over 50% for comparable performance"

## Used by
[[topic-model-effort-routing-cost]]
