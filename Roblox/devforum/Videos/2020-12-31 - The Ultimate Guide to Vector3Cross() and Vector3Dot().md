---
title: "The Ultimate Guide to Vector3:Cross() and Vector3:Dot()"
url: https://devforum.roblox.com/t/the-ultimate-guide-to-vector3cross-and-vector3dot/953984
creator: Roblox DevForum
official: false
advice_density: low
date: 2020-12-31
views: 899
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# The Ultimate Guide to Vector3:Cross() and Vector3:Dot()

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/the-ultimate-guide-to-vector3cross-and-vector3dot/953984) | Roblox DevForum | 899 views | 2020-12-31

## Summary
Moonvane's tutorial explaining Vector3:Dot() and Vector3:Cross() for Roblox scripters. Dot measures directional alignment of two vectors (1 same, -1 opposite, 0 perpendicular). Cross returns a vector perpendicular to two inputs; order matters. Covers LookVector/RightVector/UpVector derivation and practical uses.

## Tips
- [page](https://devforum.roblox.com/t/the-ultimate-guide-to-vector3cross-and-vector3dot/953984) **[[luau-language-and-types]]** Use Vector3:Dot() on unit vectors to test facing: result 1 = same direction, -1 = opposite, 0 = perpendicular. Useful for 'only attack if facing NPC' checks.
- [page](https://devforum.roblox.com/t/the-ultimate-guide-to-vector3cross-and-vector3dot/953984) **[[luau-language-and-types]]** Clamp dot product to [-1, 1] before math.acos when computing angles, since floating point can push values slightly outside that range.
- [page](https://devforum.roblox.com/t/the-ultimate-guide-to-vector3cross-and-vector3dot/953984) **[[luau-language-and-types]]** Vector3:Cross() order matters: LookVector:Cross(UpVector) gives RightVector, while the reverse gives LeftVector. Swap operands to flip the result.
- [page](https://devforum.roblox.com/t/the-ultimate-guide-to-vector3cross-and-vector3dot/953984) **[[genre-mechanics]]** Dot can gate teleport-behind-player monsters so they only teleport when the player is not looking at them.

## Numbers
- [page](https://devforum.roblox.com/t/the-ultimate-guide-to-vector3cross-and-vector3dot/953984) Dot of parallel same-direction vectors: **1**
- [page](https://devforum.roblox.com/t/the-ultimate-guide-to-vector3cross-and-vector3dot/953984) Dot of opposite-direction vectors: **-1**
- [page](https://devforum.roblox.com/t/the-ultimate-guide-to-vector3cross-and-vector3dot/953984) Dot of perpendicular vectors: **0**

## Topics
[[genre-mechanics]] [[luau-language-and-types]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
