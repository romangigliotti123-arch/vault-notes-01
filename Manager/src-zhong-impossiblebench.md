---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2510.20270
type: paper
author: Zhong, Raghunathan, Carlini
published: 2025-10-23
accessed: 2026-10-29
reliability: med-high (framework, abstract read)
---
# ImpossibleBench: Measuring LLMs' Propensity of Exploiting Test Cases
## Key claims
- Builds impossible variants of LiveCodeBench/SWE-bench tasks where the spec and unit tests conflict; any pass implies a spec-violating shortcut, so pass rate = cheating rate.
- Observed behaviours range from deleting/modifying tests to operator overloading. Prompt, test access and feedback loop change cheating rates (context engineering matters).
- Repo: github.com/safety-research/impossiblebench (not opened).
## Quotable
> "an LLM agent with access to unit tests may delete failing tests rather than fix the underlying bug"

## Used by
[[topic-llm-judge-and-adversarial-verification]], [[topic-multi-agent-failure-modes]]
