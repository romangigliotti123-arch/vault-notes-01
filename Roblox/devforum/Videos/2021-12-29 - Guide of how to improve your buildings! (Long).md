---
title: "Guide of how to improve your buildings! (Long)"
url: https://devforum.roblox.com/t/guide-of-how-to-improve-your-buildings-long/1606301
creator: Roblox DevForum
official: false
advice_density: medium
date: 2021-12-29
views: 167
transcript: web-page
confidence: medium
tags: [roblox, roblox devforum, youtube-learn]
---

# Guide of how to improve your buildings! (Long)

[Open](https://devforum.roblox.com/t/guide-of-how-to-improve-your-buildings-long/1606301) | Roblox DevForum | 167 views | 2021-12-29

## Summary
Developer guide on improving Roblox building: recommended build/editing plugins (Atmos, F3X, Archimedes, Brush Tool, GapFill, Model Reflect, Texture Library), part-count optimization with the author's tester-based limits (~5k parts in render area, streaming), material and lighting performance costs, lighting filter setup, low-poly textures, and terrain use.

## Tips
- [page](https://devforum.roblox.com/t/guide-of-how-to-improve-your-buildings-long/1606301) **[[building-and-level-design]]** Keep a city's building part count low: an 800-part building cut to 68 parts via wall shapes, then cloned 100 times, yields 6,800 parts instead of 80,000.
- [page](https://devforum.roblox.com/t/guide-of-how-to-improve-your-buildings-long/1606301) **[[optimization-and-streaming]]** Target about 5k parts within the players' rendering area; author's testers saw 60fps under 5k and 25-30fps from 9k parts.
- [page](https://devforum.roblox.com/t/guide-of-how-to-improve-your-buildings-long/1606301) **[[optimization-and-streaming]]** Enable Workspace StreamingEnabled with a streaming radius (default 1024 studs) for large maps with many details; author rated it reducing lag 4/5.
- [page](https://devforum.roblox.com/t/guide-of-how-to-improve-your-buildings-long/1606301) **[[optimization-and-streaming]]** Use SmoothPlastic instead of Neon for large amounts of parts; Neon is the heaviest material for low-VRAM devices, so simulators and tycoons stick to SmoothPlastic.
- [page](https://devforum.roblox.com/t/guide-of-how-to-improve-your-buildings-long/1606301) **[[optimization-and-streaming]]** Use ShadowMap lighting by default for well-optimized games; switch to Future only for demanding visuals.
- [page](https://devforum.roblox.com/t/guide-of-how-to-improve-your-buildings-long/1606301) **[[optimization-and-streaming]]** Disable Haze and avoid neon/glass/dynamic clouds where possible; author rated Haze as reducing lag and dynamic clouds as causing heavy lag (4.5/5).
- [page](https://devforum.roblox.com/t/guide-of-how-to-improve-your-buildings-long/1606301) **[[optimization-and-streaming]]** Anchor your constructions; moving unanchored parts causes lag.
- [page](https://devforum.roblox.com/t/guide-of-how-to-improve-your-buildings-long/1606301) **[[building-and-level-design]]** Use unions (Solid Modeling) or meshes to reduce part counts for complex shapes, but check triangle counts in wireframe, since poorly topologized meshes can cost more than parts.
- [page](https://devforum.roblox.com/t/guide-of-how-to-improve-your-buildings-long/1606301) **[[building-art-and-assets]]** Use Brick Counter plugin to measure total parts in your place and per model before optimizing.
- [page](https://devforum.roblox.com/t/guide-of-how-to-improve-your-buildings-long/1606301) **[[building-art-and-assets]]** Use Texture Library Tool plugin and low-poly texture packs to add color and realism to low-poly builds cheaply.
- [page](https://devforum.roblox.com/t/guide-of-how-to-improve-your-buildings-long/1606301) **[[building-and-level-design]]** Use Part To Terrain to convert blocks into grass, water, or rivers quickly, and raise buildings above terrain to make small street scenes.
- [page](https://devforum.roblox.com/t/guide-of-how-to-improve-your-buildings-long/1606301) **[[ui-ux-design]]** Lighting filters (Sun rays, Color Correction, Bloom, Depth of Field) add mood; Color Correction is widely used in tycoons and simulators to make colors more vivid.
- [page](https://devforum.roblox.com/t/guide-of-how-to-improve-your-buildings-long/1606301) **[[building-art-and-assets]]** Use Stravant GapFill and Model Reflect plugins for precise connecting geometry and symmetrical builds.

## Numbers
- [page](https://devforum.roblox.com/t/guide-of-how-to-improve-your-buildings-long/1606301) part budget: **~5k parts in players' render area** (author's tester-based limit for 60fps; 9k parts gave 25-30fps)
- [page](https://devforum.roblox.com/t/guide-of-how-to-improve-your-buildings-long/1606301) part count reduction: **800 -> 68 parts per building** (wall-shape building; 100 clones = 6,800 parts vs 80,000)
- [page](https://devforum.roblox.com/t/guide-of-how-to-improve-your-buildings-long/1606301) StreamingEnabled default radius: **1024 studs** (Workspace streaming option; author's 300-stud loading example)
- [page](https://devforum.roblox.com/t/guide-of-how-to-improve-your-buildings-long/1606301) lag rating Dynamic Clouds: **4.5/5** (author tester average, lag scale 1-5)
- [page](https://devforum.roblox.com/t/guide-of-how-to-improve-your-buildings-long/1606301) lag rating Neon and Glass: **3/5** (author tester average, lag scale 1-5)
- [page](https://devforum.roblox.com/t/guide-of-how-to-improve-your-buildings-long/1606301) lag rating Lights: **3/5** (author tester average, lag scale 1-5)
- [page](https://devforum.roblox.com/t/guide-of-how-to-improve-your-buildings-long/1606301) lag reduction Haze: **3.5/5** (author tester average)
- [page](https://devforum.roblox.com/t/guide-of-how-to-improve-your-buildings-long/1606301) lag reduction Streaming On: **4/5** (author tester average)
- [page](https://devforum.roblox.com/t/guide-of-how-to-improve-your-buildings-long/1606301) Atmos plugin price: **150 Robux** (paid lighting/skybox plugin)
- [page](https://devforum.roblox.com/t/guide-of-how-to-improve-your-buildings-long/1606301) Testers hardware floor: **Pentium Dual-Core 3.2GHz, 2-4GB RAM, Intel 4 Series GPU** (low-end test devices, 32-bit Windows)

## Tools
Atmos, Building Tools by F3X, Archimedes 2, Brush Tool 2.1, Part To Terrain, Stravant GapFill, Stravant Model Reflect, Texture Library Tool

## He points to
- Atmos - professional skyboxes and lighting
- HOW TO USE F3X: The Basics (YouTube)
- Getting Started with Atmos (YouTube)

## Topics
[[building-and-level-design]] [[building-art-and-assets]] [[optimization-and-streaming]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
