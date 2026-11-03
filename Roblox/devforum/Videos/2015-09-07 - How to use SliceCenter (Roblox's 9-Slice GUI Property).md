---
title: "How to use SliceCenter (Roblox's 9-Slice GUI Property)"
url: https://devforum.roblox.com/t/how-to-use-slicecenter-robloxs-9-slice-gui-property/18313
creator: Roblox DevForum
official: false
advice_density: medium
date: 2015-09-07
views: 257
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How to use SliceCenter (Roblox's 9-Slice GUI Property)

[Open](https://devforum.roblox.com/t/how-to-use-slicecenter-robloxs-9-slice-gui-property/18313) | Roblox DevForum | 257 views | 2015-09-07

## Summary
Tutorial on using Roblox's 9-Slice GUI scaling: set ScaleType to Slice, then define SliceCenter as a Rect2D (X0,Y0,X1,Y1) forming the center box. Everything outside that box is a border that stretches correctly when the ImageLabel/ImageButton is resized.

## Tips
- [page](https://devforum.roblox.com/t/how-to-use-slicecenter-robloxs-9-slice-gui-property/18313) **[[ui-ux-design]]** For resizable GUI borders, set ImageLabel/ImageButton ScaleType to Slice so the image is sliced instead of stretched.
- [page](https://devforum.roblox.com/t/how-to-use-slicecenter-robloxs-9-slice-gui-property/18313) **[[ui-ux-design]]** SliceCenter is Rect2D (X0,Y0,X1,Y1); the two points define the center box. Everything outside it is border and follows 9-slice rules.
- [page](https://devforum.roblox.com/t/how-to-use-slicecenter-robloxs-9-slice-gui-property/18313) **[[building-art-and-assets]]** Design the template so corners stay fixed, side edges stretch in one direction, and the center stretches; example: 48x48 image with 6px borders gives a 36x36 center.

## Numbers
- [page](https://devforum.roblox.com/t/how-to-use-slicecenter-robloxs-9-slice-gui-property/18313) Example border width: **6 px per side on a 48x48 image (36x36 center)** (Example SliceCenter setup from the tutorial)

## Tools
Roblox Studio

## He points to
- Real World Illustrator: Understanding 9-Slice Scaling

## Topics
[[building-art-and-assets]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
