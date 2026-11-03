---
title: "Docs: characters / character-controller-library / custom-abilities"
url: https://create.roblox.com/docs/characters/character-controller-library/custom-abilities.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: characters / character-controller-library / custom-abilities

[Open](https://create.roblox.com/docs/characters/character-controller-library/custom-abilities.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Docs page showing how to add a custom Dash ability using the Character Controller Library (CCL): enable the beta, define an AbilityDefinition with StartsWhen/RunsWhile/TimedLabels, register it server-side per character, and apply an impulse in OnStart.

## Tips
- [page](https://create.roblox.com/docs/characters/character-controller-library/custom-abilities) **[[development-process-and-speed]]** Enable the CCL via File > Beta Features > AvatarAbilities Character Controller Library, then toggle abilities in Avatar Settings > Movement > Abilities.
- [page](https://create.roblox.com/docs/characters/character-controller-library/custom-abilities) **[[core-loops-and-game-design]]** Don't disable Running in CCL; doing so stops characters moving on the ground. Keep Getting Up enabled whenever Falling Down is enabled, or characters trip and never recover.
- [page](https://create.roblox.com/docs/characters/character-controller-library/custom-abilities) **[[combat-and-gameplay-systems]]** Give each ability a unique Name; registering two abilities with the same Name throws an error. Share a label across similar abilities for coordination.
- [page](https://create.roblox.com/docs/characters/character-controller-library/custom-abilities) **[[code-architecture-and-frameworks]]** Abilities should never call each other; coordinate by broadcasting and testing Labels (world mask), using TimedLabels for cooldowns and active windows.
- [page](https://create.roblox.com/docs/characters/character-controller-library/custom-abilities) **[[client-server-and-remotes]]** Register abilities on the server, but keep ability callbacks deterministic since they run in both predicted client and authoritative server simulations.
- [page](https://create.roblox.com/docs/characters/character-controller-library/custom-abilities) **[[combat-and-gameplay-systems]]** Use RunsWhile only for world conditions; never put the input into RunsWhile (it throws an error). Use Input.Mode or Input.OutlivesInputWhile for input-driven timing.
- [page](https://create.roblox.com/docs/characters/character-controller-library/custom-abilities) **[[ui-ux-design]]** On mobile, action slots 1-7 map to on-screen buttons; pick slots accordingly when binding abilities for touch players.

## Numbers
- [page](https://create.roblox.com/docs/characters/character-controller-library/custom-abilities) Dash active window: **0.2 seconds (DashWindow TimedLabel)**
- [page](https://create.roblox.com/docs/characters/character-controller-library/custom-abilities) Dash cooldown: **1.0 second (DashCooldown TimedLabel)**
- [page](https://create.roblox.com/docs/characters/character-controller-library/custom-abilities) Dash impulse: **LookVector * 80 * AssemblyMass**
- [page](https://create.roblox.com/docs/characters/character-controller-library/custom-abilities) Mobile on-screen action slots: **Slots 1-7**
- [page](https://create.roblox.com/docs/characters/character-controller-library/custom-abilities) Keyboard/mouse slot count: **Slots 1-11 have default bindings; slot 5 = MouseLeftButton**

## Tools
Roblox Studio, AvatarAbilities / Character Controller Library (CCL)

## He points to
- @rbx/AvatarAbilities

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[combat-and-gameplay-systems]] [[core-loops-and-game-design]] [[development-process-and-speed]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
