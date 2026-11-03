---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2601.08815
type: paper
author: (authors not extracted)
published: 2026-01-13
accessed: 2026-10-29
reliability: low-med (abstract opened; author-run experiments; single-source numbers)
---
# Agent Contracts: a formal framework for resource-bounded autonomous AI systems
## Key claims
- Extends the 1980 Contract Net Protocol idea from task allocation to resource governance: a contract bundles input/output spec, multi-dimensional resource limits (tokens, time), temporal bounds and success criteria, with lifecycle semantics.
- "Conservation laws" make delegated budgets respect the parent's: a sub-contract cannot exceed what the parent holds (hierarchical coordination through contract delegation).
- Reports (4 experiments) "90% token reduction with 525x lower variance in iterative workflows, zero conservation violations in multi-agent delegation".
- Relevance: the manager already passes max-turns / effort; this suggests passing explicit budget + success criteria + deadline as a contract in every brief and tracking the remaining budget.

## Used by
[[topic-orchestration-patterns]]
