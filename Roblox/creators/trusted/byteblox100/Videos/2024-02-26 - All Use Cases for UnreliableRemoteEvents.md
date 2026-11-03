---
title: "All Use Cases for UnreliableRemoteEvents"
url: https://youtu.be/VitH_k_-AZU
creator: ByteBlox
official: false
advice_density: medium
date: 2024-02-26
views: 4807
transcript: auto-captions
confidence: high
tags: [roblox, byteblox100, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# All Use Cases for UnreliableRemoteEvents

[Watch](https://youtu.be/VitH_k_-AZU) | byteblox100 | 4,807 views | 2024-02-26

## Summary
Explains what UnreliableRemoteEvents are (fire-and-forget, no delivery guarantee, better performance) and demos a 0.1s spam test comparing them to RemoteEvents. Concludes unreliable events suit cosmetic, non-critical events (sparkles, particles) while RemoteEvents suit critical actions like firing a gun. Notes UnreliableRemoteFunctions don't exist.

## Tips
- [6:06](https://youtu.be/VitH_k_-AZU?t=366) **[[client-server-and-remotes]]** Use UnreliableRemoteEvents only for non-critical, high-frequency events where losing an occasional message doesn't matter, e.g. cosmetic sparkles or particles.
- [7:25](https://youtu.be/VitH_k_-AZU?t=445) **[[client-server-and-remotes]]** Use regular RemoteEvents for anything that must arrive, such as firing a gun or purchases; the small performance cost is worth guaranteed delivery.
- [6:06](https://youtu.be/VitH_k_-AZU?t=366) **[[scripting-and-performance]]** Unreliable events save performance because the engine doesn't track delivery; reserve them for event spam where dropped messages are harmless.
- [2:57](https://youtu.be/VitH_k_-AZU?t=177) **[[testing-debugging-and-qa]]** Compare unreliable vs reliable remotes by firing both in a loop and counting received messages on the server; mismatched counts reveal dropped events.

## Numbers
- [2:29](https://youtu.be/VitH_k_-AZU?t=149) Test fire interval: **0.1 seconds** (Loop firing unreliable event to server in Studio test)
- [2:57](https://youtu.be/VitH_k_-AZU?t=177) Dropped events observed: **About 2 slowdowns** (Speaker noticed two moments of slowdown in unreliable event test)

## Tools
Roblox Studio, UnreliableRemoteEvent, RemoteEvent

## Topics
[[client-server-and-remotes]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[byteblox100 - How to make successful Roblox games]]
