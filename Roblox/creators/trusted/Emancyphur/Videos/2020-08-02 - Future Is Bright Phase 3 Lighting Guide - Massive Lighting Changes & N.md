---
title: "Future Is Bright Phase 3 Lighting Guide - Massive Lighting Changes & New 'Future' Setting - [EP 20]"
url: https://youtu.be/ScdTM3ju-yk
creator: Emancyphur
official: false
advice_density: medium
date: 2020-08-02
views: 17043
transcript: manual-subs
confidence: high
tags: [roblox, emancyphur, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.6
---

> [!note] Trust: TRUSTED (credibility audit score 7.6): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Future Is Bright Phase 3 Lighting Guide - Massive Lighting Changes & New "Future" Setting - [EP 20]

[Watch](https://youtu.be/ScdTM3ju-yk) | Emancyphur | 17,043 views | 2020-08-02

## Summary
Overview of Future Is Bright Phase 3 lighting update for Roblox: enabling the "Future" Technology setting, how PointLights, SpotLights and SurfaceLights changed versus ShadowMap, what SurfaceLights still lack (shadows), and the trade-offs of using it (graphics-level requirement, performance cost, fallback lighting for low-end users).

## Tips
- [0:58](https://youtu.be/ScdTM3ju-yk?t=58) **[[scripting-and-performance]]** Set Lighting Technology to Future in Properties; players need 5+ graphics bars (or Studio quality level 10+) to see it, others fall back to ShadowMap/Voxel.
- [4:15](https://youtu.be/ScdTM3ju-yk?t=255) **[[optimization-and-streaming]]** Expect Future lighting to cost performance; one developer saw menu FPS drop from about 200 to 100. Test on low-end PCs and mobile.
- [4:15](https://youtu.be/ScdTM3ju-yk?t=255) **[[optimization-and-streaming]]** Prefer shadowed SpotLights over shadowed PointLights; the staff note says shadowed PointLights cost more performance.
- [3:06](https://youtu.be/ScdTM3ju-yk?t=186) **[[building-art-and-assets]]** Don't rely on SurfaceLight shadows under Future; they are not supported yet, so use SpotLights if shadows matter.
- [4:59](https://youtu.be/ScdTM3ju-yk?t=299) **[[building-art-and-assets]]** Re-tune lighting for every time of day, especially interiors that relied on few light sources, since Future lighting changes how areas look.
- [4:59](https://youtu.be/ScdTM3ju-yk?t=299) **[[testing-debugging-and-qa]]** Switch between Future and ShadowMap and check both to see what lower-graphics players will see; there are known bugs when swapping.
- [0:23](https://youtu.be/ScdTM3ju-yk?t=23) **[[roblox-platform-changes]]** Future Is Bright Phase 3 was in beta as of Aug 2020; features won't show in live play until full release, so check the announcement thread for changes.

## Numbers
- [4:15](https://youtu.be/ScdTM3ju-yk?t=255) FPS on menu screen (reported by one user): **~200 down to ~100 FPS** (Drop after enabling Future lighting in one game)
- [3:34](https://youtu.be/ScdTM3ju-yk?t=214) Minimum in-game graphics bars for Future lighting: **5 bars** (Players below this default to ShadowMap or Voxel)
- [1:01](https://youtu.be/ScdTM3ju-yk?t=61) Studio Edit Quality Level needed to preview Future: **10 or higher** (Rendering tab setting in Studio)

## Tools
Roblox Studio Lighting properties (Technology setting)

## He points to
- Future Is Bright tutorial playlist (Roblox lighting series)
- Roblox DevForum announcement thread for Future Is Bright updates

## Topics
[[building-art-and-assets]] [[optimization-and-streaming]] [[roblox-platform-changes]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Emancyphur - How to make successful Roblox games]]
