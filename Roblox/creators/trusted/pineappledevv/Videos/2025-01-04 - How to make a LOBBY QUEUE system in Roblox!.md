---
title: "How to make a LOBBY QUEUE system in Roblox!"
url: https://youtu.be/E2nFsr22A1M
creator: PineappleDev
official: false
advice_density: medium
date: 2025-01-04
views: 263526
transcript: auto-captions
confidence: high
tags: [roblox, pineappledevv, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to make a LOBBY QUEUE system in Roblox!

[Watch](https://youtu.be/E2nFsr22A1M) | pineappledevv | 263,526 views | 2025-01-04

## Summary
Shows how to install and configure a lobby queue system in Roblox. Covers placing the Q folders and scripts, creating a destination place via Asset Manager, wiring its place ID into the Q Server module, and adding queue rooms by duplicating folders named by player count. The game must be public and published to work.

## Tips
- [0:15](https://youtu.be/E2nFsr22A1M?t=15) **[[code-architecture-and-frameworks]]** Place the Q folder with RemoteEvents in ReplicatedStorage, Q Server in ServerScriptService, Q Client in StarterPlayerScripts, Qi UI in StarterGui, and the Q's folder in Workspace.
- [1:36](https://youtu.be/E2nFsr22A1M?t=96) **[[matchmaking-and-teleport]]** Create a separate destination place in Asset Manager, set its permissions to public, publish it, and paste its place ID into the Q Server teleport ID field.
- [2:28](https://youtu.be/E2nFsr22A1M?t=148) **[[matchmaking-and-teleport]]** Duplicate the queue room folder for more rooms and rename it to the desired player count; the UI and countdown update automatically.
- [3:09](https://youtu.be/E2nFsr22A1M?t=189) **[[matchmaking-and-teleport]]** Do not edit the Q folder, which tracks current queue members. Custom room visuals can go inside the room model.
- [3:49](https://youtu.be/E2nFsr22A1M?t=229) **[[ui-ux-design]]** Restyle the queue UI freely, but keep the Players and Time text object names unchanged or the system will break.
- [4:29](https://youtu.be/E2nFsr22A1M?t=269) **[[testing-debugging-and-qa]]** The game must be public and published before testing; private games fail, and Studio testing also requires publishing first.

## Numbers
- [1:36](https://youtu.be/E2nFsr22A1M?t=96) Queue countdown: **Starts at 10s; 3-player queue ~20s, 4-player queue ~30s** (Countdown length scales with queue size in the demo)

## Tools
Roblox Studio, Asset Manager

## Topics
[[code-architecture-and-frameworks]] [[matchmaking-and-teleport]] [[testing-debugging-and-qa]] [[ui-ux-design]]

Back to [[pineappledevv - How to make successful Roblox games]]
