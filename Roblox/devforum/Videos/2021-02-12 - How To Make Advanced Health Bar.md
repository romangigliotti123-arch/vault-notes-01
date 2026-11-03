---
title: "How To Make Advanced Health Bar"
url: https://devforum.roblox.com/t/how-to-make-advanced-health-bar/1042705
creator: Roblox DevForum
official: false
advice_density: low
date: 2021-02-12
views: 151
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How To Make Advanced Health Bar

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/how-to-make-advanced-health-bar/1042705) | Roblox DevForum | 151 views | 2021-02-12

## Summary
Tutorial for a client-side animated health bar in Roblox. A LocalScript in a ScreenGui frame uses TweenService to resize the bar whenever Humanoid Health or MaxHealth changes. The bar is visible only to the local player.

## Tips
- [page](https://devforum.roblox.com/t/how-to-make-advanced-health-bar/1042705) **[[ui-ux-design]]** Enable ResetOnSpawn on the health ScreenGui so it is recreated with each character spawn.
- [page](https://devforum.roblox.com/t/how-to-make-advanced-health-bar/1042705) **[[client-server-and-remotes]]** Place the health bar script in a LocalScript so only the local player sees the bar; it reads Humanoid values on the client.
- [page](https://devforum.roblox.com/t/how-to-make-advanced-health-bar/1042705) **[[ui-ux-design]]** Drive bar width with UDim2.fromScale(health ratio, 1) and clamp the ratio to 0-1 to avoid overflow.
- [page](https://devforum.roblox.com/t/how-to-make-advanced-health-bar/1042705) **[[ui-ux-design]]** Connect to Humanoid:GetPropertyChangedSignal for Health and MaxHealth so the bar updates on damage, healing and max changes.

## Tools
TweenService, LocalScript, ScreenGui

## Topics
[[client-server-and-remotes]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
