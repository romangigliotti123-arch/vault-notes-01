# Standard test game 1: obstacle course (obby)

Spec id `obby`, version 1, target stage `prototype`. Suggested budget: 90 minutes, 150 turns (record the real numbers in benchmark-run.json).

## Fixed prompt (give it verbatim, change nothing, in every version you compare)

> Make a Roblox obstacle course (obby) for ages 8 to 14. 24 stages in 3 themed zones of 8 stages each (for example grass, ice, lava; you choose). A checkpoint every 4 stages that becomes the respawn point. At least 3 different hazard kinds (kill bricks, spinning bars, disappearing platforms, moving platforms). A HUD with current stage and a run timer. A finish line that gives a clear reward moment. Stage progress saves between visits (DataStore, wrapped in pcall). It must be playable on phone and desktop. Name the models so a scan can find them: Spawn, Checkpoint_<n>, Hazard_<kind>_<n>, Platform_<n>, Finish. No purchases, no pay-to-win. Report when it is playable; do not call it done unless the gates pass.

## Target features (the critic scores each 0, 0.5 or 1 with evidence)

| id | weight | feature |
|---|---|---|
| stages | 2 | 24 stages in 3 zones, each zone has its own palette and props |
| checkpoints | 2 | checkpoint every 4 stages; dying respawns at the last one; the checkpoint shows it is active |
| hazards | 2 | 3 or more distinct hazard kinds that actually kill or reset the player |
| moving | 1 | at least 2 kinds of moving or timed platforms that are fair (telegraphed) |
| hud | 1 | stage counter and run timer HUD, readable on phone, no overlap |
| save | 2 | stage progress saved with DataStore + pcall, loaded on join, no data loss on shutdown |
| finish | 1 | finish line with visible and audible reward feedback |
| curve | 2 | stage 1 is trivially safe; difficulty ramps; no stage needs a jump the character cannot make |
| mobile | 1 | touch controls usable: no precision jump on a moving part with no ledge, UI clear of the thumbstick and jump zones |
| juice | 1 | sound and/or particles on checkpoint, death and finish |

## Required screenshots (viewport-moment, as in game-dev-visual-qa; 6 base + extras)

desktop-spawn, phone-spawn, desktop-action, phone-action, desktop-effect, phone-effect, desktop-zone2, desktop-zone3, desktop-finish

## Scan points (the placement scan must contain models whose path matches)

| id | pattern | min | meaning |
|---|---|---|---|
| spawn | `(?i)spawn` | 1 | a Spawn model |
| checkpoints | `(?i)checkpoint` | 5 | 5 or more checkpoints (24 stages / 4 = 6) |
| hazards | `(?i)hazard` | 6 | 6 or more hazard models |
| platforms | `(?i)platform` | 20 | 20 or more platform/stage models |
| finish | `(?i)finish` | 1 | a Finish model |

## Scoring rubric (independent critic, 1-10 per item, evidence text per item; 3 = clearly failing, 7 = pass, 9 = front-page quality)

**B1 Core loop works start to finish**
- 3: cannot reach the finish, or a stage is impossible or the checkpoint does not hold
- 7: a tester completes all 24 stages, dies and respawns correctly, rejoin keeps progress
- 9: as 7 plus no console errors in a full run and a stranger finishes it without being told how

**B2 Level design and difficulty curve**
- 3: same jump repeated, sudden spikes, unfair blind jumps
- 7: each zone introduces one new mechanic and then combines it; gradual ramp; hazards telegraphed
- 9: as 7 plus a memorable set piece per zone and optional risk/reward routes

**B3 Visual identity**
- 3: grey blocks, default baseplate look, one flat colour
- 7: 3 clearly distinct zones with their own palette, materials, props and lighting
- 9: could sit beside front-page obbies; hero hazards are multi-part models

**B4 Game feel and feedback**
- 3: silent, no reaction on death/checkpoint/finish
- 7: sound + particle or tween on checkpoint, death and finish; HUD updates animate
- 9: as 7 plus camera/UI reaction and consistent audio mix

**B5 Robustness**
- 3: errors in output, progress lost, can exploit by skipping stages
- 7: no errors in a full run; DataStore failure handled; cannot skip stages by falling out of the map
- 9: as 7 plus anti-skip server check and a test showing rejoin/shutdown save

**B6 Mobile fitness**
- 3: UI overlaps controls, tiny text, jumps need keyboard precision
- 7: phone screenshots clean, text >= 14 px, jump sizes forgiving
- 9: as 7 plus verified in a phone-size capture with the Roblox top bar and chat clear

**B7 Code quality and safety**
- 3: everything in one script, magic numbers, no pcall around DataStore
- 7: modular server/client split, constants named, strict Luau, pcall everywhere data/network
- 9: as 7 plus tests or a verification script and clean selene/stylua

## benchmark-scores.json template

```json
{
 "spec": "obby",
 "scorer": "critic",
 "features": {
  "stages": 0,
  "checkpoints": 0,
  "hazards": 0,
  "moving": 0,
  "hud": 0,
  "save": 0,
  "finish": 0,
  "curve": 0,
  "mobile": 0,
  "juice": 0
 },
 "rubric": {
  "B1": 0,
  "B2": 0,
  "B3": 0,
  "B4": 0,
  "B5": 0,
  "B6": 0,
  "B7": 0
 },
 "evidence": {
  "B1": "what you saw, with file names",
  "B2": "what you saw, with file names",
  "B3": "what you saw, with file names",
  "B4": "what you saw, with file names",
  "B5": "what you saw, with file names",
  "B6": "what you saw, with file names",
  "B7": "what you saw, with file names"
 }
}
```

Spec gate = mean of: features (weighted coverage x 10), rubric mean, screenshots found / required x 10, scan points met / total x 10. Pass needs every part >= 7 and all features at 1.
