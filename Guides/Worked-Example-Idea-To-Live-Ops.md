---
tags: [guide, rbx-workflow]
description: "Worked example: one game from idea to live-ops with /rbx-workflow (each stage: what you type, what Claude does, critic verdict, files created)."
---
# Worked example: how a game goes from idea to live-ops with /rbx-workflow

One game, "Cozy Cat Cafe", followed through every stage. The idea, critic, build, weekly, harvest and mentor steps below were **really run** in headless Claude sessions on a clean copy of this vault (quotes are exact short excerpts). Steps marked **(not run in the test)** need things a test machine cannot have (Roblox Studio signed in, a published game, real players); they show what Claude does and what you do. Nothing here is a real game's data: the weekly numbers are made-up sample values, labelled SAMPLE in the files.

You do not need to remember any of this: type `/rbx-workflow` any time and it works out where you are (it reads the real files and numbers, not just what `GAME.md` claims) and does the next step. `/rbx-mentor` can sit beside any job and suggest the right skill or note.

## Where everything lives
| What | Where |
|---|---|
| The game's community (hub `GAME.md`, design, decisions, systems, critic verdicts, playtests, weekly plans) | `Games/<game>/` in your vault. Protected: `/rbx-update` and `/rbx-clean` never overwrite or remove it. It is yours and is never shipped. |
| The game's code (Rojo project) | `Games/<game>/project/` by default (also protected). Set `ROBLOX_PROJECTS` to keep projects elsewhere; then `GAME.md` records the path in `project:`. Never the vault root and never `~/.claude`. |
| Things worth reusing in the next game | `Games/_Reusable/<name>/` (code + notes), searched first by `vault-find.py` |
| Tested drop-in systems from the kit | `~/.claude/claude-kit/systems/` (PlayerData, Shop, DailyRewards, Analytics, Admin), added with `games.py system add` |

## Stage 0: first run (onboarding)
- **You type:** `/rbx-workflow I want to make a cozy cat cafe tycoon where you run a late-night cafe for stray cats, and every cat has a quirky order and a story you unlock by serving it.`
- **Claude does:** there is no `Games/_profile.json` yet, so it asks two things once (experience level, game type). Interactive: you pick from a list. Unattended it takes defaults and says so. Result: `{"level": "some", "type": "Tycoon / simulator"}`. Then it creates the game with `games.py init cozy-cat-cafe --rojo`.
- **Files created:** `Games/_profile.json`, `Games/README.md` (hub), `Games/cozy-cat-cafe/{GAME,design,decisions,systems}.md` plus `critic/`, `playtests/`, `weekly/`, and the Rojo scaffold in `Games/cozy-cat-cafe/project/`. Every file links to `GAME.md` and to the vault notes it relies on (first-session onboarding, core loops, retention D1/D7, game passes, benchmarks), so the game forms its own cluster in the Obsidian graph.
- **Critic verdict:** none yet.

## Stage 1: idea (elaborate, rate, plan, critic)
- **You type:** nothing more; the same command continues.
- **Claude does:** searches the vault for the best core loop, first 30 seconds, progression, monetisation (prices from the vault) and risks; rates the idea 1.00-10.00 on 12 weighted criteria with an evidence line each; fixes the weakest points once; writes `game-plan.md` (systems, milestones with pass/fail tests, which skill and agent per job, budget). Interactive runs end with one question, "Ready to build?". Unattended runs stop there and say how to resume.
- **Critic (independent `rbx-judge` agent):** judges WORKS (no bugs) separately from GOOD (fun, retains, pays fairly) on 10 factors, compared with hit games in the vault. The real result for this idea, twice:
  - round 1: `NOT YET`, mean 5.73, core loop and scope under their minimum of 6;
  - Claude fixed its own design (counter slots so order choice matters, a smaller first proof, a 3-person playtest before shop and saving); round 2: `NOT YET`, mean 6.14, all critical factors at 6 or more, but GOOD needs 7.00.
  - Its output reads e.g. "Mean from verdict.py ... = 67.5 / 11 = 6.14. ... Not met: mean 7.00." and lists what top hits have that this lacks ("Friends in the loop from minute one").
- **Gate:** `games.py advance` refuses without a GOOD verdict, so the game stays at stage `idea`. Claude tells you plainly and lists the cheapest fixes in `GAME.md` under "Next tasks".
- **Files:** `critic/2026-11-01-idea.md`, `critic/2026-11-01-idea2.md`, plan files in the project folder, a `decisions.md` line for every change.

### If your idea is weak

Same flow with push-back; Claude declines to skip the rating and critic, you may overrule what to build but never a verdict. [cold:worked-example/steps-detail.md] read only to see how a weak idea or a skipped-critic request is handled in a real run.

## Stage 2: prototype
- **You type:** `/rbx-workflow cozy-cat-cafe`, and if you want to proceed despite NOT YET: "I accept the critic's NOT YET as enough to start the M1 greybox."
- **Claude does:** logs your decision in `decisions.md` ("overruled by user"), notes the plan's own risk ("features before validation"), then builds in the project folder. Reuse order: `Games/_Reusable/` first, then the kit systems: `games.py system add PlayerData`, `Shop`, `DailyRewards`; thin wiring in `src/shared/Config.luau` and `src/server/Main.server.luau`.
- **Checks it ran (real output):** kit `check.py`: `ALL PASSED` (PlayerData 16, Shop 13, DailyRewards 10 tests); stylua, selene, luau-lsp clean (luau-lsp first found 6 real type errors, fixed); `rojo build`: "Built project to x.rbxl". Mode: Rojo files, "checked, not run" (Studio MCP not connected; with it connected Claude would also run a playtest and read Output).
- **Stage detection from evidence:** `games.py detect` reports the stage from files, not claims. Copied drop-in systems do not count as your own code, so a scaffold plus three systems still reads `idea` ("only 3 script(s)/111 lines"). A stage moves only on evidence plus a GOOD verdict.
- **Files:** `Games/cozy-cat-cafe/project/**`, `systems.md` (source and tested-or-not for each system), `decisions.md`.

## Stage 3: playtest **(not run in the test)**

[cold:worked-example/steps-detail.md] read only to see what the playtest stage looks like.

## Stage 4: launch **(not run in the test)**

[cold:worked-example/steps-detail.md] read only to see what the launch stage looks like.

## Stage 5: growth, the weekly check (real run, SAMPLE numbers)

[cold:worked-example/steps-detail.md] read only to see a real weekly-check run with its sample numbers and verdict wording.

## Stage 6: live-ops **(not run in the test)**

[cold:worked-example/steps-detail.md] read only to see what the live-ops stage looks like.

## Harvest: what the next game gets for free (real run)

[cold:worked-example/steps-detail.md] read only to see a real harvest run and how the item is found again.

## Mentor beside any job (real run)

[cold:worked-example/steps-detail.md] read only to see a real mentor run and its answer style.

## Rules that held throughout
- Judgement over obedience: a stage moves only on evidence plus a critic GOOD; "works" and "good" are reported separately.
- You decide what to build and publish; Claude pushes back with evidence and logs it, and never publishes, spends or posts for you.
- No fake data: sample numbers are labelled, asset and product ids are `0` until you set them.

Related: [[master-playbook]] | [[Combined-Brain]] | [[CAPABILITIES]]
