---
title: "Optimizing Tweens - Roblox Scripting Tutorial"
url: https://youtu.be/ZJnMimf9n5Y
creator: Suphi Kaner
official: false
advice_density: medium
date: 2023-02-27
views: 45512
transcript: auto-captions
confidence: high
tags: [roblox, 5uphi, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.8
---

> [!note] Trust: TRUSTED (credibility audit score 8.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Optimizing Tweens - Roblox Scripting Tutorial

[Watch](https://youtu.be/ZJnMimf9n5Y) | 5uphi | 45,512 views | 2023-02-27

## Summary
Technical tutorial on optimizing Roblox tweens. Shows server-side tweens replicate property changes each frame (network ~1.66 KB/s vs 0.16 idle), then moves tweening to the client via a RemoteEvent-driven module. Covers handling repeat/reverse/delay to sync server state, and cancelling stale task.delay threads when a new tween starts.

## Tips
- [0:00](https://youtu.be/ZJnMimf9n5Y?t=0) **[[scripting-and-performance]]** Server-side tweens replicate every property change to all clients; this cost showed as network incoming rising from ~0.16 to ~1.66 KB/s in the video's test.
- [2:46](https://youtu.be/ZJnMimf9n5Y?t=166) **[[client-server-and-remotes]]** Fire a RemoteEvent with the instance, TweenInfo as a table, and properties, then tween locally on each client to avoid constant network updates.
- [4:09](https://youtu.be/ZJnMimf9n5Y?t=249) **[[client-server-and-remotes]]** TweenInfo cannot be sent over a RemoteEvent; convert it to a plain table and rebuild with TweenInfo.new(unpack(table)) on the client.
- [8:59](https://youtu.be/ZJnMimf9n5Y?t=539) **[[client-server-and-remotes]]** Wait for the player to load (e.g. task.wait(5)) before firing remote-driven tweens at server start, or the event fires before clients are ready.
- [13:13](https://youtu.be/ZJnMimf9n5Y?t=793) **[[scripting-and-performance]]** Create TweenInfo once at the top of the script and reuse it rather than rebuilding it on every trigger.
- [15:18](https://youtu.be/ZJnMimf9n5Y?t=918) **[[scripting-and-performance]]** Skip server-side property setting when TweenInfo.Reverses is true, since the instance returns to its original state; return early when RepeatCount is -1 (infinite).
- [16:41](https://youtu.be/ZJnMimf9n5Y?t=1001) **[[scripting-and-performance]]** Total tween duration = (DelayTime + Time) * (RepeatCount + 1); use this to schedule the server-side state sync with task.delay.
- [18:02](https://youtu.be/ZJnMimf9n5Y?t=1082) **[[scripting-and-performance]]** After the tween duration, set the final properties on the server so server and client state match once the tween ends.
- [19:25](https://youtu.be/ZJnMimf9n5Y?t=1165) **[[scripting-and-performance]]** task.delay cannot be cancelled by a new tween on its own; store the returned thread per instance and cancel it before starting a new tween to avoid stale property sets.

## Numbers
- [0:40](https://youtu.be/ZJnMimf9n5Y?t=40) Incoming network (server tween): **~1.66 KB/s while tweening vs ~0.16 KB/s idle** (Measured in View > Network Stats with server-side tween running)
- [9:42](https://youtu.be/ZJnMimf9n5Y?t=582) Incoming network (client tween): **stays ~0.16 KB/s while tweening** (Same part tweened locally via RemoteEvent)
- [15:59](https://youtu.be/ZJnMimf9n5Y?t=959) Tween duration formula: **(delay + time) × (repeatCount + 1)** (Example: 0+3 = 3 seconds for one non-repeating tween)

## Tools
TweenService, RemoteEvent, task.delay, task.wait, ProximityPrompt, Network Stats (View tab)

## Topics
[[client-server-and-remotes]] [[scripting-and-performance]]

Back to [[5uphi - How to make successful Roblox games]]
