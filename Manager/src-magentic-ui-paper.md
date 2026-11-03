---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2507.22358 (html v1 read in full)
type: paper
author: Mozannar, Bansal, Tan, Fourney, ... Kamar, Amershi (Microsoft Research)
published: 2025-07-30
accessed: 2026-10-29
reliability: high (paper plus user study, but small N)
---
# Magentic-UI: Towards Human-in-the-loop Agentic Systems
## Key claims
- Six mechanisms: co-planning (edit the plan before execution), co-tasking (take/hand back control), action approval/guards, answer verification, memory (reuse saved plans), multi-tasking (parallel sessions; red dot when input needed).
- ActionGuard is two-stage: a developer-set irreversibility heuristic per action (always / maybe / never irreversible). Always -> ask human, never -> auto-run, maybe -> LLM judge decides whether to ask.
- Qualitative study (12 participants, SUS 74.58): participants "often edited the plan before execution, usually to incorporate subjective preferences"; co-planning was a favourite part; many want tasks in the background with safeguards.
- Approval UX findings: approval for low-risk steps (add to cart) seen as unnecessary; for high-risk (payment, sending email, subscribing) endorsed; "making a request to change the plan, then having an action approval appear to agree to the new plan felt excessive"; users asked for a THIRD option on guards beyond allow/deny.
- Clarifying questions welcomed when a task is underspecified; users "preferred multiple questions to asked during one interruption, rather than spreading questions out over time" (batch questions).
- Main pain: latency. Verbose reasoning text and wordy multi-concept plan steps disliked; summaries appreciated. Users wanted to fix a past step and re-run from there.
## Quotable
> watching what it's doing the whole time .. defeats the whole purpose. (participant P12)

## Used by
[[topic-agent-security]], [[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]], [[topic-remote-mobile-ux]]
