---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2311.17371
type: paper
author: Smit et al.
published: 2023-11-29
accessed: 2026-10-29
reliability: med (abstract opened; 2023 models)
---
# Should we be going MAD? A look at multi-agent debate strategies for LLMs
## Key claims
- Benchmarks debate protocols against self-consistency, ensembling and other prompting strategies on cost, time and accuracy: "multi-agent debating systems, in their current form, do not reliably outperform other proposed prompting strategies, such as self-consistency and ensembling using multiple reasoning paths."
- With hyperparameter tuning some protocols (e.g. Multi-Persona) do better: MAD is "more sensitive to different hyperparameter settings and difficult to optimize"; adjusting agent agreement levels helped and could beat all non-debate protocols.
- Companion evidence: [[src-stop-overvaluing-mad]] (5 MAD methods, 9 benchmarks, 4 models: MAD often fails to beat CoT / self-consistency despite more compute; heterogeneous models help). Original positive result: [[src-du-multiagent-debate]].

## Used by
[[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
