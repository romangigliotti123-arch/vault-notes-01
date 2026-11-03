---
title: "Voice Chat is now supported in servers of up to 100 users!"
url: https://devforum.roblox.com/t/voice-chat-is-now-supported-in-servers-of-up-to-100-users/4534031
creator: Roblox DevForum
official: false
advice_density: medium
date: 2026-03-24
views: 304
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Voice Chat is now supported in servers of up to 100 users!

[Open](https://devforum.roblox.com/t/voice-chat-is-now-supported-in-servers-of-up-to-100-users/4534031) | Roblox DevForum | 304 views | 2026-03-24

## Summary
Roblox DevForum announcement: Voice Chat server size raised from 50 to 100 users, now enabled by default for age-checked 13+ users in new experiences. Covers custom matchmaking with the Age signal, design and performance considerations for 50+ user servers, and MicroProfiler/Creator Hub checks for voice issues.

## Tips
- [page](https://devforum.roblox.com/t/voice-chat-is-now-supported-in-servers-of-up-to-100-users/4534031) **[[social-features-and-virality]]** Voice Chat now works in servers up to 100 users (up to 50 previously). Voice is on by default for age-checked 13+ users in new experiences, with a 100-player max.
- [page](https://devforum.roblox.com/t/voice-chat-is-now-supported-in-servers-of-up-to-100-users/4534031) **[[matchmaking-and-teleport]]** If your experience relies heavily on voice, use the custom matchmaking Age signal. Only users in the same age group can chat, so this raises the odds of voice-compatible server mates.
- [page](https://devforum.roblox.com/t/voice-chat-is-now-supported-in-servers-of-up-to-100-users/4534031) **[[building-and-level-design]]** Before scaling past 50 users, check that the map is large enough for players to interact without crowding.
- [page](https://devforum.roblox.com/t/voice-chat-is-now-supported-in-servers-of-up-to-100-users/4534031) **[[optimization-and-streaming]]** Before scaling past 50 users, estimate the added cost of extra avatars, player-placed tools and structures. Confirm the experience has headroom for 50 more avatars.
- [page](https://devforum.roblox.com/t/voice-chat-is-now-supported-in-servers-of-up-to-100-users/4534031) **[[analytics-metrics]]** Monitor performance with the MicroProfiler, Creator Hub performance analytics, and a community bug-report channel after raising server size.
- [page](https://devforum.roblox.com/t/voice-chat-is-now-supported-in-servers-of-up-to-100-users/4534031) **[[testing-debugging-and-qa]]** For voice issues, inspect the Sound FMOD::Output::Mix and Voice CustomAudioMixer::Mix MicroProfiler tabs, and the Sound and Voice memory counters.
- [page](https://devforum.roblox.com/t/voice-chat-is-now-supported-in-servers-of-up-to-100-users/4534031) **[[community-and-discord]]** Keep an open channel with your community for bug reports when server size or voice usage changes.

## Numbers
- [page](https://devforum.roblox.com/t/voice-chat-is-now-supported-in-servers-of-up-to-100-users/4534031) Voice Chat max server size: **100 users (up from 50); next target 200**
- [page](https://devforum.roblox.com/t/voice-chat-is-now-supported-in-servers-of-up-to-100-users/4534031) Voice Chat default eligibility: **Age-checked 13+ users, enabled by default on new experiences**

## Tools
MicroProfiler, Creator Hub performance analytics, Roblox Studio (Enable Voice Chat setting)

## He points to
- Voice Chat documentation (linked from post)
- Custom matchmaking Age signal

## Topics
[[analytics-metrics]] [[building-and-level-design]] [[community-and-discord]] [[matchmaking-and-teleport]] [[optimization-and-streaming]] [[social-features-and-virality]] [[testing-debugging-and-qa]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
