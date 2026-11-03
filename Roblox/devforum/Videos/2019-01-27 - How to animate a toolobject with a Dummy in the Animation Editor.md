---
title: "How to animate a tool/object with a Dummy in the Animation Editor"
url: https://devforum.roblox.com/t/how-to-animate-a-toolobject-with-a-dummy-in-the-animation-editor/232317
creator: Roblox DevForum
official: false
advice_density: medium
date: 2019-01-27
views: 777
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How to animate a tool/object with a Dummy in the Animation Editor

[Open](https://devforum.roblox.com/t/how-to-animate-a-toolobject-with-a-dummy-in-the-animation-editor/232317) | Roblox DevForum | 777 views | 2019-01-27

## Summary
Tutorial on animating a tool (e.g., a gun) with an R15 or R6 dummy in the Animation Editor. Covers preparing a Handle part, welding tool parts with a plugin, attaching the Handle to the RightHand/Right Arm via a Motor6D, and then animating the tool with the rig.

## Tips
- [page](https://devforum.roblox.com/t/how-to-animate-a-toolobject-with-a-dummy-in-the-animation-editor/232317) **[[building-art-and-assets]]** Create a Handle part in the Tool, set Transparency to 1 and CanCollide to false, and place it where the tool should be held from.
- [page](https://devforum.roblox.com/t/how-to-animate-a-toolobject-with-a-dummy-in-the-animation-editor/232317) **[[building-art-and-assets]]** Make the Handle the primary part; weld all other tool parts to it (not the Handle itself) so the tool doesn't fall apart while animating.
- [page](https://devforum.roblox.com/t/how-to-animate-a-toolobject-with-a-dummy-in-the-animation-editor/232317) **[[3d-modeling-rigging-and-animation]]** Attach the tool to the rig with a Motor6D named HandleMotor6D: Part0 = RightHand (R15) or Right Arm (R6), Part1 = the Handle.
- [page](https://devforum.roblox.com/t/how-to-animate-a-toolobject-with-a-dummy-in-the-animation-editor/232317) **[[3d-modeling-rigging-and-animation]]** Once attached, the Handle appears under RightArm in the Animation Editor; moving or rotating the Handle moves the whole tool.

## Tools
Roblox Studio Animation Editor, Rig Builder plugin, Weld plugin (weld selected parts to Handle), Motor6D

## He points to
- Weapon.rbxm example gun (attached to original post)
- AnimationTutorial.rbxl example file (attached to original post)

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
