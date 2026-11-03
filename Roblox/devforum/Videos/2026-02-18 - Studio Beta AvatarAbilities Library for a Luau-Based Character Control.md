---
title: "[Studio Beta] AvatarAbilities Library for a Luau-Based Character Controller"
url: https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904
creator: Roblox DevForum
official: false
advice_density: medium
date: 2026-02-18
views: 953
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# [Studio Beta] AvatarAbilities Library for a Luau-Based Character Controller

[Open](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904) | Roblox DevForum | 953 views | 2026-02-18

## Summary
Studio Beta announcement and March 2026 update for AvatarAbilities, a Luau-based character controller library replacing the C++ Humanoid. Covers architecture (AbilityManager, ControllerManager), tuning properties, install steps, server authority support, known issues, and the Sensor/Label/Rule ability system.

## Tips
- [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904) **[[development-process-and-speed]]** Start prototypes from the Avatar Abilities Beta Template placefile to test default abilities before integrating into your own experience.
- [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904) **[[core-loops-and-game-design]]** Tune movement via GroundController Friction/FrictionWeight and TurnSpeedFactor for snappier or looser ground feel.
- [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904) **[[core-loops-and-game-design]]** Set AirController MoveMaxForce and TurnMaxTorque to control air acceleration and turning; toggle MaintainLinearMomentum/MaintainAngularMomentum to keep position on moving platforms.
- [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904) **[[core-loops-and-game-design]]** Use Labels and Rules (RequiresToActivate, RequiresToContinue, BlocksWhileActive, CancelsOnActivation) for layered abilities instead of if/else state chains.
- [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904) **[[core-loops-and-game-design]]** Use ExclusiveGroup with priority to make mutually exclusive abilities (e.g. Locomotion group) so higher priority overrides lower, such as FallingDown (60) over Running (20).
- [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904) **[[common-mistakes]]** Do not assume existing experiences will get this controller; it will not be backported and only targets new experiences. Keep Humanoid-based code for existing games.
- [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904) **[[common-mistakes]]** Library currently assumes R15 rigs and is not fully supported for NPCs or R6 characters yet.
- [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904) **[[scripting-and-performance]]** Keep the AbilityManagerActor folder intact with both ServerInitialize and ClientInitialize scripts when moving scripts into your experience.
- [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904) **[[scripting-and-performance]]** Update to the latest library version (restart Studio to force update) to get the RemoteEvent Player argument verification fix.
- [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904) **[[client-server-and-remotes]]** Validate the Player argument on OnServerEvent calls; unverified RemoteEvents let other players kill your character.
- [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904) **[[ai-and-tools]]** Force-load autocomplete by running require("@rbx/AvatarAbilities") in the command bar after each Studio reload while the beta is active.
- [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904) **[[development-process-and-speed]]** Expect breaking API changes during beta; they are limited to once a week and announced a day in advance with change notes.
- [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904) **[[ui-ux-design]]** Shift Lock and Sprint both bind to Left Shift today, causing conflicts; test input defaults carefully and give feedback on cross-platform keybinds.
- [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904) **[[cross-platform-and-console]]** Strafe defaults to Left Alt on PC and Left Option on Mac; Crouch uses C; Sprint uses Left Shift. Input bindings are still in beta and may change.
- [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904) **[[client-server-and-remotes]]** With Server Authority beta, set the Workspace AuthorityMode attribute to Server; abilities sync across peers but expect minor animation glitches.
- [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904) **[[optimization-and-streaming]]** Controller work runs only when state changes, giving near zero-cost idle; avoid custom server-side NPC movement solutions where possible.
- [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904) **[[physics-pathfinding-and-npc-ai]]** The controller is physics-based (ControllerManager, 240hz constraints) so ice-friction and momentum behave per floor material; account for this in level design.

## Numbers
- [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904) Efficiency gain: **25% boost to Luau controller efficiency in March 18, 2026 update** (Architectural refactors and internal script optimizations)
- [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904) Bugs resolved: **over 25** (Found during beta, March 18, 2026 update)
- [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904) Physics solver rate: **up to 240hz** (ControllerManager constraints step alongside collision constraints)
- [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904) Breaking change frequency: **at most once a week** (During beta, announced one day in advance)
- [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904) Priority example: **FallingDown 60 vs Running 20** (Exclusive group priority overrides)

## Tools
AvatarAbilities library (require("@rbx/AvatarAbilities")), AbilityManager, ControllerManager, GroundController, AirController, Roblox Studio Beta Features, Server Authority beta

## He points to
- Avatar Abilities Beta Template placefile
- ControllerManager documentation
- Server Authority beta

## Quotes
- [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904) "Concurrent Abilities: The Ability system supports overlapping and sequencing character behaviors by leveraging Labels and Rules."
- [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904) "We'll limit breaking changes to once a week, and announce releases a day in advance with change notes."

## Topics
[[ai-and-tools]] [[client-server-and-remotes]] [[common-mistakes]] [[core-loops-and-game-design]] [[cross-platform-and-console]] [[development-process-and-speed]] [[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
