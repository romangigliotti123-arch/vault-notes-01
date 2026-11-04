---
name: rbx-bench
description: "Measures whether vault changes make better Roblox games and what load mode costs: scorecard.py (0-100 card, compare), 3 standard test games, vault_cost.py (load-mode tokens), learn_stats.py."
argument-hint: "[game folder | compare | cost | learn]"
---

# rbx-bench

Precedence: When a kit skill and another installed skill cover the same job, use the kit skill.

Gates (visual V1-V7, placement P1-P7, lighting, critic) judge one game at a time; this skill reads what they already wrote, turns it into one comparable number per run, and measures the vault itself. It never changes a gate, a verdict or a game.

## Three tools (stdlib Python, run with `claude-kit/tools/pyrun` or `python -I`)
- **Score a game**: `python scripts/scorecard.py collect Games/<slug> [--spec obby|tycoon|tower-defense] [--require-critic]` writes `benchmarks/runs/<id>/scorecard.json` + `.md` (per-gate pass/fail, per-check scores, weighted overall 0-100, top 3 problems with fixes, integrity flags) and appends a row to `benchmarks/history.csv` (date, vault version, game, scores). Every `gate.json` / `gate-*.json` under the game folder is discovered, so a new gate appears without a code change. The `hiccup` gate (`hiccup-qa/`, written by `tools/hiccup.py check|retro`: H1 reported vs objective events, H2 pre-flight run, H3 retro run) is scored, never blocking; the card shows the hiccups-per-game trend of the personal ledger.
- **Compare**: `scorecard.py compare <A> <B>` (scorecard file, run id, `baseline`, `last`, `prev`); `baseline set <scorecard.json>`; `--strict` exits 1 on a regression. `history`, `verify` (were the scored gate files edited afterwards?), `spec show <id>`.
- **Vault cost**: `python scripts/vault_cost.py --kit <kit> [--install-test]` (or `--config ~/.claude`): skills/agents loaded by `/rbx-load`, estimated tokens of every description and of the mode rules (chars / 4, method stated in the report), install time, disk size, 10 heaviest skills, descriptions over the threshold. `python scripts/learn_stats.py [--clone PATH | --repo owner/name]`: queue and inbox counts, accepted/rejected ratio, notes per topic (read-only).

## The standard benchmark
`benchmarks/standard/{obby,tycoon,tower-defense}.json` (+ `.md` cards): fixed prompt, target features, required screenshots, scan points, rubric. Run the SAME prompt in every vault version you compare. How to run, save, score and avoid score gaming: `references/protocol.md` (read it before a benchmark build). Output formats: `references/scorecard-format.md`.

## Rules
- The builder never scores its own run. An independent critic reads the scorecard and fills `benchmark-scores.json`; scores need evidence text; the card flags builder-scored gates and blanket scores.
- A scorecard is a measurement, not a target: never edit gate files, verdicts or specs to raise it, and never compare cards of different specs as if they were the same task.
- Token numbers are chars/4 estimates for comparing versions, not a bill.
- Do not edit anything outside the benchmark folder, the game folder's `benchmark-*.json` files and the report you were asked for.

## Learn
`/rbx-learn` for a verified non-obvious finding (one note each); on a problem run `vault-find.py "<problem>" --type learned` first.
