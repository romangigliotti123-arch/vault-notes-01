---
title: "Docs: characters / character-controller-library / quick-start"
url: https://create.roblox.com/docs/characters/character-controller-library/quick-start.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: characters / character-controller-library / quick-start

[Open](https://create.roblox.com/docs/characters/character-controller-library/quick-start.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs quick start for the Character Controller Library (CCL), an opt-in beta. Covers enabling it in Avatar Settings, configuring per-ability attributes (Running, Jumping, Climbing, etc.), and tuning controllers (GroundController, AirController, ClimbController, SwimController) via server scripts in ServerScriptService.

## Tips
- [page](https://create.roblox.com/docs/characters/character-controller-library/quick-start) **[[roblox-platform-changes]]** CCL is opt-in: enable File > Beta Features > AvatarAbilities Character Controller Library, then pick it under Avatar Settings > Movement > Abilities.
- [page](https://create.roblox.com/docs/characters/character-controller-library/quick-start) **[[common-mistakes]]** Do not disable Running; characters then cannot move along the ground. Keep Getting Up enabled whenever Falling Down is enabled, or characters trip and never recover.
- [page](https://create.roblox.com/docs/characters/character-controller-library/quick-start) **[[scripting-and-performance]]** Configure abilities via a server Script in ServerScriptService using AvatarAbilities.getAbilityConfigurationForCharacter(), since the Abilities folder contents vary with which abilities are enabled.
- [page](https://create.roblox.com/docs/characters/character-controller-library/quick-start) **[[scripting-and-performance]]** Wait for the ability configuration and ControllerManager to exist before editing controllers; the example uses timeouts of 10 seconds while polling with task.wait().
- [page](https://create.roblox.com/docs/characters/character-controller-library/quick-start) **[[core-loops-and-game-design]]** Tune movement feel by scaling GroundController.MoveSpeedFactor and TurnSpeedFactor, and set AccelerationTime (e.g. 0.2s) and DecelerationTime (e.g. 0.4s) for slight easing.
- [page](https://create.roblox.com/docs/characters/character-controller-library/quick-start) **[[client-server-and-remotes]]** Apply movement and ability changes from a server script so they apply to all characters consistently, handling both existing players and PlayerAdded with CharacterAdded.

## Numbers
- [page](https://create.roblox.com/docs/characters/character-controller-library/quick-start) Running SpeedMultiplier example: **2x (doubles ground move speed in sample script)**
- [page](https://create.roblox.com/docs/characters/character-controller-library/quick-start) Ground AccelerationTime example: **0.2 seconds**
- [page](https://create.roblox.com/docs/characters/character-controller-library/quick-start) Ground DecelerationTime example: **0.4 seconds**
- [page](https://create.roblox.com/docs/characters/character-controller-library/quick-start) Ability/controller wait timeout in sample: **10 seconds**

## Tools
Roblox Studio, Character Controller Library (CCL) beta, AvatarAbilities module, Luau

## He points to
- Custom abilities documentation (Roblox docs)

## Topics
[[client-server-and-remotes]] [[common-mistakes]] [[core-loops-and-game-design]] [[roblox-platform-changes]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
