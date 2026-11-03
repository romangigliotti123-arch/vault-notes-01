---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2505.18286
type: paper
author: Gao et al.
published: 2025-05-23
accessed: 2026-10-29
reliability: med (abstract opened only; cited by the scaling-agent-systems paper)
---
# Single-agent or Multi-agent Systems? Why Not Both?
## Key claims
- Empirical MAS-vs-SAS comparison across popular agentic applications: "the benefits of MAS over SAS diminish as LLM capabilities improve" (frontier models such as o3 and Gemini 2.5 Pro have better long context, memory and tool use, removing reasons MAS were built).
- Proposes request cascading: run the cheap single agent first and escalate to the multi-agent system only when needed. Reported: accuracy +1.1-12% and deployment cost down by up to 20% across applications.
- Also proposes mechanisms to pinpoint the error-prone agent in a MAS.

## Used by
[[topic-orchestration-patterns]]
