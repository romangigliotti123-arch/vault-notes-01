---
title: "Create a REALISTIC First-Person ITEM SYSTEM for Roblox HORROR Games | Viewmodels"
url: https://youtu.be/2HRX5AqBfNA
creator: PineappleDev
official: false
advice_density: medium
date: 2025-01-24
views: 21103
transcript: auto-captions
confidence: medium
tags: [roblox, pineappledevv, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Create a REALISTIC First-Person ITEM SYSTEM for Roblox HORROR Games | Viewmodels

[Watch](https://youtu.be/2HRX5AqBfNA) | pineappledevv | 21,103 views | 2025-01-24

## Summary
Tutorial on building a first-person viewmodel item system for Roblox: a LocalScript in StarterCharacterScripts clones a viewmodel from ReplicatedStorage onto the camera, follows the camera with bob/sway, and hides the real tool locally. Covers viewmodel setup (anchored handle, welded parts, offset attribute) and client/server scripting split.

## Tips
- [8:40](https://youtu.be/2HRX5AqBfNA?t=520) **[[building-art-and-assets]]** Group viewmodel meshes under a Model named exactly like the Tool, with a part called Handle; anchor only the Handle and weld everything else to it.
- [9:21](https://youtu.be/2HRX5AqBfNA?t=561) **[[building-art-and-assets]]** Set the viewmodel's PrimaryPart to the Handle, and store a CFrame 'offset' attribute on the model so you can tune position live in-game.
- [10:02](https://youtu.be/2HRX5AqBfNA?t=602) **[[building-art-and-assets]]** Tune viewmodel offset by changing the attribute while playtesting; fix backwards orientation by adjusting the offset's rotation.
- [5:09](https://youtu.be/2HRX5AqBfNA?t=309) **[[scripting-and-performance]]** Put the viewmodel controller in a LocalScript under StarterCharacterScripts so it runs on each spawn and only handles the local player.
- [5:52](https://youtu.be/2HRX5AqBfNA?t=352) **[[scripting-and-performance]]** Clone the viewmodel into workspace.CurrentCamera so only the local player sees it, and start it below view to fake pulling the item out of a pocket.
- [6:33](https://youtu.be/2HRX5AqBfNA?t=393) **[[building-art-and-assets]]** Set LocalTransparencyModifier to 1 on the real tool's BaseParts so the world tool is hidden for the holder while the viewmodel shows.
- [7:13](https://youtu.be/2HRX5AqBfNA?t=433) **[[scripting-and-performance]]** Clean up on unequip by destroying the cloned viewmodel and clearing the reference, so no stale viewmodels remain on the camera.
- [7:55](https://youtu.be/2HRX5AqBfNA?t=475) **[[vfx-and-particles]]** Lerp the viewmodel CFrame toward the target each RenderStepped frame with a smoothing factor so it lags the camera slightly and feels less stuck to the screen.
- [11:50](https://youtu.be/2HRX5AqBfNA?t=710) **[[client-server-and-remotes]]** Viewmodels exist only on the client, so item effects (light on/off, animations) must be applied in both a server Script for the real tool and a LocalScript for the viewmodel.

## Numbers
- [2:25](https://youtu.be/2HRX5AqBfNA?t=145) Bob/sway starting values: **Bob speed 1.5, distance 0.1, walk multi 3, velocity threshold 9, sway speed 1.1, sway distance 0.7, sway multi 2, smoothing 50** (Starting values for viewmodel bob and sway script)

## Tools
Roblox Studio, Luau, RunService.RenderStepped, CurrentCamera

## He points to
- Previous first-person tutorial by the same creator (linked in description)
- Code links in video description

## Topics
[[building-art-and-assets]] [[client-server-and-remotes]] [[scripting-and-performance]] [[vfx-and-particles]]

Back to [[pineappledevv - How to make successful Roblox games]]
