---
name: sequel-planner
description: "Decide whether to update, spin off or sequel an existing game: gather the game's own evidence (retention, update response, audience), apply decision rules, write the choice with kill criteria. Use when a game plateaus or after a successful launch, before committing months to a new project."
category: design
tags: sequel, spin-off, update, big update, lifecycle, portfolio, plateau, decision, roadmap
kb: Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/case-studies-spin-or-die.md, Roblox/roblox-kb/case-studies-rainbow-friends.md, Roblox/roblox-kb/case-studies-pet-simulator.md, Roblox/roblox-kb/case-studies-racing-game-unnamed.md
related: feature-prioritizer, update-cadence-planner, retention-diagnoser, dau-drop-investigator, competitor-teardown, rbx-workflow
---

# sequel-planner

Vault: big updates revive games (Rainbow Friends recovered with Chapter 2, official talk; Spin or Die kept updating and grew while an abandoned sibling declined); reputation does not rescue a weak concept (a well-known developer's racing game failed); hype without a reason to return fades; do not drop cadence while building a big update.

## When to use
A live game has plateaued, or you plan a new game from an existing hit. Not for: weekly content (`update-cadence-planner`), diagnosing a drop (`dau-drop-investigator`).

## Inputs (max 3)
1. The game's metrics (default: `metrics-snapshot-logger` output or Creator Hub numbers: D1, D7, CCU trend, session length). 2. Team capacity in weeks (default: solo, 12 weeks). 3. The candidate: major update, spin-off, or sequel.

## Procedure
1. Evidence table: current D1 and D7 against `_tools/BENCHMARKS.md` flags, trend of the last 8 weeks, share of players who reach the endgame, top three player complaints. Missing data = `KB gap` or `unknown`; do not guess.
2. Diagnose the type of problem: (a) a missing endgame or returning reason (low D30 and D7: fix with a major update), (b) a saturated or old core (long decline despite updates: a sequel or spin-off may help), (c) packaging or discovery (low CTR: not a design problem), (d) technical debt (the old codebase blocks change).
3. Decision rules: update when the loop is liked (retention healthy) but content is exhausted; spin off when a system or mode proved popular on its own and could carry a new loop (beware tumors and splitting players); sequel when the core needs a rebuild and the brand carries recognisable value; do nothing new when the cadence has not been tried.
4. Cost check: a big update is typically a 4-6 week to quarterly cycle in the vault; a sequel is a new launch with the marketing and discovery problem again (about 16,000 new experiences a day per `discovery-algorithm`). Sunk cost does not count.
5. Protect the live game: keep cadence running while building the big thing, else the expansion launches to a shrunken audience.
6. Write the decision and its kill criteria: the metric, the threshold and the date at which you stop (e.g. D1 under X after 4 weeks, with X taken from your baseline).
7. Record the reasoning and the dissent in `decisions.md`; save `design/sequel.md`; run the doc check.

## Studio MCP path
Design only.

## Fallback
Pure document; numbers from Creator Hub by hand.

## Evidence
`updates-live-ops` (cadence versus major updates; expansions per quarter; do not drop cadence), `case-studies-spin-or-die`, `case-studies-rainbow-friends` (update revival, official talk), `case-studies-pet-simulator` (a long-running series: lineage pattern; claims are creator/tracker), `case-studies-racing-game-unnamed` (reputation does not rescue a weak concept, official 2018).

## Output
`design/sequel.md`: evidence table, problem type, decision with reasons, cost, protect-live-game plan, kill criteria.

## Acceptance checks
- [ ] Every metric has a source or `unknown`.
- [ ] The decision names the problem type it solves.
- [ ] Kill criteria have a metric, a threshold and a date.
- [ ] Executed: `python gdd-one-pager/scripts/docheck.py design/sequel.md --kind sequel` prints PASS.

## Pitfalls
A sequel to escape an unfixed loop problem. Letting the live game die during the build. Assuming the brand carries a weaker game. Starting a spin-off that competes for the same players.

## Related
`feature-prioritizer`, `update-cadence-planner`, `retention-diagnoser`, `competitor-teardown`.
