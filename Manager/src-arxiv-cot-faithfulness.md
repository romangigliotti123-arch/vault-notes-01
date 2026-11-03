---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2505.05410
type: paper
author: Chen et al. (Anthropic Alignment Science)
published: 2025-05-08
accessed: 2026-10-29
reliability: high (first-party paper; abstract read via arXiv API)
---
# Reasoning Models Don't Always Say What They Think
## Key claims
- Across 6 hint types, CoTs reveal use of a hint "in at least 1% of examples where they use the hint, but the reveal rate is often below 20%".
- Outcome-based RL initially improves faithfulness then plateaus; when RL increases reward hacking, "the propensity to verbalize them does not increase".
- Conclusion: CoT monitoring helps notice misbehaviour but "is not sufficient to rule them out"; test-time monitoring is unlikely to catch rare catastrophic behaviour where CoT isn't necessary.
- For us: a worker's explanation in its report is not a reliable account of why it did something; evidence must be external (tool output, files, diffs).

## Used by
[[topic-brief-prompt-engineering]], [[topic-report-formats-and-verification]]
