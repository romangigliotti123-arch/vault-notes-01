---
title: "How to think about Quaternions"
url: https://devforum.roblox.com/t/how-to-think-about-quaternions/143295
creator: Roblox DevForum
official: false
advice_density: low
date: 2018-07-05
views: 235
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How to think about Quaternions

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/how-to-think-about-quaternions/143295) | Roblox DevForum | 235 views | 2018-07-05

## Summary
EgoMoose's guide to quaternions for Roblox scripters. Explains single- and multi-axis quaternion rotation, double cover, quaternion twins for choosing SLERP direction, normalization in CFrame.new, and how CFrame SLERPs pick the shorter twin via dot product.

## Tips
- [page](https://devforum.roblox.com/t/how-to-think-about-quaternions/143295) **[[luau-language-and-types]]** Use quaternion twins (negate all components) to pick SLERP direction; flip only W when going the opposite way for a full 360-degree spin.
- [page](https://devforum.roblox.com/t/how-to-think-about-quaternions/143295) **[[scripting-and-performance]]** When blending rotations, pass unnormalized component weights to CFrame.new(0,0,0,X,Y,Z,W); it normalizes them onto the 4D unit sphere for you.
- [page](https://devforum.roblox.com/t/how-to-think-about-quaternions/143295) **[[scripting-and-performance]]** For custom slerp, choose the twin with positive dot product between start and end quaternions so the path is the shortest rotation.

## Numbers
- [page](https://devforum.roblox.com/t/how-to-think-about-quaternions/143295) Quaternion double cover: **Angle on the quaternion is twice the represented angle (e.g. 90 deg rotation uses (0.707,0.707))** (Single-axis quaternion rotation mapping)

## Tools
Roblox CFrame constructor with quaternion components, EgoMoose quaternion class (gist)

## Topics
[[luau-language-and-types]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
