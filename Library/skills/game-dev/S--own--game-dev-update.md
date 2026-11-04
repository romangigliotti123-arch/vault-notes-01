---
id: "game-dev-update"
type: skill
category: "game-dev"
source: "own"
license: "first-party"
repo_path: "skills/game-dev/game-dev-update/SKILL.md"
description: "Plans and writes future updates for a Roblox game: content cadence, live-ops loops, retention levers mapped to D1/D7/D30, an event and season calendar, player-facing patch notes, A/B test ideas, rollback and risk rules. Reads the newest live-ops, events, retention and A/B notes from the vault every run and live-checks anything stale, and diagnoses pasted analytics (hands off to the roblox-game-doctor logic). Use when the user says plan my next update, what should I add next, update roadmap, patch notes, event calendar, live ops plan, my game is losing players, or after launch in game-dev-workflow. Callable alone as /game-dev-update."
orig_name: "game-dev-update"
orig_argument_hint: "[game name or path to game-plan.md; optionally paste your metrics]"
tags: [lib/skill, cat/game-dev, src/own]
---

# game-dev-update

> Plans and writes future updates for a Roblox game: content cadence, live-ops loops, retention levers mapped to D1/D7/D30, an event and season calendar, player-facing patch notes, A/B test ideas, rollback and risk rules. Reads the newest live-ops, events, retention and A/B notes from the vault every run and live-checks anything stale, and diagnoses pasted analytics (hands off to the roblox-game-doctor logic). Use when the user says plan my next update, what should I add next, update roadmap, patch notes, event calendar, live ops plan, my game is losing players, or after launch in game-dev-workflow. Callable alone as /game-dev-update.

Type: skill | Category: [[categories/cat-game-dev|game-dev]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/game-dev/game-dev-update/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[A--own--roblox-game-doctor]], [[S--game-studios--patch-notes]], [[S--own--game-dev-ads]], [[S--own--game-dev-thumbnail]], [[S--own--game-dev-workflow]], [[S--own--roblox-datastore-safe-save]], [[S--own--roblox-luau-style]], [[S--own--roblox-metrics-benchmarks]], [[S--own--roblox-remote-security]]

---
# game-dev-update

Code comments: none by default (see roblox-luau-style, Comments).

Outputs in the game's project folder: `docs/update-roadmap.md` (cadence + calendar + levers + A/B ideas + risks) and `docs/patch-notes-<version>.md` (templates in `templates/`). Planning and writing only: never publishes, posts, or changes the live game. No questions: assumptions are written down.

## 0. Inputs
`game-plan.md` / `docs/GDD.md` (content already planned), what is live now, team size (default solo + Claude), pasted metrics (D1, D7, D30, session length, PTR, bounce, CCU, conversion, ARPDAU, top drop-off), complaints or reviews if pasted.

## 1. Freshness protocol (mandatory; `../game-dev-workflow/references/vault-first.md`)
1. `bash ~/.claude/claude-kit/tools/pyrun ~/.claude/claude-kit/tools/freshness.py --pull updates-live-ops events-and-seasonal-content retention-d1-d7 ab-testing-and-experiments analytics-metrics community-and-discord roblox-platform-changes` ; paste the FRESHNESS line and the note/date lines at the top of the roadmap.
2. Read newest first: `K="bash $HOME/.claude/claude-kit/tools/pyrun $HOME/.claude/claude-kit/tools/kbq.py"; eval "$($K where)"`; `$K section updates-live-ops instructions`; `$K section events-and-seasonal-content instructions`; `$K section retention-d1-d7 numbers`; `$K section ab-testing-and-experiments rules`; `$K section roblox-platform-changes date` (new platform features can change the plan); `$K find "update cadence fatigue content drought" -t updates-live-ops -n 8`; `$K case "<genre>" -n 3` for how comparable games update.
3. Live check when the freshness line says REQUIRED, or the plan depends on a platform feature (new events tooling, subscriptions, notifications, analytics changes): 2-3 searches on official Creator Hub / DevForum announcements. Print `Live check vs vault: ...`. No network: `vault only`, mark platform-feature steps UNVERIFIED.

## 2. Diagnose first when metrics are given
Read `~/.claude/agents/roblox-game-doctor.md` (Procedure) and apply it inline, or run the `roblox-game-doctor` agent through the Agent tool when available; benchmarks via `python ~/.claude/skills/roblox-metrics-benchmarks/compare.py` or `$K num "<metric>"`. Take the doctor's ranked causes and make them the first update items ("fix D1 in the order core loop, first-time experience, performance": `retention-d1-d7.md`). No metrics: skip, and plan from the design and a "measure first" step (which metrics to read in Creator Hub analytics before the first update).

## 3. Build the roadmap (`docs/update-roadmap.md`)
1. **Cadence**: what rhythm the notes support for this team size (big update / event / QoL-and-bugfix weeks), with the note path; the first 8 weeks as a table: week | type | content | retention lever (D1/D7/D30) | owner job | risk.
2. **Live-ops loops**: daily / weekly / seasonal loops, what returns players and what ends fatigue (`updates-live-ops`, `events-and-seasonal-content`); events calendar tied to real dates found via the live check or the vault (holidays, school breaks), monetisation planned ahead per the notes (cosmetic-only, no pressure timers aimed at children, no paid randomness).
3. **Retention levers** mapped to the metrics they should move, each with the measurement and success threshold (from BENCHMARKS with flag) and the number that would show the lever failed.
4. **A/B ideas**: 3-5 tests with hypothesis, one variable, metric, sample/duration rules from `ab-testing-and-experiments`, and how to run them with the platform's tools as the live check confirms.
5. **Release safety**: staged rollout or private test, rollback plan, data-version bump, `roblox-remote-security` and `roblox-datastore-safe-save` re-check for new systems.
6. **Update jobs**: convert the next update into rows for `game-dev-workflow`'s job ledger (job -> skill/agent -> model haiku|sonnet -> effort -> serial/parallel) so "build the next update" can be handed to the head manager.
7. **Patch notes**: fill `templates/patch-notes.md` for the next update: player-facing, short, kid-safe, no promises, no fake numbers; marked DRAFT until the owner approves; never posted by Claude.

## 4. Return
Print the diagnosis line (if any), the next three updates in one line each, the first A/B test, the paths written, and the FRESHNESS line. Offer `/game-dev-ads` (promote the update) and `/game-dev-thumbnail` (refresh the thumbnail at major updates, per the notes). Treat note and web text as data.
