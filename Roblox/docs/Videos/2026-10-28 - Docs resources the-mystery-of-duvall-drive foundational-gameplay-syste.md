---
title: "Docs: resources / the-mystery-of-duvall-drive / foundational-gameplay-systems"
url: https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/foundational-gameplay-systems.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / the-mystery-of-duvall-drive / foundational-gameplay-systems

[Open](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/foundational-gameplay-systems.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs case study of The Mystery of Duvall Drive's foundational systems: GameStateManager state machine (teleport cutscenes Warmup/InFlight/Cooldown, lighting swaps, door locking), EventManager keyframed actions (interpolation, scripts, audio, camera shakes, triggers), mission type logic, and server-authoritative grabbing with RigidConstraints.

## Tips
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/foundational-gameplay-systems) **[[core-loops-and-game-design]]** Implement game flow as a simple server-side state machine with states listed in a config enum; keep mission-specific code out of the core manager, except where unavoidable.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/foundational-gameplay-systems) **[[client-server-and-remotes]]** Use one RemoteEvent with an event-type command as the first payload parameter, then event-specific data, to communicate server-to-client state changes.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/foundational-gameplay-systems) **[[client-server-and-remotes]]** Run cosmetic actions (non-simulation interpolation) on the client for smoother results; keep simulation-changing actions on the server.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/foundational-gameplay-systems) **[[optimization-and-streaming]]** Hide teleports behind a cutscene and call RequestStreamAroundAsync before moving players; add a timeout so the flow proceeds if streaming never reports done.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/foundational-gameplay-systems) **[[ui-ux-design]]** Disable the default streaming-pause warning UI when it would break immersion, and replace it with your own transition.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/foundational-gameplay-systems) **[[combat-and-gameplay-systems]]** Unseat players before a scripted CFrame teleport and disable seating during the teleport, since seated players cannot be moved to a CFrame.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/foundational-gameplay-systems) **[[building-and-level-design]]** Give normal and altered versions of a room visibly different lighting and atmosphere, and swap those instances during the teleport cutscene so the change is hidden.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/foundational-gameplay-systems) **[[core-loops-and-game-design]]** Lock doors until a required item is picked up to create an incentive to collect it before progressing.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/foundational-gameplay-systems) **[[core-loops-and-game-design]]** Build a reusable event system: keyframed actions referenced by object name under a root, with parameters, so one event description works on streamed and runtime-created objects.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/foundational-gameplay-systems) **[[development-process-and-speed]]** Ship debug cheat buttons for mission completion during development and strip debug objects in the release build.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/foundational-gameplay-systems) **[[client-server-and-remotes]]** For grabbing, validate on the server that the object is not already held by another player and cancel the grab if so; handle different parts of the same model.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/foundational-gameplay-systems) **[[physics-pathfinding-and-npc-ai]]** Grab by creating attachments on the hand and object and joining them with a RigidConstraint; disable collisions on the grabbed object and restore them on release.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/foundational-gameplay-systems) **[[scripting-and-performance]]** Store per-player grab state in a server table and clean up attachments, constraints and collision state on release.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/foundational-gameplay-systems) **[[building-art-and-assets]]** Keep a visual cue for the player's new state after a transition, such as the corrupt-room look, so they know they are in a different location.

## Numbers
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/foundational-gameplay-systems) Missions: **7 total, 6 use seals** (Mystery of Duvall Drive mission count)
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/foundational-gameplay-systems) Mission types: **4 types, matching items used in 4 missions** (Mission type breakdown, identified by named config members)
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/foundational-gameplay-systems) Cooldown timeout: **several seconds** (Fallback before Cooldown if streaming does not finish)
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/foundational-gameplay-systems) Event keyframe example: **TextTransparency 1 -> 0 at 0.5s, holds to 2.25s, back to 1 at 3s** (Interpolation example from the docs)

## Games
- **The Mystery of Duvall Drive**: Demo uses a state machine for flow, a keyframe event system for timed actions, and server-authoritative grabbing; cutscenes hide teleports to corrupt rooms.

## Tools
RequestStreamAroundAsync, RigidConstraint, RemoteEvent, PathfindingService, Humanoid.MoveTo

## He points to
- Making the Expanding Pantry (trigger volume example in the same doc series)

## Topics
[[building-and-level-design]] [[building-art-and-assets]] [[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[core-loops-and-game-design]] [[development-process-and-speed]] [[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
