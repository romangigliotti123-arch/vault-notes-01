---
title: "Docs: chat / guidelines"
url: https://create.roblox.com/docs/chat/guidelines.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: chat / guidelines

[Open](https://create.roblox.com/docs/chat/guidelines.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official guidelines for in-game text chat. Defines what counts as chat, requires TextChatService for user conversations, mandates text filtering of incoming user text, rate limits (at least 1 minute) for editable shared text like signs, and privacy-setting checks for direct messaging.

## Tips
- [page](https://create.roblox.com/docs/chat/guidelines) **[[community-and-discord]]** Integrate Class.TextChatService for any in-game text chat between users; legacy chat system must be migrated, per Misusing Roblox Systems Community Standard.
- [page](https://create.roblox.com/docs/chat/guidelines) **[[age-ratings-moderation-and-tos]]** Run all incoming user-originated text through text filtering before displaying it to other users.
- [page](https://create.roblox.com/docs/chat/guidelines) **[[client-server-and-remotes]]** Rate-limit editable user-shared text (signs, bulletin boards) to at least once per minute; use the rate-limited text input pattern.
- [page](https://create.roblox.com/docs/chat/guidelines) **[[age-ratings-moderation-and-tos]]** Call TextChannel:SendAsync() for messages, which handles basic privacy and parental settings automatically.
- [page](https://create.roblox.com/docs/chat/guidelines) **[[age-ratings-moderation-and-tos]]** Call TextChannel:SetDirectChatRequester() on TextChannels created for direct chat so they are marked correctly.
- [page](https://create.roblox.com/docs/chat/guidelines) **[[age-ratings-moderation-and-tos]]** Check TextChatService:CanUserChatAsync(), CanUsersChatAsync() or CanUsersDirectChatAsync() before allowing messaging requests.
- [page](https://create.roblox.com/docs/chat/guidelines) **[[age-ratings-moderation-and-tos]]** Use TextChannels for chat so messages stay reportable for abuse and visible to moderators; they handle this automatically.
- [page](https://create.roblox.com/docs/chat/guidelines) **[[common-mistakes]]** Developer menu text, status messages, admin announcements and audit logs are not chat, but any user-generated text shared with others still needs text filtering.
- [page](https://create.roblox.com/docs/chat/guidelines) **[[age-ratings-moderation-and-tos]]** Repeated community-standard violations lead to warnings and temporary chat restrictions; see Text Chat Nudge FAQ.

## Numbers
- [page](https://create.roblox.com/docs/chat/guidelines) Minimum rate limit for editable shared text: **1 minute** (Applies to signs, bulletin boards and similar user-editable text)

## Tools
Class.TextChatService, Class.TextChannel, Text filtering, Migrate from legacy chat guide

## He points to
- Misusing Roblox Systems Community Standard
- Text Chat Nudge FAQ
- Rate-limited text inputs guide
- Migrate from legacy chat

## Topics
[[age-ratings-moderation-and-tos]] [[client-server-and-remotes]] [[common-mistakes]] [[community-and-discord]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
