---
title: "Docs: resources / the-mystery-of-duvall-drive / main-design-requirements"
url: https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/main-design-requirements.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / the-mystery-of-duvall-drive / main-design-requirements

[Open](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/main-design-requirements.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs page on the main technical design requirements for The Mystery of Duvall Drive: a mission framework with seals and game states, corrupt/normal room swapping via cloned rooms far from the house, three teleport types (reserved-server lobby, cutscene teleports via EventManager, short respawn teleports), and tag-based custom behavior with CollectionService managers, with server/client split for gameplay vs. visual effects.

## Tips
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/main-design-requirements) **[[scripting-and-performance]]** Run object functionality that affects other players' simulation (e.g. collisions) on the server; run purely visual/audio effects (lights, particles, environmental animation) on clients to reduce bandwidth.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/main-design-requirements) **[[code-architecture-and-frameworks]]** Use one manager Script per CollectionService tag category instead of copying scripts into many objects; the manager's Init finds tagged objects at start.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/main-design-requirements) **[[code-architecture-and-frameworks]]** Connect CollectionService GetInstanceAddedSignal and GetInstanceRemovedSignal so objects tagged or untagged at runtime get or lose behavior; Init alone misses them.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/main-design-requirements) **[[code-architecture-and-frameworks]]** Build a mission framework with shared start/finish hooks, a config data read, and a debug completion button so every puzzle follows the same flow.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/main-design-requirements) **[[testing-debugging-and-qa]]** Keep a debug build with skip-lobby, skip-cutscene, and auto-complete-mission cheats, toggled by a settings script that checks PlaceId and RunService:IsStudio().
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/main-design-requirements) **[[optimization-and-streaming]]** Store alternate room states far off-map (about 6,500 studs away) and clone them in on demand from ServerStorage, so the house stays lightweight.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/main-design-requirements) **[[matchmaking-and-teleport]]** Group players (five per group) in a simple lobby, then teleport them once into a reserved server so late joiners cannot miss story beats.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/main-design-requirements) **[[matchmaking-and-teleport]]** Use a scripted cutscene system (EventManager-style) to hide streaming and teleports behind camera shakes, effects and audio.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/main-design-requirements) **[[core-loops-and-game-design]]** Use game states to gate progression: the player can only pick up, place, or trigger a seal during the matching state.

## Numbers
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/main-design-requirements) Off-map corrupt room offset: **~6,500 studs in X direction** (Distance from main house where corrupted room clones are placed)
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/main-design-requirements) Lobby group size: **5 players** (Players grouped before teleport to reserved server)
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/main-design-requirements) Rooms with normal and corrupt states: **6** (Six rooms each had normal and corrupted states)

## Games
- **The Mystery of Duvall Drive**: Mission-driven haunted-house game using seals, corrupt/normal room swaps, reserved-server lobby teleports, and tag-based managers.

## Tools
Roblox Studio, CollectionService, ServerStorage, EventManager (custom), GameStateManager (custom), DemoGlobalSettings (custom)

## He points to
- Missions Logic
- GameStateManager
- EventManager
- DoorManager
- Configuration Scripts
- Foundational gameplay systems

## Topics
[[code-architecture-and-frameworks]] [[core-loops-and-game-design]] [[matchmaking-and-teleport]] [[optimization-and-streaming]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
