---
title: "Docs: education / build-it-play-it-galactic-speedway / customize-and-share"
url: https://create.roblox.com/docs/education/build-it-play-it-galactic-speedway/customize-and-share.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: education / build-it-play-it-galactic-speedway / customize-and-share

[Open](https://create.roblox.com/docs/education/build-it-play-it-galactic-speedway/customize-and-share.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Final lesson of the Galactic Speedway tutorial: how to tune a driftspeeder's speed and steering by editing the Settings script (DefaultSpeed, BoostSpeed, BoostAmount, Steering), playtest the change, and give each speeder unique strengths/weaknesses.

## Tips
- [page](https://create.roblox.com/docs/education/build-it-play-it-galactic-speedway/customize-and-share) **[[core-loops-and-game-design]]** Give each vehicle distinct strengths and weaknesses (e.g., slower base speed with faster boost, or very fast but slow to turn) so multiple options feel unique.
- [page](https://create.roblox.com/docs/education/build-it-play-it-galactic-speedway/customize-and-share) **[[playtesting-and-feedback]]** After changing a tuning value, playtest and judge whether the speed fits the vehicle's design and feels exciting in a race.
- [page](https://create.roblox.com/docs/education/build-it-play-it-galactic-speedway/customize-and-share) **[[scripting-and-performance]]** Keep tunable values (speed, boost duration, steering) in a single Settings module table so they can be adjusted without touching core logic.
- [page](https://create.roblox.com/docs/education/build-it-play-it-galactic-speedway/customize-and-share) **[[development-process-and-speed]]** Use documented ranges on tuning values (DefaultSpeed 50-300, BoostSpeed max 400, Steering 1-10) as safe bounds when adjusting.

## Numbers
- [page](https://create.roblox.com/docs/education/build-it-play-it-galactic-speedway/customize-and-share) DefaultSpeed range: **50-300 studs/second** (Settings.DefaultSpeed, default 100)
- [page](https://create.roblox.com/docs/education/build-it-play-it-galactic-speedway/customize-and-share) BoostSpeed maximum: **400 studs/second** (Settings.BoostSpeed, default 200)
- [page](https://create.roblox.com/docs/education/build-it-play-it-galactic-speedway/customize-and-share) Steering range: **1-10** (Settings.Steering, default 5; higher turns faster)
- [page](https://create.roblox.com/docs/education/build-it-play-it-galactic-speedway/customize-and-share) BoostAmount: **10 seconds (default)** (Duration of boost in seconds)

## Games
- **Galactic Speedway**: Tutorial game: tune driftspeeder via Settings script; differentiate speeders by strengths and weaknesses.

## Tools
Roblox Studio, Explorer window, Luau scripts

## Topics
[[core-loops-and-game-design]] [[development-process-and-speed]] [[playtesting-and-feedback]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
