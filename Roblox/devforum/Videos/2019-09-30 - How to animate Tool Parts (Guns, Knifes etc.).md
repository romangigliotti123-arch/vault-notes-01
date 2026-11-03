---
title: "How to animate Tool Parts (Guns, Knifes etc.)"
url: https://devforum.roblox.com/t/how-to-animate-tool-parts-guns-knifes-etc/359484
creator: Roblox DevForum
official: false
advice_density: medium
date: 2019-09-30
views: 3063
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How to animate Tool Parts (Guns, Knifes etc.)

[Open](https://devforum.roblox.com/t/how-to-animate-tool-parts-guns-knifes-etc/359484) | Roblox DevForum | 3,063 views | 2019-09-30

## Summary
Headstackk's DevForum tutorial on animating Roblox tools (guns, knives) with a rig-based approach: create a BodyAttach root part, weld static parts and use Motor6Ds for moving parts, attach the tool via a Motor6D to Torso or arm, then wire up server/client scripts so the tool stays gripped in-game.

## Tips
- [page](https://devforum.roblox.com/t/how-to-animate-tool-parts-guns-knifes-etc/359484) **[[building-art-and-assets]]** Group all tool parts under a model with a BodyAttach root part near the trigger/grip; place the model under the animating rig dummy.
- [page](https://devforum.roblox.com/t/how-to-animate-tool-parts-guns-knifes-etc/359484) **[[building-art-and-assets]]** Use Constraint Editor plugin: select BodyAttach, Ctrl-click parts; New Motor6D for moving parts (magazine, bolt), New Weld for static parts. Every part needs a weld or Motor6D.
- [page](https://devforum.roblox.com/t/how-to-animate-tool-parts-guns-knifes-etc/359484) **[[3d-modeling-rigging-and-animation]]** Weld the tool to Torso rather than Right Arm if you want to animate the tool freely (reloads, knife tricks); arm-welded tools move with the arm.
- [page](https://devforum.roblox.com/t/how-to-animate-tool-parts-guns-knifes-etc/359484) **[[3d-modeling-rigging-and-animation]]** Make sure everything under the tool is unanchored, or parts will go missing when connected to the dummy.
- [page](https://devforum.roblox.com/t/how-to-animate-tool-parts-guns-knifes-etc/359484) **[[scripting-and-performance]]** Set RequireHandles to OFF on the Tool, otherwise the custom grip setup will not work in game.
- [page](https://devforum.roblox.com/t/how-to-animate-tool-parts-guns-knifes-etc/359484) **[[client-server-and-remotes]]** Server script: create a Motor6D 'ToolGrip' on each character's Torso at CharacterAdded and set Part1 to BodyAttach via ChildAdded; mirror it on the client for instant visual connection.
- [page](https://devforum.roblox.com/t/how-to-animate-tool-parts-guns-knifes-etc/359484) **[[building-art-and-assets]]** Play tool animations on Equipped and stop on Unequipped using a LocalScript under the tool, with Humanoid:LoadAnimation.

## Games
- **Weaponry**: Author's weapon framework game using detached magazines and moving bolts via Motor6D-animated tool parts.

## Tools
Roblox Rig Builder, Roblox Animation Editor, Constraint Editor plugin, Blender

## He points to
- Phantom Forces (advanced shooter framework reference)

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[client-server-and-remotes]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
