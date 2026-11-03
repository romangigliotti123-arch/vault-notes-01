---
title: "Animation Controller - Roblox Scripting Tutorial"
url: https://youtu.be/ZPviBfpPloE
creator: Suphi Kaner
official: false
advice_density: medium
date: 2024-10-10
views: 21032
transcript: auto-captions
confidence: medium
tags: [roblox, 5uphi, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.8
---

> [!note] Trust: TRUSTED (credibility audit score 8.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Animation Controller - Roblox Scripting Tutorial

[Watch](https://youtu.be/ZPviBfpPloE) | 5uphi | 21,032 views | 2024-10-10

## Summary
Compares three ways to make Roblox doors move: Animator keyframe animation, TweenService, and physics HingeConstraint. Benchmarks CPU and network use for each with 60 cloned doors. Animation shows lowest CPU and near-zero network during playback; tween is worst on both; physics throttles when pushed.

## Tips
- [0:05](https://youtu.be/ZPviBfpPloE?t=5) **[[building-and-level-design]]** Build the door as a Model with an anchored frame part and a slab part joined by a Motor6D; set C1/C0 offsets so the slab rotates around the frame edge, not its center.
- [8:26](https://youtu.be/ZPviBfpPloE?t=506) **[[ai-and-tools]]** Publish the Animation Editor keyframes to Roblox with 'Overwrite existing asset' to get an animation ID; later edits only need re-publishing, not a new ID.
- [7:01](https://youtu.be/ZPviBfpPloE?t=421) **[[scripting-and-performance]]** Add an animation event (e.g. 'pause') in the Animation Editor and connect GetMarkerReachedSignal to control timing from script; set AnimationTrack.Speed to 0 to pause.
- [19:05](https://youtu.be/ZPviBfpPloE?t=1145) **[[client-server-and-remotes]]** Animator tracks replicate only play state, not per-frame transforms; the client animates locally, so network use is near zero while playing. Prefer Animator over per-frame updates for many moving parts.
- [20:29](https://youtu.be/ZPviBfpPloE?t=1229) **[[optimization-and-streaming]]** Avoid TweenService on server-owned parts with many instances: in the test it used ~60ms CPU and ~1,800 KB/s received data versus ~16ms and ~0 during animation playback.
- [21:54](https://youtu.be/ZPviBfpPloE?t=1314) **[[physics-pathfinding-and-npc-ai]]** HingeConstraint servo doors are cheap (~32ms CPU, ~41 KB/s) but Roblox throttles physics under load, causing lag and uneven timing; keep physics simulations small and few.
- [15:22](https://youtu.be/ZPviBfpPloE?t=922) **[[physics-pathfinding-and-npc-ai]]** Attach HingeConstraint attachments with a 90 degree rotation on the axis matching the door hinge, or the constraint rotates around the wrong axis.
- [16:44](https://youtu.be/ZPviBfpPloE?t=1004) **[[physics-pathfinding-and-npc-ai]]** Animated and tweened doors do not carry characters standing on them; physics doors do. Choose the method based on whether players should ride the moving part.
- [12:38](https://youtu.be/ZPviBfpPloE?t=758) **[[building-and-level-design]]** Tween easing like Cubic InOut gives natural acceleration; Animation editor keyframes with Elastic easing give spring-like motion; the speed is set at play time via AnimationTrack.

## Numbers
- [18:23](https://youtu.be/ZPviBfpPloE?t=1103) CPU usage (animation door, moving): **~16 ms (idle ~5)** (60 cloned doors in test, animation playback)
- [20:29](https://youtu.be/ZPviBfpPloE?t=1229) CPU usage (tween door, moving): **~60 ms (idle ~5)** (60 doors in test, tweened)
- [21:10](https://youtu.be/ZPviBfpPloE?t=1270) Received network data (tween door): **~1,800 KB/s while moving** (Tween replicates property changes constantly)
- [19:47](https://youtu.be/ZPviBfpPloE?t=1187) Received network data (animation door): **~100 KB spike at start, ~0 while playing** (Only play state replicates)
- [21:54](https://youtu.be/ZPviBfpPloE?t=1314) CPU and network (physics door): **~32 ms CPU, ~41 KB/s** (Hinge servo, angular speed 0.3 throttled; 3.3 fixes opening)
- [14:00](https://youtu.be/ZPviBfpPloE?t=840) Tween rotation angle: **-112.5 degrees** (Slab orientation read from keyframe; used for door opening)
- [10:30](https://youtu.be/ZPviBfpPloE?t=630) Loop timing: **10 s open, 10 s close** (Door demo loop with wait intervals)
- [15:22](https://youtu.be/ZPviBfpPloE?t=922) Attachment offsets: **0.5 frame, 3.5 slab** (Pivot at frame edge for hinge and Motor6D)

## Tools
Roblox Studio, Animation Editor, Motor6D, TweenService, HingeConstraint, Animator, AnimationTrack, Luau

## Topics
[[ai-and-tools]] [[building-and-level-design]] [[client-server-and-remotes]] [[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[5uphi - How to make successful Roblox games]]
