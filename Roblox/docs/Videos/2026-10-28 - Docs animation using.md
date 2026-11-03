---
title: "Docs: animation / using"
url: https://create.roblox.com/docs/animation/using.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: animation / using

[Open](https://create.roblox.com/docs/animation/using.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on using animations: playing animations from scripts for Humanoid rigs (Animator + LoadAnimation + AnimationTrack) and non-Humanoid rigs (AnimationController + Animator), replacing default character animations via the Animate script in ServerScriptService, weighting multiple idle variations, and a table of catalog animation asset IDs.

## Tips
- [page](https://create.roblox.com/docs/animation/using) **[[building-art-and-assets]]** Humanoid rigs need an Animator child inside the Humanoid; non-Humanoid rigs need an AnimationController with a child Animator before LoadAnimation.
- [page](https://create.roblox.com/docs/animation/using) **[[scripting-and-performance]]** Use GetMarkerReachedSignal(name) on an AnimationTrack to trigger gameplay events (e.g. hit frames) tied to named keyframe markers.
- [page](https://create.roblox.com/docs/animation/using) **[[building-art-and-assets]]** To replace default character animations, put a server Script in ServerScriptService, hook CharacterAppearanceLoaded, stop playing tracks, then set Animate script AnimationId values.
- [page](https://create.roblox.com/docs/animation/using) **[[building-art-and-assets]]** Multiple idle animations are picked randomly; set Weight values so the chance equals animation weight divided by total weight of all state animations (e.g. 5 and 10 gives 1/3 and 2/3).
- [page](https://create.roblox.com/docs/animation/using) **[[building-art-and-assets]]** Catalog avatar animation bundles (Ninja, Knight, Zombie, etc.) provide run, walk, jump, idle, fall, swim, swim idle and climb IDs you can reuse as replacements.

## Numbers
- [page](https://create.roblox.com/docs/animation/using) Idle animation weighting example: **Weights 5 and 10 => 1/3 and 2/3 play chance** (Animate script random pick weighted by Weight values)
- [page](https://create.roblox.com/docs/animation/using) Default character animation states: **8 states (run, walk, jump, idle x2, fall, swim, swim idle, climb)** (Replaceable via Animate script references)
- [page](https://create.roblox.com/docs/animation/using) Catalog avatar bundles listed: **16 bundles (Astronaut to Zombie)** (Each provides run/walk/jump/idle/fall/swim/climb asset IDs)

## Tools
Animator, AnimationController, AnimationTrack, Animation, Animate script, Animation Editor

## He points to
- Roblox Creator Docs: Animation editor export instructions
- Roblox catalog animation reference table

## Topics
[[building-art-and-assets]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
