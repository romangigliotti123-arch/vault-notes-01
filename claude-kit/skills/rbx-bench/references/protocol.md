# Benchmark protocol (how to measure a vault version)

Goal: answer "does vault version B build better games than version A, and at what cost" with numbers that two people can reproduce. One benchmark run = one standard test game built in `/rbx-load` mode, gated by the normal gates, scored by an independent critic, recorded by `scorecard.py`.

## Roles (never merge them)
- **Operator** (Roman or the master session): picks the vault version, the spec and the budget; starts the builder; never helps it mid-run.
- **Builder** (master + its workers in load mode): receives the fixed prompt only. It does not see the rubric anchors, the scorecard formula or earlier scorecards of the same spec.
- **Independent critic** (`rbx-judge`, a fresh session or agent that did not build): runs the gates itself (`scorer: critic`), fills `benchmark-scores.json`, then runs `scorecard.py`. The critic reads the scorecard; the builder does not.

## Steps
1. **Pin the version.** Record `vault_version` (kit commit or `KIT-VERSION`; `vault_cost.py` and `scorecard.py` print it) and the model name. Two versions are compared only on the same spec version, the same model and a comparable budget.
2. **Clean room, blind builder.** After `/rbx-load`, delete `<project>/.claude/skills/rbx-bench` in the BUILDER's project (load mode copies this skill there, with the rubric anchors and formula; `scorecard.py --project` flags the run if it is still present) and set `"benchmark_skill_hidden": true` in `benchmark-run.json`. (`/rbx-unload` copes with the missing folder; `/rbx-update` or a new load puts it back, so delete it again right before the builder starts.) The critic works in its own project where the skill stays. A new empty Roblox project folder and a new `Games/<slug>` named `bench-<spec>-<version>-<n>`; no earlier benchmark games in reach (`--add-dir` nothing else). Run `/rbx-load` there. Use a temp or dedicated HOME when comparing installs so the user's own skills do not leak in.
3. **Cost first.** Before building: `python scripts/vault_cost.py --kit <kit> --install-test --out <bench>/cost` for this version (load-mode tokens, install time, disk).
4. **Build.** Paste the spec's fixed prompt verbatim (`benchmarks/standard/<id>.md`, "Fixed prompt"). Nothing else: no hints about gates, no extra requirements. The builder follows the vault's normal workflow (art direction, placement gate after each model, visual gate, critic). Stop at the budget (spec `suggested_minutes` / `suggested_turns`) or when the builder says playable, whichever is first. Record actual minutes, turns, tokens and cost as `Games/<slug>/benchmark-run.json` (`{"minutes": 88, "turns": 140, "model": "...", "tokens": 0}`; the operator writes it, not the builder).
5. **Save** (what to save, all inside `Games/<slug>/`, nothing else is scored):
   - `visual-qa/` (gate.json, gate-critic.json, `r<N>/` screenshots incl. the spec's required ones: `<viewport>-<moment>.png`)
   - `placement-qa/` (scan-critic.json, gate-critic.json) and any other `<name>-qa/gate*.json` the gates wrote (lighting, model quality, ...)
   - `comment-scan/`, `scope-scan/`, `security-scan/`, `bugfix/`, `tune/` (gate.json each) and `code-gates/run.json`, all written by `code_gates.py --scorer critic --write Games/<slug>`
   - `critic/<date>-<stage>.md` (written by `verdict.py --write`)
   - `benchmark-run.json` (effort) and the project source (for the staleness check: `--project`)
   - the console transcript/log of the final full run (errors count as evidence for rubric B5/B6/B7)
6. **Score.** The critic: (a) re-runs placement scan and visual gate itself, (b) plays the game or reads the captures and fills `benchmark-scores.json` (template at the end of the spec card): features 0 / 0.5 / 1 each with a reason, rubric B1-B7 1-10 each with an evidence sentence that names a file, screenshot or console line, (c) runs
   `python scripts/scorecard.py collect Games/<slug> --spec <id> --require-critic --project <project folder> --label "<vault version> run n"`.
   `--require-critic` counts every gate not scored by the critic as 0.
7. **Compare.** First run of a spec: `scorecard.py baseline set <scorecard.json>`. Later versions: `scorecard.py compare baseline <new scorecard.json> --strict`. Read: overall delta, gate deltas, per-check deltas, regressions. One run per version is a sample, not proof: repeat 3 times and compare medians when the difference is under 10 points (model variance is real).
8. **Report.** Per run: scorecard card, the compare, the cost line (`vault_cost.py`). State what was not measured.

## Avoiding score gaming
- The score is computed from the gate records the gates themselves wrote. Do not hand-write `gate.json`; use `visual_gate.py --write`, `placement_gate.py ingest`, `verdict.py --write`. `scorecard.py verify <scorecard.json>` re-hashes the scored files, so edits after scoring show as CHANGED.
- Builder-scored records are flagged (`scorer`), blanket scores (all checks identical and >= 9) are flagged, rubric scores without evidence text are flagged, a critic file that claims `visual: pass` while the gate record fails is flagged, gate records older than the newest Luau source are flagged (stale). Treat a card with integrity flags as advisory until they are cleared by a re-run, not by an argument.
- The prompt and the spec are frozen per spec version. Changing a spec (features, rubric, scan points) means a new `version` in the JSON and a new baseline; `compare` warns when the spec version differs.
- The builder must not know the formula, the weights or the previous scorecards. A builder that names models to match the scan patterns is allowed (the prompt tells it the names); a builder that tunes to the rubric anchors is not: the benchmark skill is hidden in its project (step 2) and it gets only the prompt text.
- No gate may be loosened to pass (tolerances, waivers over 10%, skipped checks). A benchmark run with a waived or skipped gate is reported with that gate as skipped (score 0).
- Same model, same budget, same machine class. Note any manual intervention in `benchmark-run.json` (`"interventions": 2`) and say it in the report.

## Reading the numbers
- Overall is a weighted mean (visual 25, placement 20, critic 25, lighting 15 when present, spec 20 with `--spec`, other gates 10). It is for comparing versions on the same spec, not for ranking different games.
- `all_required_pass` is the real "done" signal; a high overall with `no` means a gate still fails.
- Cost numbers (`vault_cost.py`) are estimates (chars / 4). A change that raises scores 3 points and costs 2000 more tokens in every session is a trade-off to decide, not a win.

## Order of use
`vault_cost.py` (cost of the version) -> build -> critic scores -> `scorecard.py collect` -> `compare baseline` -> report.
