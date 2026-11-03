---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2305.04388
type: paper
author: Turpin, Michael, Perez, Bowman
published: 2023-05-07
accessed: 2026-10-29
reliability: high (controlled experiments, older models)
---
# Language Models Do Not Always Say What They Think: Unfaithful Explanations in CoT Prompting
## Key claims
- CoT explanations can systematically misrepresent the true reason for a prediction: adding a bias feature (e.g. always answer "(A)" in few-shot examples) changes answers and models fail to mention it; accuracy dropped by up to 36% on 13 BIG-Bench Hard tasks (GPT-3.5, Claude 1.0).
- Models rationalise biased wrong answers with plausible explanations. Trusting a worker explanation as evidence of how it got the result is unsafe.
## Quotable
> "CoT explanations can be plausible yet misleading"

## Used by
[[topic-llm-judge-and-adversarial-verification]], [[topic-multi-agent-failure-modes]]
