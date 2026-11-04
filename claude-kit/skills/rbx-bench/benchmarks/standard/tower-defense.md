# Standard test game 3: tower defense

Spec id `tower-defense`, version 1, target stage `prototype`. Suggested budget: 150 minutes, 250 turns (record the real numbers in benchmark-run.json).

## Fixed prompt (give it verbatim, change nothing, in every version you compare)

> Make a Roblox tower-defense game for ages 8 to 14, one map. Enemies follow a waypoint path from a spawner to the player base. 10 waves with at least 3 enemy types (fast, tank, flying or armoured). 3 tower types (single target, area, slow) that the player buys with coins earned from kills and places on a grid of valid tower pads (snapped, no placing on the path or on another tower), upgrades once each, and can sell. Base health, wave counter and coin HUD, a start-wave button, win screen after wave 10 and a loss screen when base health reaches 0, then restart. It must be playable on phone and desktop. Name the models so a scan can find them: Spawn, Base, Waypoint_<n>, TowerPad_<n>, Tower_<kind>_<n>, Enemy_<kind>. No purchases, no pay-to-win. Report when it is playable; do not call it done unless the gates pass.

## Target features (the critic scores each 0, 0.5 or 1 with evidence)

| id | weight | feature |
|---|---|---|
| path | 2 | enemies follow waypoints from spawner to base without getting stuck or cutting corners |
| waves | 2 | 10 waves, scaling difficulty, 3 or more enemy types with different behaviour |
| towers | 2 | 3 tower types with different roles (single, area, slow) that actually do what they say |
| placement | 2 | towers snap to valid pads, cannot be placed on path or on another tower, rotate to face the path |
| economy | 2 | coins from kills, buy/upgrade/sell, costs balanced so all 3 types are used |
| hud | 1 | base health, wave counter, coins, start-wave button, readable on phone |
| winloss | 2 | win after wave 10, loss at 0 base health, restart works |
| feedback | 1 | tower fire effects, enemy hit/death feedback, damage numbers or health bars |
| server | 2 | enemy and tower logic runs on the server; placement requests validated |
| perf | 1 | no frame-rate collapse at the largest wave (enemy count capped, pooling or cleanup) |

## Required screenshots (viewport-moment, as in rbx-visual; 6 base + extras)

desktop-spawn, phone-spawn, desktop-action, phone-action, desktop-effect, phone-effect, desktop-wave, phone-wave, desktop-placement, desktop-gameover

## Scan points (the placement scan must contain models whose path matches)

| id | pattern | min | meaning |
|---|---|---|---|
| spawn | `(?i)spawn` | 1 | an enemy Spawn model |
| base | `(?i)base` | 1 | a Base model |
| waypoints | `(?i)waypoint` | 6 | 6 or more waypoints |
| pads | `(?i)towerpad` | 8 | 8 or more tower pads |
| towers | `(?i)tower_` | 3 | 3 or more placed towers in the scan (place at least one of each type before scanning) |

## Scoring rubric (independent critic, 1-10 per item, evidence text per item; 3 = clearly failing, 7 = pass, 9 = front-page quality)

**B1 Core loop works**
- 3: enemies stuck, towers do nothing, waves cannot be completed
- 7: all 10 waves complete, win and loss screens work, restart works
- 9: as 7 plus no console errors across a full run

**B2 Balance and strategy**
- 3: one tower type wins everything or the game is unwinnable
- 7: each tower type has a role; mixing is needed from wave 6; winnable but not trivial
- 9: as 7 plus a simulation of the economy and a meaningful upgrade choice

**B3 Placement quality**
- 3: towers float, sink, overlap pads or face away from the path
- 7: placement gate passes: grounded, upright, facing the path, snapped, no overlap
- 9: as 7 plus placement preview/ghost with valid/invalid colour

**B4 Visual identity**
- 3: grey blocks, no map theme
- 7: map has a theme with path, pads and props distinct; towers and enemies are multi-part models
- 9: could sit beside front-page tower defense games

**B5 Feedback and juice**
- 3: no shot effects, no hit reaction
- 7: projectiles/beams, hit flash, death effect, wave-start banner, sounds
- 9: as 7 plus camera shake on base hit and satisfying kill chains

**B6 UI and mobile fitness**
- 3: controls overlap, buttons tiny, tower menu unusable on phone
- 7: clean at phone size, tap to select pad/tower, text >= 14 px
- 9: as 7 plus drag-to-place with a thumb-safe layout

**B7 Robustness and performance**
- 3: errors, leaks, FPS collapse at wave 10
- 7: server-authoritative logic, validated placement remotes, enemy cleanup, stable FPS
- 9: as 7 plus pooling and a stress test with the cap raised

## benchmark-scores.json template

```json
{
 "spec": "tower-defense",
 "scorer": "critic",
 "features": {
  "path": 0,
  "waves": 0,
  "towers": 0,
  "placement": 0,
  "economy": 0,
  "hud": 0,
  "winloss": 0,
  "feedback": 0,
  "server": 0,
  "perf": 0
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
