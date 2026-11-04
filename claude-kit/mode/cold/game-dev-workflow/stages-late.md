<!-- cold: game-dev-workflow/stages-late.md | read when: read only when the evidence stage is launch, growth or live-ops (work, Definition of Done, rubric and gate of each). -->

## From skills/game-dev-workflow/references/stages.md :: ### launch

### launch
- Work: `game-dev-launch-kit` (icon and thumbnail brief, title and description, ad budget plan, update calendar, publish checklist). Publishing to Roblox, spending Robux or money, and posting are always the user's action: write the steps and the exact settings, never do them.
- DoD: kit files exist in `Games/<slug>/launch.md` (links to each deliverable), `roblox-publish-checklist` and `roblox-launch-checklist` all checked or marked N/A with a reason, first 4 weeks of updates planned, ad plan has a stop rule (retention first: no ads while D1 is below "weak" band), the user confirmed publishing (`published: yes` in GAME.md and the place id recorded by the user).
- Rubric: F8 (critical, min 7), F1, F7, F9 as shipped; plus kit completeness.
- Gate to growth: game is live (user says so, GAME.md `published: yes`) AND first real numbers pasted into GAME.md.

### growth
- Work: weekly loop with `game-dev-weekly` (paste Creator Dashboard numbers; compare with benchmarks; plan the week: changes, ad/thumbnail tests, next event) into `Games/<slug>/weekly/<date>.md`.
- DoD: 4 weekly reports; at least one change shipped for each weak metric found; packaging test run (2 icons/thumbnails) with a result; retention not "broken" (D1 not under the broken band); ad spend, if any, tied to a measured payback.
- Rubric: the numbers table (section 4) plus F5, F6, F8. Critic compares the trend over weeks, not one week.
- Gate to live-ops: critic GOOD on growth: D1 and session in typical band or better, or a written, evidence-backed reason and plan; content cadence of 1-2 weeks is running.

### live-ops
- Work: cadence updates (`game-dev-update`), events (`events-and-seasonal-content`), weekly checks continue, re-run the critic every 4 weeks.
- DoD (continuing): cadence kept (1-2 weeks, max 2-3 weeks, `updates-live-ops`), each update has patch notes and a measured result, no regression in retention.
- No further stage; the critic still runs before big updates.
