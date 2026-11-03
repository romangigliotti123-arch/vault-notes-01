---
tags: [manager-kb, source]
url: https://eugeneyan.com/writing/llm-evaluators/
type: practitioner-blog
author: Eugene Yan
published: 2024 (exact date not shown in fetch)
accessed: 2026-10-29
reliability: med (practitioner survey of papers)
---
# Evaluating the Effectiveness of LLM-Evaluators
## Key claims
- Objective criteria: direct (pointwise) scoring, ideally binary; subjective criteria (tone, persuasiveness): pairwise comparison is "typically used, and more reliable"; reference-based when gold answers exist.
- Calibrate against human labels with Cohen kappa for binary/pairwise and Spearman/Kendall for Likert; be sceptical of correlation metrics; report recall and precision separately (one study: evaluator found over 95% of consistent summaries but only 30-60% of inconsistent ones).
- Biases: position (claude-v1 favoured the first position 70% of the time), verbosity, self-enhancement, score inflation (gpt-4 averaged 4.7 vs 2.9 for humans on one critique task).
- Pitfalls: over-reasoning with outside knowledge in reference-based checks ("don't overthink" helps); agreement inflated by non-expert annotators; fine-tuned judges behave as task-specific classifiers. Recommended: validate vs human labels, check position and verbosity bias before trusting.
## Quotable
> (none)

## Used by
[[topic-llm-judge-and-adversarial-verification]]
