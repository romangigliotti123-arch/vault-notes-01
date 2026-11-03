---
title: "Docs: characters / character-controller-library"
url: https://create.roblox.com/docs/characters/character-controller-library.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: characters / character-controller-library

[Open](https://create.roblox.com/docs/characters/character-controller-library.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page for the Character Controller Library (CCL), a beta opt-in framework where movement is defined by abilities, labels, conditions, conflicts, inputs, sensors and lifecycle callbacks instead of Humanoid states. Covers enabling, configuring and scripting abilities.

## Tips
- [page](https://create.roblox.com/docs/characters/character-controller-library) **[[development-process-and-speed]]** Enable CCL via File > Beta Features > AvatarAbilities Character Controller Library, then Avatar Settings > Movement > Abilities. It is opt-in during beta.
- [page](https://create.roblox.com/docs/characters/character-controller-library) **[[core-loops-and-game-design]]** Do not disable Running; doing so prevents characters from moving along the ground.
- [page](https://create.roblox.com/docs/characters/character-controller-library) **[[core-loops-and-game-design]]** If FallingDown is enabled, always keep GettingUp enabled; otherwise characters can trip but never get back up.
- [page](https://create.roblox.com/docs/characters/character-controller-library) **[[code-architecture-and-frameworks]]** Give each ability a unique Name; registering two abilities with the same Name throws an error. Share a Labels entry for similar abilities.
- [page](https://create.roblox.com/docs/characters/character-controller-library) **[[code-architecture-and-frameworks]]** Use labels as a coordination bus: abilities broadcast Labels/TimedLabels and other abilities' StartsWhen/RunsWhile test them, avoiding direct coupling.
- [page](https://create.roblox.com/docs/characters/character-controller-library) **[[combat-and-gameplay-systems]]** Use TimedLabels.Consumes to prevent double-triggering, e.g. CounterAttack consumes AfterBlock.
- [page](https://create.roblox.com/docs/characters/character-controller-library) **[[combat-and-gameplay-systems]]** Use Blocks, Stops, Suspends or ExclusiveGroup (with Priority) to declare conflicts instead of hand-written checks. Stops overrides priority.
- [page](https://create.roblox.com/docs/characters/character-controller-library) **[[core-loops-and-game-design]]** Use Input Mode Press for discrete actions (dash, attack, throw), Hold or Toggle for sustained actions (sprint, aim, block, crouch), Hold with Repeats for repeated jumping.
- [page](https://create.roblox.com/docs/characters/character-controller-library) **[[core-loops-and-game-design]]** Do not put Rule.Input into StartsWhen or RunsWhile; it throws an error. Let Mode control input-driven start/stop.
- [page](https://create.roblox.com/docs/characters/character-controller-library) **[[scripting-and-performance]]** Keep ability callbacks deterministic and non-yielding, since they run in both predicted client and authoritative server simulations. Never call task.wait or WaitForChild in callbacks.
- [page](https://create.roblox.com/docs/characters/character-controller-library) **[[scripting-and-performance]]** Store custom callback data only in abilityCtx.State (replicated, rolled back) or abilityCtx.Local (scratch). Writing custom fields directly to abilityCtx is an error.
- [page](https://create.roblox.com/docs/characters/character-controller-library) **[[scripting-and-performance]]** Within callbacks, avoid restricted DataModel operations such as Destroy; set an attribute and handle instance lifecycle from a regular script.
- [page](https://create.roblox.com/docs/characters/character-controller-library) **[[ui-ux-design]]** On mobile, ActionSlot 1-7 map to on-screen touch buttons; set CustomIcon/CustomIconActive/CustomIconInvalid asset IDs for those buttons.
- [page](https://create.roblox.com/docs/characters/character-controller-library) **[[core-loops-and-game-design]]** Use OutlivesInputWhile on Hold/Toggle abilities to keep an action running past release under a world condition (e.g. crouch while a ceiling is overhead).

## Numbers
- [page](https://create.roblox.com/docs/characters/character-controller-library) TimedLabels.OnStart example duration: **1 second (Dashing label)** (Dash example broadcasts Dashing label for 1 second on start)
- [page](https://create.roblox.com/docs/characters/character-controller-library) TimedLabels.OnStop example duration: **2 seconds (DashCooldown label)** (Dash example broadcasts DashCooldown for 2 seconds on stop)
- [page](https://create.roblox.com/docs/characters/character-controller-library) ExclusiveGroup priorities example: **Sprinting 200, Stagger 150, Crouching 100** (Locomotion group; Stagger can stop Sprinting despite lower priority)
- [page](https://create.roblox.com/docs/characters/character-controller-library) Mobile touch action slots: **Slots 1-7** (Slots populate on-screen buttons on mobile devices)
- [page](https://create.roblox.com/docs/characters/character-controller-library) Keyboard default slot assignments: **1 Space (Jump), 2 LeftShift (Sprint), 3 LeftControl (Crouch)** (Default action slot bindings for keyboard and mouse)

## Tools
Roblox Studio, Avatar Settings, AvatarAbilities module (@rbx/AvatarAbilities), Input Action System

## He points to
- Roblox Character Controller Library docs

## Topics
[[code-architecture-and-frameworks]] [[combat-and-gameplay-systems]] [[core-loops-and-game-design]] [[development-process-and-speed]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
