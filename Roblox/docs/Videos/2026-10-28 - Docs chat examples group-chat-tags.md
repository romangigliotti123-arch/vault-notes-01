---
title: "Docs: chat / examples / group-chat-tags"
url: https://create.roblox.com/docs/chat/examples/group-chat-tags.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: chat / examples / group-chat-tags

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/chat/examples/group-chat-tags.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Docs example showing how to tag players with a [VIP] chat prefix based on group membership. Checks IsInGroupAsync on PlayerAdded (not inside the OnIncomingMessage callback, which must not yield), stores the result as a player attribute, then a LocalScript reads that attribute in OnIncomingMessage to prepend the tag.

## Tips
- [page](https://create.roblox.com/docs/chat/examples/group-chat-tags) **[[client-server-and-remotes]]** Do not query group membership inside TextChatService.OnIncomingMessage; the callback must not yield and may hang chat. Query on PlayerAdded and store the result instead.
- [page](https://create.roblox.com/docs/chat/examples/group-chat-tags) **[[scripting-and-performance]]** Wrap player:IsInGroupAsync in pcall so a failed web request does not error out; default to false on failure.
- [page](https://create.roblox.com/docs/chat/examples/group-chat-tags) **[[core-loops-and-game-design]]** Store player status as attributes (SetAttribute) so it can be reused for area access or bonus experiences elsewhere in the game.
- [page](https://create.roblox.com/docs/chat/examples/group-chat-tags) **[[community-and-discord]]** Use group membership to visually identify VIP or role players in chat, which can reward group joins.

## Tools
TextChatService, Players:IsInGroupAsync, Instance attributes (SetAttribute/GetAttribute)

## Topics
[[client-server-and-remotes]] [[community-and-discord]] [[core-loops-and-game-design]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
