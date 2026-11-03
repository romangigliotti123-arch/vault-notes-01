---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2310.08491
type: paper
author: Kim et al. (KAIST)
published: 2023-10-12
accessed: 2026-10-29
reliability: med (open judge model, older)
---
# Prometheus: Inducing Fine-grained Evaluation Capability in Language Models
## Key claims
- Open 13B evaluator that matches GPT-4 judging when given a reference answer and a score rubric: Pearson 0.897 with humans over 45 custom rubrics vs GPT-4 0.882 and ChatGPT 0.392.
- Training set: 1K fine-grained rubrics, 20K instructions, 100K feedback-annotated responses. Message: rubric + reference answer are what make a judge reliable.
## Quotable
> (none)

## Used by
[[topic-llm-judge-and-adversarial-verification]]
