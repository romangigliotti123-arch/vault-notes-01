---
name: sprint-planner
description: "Plan a week for a solo developer or small team: honest capacity from real hours, a 2x solo estimate factor and a buffer, tasks taken in priority order, the overflow named. Use at the start of a week or after a missed week to decide what actually fits."
category: workflow
tags: sprint, week, plan, capacity, time budget, estimate, priority, buffer, solo
kb: Roblox/roblox-kb/development-process-and-speed.md, Roblox/roblox-kb/mindset-and-strategy.md, Roblox/roblox-kb/team-and-budget.md, Mentor/Combined-Brain.md, Manager/topic-managing-ai-agents-for-roblox-game-dev.md
related: task-breaker, scope-cutter, mvp-definer, scope-creep-guard, usage-budgeter, milestone-reviewer, update-cadence-planner
---

# sprint-planner

Time budgeting for the human side. `task-breaker` makes the tasks, `scope-cutter` removes features, `usage-budgeter` budgets AI usage; this skill answers "what fits in my hours this week" and leaves the rest visibly in Overflow instead of silently half-done. Live-ops cadence (weekly update rhythm for a launched game) is `update-cadence-planner` in liveops.

## When to use
Week start, a slipped week, or when a milestone date feels optimistic. Not for: cutting features (`scope-cutter`), planning AI usage (`usage-budgeter`).

## Inputs (max 2)
1. Hours you can really work per day and how many days (default 3 h x 5 days; ask only if the user has said nothing). 2. `docs/tasks.csv` from `task-breaker` with a `priority` column (1 = most important); if missing, ask for the top 5 tasks and give the user's raw hour guess.

## Procedure
1. Compute capacity: days x hours/day x (1 - buffer). Default buffer 20% for bugs, review and life.
2. Take each raw estimate and multiply by the solo factor (default 2.0; use 1.0 only with a measured velocity from earlier sprints; the vault's indie rule is that solo developers take about twice as long as planned).
3. Prepare `sprint.csv` as `id,title,est_h,priority`, then run `python sprint-planner/scripts/sprint.py sprint.csv --days 5 --hours-per-day 3`.
4. Read the PLAN and OVERFLOW lines. Do not backfill the gap with a smaller lower-priority task; if the top task does not fit, either split it (`task-breaker`) or admit the week is for that one task.
5. Add one slot at the end of the week for a playtest and a retro (what finished, what slipped, estimate error). Save the error ratio: next sprint's solo factor is that ratio, rounded.
6. Write `docs/sprint-YYYY-WW.md` with headings Capacity, Plan, Overflow (under 80 lines). Check it.
7. At week end, update the file with done/not done and the estimate error; this is the only data that improves the next plan.

## Studio MCP path
None. This is planning.

## Fallback
Pure Markdown and the script. Without tasks.csv, ask for five tasks and run the script with those.

## Evidence
`Roblox/roblox-kb/development-process-and-speed.md` (ship a barebones MVP; solo takes about twice as long as planned; under deadline cut scope, do not stretch hours), `Roblox/roblox-kb/mindset-and-strategy.md` (protect against burnout), `Roblox/roblox-kb/team-and-budget.md` (keep teams lean; time is the scarce resource), `Mentor/Combined-Brain.md` job "running a game project", `Manager/topic-managing-ai-agents-for-roblox-game-dev.md` (milestones with acceptance tests). The 20% buffer and 3 h/day defaults are this skill's own, adjustable.

## Output
`docs/sprint-YYYY-WW.md`: Capacity line, Plan table, Overflow list, retro slot.

## Acceptance checks
- [ ] Executed: `python sprint-planner/scripts/sprint.py --selftest` prints `selftest ok`; the project run prints a capacity line and PLAN rows.
- [ ] Planned hours (after the factor) do not exceed capacity.
- [ ] Executed: `python project-kickoff/scripts/wfdoc.py docs/sprint-YYYY-WW.md --kind sprint` prints PASS.
- [ ] A playtest slot exists in the plan.

## Pitfalls
Planning at 100% of calendar hours. Using the AI's speed as the human's estimate (AI runs in minutes but review, playtest and decisions are the user's hours). Quietly carrying overflow forward without re-ranking it.

## Related
`task-breaker`, `scope-cutter`, `scope-creep-guard`, `usage-budgeter`, `milestone-reviewer`, `update-cadence-planner`.
