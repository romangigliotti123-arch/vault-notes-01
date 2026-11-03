---
title: "Simple Message Queue for Server to Client Messages"
url: https://youtu.be/zmTsh66uxsI
creator: SimTek Game Development
official: false
advice_density: medium
date: 2023-01-07
views: 1716
transcript: auto-captions
confidence: high
tags: [roblox, simtekgamedevelopment, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Simple Message Queue for Server to Client Messages

[Watch](https://youtu.be/zmTsh66uxsI) | SimTekGameDevelopment | 1,716 views | 2023-01-07

## Summary
Builds a simple server-to-client message queue in Roblox. Server fires RemoteEvent messages in a burst; client LocalScript stores them in a table used as a first-in-first-out queue, then a processing thread pulls one message per second and shows each as a tweened TextLabel that slides up off screen.

## Tips
- [0:46](https://youtu.be/zmTsh66uxsI?t=46) **[[client-server-and-remotes]]** Create a RemoteEvent in ReplicatedStorage and connect on both server and client; both sides must reference the same remote.
- [3:57](https://youtu.be/zmTsh66uxsI?t=237) **[[code-architecture-and-frameworks]]** Use a table as a FIFO queue: table.insert to add at end, read index 1, then table.remove(queue, 1) to dequeue.
- [7:22](https://youtu.be/zmTsh66uxsI?t=442) **[[scripting-and-performance]]** Run the infinite queue-processing loop in task.spawn so it does not block the rest of the script.
- [11:23](https://youtu.be/zmTsh66uxsI?t=683) **[[ui-ux-design]]** Clone a hidden template label per message and parent it to the same ScreenGui as the script, so messages display sequentially instead of all at once.
- [12:47](https://youtu.be/zmTsh66uxsI?t=767) **[[ui-ux-design]]** Tween the label with TweenInfo: about 1s duration, Quad easing, Out direction, and a ~2s delay so players can read it before it moves off screen.
- [16:14](https://youtu.be/zmTsh66uxsI?t=974) **[[ui-ux-design]]** Wait for Tween.Completed then Destroy the label to avoid cluttering the client GUI.
- [17:36](https://youtu.be/zmTsh66uxsI?t=1056) **[[client-server-and-remotes]]** RemoteEvent delivery is asynchronous, so arrival order is not guaranteed; a queue preserves order only among messages already received.

## Numbers
- [2:07](https://youtu.be/zmTsh66uxsI?t=127) Wait before firing messages: **5 seconds after PlayerAdded** (Test delay so player sees the world before messages fire)
- [6:42](https://youtu.be/zmTsh66uxsI?t=402) Queue poll interval: **1 second** (Client loop checks queue every second)
- [13:28](https://youtu.be/zmTsh66uxsI?t=808) Tween duration and delay: **1s tween, 2s delay** (Label slides off screen after a 2 second read delay)

## Tools
Roblox Studio, RemoteEvent, table.insert / table.remove, TweenService, TweenInfo

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[SimTekGameDevelopment - How to make successful Roblox games]]
