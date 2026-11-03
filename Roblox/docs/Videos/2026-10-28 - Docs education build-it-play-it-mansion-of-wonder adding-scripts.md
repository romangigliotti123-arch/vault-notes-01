---
title: "Docs: education / build-it-play-it-mansion-of-wonder / adding-scripts"
url: https://create.roblox.com/docs/education/build-it-play-it-mansion-of-wonder/adding-scripts.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: education / build-it-play-it-mansion-of-wonder / adding-scripts

[Open](https://create.roblox.com/docs/education/build-it-play-it-mansion-of-wonder/adding-scripts.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Education docs page on adding three premade scripts to a tutorial system: TutorialManager ModuleScript, server particle script, and client beam script. Covers storing beam/particle assets, creating RemoteEvents, testing, troubleshooting, and limitations (tutorial progress not persistent).

## Tips
- [page](https://create.roblox.com/docs/education/build-it-play-it-mansion-of-wonder/adding-scripts) **[[client-server-and-remotes]]** Put shared RemoteEvents (NextGoal, TutorialEnd) in ReplicatedStorage so client and server scripts can both reference them.
- [page](https://create.roblox.com/docs/education/build-it-play-it-mansion-of-wonder/adding-scripts) **[[code-architecture-and-frameworks]]** Put shared tutorial logic in a ModuleScript in ReplicatedStorage and require it from both client and server scripts.
- [page](https://create.roblox.com/docs/education/build-it-play-it-mansion-of-wonder/adding-scripts) **[[scripting-and-performance]]** Store templates (beams, particle emitters) in ReplicatedStorage/ServerStorage and Clone() them at runtime instead of keeping them in the workspace.
- [page](https://create.roblox.com/docs/education/build-it-play-it-mansion-of-wonder/adding-scripts) **[[testing-debugging-and-qa]]** If particles play on game start, disable Enabled on the particle emitter template in ServerStorage.
- [page](https://create.roblox.com/docs/education/build-it-play-it-mansion-of-wonder/adding-scripts) **[[testing-debugging-and-qa]]** Infinite yield warnings usually mean an object name or location doesn't match what the script expects; verify names and paths against the tutorial.
- [page](https://create.roblox.com/docs/education/build-it-play-it-mansion-of-wonder/adding-scripts) **[[data-persistence]]** Tutorial progress is not persistent by default; implement saving (e.g. DataStores) to keep progress across sessions.
- [page](https://create.roblox.com/docs/education/build-it-play-it-mansion-of-wonder/adding-scripts) **[[first-session-onboarding]]** Use a beam from the player to the next objective plus proximity prompts on goals to guide new players through a tutorial.
- [page](https://create.roblox.com/docs/education/build-it-play-it-mansion-of-wonder/adding-scripts) **[[vfx-and-particles]]** Emit particle bursts on goal interaction via ParticleEmitter:Emit(count) for feedback; add multiple emitters in the template folder for complex effects.

## Numbers
- [page](https://create.roblox.com/docs/education/build-it-play-it-mansion-of-wonder/adding-scripts) Particle emit count: **50 (EMIT_RATE in TutorialParticles script)** (Particles emitted per goal interaction in the sample script)
- [page](https://create.roblox.com/docs/education/build-it-play-it-mansion-of-wonder/adding-scripts) Tutorial goals in sample: **2 (GoalPart1, GoalPart2)** (Goal parts ordered in TutorialManager table)

## Tools
Roblox Studio, Luau, ModuleScript, RemoteEvent, LocalScript, Script

## He points to
- Coding Fundamentals tutorial
- Saving Data article

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[data-persistence]] [[first-session-onboarding]] [[scripting-and-performance]] [[testing-debugging-and-qa]] [[vfx-and-particles]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
