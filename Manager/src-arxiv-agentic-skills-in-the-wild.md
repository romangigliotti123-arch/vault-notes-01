---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2604.04323
type: paper
author: Liu et al. (MIT)
published: 2026-04-06
accessed: 2026-10-29
reliability: med-high: preprint, Terminal-Bench 2.0
---
# How Well Do Agentic Skills Work in the Wild: Benchmarking LLM Skill Usage in Realistic Settings
## Key claims
- Agents retrieve from a pool of 34k real skills (no hand-picked skills). Benefits of skills are "fragile": pass rates approach no-skill baselines in the hardest realistic scenarios.
- Query-specific refinement recovers much of the loss, but only when initial skills are reasonably relevant and decent quality. Terminal-Bench 2.0: retrieval + refinement lifted Claude Opus 4.6 from 57.7% to 65.5%.
- Implication for 5,600 imported skills: unvetted breadth gives little; relevance and quality of the few retrieved items dominate.
## Quotable
> (paraphrase only; abstract says benefits are "fragile")

## Used by
[[topic-skill-library-retrieval]]
