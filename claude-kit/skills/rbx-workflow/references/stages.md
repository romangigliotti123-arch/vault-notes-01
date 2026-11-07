# stages: detection, Definition of Done, rubric and gates

Six stages: **idea > prototype > playtest > launch > growth > live-ops**. The factor numbers F1-F10 are those of `quality-model.md`. The state of a game lives in `Games/<slug>/` (helper: `python .rbx/claude-kit/tools/games.py ...`, called `G` below).

## 1. Detect the real stage (evidence beats GAME.md)
`G detect <slug> --project <project folder>` prints claimed stage (GAME.md), evidence stage and the reasons. Rules it applies, which you then confirm by looking:
| Evidence stage | Needs |
|---|---|
| idea | a pitch, `game-plan.md` or `docs/` exist; fewer than 3 Luau scripts or under 150 lines |
| prototype | 3 or more Luau scripts and 150 or more lines in the project folder |
| playtest | prototype plus at least one playtest report (`Games/<slug>/playtests/*.md` or the project's `docs/PLAYTEST.md`) |
| launch | playtest plus a critic GOOD for playtest plus (published: yes in GAME.md, or `Games/<slug>/launch.md`) |
| growth | launch plus published plus real numbers in GAME.md or weekly reports |
| live-ops | growth plus 4 or more weekly reports plus critic GOOD for growth |
If GAME.md claims more than the evidence supports, say so in one line ("GAME.md says playtest, I only find a prototype: no playtest report") and work from the evidence stage; fix the claim only by doing the missing step. If the evidence is higher than GAME.md (user built things outside the flow), keep the claim and propose catching up through the critic.
**Studio evidence hook** (skill `rbx-studio`): if tools named `mcp__Roblox_Studio__*` exist in your tool list, add the open place to the evidence: `list_roblox_studios`, script count (`script_search`/`search_game_tree`), baseline `get_console_output`, a playtest (`start_stop_play`) while reading Output, errors quoted exactly, and write it to `Games/<slug>/playtests/<date>.md` (mode: Studio MCP). That run is the "works" evidence for prototype and playtest; no errors in a 3-minute run is the DoD line. If the tools do not exist: Rojo project files if `default.project.json` exists (evidence = static checks + `rojo build`, "checked, not run"), else hand code (everything needing a run is `untested`). Say which of the three modes you are in. Setup is opt-in and the user's choice (`studio-setup.ps1` / `.sh`). Never launch Studio yourself.

## 2. Resume protocol (what /rbx-workflow does on every run)
1. Profile: `G profile` (first run only: onboarding, see `onboarding.md`).
2. Find the game: argument slug, else `G list`; one game = resume it; several = ask which (AskUserQuestion; headless: the most recently changed); none = new game (`G init <slug> ...`, then Stage 1 of SKILL.md).
3. `G detect`, then read `Games/<slug>/GAME.md` (next tasks, decisions) and the latest critic verdict.
4. Do the next step of the evidence stage from the table in section 3, run the critic when the Definition of Done looks met, and only then `G advance`.
5. Update GAME.md (numbers, next tasks), `decisions.md` for any decision or pushback, and the stage's evidence file. Reuse before building: `systems.md` rule (Games/_Reusable first). Anything reusable you finish: `rbx-harvest`.

## 3. Per stage: the work, Definition of Done (DoD), rubric, gate
Rubric = the factors scored 1-10 with evidence (see `rbx-critic` for the report). "Critical" factors must reach the stated minimum or the verdict cannot be GOOD. **Critical factors per stage (single list; `quality-model.md` defines F1-F10 only):**

| stage | critical (min) | note |
|---|---|---|
| idea | F1, F2, F7, F10 (6 each; F7 also no violation) | scored on the plan |
| prototype | F1, F2 (6 each) | F7 becomes critical (min 6) if the last verdict (idea or earlier critic file) flagged F7 below 6; F9 and F10 scored, not critical |
| playtest | F1, F2, F3, F4, F7, F9 (6 each) | weighted mean 7.0 |
| launch | F8 (7) | F1, F7, F9 as shipped |
| growth, live-ops | none fixed | numbers table plus F5, F6, F8 |

**LOOKS (visual gate) is a third requirement, not a factor:** from prototype on a verdict can be GOOD only if `rbx-visual` produced a passing gate (V1-V7 >= 7, zero layout findings at phone/tablet/desktop, >= 6 screenshots of the current build); the critic re-scores the screenshots itself (`verdict.py` input `visual_gate`). Without it the status is `playable prototype, visuals not polished`.
**PLACEMENT (placement gate) is a fourth requirement:** from prototype on a verdict can be GOOD only if the critic's own fresh full-map scan (`rbx-placement`, `placement_gate.py --scorer critic`) passed: every model has a pivot, a sane size, rests on its surface, is upright, faces its target, overlaps nothing, is anchored and lines up with its neighbours (`verdict.py` input `placement_gate`). Without it the status is `playable prototype, placement not verified`.
**LIGHTING (lighting gate) is a fifth requirement:** from prototype on a verdict can be GOOD only if the critic's own fresh scan (`rbx-lighting`, `lighting_gate.py --scorer critic`) passed checks L1-L12: not the default Roblox look, Atmosphere and Sky present, effects in sane ranges, grading cohesive with the palette, brightness neither crushed nor blown, shadows on, fog that suits the genre, lit interiors, within the mobile/PC budget, no duplicate effects, time of day coherent (`verdict.py` input `lighting_gate`). Without it the status is `playable prototype, lighting not verified`.

Per-factor and per-stage pass/fail checks with numbers: `critic-checks.md` (the critic runs them; a failed check with no exception caps the factor at 5).

Without Studio/MCP the run-based prototype items are `untested`, F1/F2 timings `estimated`, and the best verdict is `GOOD (provisional)`; advancing needs Studio evidence or the user's phone-stopwatch confirmation (manager.md section 8).

### idea
- Work: Stages 1-5 of SKILL.md (idea, elaborate from the vault, rate, plan). Do the pushback now: a weak idea is cheapest to fix here.
- DoD: one-sentence pitch; core loop written as action > reward > repeat with cycle time; first 30 seconds written; monetisation stated and fair; scope that one person can ship a first playable of; `rbx-rate` overall of 6.00 or more with no hard-rule flag; `design.md` filled; plan in `game-plan.md`.
- Rubric: F2 (critical, min 6), F1 (critical, min 6), F7 (critical, min 6, no violation), F10 (critical, min 6), F5, F6, F8 (as plans, scored on the plan).
- Gate to prototype: critic GOOD on the idea (the `rbx-rate` table counts as evidence) AND the user said "Ready to build".

### prototype
- Work: build the smallest playable of the core loop plus first 30 seconds (Stage 6, manager). Studio MCP if connected, else files and Rojo. Use `systems.md` rule for each system.
- DoD (works): the project loads (luau-check or Studio), no errors in Output during a 3-minute run (Studio only; else `untested`), core loop playable start to first reward, no placeholder/mock data presented as real. (good): a stranger-style walk-through shows the first action under 10 s and first reward under 30 s (measured in Studio or on the user's phone; else `estimated`, verdict at most `GOOD (provisional)`); the loop is fun for 3 minutes by itself. (looks): `Games/<slug>/art-direction.md` exists and the project uses its StyleKit; the visual gate passed (`rbx-visual`, screenshots attached), else the stage result is reported as `playable prototype, visuals not polished` with `polish-backlog.md`.
- Rubric: F1, F2 (critical, min 6 each), F3, F4, F9 (stability), F10. Others N/A.
- Gate to playtest: WORKS pass (rbx-playtest static scan + run) AND LOOKS pass (visual gate with screenshots) AND critic GOOD.
- Gate to playtest (placement): every model placed in the map was checked when it was placed (`Games/<slug>/placement-qa/placements/`) and the full-map scan passed (`PLACEMENT GATE: PASS`).
- Gate to playtest (lighting): the genre preset was applied early (`LightingKit.apply`, stamped on `Lighting`) and the lighting scan passed (`LIGHTING GATE: PASS`, `Games/<slug>/lighting-qa/gate.json`).

### playtest
- Work: `rbx-playtest` report into `Games/<slug>/playtests/<date>.md`; get real players if the user can (friends); fix the top issues; re-test. Measure first-session funnel when possible.
- DoD: at least 2 playtest rounds (or 1 round with 3 or more real players) with a written bug list and a feel list; top 3 issues fixed and re-tested; every factor F1-F10 scored on observed play, not plans; WORKS fully clean; monetisation present and fair; icon, thumbnail and title drafted (F8).
- Rubric: all ten factors; critical (min 6): F1, F2, F3, F4, F7, F9. Weighted mean 7.0 or more for GOOD.
- Gate to launch: critic GOOD, plus the launch kit prepared (see launch). KB benchmark gate: if real session data exists, D1 at or above the "typical" band for the genre (Creator Hub similar-experience benchmark first, `compare.py` second); no data yet means say "no numbers, scored on observed play".

### launch
- Work: `rbx-launch-kit` (icon and thumbnail brief, title and description, ad budget plan, update calendar, publish checklist). Publishing to Roblox, spending Robux or money, and posting are always the user's action: write the steps and the exact settings, never do them.
- DoD: kit files exist in `Games/<slug>/launch.md` (links to each deliverable), `rbx-publish` and `rbx-launch-check` all checked or marked N/A with a reason, first 4 weeks of updates planned, ad plan has a stop rule (retention first: no ads while D1 is below "weak" band), the user confirmed publishing (`published: yes` in GAME.md and the place id recorded by the user).
- Rubric: F8 (critical, min 7), F1, F7, F9 as shipped; plus kit completeness.
- Gate to growth: game is live (user says so, GAME.md `published: yes`) AND first real numbers pasted into GAME.md.

### growth
- Work: weekly loop with `rbx-weekly` (paste Creator Dashboard numbers; compare with benchmarks; plan the week: changes, ad/thumbnail tests, next event) into `Games/<slug>/weekly/<date>.md`.
- DoD: 4 weekly reports; at least one change shipped for each weak metric found; packaging test run (2 icons/thumbnails) with a result; retention not "broken" (D1 not under the broken band); ad spend, if any, tied to a measured payback.
- Rubric: the numbers table (section 4) plus F5, F6, F8. Critic compares the trend over weeks, not one week.
- Gate to live-ops: critic GOOD on growth: D1 and session in typical band or better, or a written, evidence-backed reason and plan; content cadence of 1-2 weeks is running.

### live-ops
- Work: cadence updates (`rbx-game-update`), events (`events-and-seasonal-content`), weekly checks continue, re-run the critic every 4 weeks.
- DoD (continuing): cadence kept (1-2 weeks, max 2-3 weeks, `updates-live-ops`), each update has patch notes and a measured result, no regression in retention.
- No further stage; the critic still runs before big updates.

## 4. Verdict rules (used by rbx-critic)
- Weighted mean of the scored factors (equal weights unless the stage lists critical ones, which count double) plus the WORKS result.
- **GOOD**: WORKS pass, mean 7.0 or more, every critical factor at its minimum, no hard-rule violation.
- **LOOKS**: from prototype on, GOOD needs the visual gate PASS. Missing, skipped or failing gate = at most NOT YET, and the report carries `STATUS: playable prototype, visuals not polished`. `games.py advance` also refuses a verdict file without `visual: pass`.
- **PLACEMENT**: from prototype on, GOOD also needs the placement gate PASS from a scan the critic made itself. Missing, skipped, stale or failing = at most NOT YET and `STATUS: playable prototype, placement not verified`. `games.py advance` refuses a verdict file without `placement: pass` (and without `visual: pass`).
- **LIGHTING**: from prototype on, GOOD also needs the lighting gate PASS from a scan the critic made itself. Missing, skipped, stale or failing = at most NOT YET and `STATUS: playable prototype, lighting not verified`. `games.py advance` refuses a verdict file without `lighting: pass` (a verdict written before the lighting gate existed has no such line: run a fresh critic pass).
- **NOT YET**: WORKS pass or fixable, mean 4.5 to 6.9, any critical factor under its minimum, or LOOKS not passed. Blocks advancing. The report lists the top 3 fixes with the factor each lifts.
- **BAD**: mean under 4.5, or a hard-rule violation (pay-to-win, paid randomness for kids, pressure timers, stranger contact, copying another game's assets), or the core loop (F2) scored 3 or lower, or WORKS fails in a way that loses data or exposes players. Say it plainly and give the cheapest path: fix, pivot or stop.
- The mean is computed with a script or shown arithmetic; do not eyeball it.
- Numbers (growth and live-ops): the critic cites `compare.py` verdicts and the Creator Hub benchmark; "typical" is the minimum for GOOD, "weak" is NOT YET, "broken" is BAD for that factor.

## 5. Where things are written
`Games/<slug>/GAME.md` (stage, numbers, next tasks), `design.md`, `decisions.md`, `systems.md`, `playtests/<date>.md`, `weekly/<date>.md`, `critic/<date>-<stage>.md` (frontmatter `stage:`, `verdict:`, `date:`, `score:`; `G advance` reads it), `launch.md`. All of it stays in the protected Games folder, linked both ways so Obsidian shows one cluster per game.
