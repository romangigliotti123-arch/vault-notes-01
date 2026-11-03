---
tags: [manager-kb, source]
url: https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons/
type: eng-blog
author: METR
published: 2025-08-12
accessed: 2026-10-29
reliability: high (primary, but n=18 / n=15 small)
---
# Research update: reconciling slowdown with time horizons (algorithmic vs holistic scoring)
## Key claims
- Claude 3.7 Sonnet passed maintainer tests on 38% (+-19%) of 18 real issues; after manual review none of the test-passing PRs were mergeable as-is.
- Four test-passing runs: 100% had test-coverage gaps, 75% documentation problems, 75% lint/format/type issues, 50% other code quality, 25% core functionality errors. Fixing a passing PR took ~26 min on average vs 1.3 h for the original human work.
- Conclusion: "algorithmic scoring based on unit tests overestimates model capabilities"; a passing test suite is a weak signal of mergeability. Optimising for such benchmarks may amplify reward hacking.
## Quotable
> "none of them are mergeable as-is"

## Used by
[[topic-llm-judge-and-adversarial-verification]], [[topic-multi-agent-failure-modes]]
