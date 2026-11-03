---
title: "Docs: chat / examples / proximity-chat"
url: https://create.roblox.com/docs/chat/examples/proximity-chat.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: chat / examples / proximity-chat

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/chat/examples/proximity-chat.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs example for proximity-based chat: uses TextChatService's RBXGeneral channel and ShouldDeliverCallback to deliver messages only between players within 50 studs of each other, computed from character pivot positions.

## Tips
- [page](https://create.roblox.com/docs/chat/examples/proximity-chat) **[[client-server-and-remotes]]** Run the ShouldDeliverCallback logic in a server Script; it controls message delivery per recipient, so clients cannot bypass the distance check.
- [page](https://create.roblox.com/docs/chat/examples/proximity-chat) **[[combat-and-gameplay-systems]]** For proximity features, get positions via player.Character:GetPivot().Position and fall back to Vector3.zero if the character is missing.
- [page](https://create.roblox.com/docs/chat/examples/proximity-chat) **[[scripting-and-performance]]** Use a dedicated channel instead of RBXGeneral in production so proximity rules don't affect the global chat.

## Numbers
- [page](https://create.roblox.com/docs/chat/examples/proximity-chat) Proximity chat delivery range: **50 studs (Magnitude < 50)** (Example threshold in the ShouldDeliverCallback proximity chat sample)

## Tools
TextChatService, TextChannel.ShouldDeliverCallback, Players:GetPlayerByUserId, Model:GetPivot

## Topics
[[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
