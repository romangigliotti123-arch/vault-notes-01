---
title: "Introduction to Tweening Models"
url: https://devforum.roblox.com/t/introduction-to-tweening-models/315253
creator: Roblox DevForum
official: false
advice_density: medium
date: 2019-07-24
views: 876
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Introduction to Tweening Models

[Open](https://devforum.roblox.com/t/introduction-to-tweening-models/315253) | Roblox DevForum | 876 views | 2019-07-24

## Summary
Tutorial on tweening Roblox models: treat the model as a proxy root part, weld unanchored parts to an anchored root, and tween the root's CFrame with TweenService. Covers root orientation checks, WeldConstraints over Weld, and why SetPrimaryPartCFrame and CFrameValue proxies are discouraged.

## Tips
- [page](https://devforum.roblox.com/t/introduction-to-tweening-models/315253) **[[building-and-level-design]]** Choose a root that forms a bounding box over the model for accurate moves, or a invisible hinge pole for swinging doors matching the model's full height.
- [page](https://devforum.roblox.com/t/introduction-to-tweening-models/315253) **[[building-art-and-assets]]** Verify root orientation before rigging: green (top) arrow must point up; red (right) and blue (front) define axes. Use Handles in the command bar to check.
- [page](https://devforum.roblox.com/t/introduction-to-tweening-models/315253) **[[building-art-and-assets]]** Weld parts in Studio rather than live servers to avoid slightly displaced parts in running servers.
- [page](https://devforum.roblox.com/t/introduction-to-tweening-models/315253) **[[client-server-and-remotes]]** Anchor the root, unanchor the rest, and weld parts with WeldConstraints; welded unanchored parts are not physically simulated, so performance is safe.
- [page](https://devforum.roblox.com/t/introduction-to-tweening-models/315253) **[[scripting-and-performance]]** Tween the root's CFrame, not its Position; welds only propagate CFrame changes to other parts.
- [page](https://devforum.roblox.com/t/introduction-to-tweening-models/315253) **[[scripting-and-performance]]** Use TweenService directly for model tweens; avoid CFrameValue proxies with SetPrimaryPartCFrame, which add overhead and fail without a PrimaryPart.
- [page](https://devforum.roblox.com/t/introduction-to-tweening-models/315253) **[[scripting-and-performance]]** Avoid SetPrimaryPartCFrame for repeated moves: floating-point offset errors accumulate and tear models apart over time (deprecated; use Pivot API).
- [page](https://devforum.roblox.com/t/introduction-to-tweening-models/315253) **[[building-art-and-assets]]** Prefer WeldConstraint over Weld: it needs no C0/C1 offsets and welds relative position automatically. Use Motor6D only for animation joints.
- [page](https://devforum.roblox.com/t/introduction-to-tweening-models/315253) **[[common-mistakes]]** Don't use the CFrameValue-plus-SetPrimaryPartCFrame legacy pattern; the author says it's fragile and should not be accepted as a solution.

## Numbers
- [page](https://devforum.roblox.com/t/introduction-to-tweening-models/315253) Tween step: **Tween CFrame (radians for CFrame.Angles)** (Rotation example uses math.rad(180) on the root CFrame)

## Tools
TweenService, WeldConstraint, Handles (command bar script for axis check), Constraint viewer

## He points to
- Roblox official 'Animating a Model' code sample on Creator Marketplace
- Thread: SetPrimaryPartCFrame() gradually offsets component parts (Engine Bugs)

## Topics
[[building-and-level-design]] [[building-art-and-assets]] [[client-server-and-remotes]] [[common-mistakes]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
