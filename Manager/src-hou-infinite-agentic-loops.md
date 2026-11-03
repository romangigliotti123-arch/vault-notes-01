---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2607.01641
type: paper
author: Hou, Wang, Zhao, Wang et al.
published: 2026-07-02
accessed: 2026-10-29
reliability: med-high (static analysis of 6,549 repos; abstract read)
---
# When Agents Do Not Stop: Uncovering Infinite Agentic Loops in LLM Agents (IAL-Scan)
## Key claims
- Infinite Agentic Loops (IALs): an agent repeatedly executes model calls, tools, workflow transitions or agent handoffs because the feedback path is not effectively bounded; they arise from the interaction of agent logic, framework semantics, runtime observations and termination mechanisms.
- Consequences named: cost exhaustion, model denial of service, context growth, repeated external side effects.
- IAL-Scan static analyser on 6,549 LLM agent repositories reported 74 findings; manual review confirmed 68 IAL failures across 47 projects (91.9% precision).
- Takeaway for a manager: every loop (retry, review-fix, handoff) needs an explicit bound (max iterations/turns/budget) and side-effecting steps inside loops need idempotence guards.
## Quotable
> "an agent may repeatedly execute model calls, tools, workflow transitions, or agent handoffs when the feedback path is not effectively bounded"

## Used by
[[topic-llm-judge-and-adversarial-verification]], [[topic-multi-agent-failure-modes]]
