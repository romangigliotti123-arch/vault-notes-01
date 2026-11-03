---
tags: [manager-kb, source]
url: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
type: eng-blog
author: Mikaela Grace, Jeremy Hadfield, Rodrigo Olivares, Jiri De Jonghe
published: 2026-01-09
accessed: 2026-10-29
reliability: high (primary)
---
# Demystifying evals for AI agents
## Key claims
- Vocabulary: task, trial, grader, transcript, outcome, harness, suite. Graders: code-based (cheap, brittle), model-based (flexible, nondeterministic, calibrate vs humans), human (gold, slow).
- Capability evals (low pass rate, headroom) vs regression evals (~100%). pass@k (any success) vs pass^k (all succeed; 75% per trial -> ~42% over 3 trials).
- Roadmap: start with 20-50 tasks from real failures; unambiguous tasks with reference solutions (0% pass usually = broken task); balanced positive/negative cases; clean isolated trials; grade outcomes not paths; partial credit; calibrate LLM judges; read transcripts; watch saturation; clear ownership.
- "A good task is one where two domain experts would independently reach the same pass/fail verdict."
- Research agents: groundedness, coverage, source-quality checks.
## Quotable
> "it's often better to grade what the agent produced, not the path it took."
> "Failures should seem fair: it's clear what the agent got wrong and why."

## Used by
[[topic-anthropic-agent-guidance]], [[topic-llm-judge-and-adversarial-verification]], [[topic-multi-agent-failure-modes]], [[topic-observability]], [[topic-report-formats-and-verification]]
