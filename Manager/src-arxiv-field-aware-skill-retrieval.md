---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2608.02880
type: paper
author: Goulart et al.
published: 2026-08-03
accessed: 2026-10-29
reliability: med: preprint
---
# Field-Aware Agent Skill Retrieval
## Key claims
- Most methods flatten name + description + body into one document; this paper scores each field separately (sparse and dense per field) and combines with uniform weights or a small learned MLP.
- Field-aware MLP: Recall@10 77.95 on SkillRet, 83.78 on SRA-Bench; advantage grows with skill-bank size.
- Supports separate field weighting (name > description > body) in a keyword search like find.ps1.
## Quotable
> "the advantage grows as the skill bank becomes larger"

## Used by
[[topic-skill-library-retrieval]]
