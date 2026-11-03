---
title: "Docs: tutorials / first-experience"
url: https://create.roblox.com/docs/tutorials/first-experience.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / first-experience

[Open](https://create.roblox.com/docs/tutorials/first-experience.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs tutorial walking a new creator through building a first game in Studio: using the Baseplate template, importing a catapult asset pack from the Creator Store, customizing parts, organizing scripts into container services (ReplicatedStorage, ServerScriptService), tuning projectile materials for mass, and publishing via the Creator Dashboard.

## Tips
- [page](https://create.roblox.com/docs/tutorials/first-experience) **[[first-session-onboarding]]** Start from the Baseplate template for a first game; it provides a SpawnLocation and a 4x4 grid baseplate aligned to studs for positioning objects.
- [page](https://create.roblox.com/docs/tutorials/first-experience) **[[scripting-and-performance]]** Place scripts in the correct container service: Workspace renders, ReplicatedStorage is shared with clients, ServerScriptService is server-only. Wrong placement can break gameplay.
- [page](https://create.roblox.com/docs/tutorials/first-experience) **[[client-server-and-remotes]]** Set a Script's RunContext deliberately (Legacy, Server, or Client) since it overrides parent-container behavior; Legacy is the default.
- [page](https://create.roblox.com/docs/tutorials/first-experience) **[[scripting-and-performance]]** Put shared gameplay logic that the UI needs in ReplicatedStorage, and put logic that launches or resets objects in ServerScriptService.
- [page](https://create.roblox.com/docs/tutorials/first-experience) **[[testing-debugging-and-qa]]** Playtest after each structural change (moving scripts, editing properties) to verify behavior before moving on.
- [page](https://create.roblox.com/docs/tutorials/first-experience) **[[development-process-and-speed]]** Build with a small, scoped first project and ship it; the tutorial's target is a playable game with five projectiles, not a full product.
- [page](https://create.roblox.com/docs/tutorials/first-experience) **[[analytics-metrics]]** Use the Creator Dashboard analytics for player activity and retention to decide which iterations to make after publishing.
- [page](https://create.roblox.com/docs/tutorials/first-experience) **[[updates-live-ops]]** Republish updates to the live game with one click; changes become available immediately on the platform.
- [page](https://create.roblox.com/docs/tutorials/first-experience) **[[localization-and-international]]** Enable automatic translation via localization features in the Creator Dashboard to reach a global, multi-language audience.
- [page](https://create.roblox.com/docs/tutorials/first-experience) **[[cross-platform-and-console]]** Enable every device you want players to use (phones, computers, tablets, consoles, VR) in the Devices section at publish time.
- [page](https://create.roblox.com/docs/tutorials/first-experience) **[[monetisation-gamepasses]]** Configure in-game purchases and immersive ads from the Creator Dashboard monetization features once the game is published.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/first-experience) Stud length: **1 stud ≈ 28 cm** (Studio's base unit of length, per Roblox Units.)
- [page](https://create.roblox.com/docs/tutorials/first-experience) Projectiles in tutorial: **5 projectiles / 3 ball part projectiles** (Tutorial launches five projectiles; asset pack includes three ball projectiles.)

## Tools
Roblox Studio, Creator Store, Toolbox, Creator Dashboard, Explorer window, Properties window

## He points to
- Roblox Units
- Materials - Default Physical Properties
- Creator Store
- Open Cloud overview
- Core curriculum

## Topics
[[analytics-metrics]] [[client-server-and-remotes]] [[cross-platform-and-console]] [[development-process-and-speed]] [[first-session-onboarding]] [[localization-and-international]] [[monetisation-gamepasses]] [[scripting-and-performance]] [[testing-debugging-and-qa]] [[updates-live-ops]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
