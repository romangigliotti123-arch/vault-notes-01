---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2608.11434
type: paper
author: Wang, Gu, Chi, Liu et al.
published: 2026-08-11
accessed: 2026-10-29
reliability: med (931 human-annotated trajectories; abstract read)
---
# Benchmarking LLM Judges for Mobile Agent Evaluation (MobileJudgeBench)
## Key claims
- 931 human-annotated trajectories, 6 mobile agent benchmarks, 4 agent models, 68 apps; 6 judge methods compared.
- A simple baseline judge with sampled screenshots is competitive with, and often exceeds, purpose-built judge pipelines: "more elaborate judge pipelines do not consistently improve judge quality"; the LLM backbone is the primary driver.
- Failure profiles differ by backbone: one conservative, one permissive (precision-recall characteristics). Know your judge model tendency.
## Quotable
> "more elaborate judge pipelines do not consistently improve judge quality"

## Used by
[[topic-llm-judge-and-adversarial-verification]]
