---
title: "A Couple of Advanced CFrame Tricks"
url: https://devforum.roblox.com/t/a-couple-of-advanced-cframe-tricks/337682
creator: Roblox DevForum
official: false
advice_density: low
date: 2019-08-24
views: 498
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# A Couple of Advanced CFrame Tricks

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/a-couple-of-advanced-cframe-tricks/337682) | Roblox DevForum | 498 views | 2019-08-24

## Summary
EgoMoose's DevForum post on advanced CFrame techniques: computing the shortest rotation between two vectors (plain, lerp, and quaternion methods), surface-aligned CFrames, swing-twist decomposition for measuring spin around an axis (e.g. camera matching a spinning platform), and finding a center of rotation from two CFrames. Code-heavy, no game-business advice.

## Tips
- [page](https://devforum.roblox.com/t/a-couple-of-advanced-cframe-tricks/337682) **[[scripting-and-performance]]** Use the quaternion trick for rotation between vectors: add [1+dot, cross] and let the CFrame constructor normalize; cheaper and more robust than acos/fromAxisAngle.
- [page](https://devforum.roblox.com/t/a-couple-of-advanced-cframe-tricks/337682) **[[scripting-and-performance]]** Guard the opposite-vector case (dot < -0.99999) separately with a backup axis; the quaternion sum is zero there and cannot be normalized.
- [page](https://devforum.roblox.com/t/a-couple-of-advanced-cframe-tricks/337682) **[[scripting-and-performance]]** Measure spin around an axis with swing-twist decomposition on the delta CFrame rather than the part's delta CFrame; this avoids errors from wobbling parts.
- [page](https://devforum.roblox.com/t/a-couple-of-advanced-cframe-tricks/337682) **[[client-server-and-remotes]]** For a camera matching a spinning platform, update the spin each frame on RunService Heartbeat and reset delta to 0 when the player switches the part they stand on.

## Tools
Roblox CFrame API (fromAxisAngle, ToAxisAngle, Lerp), RunService.Heartbeat

## Topics
[[client-server-and-remotes]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
