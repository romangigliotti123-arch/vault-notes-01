---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2609.01660
type: paper
author: Shubhra Mittal
published: 2026-08-31
accessed: 2026-10-29
reliability: med (preprint v1, abstract page only read)
---
# How Fast Do Agents Rot? Long-horizon degradation in LLM agents
## Key claims
- "Task success follows a geometric law governed by a single per-step reliability parameter": success = p^steps; reliability rises with scale but stays < 1.
- On a tool-use task all tested models "dropped from near-perfect success to near zero within about sixteen steps".
- Step count, not context length, drives decay: limiting context made decay steeper (logit slope -0.69 vs -0.44), contradicting a pure lost-in-the-middle story.
- Projected reliability 0.42 at GAIA-length horizons vs 0.24 at 100-step production horizons. Calls for horizon-aware evaluation and reliability budgeting.
- Implication: keep each delegated job short (few dependent steps) and verify at boundaries; do not let one agent run a 100-step chain.

## Used by
[[topic-anthropic-agent-guidance]], [[topic-context-engineering]], [[topic-long-running-always-on-agents]]
