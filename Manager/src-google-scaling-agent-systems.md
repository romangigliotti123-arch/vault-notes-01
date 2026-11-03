---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2512.08296
type: paper
author: Kim, Gu, Park, Park et al. (20 authors)
published: 2025-12-09
accessed: 2026-10-29
reliability: high (260 configs, controlled)
---
# Towards a Science of Scaling Agent Systems
## Key claims
- 260 configurations across 6 benchmarks, 5 architectures (single agent; independent, centralized, decentralized, hybrid multi-agent), 3 LLM families, standardised tools/prompts/compute.
- Capability ceiling: tasks where the single-agent baseline already exceeds about 45% accuracy see negative returns from adding agents (beta -0.236, p=0.004).
- Error amplification: independent agents amplify trace-level errors 17.2x; centralized coordination with validation bottlenecks contains it to 4.4x. "architectures without centralized verification tend to propagate errors more".
- Tool-heavy tasks incur a multi-agent coordination tax; relative change vs single agent ranges from +80.8% (decomposable financial reasoning) to -70.0% (sequential planning). The framework picks the best architecture for 87% of held-out configs.
## Quotable
> "architectures without centralized verification tend to propagate errors more than those with centralized coordination"

## Used by
[[topic-llm-judge-and-adversarial-verification]], [[topic-multi-agent-failure-modes]], [[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
