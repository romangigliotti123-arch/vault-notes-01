---
name: scope-creep-guard
description: "Hold a frozen scope with a swap rule: every new item must name an equal-or-larger item that leaves, checked by scopeguard.py, plus a freeze trigger and a re-open condition. Use after scope-cutter or mvp-definer has fixed the plan, whenever someone says 'one more thing'."
category: workflow
tags: scope creep, freeze, swap rule, feature creep, mvp, change control, add feature
kb: Roblox/roblox-kb/development-process-and-speed.md, Roblox/roblox-kb/common-mistakes.md, Roblox/roblox-kb/mindset-and-strategy.md, Roblox/roblox-kb/core-loops-and-game-design.md, Mentor/Combined-Brain.md, Manager/topic-multi-agent-failure-modes.md
related: scope-cutter, mvp-definer, feature-prioritizer, sprint-planner, decision-log-writer, milestone-reviewer, task-breaker
---

# scope-creep-guard

`scope-cutter` makes the cut once; this skill defends it afterwards. The rule set is deliberately mechanical so a tired human or an enthusiastic AI worker cannot argue past it: nothing enters a frozen scope for free, and every swap is written down.

## When to use
A frozen scope exists (`design/scope.md` or `docs/kickoff.md`) and a request arrives to add something, or a worker proposes extras in its SUGGESTED_NEXT. Not for: choosing the first scope (`scope-cutter`, `mvp-definer`) or ranking all features (`feature-prioritizer`).

## Inputs (max 2)
1. The frozen scope with days per item (default: `design/scope.md`). 2. The proposed addition and its estimate in days.

## Procedure
1. Classify the request: bug fix of in-scope behaviour (allowed, status `fix`), enabler required by an in-scope item (allowed, needs an estimate), or new feature (needs a swap).
2. Check the loop test from the vault: does it feed the core loop, or is it a second loop (a tumor)? A second loop is declined or deferred regardless of cost.
3. Write the swap in `scope.csv` (`item,status,days,swap_for`): mark the item that leaves as `swapped_out` and the new one `added` with `swap_for` naming it. Estimate with the solo factor (see `sprint-planner`).
4. Run `python scope-creep-guard/scripts/scopeguard.py scope.csv`. FAIL lines name what to cut: unpaid additions, a swap smaller than the addition, one swap paying for two additions, a live total above the frozen total.
5. Anything declined goes to the Deferred list with a **return condition** (a measurable trigger, e.g. "after the loop playtest shows D1 above the benchmark"), not "maybe later".
6. Record accepted swaps with `decision-log-writer` so the reason survives the session.
7. Write `docs/scope-guard.md` (headings Frozen, Swap, Rule; under 70 lines) and check it. Unfreeze only at the named playtest or milestone review (`milestone-reviewer`).

## Studio MCP path
None.

## Fallback
CSV and Markdown only.

## Evidence
`Roblox/roblox-kb/development-process-and-speed.md` (ship a barebones MVP around one loop; avoid feature creep and months of perfecting before release; cut scope under deadline), `Roblox/roblox-kb/common-mistakes.md`, `Roblox/roblox-kb/core-loops-and-game-design.md` (tie every system to the loop; avoid tumors and parallel loops), `Roblox/roblox-kb/mindset-and-strategy.md`, `Manager/topic-multi-agent-failure-modes.md` (workers add unrequested work; fence the scope and list ideas under suggested-next instead of building them). The swap rule is this skill's own policy.

## Output
`scope.csv` with the swap and the script verdict; `docs/scope-guard.md`; entries in Deferred with return conditions.

## Acceptance checks
- [ ] Executed: `python scope-creep-guard/scripts/scopeguard.py --selftest` prints `selftest ok`; the project run ends PASS.
- [ ] Executed: `python project-kickoff/scripts/wfdoc.py docs/scope-guard.md --kind scopeguard` prints PASS.
- [ ] Every declined item has a return condition that can be measured.
- [ ] The live total is at or below the frozen total.

## Pitfalls
Calling a feature a bug fix. Paying for a big addition with a vague "polish" item. Letting a worker implement a "small extra" before the swap is recorded. Silent unfreezing after a bad week.

## Related
`scope-cutter`, `mvp-definer`, `feature-prioritizer`, `sprint-planner`, `decision-log-writer`, `milestone-reviewer`.
