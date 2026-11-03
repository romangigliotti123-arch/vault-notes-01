---
tags: [manager-kb, source]
url: https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering
type: eng-blog
author: Vivek Trivedy (LangChain)
published: 2026-02-17
accessed: 2026-11-01
reliability: med-high (vendor, measured, single benchmark)
---
# Improving Deep Agents with harness engineering
## Key claims
- Terminal Bench 2.0 (89 tasks): 52.8% to 66.5% (+13.7 pts) changing only the harness, model fixed (gpt-5.2-codex).
- Most common failure: the agent re-reads its code, decides it looks fine, and stops. Fix: build-verify-fix prompt plus a pre-completion checklist middleware forcing a verification pass before exit. "Models are biased towards their first plausible solution."
- Loop-detection middleware counts per-file edits and, past a threshold, tells the agent to reconsider ("doom loops" of near-identical edits, 10+ times in some traces).
- Reasoning budget: always xhigh scored 53.9% (timeouts) vs high 63.6%; a "reasoning sandwich" (more reasoning on planning and verification) reached 66.5%.
- Environment mapping at start and time-budget warnings push agents toward verification. Opus 4.6 scored 59.6% on an earlier harness version.
## Quotable
> The purpose of the harness engineer: prepare and deliver context so agents can autonomously complete work.
## Used by
[[topic-multi-agent-failure-modes]], [[topic-model-effort-routing-cost]], [[topic-llm-judge-and-adversarial-verification]]
