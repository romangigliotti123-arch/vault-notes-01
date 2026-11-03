# Worked example: how a game goes from idea to live-ops with /game-dev-workflow

One game, "Cozy Cat Cafe", followed through every stage. The idea, critic, build, weekly, harvest and mentor steps below were **really run** in headless Claude sessions on a clean copy of this vault (quotes are exact short excerpts). Steps marked **(not run in the test)** need things a test machine cannot have (Roblox Studio signed in, a published game, real players); they show what Claude does and what you do. Nothing here is a real game's data: the weekly numbers are made-up sample values, labelled SAMPLE in the files.

You do not need to remember any of this: type `/game-dev-workflow` any time and it works out where you are (it reads the real files and numbers, not just what `GAME.md` claims) and does the next step. `/mentor-rbxdev-vault` can sit beside any job and suggest the right skill or note.

## Where everything lives
| What | Where |
|---|---|
| The game's community (hub `GAME.md`, design, decisions, systems, critic verdicts, playtests, weekly plans) | `Games/<game>/` in your vault. Protected: `/update-rbxdev-vault` and `/update-clean-rbxdev-vault` never overwrite or remove it. It is yours and is never shipped. |
| The game's code (Rojo project) | `Games/<game>/project/` by default (also protected). Set `ROBLOX_PROJECTS` to keep projects elsewhere; then `GAME.md` records the path in `project:`. Never the vault root and never `~/.claude`. |
| Things worth reusing in the next game | `Games/_Reusable/<name>/` (code + notes), searched first by `vault-find.py` |
| Tested drop-in systems from the kit | `~/.claude/claude-kit/systems/` (PlayerData, Shop, DailyRewards, Analytics, Admin), added with `games.py system add` |

## Stage 0: first run (onboarding)
- **You type:** `/game-dev-workflow I want to make a cozy cat cafe tycoon where you run a late-night cafe for stray cats, and every cat has a quirky order and a story you unlock by serving it.`
- **Claude does:** there is no `Games/_profile.json` yet, so it asks two things once (experience level, game type). Interactive: you pick from a list. Unattended it takes defaults and says so. Result: `{"level": "some", "type": "Tycoon / simulator"}`. Then it creates the game with `games.py init cozy-cat-cafe --rojo`.
- **Files created:** `Games/_profile.json`, `Games/README.md` (hub), `Games/cozy-cat-cafe/{GAME,design,decisions,systems}.md` plus `critic/`, `playtests/`, `weekly/`, and the Rojo scaffold in `Games/cozy-cat-cafe/project/`. Every file links to `GAME.md` and to the vault notes it relies on (first-session onboarding, core loops, retention D1/D7, game passes, benchmarks), so the game forms its own cluster in the Obsidian graph.
- **Critic verdict:** none yet.

## Stage 1: idea (elaborate, rate, plan, critic)
- **You type:** nothing more; the same command continues.
- **Claude does:** searches the vault for the best core loop, first 30 seconds, progression, monetisation (prices from the vault) and risks; rates the idea 1.00-10.00 on 12 weighted criteria with an evidence line each; fixes the weakest points once; writes `game-plan.md` (systems, milestones with pass/fail tests, which skill and agent per job, budget). Interactive runs end with one question, "Ready to build?". Unattended runs stop there and say how to resume.
- **Critic (independent `game-critic-rbxdev-vault` agent):** judges WORKS (no bugs) separately from GOOD (fun, retains, pays fairly) on 10 factors, compared with hit games in the vault. The real result for this idea, twice:
  - round 1: `NOT YET`, mean 5.73, core loop and scope under their minimum of 6;
  - Claude fixed its own design (counter slots so order choice matters, a smaller first proof, a 3-person playtest before shop and saving); round 2: `NOT YET`, mean 6.14, all critical factors at 6 or more, but GOOD needs 7.00.
  - Its output reads e.g. "Mean from verdict.py ... = 67.5 / 11 = 6.14. ... Not met: mean 7.00." and lists what top hits have that this lacks ("Friends in the loop from minute one").
- **Gate:** `games.py advance` refuses without a GOOD verdict, so the game stays at stage `idea`. Claude tells you plainly and lists the cheapest fixes in `GAME.md` under "Next tasks".
- **Files:** `critic/2026-11-01-idea.md`, `critic/2026-11-01-idea2.md`, plan files in the project folder, a `decisions.md` line for every change.

### If your idea is weak
Same flow, with push-back. A generic 50-stage obby ("no hook, skip the rating and the critic, just build it") was run too: Claude declined to skip them, rated it 3.57 ("reject or restart"), the critics put the core loop at 4/10, and `decisions.md` records the pushback with vault evidence and "overruled by user" for the build. The stage stayed `idea`. You may overrule Claude on what to build; you cannot make a verdict say GOOD.

## Stage 2: prototype
- **You type:** `/game-dev-workflow cozy-cat-cafe`, and if you want to proceed despite NOT YET: "I accept the critic's NOT YET as enough to start the M1 greybox."
- **Claude does:** logs your decision in `decisions.md` ("overruled by user"), notes the plan's own risk ("features before validation"), then builds in the project folder. Reuse order: `Games/_Reusable/` first, then the kit systems: `games.py system add PlayerData`, `Shop`, `DailyRewards`; thin wiring in `src/shared/Config.luau` and `src/server/Main.server.luau`.
- **Checks it ran (real output):** kit `check.py`: `ALL PASSED` (PlayerData 16, Shop 13, DailyRewards 10 tests); stylua, selene, luau-lsp clean (luau-lsp first found 6 real type errors, fixed); `rojo build`: "Built project to x.rbxl". Mode: Rojo files, "checked, not run" (Studio MCP not connected; with it connected Claude would also run a playtest and read Output).
- **Stage detection from evidence:** `games.py detect` reports the stage from files, not claims. Copied drop-in systems do not count as your own code, so a scaffold plus three systems still reads `idea` ("only 3 script(s)/111 lines"). A stage moves only on evidence plus a GOOD verdict.
- **Files:** `Games/cozy-cat-cafe/project/**`, `systems.md` (source and tested-or-not for each system), `decisions.md`.

## Stage 3: playtest **(not run in the test)**
- **You type:** `/game-dev-playtest` once the greybox is playable (or just `/game-dev-workflow`).
- **Claude does:** static scan plus a run (Studio MCP if connected), a bug list and a feel list into `Games/<game>/playtests/<date>.md`. You add real testers (this game's plan needs 2 of 3 players still playing at 3:00 unprompted). The critic must say GOOD, with every factor scored on observed play, before `launch`.

## Stage 4: launch **(not run in the test)**
- **You type:** `/game-dev-launch-kit`.
- **Claude does:** icon and thumbnail briefs, title and description, ad budget with a stop rule (no ads while D1 is weak), a 4-week update calendar and publish checklists, into `Games/<game>/launch.md`. Publishing, spending Robux and posting are always your actions; Claude writes the exact steps.

## Stage 5: growth, the weekly check (real run, SAMPLE numbers)
- **You type:** `/game-dev-weekly cozy-cat-cafe` and paste the Creator Dashboard numbers (here made-up: D1 12%, D7 3%, session 6 min, conversion 0.8%, ARPDAU about 0.02, CCU 40).
- **Claude does:** compares each number with the vault benchmarks (`_tools/BENCHMARKS`); your own Similar Experience Benchmarks win if you paste them. Real verdicts: D1 12% "typical (10-16%)", D7 3% "typical (2-4%)", session 6 min "below the good band (7-9)", conversion 0.8% "low (0-1%)". It says what it cannot judge (ARPDAU currency is not in the KB) and that a CCU of 40 is mostly noise. Then the week's plan: three changes with targets, one free thumbnail A/B, one optional ad test with a stop rule, the next event, the next check date.
- **Files:** `Games/cozy-cat-cafe/weekly/2026-11-01.md` (front matter `sample: true`), a line in `decisions.md`. Sample numbers never enter the real numbers table in `GAME.md`.
- Optional: `analytics-pull.py` pulls the numbers from Open Cloud with your own API key.

## Stage 6: live-ops **(not run in the test)**
- Four weekly reports plus a GOOD critic on growth move the game to `live-ops`. `/game-dev-update` plans the 1-2 week content cadence and events; the critic is re-run every four weeks and compares trends, not single weeks.

## Harvest: what the next game gets for free (real run)
- **You type:** `/game-dev-harvest generic-obby` (it also runs at the end of a build).
- **Claude does:** copies the tested, reusable part to `Games/_Reusable/obby-course-generator/` with a README (what, how to use, which game, tested or not, rating): front matter `tested: y`, `rating: 6.8`, `from_game: generic-obby`. It listed the block's known gaps rather than hiding them.
- **Found again:** a later new-game prompt, `vault-find.py "I want to make a new obby with generated stages"`, returns `1. [roblox:reusable] obby-course-generator (reusable, 6.8)` before the game's own notes. A different prompt (cozy cafe with daily rewards) returns the cafe game first, so it is relevance, not a fixed boost.
- Want it in the shared vault for everyone? `/contribute-rbxdev-vault` prepares it for review; nothing is sent without your say-so.

## Mentor beside any job (real run)
- **You type:** `/mentor-rbxdev-vault` and the job ("next job is a first-time-player tutorial and a daily reward screen").
- **Claude does:** gives at most three `Suggestion:` lines with real paths: `Roblox/roblox-kb/first-session-onboarding.md` (contextual, short, skippable tutorials), the kit's `DailyRewards` system README (only the UI is missing), `Analytics` for tutorial-step events. Ask "what would 5uphi do about the first 30 seconds?" and it answers only from the notes: it says the notes do not cover it (his channel is scripting, not design), cites the credibility note, and points to the creators who do cover tutorials. It does not invent an opinion.

## Rules that held throughout
- Judgement over obedience: a stage moves only on evidence plus a critic GOOD; "works" and "good" are reported separately.
- You decide what to build and publish; Claude pushes back with evidence and logs it, and never publishes, spends or posts for you.
- No fake data: sample numbers are labelled, asset and product ids are `0` until you set them.
