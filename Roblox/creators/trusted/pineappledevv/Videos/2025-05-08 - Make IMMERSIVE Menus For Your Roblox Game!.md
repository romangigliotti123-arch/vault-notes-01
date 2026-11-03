---
title: "Make IMMERSIVE Menus For Your Roblox Game!"
url: https://youtu.be/Iz2ljOdZRJI
creator: PineappleDev
official: false
advice_density: low
date: 2025-05-08
views: 2631
transcript: auto-captions
confidence: high
tags: [roblox, pineappledevv, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Make IMMERSIVE Menus For Your Roblox Game!

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/Iz2ljOdZRJI) | pineappledevv | 2,631 views | 2025-05-08

## Summary
Tutorial for adding immersive menu effects in Roblox: a shared ModuleScript tweens Lighting Blur and camera FOV when a menu opens or closes, plays a UI sound, and is wired to a button and close X via a LocalScript. Includes a downloadable model option.

## Tips
- [0:17](https://youtu.be/Iz2ljOdZRJI?t=17) **[[ui-ux-design]]** Structure menus as one Frame containing all menu contents so a single visibility toggle opens and closes the whole menu.
- [1:35](https://youtu.be/Iz2ljOdZRJI?t=95) **[[code-architecture-and-frameworks]]** Keep a dictionary of menu name to frame in a shared ModuleScript so open/close functions work for any menu by name.
- [2:16](https://youtu.be/Iz2ljOdZRJI?t=136) **[[ui-ux-design]]** Read the default FOV from the camera at runtime and add an offset (e.g. +20) so you can tweak FOV without editing the script.
- [2:16](https://youtu.be/Iz2ljOdZRJI?t=136) **[[ui-ux-design]]** Store the default blur size in a variable instead of hardcoding zero so existing background blur isn't wiped when menus close.

## Numbers
- [2:16](https://youtu.be/Iz2ljOdZRJI?t=136) Menu FOV offset: **+20 from default FOV (tutorial example)** (Camera FOV increase when a menu is open)
- [3:41](https://youtu.be/Iz2ljOdZRJI?t=221) Blur size when menu open: **18** (Lighting Blur size while menu open; default 0)
- [2:58](https://youtu.be/Iz2ljOdZRJI?t=178) TweenInfo duration: **5 (as typed in video, likely 0.5s)** (Tween duration used for all menu tweens)

## Tools
Roblox Studio, TweenService, Lighting Blur effect, Luau ModuleScript

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[player-psychology-and-game-feel]] [[ui-ux-design]] [[vfx-and-particles]]

Back to [[pineappledevv - How to make successful Roblox games]]
