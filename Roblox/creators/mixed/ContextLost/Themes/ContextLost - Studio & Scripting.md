---
title: ContextLost - Studio & Scripting
creator: ContextLost
tags: [roblox, contextlost, theme]
creator_trust: MIXED
creator_score: 6.4
---

> [!note] Trust: MIXED (credibility audit score 6.4): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# ContextLost: Studio & Scripting

All ContextLost tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[scripting-and-performance]]
- 2018-11-06 [0:40](https://youtu.be/fNf3JtvrzRg?t=40) Check the read-only Active property on joints (returned by GetJoints) to see which redundant welds Roblox actually uses; delete inactive ones that contribute nothing. ([[2018-11-06 - Active Property for Joints|Active Property for Joints]])
- 2018-11-06 [2:44](https://youtu.be/fNf3JtvrzRg?t=164) Welds forming a cycle are arbitrarily ignored by the spanning tree; if you need predictable behaviour, break cycles yourself rather than relying on the engine's choice. ([[2018-11-06 - Active Property for Joints|Active Property for Joints]])

## [[building-and-level-design]]
- 2018-11-06 [3:24](https://youtu.be/fNf3JtvrzRg?t=204) If your game does not support arbitrary destruction of models, remove welds that are inactive to avoid redundant or conflicting joint configurations. ([[2018-11-06 - Active Property for Joints|Active Property for Joints]])

Up: [[ContextLost - How to make successful Roblox games]]
