---
tags: [manager-kb, source]
url: https://hamel.dev/blog/posts/llm-judge/
type: practitioner-blog
author: Hamel Husain
published: 2024 (exact date not shown in fetch)
accessed: 2026-10-29
reliability: med (practitioner method, one consultancy)
---
# Creating a LLM-as-a-Judge That Drives Business Results
## Key claims
- Critique-shadowing process: one principal domain expert makes binary pass/fail calls with written critiques; critiques become few-shot examples for the judge prompt; iterate until agreement converges (Honeycomb example: 3 iterations to 90% agreement).
- Split labelled data train (10-20%) / dev (40-45%) / test (40-45%); aim for 30-50 examples of each label in dev and test; start with ~30 diverse examples.
- Measure true positive rate and true negative rate separately, not raw agreement ("Raw agreement can be misleading when classes are imbalanced"). Avoid 1-5 Likert scales: binary verdicts are more actionable.
## Quotable
> "Raw agreement can be misleading when classes are imbalanced"

## Used by
[[topic-llm-judge-and-adversarial-verification]]
