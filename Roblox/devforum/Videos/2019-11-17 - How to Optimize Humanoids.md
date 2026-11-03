---
title: "How to Optimize Humanoids"
url: https://devforum.roblox.com/t/how-to-optimize-humanoids/389801
creator: Roblox DevForum
official: false
advice_density: high
date: 2019-11-17
views: 344
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How to Optimize Humanoids

[Open](https://devforum.roblox.com/t/how-to-optimize-humanoids/389801) | Roblox DevForum | 344 views | 2019-11-17

## Summary
DevForum post arguing humanoids are not inherently laggy; most performance problems come from user code. Covers disabling unneeded humanoid states, client-side visuals with TweenService, minimizing clothing texture memory, keeping NPC AI simple, and avoiding custom humanoids unless truly needed.

## Tips
- [page](https://devforum.roblox.com/t/how-to-optimize-humanoids/389801) **[[scripting-and-performance]]** Before blaming Humanoid, analyze your own NPC code and ask Scripting Support to review it; the author says it usually can be improved for significant gains.
- [page](https://devforum.roblox.com/t/how-to-optimize-humanoids/389801) **[[optimization-and-streaming]]** Disable humanoid states you don't need (e.g. climbing, swimming) and enable them on the fly only when required.
- [page](https://devforum.roblox.com/t/how-to-optimize-humanoids/389801) **[[client-server-and-remotes]]** Keep NPC logic on the server but handle visuals such as animation and movement display on the client to reduce server overhead.
- [page](https://devforum.roblox.com/t/how-to-optimize-humanoids/389801) **[[physics-pathfinding-and-npc-ai]]** Consider TweenService instead of Humanoid:MoveTo() for NPC movement visuals, moving the cost to the client; the author notes this is tricky to implement.
- [page](https://devforum.roblox.com/t/how-to-optimize-humanoids/389801) **[[building-art-and-assets]]** Minimize clothing memory: Roblox builds one clothing texture per humanoid, so keep texture file sizes small, limit item count, and reuse items.
- [page](https://devforum.roblox.com/t/how-to-optimize-humanoids/389801) **[[physics-pathfinding-and-npc-ai]]** Keep NPC AI as simple ('dumb') as possible; more advanced AI costs more resources, especially with many NPCs.
- [page](https://devforum.roblox.com/t/how-to-optimize-humanoids/389801) **[[common-mistakes]]** Don't build a custom Humanoid just for performance; the default is refined and useful, so only replace it if you won't need most of its features.

## Numbers
- [page](https://devforum.roblox.com/t/how-to-optimize-humanoids/389801) Example load: **50 zombies chasing 30 players** (Author's example of an NPC chase scenario that becomes resource-intensive)

## Tools
TweenService, TweenService V2 (by SteadyOn)

## He points to
- @CompilerError DevForum post on coding many NPCs
- @SteadyOn TweenService V2 module

## Quotes
- [page](https://devforum.roblox.com/t/how-to-optimize-humanoids/389801) "Make your NPCs as dumb as possible; the more advanced it is, the more resources you'll need."
- [page](https://devforum.roblox.com/t/how-to-optimize-humanoids/389801) "Before you blame humanoids for your game's lackluster performance, analyze your code."

## Topics
[[building-art-and-assets]] [[client-server-and-remotes]] [[common-mistakes]] [[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
