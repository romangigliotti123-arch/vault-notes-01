---
title: "This makes your Roblox game slow, here’s how to fix it!"
url: https://youtu.be/xVUqKk3OnnU
creator: BubuTheDev
official: false
advice_density: low
date: 2024-09-07
views: 170
transcript: auto-captions
confidence: medium
tags: [roblox, bubuthedev, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.9
---

> [!note] Trust: TRUSTED (credibility audit score 7.9): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# This makes your Roblox game slow, here’s how to fix it!

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/xVUqKk3OnnU) | BubuTheDev | 170 views | 2024-09-07

## Summary
Shows how to replace a scripted Toolbox conveyor belt with a script-free version by setting the part's AssemblyLinearVelocity in Properties (e.g. X = -50, or Z for rotated belts). Claims this improves game performance. Very short video, no real revenue or growth advice.

## Tips
- [0:00](https://youtu.be/xVUqKk3OnnU?t=0) **[[optimization-and-streaming]]** Delete the Toolbox conveyor's per-0.1-second script; it runs constantly and is unnecessary for moving a belt.
- [0:41](https://youtu.be/xVUqKk3OnnU?t=41) **[[building-art-and-assets]]** Make a script-free conveyor by setting the belt part's AssemblyLinearVelocity in Properties to the axis speed (e.g. X = -50).
- [2:04](https://youtu.be/xVUqKk3OnnU?t=124) **[[building-and-level-design]]** If the belt is oriented on a different axis, set the velocity on that axis (e.g. Z = 50) instead; flip the sign if it moves the wrong way.

## Numbers
- [0:00](https://youtu.be/xVUqKk3OnnU?t=0) script loop interval in Toolbox conveyor: **every 0.1 seconds**
- [0:41](https://youtu.be/xVUqKk3OnnU?t=41) example conveyor velocity: **50 studs/s on X axis (sign reversed to -50)**

## Tools
Roblox Studio Toolbox, Properties window (AssemblyLinearVelocity)

## Topics
[[building-and-level-design]] [[building-art-and-assets]] [[optimization-and-streaming]]

Back to [[BubuTheDev - How to make successful Roblox games]]
