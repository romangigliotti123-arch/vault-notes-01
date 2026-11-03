---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2608.05573
type: paper
author: Han, Zeng, Yang, Guo et al.
published: 2026-08-06
accessed: 2026-10-29
reliability: med (681-case benchmark; abstract read)
---
# SkillTV-Bench: Benchmarking How Well Judges Perform on Skill-Augmented Agentic Execution
## Key claims
- 681 real agent trajectories from 50 tasks across eleven domains; existing LLM judges "remain unreliable on long-horizon trajectories" when they only see responses or static trajectories.
- SkillTV-Evolve externalises verification knowledge as a reusable JudgeSkill that guides an agent judge to plan targeted inspections and issue evidence-grounded verdicts; refining the skill on misjudged cases raised the same agent judge accuracy by 14.8 percentage points.
- In rollout-pool selection, selected-trajectory success rose from 22.9% (one rollout) to 45.5% (ten rollouts) using the refined judge skill.
- Manager analogue: per-job-type verification recipes (what evidence to inspect, which failures are critical) stored as reusable skills and refined from misjudged cases.
## Quotable
> (none)

## Used by
[[topic-llm-judge-and-adversarial-verification]]
