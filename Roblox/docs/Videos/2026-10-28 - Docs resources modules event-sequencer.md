---
title: "Docs: resources / modules / event-sequencer"
url: https://create.roblox.com/docs/resources/modules/event-sequencer.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / modules / event-sequencer

[Open](https://create.roblox.com/docs/resources/modules/event-sequencer.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs for the EventSequencer module: a framework for building scheduled, cross-server events and cutscenes. Covers installation, replace vs inline modes, scenes and their Environment folders, schema lifecycle hooks, configurations (audio, animate, tween, interval, schedule, inform), seeking permissions, and the Scene Manager plugin.

## Tips
- [page](https://create.roblox.com/docs/resources/modules/event-sequencer) **[[development-process-and-speed]]** Use replace mode for new multi-scene event games; use inline mode for existing games to preserve the place's layout while orchestrating cutscenes.
- [page](https://create.roblox.com/docs/resources/modules/event-sequencer) **[[core-loops-and-game-design]]** Perform audio and animation operations on the client side, as in a typical game, and keep schema configurations in both client and server modules where needed.
- [page](https://create.roblox.com/docs/resources/modules/event-sequencer) **[[first-session-onboarding]]** Keep OnSetup and OnRun free of wait calls; waiting delays the start while the scene timer keeps counting, desynchronising the show.
- [page](https://create.roblox.com/docs/resources/modules/event-sequencer) **[[data-persistence]]** Call inform() for any connection or module created in OnRun so it is cleaned up correctly when seeking backward; initialise persistent references in OnSetup and clean up in OnEndScene.
- [page](https://create.roblox.com/docs/resources/modules/event-sequencer) **[[optimization-and-streaming]]** Use the Scene Manager plugin to load and unload scenes instead of manually moving objects; always click Save Terrain even for empty scenes to clear previous terrain.
- [page](https://create.roblox.com/docs/resources/modules/event-sequencer) **[[common-mistakes]]** Do not place Environment folder assets in scenes used with inline mode; inline mode expects existing place assets and global lighting settings.
- [page](https://create.roblox.com/docs/resources/modules/event-sequencer) **[[common-mistakes]]** Scenes must be tagged SequencerScene to appear in the Scene Manager plugin; if a new scene is missing, tag it, then save and reopen the place.
- [page](https://create.roblox.com/docs/resources/modules/event-sequencer) **[[matchmaking-and-teleport]]** Restrict seeking via setSeekingPermissions using placeIDs, userIDs, and group minimum ranks so ordinary players cannot control event timing.
- [page](https://create.roblox.com/docs/resources/modules/event-sequencer) **[[core-loops-and-game-design]]** Omit OnEndScene for endless scenes such as post-show venues and set TimeLength long enough to cover all configurations.

## Numbers
- [page](https://create.roblox.com/docs/resources/modules/event-sequencer) Seek grace period: **5 seconds** (loadScene waits 5s for server load before seeking to startTime)
- [page](https://create.roblox.com/docs/resources/modules/event-sequencer) Default audio volume: **0.5** (audio configuration default Volume)
- [page](https://create.roblox.com/docs/resources/modules/event-sequencer) Default animation fade in/out: **0.2 seconds each** (animate configuration defaults for FadeInTime and FadeOutTime)
- [page](https://create.roblox.com/docs/resources/modules/event-sequencer) Default animation speed: **1** (animate configuration default Speed)

## Games
- **Twenty One Pilots concert**: Framework was battle-tested in this Roblox event.
- **24kGoldn concert**: Framework was battle-tested in this Roblox event.

## Tools
EventSequencer module (Creator Store package), Scene Manager plugin, Roblox Studio Concert template

## He points to
- Concert template in Roblox Studio
- Creator Store Packages: Event Sequencer

## Topics
[[common-mistakes]] [[core-loops-and-game-design]] [[data-persistence]] [[development-process-and-speed]] [[first-session-onboarding]] [[matchmaking-and-teleport]] [[optimization-and-streaming]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
