---
title: "Docs: chat / examples / rate-limit-public-text-inputs"
url: https://create.roblox.com/docs/chat/examples/rate-limit-public-text-inputs.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: chat / examples / rate-limit-public-text-inputs

[Open](https://create.roblox.com/docs/chat/examples/rate-limit-public-text-inputs.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Docs example: rate-limiting a public text input (one post per 60 seconds per player) using a server-side RemoteEvent, tick()-based cooldown table, text filtering before broadcast, and cleanup on PlayerRemoving.

## Tips
- [page](https://create.roblox.com/docs/chat/examples/rate-limit-public-text-inputs) **[[anti-exploit-and-security]]** Enforce cooldowns on the server, storing last-action timestamps per UserId; never trust client-side timers for rate limits.
- [page](https://create.roblox.com/docs/chat/examples/rate-limit-public-text-inputs) **[[client-server-and-remotes]]** Send a cooldown response back to the client with remaining seconds (math.ceil) so the UI can show accurate wait time.
- [page](https://create.roblox.com/docs/chat/examples/rate-limit-public-text-inputs) **[[common-mistakes]]** All text shown to other players must pass through the text filter (GetNonChatStringForBroadcastAsync) before broadcasting; wrap the call in pcall.
- [page](https://create.roblox.com/docs/chat/examples/rate-limit-public-text-inputs) **[[data-persistence]]** Clear per-player entries from lookup tables on Players.PlayerRemoving to avoid memory leaks.
- [page](https://create.roblox.com/docs/chat/examples/rate-limit-public-text-inputs) **[[community-and-discord]]** Community bulletin boards with rate-limited player notes give players a social outlet; limit posting frequency to reduce spam.

## Numbers
- [page](https://create.roblox.com/docs/chat/examples/rate-limit-public-text-inputs) Post cooldown: **60 seconds per player** (Rate limit example for public note posting)

## Tools
Roblox Studio, RemoteEvent, TextService (filter via GetNonChatStringForBroadcastAsync), tick()

## Quotes
- [page](https://create.roblox.com/docs/chat/examples/rate-limit-public-text-inputs) "All text shared publicly must go through a text filter"

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[common-mistakes]] [[community-and-discord]] [[data-persistence]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
