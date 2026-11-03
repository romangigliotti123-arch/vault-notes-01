---
title: "Docs: chat / voice-chat"
url: https://create.roblox.com/docs/chat/voice-chat.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: chat / voice-chat

[Open](https://create.roblox.com/docs/chat/voice-chat.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on Voice Chat: availability (13+ age-verified users in supported countries), enabling it per place in Experience Settings, the 100-player max requirement, proximity-based default behavior, and scripting examples for team-based and non-spatial voice via VoiceChatService, AudioDeviceInput, and Wires. Also covers disabling per place and checking a player's voice status.

## Tips
- [page](https://create.roblox.com/docs/chat/voice-chat) **[[cross-platform-and-console]]** Keep max players at 100 or fewer; Voice Chat is only available for places supporting a maximum of 100 players.
- [page](https://create.roblox.com/docs/chat/voice-chat) **[[cross-platform-and-console]]** After lowering max players below 100, restart servers, since existing higher-capacity servers won't support Voice Chat.
- [page](https://create.roblox.com/docs/chat/voice-chat) **[[scripting-and-performance]]** Check a player's voice status with VoiceChatService:IsVoiceEnabledForUserIdAsync() wrapped in pcall, from a LocalScript or client-context Script.
- [page](https://create.roblox.com/docs/chat/voice-chat) **[[common-mistakes]]** Non-spatial voice scripts route all players to themselves too; add a LocalScript that destroys Wires under your own player to avoid hearing your own voice.
- [page](https://create.roblox.com/docs/chat/voice-chat) **[[genre-mechanics]]** For team-only voice, use AudioDeviceInput.AccessType and SetUserIdAccessList, updating the allowed list on Team PlayerAdded/PlayerRemoved.
- [page](https://create.roblox.com/docs/chat/voice-chat) **[[ai-and-tools]]** Enable Voice Chat in Experience Settings > Communication to use the speech-to-text API.
- [page](https://create.roblox.com/docs/chat/voice-chat) **[[community-and-discord]]** Voice Chat is opt-in per user; verified 13+ users must enable it in Settings, so design so voice is optional rather than assumed.
- [page](https://create.roblox.com/docs/chat/voice-chat) **[[social-features-and-virality]]** Roblox states games with voice often see an uplift in engagement, DAU, and spending.

## Numbers
- [page](https://create.roblox.com/docs/chat/voice-chat) Max players for Voice Chat: **100** (Maximum Visitor Count must be 100 or fewer for Voice Chat)
- [page](https://create.roblox.com/docs/chat/voice-chat) Eligible users: **13+ age-verified** (Users outside supported countries need ID verification)

## Tools
Roblox Studio, Experience Settings, VoiceChatService, AudioDeviceInput, Wire, AudioFader, AudioDeviceOutput

## He points to
- Voice Chat FAQ

## Topics
[[ai-and-tools]] [[common-mistakes]] [[community-and-discord]] [[cross-platform-and-console]] [[genre-mechanics]] [[scripting-and-performance]] [[social-features-and-virality]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
