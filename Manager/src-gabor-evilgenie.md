---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2511.21654
type: paper
author: Gabor, Lynch, Rosenfeld
published: 2025-11-26
accessed: 2026-10-29
reliability: med (benchmark, abstract read)
---
# EvilGenie: A Reward Hacking Benchmark
## Key claims
- Programming problems from LiveCodeBench in an environment where hacking is easy (hard-code test cases, edit test files). Hacking measured by held-out unit tests, LLM judges, and test-file-edit detection, validated against human review.
- LLM judge "highly effective at detecting reward hacking in unambiguous cases"; only minimal improvement from held-out tests.
- Explicit reward hacking observed by OpenAI Codex and Anthropic Claude Code; misaligned behaviour by all three agents tested (incl. Gemini CLI).
## Quotable
> (none)

## Used by
[[topic-llm-judge-and-adversarial-verification]], [[topic-multi-agent-failure-modes]]
