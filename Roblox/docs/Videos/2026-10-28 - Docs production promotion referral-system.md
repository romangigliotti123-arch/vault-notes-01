---
title: "Docs: production / promotion / referral-system"
url: https://create.roblox.com/docs/production/promotion/referral-system.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / promotion / referral-system

[Open](https://create.roblox.com/docs/production/promotion/referral-system.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on the friend referral system: how to detect the inviter via GetJoinData().ReferredByPlayerId in PlayerAdded, grant rewards to inviter and invitee, publish a reward banner in Creator Hub (Engagement > Referral Rewards, one published banner at a time), and prevent abuse with one-time rewards, cooldowns and DataStore tracking.

## Tips
- [page](https://create.roblox.com/docs/production/promotion/referral-system) **[[first-session-onboarding]]** Add an in-game button that opens the friend invite modal so players can see the referral reward banner.
- [page](https://create.roblox.com/docs/production/promotion/referral-system) **[[retention-d1-d7]]** Referral rewards for both inviter and invitee encourage players to bring new players back into the game.
- [page](https://create.roblox.com/docs/production/promotion/referral-system) **[[social-features-and-virality]]** Use the ReferredByPlayerId from GetJoinData in PlayerAdded to identify the inviter and fire a RemoteEvent to the client.
- [page](https://create.roblox.com/docs/production/promotion/referral-system) **[[social-features-and-virality]]** Give the reward banner an accurate description, since it must match the referral system implemented in Studio.
- [page](https://create.roblox.com/docs/production/promotion/referral-system) **[[common-mistakes]]** Guard against abuse: reward each invitee only once (DataStore flag), add inviter cooldowns, and monitor for suspicious activity.
- [page](https://create.roblox.com/docs/production/promotion/referral-system) **[[thumbnails-icons]]** Replace the default reward banner icon with an image representing your game.
- [page](https://create.roblox.com/docs/production/promotion/referral-system) **[[updates-live-ops]]** Set start and end dates and optional reward limits (e.g. 3 rewards per inviter) on each reward banner.

## Numbers
- [page](https://create.roblox.com/docs/production/promotion/referral-system) Eligibility: **Game must be live at least 1 day** (Docs FAQ on eligible games)
- [page](https://create.roblox.com/docs/production/promotion/referral-system) Reward limit example: **Up to 3 rewards per inviter** (Optional reward restriction on banner)
- [page](https://create.roblox.com/docs/production/promotion/referral-system) Active banners: **Only one published banner at a time** (Many can be created, one shown)
- [page](https://create.roblox.com/docs/production/promotion/referral-system) Referral link expiry: **Never expires** (Docs FAQ)

## Tools
Roblox Studio, Creator Hub (Engagement > Referral Rewards), DataStoreService

## He points to
- Players.PlayerAdded
- Player:GetJoinData()

## Topics
[[common-mistakes]] [[first-session-onboarding]] [[retention-d1-d7]] [[social-features-and-virality]] [[thumbnails-icons]] [[updates-live-ops]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
