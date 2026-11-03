---
tags: [manager-kb, source]
url: https://www.anthropic.com/engineering/AI-resistant-technical-evaluations
type: eng-blog
author: Tristan Hume (Anthropic performance engineering)
published: 2026-01-21
accessed: 2026-11-01
reliability: high (primary; fetched via summariser)
---
# Designing AI-resistant technical evaluations
## Key claims
- A hiring take-home (>1,000 candidates) had to be redesigned for each new model: Opus 4 beat almost all humans in 4 h (May 2025); Opus 4.5 matched the best human in 2 h and kept improving; time limit cut 4 h to 2 h.
- Opus 4.5 cycle counts on the released problem: 1790 casual session, 1579 after 2 h, 1363 in an improved harness after many hours (open-challenge threshold 1487): harness and test-time compute changed the score.
- "Evals have a short shelf life": each model generation needs a redesign; use the model to find where it struggles, build the next version from there.
- Models give up early: Opus 4.5 declared a bottleneck insurmountable until it was given a target cycle count, then found a workaround (a numeric target changes behaviour).
- Realistic tasks are easier for models (resemble training data); novel tasks are harder but less representative.
## Quotable
> Evals have a short shelf life; each new model required a redesign of the take-home.
## Used by
[[topic-llm-judge-and-adversarial-verification]], [[topic-brief-prompt-engineering]]
