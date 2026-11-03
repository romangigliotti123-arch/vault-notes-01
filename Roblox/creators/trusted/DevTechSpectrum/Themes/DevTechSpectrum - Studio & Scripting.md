---
title: DevTechSpectrum - Studio & Scripting
creator: DevTechSpectrum
tags: [roblox, devtechspectrum, theme]
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# DevTechSpectrum: Studio & Scripting

All DevTechSpectrum tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[scripting-and-performance]]
- 2021-01-23 [6:31](https://youtu.be/-PPg4N5sKXE?t=391) Use the Microprofiler (Ctrl+F6 style toggle in Developer Stats) and pause at the biggest spike; dump 32-64 frames to inspect later. ([[2021-01-23 - Roblox Performance Tutorial (Microprofiler, Developer Stats, Developer|Roblox Performance Tutorial (Microprofiler, Develo]])
- 2021-01-23 [9:28](https://youtu.be/-PPg4N5sKXE?t=568) A large RayCast bar in the Microprofiler suggests too many raycasts; reduce how often or how many you cast. ([[2021-01-23 - Roblox Performance Tutorial (Microprofiler, Developer Stats, Developer|Roblox Performance Tutorial (Microprofiler, Develo]])
- 2021-01-23 [15:26](https://youtu.be/-PPg4N5sKXE?t=926) Check the Network tab for frequent service calls (FriendService, MarketplaceService, GamePassService) and reduce them on the server. ([[2021-01-23 - Roblox Performance Tutorial (Microprofiler, Developer Stats, Developer|Roblox Performance Tutorial (Microprofiler, Develo]])

## [[optimization-and-streaming]]
- 2021-01-23 [1:08](https://youtu.be/-PPg4N5sKXE?t=68) Target 400-500 MB memory for a full game; under 400 is a very small game; avoid approaching 1000 MB. ([[2021-01-23 - Roblox Performance Tutorial (Microprofiler, Developer Stats, Developer|Roblox Performance Tutorial (Microprofiler, Develo]])
- 2021-01-23 [2:32](https://youtu.be/-PPg4N5sKXE?t=152) Memory grows from textures, meshes, loops that don't free memory, and undisconnected connections; disconnect events to prevent slow buildup. ([[2021-01-23 - Roblox Performance Tutorial (Microprofiler, Developer Stats, Developer|Roblox Performance Tutorial (Microprofiler, Develo]])
- 2021-01-23 [3:16](https://youtu.be/-PPg4N5sKXE?t=196) Aim for CPU frame time of about 15-20 ms at best; investigate code and physics when it goes above that. ([[2021-01-23 - Roblox Performance Tutorial (Microprofiler, Developer Stats, Developer|Roblox Performance Tutorial (Microprofiler, Develo]])
- 2021-01-23 [3:57](https://youtu.be/-PPg4N5sKXE?t=237) Aim for GPU frame time around 13-20 ms on phone; GPU covers lighting, effects, textures and the whole map. ([[2021-01-23 - Roblox Performance Tutorial (Microprofiler, Developer Stats, Developer|Roblox Performance Tutorial (Microprofiler, Develo]])
- 2021-01-23 [5:37](https://youtu.be/-PPg4N5sKXE?t=337) Keep network sent well under 50 KB/s and optimise received traffic when it reaches 70; received rises when the server broadcasts events like gunfire to all clients. ([[2021-01-23 - Roblox Performance Tutorial (Microprofiler, Developer Stats, Developer|Roblox Performance Tutorial (Microprofiler, Develo]])
- 2021-01-23 [11:27](https://youtu.be/-PPg4N5sKXE?t=687) Look for high draw calls or too many shadows in the Microprofiler when a bar is too large; disabling shadows can shrink it. ([[2021-01-23 - Roblox Performance Tutorial (Microprofiler, Developer Stats, Developer|Roblox Performance Tutorial (Microprofiler, Develo]])
- 2021-01-23 [13:24](https://youtu.be/-PPg4N5sKXE?t=804) In Developer Console, read Place memory rather than Core memory; check graphics texture and character memory, which grows with player count. ([[2021-01-23 - Roblox Performance Tutorial (Microprofiler, Developer Stats, Developer|Roblox Performance Tutorial (Microprofiler, Develo]])
- 2021-01-23 [14:45](https://youtu.be/-PPg4N5sKXE?t=885) If texture memory is large, compress and shrink textures; many textures at compressed size is a red flag. ([[2021-01-23 - Roblox Performance Tutorial (Microprofiler, Developer Stats, Developer|Roblox Performance Tutorial (Microprofiler, Develo]])

Up: [[DevTechSpectrum - How to make successful Roblox games]]
