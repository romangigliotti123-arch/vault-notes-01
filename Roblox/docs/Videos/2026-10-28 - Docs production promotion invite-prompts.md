---
title: "Docs: production / promotion / invite-prompts"
url: https://create.roblox.com/docs/production/promotion/invite-prompts.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / promotion / invite-prompts

[Open](https://create.roblox.com/docs/production/promotion/invite-prompts.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on player invite prompts: how to set ExperienceInviteOptions (prompt message, target specific friend, notification string asset, launch data up to 200 chars), check eligibility with CanSendGameInviteAsync inside pcall, prompt via SocialService:PromptGameInvite, and read launch data server-side with GetJoinData.

## Tips
- [page](https://create.roblox.com/docs/production/promotion/invite-prompts) **[[social-features-and-virality]]** Check CanSendGameInviteAsync inside pcall before PromptGameInvite, since the call is async network and may fail or be unavailable on some platforms.
- [page](https://create.roblox.com/docs/production/promotion/invite-prompts) **[[social-features-and-virality]]** Use launch data to route invited friends to the sender's location or a spot in the game, improving co-experience gameplay.
- [page](https://create.roblox.com/docs/production/promotion/invite-prompts) **[[social-features-and-virality]]** Encode multiple launch data values with HttpService:JSONEncode and keep the total under 200 characters.
- [page](https://create.roblox.com/docs/production/promotion/invite-prompts) **[[social-features-and-virality]]** On the receiving side, poll Player:GetJoinData() for several seconds because launch data can take a few seconds to arrive after joining.
- [page](https://create.roblox.com/docs/production/promotion/invite-prompts) **[[titles-descriptions]]** Create custom notification strings with {experienceName} placeholder (required) and optional {displayName} so invitees see a compelling message.
- [page](https://create.roblox.com/docs/production/promotion/invite-prompts) **[[first-session-onboarding]]** Keep custom invite prompt messages short; overly long text that overflows the UI will not be shown at all.

## Numbers
- [page](https://create.roblox.com/docs/production/promotion/invite-prompts) LaunchData maximum length: **200 characters**
- [page](https://create.roblox.com/docs/production/promotion/invite-prompts) Launch data retrieval wait pattern in example: **10 attempts, 1 second delay**

## Tools
SocialService, ExperienceInviteOptions, HttpService, Creator Dashboard Notifications

## He points to
- Friend Invite Reward System

## Topics
[[first-session-onboarding]] [[social-features-and-virality]] [[titles-descriptions]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
