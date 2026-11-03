---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2507.01701
type: paper
author: Bochen Han, Songmao Zhang (CAS Beijing)
published: 2025-07-02
accessed: 2026-10-29
reliability: med (small QA/math benchmarks, no coding or tool-use tasks; HTML full text read)
---
# Exploring Advanced LLM Multi-Agent Systems Based on Blackboard Architecture (LbMAS)
## Key claims
- Classic 1980s blackboard architecture ported to LLM MAS: knowledge sources (LLM agents with roles), a shared blackboard (public space all agents read/write + private spaces for debate/self-reflection), and a control unit (an LLM) that, each cycle, picks which agents act based on the current board content.
- Fixed agents: planner, decider, critic, conflict-resolver, cleaner; plus query-related expert agents generated per question. Cycle repeats until the decider says the board suffices, or max rounds (4 used; average 2.88-3.29 rounds on MMLU/GPQA/MATH).
- The blackboard replaces per-agent memory modules: all messages live on the board.
- Results on MMLU, ARC-C, GPQA-Diamond, BBH-date, MATH, GSM8K: best average performance, "outperforming CoT methods by an average of 4.33% and static methods by 5.02%"; second-lowest token cost on MATH vs static and autonomous MAS (autonomous ones pay extra tokens to search a workflow first).
- Ablation: the control unit "can significantly reduce the token cost" with a slight performance effect (agents deciding for themselves whether to react costs more tokens).
- Easy questions stop after one round; hard ones get multiple rounds (adaptive cost).
## Caveats (ours)
- Benchmarks are single-turn reasoning/QA, not agentic tool use. The scaling-agent-systems paper shows MAS behaves differently on agentic tasks. Gains of 4-5 points are modest.
## Quotable
> agents that will take actions are selected based on the current content of the blackboard ... the selection and execution round is repeated until a consensus is reached on the blackboard.

## Used by
[[topic-orchestration-patterns]]
