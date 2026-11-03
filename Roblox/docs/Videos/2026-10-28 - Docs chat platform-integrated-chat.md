---
title: "Docs: chat / platform-integrated-chat"
url: https://create.roblox.com/docs/chat/platform-integrated-chat.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: chat / platform-integrated-chat

[Open](https://create.roblox.com/docs/chat/platform-integrated-chat.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs on Platform-integrated chat. Explains that once enabled in Studio, chat renders only in the default window or TextChannelWindow, message text is inaccessible to code (APIs return ""), and chat commands must migrate to TextChatCommand. Mandatory for all games from May 2027.

## Tips
- [page](https://create.roblox.com/docs/chat/platform-integrated-chat) **[[common-mistakes]]** Platform-integrated chat becomes required for all games from May 2027; unsupported chat APIs will be deprecated, so plan migration before then.
- [page](https://create.roblox.com/docs/chat/platform-integrated-chat) **[[client-server-and-remotes]]** Don't rely on Player.Chatted or TextChatService.OnIncomingMessage for admin commands once enabled; they return empty text. Use TextChatCommand instead.
- [page](https://create.roblox.com/docs/chat/platform-integrated-chat) **[[ui-ux-design]]** Custom chat UIs can no longer render messages; place a TextChannelWindow in a ScreenGui and bind its Target to a TextChannel.
- [page](https://create.roblox.com/docs/chat/platform-integrated-chat) **[[community-and-discord]]** Use read-only chat permissions for moderators to view chat during live events, since message content is no longer exposed in code.
- [page](https://create.roblox.com/docs/chat/platform-integrated-chat) **[[combat-and-gameplay-systems]]** Replace chat-based presets/chat wheels that used TextChannel:SendAsync() with Quick Words creator customization.
- [page](https://create.roblox.com/docs/chat/platform-integrated-chat) **[[ui-ux-design]]** Set ChatWindowConfiguration.TextChannelDisplayMode to DefaultTextChannels in Studio so a custom channel shows only in its own window; scripts cannot change it.
- [page](https://create.roblox.com/docs/chat/platform-integrated-chat) **[[common-mistakes]]** Prefixes aren't supported under platform-integrated chat; if your game requires chat prefixes, don't enable it yet.
- [page](https://create.roblox.com/docs/chat/platform-integrated-chat) **[[common-mistakes]]** Disable the property (PlatformIntegratedChat) again to revert; it can only be changed in Studio, not from scripts.
- [page](https://create.roblox.com/docs/chat/platform-integrated-chat) **[[common-mistakes]]** Games using default Roblox chat with no customizations need no action and should see no change.
- [page](https://create.roblox.com/docs/chat/platform-integrated-chat) **[[common-mistakes]]** Signs, boards, notes and comment systems are not affected by this update; it covers TextChatService only.

## Numbers
- [page](https://create.roblox.com/docs/chat/platform-integrated-chat) Mandatory date: **May 2027 platform-integrated chat required for all games** (Docs info banner; unsupported APIs deprecated then)
- [page](https://create.roblox.com/docs/chat/platform-integrated-chat) In-world text rate limit: **at least 1 minute** (Signs/boards/notes policy, unchanged by this update)

## Tools
Roblox Studio, TextChatService, TextChannelWindow, TextChatCommand, Quick Words

## He points to
- Custom text chat commands (Roblox docs)

## Topics
[[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[common-mistakes]] [[community-and-discord]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
