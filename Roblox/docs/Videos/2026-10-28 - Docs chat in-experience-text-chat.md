---
title: "Docs: chat / in-experience-text-chat"
url: https://create.roblox.com/docs/chat/in-experience-text-chat.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: chat / in-experience-text-chat

[Open](https://create.roblox.com/docs/chat/in-experience-text-chat.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on TextChatService, the modern text chat system. Covers channels, text sources, messages, commands, the client-server send/deliver flow, non-yielding callbacks for delivery and display customization, and a migration guide from legacy chat including attribute-based name colors and tags.

## Tips
- [page](https://create.roblox.com/docs/chat/in-experience-text-chat) **[[community-and-discord]]** Enable TextChatService.ChatVersion to TextChatService when migrating from legacy chat; SendAsync supports rich text, message priority and built-in filtering.
- [page](https://create.roblox.com/docs/chat/in-experience-text-chat) **[[common-mistakes]]** Do not yield inside TextChatService callbacks (ShouldDeliverCallback, OnIncomingMessage, OnBubbleAdded, OnChatWindowAdded); yielding blocks the chat system.
- [page](https://create.roblox.com/docs/chat/in-experience-text-chat) **[[common-mistakes]]** Avoid multiple TextChannels with the same name; it can cause unintended behavior with the default chat window.
- [page](https://create.roblox.com/docs/chat/in-experience-text-chat) **[[client-server-and-remotes]]** Define ShouldDeliverCallback on the server only; use it for proximity chat or blocking players with certain attributes from messaging others.
- [page](https://create.roblox.com/docs/chat/in-experience-text-chat) **[[ui-ux-design]]** Define OnIncomingMessage, OnBubbleAdded and OnChatWindowAdded on the client only; use them to style chat independently of each other.
- [page](https://create.roblox.com/docs/chat/in-experience-text-chat) **[[monetisation-other]]** Use player attributes (NameColor, ChatColor, custom tag flags) set on Players and read in OnChatWindowAdded to emulate legacy SetExtraData name colors and tags.
- [page](https://create.roblox.com/docs/chat/in-experience-text-chat) **[[common-mistakes]]** When platform-integrated chat is enabled, custom chat must use Roblox native systems; message content is not accessible in code.
- [page](https://create.roblox.com/docs/chat/in-experience-text-chat) **[[core-loops-and-game-design]]** Build custom commands with TextChatCommand parented to TextChatService; set CreateDefaultCommands/CreateDefaultTextChannels to true for defaults.
- [page](https://create.roblox.com/docs/chat/in-experience-text-chat) **[[ui-ux-design]]** Disable ChatWindowConfiguration, ChatInputBarConfiguration, ChannelTabsConfiguration or BubbleChatConfiguration to hide their UI, or replace them with custom interfaces.

## Tools
TextChatService, TextChannel, TextSource, TextChatMessage, TextChatCommand, ChatWindowConfiguration, BubbleChatConfiguration

## Topics
[[client-server-and-remotes]] [[common-mistakes]] [[community-and-discord]] [[core-loops-and-game-design]] [[monetisation-other]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
