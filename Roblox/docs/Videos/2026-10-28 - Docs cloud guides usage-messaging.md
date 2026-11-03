---
title: "Docs: cloud / guides / usage-messaging"
url: https://create.roblox.com/docs/cloud/guides/usage-messaging.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / guides / usage-messaging

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/cloud/guides/usage-messaging.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Open Cloud docs for the Messaging Service API. Covers use cases (announcement portals, moderation, LiveOps), rate and size limits, topic setup via Studio and SubscribeAsync, publishing via API key or OAuth 2.0 with the publishMessage endpoint, and HttpService access.

## Tips
- [page](https://create.roblox.com/docs/cloud/guides/usage-messaging) **[[scripting-and-performance]]** Disconnect MessagingService subscriptions when the player leaves (e.g. on AncestryChanged) to avoid leaking subscriptions.
- [page](https://create.roblox.com/docs/cloud/guides/usage-messaging) **[[scripting-and-performance]]** Keep messages under 1,024 characters and topic names under 80 characters; larger payloads will be rejected.
- [page](https://create.roblox.com/docs/cloud/guides/usage-messaging) **[[anti-exploit-and-security]]** Create API keys with only messaging-service and universe-messaging-service:publish permissions to limit blast radius.
- [page](https://create.roblox.com/docs/cloud/guides/usage-messaging) **[[updates-live-ops]]** Use a LiveOps dashboard to trigger events and reward users without shipping a code update.

## Numbers
- [page](https://create.roblox.com/docs/cloud/guides/usage-messaging) Messages sent per game server: **600 + 240 × players in server, per minute**
- [page](https://create.roblox.com/docs/cloud/guides/usage-messaging) Messages received per topic: **40 + 80 × servers, per minute**
- [page](https://create.roblox.com/docs/cloud/guides/usage-messaging) Messages received for entire game: **400 + 200 × servers, per minute**
- [page](https://create.roblox.com/docs/cloud/guides/usage-messaging) Subscriptions allowed per game server: **20 + 8 × players in server**

## Tools
Open Cloud Messaging Service API, Creator Dashboard API keys, Roblox Studio, HttpService

## Topics
[[age-ratings-moderation-and-tos]] [[ai-and-tools]] [[anti-exploit-and-security]] [[scripting-and-performance]] [[updates-live-ops]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
