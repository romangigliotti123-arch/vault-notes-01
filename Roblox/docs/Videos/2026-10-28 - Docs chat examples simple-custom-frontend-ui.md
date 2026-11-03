---
title: "Docs: chat / examples / simple-custom-frontend-ui"
url: https://create.roblox.com/docs/chat/examples/simple-custom-frontend-ui.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: chat / examples / simple-custom-frontend-ui

[Open](https://create.roblox.com/docs/chat/examples/simple-custom-frontend-ui.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs page showing how to build a custom text chat frontend with TextChatService: disable default chat windows, build a TextBox that sends via RBXGeneral:SendAsync, and a ScrollingFrame that renders messages from MessageReceived with de-duplication by MessageId.

## Tips
- [page](https://create.roblox.com/docs/chat/examples/simple-custom-frontend-ui) **[[ui-ux-design]]** Warning: with platform-integrated chat enabled, custom UIs can no longer render message text themselves. Use TextChannelWindow instead of reading TextChatMessage.Text or MessageReceived for display.
- [page](https://create.roblox.com/docs/chat/examples/simple-custom-frontend-ui) **[[client-server-and-remotes]]** Send chat with TextChannel:SendAsync inside pcall and show a DisplaySystemMessage on failure rather than losing the message silently.
- [page](https://create.roblox.com/docs/chat/examples/simple-custom-frontend-ui) **[[ui-ux-design]]** Clear the input TextBox after sending, since players expect the input to reset after pressing Enter.
- [page](https://create.roblox.com/docs/chat/examples/simple-custom-frontend-ui) **[[common-mistakes]]** MessageReceived fires twice per message: once when sending and once when the server confirms. Check for an existing label by MessageId before adding a new one.
- [page](https://create.roblox.com/docs/chat/examples/simple-custom-frontend-ui) **[[ui-ux-design]]** Use a UIListLayout inside a ScrollingFrame with AutomaticSize XY on labels so chat messages stack and resize automatically.
- [page](https://create.roblox.com/docs/chat/examples/simple-custom-frontend-ui) **[[ui-ux-design]]** Set ChatWindowConfiguration.Enabled and ChatInputBarConfiguration.Enabled to false to disable the default chat UI before building a custom one.
- [page](https://create.roblox.com/docs/chat/examples/simple-custom-frontend-ui) **[[ui-ux-design]]** Shade outgoing messages differently (BackgroundTransparency 0.5 while Status is Sending) so players can tell their pending messages apart.

## Numbers
- [page](https://create.roblox.com/docs/chat/examples/simple-custom-frontend-ui) Label BackgroundTransparency for outgoing messages: **0.5** (Sample code sets outgoing (Sending status) labels to 0.5, incoming to 0)
- [page](https://create.roblox.com/docs/chat/examples/simple-custom-frontend-ui) Label TextSize: **18** (Sample code default text size for chat labels)

## Tools
TextChatService, ScreenGui, TextBox, ScrollingFrame, UIListLayout, LocalScript

## He points to
- Class.TextChatService.CreateDefaultTextChannels
- Class.TextChannelWindow

## Topics
[[client-server-and-remotes]] [[common-mistakes]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
