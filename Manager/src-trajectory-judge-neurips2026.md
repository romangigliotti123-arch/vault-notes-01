---
tags: [manager-kb, source]
url: https://neurips.cc/virtual/2026/172954
type: paper
author: (authors not shown in fetch) NeurIPS 2026 listing
published: 2026
accessed: 2026-10-29
reliability: low-med (abstract on conference page only; 14B judge, synthetic support-desk testbed)
---
# trajectory-judge: What Outcome-Only LLM Judges Miss on Agent Trajectories
## Key claims
- Deterministic support-desk testbed, 400 labelled trajectories, faults injected into correct runs; a 14B judge that sees only the request and final reply has 34-76% recall on four fault types that leave the reply unchanged (paired discrimination zero: recall equals its flag rate on clean runs).
- Loud faults (break the outcome): 84% recall; silent faults: 45% recall (paired +0.048).
- When told to check each step, the judge flagged every fault of those four types and flagged 0 of 100 clean runs; shown every step but asked only about the reply, paired discrimination +0.69 (vs +1.00 when told to check each step).
- Takeaway: give the verifier the steps/artifacts AND explicitly instruct it to check each step or claim; outcome-only judging misses silent faults.
## Quotable
> (none)
## Note
Small synthetic testbed and small judge model; direction matters more than the numbers.

## Used by
[[topic-llm-judge-and-adversarial-verification]], [[topic-multi-agent-failure-modes]]
