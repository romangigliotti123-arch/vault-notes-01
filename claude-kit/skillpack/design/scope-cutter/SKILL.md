---
name: scope-cutter
description: "Cut a feature list to what the core loop needs: score each feature's loop layer, cost and risk with featureprio.py, keep within a day budget, and write a deferred list with reasons. Use when the plan is bigger than the time box or a project has stalled on features."
category: design
tags: scope, cut, feature creep, deferred, budget, mvp, prioritise, time box
kb: Roblox/roblox-kb/development-process-and-speed.md, Roblox/roblox-kb/common-mistakes.md, Roblox/roblox-kb/mindset-and-strategy.md, Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/case-studies-doors.md
related: feature-prioritizer, mvp-definer, core-loop-designer, idea-validator, gdd-one-pager, core-fantasy-definer
---

# scope-cutter

Vault: avoid feature creep and six months of perfecting before release; ship a barebones MVP around one core loop; solo developers take about twice as long as planned (Zyonic, indie); under deadline, cut scope. This skill makes the cut explicit and reversible.

## When to use
The feature list exceeds the time box, or a plan has more than one loop. Not for: ranking features that all stay (`feature-prioritizer`), defining the playable minimum (`mvp-definer`).

## Inputs (max 2)
1. The feature list (default: the GDD or `docs/idea.md`). 2. Budget in working days (default: 14 for a first playable; use 6 productive hours per day and double solo estimates).

## Procedure
1. Collect every candidate feature, including art, UI, monetisation, events. One line each.
2. For each feature write: which loop layer it feeds (1 minute-to-minute, 2 session, 3 progression, 0 none), an impact 0-5, a cost in days (include test time), a risk 1-5. Features that feed no layer score 0 and are cut at once.
3. Save the table as `features.csv` (`feature,loop_layer,impact,cost_days,risk`) and run `python feature-prioritizer/scripts/featureprio.py features.csv --budget-days 14`. It labels KEEP, DEFER, CUT.
4. Review the cut line like a sceptic: does the KEEP set still make the loop fun alone? If not, move the missing enabler up and push something else down. Second check: any feature that creates a second loop (a tumor) is CUT or DEFER regardless of score.
5. Write a reason for each DEFER (what has to be true to bring it back, e.g. D1 above a threshold, or the loop proven fun) and for each CUT.
6. Add a freeze rule: no new feature enters the KEEP set until a playtest of the KEEP set is done.
7. Save `design/scope.md`; append the cut list to `decisions.md`; run the doc check.

## Studio MCP path
Design only.

## Fallback
Pure document plus the Python script.

## Evidence
`development-process-and-speed` (barebones MVP around one loop; ship many small games; cut scope under deadline; do not over-engineer one-time content), `common-mistakes`, `mindset-and-strategy`, `core-loops-and-game-design` (tie every system to the loop; avoid tumors and parallel loops), `case-studies-doors` (a white hallway with two monsters was fun first). The loop-layer weights in the script are the skill's own.

## Output
`design/scope.md`: Keep (with days), Deferred (with return condition), Cut (with reason), freeze rule, script output.

## Acceptance checks
- [ ] Executed: `python feature-prioritizer/scripts/featureprio.py --selftest` prints `selftest ok`; the project run shows the budget line.
- [ ] Every feature has a verdict and a reason.
- [ ] KEEP total days is at or under the budget.
- [ ] Executed: `python gdd-one-pager/scripts/docheck.py design/scope.md --kind scope` prints PASS.

## Pitfalls
Cutting the juice and keeping the menus. Deferring without a return condition (it becomes a wish list). Counting art as free. Hiding a cut feature behind a "coming soon" button.

## Related
`feature-prioritizer`, `mvp-definer`, `core-loop-designer`, `gdd-one-pager`.
