---
tags: [manager-kb, source]
url: https://www.langchain.com/blog/better-harness-a-recipe-for-harness-hill-climbing-with-evals
type: eng-blog
author: Vivek Trivedy (LangChain)
published: 2026-04-08
accessed: 2026-11-01
reliability: low-med (method post, qualitative results, tiny sample)
---
# Better Harness: harness hill-climbing with evals
## Key claims
- Evals are the learning signal for editing the harness (prompts, instructions, tools): tag evals by behaviour, split each category into optimisation and holdout sets to catch overfitting.
- Loop: baseline, diagnose failures from traces, ONE targeted harness change, check regressions, accept; review changes manually before shipping.
- Tested with Claude Sonnet 4.6 and GLM-5 on a small sample; reported gains qualitative only (fewer redundant follow-up questions); no aggregate scores.
## Used by
[[topic-skill-library-retrieval]], [[topic-brief-prompt-engineering]]
