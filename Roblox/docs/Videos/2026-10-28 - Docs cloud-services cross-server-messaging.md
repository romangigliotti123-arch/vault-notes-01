---
title: "Docs: cloud-services / cross-server-messaging"
url: https://create.roblox.com/docs/cloud-services/cross-server-messaging.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud-services / cross-server-messaging

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/cloud-services/cross-server-messaging.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on cross-server messaging via MessagingService. Covers use cases (global announcements, real-time server browser listing up to 20 servers updated every minute), topic-based setup, subscribing with SubscribeAsync and unsubscribing on player leave, and publishing with PublishAsync.

## Tips
- [page](https://create.roblox.com/docs/cloud-services/cross-server-messaging) **[[data-persistence]]** Wrap SubscribeAsync and PublishAsync in pcall; both can fail, and failures should be handled rather than assumed successful.
- [page](https://create.roblox.com/docs/cloud-services/cross-server-messaging) **[[client-server-and-remotes]]** Subscribe and publish from server scripts; MessagingService is server-side cross-server communication, not a client channel.
- [page](https://create.roblox.com/docs/cloud-services/cross-server-messaging) **[[scripting-and-performance]]** Store the SubscribeAsync connection and call Disconnect when the player leaves to avoid leaking subscriptions.
- [page](https://create.roblox.com/docs/cloud-services/cross-server-messaging) **[[matchmaking-and-teleport]]** Use MessagingService for cross-server features like friend-server notifications or a real-time server browser instead of polling DataStores.

## Numbers
- [page](https://create.roblox.com/docs/cloud-services/cross-server-messaging) Server browser refresh interval: **every 1 minute** (Real-time server browser example updates server list every minute)
- [page](https://create.roblox.com/docs/cloud-services/cross-server-messaging) Server browser max servers displayed: **20** (Real-time server browser example displays a maximum of 20 servers)

## Games
- **Teleportation Playground**: Official sample game demonstrating cross-server messaging behaviour before implementing it yourself.

## Tools
MessagingService, Teleportation Playground sample game

## Topics
[[client-server-and-remotes]] [[data-persistence]] [[matchmaking-and-teleport]] [[scripting-and-performance]] [[social-features-and-virality]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
