---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2609.14767
type: paper
author: (authors not extracted)
published: 2026-09-13
accessed: 2026-10-29
reliability: med (abstract opened only; one open-ended task family, 86 runs; very recent)
---
# Loop-Back Authority in LLM Agent Teams: flat vs hierarchical coordination
## Key claims
- Question: does giving a Manager agent authority to send a worker's output back for revision improve quality? Task: business-intelligence reporting, 43 paired products, 86 runs, each report written once by a hierarchical team and once by a flat team.
- Result: "flat teams produce higher-quality reports" - Utility d=0.42 (p=0.009), Writing Clarity d=0.34 (p=0.030). Hierarchical reports use 53% more hedging words; each revision is associated with a 0.14-point drop in clarity (1-5 scale). The first drafts were indistinguishable; the gap "can be traced to revision".
- "Authority improves quality when the Manager can verify the work, else when it can only provide feedback it has a negative effect on quality."
- Relevance: a manager that bounces reports back with vague feedback ("improve this") on open-ended deliverables can make them worse; send back only with a verifiable defect (failed check, missing item).

## Used by
[[topic-orchestration-patterns]]
