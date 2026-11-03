---
title: "Replication, Client-Server Model - Roblox Scripting Tutorial"
url: https://youtu.be/Ng1uYpFcpOA
creator: Suphi Kaner
official: false
advice_density: medium
date: 2023-02-17
views: 22428
transcript: auto-captions
confidence: high
tags: [roblox, 5uphi, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.8
---

> [!note] Trust: TRUSTED (credibility audit score 8.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Replication, Client-Server Model - Roblox Scripting Tutorial

[Watch](https://youtu.be/Ng1uYpFcpOA) | 5uphi | 22,428 views | 2023-02-17

## Summary
Explains client-server replication in Roblox Studio using a text-file analogy, then tests in a local server with two instances which properties, attributes, scripts, humanoid states, parts, tools and network ownership replicate server-to-client versus client-to-server.

## Tips
- [2:04](https://youtu.be/Ng1uYpFcpOA?t=124) **[[client-server-and-remotes]]** Test replication yourself: run Test > local server with 1 player, open two instances, and change things on each side to see what syncs.
- [6:49](https://youtu.be/Ng1uYpFcpOA?t=409) **[[client-server-and-remotes]]** Only the server's changes replicate reliably; client changes to most instances are not sent back, so never trust client-side state.
- [8:14](https://youtu.be/Ng1uYpFcpOA?t=494) **[[anti-exploit-and-security]]** Network ownership lets the nearest client drive unanchored parts' physics and send positions to server; a malicious client can place them anywhere, so validate on server.
- [10:20](https://youtu.be/Ng1uYpFcpOA?t=620) **[[data-persistence]]** Attributes replicate server to client only; client-created or client-edited attributes and deletions do not reach the server.
- [11:03](https://youtu.be/Ng1uYpFcpOA?t=663) **[[scripting-and-performance]]** Scripts, local scripts and modules created or edited on the client do not replicate to the server; keep authoritative logic on the server.
- [13:06](https://youtu.be/Ng1uYpFcpOA?t=786) **[[anti-exploit-and-security]]** Humanoid health changed on the client does not replicate; health is server-authoritative, so do damage and checks on the server.
- [13:47](https://youtu.be/Ng1uYpFcpOA?t=827) **[[anti-exploit-and-security]]** Client can set Humanoid state (e.g. Dead) and it replicates to the server; validate such state changes server-side.
- [14:27](https://youtu.be/Ng1uYpFcpOA?t=867) **[[client-server-and-remotes]]** Calling SetNetworkOwner(nil) on a part's root gives server ownership; the client then can no longer move it or set its humanoid state.
- [17:15](https://youtu.be/Ng1uYpFcpOA?t=1035) **[[client-server-and-remotes]]** Tools created on the client do not replicate; tools parented to the backpack by the server let the client reparent them, so validate tool parenting on the server.

## Numbers
- [2:45](https://youtu.be/Ng1uYpFcpOA?t=165) Outgoing network traffic (idle, server to client): **~0.16 KB/s** (Overall outgoing KB/s with one static part in workspace via Stats > Network)
- [6:49](https://youtu.be/Ng1uYpFcpOA?t=409) Outgoing network traffic while moving a part quickly: **~1.5 KB/s** (Server moving an anchored=false part left and right)
- [8:56](https://youtu.be/Ng1uYpFcpOA?t=536) Outgoing network traffic when client owns and moves part: **0.18 to 0.8 KB/s** (Bob's overall outgoing KB/s while moving network-owned part)

## Tools
Roblox Studio, Stats > Network (View tab), Command Bar, Avatar tab rig builder

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[data-persistence]] [[scripting-and-performance]]

Back to [[5uphi - How to make successful Roblox games]]
