---
title: "Ultimate Perlin Noise and How To Make Procedural Terrain Guide | 24,231 Characters DETAILED"
url: https://devforum.roblox.com/t/ultimate-perlin-noise-and-how-to-make-procedural-terrain-guide-24231-characters-detailed/3109400
creator: Roblox DevForum
official: false
advice_density: medium
date: 2024-08-08
views: 115
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Ultimate Perlin Noise and How To Make Procedural Terrain Guide | 24,231 Characters DETAILED

[Open](https://devforum.roblox.com/t/ultimate-perlin-noise-and-how-to-make-procedural-terrain-guide-24231-characters-detailed/3109400) | Roblox DevForum | 115 views | 2024-08-08

## Summary
Step-by-step guide to building Perlin-noise procedural terrain in Roblox using math.noise, Random-based seed offsets, scale/frequency/amplitude parameters, height-based color dictionary, chunking, and smoothing water flat. Includes full source code.

## Tips
- [page](https://devforum.roblox.com/t/ultimate-perlin-noise-and-how-to-make-procedural-terrain-guide-24231-characters-detailed/3109400) **[[scripting-and-performance]]** Do not use tick() as the Z argument of math.noise; Roblox clamps Z to 0-1, so use a Random-generated seed offset instead.
- [page](https://devforum.roblox.com/t/ultimate-perlin-noise-and-how-to-make-procedural-terrain-guide-24231-characters-detailed/3109400) **[[scripting-and-performance]]** Generate offsets with Random.new(Seed):NextNumber(-100000, 100000); the author says larger offsets distort the terrain.
- [page](https://devforum.roblox.com/t/ultimate-perlin-noise-and-how-to-make-procedural-terrain-guide-24231-characters-detailed/3109400) **[[scripting-and-performance]]** Clamp the math.noise result to 0-1 but multiply by Amplitude afterward; clamping after amplitude removes all hills.
- [page](https://devforum.roblox.com/t/ultimate-perlin-noise-and-how-to-make-procedural-terrain-guide-24231-characters-detailed/3109400) **[[scripting-and-performance]]** Add a task.wait() per outer loop iteration to avoid crashing Studio when generating large maps.
- [page](https://devforum.roblox.com/t/ultimate-perlin-noise-and-how-to-make-procedural-terrain-guide-24231-characters-detailed/3109400) **[[optimization-and-streaming]]** Use chunk size to scale up world size rather than scale; MapSize controls width and length. The guide claims huge maps generate in under 2 seconds.
- [page](https://devforum.roblox.com/t/ultimate-perlin-noise-and-how-to-make-procedural-terrain-guide-24231-characters-detailed/3109400) **[[building-and-level-design]]** Typical starting values: Scale 10, Frequency 0.4, Amplitude 10-15, ChunkSize 2, SmoothingFactor around 0.25 for best results.
- [page](https://devforum.roblox.com/t/ultimate-perlin-noise-and-how-to-make-procedural-terrain-guide-24231-characters-detailed/3109400) **[[building-and-level-design]]** Map height to color with a threshold dictionary (0-1 keys); the color applies to any height greater than the key, e.g. water, grass, rock, snow.
- [page](https://devforum.roblox.com/t/ultimate-perlin-noise-and-how-to-make-procedural-terrain-guide-24231-characters-detailed/3109400) **[[building-and-level-design]]** Flatten water by remapping heights above a threshold with inverse lerp, keeping the original height for colouring via a preservedBaseY variable.
- [page](https://devforum.roblox.com/t/ultimate-perlin-noise-and-how-to-make-procedural-terrain-guide-24231-characters-detailed/3109400) **[[building-and-level-design]]** Set part Y size to y*2+1 so terrain columns are solid and holes disappear.

## Numbers
- [page](https://devforum.roblox.com/t/ultimate-perlin-noise-and-how-to-make-procedural-terrain-guide-24231-characters-detailed/3109400) Generation time: **under 2 seconds for huge maps (author claim)** (Perlin generator with MapSize-driven loops)
- [page](https://devforum.roblox.com/t/ultimate-perlin-noise-and-how-to-make-procedural-terrain-guide-24231-characters-detailed/3109400) Seed offset range: **-100000 to 100000** (Random:NextNumber offsets; author says higher distorts terrain)
- [page](https://devforum.roblox.com/t/ultimate-perlin-noise-and-how-to-make-procedural-terrain-guide-24231-characters-detailed/3109400) Recommended smoothing factor: **0-1, about 0.25 best** (Flattens water bumps via inverse lerp)
- [page](https://devforum.roblox.com/t/ultimate-perlin-noise-and-how-to-make-procedural-terrain-guide-24231-characters-detailed/3109400) Starting parameters: **Scale 10, Frequency 0.4, Amplitude 15, ChunkSize 2** (Author's suggested defaults for realistic terrain)

## Tools
math.noise, Random, ModuleScript, Roblox Studio command bar

## He points to
- Sebastian Lague Perlin noise video
- Roblox Perlin Generator GitHub repo (LxckyDev)

## Topics
[[building-and-level-design]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
