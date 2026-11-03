---
title: "Roblox Developer Conference 2018 - Designing for Performance"
url: https://youtu.be/rBrILsiVdtQ
creator: Roblox
official: true
advice_density: high
date: 2018-07-24
views: 10575
transcript: auto-captions
confidence: high
tags: [roblox, robloxofficial, youtube-learn]
---

# Roblox Developer Conference 2018 - Designing for Performance

[Watch](https://youtu.be/rBrILsiVdtQ) | RobloxOfficial | 10,575 views | 2018-07-24

## Summary
Roblox DevConf 2018 talk by Arseny (technical director) on performance: memory, join time, frame time budgets; analysis tools (Performance Stats, Client/Server memory, Microprofiler, stopwatch); new instancing, LOD, texture transcoding, UI caching; scripting, building (terrain, parts, mesh, CSG), physics, rendering and transparency guidance.

## Tips
- [3:14](https://youtu.be/rBrILsiVdtQ?t=194) **[[analytics-metrics]]** Target join time: median around 5 seconds is good; over 10 seconds is not great. Measure up to the interactive state, including loading screens.
- [4:06](https://youtu.be/rBrILsiVdtQ?t=246) **[[scripting-and-performance]]** Frame budget is 15-30 ms per frame (60-30 FPS). Watch worst-case frames, not just average; isolated spikes feel far worse than steady slightly slower frames.
- [6:03](https://youtu.be/rBrILsiVdtQ?t=363) **[[analytics-metrics]]** Check the Developer Console client and server memory breakdown per device type; memory categories differ between platforms, so measure on the target device.
- [7:29](https://youtu.be/rBrILsiVdtQ?t=449) **[[analytics-metrics]]** Use Microprofiler (Ctrl+Alt+F6 on desktop, enabled in settings on mobile) to find why frames are slow, including your own script timings.
- [8:46](https://youtu.be/rBrILsiVdtQ?t=526) **[[scripting-and-performance]]** Join time is mostly a function of instance and voxel count; use streaming. Avoid blocking server calls in character loading, e.g. third-party analytics, which caused 30 s waits when the service went down.
- [19:23](https://youtu.be/rBrILsiVdtQ?t=1163) **[[scripting-and-performance]]** Prefer event-based code over running every frame. Slice long-running work into small per-frame pieces to avoid single-frame spikes.
- [20:46](https://youtu.be/rBrILsiVdtQ?t=1246) **[[scripting-and-performance]]** Heartbeat, Stepped and RenderStepped all run every frame; RenderStepped runs before rendering and inflates render time, so prefer Heartbeat or Stepped.
- [21:46](https://youtu.be/rBrILsiVdtQ?t=1306) **[[scripting-and-performance]]** Cache property reads and object creation in Lua; use Roblox built-in APIs (animation, UI layout) instead of rewriting them, and request missing features instead.
- [24:29](https://youtu.be/rBrILsiVdtQ?t=1469) **[[building-art-and-assets]]** Terrain is efficient per unit of detail with stable performance; don't export it to mesh parts or hollow it into thin shells, which runs slower.
- [28:26](https://youtu.be/rBrILsiVdtQ?t=1706) **[[building-art-and-assets]]** On low-end mobile, budget tens of thousands of parts per area; hundreds of thousands are fine only with streaming and sparse layouts.
- [31:22](https://youtu.be/rBrILsiVdtQ?t=1882) **[[building-art-and-assets]]** Use Roblox materials rather than SurfaceAppearance/texture objects. Don't use unions as a performance fix; they defeat instancing. Keep unions to dozens of parts.
- [32:50](https://youtu.be/rBrILsiVdtQ?t=1970) **[[building-art-and-assets]]** Avoid many transparent objects; fully transparent (1) is cheapest, fully opaque (0) next, and partial transparency is the costliest. Don't hide parts by covering them with decals.
- [17:06](https://youtu.be/rBrILsiVdtQ?t=1026) **[[building-art-and-assets]]** Split on-screen UI into separate ScreenGuis by update frequency. Updating any element in a shared ScreenGui forces the slow render path.
- [12:57](https://youtu.be/rBrILsiVdtQ?t=777) **[[building-art-and-assets]]** Cloning mesh parts (instancing) keeps memory roughly constant. Resizing or recolouring a copy does not block instancing for mesh parts, but wedges weren't instanced yet at the time.
- [29:29](https://youtu.be/rBrILsiVdtQ?t=1769) **[[building-art-and-assets]]** Use simple collision fidelity (Box or Hull) when possible. Disabling collision on distant anchored parts only helps when nothing moving nearby can touch them.
- [22:28](https://youtu.be/rBrILsiVdtQ?t=1348) **[[scripting-and-performance]]** Collection Service tags are efficient even at about a thousand tags. Use multiple remote events for large data volumes; one event suits low traffic.
- [14:20](https://youtu.be/rBrILsiVdtQ?t=860) **[[scripting-and-performance]]** Instancing does not support outlines or Humanoids at the time; disable outlines when not needed and keep Humanoids for characters only.
- [16:25](https://youtu.be/rBrILsiVdtQ?t=985) **[[building-art-and-assets]]** A 1024x1024 texture costs about 5 MB of memory regardless of PNG file size; texture transcoding will reduce mobile memory.
- [11:33](https://youtu.be/rBrILsiVdtQ?t=693) **[[scripting-and-performance]]** Simplify mesh triangle counts and combine meshes where possible; splitting one high-poly mesh into many smaller ones does not speed rendering.

## Numbers
- [2:26](https://youtu.be/rBrILsiVdtQ?t=146) Memory budget: **Hundreds of MB on mobile, varies by device; 1024x1024 texture ~5 MB**
- [3:14](https://youtu.be/rBrILsiVdtQ?t=194) Join time: **Average/median ~5 s good; >10 s not great**
- [4:06](https://youtu.be/rBrILsiVdtQ?t=246) Frame time budget: **15-30 ms (60-30 FPS)**
- [28:26](https://youtu.be/rBrILsiVdtQ?t=1706) Basic parts on low-end mobile: **Target tens of thousands of parts**
- [12:57](https://youtu.be/rBrILsiVdtQ?t=777) Instancing deployment: **Mesh parts and CSG on most platforms; ~20% of Android Wear devices**
- [10:08](https://youtu.be/rBrILsiVdtQ?t=608) Join-time outage example: **15,000 concurrent players; 30 s timeouts from third-party analytics**
- [27:04](https://youtu.be/rBrILsiVdtQ?t=1624) Terrain LOD shell thickness: **Needs 4-8 voxels thick, one-voxel shells perform poorly**
- [32:03](https://youtu.be/rBrILsiVdtQ?t=1923) Union size guidance: **Target dozens of parts per union**

## Games
- **Jailbreak** [31:22](https://youtu.be/rBrILsiVdtQ?t=1882): Used as example of a visual bug when rolling out mesh part instancing (broke UV mapping).

## Tools
Performance Stats, Developer Console (client/server memory), Microprofiler, Stopwatch (join time), Roblox Studio device emulator (planned)

## He points to
- Roblox DevForum performance threads
- Roblox Lua performance tips by Roberto Ierusalimschy

## Quotes
- [34:18](https://youtu.be/rBrILsiVdtQ?t=2058) "If you don't tell us anything then we will not get better so talk to us."
- [31:22](https://youtu.be/rBrILsiVdtQ?t=1882) "Don't treat CSG as this magical performance fixing solution. Unions every pair of parts in my world surely it must become more efficient, no."

## On screen
Contact sheet shows the Performance/Developer Console client memory table (7:15), a stopwatch slide for join time (9:47, 10:13) stating load time scales with instances/voxels and to watch server delays, and the UI caching slide (17:29) advising separate ScreenGuis for related UI elements.

## Topics
[[analytics-metrics]] [[building-art-and-assets]] [[scripting-and-performance]]

Back to [[RobloxOfficial - How to make successful Roblox games]]
