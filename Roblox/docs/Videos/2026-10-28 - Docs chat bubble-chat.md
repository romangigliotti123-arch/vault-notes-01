---
title: "Docs: chat / bubble-chat"
url: https://create.roblox.com/docs/chat/bubble-chat.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: chat / bubble-chat

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/chat/bubble-chat.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox documentation on bubble chat in TextChatService: enabling it, basic and advanced appearance customization (ImageLabel, UIGradient, UICorner, UIPadding), per-bubble overrides via OnBubbleAdded and BubbleChatMessageProperties, and NPC bubbles via TextChatService:DisplayBubble on the client.

## Tips
- [page](https://create.roblox.com/docs/chat/bubble-chat) **[[ui-ux-design]]** Use BubbleChatConfiguration Properties window for basic changes (text color, spacing); use a LocalScript in StarterPlayerScripts for runtime overrides that take precedence over Studio settings.
- [page](https://create.roblox.com/docs/chat/bubble-chat) **[[player-psychology-and-game-feel]]** Use per-bubble customization (OnBubbleAdded) for special effects tied to events, e.g. VIP styling or highlighting low health, to make chat more contextually meaningful.
- [page](https://create.roblox.com/docs/chat/bubble-chat) **[[client-server-and-remotes]]** TextChatService:DisplayBubble only works in client-side scripts (LocalScript or Script with RunContext set to Client); call it from client code for NPC bubbles.
- [page](https://create.roblox.com/docs/chat/bubble-chat) **[[ui-ux-design]]** Set ScaleType to Slice and configure SliceCenter/SliceScale when using 9-sliced bubble background images so corners stay undistorted.

## Numbers
- [page](https://create.roblox.com/docs/chat/bubble-chat) BubbleDuration default: **30 seconds** (Time before a bubble fades out)
- [page](https://create.roblox.com/docs/chat/bubble-chat) MaxBubbles default: **3** (Maximum bubbles displayed before older ones disappear)
- [page](https://create.roblox.com/docs/chat/bubble-chat) MaxDistance default: **100 studs** (Maximum camera distance at which bubbles are shown)
- [page](https://create.roblox.com/docs/chat/bubble-chat) MinimizeDistance default: **40 studs** (Distance where bubbles collapse into a single ellipsis bubble)

## Tools
TextChatService, BubbleChatConfiguration, BubbleChatMessageProperties, TextChatService.OnBubbleAdded

## Topics
[[client-server-and-remotes]] [[player-psychology-and-game-feel]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
