---
title: "Collision Summaries API: Detailed Collision Data From The Engine"
url: https://devforum.roblox.com/t/collision-summaries-api-detailed-collision-data-from-the-engine/4918568
creator: Roblox DevForum
official: false
advice_density: low
date: 2026-10-06
views: 553
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Collision Summaries API: Detailed Collision Data From The Engine

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/collision-summaries-api-detailed-collision-data-from-the-engine/4918568) | Roblox DevForum | 553 views | 2026-10-06

## Summary
Roblox Physics Team introduces BasePart:BindToCollisionSummaries, an engine-generated API giving per-frame contact data (point, normal, relative velocity, area) for collisions involving a subscribed part. Explains usage, normal direction, network ownership, and limitations.

## Tips
- [page](https://devforum.roblox.com/t/collision-summaries-api-detailed-collision-data-from-the-engine/4918568) **[[scripting-and-performance]]** Don't call BindToCollisionSummaries from inside a Touched handler; it is a separate API for collision information.
- [page](https://devforum.roblox.com/t/collision-summaries-api-detailed-collision-data-from-the-engine/4918568) **[[scripting-and-performance]]** Subscribe only the parts you need; processing overhead scales with subscribed parts, not total scene collisions.
- [page](https://devforum.roblox.com/t/collision-summaries-api-detailed-collision-data-from-the-engine/4918568) **[[client-server-and-remotes]]** Summaries are generated on the network owner (client or server) and not replicated; fire your own RemoteEvent with only the needed data to inform other clients.
- [page](https://devforum.roblox.com/t/collision-summaries-api-detailed-collision-data-from-the-engine/4918568) **[[scripting-and-performance]]** Dot RelativeVelocity with Normal to get head-on impact speed; use the tangential component to detect glancing hits and sliding.

## Numbers
- [page](https://devforum.roblox.com/t/collision-summaries-api-detailed-collision-data-from-the-engine/4918568) Example impact speed threshold: **10 (studs/s, relative velocity dot normal)** (Used in sample code to trigger spawnSparks)

## Tools
BasePart:BindToCollisionSummaries, RBXScriptConnection

## Topics
[[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[scripting-and-performance]] [[vfx-and-particles]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
