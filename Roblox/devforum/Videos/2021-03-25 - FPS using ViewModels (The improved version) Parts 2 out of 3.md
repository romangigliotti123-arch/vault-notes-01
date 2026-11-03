---
title: "FPS using ViewModels (The improved version) // Parts: 2 out of 3"
url: https://devforum.roblox.com/t/fps-using-viewmodels-the-improved-version-parts-2-out-of-3/1129877
creator: Roblox DevForum
official: false
advice_density: medium
date: 2021-03-25
views: 156
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# FPS using ViewModels (The improved version) // Parts: 2 out of 3

[Open](https://devforum.roblox.com/t/fps-using-viewmodels-the-improved-version-parts-2-out-of-3/1129877) | Roblox DevForum | 156 views | 2021-03-25

## Summary
Part 2 of a DevForum tutorial (by rokoblox5) on building an FPS ViewModel for Roblox, covering R6/R15 support. It clones the character, strips legs/face/accessories, sets up a collision group, copies animations flagged with a ViewModelAnimation attribute, welds tools to the ViewModel arm, and syncs shirt and BodyColors. The author says the tutorial is no longer supported.

## Tips
- [page](https://devforum.roblox.com/t/fps-using-viewmodels-the-improved-version-parts-2-out-of-3/1129877) **[[ui-ux-design]]** Set Character.Archivable = true before cloning, then reset to false; Character:Clone() fails on non-archivable characters.
- [page](https://devforum.roblox.com/t/fps-using-viewmodels-the-improved-version-parts-2-out-of-3/1129877) **[[physics-pathfinding-and-npc-ai]]** Put ViewModel parts in their own collision group so they don't collide with the player's world or tools.
- [page](https://devforum.roblox.com/t/fps-using-viewmodels-the-improved-version-parts-2-out-of-3/1129877) **[[core-loops-and-game-design]]** Set tool parts CanCollide off and Massless on, otherwise they can fling the player.
- [page](https://devforum.roblox.com/t/fps-using-viewmodels-the-improved-version-parts-2-out-of-3/1129877) **[[combat-and-gameplay-systems]]** Wait one frame before changing a tool's RightGrip Part0 to the ViewModel arm, since Roblox resets the weld if changed immediately.
- [page](https://devforum.roblox.com/t/fps-using-viewmodels-the-improved-version-parts-2-out-of-3/1129877) **[[optimization-and-streaming]]** Disable CastShadow on ViewModel parts and remove unneeded legs, face decals, accessories and LocalScripts from the clone.
- [page](https://devforum.roblox.com/t/fps-using-viewmodels-the-improved-version-parts-2-out-of-3/1129877) **[[scripting-and-performance]]** Drive ViewModel animations manually each RenderStepped by copying TimePosition, IsPlaying and WeightCurrent from the character track; use Animator, not Humanoid, for animations.
- [page](https://devforum.roblox.com/t/fps-using-viewmodels-the-improved-version-parts-2-out-of-3/1129877) **[[client-server-and-remotes]]** Remove old ViewModels from Camera on respawn (Camera:FindFirstChild('ViewModel'):Destroy()) since the LocalScript re-runs per character.

## Tools
Roblox Studio Collision Groups, PhysicsService, RunService, Animator.AnimationPlayed

## He points to
- EgoMoose ViewModel tutorial (recommended by author as better alternative)

## Topics
[[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[core-loops-and-game-design]] [[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
