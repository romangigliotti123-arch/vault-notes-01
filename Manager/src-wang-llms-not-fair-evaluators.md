---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2305.17926
type: paper
author: Peiyi Wang et al.
published: 2023-05-29
accessed: 2026-10-29
reliability: med-high (clear controlled demo)
---
# Large Language Models are not Fair Evaluators
## Key claims
- Quality ranking by an LLM referee can be flipped by changing answer order: Vicuna-13B beat ChatGPT on 66 of 80 queries with ChatGPT as evaluator when positions were manipulated.
- Three calibrations: Multiple Evidence Calibration (write evidence before rating), Balanced Position Calibration (aggregate over orders), Human-in-the-Loop Calibration (escalate high-uncertainty cases using a position-diversity entropy).
## Quotable
> "the quality ranking of candidate responses can be easily hacked by simply altering their order of appearance in the context"

## Used by
[[topic-llm-judge-and-adversarial-verification]]
