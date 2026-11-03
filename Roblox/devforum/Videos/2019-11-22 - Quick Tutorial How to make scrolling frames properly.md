---
title: "Quick Tutorial: How to make scrolling frames properly"
url: https://devforum.roblox.com/t/quick-tutorial-how-to-make-scrolling-frames-properly/392792
creator: Roblox DevForum
official: false
advice_density: medium
date: 2019-11-22
views: 180
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Quick Tutorial: How to make scrolling frames properly

[Open](https://devforum.roblox.com/t/quick-tutorial-how-to-make-scrolling-frames-properly/392792) | Roblox DevForum | 180 views | 2019-11-22

## Summary
Beginner tutorial on making ScrollingFrames fit their content: read UIListLayout/UIGridLayout AbsoluteContentSize and set CanvasSize to it, updating via a function when content changes. Notes AutoCanvasSize as a newer alternative with issues.

## Tips
- [page](https://devforum.roblox.com/t/quick-tutorial-how-to-make-scrolling-frames-properly/392792) **[[ui-ux-design]]** Size ScrollingFrames with Offset rather than Scale, as the author recommends.
- [page](https://devforum.roblox.com/t/quick-tutorial-how-to-make-scrolling-frames-properly/392792) **[[ui-ux-design]]** Use UI constraints (UIListLayout/UIGridLayout) to lay out scrolling content; the author says to use them if you aren't already.
- [page](https://devforum.roblox.com/t/quick-tutorial-how-to-make-scrolling-frames-properly/392792) **[[ui-ux-design]]** Set ScrollingFrame.CanvasSize to the layout's AbsoluteContentSize X and Y so content neither overscrolls nor underscrolls.
- [page](https://devforum.roblox.com/t/quick-tutorial-how-to-make-scrolling-frames-properly/392792) **[[scripting-and-performance]]** For constantly changing UI like inventories or player lists, wrap the CanvasSize update in a function and call it whenever content changes.
- [page](https://devforum.roblox.com/t/quick-tutorial-how-to-make-scrolling-frames-properly/392792) **[[ui-ux-design]]** For static content like a store GUI, set CanvasSize once manually or via script.
- [page](https://devforum.roblox.com/t/quick-tutorial-how-to-make-scrolling-frames-properly/392792) **[[roblox-platform-changes]]** AutoCanvasSize may replace this manual method, but the author says it currently has issues and unclear whether it works in-game or only in Studio.

## Tools
UIListLayout, UIGridLayout, ScrollingFrame, Roblox Studio Luau

## He points to
- AutoCanvasSize property

## Topics
[[roblox-platform-changes]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
