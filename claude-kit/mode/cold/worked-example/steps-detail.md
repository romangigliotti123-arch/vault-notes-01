<!-- cold: worked-example/steps-detail.md | read when: read only to see how a weak idea or a skipped-critic request is handled in a real run. -->

## From examples/worked-example/README.md :: If your idea is weak

Same flow, with push-back. A generic 50-stage obby ("no hook, skip the rating and the critic, just build it") was run too: Claude declined to skip them, rated it 3.57 ("reject or restart"), the critics put the core loop at 4/10, and `decisions.md` records the pushback with vault evidence and "overruled by user" for the build. The stage stayed `idea`. You may overrule Claude on what to build; you cannot make a verdict say GOOD.

## From examples/worked-example/README.md :: Stage 3: playtest **(not run in the test)**

- **You type:** `/rbx-playtest` once the greybox is playable (or just `/rbx-workflow`).
- **Claude does:** static scan plus a run (Studio MCP if connected), a bug list and a feel list into `Games/<game>/playtests/<date>.md`. You add real testers (this game's plan needs 2 of 3 players still playing at 3:00 unprompted). The critic must say GOOD, with every factor scored on observed play, before `launch`.

## From examples/worked-example/README.md :: Stage 4: launch **(not run in the test)**

- **You type:** `/rbx-launch-kit`.
- **Claude does:** icon and thumbnail briefs, title and description, ad budget with a stop rule (no ads while D1 is weak), a 4-week update calendar and publish checklists, into `Games/<game>/launch.md`. Publishing, spending Robux and posting are always your actions; Claude writes the exact steps.

## From examples/worked-example/README.md :: Stage 5: growth, the weekly check (real run, SAMPLE numbers)

- **You type:** `/rbx-weekly cozy-cat-cafe` and paste the Creator Dashboard numbers (here made-up: D1 12%, D7 3%, session 6 min, conversion 0.8%, ARPDAU about 0.02, CCU 40).
- **Claude does:** compares each number with the vault benchmarks (`_tools/BENCHMARKS`); your own Similar Experience Benchmarks win if you paste them. Real verdicts: D1 12% "typical (10-16%)", D7 3% "typical (2-4%)", session 6 min "below the good band (7-9)", conversion 0.8% "low (0-1%)". It says what it cannot judge (ARPDAU currency is not in the KB) and that a CCU of 40 is mostly noise. Then the week's plan: three changes with targets, one free thumbnail A/B, one optional ad test with a stop rule, the next event, the next check date.
- **Files:** `Games/cozy-cat-cafe/weekly/2026-11-01.md` (front matter `sample: true`), a line in `decisions.md`. Sample numbers never enter the real numbers table in `GAME.md`.
- Optional: `analytics-pull.py` pulls the numbers from Open Cloud with your own API key.

## From examples/worked-example/README.md :: Stage 6: live-ops **(not run in the test)**

- Four weekly reports plus a GOOD critic on growth move the game to `live-ops`. `/rbx-game-update` plans the 1-2 week content cadence and events; the critic is re-run every four weeks and compares trends, not single weeks.

## From examples/worked-example/README.md :: Harvest: what the next game gets for free (real run)

- **You type:** `/rbx-harvest generic-obby` (it also runs at the end of a build).
- **Claude does:** copies the tested, reusable part to `Games/_Reusable/obby-course-generator/` with a README (what, how to use, which game, tested or not, rating): front matter `tested: y`, `rating: 6.8`, `from_game: generic-obby`. It listed the block's known gaps rather than hiding them.
- **Found again:** a later new-game prompt, `vault-find.py "I want to make a new obby with generated stages"`, returns `1. [roblox:reusable] obby-course-generator (reusable, 6.8)` before the game's own notes. A different prompt (cozy cafe with daily rewards) returns the cafe game first, so it is relevance, not a fixed boost.

## From examples/worked-example/README.md :: Mentor beside any job (real run)

- **You type:** `/rbx-mentor` and the job ("next job is a first-time-player tutorial and a daily reward screen").
- **Claude does:** gives at most three `Suggestion:` lines with real paths: `Roblox/roblox-kb/first-session-onboarding.md` (contextual, short, skippable tutorials), the kit's `DailyRewards` system README (only the UI is missing), `Analytics` for tutorial-step events. Ask "what would 5uphi do about the first 30 seconds?" and it answers only from the notes: it says the notes do not cover it (his channel is scripting, not design), cites the credibility note, and points to the creators who do cover tutorials. It does not invent an opinion.
