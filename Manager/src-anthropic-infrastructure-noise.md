---
tags: [manager-kb, source]
url: https://www.anthropic.com/engineering/infrastructure-noise
type: eng-blog
author: Gian Segato (Anthropic)
published: 2026-02-05
accessed: 2026-10-29
reliability: high (primary; eval-methodology focus)
---
# Quantifying infrastructure noise in agentic coding evals
## Key claims
- Infrastructure configuration alone (resource limits, enforcement) can shift agentic coding eval scores by more than leaderboard gaps: Terminal-Bench 2.0 gap between most- and least-resourced setups 6 percentage points (p<0.01); infra error rate 5.8% under strict enforcement vs 0.5% uncapped; up to ~3x spec headroom mostly fixes reliability, beyond that agents solve more by using heavier approaches.
- Recommendations: treat resource config as a controlled variable; specify guaranteed allocation and a separate hard kill threshold per task; report headroom; be skeptical of differences under ~3 points.
- Implication for a manager: a worker's failure or success may reflect environment limits (timeouts, memory, flaky machine) not skill - record environment in reports and rerun before blaming the model.
## Quotable
> "infrastructure configuration alone can produce differences that exceed those margins."

## Used by
[[topic-anthropic-agent-guidance]]
