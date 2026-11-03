---
title: "Designing Season Passes with Dspav and BreakfastCandy"
url: https://youtu.be/k2gbQI-ggB4
creator: Roblox Creators
official: true
advice_density: high
date: 2021-09-16
views: 7474
transcript: manual-subs
confidence: high
tags: [roblox, mustwatch, youtube-learn]
---

# Designing Season Passes with Dspav and BreakfastCandy

[Watch](https://youtu.be/k2gbQI-ggB4) | MustWatch | 7,474 views | 2021-09-16

## Summary
Roblox Level Up workshop by Dan Spaventa (Roblox Game Insights) and Erin (BreakfastCandy) on designing and balancing a season pass system. Covers what season passes are, design doc sections, a spreadsheet balancing workflow (goals/assumptions/constants, player profiles, VLOOKUP-driven difficulty, curve-based pacing, mission time budgeting, weighted-average XP). Mostly a spreadsheet tutorial.

## Tips
- [1:11](https://youtu.be/k2gbQI-ggB4?t=71) **[[core-loops-and-game-design]]** Build season passes as a meta layer over existing systems; players do the normal game to earn pass XP, so little new content is needed.
- [3:14](https://youtu.be/k2gbQI-ggB4?t=194) **[[development-process-and-speed]]** Season passes let you frontload content so the team has time to build the next pass instead of a weekly content rat race.
- [5:19](https://youtu.be/k2gbQI-ggB4?t=319) **[[first-session-onboarding]]** Let players claim tier rewards manually from the pass UI rather than auto-granting; it keeps them aware of the system and shows what they got and why.
- [6:00](https://youtu.be/k2gbQI-ggB4?t=360) **[[monetisation-gamepasses]]** When a player buys the premium pass, grant rewards for all already-completed tiers so buying late is not penalised.
- [7:23](https://youtu.be/k2gbQI-ggB4?t=443) **[[monetisation-gamepasses]]** Put a special high-visibility reward on the final tier of free and premium tracks to motivate players to finish the season.
- [8:20](https://youtu.be/k2gbQI-ggB4?t=500) **[[development-process-and-speed]]** Write a feature design doc with overview, goals, UI preview, systems rules, examples, asset requests and future updates before building.
- [14:58](https://youtu.be/k2gbQI-ggB4?t=898) **[[updates-live-ops]]** Log future-update ideas in the design doc and plan to refresh new systems over a month or year, not just one release.
- [22:33](https://youtu.be/k2gbQI-ggB4?t=1353) **[[monetisation-gamepasses]]** Model separate progression paces for paying and free players; premium adds a mission slot, so track their completion rates separately.
- [17:07](https://youtu.be/k2gbQI-ggB4?t=1027) **[[core-loops-and-game-design]]** Launch difficulty slightly harder than target and ease it later; players dislike a sudden spike in difficulty after a fixed pace.
- [36:13](https://youtu.be/k2gbQI-ggB4?t=2173) **[[analytics-metrics]]** Assume players are active only about 75% of logged-in session time (and that paying players are more engaged); tune from real analytics after first season.
- [49:03](https://youtu.be/k2gbQI-ggB4?t=2943) **[[analytics-metrics]]** Instrument analytics in your game; use percentile player profiles (P30 to P100) for session length and sessions per day, split by PC and mobile.
- [31:29](https://youtu.be/k2gbQI-ggB4?t=1889) **[[core-loops-and-game-design]]** Plan for missions to be locked and released per day so players cannot burn through the whole season on day one, which protects retention.
- [37:11](https://youtu.be/k2gbQI-ggB4?t=2231) **[[core-loops-and-game-design]]** Use a non-linear XP curve so early tiers feel rewarding quickly and later tiers feel more earned, instead of monotonous linear grind.
- [39:36](https://youtu.be/k2gbQI-ggB4?t=2376) **[[development-process-and-speed]]** Keep XP values as flavor; balance by player time spent per mission, since the number of missions drives effort, not the XP number.
- [52:32](https://youtu.be/k2gbQI-ggB4?t=3152) **[[core-loops-and-game-design]]** Budget only a share of daily playtime (e.g. 25-75%) for the season pass so it does not replace socialising and other systems.
- [1:10:16](https://youtu.be/k2gbQI-ggB4?t=4216) **[[common-mistakes]]** Do not let players complete all content on day one; pace missions per day, a common season pass mistake.
- [1:01:11](https://youtu.be/k2gbQI-ggB4?t=3671) **[[common-mistakes]]** Do not assume players play the full season duration; compute days played per week from player profile data first.
- [1:04:48](https://youtu.be/k2gbQI-ggB4?t=3888) **[[common-mistakes]]** Do not round intermediate values in balance formulas; round only the final result to avoid compounding error.
- [38:15](https://youtu.be/k2gbQI-ggB4?t=2295) **[[analytics-metrics]]** After the first season, use completion data (tiers reached, percent finishing, average dailies completed) to rebalance the next season.
- [1:19:10](https://youtu.be/k2gbQI-ggB4?t=4750) **[[development-process-and-speed]]** Balance in a spreadsheet first, with constants and assumptions tabs referenced by formulas, then export values to the game and keep them in sync.
- [1:34:20](https://youtu.be/k2gbQI-ggB4?t=5660) **[[analytics-metrics]]** Use A/B tests to tailor mission difficulty per player segment if resources allow, but watch for player outrage when segments see unequal tasks.
- [1:59:59](https://youtu.be/k2gbQI-ggB4?t=7199) **[[core-loops-and-game-design]]** Weight mission rewards by their frequency using SUMPRODUCT to get a realistic average XP per daily.
- [1:48:27](https://youtu.be/k2gbQI-ggB4?t=6507) **[[development-process-and-speed]]** Treat the balance sheet as a first pass; playtest, collect player feedback, then iterate the tuning.
- [1:36:22](https://youtu.be/k2gbQI-ggB4?t=5782) **[[mindset-and-strategy]]** Expect the first balance to be wrong; balancing is about 50% math and 50% iteration with live players.

## Numbers
- [1:10](https://youtu.be/k2gbQI-ggB4?t=70) Premium pass price (Jailbreak example): **about 300 Robux** (Jailbreak season pass premium track cost cited by Dan)
- [1:53](https://youtu.be/k2gbQI-ggB4?t=113) Season pass tiers in example: **10 tiers** (Jailbreak example and workshop model use ten tiers)
- [9:14](https://youtu.be/k2gbQI-ggB4?t=554) Season duration in example: **30 days** (Workshop balances a 30-day season)
- [24:38](https://youtu.be/k2gbQI-ggB4?t=1478) Missions per day: **Free 2, premium 3** (Premium adds one daily mission)
- [35:33](https://youtu.be/k2gbQI-ggB4?t=2133) Average mission completion assumption: **75% of available missions** (Pizza-break assumption, players active about 75% of logged-in time)
- [46:58](https://youtu.be/k2gbQI-ggB4?t=2818) Observed activity efficiency: **70-80%** (Presenter's observed range for target group)
- [52:27](https://youtu.be/k2gbQI-ggB4?t=3147) PC vs mobile P75 sessions: **PC 38 min, 5 sessions/day; mobile 21 min, 6 sessions/day** (Example player profile data, simulated averages)
- [1:23:23](https://youtu.be/k2gbQI-ggB4?t=5003) Mobile share of Roblox players: **about 75%** (Stated by Dan as justification for modelling mobile P75 user)
- [1:31:49](https://youtu.be/k2gbQI-ggB4?t=5509) Total missions to complete season (payer, P75 mobile): **about 58** (Output of difficulty formula for example season)
- [1:47:46](https://youtu.be/k2gbQI-ggB4?t=6466) Days per tier: **tier 1 to 2 about 1 day; tier 9 to 10 about 6.2 days** (Pacing output from example curve)

## Games
- **Jailbreak** [1:10](https://youtu.be/k2gbQI-ggB4?t=70): Season pass with free and premium tracks, ten tiers, daily quests like capturing criminals or completing heists, premium around 300 Robux.

## Tools
Google Sheets, Microsoft Excel

## He points to
- Level Up workshop series (Roblox)
- Dan's earlier workshop on game expansions
- Dan's earlier economy design talks

## Quotes
- [1:11](https://youtu.be/k2gbQI-ggB4?t=71) "A season pass is a feature that runs for a set duration of time... it facilitates that core loop."
- [13:39](https://youtu.be/k2gbQI-ggB4?t=819) "If your players can't find it, if they don't know where it lives in the UI, they're not going to engage with it. So surfacing is really important."
- [1:17:07](https://youtu.be/k2gbQI-ggB4?t=4627) "It's always easier to make a feature easier over the span of it actually being live, than more difficult."
- [43:01](https://youtu.be/k2gbQI-ggB4?t=2581) "For me as an economy designer, the only thing that matters is the amount of effort, a.k.a. time that goes into a player completing a feature."

## Topics
[[analytics-metrics]] [[common-mistakes]] [[core-loops-and-game-design]] [[development-process-and-speed]] [[first-session-onboarding]] [[mindset-and-strategy]] [[monetisation-gamepasses]] [[updates-live-ops]]

Back to [[MustWatch - How to make successful Roblox games]]
