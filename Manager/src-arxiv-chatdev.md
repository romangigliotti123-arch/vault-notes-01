---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2307.07924
type: paper
author: Qian et al. (OpenBMB)
published: 2023-07-16
accessed: 2026-10-29
reliability: med (abstract + repo README opened; 2023; MAST gives independent failure data)
---
# ChatDev: Communicative Agents for Software Development
## Key claims
- A "virtual software company": role-played agents (CEO, CTO, programmer, reviewer, tester) follow a chat chain (what to communicate) with "communicative dehallucination" (how to communicate: agents ask for specifics before answering). Phases: design, coding, testing. Natural language is useful for design, programming-language messages for debugging.
- Repo status (gh api 2026-10-29): 34,604 stars, Apache-2.0, pushed 2026-10-16 (active, but now a much larger "ChatDev 2.0" platform; README not reviewed in depth).
- MAST (2503.13657) case study on ChatDev: improving role specs alone gave +9.4% success; adding a high-level task-objective verification step +15.6% on ProgramDev; changing the topology (DAG to cyclic with CTO sign-off) was not significant with GPT-4 (Wilcoxon p=0.4) but was with GPT-4o (p=0.03). Success rates stayed low.
- MAST observed ChatDev verifiers doing "superficial checks" (code compiles, no TODOs) while the chess program had runtime bugs.

## Used by
[[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
