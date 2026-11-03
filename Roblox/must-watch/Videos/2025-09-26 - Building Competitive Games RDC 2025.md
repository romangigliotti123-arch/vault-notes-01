---
title: "Building Competitive Games | RDC 2025"
url: https://youtu.be/V7MKrGggOOA
creator: Roblox
official: true
advice_density: medium
date: 2025-09-26
views: 7594
transcript: auto-captions
confidence: high
tags: [roblox, mustwatch, youtube-learn]
---

# Building Competitive Games | RDC 2025

[Watch](https://youtu.be/V7MKrGggOOA) | MustWatch | 7,594 views | 2025-09-26

## Summary
Roblox RDC 2025 talk by Owen, Brian and Andreas on making competitive games easier. Covers custom matchmaking signals (round-based and ELO skill matching, with closed-beta case-study lifts) and server authority with latency compensation (prediction, rollback and resimulation) to stop client-side cheats and enable better physics. Mostly platform announcements in closed beta or early access.

## Tips
- [3:46](https://youtu.be/V7MKrGggOOA?t=226) **[[analytics-metrics]]** Test matchmaking configs on a subset of players with the experimentation platform, measuring retention and play time before full rollout.
- [6:23](https://youtu.be/V7MKrGggOOA?t=383) **[[core-loops-and-game-design]]** In round-based games, use a signal that prioritises servers where a round starts soon so late joiners don't wait in lobbies (one puzzle game saw +7% session time).
- [7:33](https://youtu.be/V7MKrGggOOA?t=453) **[[core-loops-and-game-design]]** For skill-matched games, store ELO as a player attribute or in a data store and use a proximity signal to match similar-skill players.
- [9:34](https://youtu.be/V7MKrGggOOA?t=574) **[[common-mistakes]]** Don't rely on custom cheat detection alone; cheat-vs-defence cycles never end. Enable server authority so authority-based cheats fail regardless of method.
- [28:27](https://youtu.be/V7MKrGggOOA?t=1707) **[[scripting-and-performance]]** Enable server authority in workspace properties to get latency compensation for avatars and nearby parts with no custom code.
- [30:42](https://youtu.be/V7MKrGggOOA?t=1842) **[[scripting-and-performance]]** Keep part prediction on auto mode; set prediction on only for key objects like balls, since predicting too many parts costs frame rate.
- [31:21](https://youtu.be/V7MKrGggOOA?t=1881) **[[scripting-and-performance]]** Put core game logic in the new fixed heartbeat hook, which runs at a fixed rate and re-runs during rollback.
- [34:46](https://youtu.be/V7MKrGggOOA?t=2086) **[[scripting-and-performance]]** Store rollback-sensitive state such as scores in attributes, not Luau variables, because attributes roll back on misprediction.
- [33:38](https://youtu.be/V7MKrGggOOA?t=2018) **[[scripting-and-performance]]** Validate all client inputs on the server even with server authority, since clients can still send arbitrary values.
- [1:36](https://youtu.be/V7MKrGggOOA?t=96) **[[common-mistakes]]** Avoid one-sided matches; getting stomped by pros is a bad onboarding experience, so use matchmaking to balance players.
- [0:42](https://youtu.be/V7MKrGggOOA?t=42) **[[building-art-and-assets]]** Use avatar settings such as uniform collision boxes and consistent scaling to keep competitive play level without stripping player identity.

## Numbers
- [4:27](https://youtu.be/V7MKrGggOOA?t=267) Medium ping decrease: **18% (Deepwoken, latency signal weight, closed beta)** (Deepwoken raised latency weight in custom matchmaking)
- [4:27](https://youtu.be/V7MKrGggOOA?t=267) Play time increase: **3% statistically significant (Brookhaven A/B test)** (Language signal weight boosted in matchmaking config)
- [6:23](https://youtu.be/V7MKrGggOOA?t=383) Average session time increase: **7% (round-based puzzle game)** (New-round-starting-soon signal, closed beta)
- [9:34](https://youtu.be/V7MKrGggOOA?t=574) Decrease in playtime exposed to untrusted clients: **over 80% in three months** (After switching from manual ban waves to automatic banning)

## Games
- **Deepwoken**: Raised latency signal weight in custom matchmaking; cut medium ping by 18% in closed beta.
- **Brookhaven**: A/B tested a matchmaking config boosting language signal; got 3% significant play time increase.
- **Ultimate Paintball**: First Roblox experience to reach 1 million visits; PvP mechanics drove its success.

## Tools
Custom matchmaking signals (closed beta, open to all creators), Experimentation platform (A/B testing for matchmaking), Server authority with latency compensation (early access), Fixed heartbeat (RunService hook), Input action system, Matchmaking services API

## He points to
- Roblox developer forum server authority early access announcement

## Quotes
- [9:34](https://youtu.be/V7MKrGggOOA?t=574) "Playing with cheaters is no fun and it's something we're determined to fix."

## On screen
Matchmaking slide shows Deepwoken and Brookhaven logos at 4:28. At 6:29 a Create Custom Signal dialog lists signal weights (Occupancy, Age, Latency, Friends, Device Type, Voice Chat, Play History, New Round Starting Soon). At 19:18 a prediction demo shows Latency, Server authority and Prediction toggles.

## Topics
[[analytics-metrics]] [[building-art-and-assets]] [[common-mistakes]] [[core-loops-and-game-design]] [[scripting-and-performance]]

Back to [[MustWatch - How to make successful Roblox games]]
