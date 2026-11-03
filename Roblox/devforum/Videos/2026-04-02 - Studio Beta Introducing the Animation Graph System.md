---
title: "[Studio Beta] Introducing the Animation Graph System"
url: https://devforum.roblox.com/t/studio-beta-introducing-the-animation-graph-system/4554788
creator: Roblox DevForum
official: false
advice_density: medium
date: 2026-04-02
views: 921
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# [Studio Beta] Introducing the Animation Graph System

[Open](https://devforum.roblox.com/t/studio-beta-introducing-the-animation-graph-system/4554788) | Roblox DevForum | 921 views | 2026-04-02

## Summary
Roblox DevForum announcement of the Animation Graph Studio Beta: a node-based editor for composing and blending character animation with less Luau. Covers enabling the beta, node library, parameters driven from scripts, known issues, and the Avatar Joint Upgrade timeline.

## Tips
- [page](https://devforum.roblox.com/t/studio-beta-introducing-the-animation-graph-system/4554788) **[[ai-and-tools]]** Enable via File > Beta Features > Animation Graph in Studio; open the Clip Editor (Animation Graph Editor) from the Avatar tab on a rig with an Animator.
- [page](https://devforum.roblox.com/t/studio-beta-introducing-the-animation-graph-system/4554788) **[[3d-modeling-rigging-and-animation]]** Keep using ACE (Animation Clip Editor) for creating clips and fine-tuning keyframes/curves; use the Graph Editor only to organize clips into logic.
- [page](https://devforum.roblox.com/t/studio-beta-introducing-the-animation-graph-system/4554788) **[[scripting-and-performance]]** Set graph parameters from Lua with track:SetParameter("Speed", value) instead of manually blending tracks in code.
- [page](https://devforum.roblox.com/t/studio-beta-introducing-the-animation-graph-system/4554788) **[[testing-debugging-and-qa]]** Use the real-time graph highlighting in Studio and the parameter sliders to test blending before writing any script.
- [page](https://devforum.roblox.com/t/studio-beta-introducing-the-animation-graph-system/4554788) **[[3d-modeling-rigging-and-animation]]** Test graphs with Avatar Joint Upgrade (AJU) enabled now, since the platform-wide transition is in May 2026.
- [page](https://devforum.roblox.com/t/studio-beta-introducing-the-animation-graph-system/4554788) **[[common-mistakes]]** Graphs do not play in-experience yet (Studio only); granting graph access does not grant access to its clip animations, so grant those separately.
- [page](https://devforum.roblox.com/t/studio-beta-introducing-the-animation-graph-system/4554788) **[[common-mistakes]]** Negative values are unsupported for Clip/Speed Speed properties and Add/Subtract Weight; avoid relying on them. AnimationId of ClipNode cannot be wired to a parameter.
- [page](https://devforum.roblox.com/t/studio-beta-introducing-the-animation-graph-system/4554788) **[[scripting-and-performance]]** Existing LoadAnimation scripts keep working; adopt the graph only where complex blending or sequencing justifies it.

## Numbers
- [page](https://devforum.roblox.com/t/studio-beta-introducing-the-animation-graph-system/4554788) Maximum nodes per animation graph: **No set maximum (performance work ongoing during beta)**
- [page](https://devforum.roblox.com/t/studio-beta-introducing-the-animation-graph-system/4554788) AJU platform-wide transition: **May 2026**

## Tools
Roblox Studio, Animation Graph Editor, Animation Clip Editor (ACE), Avatar Joint Upgrade (AJU)

## He points to
- MaximumADHD (graph image courtesy)
- Roblox documentation on Animation Graph

## Topics
[[3d-modeling-rigging-and-animation]] [[ai-and-tools]] [[common-mistakes]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
