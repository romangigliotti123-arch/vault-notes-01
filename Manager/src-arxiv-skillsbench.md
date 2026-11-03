---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2602.12670
type: paper
author: Li et al. (77 authors, Dawn Song last)
published: 2026-02-13
accessed: 2026-10-29
reliability: high: NeurIPS 2026 poster, deterministic verifiers
---
# SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks
## Key claims
- 87 tasks, 8 domains (counts differ between versions: 84-87 tasks), deterministic verifiers. Curated skills lift average pass rate 33.9% -> 50.5% (+16.6 pp) at v4; configuration-level gains +4.1 to +25.7 pp over 18 model-harness configs.
- Search snippets (not opened in full): self-generated skills give no benefit (about -1.3 pp); 18 of 84 tasks regress with curated skills.
- Smaller models with skills can match larger models without them.
## Quotable
> "Focused Skills with at most three modules outperform larger or exhaustive bundles."

## Used by
[[topic-personal-assistant-agents]], [[topic-skill-library-retrieval]]
