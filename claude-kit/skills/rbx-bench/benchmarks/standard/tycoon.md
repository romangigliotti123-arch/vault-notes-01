# Standard test game 2: simulator/tycoon loop

Spec id `tycoon`, version 1, target stage `prototype`. Suggested budget: 120 minutes, 200 turns (record the real numbers in benchmark-run.json).

## Fixed prompt (give it verbatim, change nothing, in every version you compare)

> Make a Roblox click-and-collect simulator with tycoon upgrades for ages 8 to 14. Core loop: the player collects resources (click or walk-over nodes), sells them at a sell pad for coins, buys upgrades (more per click, bigger backpack, auto-collector), and can rebirth after reaching a coin goal for a permanent multiplier. A shop UI with at least 6 upgrades and clear prices, a coins/backpack/rebirth HUD, a leaderboard of coins, a daily reward, saved data (DataStore, pcall, session safe). Three areas unlock progressively. It must be playable on phone and desktop. Name the models so a scan can find them: Spawn, ResourceNode_<n>, SellPad, Shop, Area<n>_Gate, Collector_<n>. Hard rules: no pay-to-win, no paid randomness, no pressure timers, no real-money purchases in this test. Report when it is playable; do not call it done unless the gates pass.

## Target features (the critic scores each 0, 0.5 or 1 with evidence)

| id | weight | feature |
|---|---|---|
| collect | 2 | collecting resources works by click or touch with visible and audible feedback |
| sell | 2 | backpack fills, sell pad converts it to coins with a clear animation |
| shop | 2 | shop UI with 6 or more upgrades, prices, affordability state, purchase feedback, no overlap at phone size |
| auto | 1 | an auto-collector or helper that runs while the player does something else |
| rebirth | 2 | rebirth at a goal with a permanent multiplier and a clear explanation |
| areas | 2 | three areas that unlock progressively with gates and different resource values |
| save | 2 | coins, upgrades, rebirths saved with DataStore + pcall, server-authoritative economy |
| leaderboard | 1 | coins leaderboard visible in game |
| daily | 1 | daily reward with a streak display and no pressure timer |
| economy | 2 | progression pacing documented: time to first upgrade under 60 s, to first rebirth about 20-30 min; numbers from an economy simulation |
| security | 2 | all purchases and currency changes happen on the server; remotes validated |

## Required screenshots (viewport-moment, as in rbx-visual; 6 base + extras)

desktop-spawn, phone-spawn, desktop-action, phone-action, desktop-effect, phone-effect, desktop-shop, phone-shop, desktop-rebirth

## Scan points (the placement scan must contain models whose path matches)

| id | pattern | min | meaning |
|---|---|---|---|
| spawn | `(?i)spawn` | 1 | a Spawn model |
| nodes | `(?i)resourcenode` | 8 | 8 or more resource nodes |
| sell | `(?i)sellpad` | 1 | a SellPad |
| shop | `(?i)shop` | 1 | a Shop model |
| gates | `(?i)gate` | 2 | 2 or more area gates |
| collectors | `(?i)collector` | 1 | an auto-collector model |

## Scoring rubric (independent critic, 1-10 per item, evidence text per item; 3 = clearly failing, 7 = pass, 9 = front-page quality)

**B1 Core loop works and is fun for 5 minutes**
- 3: loop breaks, soft-locks, or nothing to do after 1 minute
- 7: collect, sell, upgrade, repeat works; a tester wants one more upgrade after 5 minutes
- 9: as 7 plus the first rebirth decision is exciting and clearly explained

**B2 Economy and pacing**
- 3: numbers arbitrary, one upgrade dominates, grind wall before minute 5
- 7: costs/gains follow a documented curve; first upgrade under 60 s; no dominant strategy
- 9: as 7 plus a simulation output and a catch-up mechanic

**B3 UI and shop clarity**
- 3: overlapping panels, unclear prices, tiny text
- 7: one component style, affordable/unaffordable states, purchase feedback, clean at phone size
- 9: as 7 plus polished open/close tweens and icons for every upgrade

**B4 Visual identity**
- 3: grey blocks and default look
- 7: three areas with distinct palette/lighting; hero objects are real models
- 9: could sit beside front-page simulators

**B5 Feedback and juice**
- 3: silent numbers
- 7: coin pop-ups, sell animation, sound for collect/sell/buy/rebirth
- 9: as 7 plus screen-space effects and a satisfying rebirth sequence

**B6 Robustness and security**
- 3: client can grant itself coins, errors in output, data lost on rejoin
- 7: server-authoritative, validated remotes, DataStore with pcall and retry, rejoin test passed
- 9: as 7 plus rate limits and shutdown save verified

**B7 Ethics and rules**
- 3: pay-to-win, paid randomness, pressure timers or stranger contact
- 7: none of the hard rules violated
- 9: as 7 plus kid-friendly onboarding and no dark patterns

## benchmark-scores.json template

```json
{
 "spec": "tycoon",
 "scorer": "critic",
 "features": {
  "collect": 0,
  "sell": 0,
  "shop": 0,
  "auto": 0,
  "rebirth": 0,
  "areas": 0,
  "save": 0,
  "leaderboard": 0,
  "daily": 0,
  "economy": 0,
  "security": 0
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
