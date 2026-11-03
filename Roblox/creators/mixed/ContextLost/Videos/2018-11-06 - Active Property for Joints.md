---
title: "Active Property for Joints"
url: https://youtu.be/fNf3JtvrzRg
creator: ContextLost
official: false
advice_density: low
date: 2018-11-06
views: 1218
transcript: auto-captions
confidence: high
tags: [roblox, contextlost, youtube-learn]
creator_trust: MIXED
creator_score: 6.4
---

> [!note] Trust: MIXED (credibility audit score 6.4): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# Active Property for Joints

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/fNf3JtvrzRg) | ContextLost | 1,218 views | 2018-11-06

## Summary
Engineer from Roblox's physics team explains the new read-only `Active` property added to all joint types. It is true when a joint is enabled and its parts are in workspace. For rigid and kinematic joints (Snap, Weld, Motor6D), it shows which of several conflicting welds Roblox is actually using. Also shows the spanning-tree debug visualization for welded cycles, and how to find and remove redundant welds.

## Tips
- [0:40](https://youtu.be/fNf3JtvrzRg?t=40) **[[scripting-and-performance]]** Check the read-only Active property on joints (returned by GetJoints) to see which redundant welds Roblox actually uses; delete inactive ones that contribute nothing.
- [3:24](https://youtu.be/fNf3JtvrzRg?t=204) **[[building-and-level-design]]** If your game does not support arbitrary destruction of models, remove welds that are inactive to avoid redundant or conflicting joint configurations.
- [2:44](https://youtu.be/fNf3JtvrzRg?t=164) **[[scripting-and-performance]]** Welds forming a cycle are arbitrarily ignored by the spanning tree; if you need predictable behaviour, break cycles yourself rather than relying on the engine's choice.

## Tools
Studio debug visualization for spanning tree

## Topics
[[building-and-level-design]] [[scripting-and-performance]]

Back to [[ContextLost - How to make successful Roblox games]]
