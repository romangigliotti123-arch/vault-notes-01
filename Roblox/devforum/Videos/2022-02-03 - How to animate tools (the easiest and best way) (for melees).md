---
title: "How to animate tools (the easiest and best way) (for melees)"
url: https://devforum.roblox.com/t/how-to-animate-tools-the-easiest-and-best-way-for-melees/1654589
creator: Roblox DevForum
official: false
advice_density: medium
date: 2022-02-03
views: 344
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How to animate tools (the easiest and best way) (for melees)

[Open](https://devforum.roblox.com/t/how-to-animate-tools-the-easiest-and-best-way-for-melees/1654589) | Roblox DevForum | 344 views | 2022-02-03

## Summary
Tutorial on animating Roblox tools (melee weapons): group weapon parts welded to an invisible Handle, use Tool Grip Editor and Reclass to convert the dummy's Right Grip Weld into a Motor6D, animate the Handle in Moon Animator, and script the Motor6D on equip/unequip.

## Tips
- [page](https://devforum.roblox.com/t/how-to-animate-tools-the-easiest-and-best-way-for-melees/1654589) **[[building-art-and-assets]]** Group all weapon parts and meshes, add an invisible part named Handle directly under the Tool (not the model), and weld everything to it.
- [page](https://devforum.roblox.com/t/how-to-animate-tools-the-easiest-and-best-way-for-melees/1654589) **[[building-art-and-assets]]** Use the Tool Grip Editor plugin to align how the character holds the weapon before animating.
- [page](https://devforum.roblox.com/t/how-to-animate-tools-the-easiest-and-best-way-for-melees/1654589) **[[3d-modeling-rigging-and-animation]]** Convert the dummy's Right Grip weld to a Motor6D with Reclass; the Handle then appears as a body part under the right arm/hand in the animation editor.
- [page](https://devforum.roblox.com/t/how-to-animate-tools-the-easiest-and-best-way-for-melees/1654589) **[[3d-modeling-rigging-and-animation]]** Moon Animator reportedly works best for animating tools, per the author.
- [page](https://devforum.roblox.com/t/how-to-animate-tools-the-easiest-and-best-way-for-melees/1654589) **[[client-server-and-remotes]]** On Equipped, replace the RightGrip Weld with a Motor6D copying Part0, Part1, C0 and C1; on Unequipped, destroy it so the animation can drive the Handle.
- [page](https://devforum.roblox.com/t/how-to-animate-tools-the-easiest-and-best-way-for-melees/1654589) **[[combat-and-gameplay-systems]]** Redo the Motor6D swap every time the tool is equipped; delete the old Motor6D first to avoid stale grips.

## Tools
Moon Animator, Reclass plugin, Tool Grip Editor plugin

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[client-server-and-remotes]] [[combat-and-gameplay-systems]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
