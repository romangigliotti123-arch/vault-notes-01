---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2510.01285
type: paper
author: Salemi et al. (per search summary; abstract page opened, author list not verified)
published: 2025-09-30
accessed: 2026-10-29
reliability: med (abstract opened only; v2 numbers via search snippet)
---
# LLM-Based Multi-Agent Blackboard System for Information Discovery in Data Science
## Key claims
- Argues master-slave MAS "rely on a rigid central controller that requires precise knowledge of each sub-agent's capabilities", which fails when the main agent lacks full observability of sub-agents' knowledge (large data lakes).
- Design: a central agent posts requests on a shared blackboard; autonomous subordinate agents (each owning a data-lake partition, or web retrieval) volunteer based on their own capabilities. This is an auction/volunteer flavour of blackboard.
- Benchmarks KramaBench, modified DSBench, DA-Code: abstract (v1) says "13%-57% relative improvements in end-to-end success and up to a 9% relative gain in data discovery F1 over the best baseline" (baselines include RAG and master-slave).
- Distinguishes a blackboard (agents decide whether to contribute) from plain shared memory (agents execute what a coordinator assigned).
## Caveats (ours)
- Domain is data discovery over large heterogeneous corpora; no software-engineering comparison found.

## Used by
[[topic-orchestration-patterns]]
