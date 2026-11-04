<!-- cold: rbx-workflow/stages-late.md | read when: read only when the evidence stage is launch, growth or live-ops (work, Definition of Done, rubric and gate of each). -->

## From skills/rbx-workflow/references/stages.md :: ### launch

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

## From skills/rbx-workflow/references/stages.md :: ### playtest

### playtest
- Work: `rbx-playtest` report into `Games/<slug>/playtests/<date>.md`; get real players if the user can (friends); fix the top issues; re-test. Measure first-session funnel when possible.
- DoD: at least 2 playtest rounds (or 1 round with 3 or more real players) with a written bug list and a feel list; top 3 issues fixed and re-tested; every factor F1-F10 scored on observed play, not plans; WORKS fully clean; monetisation present and fair; icon, thumbnail and title drafted (F8).
- Rubric: all ten factors; critical (min 6): F1, F2, F3, F4, F7, F9. Weighted mean 7.0 or more for GOOD.
- Gate to launch: critic GOOD, plus the launch kit prepared (see launch). KB benchmark gate: if real session data exists, D1 at or above the "typical" band for the genre (Creator Hub similar-experience benchmark first, `compare.py` second); no data yet means say "no numbers, scored on observed play".
