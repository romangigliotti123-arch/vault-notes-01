---
title: "How to think about CFrames"
url: https://devforum.roblox.com/t/how-to-think-about-cframes/11743
creator: Roblox DevForum
official: false
advice_density: low
date: 2015-01-03
views: 371
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How to think about CFrames

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/how-to-think-about-cframes/11743) | Roblox DevForum | 371 views | 2015-01-03

## Summary
Explains CFrame internals in Roblox: the 12 components (position plus right, top, back unit direction vectors forming a rotation matrix), and how CFrame * Vector3 and CFrame:inverse() * Vector3 convert between local and world coordinates, with hand-coded equivalents using dot products.

## Tips
- [page](https://devforum.roblox.com/t/how-to-think-about-cframes/11743) **[[scripting-and-performance]]** Use CFrame:components() to read raw values when doing custom math; it is faster than repeated CFrame operations in hot code.
- [page](https://devforum.roblox.com/t/how-to-think-about-cframes/11743) **[[scripting-and-performance]]** Remember the Right, Top, Back vectors are directions (unit length), not face-center positions.
- [page](https://devforum.roblox.com/t/how-to-think-about-cframes/11743) **[[luau-language-and-types]]** Use CFrame * Vector3 to convert local offsets to world space and CFrame:inverse() * Vector3 to convert world positions into a CFrame's local space.
- [page](https://devforum.roblox.com/t/how-to-think-about-cframes/11743) **[[common-mistakes]]** Do not treat the Right/Top/Back vectors as positions; they only encode orientation, and the position is CFrame.p alone.

## Numbers
- [page](https://devforum.roblox.com/t/how-to-think-about-cframes/11743) CFrame components: **12 numbers: 1 position (x,y,z) plus 3 unit direction vectors (9 values)** (Full CFrame:components() output structure)

## Tools
CFrame:components(), CFrame:inverse()

## Topics
[[common-mistakes]] [[luau-language-and-types]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
