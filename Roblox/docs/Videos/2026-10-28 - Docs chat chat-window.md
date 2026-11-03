---
title: "Docs: chat / chat-window"
url: https://create.roblox.com/docs/chat/chat-window.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: chat / chat-window

[Open](https://create.roblox.com/docs/chat/chat-window.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs on customizing the in-game text chat window: toggling chat window, input bar and channel tabs, styling via ChatWindowConfiguration, ChatInputBarConfiguration and ChannelTabsConfiguration, customizing message prefixes/colors with OnChatWindowAdded, and handling system messages from non-player sources.

## Tips
- [page](https://create.roblox.com/docs/chat/chat-window) **[[ui-ux-design]]** Channel tabs are disabled by default; enable ChannelTabsConfiguration explicitly if you want per-channel tabs (RBXGeneral and RBXSystem merge into one General tab).
- [page](https://create.roblox.com/docs/chat/chat-window) **[[ui-ux-design]]** Customize chat via ChatWindowMessageProperties and OnChatWindowAdded callbacks rather than overriding the existing UI, so default chat keeps working.
- [page](https://create.roblox.com/docs/chat/chat-window) **[[ui-ux-design]]** Reference system messages by TextChatMessage.Metadata rather than text, since default system messages are localized.
- [page](https://create.roblox.com/docs/chat/chat-window) **[[localization-and-international]]** Do not match system messages by their localized string; use Metadata to identify them across languages.
- [page](https://create.roblox.com/docs/chat/chat-window) **[[ui-ux-design]]** Use DeriveNewMessageProperties() from the chat window configuration as the base for per-message styling to keep defaults consistent.

## Numbers
- [page](https://create.roblox.com/docs/chat/chat-window) Chat window default BackgroundTransparency: **0.3** (ChatWindowConfiguration default background transparency)
- [page](https://create.roblox.com/docs/chat/chat-window) Chat text default TextSize: **14** (ChatWindowConfiguration and ChatInputBarConfiguration default)
- [page](https://create.roblox.com/docs/chat/chat-window) Channel tabs default TextSize: **18** (ChannelTabsConfiguration default text size)
- [page](https://create.roblox.com/docs/chat/chat-window) Input bar default KeyboardKeyCode: **Slash** (Additional key that focuses the default chat input bar)
- [page](https://create.roblox.com/docs/chat/chat-window) Chat window default HeightScale and WidthScale: **1 and 1** (Relative to screen size)

## Tools
TextChatService, ChatWindowConfiguration, ChatInputBarConfiguration, ChannelTabsConfiguration, ChatWindowMessageProperties, UIGradient

## He points to
- Bubble Chat documentation

## Topics
[[localization-and-international]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
