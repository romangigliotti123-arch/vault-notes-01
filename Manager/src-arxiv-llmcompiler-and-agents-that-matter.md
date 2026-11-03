---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2312.04511
type: paper
author: Kim et al. (LLMCompiler); Kapoor et al. (AI Agents That Matter, arXiv 2407.01502)
published: 2023-12-07 and 2024-07-01
accessed: 2026-10-29
reliability: med (abstracts opened; older models; both widely cited)
---
# LLMCompiler (parallel function-calling planner) + AI Agents That Matter (cost-aware evaluation)
## Key claims
- LLMCompiler: a planner emits a DAG of function calls, a task-fetching unit dispatches independent calls in parallel, an executor runs them. Against ReAct: "consistent latency speedup of up to 3.7x, cost savings of up to 6.7x, and accuracy improvement of up to ~9%". It is the formal version of "plan once, run independent steps in parallel, re-plan only on failure" (plan-and-execute family with ReWOO).
- AI Agents That Matter: current benchmarks over-focus on accuracy, so "SOTA agents are needlessly complex and costly, and the community has reached mistaken conclusions about the sources of accuracy gains"; argues for jointly optimising cost and accuracy and compares against simple baselines. Cited by the scaling-agent-systems paper as showing that accuracy-only evaluation yields needlessly complex agents.
- Use for us: when judging any orchestration change, compare against the plain baseline (one Sonnet worker doing the job) on cost AND success, repeat runs.

## Used by
[[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
