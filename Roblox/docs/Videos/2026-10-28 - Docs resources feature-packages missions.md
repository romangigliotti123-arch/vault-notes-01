---
title: "Docs: resources / feature-packages / missions"
url: https://create.roblox.com/docs/resources/feature-packages/missions.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / feature-packages / missions

[Open](https://create.roblox.com/docs/resources/feature-packages/missions.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs for the Missions feature package (beta): defining missions with IDs, categories, tasks, unlock conditions, metadata; count vs timed tasks; server integration via Missions and CounterSystem calls; category repeat delays; UI customization.

## Tips
- [page](https://create.roblox.com/docs/resources/feature-packages/missions) **[[first-session-onboarding]]** Use missions to onboard new players into the game; the docs say this improves D1 retention.
- [page](https://create.roblox.com/docs/resources/feature-packages/missions) **[[retention-d1-d7]]** Add mid- to long-term missions and progression goals to target D7 and D30 retention.
- [page](https://create.roblox.com/docs/resources/feature-packages/missions) **[[core-loops-and-game-design]]** Reward players for interacting with the game's various systems to surface them and increase engagement.
- [page](https://create.roblox.com/docs/resources/feature-packages/missions) **[[core-loops-and-game-design]]** Give missions an empty tasks list to create instantly claimable rewards.
- [page](https://create.roblox.com/docs/resources/feature-packages/missions) **[[combat-and-gameplay-systems]]** Share one counterId across multiple tasks (e.g. a 'coins' counter) so they all track the same progress.
- [page](https://create.roblox.com/docs/resources/feature-packages/missions) **[[combat-and-gameplay-systems]]** Set continueFromCounter to true if a task should start from the player's existing counter total rather than zero.
- [page](https://create.roblox.com/docs/resources/feature-packages/missions) **[[updates-live-ops]]** Use category repeatDelaySeconds to reset all missions in a category on a timer for recurring dailies or weeklies.
- [page](https://create.roblox.com/docs/resources/feature-packages/missions) **[[ui-ux-design]]** Enable SingleTaskMode in Constants to show a progress bar on missions with only one task.
- [page](https://create.roblox.com/docs/resources/feature-packages/missions) **[[ui-ux-design]]** Keep the Missions UI object hierarchy intact; moving objects breaks the code that finds them unless you update MissionsUI.
- [page](https://create.roblox.com/docs/resources/feature-packages/missions) **[[client-server-and-remotes]]** Award rewards only in the server-side completion handler set via Missions.setCompletionHandler.
- [page](https://create.roblox.com/docs/resources/feature-packages/missions) **[[data-persistence]]** Counters are player-specific persistent storage, so mission progress persists across sessions.
- [page](https://create.roblox.com/docs/resources/feature-packages/missions) **[[ui-ux-design]]** Put translatable strings in FeaturePackagesCore TranslationStrings rather than hardcoding them.
- [page](https://create.roblox.com/docs/resources/feature-packages/missions) **[[core-loops-and-game-design]]** Set expireSeconds to fail stale missions, and expireCountOffline to decide whether offline time counts toward expiry.

## Numbers
- [page](https://create.roblox.com/docs/resources/feature-packages/missions) Retention targets named: **D1, D7, D30** (Docs cite these retention windows as mission design goals)
- [page](https://create.roblox.com/docs/resources/feature-packages/missions) Required mission fields: **3 (missionId, categoryId, tasks)** (Tasks list may be empty for immediately claimable missions)

## Tools
Missions feature package, Core feature package, CounterSystem, Creator Store / Toolbox, Roblox Studio

## He points to
- Introduction to Quest Design

## Topics
[[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[core-loops-and-game-design]] [[data-persistence]] [[first-session-onboarding]] [[retention-d1-d7]] [[ui-ux-design]] [[updates-live-ops]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
