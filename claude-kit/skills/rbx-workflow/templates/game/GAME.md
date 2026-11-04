---
type: game
slug: {{slug}}
stage: idea
stage_since: {{date}}
created: {{date}}
pitch: {{pitch}}
genre: {{genre}}
project: {{project}}
published: no
---
# {{slug}}

> {{pitch}}

**Hub of this game's community.** Everything about {{slug}} links from here and back to here.

## Map
- Design: [[{{slug}}/design|design]] (loop, first 30 seconds, progression, monetisation)
- Why we chose what we chose: [[{{slug}}/decisions|decisions]]
- Systems used and built: [[{{slug}}/systems|systems]] (checks `Games/_Reusable` first)
- Evidence: [[{{slug}}/playtests/README|playtests]] | [[{{slug}}/weekly/README|weekly numbers]] | [[{{slug}}/critic/README|critic verdicts]]
- All games and reusable blocks: [[Games/README|Games hub]]
- Knowledge it leans on: [[Roblox/roblox-kb/first-session-onboarding|first session]] | [[Roblox/roblox-kb/core-loops-and-game-design|core loops]] | [[Roblox/roblox-kb/retention-d1-d7|retention D1/D7]] | [[Roblox/roblox-kb/monetisation-gamepasses|game passes]] | [[Roblox/roblox-kb/thumbnails-icons|thumbnails]] | [[Roblox/roblox-kb/updates-live-ops|live-ops]] | [[Roblox/roblox-kb/_tools/BENCHMARKS-TLDR|benchmarks]]

## Stage: idea
Stages: idea > prototype > playtest > launch > growth > live-ops. The `stage:` line above only changes through `games.py advance`, which needs a critic verdict GOOD for the current stage. The real stage is always re-derived from evidence (`games.py detect {{slug}}`); if this file claims more than the evidence supports, the evidence wins.
Definition of Done per stage: the skill `rbx-workflow` file `references/stages.md`.

## Numbers (real ones only; empty until the game is live. Paste from Creator Dashboard)
| Date | CCU | D1 % | D7 % | Session min | PTR % | Payer conv % | Source |
|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | none yet |

## Next tasks (max 5, newest first)
- [ ] Write the one-sentence pitch and run the idea rating (`rbx-rate`)

## Latest critic verdict
none yet

## Placement gate
not run. Status: playable prototype, placement not verified. (`rbx-placement`: every model checked when placed; PASS needs the full-map scan with P1-P7 clean; report in `placement-qa/`.)

## Lighting gate
not run. Status: playable prototype, lighting not verified. (`rbx-lighting`: genre preset applied early, genre / time of day / platform recorded here; PASS needs the scan with L1-L12 clean; report in `lighting-qa/`.)

## Visual gate (LOOKS)
not run. Status: playable prototype, visuals not polished. (`rbx-visual`: PASS needs V1-V7 >= 7 with screenshots; backlog in `polish-backlog.md`.)

## Notes
(free space: things worth remembering about this game)
