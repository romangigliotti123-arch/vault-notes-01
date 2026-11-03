---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2305.18323
type: paper
author: Xu et al.
published: 2023-05-23
accessed: 2026-10-29
reliability: med (abstract opened; 2023 models; token claim from the authors)
---
# ReWOO: Decoupling Reasoning from Observations for Efficient Augmented Language Models
## Key claims
- Separates planning from tool observation: the LLM plans the whole tool-call chain up front (with placeholders for earlier results), workers execute, a solver composes the answer. Avoids re-sending the growing observation history on every step.
- "ReWOO achieves 5x token efficiency and 4% accuracy improvement on HotpotQA"; robust under tool-failure scenarios; planning ability can be distilled from 175B GPT-3.5 into a 7B LLaMA.
- Six public NLP benchmarks plus a curated dataset.
## Caveats (ours)
- 2023, GPT-3.5-era; frontier models with prompt caching and interleaved thinking changed the cost picture. Up-front plans are brittle when early observations change the plan (ReAct's strength); the LangChain post notes ReWOO is still sequential.

## Used by
[[topic-orchestration-patterns]]
