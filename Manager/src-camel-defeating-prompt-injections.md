---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2503.18813
type: paper
author: Debenedetti, Shumailov, Fan, Hayes, Carlini, Fabian, Kern, Shi, Terzis, Tramer (Google, DeepMind, ETH)
published: 2025-03-24 (v2 2025-06-24)
accessed: 2026-10-29
reliability: high
---
# Defeating Prompt Injections by Design (CaMeL)
## Key claims
- Separates control flow and data flow derived from the trusted user query so "untrusted data retrieved by the LLM can never impact the program flow"; capabilities block data exfiltration via tool calls.
- AgentDojo: 77% of tasks completed with provable security vs 84% undefended.
## Quotable
> "untrusted data retrieved by the LLM can never impact the program flow"

## Used by
[[topic-multi-agent-failure-modes]]
