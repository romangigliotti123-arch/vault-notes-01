---
name: game-dev-tune
description: "Metric-gated tuning loop for a Roblox game: pick ONE number (gate score, economy simulation, frame cost), baseline it, run single-change experiments, keep only strict improvements, revert the rest, log every run in a ledger. Use for balance, optimise, polish, make it better, tune the economy."
argument-hint: "[what to improve] [metric]"
---

# game-dev-tune

Code comments: none by default (see roblox-luau-style, Comments). Smallest complete change: see roblox-luau-style.

Tune with a number, never a feeling. A run is a ledger in `Games/<slug>/tune/<run-id>/` that `scripts/tune_check.py` validates and `game-dev-critic` re-checks. Detail (evaluators, noise, snapshots, stop rules): `references/loop.md`.

## 1. Set up (before any edit)
1. ONE metric, its direction (up or down) and a READ-ONLY evaluator that prints the number (economy: `game-economy-simulation` or `roblox-metrics-benchmarks/compare.py`; lighting: `lighting_gate.py`; placement: `placement_gate.py`; code: `code_gates.py`; frame or part cost: `execute_luau` counters or `static_scan.py`). No evaluator: write it first, or stop and say the target cannot be measured.
2. Budget: 10 experiments (hard cap 25; low-usage mode 5). Guard rails: every gate that passed before must still pass.
3. `python <skill>/scripts/tune_check.py init Games/<slug>/tune/<run-id> --metric M --direction up|down --evaluator FILE --budget N`, run the evaluator once, then `tune_check.py baseline <run-dir> --value X` (row 0). Snapshot the files you may change.

## 2. Loop: one change per experiment
Change ONE thing, measure (twice when the number is noisy), keep it only if the metric is strictly better and the guard rails still pass, else restore the snapshot exactly. Log every try: `tune_check.py log <run-dir> --change "<text>" --before X --after Y --status keep|discard|crash [--gates-pass false]`. Same result with less code: keep. Tiny gain with ugly code: discard. Never edit the evaluator during a run (its sha256 is checked).

## 3. Stop and report
Stop at the budget, at the target, or after 3 non-improving experiments in a row (change the kind of change once, then stop). Report kept changes with before and after, discarded ideas (so nobody retries them), and the output of `tune_check.py check Games/<slug> --write Games/<slug>`. The critic runs the evaluator itself; a builder-made number is evidence only.

## Sources
Loop idea (baseline, one change, keep or revert, ledger) from Andrej Karpathy's autoresearch (github.com/karpathy/autoresearch). The repository has no LICENSE file, so only the idea is used, written in our own words; its unbounded "never stop" mode and disabled permissions are not adopted.

## Triggers (moved out of the description)

Use when the user says balance the economy, tune, optimise, make it better, polish with a number, first upgrade too slow, or when a gate score is below the pass mark and fix rounds are needed.
