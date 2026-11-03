---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2505.00212
type: paper
author: Shaokun Zhang et al.
published: 2025-04-30
accessed: 2026-10-29
reliability: high (127 MAS logs, ICML 2025 per search snippet)
---
# Which Agent Causes Task Failures and When? (Who&When)
## Key claims
- Dataset of failure logs from 127 LLM multi-agent systems with the responsible agent and decisive error step annotated.
- Best automated method: 53.5% accuracy naming the failure-responsible agent but only 14.2% pinpointing the failure step; some methods below random; even o1 and R1 not practically usable.
- Implication for a manager: asking a model to diagnose which worker/step went wrong from transcripts is unreliable; keep structured step logs and checkpoint artifacts instead.
## Quotable
> (none; abstract-level)

## Used by
[[topic-multi-agent-failure-modes]]
