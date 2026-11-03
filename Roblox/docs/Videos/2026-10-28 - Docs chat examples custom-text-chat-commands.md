---
title: "Docs: chat / examples / custom-text-chat-commands"
url: https://create.roblox.com/docs/chat/examples/custom-text-chat-commands.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: chat / examples / custom-text-chat-commands

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/chat/examples/custom-text-chat-commands.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on custom text chat commands. Explains enabling built-in TextChatService default commands (CreateDefaultCommands), creating TextChatCommand instances with PrimaryAlias/SecondaryAlias, and handling the Triggered event in a server Script. Example scales character size via /super and /mini.

## Tips
- [page](https://create.roblox.com/docs/chat/examples/custom-text-chat-commands) **[[scripting-and-performance]]** Use TextChatCommand instances with Triggered:Connect for chat commands instead of parsing chat messages manually.
- [page](https://create.roblox.com/docs/chat/examples/custom-text-chat-commands) **[[client-server-and-remotes]]** Run chat command callbacks on the server in ServerScriptService and look up the player via textSource.UserId to keep authority server-side.
- [page](https://create.roblox.com/docs/chat/examples/custom-text-chat-commands) **[[anti-exploit-and-security]]** Validate command input on the server; the example only checks the first word, so ignore unexpected message content.

## Numbers
- [page](https://create.roblox.com/docs/chat/examples/custom-text-chat-commands) Size multipliers in example: **/super = 2, /mini = 0.5**

## Tools
TextChatService, TextChatCommand, Studio Properties window

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
