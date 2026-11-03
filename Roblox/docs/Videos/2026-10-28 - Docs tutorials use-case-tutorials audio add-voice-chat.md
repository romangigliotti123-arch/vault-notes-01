---
title: "Docs: tutorials / use-case-tutorials / audio / add-voice-chat"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-voice-chat.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / audio / add-voice-chat

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-voice-chat.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial on adding proximity voice chat: configuring voice chat objects, then three configurations—team-only chat via AudioDeviceInput access lists, push-to-talk with the V key, and time-based mute/unmute cycles every 15 seconds. Requires users aged 13+ with verified accounts.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-voice-chat) **[[first-session-onboarding]]** Voice chat requires players to be at least 13 and to have verified via phone number or government ID, depending on country; plan for unverified players.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-voice-chat) **[[client-server-and-remotes]]** Set a Script's RunContext to Client when controlling only the local player's microphone (e.g., push-to-talk), so the script runs on each client.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-voice-chat) **[[client-server-and-remotes]]** For team chat, set each AudioDeviceInput AccessType to Allow and call SetUserIdAccessList with teammates' UserIds; update the list on PlayerAdded/PlayerRemoved and team changes.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-voice-chat) **[[core-loops-and-game-design]]** Use time-based chat for round-based discussion or post-cutscene phases so players plan communication during specific windows.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-voice-chat) **[[core-loops-and-game-design]]** Use push-to-chat when players need privacy or must be heard over ambient noise; mute AudioDeviceInput by default and unmute on InputBegan.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-voice-chat) **[[development-process-and-speed]]** Disable each sample script before testing the next configuration, since they conflict when enabled together.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-voice-chat) **[[testing-debugging-and-qa]]** Playtest voice chat with a couple of friends to verify team isolation and mute behaviour, since it cannot be verified solo.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-voice-chat) Minimum voice chat age: **13 years** (Players must also verify account via phone or government ID)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-voice-chat) Time-based chat toggle interval: **15 seconds** (Sample script mutes/unmutes all AudioDeviceInputs alternately)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-voice-chat) Push-to-talk default key: **V** (Sample key held to unmute microphone)

## Games
- **Gingerbread Island - Voice Chat**: Roblox sample place file demonstrating team chat, push-to-chat, and time-based chat configurations.

## Tools
Roblox Studio, Luau, AudioDeviceInput, AudioEmitter, AudioListener, UserInputService, Teams service

## He points to
- Voice chat (Roblox docs, country verification requirements)
- Gingerbread Island - Voice Chat sample .rbxl

## Topics
[[client-server-and-remotes]] [[core-loops-and-game-design]] [[development-process-and-speed]] [[first-session-onboarding]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
