---
title: "Docs: chat / cross-server-chat"
url: https://create.roblox.com/docs/chat/cross-server-chat.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: chat / cross-server-chat

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/chat/cross-server-chat.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on Cross-server chat: a TextChatService extension letting players in the same universe chat across servers via a Global tab. Covers the grouping by age/language/occupancy, the ~200-user channel size, throttling, the dashboard toggle (on by default), private-server restriction, and the global chat commands.

## Tips
- [page](https://create.roblox.com/docs/chat/cross-server-chat) **[[social-features-and-virality]]** Keep cross-server chat enabled (default) in low-occupancy games; it lets players talk across servers and boosts social engagement.
- [page](https://create.roblox.com/docs/chat/cross-server-chat) **[[social-features-and-virality]]** Disable cross-server chat in Creator Dashboard > Audience > Communication Settings if your design needs isolated server chat.
- [page](https://create.roblox.com/docs/chat/cross-server-chat) **[[common-mistakes]]** Don't expect the Global tab in private servers; it is disabled there regardless of the setting, so design private-server social features around the Here tab.
- [page](https://create.roblox.com/docs/chat/cross-server-chat) **[[client-server-and-remotes]]** Global channels are capped at about 200 users; rapid senders get throttled and messages drop, so don't rely on global chat as a high-volume broadcast channel.

## Numbers
- [page](https://create.roblox.com/docs/chat/cross-server-chat) Users per global chat channel: **about 200** (Each global chat channel connects about 200 users for readability and performance)

## Tools
TextChatService

## Topics
[[client-server-and-remotes]] [[common-mistakes]] [[social-features-and-virality]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
