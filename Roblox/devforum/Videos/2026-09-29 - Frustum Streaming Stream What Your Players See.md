---
title: "Frustum Streaming: Stream What Your Players See"
url: https://devforum.roblox.com/t/frustum-streaming-stream-what-your-players-see/4904553
creator: Roblox DevForum
official: false
advice_density: medium
date: 2026-09-29
views: 400
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Frustum Streaming: Stream What Your Players See

[Open](https://devforum.roblox.com/t/frustum-streaming-stream-what-your-players-see/4904553) | Roblox DevForum | 400 views | 2026-09-29

## Summary
Roblox DevForum announcement of Frustum Streaming, an opt-in feature that streams instances inside the camera's view cone in addition to the normal streaming cube. Controlled per player via Player.FrustumStreaming (Automatic, Enabled, Disabled). Includes FAQ on performance, memory, and interaction with MRFs.

## Tips
- [page](https://devforum.roblox.com/t/frustum-streaming-stream-what-your-players-see/4904553) **[[optimization-and-streaming]]** Enable frustum streaming only where needed (scopes, racing, free camera); it is opt-in and increases client memory and possibly CPU usage.
- [page](https://devforum.roblox.com/t/frustum-streaming-stream-what-your-players-see/4904553) **[[optimization-and-streaming]]** Use Automatic mode for most games; the engine enables frustum streaming based on FOV, high directional velocity, or far camera movement.
- [page](https://devforum.roblox.com/t/frustum-streaming-stream-what-your-players-see/4904553) **[[optimization-and-streaming]]** Use manual Enabled/Disabled via server script for granular control, e.g. force-enable at start of scope equip animation so targets stream in before aiming.
- [page](https://devforum.roblox.com/t/frustum-streaming-stream-what-your-players-see/4904553) **[[optimization-and-streaming]]** Frustum streaming is capped by device render distance; if render distance is below your streaming target radius, frustum streaming won't help.
- [page](https://devforum.roblox.com/t/frustum-streaming-stream-what-your-players-see/4904553) **[[optimization-and-streaming]]** Keep client scripts compatible with streamed games; instances in view stream in, and with opportunistic behaviour they stream out shortly after looking away.
- [page](https://devforum.roblox.com/t/frustum-streaming-stream-what-your-players-see/4904553) **[[optimization-and-streaming]]** Frustum streaming is not needed for non-streaming games, since all instances are already present on the device.

## Numbers
- [page](https://devforum.roblox.com/t/frustum-streaming-stream-what-your-players-see/4904553) Frustum streaming max distance: **Smaller of max render distance and 100,000 studs** (Per-client limit on how far the frustum streams)
- [page](https://devforum.roblox.com/t/frustum-streaming-stream-what-your-players-see/4904553) Streaming region: **Union of streaming cube + frustum + active MRFs** (Frustum adds to, not replaces, the default streaming cube)

## Tools
Player.FrustumStreaming property, Enum.FrustumStreamingMode

## He points to
- Roblox streaming documentation

## Topics
[[optimization-and-streaming]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
