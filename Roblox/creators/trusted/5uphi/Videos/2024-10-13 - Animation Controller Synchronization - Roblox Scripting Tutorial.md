---
title: "Animation Controller Synchronization - Roblox Scripting Tutorial"
url: https://youtu.be/AkF-4x7qfzM
creator: Suphi Kaner
official: false
advice_density: medium
date: 2024-10-13
views: 11203
transcript: auto-captions
confidence: high
tags: [roblox, 5uphi, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.8
---

> [!note] Trust: TRUSTED (credibility audit score 8.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Animation Controller Synchronization - Roblox Scripting Tutorial

[Watch](https://youtu.be/AkF-4x7qfzM) | 5uphi | 11,203 views | 2024-10-13

## Summary
Roblox scripting tutorial on the Animation Editor and AnimationTrack behaviour. Covers whether late-joining or lagged clients stay in sync (they don't skip frames, so they lag slightly), paused vs stopped CPU cost (no difference), and building a client-side animated door driven by attributes with buffer keyframes.

## Tips
- [0:00](https://youtu.be/AkF-4x7qfzM?t=0) **[[core-loops-and-game-design]]** Keep each keyframe rotation delta under 180°; animations always take the shortest path, so a 360° jump between keys does not move at all.
- [4:12](https://youtu.be/AkF-4x7qfzM?t=252) **[[building-art-and-assets]]** Split large rotations into several small keyframes (e.g. 72° steps applied twice) because Studio's rotation input misreads large angles.
- [7:45](https://youtu.be/AkF-4x7qfzM?t=465) **[[scripting-and-performance]]** Set track speed to 1 / desired seconds (e.g. 1/10 for a 10-second cycle) so the timing is easy to tune.
- [11:44](https://youtu.be/AkF-4x7qfzM?t=704) **[[client-server-and-remotes]]** Expect clients to run slightly behind the server; Roblox won't skip frames to catch up, which keeps animations smooth for late joiners.
- [16:37](https://youtu.be/AkF-4x7qfzM?t=997) **[[client-server-and-remotes]]** Don't rely on exact animation sync across clients; design so small offsets are invisible, e.g. hold a dead zone at the open position.
- [18:57](https://youtu.be/AkF-4x7qfzM?t=1137) **[[scripting-and-performance]]** A paused track and a stopped track cost the same CPU (~6 ms in the test), so pausing is not a performance optimisation.
- [20:00](https://youtu.be/AkF-4x7qfzM?t=1200) **[[client-server-and-remotes]]** Avoid dead zones and linear easing when testing sync: abrupt motion makes desync visible, so use it to find bugs before shipping.
- [22:44](https://youtu.be/AkF-4x7qfzM?t=1364) **[[testing-debugging-and-qa]]** Simulate lag with Studio Settings > Network > incoming replication lag and sudden ping changes to reproduce desync bugs.
- [24:06](https://youtu.be/AkF-4x7qfzM?t=1446) **[[client-server-and-remotes]]** Drive animations on the client from a replicated attribute (e.g. open/time) via GetAttributeChangedSignal, not from a server-played track, so each client plays its own synced copy.
- [35:18](https://youtu.be/AkF-4x7qfzM?t=2118) **[[building-art-and-assets]]** Add buffer keyframes past the start and end markers; without them the track reaches its end and stops, snapping objects back.
- [41:31](https://youtu.be/AkF-4x7qfzM?t=2491) **[[core-loops-and-game-design]]** Check animation marker times (stored as strings) with tostring or tonumber before comparing; string vs number mismatches break logic silently.
- [44:15](https://youtu.be/AkF-4x7qfzM?t=2655) **[[building-art-and-assets]]** Animation keyframes only play forward; if reversing from a point, add keyframes covering that path rather than relying on events.
- [46:07](https://youtu.be/AkF-4x7qfzM?t=2767) **[[scripting-and-performance]]** Client-side animation logic can be moved to the server if you need authoritative door state; the client version is shown for lower cost.

## Numbers
- [4:12](https://youtu.be/AkF-4x7qfzM?t=252) Rotation keyframe spin: **360° in 1 s, playback speed 0.25 for slower spin** (Spinning part test with looping animation)
- [7:45](https://youtu.be/AkF-4x7qfzM?t=465) Rotation steps: **1440° per second split into 10 steps of 144°, applied as 2×72°** (Part spiralling around center four times per rotation)
- [11:23](https://youtu.be/AkF-4x7qfzM?t=683) Playback speed formula: **speed = 1 / seconds per cycle (e.g. 10 s = 0.1)** (Adjusting AnimationTrack speed for timing)
- [14:28](https://youtu.be/AkF-4x7qfzM?t=868) Late-joiner sync: **Late joiners sync to same position as others when paused or playing** (Tested in local server with one client)
- [18:57](https://youtu.be/AkF-4x7qfzM?t=1137) CPU cost: **~6 ms, same for paused and stopped tracks** (Test loop of cloned models in Studio)
- [22:44](https://youtu.be/AkF-4x7qfzM?t=1364) Simulated incoming replication lag: **1 s (door opens 1 s later on client)** (Studio Settings network test)
- [29:42](https://youtu.be/AkF-4x7qfzM?t=1782) Keyframe times used for door markers: **Marker times 0, 0.4, 0.5, 0.8, 0.1, 0.9** (Buffered start and end markers for bidirectional door)

## Tools
Roblox Studio, Avatar Animation Editor, AnimationTrack / Animator API, Studio Test tab (local server + client), Studio Settings > Network, ProximityPrompt, Attributes

## Topics
[[building-art-and-assets]] [[client-server-and-remotes]] [[core-loops-and-game-design]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[5uphi - How to make successful Roblox games]]
