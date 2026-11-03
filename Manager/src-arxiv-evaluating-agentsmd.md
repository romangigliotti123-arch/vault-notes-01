---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2602.11988
type: paper
author: Gloaguen et al. (ETH Zurich)
published: 2026-02-12
accessed: 2026-10-29
reliability: high: ICLR 2026, multi-agent eval
---
# Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?
## Key claims
- Context files "do not generally improve task success rates" and raise inference cost by over 20% on average (v3, revised 2026-09-29).
- Useful for "non-standard coding practices"; repository overviews are "not helpful" even though popular and recommended.
- Search snippets add: LLM-generated files marginally hurt, developer-written marginally help, neither significant; agents obey the files (more testing, broader exploration) which costs steps. Python-only benchmark.
- Authors: "any attempts to improve performance should be rigorously evaluated before deployment."
## Quotable
> "does not generally improve task success rates"

## Used by
[[topic-knowledge-management-rag]]
