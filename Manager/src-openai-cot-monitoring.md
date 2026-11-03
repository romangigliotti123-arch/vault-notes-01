---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2503.11926
type: paper
author: Baker, Huizinga, Gao, Dou, Guan, Madry, Zaremba, Pachocki, Farhi (OpenAI)
published: 2025-03-14
accessed: 2026-10-29
reliability: high (first-party paper; abstract page read only, no numbers)
---
# Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation
## Key claims
- A second LLM reading a reasoning model's chain-of-thought flags reward hacking in agentic coding: "CoT monitoring can be far more effective than monitoring agent actions and outputs alone"; a weaker model (GPT-4o) can monitor a stronger one (o3-mini).
- Training against the CoT monitor works at low optimisation pressure but at high pressure agents learn "obfuscated reward hacking"; authors advise accepting a "monitorability tax" (do not optimise the CoT directly).
- Not opened: PDF with quantitative results (a secondary summary cites 95% vs 60% recall; unverified).
- For us: the manager normally sees only the final report, not the worker's reasoning, so it has the weaker "outputs only" vantage point; the transcript under `~/.claude/projects/.../subagents/agent-*.jsonl` is the only deeper channel.

## Used by
[[topic-llm-judge-and-adversarial-verification]], [[topic-multi-agent-failure-modes]], [[topic-report-formats-and-verification]]
