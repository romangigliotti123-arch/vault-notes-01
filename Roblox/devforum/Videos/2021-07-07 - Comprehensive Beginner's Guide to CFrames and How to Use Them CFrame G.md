---
title: "Comprehensive Beginner's Guide to CFrames and How to Use Them [CFrame Guide]"
url: https://devforum.roblox.com/t/comprehensive-beginners-guide-to-cframes-and-how-to-use-them-cframe-guide/1334085
creator: Roblox DevForum
official: false
advice_density: low
date: 2021-07-07
views: 138
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Comprehensive Beginner's Guide to CFrames and How to Use Them [CFrame Guide]

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/comprehensive-beginners-guide-to-cframes-and-how-to-use-them-cframe-guide/1334085) | Roblox DevForum | 138 views | 2021-07-07

## Summary
Beginner's guide to CFrames in Roblox: coordinate frames, how Position/Orientation relate to CFrame, and core CFrame operations (+, *, Lerp, Inverse, PointToWorldSpace/ObjectSpace) and constructors (new, Angles, lookAt) with examples for positioning parts relative to other parts and aiming cameras.

## Tips
- [page](https://devforum.roblox.com/t/comprehensive-beginners-guide-to-cframes-and-how-to-use-them-cframe-guide/1334085) **[[scripting-and-performance]]** Use CFrame.lookAt(pos, target) to position and aim cameras or parts in one line instead of manual rotation math.
- [page](https://devforum.roblox.com/t/comprehensive-beginners-guide-to-cframes-and-how-to-use-them-cframe-guide/1334085) **[[building-art-and-assets]]** Use part.CFrame:PointToWorldSpace(Vector3.new(0,5,0)) to place a part relative to a rotated part, rather than adding vectors to Position.
- [page](https://devforum.roblox.com/t/comprehensive-beginners-guide-to-cframes-and-how-to-use-them-cframe-guide/1334085) **[[scripting-and-performance]]** CFrame.Angles takes radians and applies rotations in Z, Y, X order; Orientation on parts uses degrees and Y, X, Z order. Don't mix them up.
- [page](https://devforum.roblox.com/t/comprehensive-beginners-guide-to-cframes-and-how-to-use-them-cframe-guide/1334085) **[[scripting-and-performance]]** Rotation order matters: rotating by the same angles in a different order gives a different orientation.

## Numbers
- [page](https://devforum.roblox.com/t/comprehensive-beginners-guide-to-cframes-and-how-to-use-them-cframe-guide/1334085) CFrame components: **12 numbers (position + three axis direction vectors)** (Full CFrame encoding; rarely needed in practice, constructors preferred)
- [page](https://devforum.roblox.com/t/comprehensive-beginners-guide-to-cframes-and-how-to-use-them-cframe-guide/1334085) Angles units: **radians (CFrame.Angles) vs degrees (Orientation)** (Different units between constructor and part property)

## Tools
CFrame, Vector3, Attachment

## Topics
[[building-art-and-assets]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
