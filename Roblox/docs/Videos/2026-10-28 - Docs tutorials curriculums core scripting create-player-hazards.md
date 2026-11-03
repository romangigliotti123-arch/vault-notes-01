---
title: "Docs: tutorials / curriculums / core / scripting / create-player-hazards"
url: https://create.roblox.com/docs/tutorials/curriculums/core/scripting/create-player-hazards.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / curriculums / core / scripting / create-player-hazards

[Open](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/create-player-hazards.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial: creating an invisible, anchored hazard part over the water, a server Script (HazardService) that sets Humanoid.Health to 0 on Touched, and extending CoinService to reset coins on PlayerAdded/CharacterAdded/Died/PlayerRemoving, plus a playtest step.

## Tips
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/create-player-hazards) **[[core-loops-and-game-design]]** Make hazards visually obvious: keep the real water visible and make the invisible hazard part Transparency 1 so the water itself reads as the danger.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/create-player-hazards) **[[client-server-and-remotes]]** Put gameplay scripts like hazard handling in ServerScriptService so players cannot read or modify the logic.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/create-player-hazards) **[[scripting-and-performance]]** Loop through a dedicated Hazards folder with GetChildren and connect Touched once per part so new hazards are added by just placing them in the folder.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/create-player-hazards) **[[scripting-and-performance]]** Check that the touched part belongs to a player's character with Players:GetPlayerFromCharacter before acting on it.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/create-player-hazards) **[[scripting-and-performance]]** Run WaitForChild calls inside task.spawn so waiting for a Humanoid does not block the player-setup loop.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/create-player-hazards) **[[first-session-onboarding]]** Initialize players already in the server with GetPlayers() before connecting PlayerAdded, so early joiners are not missed.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/create-player-hazards) **[[data-persistence]]** Reset per-life state (e.g. coins) on Humanoid.Died and on PlayerRemoving so session values do not leak between respawns or sessions.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/create-player-hazards) **[[development-process-and-speed]]** Test hazards in Studio with Test > Play: collect items, fall in, and confirm respawn and state reset before moving on.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/create-player-hazards) **[[common-mistakes]]** Be aware that players can collect coins before PlayerAdded finishes initialising and get reset to zero; use scheduling or freeze the character until setup completes.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/create-player-hazards) Hazard part Size: **825, 1, 576** (Invisible hazard part covering water around island and platforms)
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/create-player-hazards) Hazard part CFrame.Position: **174, -6.5, 38** (Sample position matching the water height in the tutorial map)

## Tools
Roblox Studio, Explorer, Properties window, Luau

## He points to
- Roblox Creator Docs: Create player hazards tutorial

## Topics
[[client-server-and-remotes]] [[common-mistakes]] [[core-loops-and-game-design]] [[data-persistence]] [[development-process-and-speed]] [[first-session-onboarding]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
