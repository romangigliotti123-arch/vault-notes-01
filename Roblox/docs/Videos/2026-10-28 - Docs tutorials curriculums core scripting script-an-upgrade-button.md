---
title: "Docs: tutorials / curriculums / core / scripting / script-an-upgrade-button"
url: https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-an-upgrade-button.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / curriculums / core / scripting / script-an-upgrade-button

[Open](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-an-upgrade-button.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial: adds an on-screen Upgrade Jump button that spends coins to raise Humanoid.JumpPower. Covers ScreenGui/TextButton setup, a RemoteFunction for client-to-server purchase requests, server-side validation of coins, PlayerData module storing Jump, and resetting jump power on respawn.

## Tips
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-an-upgrade-button) **[[client-server-and-remotes]]** Use a RemoteFunction instead of RemoteEvent when the client must know whether the server accepted the request; RemoteFunctions yield for a reply, RemoteEvents are one-way.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-an-upgrade-button) **[[anti-exploit-and-security]]** Validate every client request on the server, e.g. check the player has enough coins before granting an upgrade, to stop exploiters submitting false requests.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-an-upgrade-button) **[[client-server-and-remotes]]** Wrap client-side InvokeServer calls in pcall to handle errors or connection issues.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-an-upgrade-button) **[[client-server-and-remotes]]** Store shared objects (RemoteFunctions, GUIs) in ReplicatedStorage so both client and server can reference them.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-an-upgrade-button) **[[scripting-and-performance]]** Set RunContext to Client on scripts that only handle UI, to run them on the client and reduce network traffic.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-an-upgrade-button) **[[first-session-onboarding]]** Make the upgrade button visible in the bottom-right corner with a large TextSize (25) so players can find the purchase action easily.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-an-upgrade-button) **[[data-persistence]]** Keep player data in a central PlayerData module keyed by userId, with generic getValue/updateValue functions so new stats (like Jump) only need a key and default value.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-an-upgrade-button) **[[core-loops-and-game-design]]** Enable StarterPlayer CharacterUseJumpPower, otherwise JumpPower values are ignored and all characters jump at a fixed height.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-an-upgrade-button) **[[core-loops-and-game-design]]** Tune difficulty by adjusting coin pace: add coins if progress is slow, remove coins or place them in trickier spots if upgrades come too easily.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-an-upgrade-button) **[[development-process-and-speed]]** Playtest purchase flows both before and after collecting currency to confirm the upgrade is not granted without enough coins.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-an-upgrade-button) **[[combat-and-gameplay-systems]]** Reset per-character stats like JumpPower on CharacterAdded and clear stored data on PlayerRemoving to avoid carrying upgrades across respawns or leaks.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-an-upgrade-button) Upgrade cost: **5 coins per jump upgrade** (JUMP_COIN_COST in tutorial example)
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-an-upgrade-button) Jump power increment: **+30 per purchase** (JUMP_POWER_INCREMENT in tutorial example; can be lowered to lengthen game)
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-an-upgrade-button) TextButton TextSize: **25** (Upgrade Jump button text size in tutorial)

## Tools
Roblox Studio, ScreenGui, TextButton, RemoteFunction, PlayerData ModuleScript, Leaderboard module

## He points to
- Create player hazards (Roblox tutorial)

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[core-loops-and-game-design]] [[data-persistence]] [[development-process-and-speed]] [[first-session-onboarding]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
