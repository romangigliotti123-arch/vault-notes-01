---
title: "Docs: resources / feature-packages / season-passes"
url: https://create.roblox.com/docs/resources/feature-packages/season-passes.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / feature-packages / season-passes

[Open](https://create.roblox.com/docs/resources/feature-packages/season-passes.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page for the Season Passes feature package (beta). Covers getting the Core, Missions and Season Passes packages into Studio, wiring mission completion to season XP, configuring premium passes, tiers with free/premium rewards, season dates, reward-claim handlers, constants and UI components.

## Tips
- [page](https://create.roblox.com/docs/resources/feature-packages/season-passes) **[[development-process-and-speed]]** Treat the Season Passes package as beta: test balance and functionality thoroughly before publishing to your audience.
- [page](https://create.roblox.com/docs/resources/feature-packages/season-passes) **[[development-process-and-speed]]** Add the Core, Missions and Season Passes packages to your inventory and drag them into ReplicatedStorage; Missions is required even if you define no missions.
- [page](https://create.roblox.com/docs/resources/feature-packages/season-passes) **[[monetisation-gamepasses]]** Create the season pass as a gamepass with a unique asset ID and set it in the season's premiumTrack pricing.gamePassId field.
- [page](https://create.roblox.com/docs/resources/feature-packages/season-passes) **[[monetisation-gamepasses]]** Test pass purchases on a published game in the client; Studio does not mock pass purchasing.
- [page](https://create.roblox.com/docs/resources/feature-packages/season-passes) **[[core-loops-and-game-design]]** Feed mission completions into the season by calling SeasonPasses.addProgressToSeason(player, xp) from your mission completion handler.
- [page](https://create.roblox.com/docs/resources/feature-packages/season-passes) **[[core-loops-and-game-design]]** Give each tier an upperBoundXP threshold and both a freeReward and premiumReward so players see progression for free and paid tracks.
- [page](https://create.roblox.com/docs/resources/feature-packages/season-passes) **[[core-loops-and-game-design]]** Keep rewardId values numeric and increasing across tiers so tiers display in the order you define them.
- [page](https://create.roblox.com/docs/resources/feature-packages/season-passes) **[[client-server-and-remotes]]** Register a reward-claimed handler for every rewardId; it must return true only if the server actually granted the reward, otherwise false.
- [page](https://create.roblox.com/docs/resources/feature-packages/season-passes) **[[updates-live-ops]]** Set startUtc and endUtc for each season; the package uses them to drive the on-screen countdown and limited-time window.
- [page](https://create.roblox.com/docs/resources/feature-packages/season-passes) **[[ui-ux-design]]** Restyle package UI by editing colors, fonts and transparency, but do not move objects in the hierarchy without updating the code that finds them.
- [page](https://create.roblox.com/docs/resources/feature-packages/season-passes) **[[data-persistence]]** Enable Studio Access to API Services in Experience Settings > Security so the package can track purchases with data store calls.
- [page](https://create.roblox.com/docs/resources/feature-packages/season-passes) **[[building-art-and-assets]]** Add an icon asset ID to each mission reward in the Missions config so tier reward icons appear on screen.
- [page](https://create.roblox.com/docs/resources/feature-packages/season-passes) **[[ui-ux-design]]** Use the Season Passes Configs/Constants file to adjust sound asset IDs and purchase effect duration and particle colors.

## Numbers
- [page](https://create.roblox.com/docs/resources/feature-packages/season-passes) XP per mission in example: **100 XP** (Example addProgressToSeason calls award 100 XP per mission)
- [page](https://create.roblox.com/docs/resources/feature-packages/season-passes) Example tier threshold: **upperBoundXP = 100** (Single-tier example: free ice lance and premium blast shield)
- [page](https://create.roblox.com/docs/resources/feature-packages/season-passes) Example season length: **2024-10-01 to 2025-02-28 (about 5 months)** (Example season startUtc and endUtc at 17:00 UTC)
- [page](https://create.roblox.com/docs/resources/feature-packages/season-passes) Example handler delay: **task.wait(2)** (Placeholder delay in sample reward-claim handler)

## Tools
Roblox Studio, Toolbox / Creator Store, Missions feature package, Season Passes feature package, Core feature package

## He points to
- Season pass design (Roblox docs)
- Define missions (Roblox docs)

## Topics
[[building-art-and-assets]] [[client-server-and-remotes]] [[core-loops-and-game-design]] [[data-persistence]] [[development-process-and-speed]] [[monetisation-gamepasses]] [[ui-ux-design]] [[updates-live-ops]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
