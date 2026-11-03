---
name: balance-sim-runner
description: "Simulate economy and combat balance in Lune with a seeded Monte Carlo: drop rates and pity, time to a goal with upgrades, time to kill with crits, then read mean, median and tail percentiles against targets. Use to check a design number before building it or to compare two tunings like for like."
category: qa
tags: balance, simulation, monte carlo, drop rate, pity, ttk, economy, progression, lune, percentile, seed
kb: Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/all-numbers-and-benchmarks.md, Roblox/roblox-kb/combat-and-gameplay-systems.md, Roblox/roblox-kb/analytics-metrics.md
related: economy-balancer, sink-source-mapper, loot-drop-builder, core-loop-designer, playtest-bot-writer, lune-unit-test-writer
---

# balance-sim-runner

Spreadsheets give averages; players feel the tail (the 1 percent drop that takes 400 rolls). `scripts/Sim.luau` is a small seeded simulator that runs under Lune with no Roblox APIs, so a balance change can be compared with the same seed. Every number it uses is YOUR design number; none is a Roblox statistic.

## When to use
Before building loot tables, egg hatching, upgrade costs, level curves, damage and health values; when a tuning change must be compared; when a tail-risk (frustration or too-fast progress) is suspected. Not for: market benchmarks (use the vault numbers files), real player behaviour (analytics), or economy flow mapping (`sink-source-mapper`).

## Inputs (max 3)
1. The mechanic and its numbers (weights, costs, damage, hp, income). 2. The target in words and numbers (default: median time-to-goal and a worst-case 99th percentile you can accept). 3. Seed (default 1; keep it fixed when comparing).

## Procedure
1. Write the mechanic as a function `trial(rng) -> number` (rolls until hit, seconds to afford, seconds to kill). Stop when one trial returns a number you can verify by hand for a trivial setting.
2. Check it by hand first: e.g. `Sim.timeToKill` with no crits equals hits / hitsPerSecond; `Sim.secondsToGoal` with no upgrades equals goal / income. Fix the model before trusting any tail.
3. Run `Sim.monteCarlo(n, seed, trial)` with n >= 2000 (10000 for tails) and read `mean, p50, p90, p99, max`. Compare p50 with the intended experience and p99 with the pain limit.
4. Drops: `Sim.rollsToTarget(rng, weights, targetIndex, pity)`; a 1 percent item needs about 100 rolls on average but p99 is around 460; pity bounds the tail (maximum equals the pity count). Always publish the odds in game if the platform or policy requires it (live-check the current rules; see `age-ratings-moderation-and-tos`).
5. Combat: `Sim.timeToKill(rng, hp, damage, hitsPerSecond, critChance, critMult)`; run attacker vs defender pairs across levels and read the matrix for outliers (one-shots, 60-second fights).
6. Economy: `Sim.secondsToGoal(goal, baseIncome, perUpgrade, upgradeCost, growth)` models greedy upgrade buying; check the time to the first, tenth and last goal and that no goal is unreachable (`math.huge`).
7. Change one number, re-run with the same seed, and record before/after in a table. Hand the final numbers to `economy-balancer` / `loot-drop-builder`.

## Studio MCP path
Not needed. After building, verify one value in the engine: `execute_luau` (Server) calling the real damage/drop function many times and comparing its distribution to the simulation (`get_console_output`).

## Fallback
Everything runs in Lune: `lune run ../skillpack/qa/balance-sim-runner/scripts/tests/Sim.test.luau` from `claude-kit/systems` proves the helpers; write your trial in a scratch file that requires `Sim`. Engine-versus-model agreement is `untested` until step "Studio MCP path" is done.

## Evidence
`Roblox/roblox-kb/testing-debugging-and-qa.md`: unit-test functions with inputs whose output you know; stress-test loops and duplicates after each change. `Roblox/roblox-kb/all-numbers-and-benchmarks.md` and `Roblox/roblox-kb/analytics-metrics.md`: market and retention numbers to compare targets with (indie numbers labelled indie, live-check). The simulator is a model: outputs are only as good as the inputs.

## Output
```
BALANCE SIM <mechanic> seed S n N
before: mean .. p50 .. p90 .. p99 .. max ..
after : mean .. p50 .. p90 .. p99 .. max ..
Verdict: meets target? tail acceptable? change made: <one line>
```

## Acceptance checks
- [ ] `lune run` of the Sim test prints "8 passed, 0 failed".
- [ ] A hand-computed trivial case matches the simulator output (quoted).
- [ ] The same seed reproduces the same numbers on a second run.
- [ ] p99 / max are reported, not just the mean.
- [ ] Inputs are labelled as design assumptions, not platform facts.

## Pitfalls
Judging by the mean. Changing the seed between before/after. Too few trials for tails. Modelling an average player (players optimise, skip or quit). Forgetting multipliers that stack in the engine. Treating the simulation as measured data.

## Related
`economy-balancer`, `sink-source-mapper`, `loot-drop-builder`, `core-loop-designer`, `playtest-bot-writer`.
