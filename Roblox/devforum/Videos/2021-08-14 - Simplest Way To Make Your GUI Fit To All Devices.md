---
title: "Simplest Way To Make Your GUI Fit To All Devices"
url: https://devforum.roblox.com/t/simplest-way-to-make-your-gui-fit-to-all-devices/1413727
creator: Roblox DevForum
official: false
advice_density: medium
date: 2021-08-14
views: 137
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Simplest Way To Make Your GUI Fit To All Devices

[Open](https://devforum.roblox.com/t/simplest-way-to-make-your-gui-fit-to-all-devices/1413727) | Roblox DevForum | 137 views | 2021-08-14

## Summary
Quick tutorial on making Roblox GUIs scale across devices: set AnchorPoint to 0.5,0.5, use a scaling plugin to rescale size and position, then optionally add UIAspectRatioConstraint to preserve aspect ratio on different screens (example uses iPhone 4S).

## Tips
- [page](https://devforum.roblox.com/t/simplest-way-to-make-your-gui-fit-to-all-devices/1413727) **[[ui-ux-design]]** Set a GUI element's AnchorPoint to 0.5,0.5 before rescaling so it stays centred; drag it back to its original position afterward.
- [page](https://devforum.roblox.com/t/simplest-way-to-make-your-gui-fit-to-all-devices/1413727) **[[ui-ux-design]]** Use a scaling plugin to rescale both Position and Size of selected UI so it fits different device resolutions.
- [page](https://devforum.roblox.com/t/simplest-way-to-make-your-gui-fit-to-all-devices/1413727) **[[ui-ux-design]]** Add UIAspectRatioConstraint to keep a frame's aspect ratio unchanged across devices; example 2:1 frame became 131x65 instead of distorted 131x90 on iPhone 4S.

## Numbers
- [page](https://devforum.roblox.com/t/simplest-way-to-make-your-gui-fit-to-all-devices/1413727) Example frame aspect ratio: **2:1 (300x150 base)** (Test frame on iPhone 4S without constraint became 131x90)
- [page](https://devforum.roblox.com/t/simplest-way-to-make-your-gui-fit-to-all-devices/1413727) Example frame with UIAspectRatioConstraint: **131x65 (closest to 2:1)** (Test frame on iPhone 4S with constraint)

## Tools
UIAspectRatioConstraint, Scaling plugin (unnamed, by Ascetis)

## Topics
[[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
