---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2407.21787
type: paper
author: Brown, Juravsky, Ehrlich, Clark et al.
published: 2024-07-31
accessed: 2026-10-29
reliability: high
---
# Large Language Monkeys: Scaling Inference Compute with Repeated Sampling
## Key claims
- Coverage (fraction solved by any sample) scales log-linearly over four orders of magnitude of samples; on SWE-bench Lite DeepSeek-Coder-V2 goes 15.9% (1 sample) -> 56% (250 samples) where verification is automatic (tests).
- Without automatic verifiers, majority voting and reward models plateau beyond several hundred samples: the verifier, not the generator, is the bottleneck.
## Quotable
> (none)

## Used by
[[topic-llm-judge-and-adversarial-verification]]
