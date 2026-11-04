<!-- cold: rbx-tune/economy-example.md | read when: read only when tuning an economy and you want a worked metric/knob/guard-rail example. -->

## From skills/rbx-tune/references/loop.md :: Economy example (obby or tycoon)

Metric: seconds until the first upgrade is affordable, direction down, target under 120. Evaluator: the simulation script from `game-economy-simulation` run on `Config.luau` values. Knobs, one per experiment: starting coins, first reward size, price of upgrade 1, income per second of the first machine. Guard rails: later tiers still unlock within the plan's session length and `code_gates.py` stays unchanged.
