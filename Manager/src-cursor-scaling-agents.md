---
tags: [manager-kb, source]
url: https://cursor.com/blog/scaling-agents
type: eng-blog
author: Wilson Lin (Cursor)
published: 2026-01 (month per secondary result; exact day not shown)
accessed: 2026-10-29
reliability: med-high (primary eng blog, vendor)
---
# Scaling long-running autonomous coding (Cursor)
## Key claims
- Locks failed: "Twenty agents would slow down to the effective throughput of two or three, with most time spent waiting"; agents held locks too long or never released them.
- Flat self-coordination failed: "With no hierarchy, agents became risk-averse. They avoided difficult tasks and made small, safe changes instead"; work churned without progress.
- What worked: planners create tasks, workers "just grind on their assigned task until it's done, then push", and a judge agent decides at the end of each cycle whether to continue; the next iteration starts fresh. Hundreds of workers push to the same branch with minimal conflicts. A dedicated integrator role for conflict resolution created more bottlenecks than it solved.
- Open problems: "We still need periodic fresh starts to combat drift and tunnel vision"; agents occasionally run far too long. "The harness and models matter, but the prompts matter more."
## Quotable
> "We still need periodic fresh starts to combat drift and tunnel vision."

## Used by
[[topic-multi-agent-failure-modes]], [[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
