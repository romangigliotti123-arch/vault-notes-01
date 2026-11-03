---
tags: [manager-kb, source]
url: https://claude.dev/blog/spending-your-effort/
type: eng-blog
author: Anthropic (Using Claude Code series)
published: undated (Fable 5.1 / Opus 5.5 era)
accessed: 2026-10-29
reliability: high (vendor internal runs, 5 attempts/task, model-judge failure categories flagged as approximate)
---
# Using Claude Code: Spending your effort
## Key claims
- Terminal-Bench 3.0, Fable 5.1, 370 attempts each: low = 140 passes, median 73k tokens/attempt; max = 214 passes, median 222k tokens (~3x tokens). Failure type "missed a case" 59 -> 24 (low -> max); "made the wrong call" 133 -> 107.
- "increasing effort tends to reduce failures due to missing edgecases... but does not fix when the model has the wrong approach" -> effort does not replace a better plan/brief or a bigger model.
- Wall-clock: underspecified app low 1.5 min, medium 4, high 11, max 67; highly specified build: low 16 min vs max 79 min ("the models behaved much more similarly" when the spec is detailed).
- Per-task: some tasks 0/5 at low -> 4-5/5 at high/xhigh; category gains largest for security (64% -> 87%), hardware (34% -> 75%); operations small (12% -> 22%).
- Rule of thumb: low = quick in-the-loop work; medium = regular engineering (feature implementation); high = verification/edge cases (brownfield bug fix); max = fully autonomous difficult problems.
- Workflow: write spec, implement at low, review at low, verify/test at high. "higher effort levels will get more work done but Claude will also make more assumptions on my behalf."
- Low-effort failure mode: tests once, does not check its own new test would catch the bug, reports first result.
## Quotable
> "increasing effort tends to reduce failures due to missing edgecases... but does not fix when the model has the wrong approach"

## Used by
[[topic-model-effort-routing-cost]]
