---
title: "Introducing Texture Streaming"
url: https://devforum.roblox.com/t/introducing-texture-streaming/4144855
creator: Roblox DevForum
official: false
advice_density: medium
date: 2025-12-12
views: 545
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Introducing Texture Streaming

[Open](https://devforum.roblox.com/t/introducing-texture-streaming/4144855) | Roblox DevForum | 545 views | 2025-12-12

## Summary
Roblox engine announcement introducing Texture Streaming, which dynamically loads textures by distance and screen footprint within a Harmony-set memory budget. Creators need no setup. Reports load-time, memory and download gains on Modern City Template, lists supported instances, and outlines the roadmap (4k rendering, more instances, mesh streaming).

## Tips
- [page](https://devforum.roblox.com/t/introducing-texture-streaming/4144855) **[[building-art-and-assets]]** Use texture atlases only when textures appear together on batchable parts; one high-res texture in an atlas streams the whole atlas at that mip level.
- [page](https://devforum.roblox.com/t/introducing-texture-streaming/4144855) **[[building-art-and-assets]]** Prefer individual unique textures over atlases for non-batchable parts so texture streaming can load mips independently.
- [page](https://devforum.roblox.com/t/introducing-texture-streaming/4144855) **[[building-art-and-assets]]** Keep near-uniform texel density across UV-mapped meshes so the mip selection heuristic produces the best results.
- [page](https://devforum.roblox.com/t/introducing-texture-streaming/4144855) **[[optimization-and-streaming]]** Stay judicious with texture memory on unsupported instances such as ParticleEmitter, since texture streaming does not yet manage them.
- [page](https://devforum.roblox.com/t/introducing-texture-streaming/4144855) **[[optimization-and-streaming]]** No creator action is needed to enable texture streaming; it rolls out automatically per platform.

## Numbers
- [page](https://devforum.roblox.com/t/introducing-texture-streaming/4144855) Time to baseline quality (initial load): **20.6s without, 3.0s with texture streaming** (Modern City Template, 100Mbit/s, clean cache)
- [page](https://devforum.roblox.com/t/introducing-texture-streaming/4144855) Time to steady state quality: **20.6s without, 9.9s with texture streaming** (Modern City Template, same run)
- [page](https://devforum.roblox.com/t/introducing-texture-streaming/4144855) Texture memory used: **280 MB without, 155 MB with texture streaming** (Modern City Template, same scene)
- [page](https://devforum.roblox.com/t/introducing-texture-streaming/4144855) Total download size (all assets): **236 MB without, 110 MB with texture streaming** (Modern City Template, same run)
- [page](https://devforum.roblox.com/t/introducing-texture-streaming/4144855) Texture memory at spawn for ideal quality: **~50 MB with streaming vs legacy peak 225 MB** (Modern City Template spawn point)
- [page](https://devforum.roblox.com/t/introducing-texture-streaming/4144855) Low-end device memory threshold: **3.5 GB; below it 4k textures disabled** (Android/iOS platform support tiers)
- [page](https://devforum.roblox.com/t/introducing-texture-streaming/4144855) Original stored image resolution: **up to 8k** (Cloud storage of uploaded textures before transcoding)

## Games
- **Modern City Template**: Official Roblox template used to benchmark texture streaming load times, memory and download size.

## Tools
Texture Streaming (engine feature), Harmony (memory budget system), Open Cloud Asset APIs

## He points to
- 4k texture rendering Studio Beta
- SLIM
- Instance streaming
- Mesh LoD simplification (RDC announcement)

## Quotes
- [page](https://devforum.roblox.com/t/introducing-texture-streaming/4144855) "As you build confidence in the system once it is released on all platforms, you should feel liberated to use more unique textures in your experience."
- [page](https://devforum.roblox.com/t/introducing-texture-streaming/4144855) "Texture streaming will work better with individual, unique textures, if they are not batchable."

## Topics
[[building-art-and-assets]] [[optimization-and-streaming]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
