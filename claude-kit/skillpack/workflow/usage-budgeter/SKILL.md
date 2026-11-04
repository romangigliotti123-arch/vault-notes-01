---
name: usage-budgeter
description: "Plan AI usage per task: route each job to haiku, sonnet or opus, cap workers and turns, total relative cost with budget.py, and say when to escalate or stop. Use before launching a batch of workers, when the usage limit is tight, or when a plan has many jobs."
category: workflow
tags: usage, budget, model, routing, cost, limits, effort, workers, turns, haiku, sonnet, opus
kb: Manager/topic-model-effort-routing-cost.md, Manager/topic-orchestration-patterns.md, Manager/topic-managing-ai-agents-for-roblox-game-dev.md, Manager/src-claude-api-pricing.md, Mentor/Combined-Brain.md
related: task-breaker, ai-brief-writer, rbx-low-usage, rbx-manager, sprint-planner, worker-verifier, rbx-workflow
---

# usage-budgeter

Limits, not money, are usually the constraint. This skill assigns a model tier and a turn cap to each task and totals the load in RELATIVE units, so a plan fits the user's allowance. `rbx-low-usage` is the global switch (short outputs, one worker); this is the per-plan budget. It does not decide what to build (`sprint-planner`) or split work (`task-breaker`).

## When to use
A plan has more than about five jobs, usage is limited, or a worker ran far over its expected turns. Not for: a single quick edit.

## Inputs (max 2)
1. The task list (default `docs/tasks.csv`). 2. Caps: max live workers (default 2) and a total unit cap (default 600 relative units, about 30 sonnet turns per unit-20 step; tune from the real usage screen).

## Procedure
1. Classify each task `kind`: lookup, mechanical (lint a folder, rename), build, review, debug, design.
2. Write `jobs.csv` as `id,kind,est_turns` and run `python usage-budgeter/scripts/budget.py jobs.csv --max-workers 2 --max-total-units 600`.
3. Read the routing: lookups and mechanical checks on haiku, builds and reviews on sonnet, planning and architecture on the strongest model. Decide the model ONCE per session; switching mid-session rebuilds the cache and costs more than it saves.
4. Fix every WARN: split any job over about 105 turns into phases that each write a checkpoint file; cut or defer jobs until the total is under the cap.
5. Set the controls in each brief (`ai-brief-writer`): a turn limit, a stop rule, and "report in at most 250 words, details to a file".
6. Escalation rule: on the first failure re-brief (the brief is usually the defect); on the second failure on the same job move one tier up or change the approach. Do not just re-run at higher effort, which fixes missed edge cases and not a wrong approach.
7. Default to ONE worker per job and parallelism only for disjoint read-only or disjoint-write work; fan-out multiplies tokens (the Manager KB cites about 15x for multi-agent chat).
8. Save `docs/budget.md` (Routing, Cap, Total; under 80 lines) and, after the run, note actual turns beside the estimate to calibrate the next plan.

## Studio MCP path
None for budgeting. Mark Studio-touching jobs serial in the ledger.

## Fallback
The script is the only dependency; without it do the multiplication by hand with the same weights.

## Evidence
`Manager/topic-model-effort-routing-cost.md` (workers are about 95% of tokens in the measured session; savings come from moving routine work Sonnet to Haiku, Haiku about 20x cheaper than Sonnet and Opus about 2x Sonnet; decide the model once; cap turns; effort does not fix a wrong approach; subscription weights are unpublished), `Manager/topic-orchestration-patterns.md` (multi-agent only wins for context protection, real parallelism or specialisation), `Manager/topic-managing-ai-agents-for-roblox-game-dev.md` (starting routing table for game work), `Manager/src-claude-api-pricing.md` (list prices; live-check, they change). The weights in the script are relative ratios from those notes, not money.

## Output
`docs/budget.md` with the routing table, per-tier totals, the total against the cap and the warnings.

## Acceptance checks
- [ ] Executed: `python usage-budgeter/scripts/budget.py --selftest` prints `selftest ok`; the project run ends without a cap WARN or lists the cut jobs.
- [ ] No job above the turn tail without a phase split.
- [ ] Executed: `python project-kickoff/scripts/wfdoc.py docs/budget.md --kind budget` prints PASS.
- [ ] Prices and limits marked live-check.

## Pitfalls
Reading relative units as dollars. Using the strongest model for lookups. Many cheap parallel workers that all load a big shared context. Forgetting that review and playtesting are the user's time, not tokens.

## Related
`task-breaker`, `ai-brief-writer`, `rbx-low-usage`, `rbx-manager`, `sprint-planner`, `worker-verifier`.
