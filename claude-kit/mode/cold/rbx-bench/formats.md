<!-- cold: rbx-bench/formats.md | read when: read only to parse scorecard.json fields. -->

## From skills/rbx-bench/references/scorecard-format.md :: scorecard.json (schema 1)

`{kind: "vault-scorecard", schema, run_id, date, time, vault_version, game, spec, spec_version, label, root, overall, grade, all_required_pass, gates: {name: {status, score, raw_score, weight, required, checks, pass_min, reasons, failing, scorer, label, source, sha256, mtime}}, problems: [{rank, gate, check, impact, text, fix}], integrity: [text], run_meta, weights, method}`

## From skills/rbx-bench/references/scorecard-format.md :: benchmarks/ layout

`history.csv` (one row per run: date, run_id, vault_version, game, spec, overall, grade, all_required_pass, visual, placement, lighting, critic, spec_score, other_gates, missing, failing, minutes, turns, label, scorecard), `runs/<run_id>/scorecard.json|.md`, `baseline.json`. Location: `--bench-dir`, else `$BENCH_DIR`, else `Games/benchmarks` when the game folder sits in a `Games` folder, else `<game folder>/benchmarks`.

## From skills/rbx-bench/references/scorecard-format.md :: vault_cost.py

JSON: `always_on`, `load_mode` (skills, agents, listing_tokens, rules_tokens, hidden_from_listing), `totals` (session_without_load_tokens, session_with_load_tokens, load_adds_tokens, description_tokens_all), `top_by_listing` / `top_by_body` / `top_by_disk`, `flagged` (threshold_chars, items, tokens_saved_if_trimmed_to_threshold), `disk`, `install` (seconds, tool), `vault_version`, `method`. History: `cost-history.csv` next to `--out`. Method: tokens = ceil(chars / 4); listing = `name: description`; a skill with `disable-model-invocation: true` lists nothing.

## From skills/rbx-bench/references/scorecard-format.md :: learn_stats.py

Local queue (`pending`, `sent`, `rejected`, `ready-to-send`, oldest pending age, topics), inbox repo (`inbox`, `processed_accepted`, `processed_rejected`, CURATION-LOG decisions and rates, reject rule codes, topics) from `--clone PATH` or read-only `gh api`. `LEARN_STATS_GH` overrides the gh command (tests).
