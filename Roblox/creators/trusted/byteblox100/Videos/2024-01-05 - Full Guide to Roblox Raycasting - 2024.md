---
title: "Full Guide to Roblox Raycasting - 2024"
url: https://youtu.be/yKIZWvhabmA
creator: ByteBlox
official: false
advice_density: low
date: 2024-01-05
views: 48977
transcript: auto-captions
confidence: high
tags: [roblox, byteblox100, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Full Guide to Roblox Raycasting - 2024

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/yKIZWvhabmA) | byteblox100 | 48,977 views | 2024-01-05

## Summary
Beginner tutorial on Roblox raycasting in a LocalScript: fire a ray from the camera through the mouse position, exclude the player's character via RaycastParams, read result properties (Instance, Position, Distance), and optionally visualize hits. Mentions raycasts are cheap performance-wise. No business or growth advice.

## Tips
- [1:18](https://youtu.be/yKIZWvhabmA?t=78) **[[scripting-and-performance]]** Put click-to-raycast logic in a LocalScript (StarterPlayerScripts) rather than sending mouse data to the server via RemoteEvent; it is more efficient.
- [4:13](https://youtu.be/yKIZWvhabmA?t=253) **[[scripting-and-performance]]** Use UserInputService:GetMouseLocation() and Camera:ViewportPointToRay(x, y) to build the ray from camera through the mouse.
- [5:22](https://youtu.be/yKIZWvhabmA?t=322) **[[scripting-and-performance]]** Use RaycastParams with FilterType Exclude and FilteredDescendantsInstances set to the player's Character so the ray passes through the player.
- [9:20](https://youtu.be/yKIZWvhabmA?t=560) **[[scripting-and-performance]]** Multiply the ray direction by a length (e.g. 10 studs for melee, a large number for near-infinite) to control raycast range.

## Numbers
- [17:57](https://youtu.be/yKIZWvhabmA?t=1077) raycasts per frame: **~6,000** (Speaker's unverified recollection that games stay fine at this rate)
- [9:20](https://youtu.be/yKIZWvhabmA?t=560) example melee ray length: **10 studs** (Direction multiplied by 10 for short melee range)

## Tools
RaycastParams, workspace:Raycast, Camera:ViewportPointToRay, UserInputService

## Topics
[[scripting-and-performance]]

Back to [[byteblox100 - How to make successful Roblox games]]
