---
title: "Docs: production / configs"
url: https://create.roblox.com/docs/production/configs.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / configs

[Open](https://create.roblox.com/docs/production/configs.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Hub docs for Experience configs: server-side key/value settings (string, number, boolean, JSON) that change live without republishing. Covers creating and staging configs, publish timing, conditional targeting by player attributes, Studio editing, history/restore, code access via ConfigService, snapshot refresh, error handling, and testing values.

## Tips
- [page](https://create.roblox.com/docs/production/configs) **[[core-loops-and-game-design]]** Use configs instead of hard-coded constants for boss health, XP gain, item prices so you can tune live without a new version.
- [page](https://create.roblox.com/docs/production/configs) **[[development-process-and-speed]]** Stage and test config changes in Studio before publishing to live players.
- [page](https://create.roblox.com/docs/production/configs) **[[playtesting-and-feedback]]** Use conditional configs with experiments to give different values to player segments and compare outcomes.
- [page](https://create.roblox.com/docs/production/configs) **[[retention-d1-d7]]** Target new players (e.g., first 0-30 days) with easier settings such as extra armor, using new vs returning or when-first-played attributes.
- [page](https://create.roblox.com/docs/production/configs) **[[updates-live-ops]]** Schedule timed content like seasonal events by switching config values at a set time.
- [page](https://create.roblox.com/docs/production/configs) **[[common-mistakes]]** Configs do nothing unless your code reads them; call GetValue in the code that uses the value.
- [page](https://create.roblox.com/docs/production/configs) **[[common-mistakes]]** Conditional values must match the default value's data type, and rule order is global; verify priority on the Conditions tab before publishing.
- [page](https://create.roblox.com/docs/production/configs) **[[scripting-and-performance]]** Call ConfigService only from server scripts; client calls error. Wrap GetConfigAsync in pcall with fallback values.
- [page](https://create.roblox.com/docs/production/configs) **[[scripting-and-performance]]** Snapshots don't auto-update; connect UpdateAvailable to Refresh and use GetValueChangedSignal to apply changes safely, e.g., between rounds in a shooter.
- [page](https://create.roblox.com/docs/production/configs) **[[development-process-and-speed]]** Use SetTestingValue to test a value on one server only; it does not affect other servers or live players.
- [page](https://create.roblox.com/docs/production/configs) **[[common-mistakes]]** Use GetConfigForPlayerAsync for targeted configs; GetConfigAsync does not apply targeting.

## Numbers
- [page](https://create.roblox.com/docs/production/configs) Active configs per experience: **up to 1,000** (Maximum active configs at any given time)
- [page](https://create.roblox.com/docs/production/configs) Publish propagation (Publish now): **~15 seconds to 1 minute** (Publish over 15 min gives a gradual rollout instead)
- [page](https://create.roblox.com/docs/production/configs) Config value size limit: **100,000 characters** (Applies to string and JSON types)
- [page](https://create.roblox.com/docs/production/configs) Conditions per game: **100** (Maximum conditions across the experience)
- [page](https://create.roblox.com/docs/production/configs) Conditions per config key: **20** (Maximum conditions for a single key)
- [page](https://create.roblox.com/docs/production/configs) Integer exactness limit: **±2^53** (Exact integer representation for number type)

## Tools
Creator Hub Configs page, Roblox Studio Configs widget, ConfigService, ConfigSnapshot

## He points to
- Add configs to your code
- Target configs to specific players

## Topics
[[common-mistakes]] [[core-loops-and-game-design]] [[development-process-and-speed]] [[playtesting-and-feedback]] [[retention-d1-d7]] [[scripting-and-performance]] [[updates-live-ops]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
