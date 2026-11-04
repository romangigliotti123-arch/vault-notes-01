# rbx-tune: loop details

## Evaluator rules
- Deterministic and cheap first. A script that prints one number beats a judgment. Seed `math.random`, fix the simulated player count, freeze the config except the knob under test.
- Read-only: the evaluator never edits the game. Keep it outside the files you tune; store its path and sha256 with `tune_check.py init` (TN3 fails when it changes).
- Not deterministic (frame time, screenshots, a simulation with randomness): measure twice and keep only when both runs beat the best value so far. Visual scoring is the most expensive evaluator, so it keeps the existing limit of 3 rounds.
- Goodhart: the metric must be the thing you want. For the economy use time to first upgrade and time to unlock the last tier from the plan's targets, not raw coins. Add a guard metric when one number can be gamed (for example frame cost plus part count).

## Economy example (obby or tycoon)

Economy: metric = seconds until the first upgrade is affordable (down, target under 120) via `game-economy-simulation` on `Config.luau`; one knob per experiment; later tiers must still unlock within the plan's session length. [cold:rbx-tune/economy-example.md] read only when tuning an economy and you want a worked metric/knob/guard-rail example.

## Snapshots and reverts
Copy the files an experiment may touch to `tune/<run-id>/snap/` before the change, or use the project's git (`git stash` or a commit per keep). A revert restores the snapshot exactly, never by hand-editing back. Record crashes (the evaluator errored) as `crash`, restore, and count them in the budget.

## Ledger format
`run.json`: metric, direction, evaluator (absolute path), evaluator_sha256, budget, target. `results.tsv` columns: n, change, metric_before, metric_after, status (baseline, keep, discard, crash), gates_pass. Row 0 is the baseline (metric_after only). `metric_before` of a keep is the best value so far. `tune_check.py check` scores TN1 baseline row, TN2 strict improvement on every keep, TN3 evaluator unchanged, TN4 rows within budget, TN5 gates_pass true on keeps, and with `--claims` TN6 (a claim that something is balanced, tuned or optimised with no ledger is an unmeasured claim, scored low, never blocking).

## Stop rules and cost
Budget reached, target reached, or three experiments in a row without an improvement (switch the kind of change once, for example from prices to rewards, then stop). Each experiment costs about 300-600 tokens plus the evaluator's printed summary; ten experiments are roughly 6-9k tokens. Low-usage mode: 5 experiments, one change class.

## Not adopted from the source idea

No unbounded or overnight runs and no disabled permissions: every run has a budget and stays in the project folder. [cold:rbx-tune/sources.md] read only to see what was deliberately not adopted from the source idea.