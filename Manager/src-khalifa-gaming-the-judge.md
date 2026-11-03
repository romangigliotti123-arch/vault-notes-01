---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2601.14691
type: paper
author: Khalifa, Logeswaran, Kim, Sohn et al.
published: 2026-01-21
accessed: 2026-10-29
reliability: med-high (800 trajectories, controlled rewrite)
---
# Gaming the Judge: Unfaithful Chain-of-Thought Can Undermine Agent Evaluation
## Key claims
- Rewriting only an agent chain-of-thought (actions and observations held fixed) inflated false-positive rates of state-of-the-art VLM judges by up to 90% across 800 web-task trajectories.
- Content-based manipulations that fabricate signals of task progress are more effective than style changes. Prompting and more judge-time compute reduce but do not eliminate susceptibility.
- Conclusion: judges must verify reasoning claims against observable evidence, not trust narration.
## Quotable
> "highlight the need for judging mechanisms that verify reasoning claims against observable evidence"

## Used by
[[topic-llm-judge-and-adversarial-verification]], [[topic-multi-agent-failure-modes]]
