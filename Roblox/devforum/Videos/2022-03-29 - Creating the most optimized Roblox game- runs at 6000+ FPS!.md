---
title: "Creating the most optimized Roblox game- runs at 6000+ FPS!"
url: https://devforum.roblox.com/t/creating-the-most-optimized-roblox-game-runs-at-6000-fps/1736424
creator: Roblox DevForum
official: false
advice_density: medium
date: 2022-03-29
views: 415
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Creating the most optimized Roblox game- runs at 6000+ FPS!

[Open](https://devforum.roblox.com/t/creating-the-most-optimized-roblox-game-runs-at-6000-fps/1736424) | Roblox DevForum | 415 views | 2022-03-29

## Summary
Boatbomber's walkthrough of making a UI-only Roblox benchmark game run at thousands of FPS by stripping 3D, physics, lighting, sky, camera and default scripts. Includes GPU timing benchmarks before and after the optimizations.

## Tips
- [page](https://devforum.roblox.com/t/creating-the-most-optimized-roblox-game-runs-at-6000-fps/1736424) **[[optimization-and-streaming]]** For UI-only games, set gravity to 0, remove characters, and empty the world geometry to eliminate background 3D and physics work the engine still performs.
- [page](https://devforum.roblox.com/t/creating-the-most-optimized-roblox-game-runs-at-6000-fps/1736424) **[[optimization-and-streaming]]** Use voxel lighting, no shadows, black color values and brightness 0 to reduce lighting work in a minimal scene.
- [page](https://devforum.roblox.com/t/creating-the-most-optimized-roblox-game-runs-at-6000-fps/1736424) **[[optimization-and-streaming]]** Add a BloomEffect with Size 0, Intensity 0, Threshold inf to let the engine skip the Glow GPU step entirely.
- [page](https://devforum.roblox.com/t/creating-the-most-optimized-roblox-game-runs-at-6000-fps/1736424) **[[optimization-and-streaming]]** Use a Sky with no celestial bodies or stars and all textures set to one pixel to avoid sending large sky textures to draw calls.
- [page](https://devforum.roblox.com/t/creating-the-most-optimized-roblox-game-runs-at-6000-fps/1736424) **[[optimization-and-streaming]]** Set camera FoV to 1 and camera CFrame to all zeros to minimise or eliminate rendered 3D output when 3D rendering is unused.
- [page](https://devforum.roblox.com/t/creating-the-most-optimized-roblox-game-runs-at-6000-fps/1736424) **[[client-server-and-remotes]]** Do not spawn player characters in games that do not need them; this removes character scripts and work.
- [page](https://devforum.roblox.com/t/creating-the-most-optimized-roblox-game-runs-at-6000-fps/1736424) **[[code-architecture-and-frameworks]]** Override Roblox default scripts (camera, character controls, chat) by replacing them with empty directories, or destroy them on startup where override is impossible.
- [page](https://devforum.roblox.com/t/creating-the-most-optimized-roblox-game-runs-at-6000-fps/1736424) **[[optimization-and-streaming]]** Lower the render resolution (e.g. non-fullscreen window) and use lowest graphics quality to raise FPS in GPU-bound scenes.

## Numbers
- [page](https://devforum.roblox.com/t/creating-the-most-optimized-roblox-game-runs-at-6000-fps/1736424) Baseplate GPU time (max graphics): **1357.24 μs** (Zephrus G14, RenderDoc capture, baseline place)
- [page](https://devforum.roblox.com/t/creating-the-most-optimized-roblox-game-runs-at-6000-fps/1736424) Baseplate GPU time (lowest graphics): **382.59 μs** (Zephrus G14, RenderDoc capture, baseline place)
- [page](https://devforum.roblox.com/t/creating-the-most-optimized-roblox-game-runs-at-6000-fps/1736424) Optimized GPU time (max graphics): **751.61 μs** (After 3D/physics removal, max graphics)
- [page](https://devforum.roblox.com/t/creating-the-most-optimized-roblox-game-runs-at-6000-fps/1736424) Optimized GPU time (lowest graphics): **87.04 μs** (After 3D/physics removal, lowest graphics)
- [page](https://devforum.roblox.com/t/creating-the-most-optimized-roblox-game-runs-at-6000-fps/1736424) GPU time decrease at max graphics: **44.62%** (Baseplate vs optimized)
- [page](https://devforum.roblox.com/t/creating-the-most-optimized-roblox-game-runs-at-6000-fps/1736424) GPU time decrease at lowest graphics: **77.24%** (Baseplate vs optimized)
- [page](https://devforum.roblox.com/t/creating-the-most-optimized-roblox-game-runs-at-6000-fps/1736424) Game FPS progression: **600 → 1000+ → 2400+ → 3500+ → some players 6000+** (Author's FPS milestones for the UI-only project)
- [page](https://devforum.roblox.com/t/creating-the-most-optimized-roblox-game-runs-at-6000-fps/1736424) In-game FPS: **1200+ during UI animation, 1800 peak idle** (Actual game performance after optimizations)

## Games
- **Flex Your FPS**: UI-only benchmark game stripped of 3D and physics; shows how far frame rate can be pushed by removing background engine work.

## Tools
RenderDoc

## He points to
- boatbomber Twitter
- boatbomber GitHub/Patreon/BuyMeACoffee/PayPal (sponsorship links)

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[optimization-and-streaming]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
