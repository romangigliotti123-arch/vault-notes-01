# Formats

## Inputs discovered by scorecard.py (nothing is written to them)
| file | gate name | notes |
|---|---|---|
| `<name>-qa/gate.json`, `gate-critic.json`, `gate-*.json`, `*-gate.json` anywhere under the game folder (depth <= 5; `benchmarks/`, `packages/`, `node_modules/`, `.git/` skipped) | folder name without `-qa` (`visual-qa` -> `visual`) | A record scored by the critic (`scorer: critic` or `critic` in the file name) beats a builder-scored one; otherwise the newest file wins. |
| `code-quality/gate.json` (written by the critic or rbx-predelivery, format in the rbx-code-rate skill: SE-n checks, severity-scored) | `code-quality` | Generic extra gate, weight 10, not required; open CRITICAL/HIGH/MEDIUM items make it fail (cap 69). |
| `comment-scan/gate.json`, `scope-scan/gate.json`, `security-scan/gate.json`, `bugfix/gate.json`, `tune/gate.json` (written by `rbx-critic/scripts/code_gates.py --write`, `tune_check.py check --write`; checks CM1-3, SC1-5, SEC1-5, FL1, TN1-6) | `comment-scan`, `scope-scan`, `security-scan`, `bugfix`, `tune` | Generic extra gates, weight 10 each, not required, scored never blocking; records with `"scripted": true` are exempt from the blanket-score flag. `code-gates/run.json` is the proof that the gates ran (not a gate): a prototype-or-later critic verdict without it, or with a builder-made one, is an integrity flag (verdict.py caps such a verdict at NOT YET). |
| `placement-qa/scan-critic.json` (else `scan-builder.json`) | read for `placement` | per-check pass rate P1..P7 over the models; also the model paths used by the spec scan points |
| `critic/<date>-<stage>.md` with `verdict:` frontmatter | `critic` | newest by date; `score` is the factor mean (1-10) |
| `benchmark-scores.json` | `spec` (with `--spec`) | `{"spec", "scorer", "features": {id: 0..1}, "rubric": {B1: 1..10}, "evidence": {B1: "text"}}` |
| `benchmark-run.json` | run effort | free numbers: minutes, turns, tokens, cost, model, interventions |

Gate record fields understood generically: status from `result` / `status` / `verdict` / `passed`; checks from `scores` or `checks` (dict of number, dict with `status`/`score`, or list of `{id, status|score}`; values above 10 are treated as percent); `pass_min` (default 7); reasons from `reasons`, `problems`, `hard_fails`; `failing` (list of `{path, failed, fix}`); `scorer`; `label`; `counts`. A gate with no explicit status gets one from its checks versus `pass_min`.

## Scoring
- check score 0-10; gate score = mean x 10; pass/fail checks count 10/0; a pass/fail gate without checks = 100 or 0.
- failed gate capped at 69 (`raw_score` keeps the uncapped value); skipped = 0; missing required gate (visual, placement, critic) = 0.
- critic: GOOD = mean x 10, NOT YET capped 69, BAD capped 39.
- overall = sum(weight x score) / sum(weight) over discovered gates plus missing required ones. Weights: visual 25, placement 20, critic 25, lighting 15, spec 20, any other gate 10.
- grade A >= 90, B >= 80, C >= 70, D >= 50, F below. `all_required_pass` = visual, placement and critic all pass.
- top 3 problems: points lost by gate shortfall, shared among checks under their pass mark by deficit and among reasons / failing models; critic problems are derived and rank low while other gates are failing. Each has a concrete fix.

## scorecard.json (schema 1)

[cold:rbx-bench/formats.md] read only to parse scorecard.json fields.

## benchmarks/ layout

[cold:rbx-bench/formats.md] read only to locate history.csv, runs/ and baseline.json or the bench-dir rules.

## vault_cost.py

[cold:rbx-bench/formats.md] read only to parse the vault_cost.py JSON fields and cost-history.csv.

## learn_stats.py

[cold:rbx-bench/formats.md] read only to interpret learn_stats.py output.