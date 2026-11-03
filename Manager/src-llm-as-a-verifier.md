---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2607.05391
type: paper
author: Kwok, Li, Atreya, Liu et al.
published: 2026-07-06
accessed: 2026-10-29
reliability: med (abstract read; needs logit access)
---
# LLM-as-a-Verifier: A General-Purpose Verification Framework
## Key claims
- Treats verification as a scaling axis: scoring by the expectation over scoring-token logits gives continuous scores; more score granularity, repeated evaluation and criteria decomposition each improve verification accuracy (variance and complexity reduction).
- Reported results include 86.5% Terminal-Bench V2 and 78.2% SWE-Bench Verified for the verifier-selected solutions (abstract).
- Not directly usable in Claude Code (no logit access), but supports two practical points: decompose criteria and repeat evaluation instead of one holistic judgement.
## Quotable
> (none)

## Used by
[[topic-llm-judge-and-adversarial-verification]]
