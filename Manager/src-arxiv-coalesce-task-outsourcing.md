---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2506.01900
type: paper
author: COALESCE authors (names not extracted)
published: 2025-06-02
accessed: 2026-10-29
reliability: low-med (abstract opened; mostly simulation; the only LLM market/contract-net paper found)
---
# COALESCE: skill-based task outsourcing among LLM agents
## Key claims
- Market-style allocation: agents outsource subtasks to cheaper specialised third-party agents when a unified cost model says outsourcing beats internal execution; skill discovery + decomposition + simplified market decision rules + a standard protocol (mentions A2A).
- Evidence: 239 theoretical simulations give 41.8% cost-reduction potential; 240 real LLM tasks show "20.3% cost reduction with proper epsilon-greedy exploration".
- Notes (via search summary, not verified in the full text) that LLM skills are qualitative/probabilistic so bids are hard to compare.
- This is the nearest thing to evidence for contract-net / auction orchestration with LLMs; it is thin. See [[src-arxiv-agent-contracts]] for the budget-governance side.

## Used by
[[topic-orchestration-patterns]]
