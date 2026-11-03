---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2505.19591
type: paper
author: Dang et al.
published: 2025-05-26
accessed: 2026-10-29
reliability: med (abstract opened only)
---
# Multi-Agent Collaboration via Evolving Orchestration (puppeteer)
## Key claims
- A centralized orchestrator ("puppeteer") trained by reinforcement learning dynamically sequences and prioritises agents ("puppets") as the task state evolves, replacing static organisational structures that "struggle to adapt as task complexity and agent numbers grow".
- Reports better performance at lower compute; analysis says gains come from "more compact, cyclic reasoning structures" emerging, not from larger teams.
- Cited by the scaling-agent-systems paper as evidence that architecture-task alignment, not team size, drives results.
- Relevance to us: supports a single, adaptive coordinator over fixed pipelines or free-for-all swarms; but the orchestrator here is trained (RL), ours is prompt-driven.

## Used by
[[topic-orchestration-patterns]]
