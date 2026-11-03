---
title: "Creating Procedural Mountains: A Fractal Noise Tutorial"
url: https://devforum.roblox.com/t/creating-procedural-mountains-a-fractal-noise-tutorial/1494362
creator: Roblox DevForum
official: false
advice_density: medium
date: 2021-10-04
views: 159
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Creating Procedural Mountains: A Fractal Noise Tutorial

[Open](https://devforum.roblox.com/t/creating-procedural-mountains-a-fractal-noise-tutorial/1494362) | Roblox DevForum | 159 views | 2021-10-04

## Summary
Tutorial on procedural Roblox terrain generation using Perlin noise and fractal noise (octaves, lacunarity, persistence), layered color mapping with thresholds and linearStep blending, and a gap-filling block algorithm for voxel-style mountains, with full code.

## Tips
- [page](https://devforum.roblox.com/t/creating-procedural-mountains-a-fractal-noise-tutorial/1494362) **[[genre-mechanics]]** Use fractal noise (4 octaves, lacunarity 3, persistence 0.35) rather than single Perlin noise for mountainous terrain; single noise looks too flat.
- [page](https://devforum.roblox.com/t/creating-procedural-mountains-a-fractal-noise-tutorial/1494362) **[[optimization-and-streaming]]** Generate only the outer shell of terrain blocks and fill gaps between adjacent columns, avoiding holes while keeping the 3D grid without generating full volumes.
- [page](https://devforum.roblox.com/t/creating-procedural-mountains-a-fractal-noise-tutorial/1494362) **[[building-and-level-design]]** Take math.abs of noise before summing octaves and square the result to flatten mountain bases and separate peaks.
- [page](https://devforum.roblox.com/t/creating-procedural-mountains-a-fractal-noise-tutorial/1494362) **[[building-and-level-design]]** Blend colour layers by fading a noise map toward a constant 1 with linearStep between StartHeight and EndHeight so high peaks become snow rather than grass.
- [page](https://devforum.roblox.com/t/creating-procedural-mountains-a-fractal-noise-tutorial/1494362) **[[building-and-level-design]]** Use 1x1x1 blocks with gap-filling instead of tall prisms; tall prisms hide slope gaps but break mining mechanics.
- [page](https://devforum.roblox.com/t/creating-procedural-mountains-a-fractal-noise-tutorial/1494362) **[[scripting-and-performance]]** Store colour and layer settings in a table and loop over it instead of long if-else chains for maintainability.
- [page](https://devforum.roblox.com/t/creating-procedural-mountains-a-fractal-noise-tutorial/1494362) **[[code-architecture-and-frameworks]]** Split generation into modules (noise, colour, block generation) once you add more noise types or features.

## Numbers
- [page](https://devforum.roblox.com/t/creating-procedural-mountains-a-fractal-noise-tutorial/1494362) Fractal noise octaves: **4** (Recommended octave count in example; lacunarity 3, persistence 0.35)
- [page](https://devforum.roblox.com/t/creating-procedural-mountains-a-fractal-noise-tutorial/1494362) Noise scale / height scale: **NOISE_SCALE 50, HEIGHT_SCALE 50** (Full code snippet terrain settings on a 200x200 grid)
- [page](https://devforum.roblox.com/t/creating-procedural-mountains-a-fractal-noise-tutorial/1494362) Map size in full snippet: **200 x 200** (Grid size used in final code)
- [page](https://devforum.roblox.com/t/creating-procedural-mountains-a-fractal-noise-tutorial/1494362) Water layer: **Transparency 0.7, height 2.95** (Translucent water part sized to map)

## Tools
math.noise, Random, Roblox Part API

## He points to
- Ken Perlin (Perlin noise, NYU)

## Topics
[[building-and-level-design]] [[code-architecture-and-frameworks]] [[genre-mechanics]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
