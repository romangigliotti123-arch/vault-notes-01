---
title: "Docs: production / promotion / experience-notifications"
url: https://create.roblox.com/docs/production/promotion/experience-notifications.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / promotion / experience-notifications

[Open](https://create.roblox.com/docs/production/promotion/experience-notifications.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs on Experience Notifications: eligibility (100+ visits, not moderated, manage permission), creating notification strings in the Creator Dashboard, sending via the Open Cloud package's createUserNotification, parameters, launch/analytics data, opt-in prompts, delivery throttling and analytics metrics, plus personalization and no-dark-pattern rules.

## Tips
- [page](https://create.roblox.com/docs/production/promotion/experience-notifications) **[[core-loops-and-game-design]]** Make notifications personalized to the recipient's in-game activity; avoid generic advertising-style messages.
- [page](https://create.roblox.com/docs/production/promotion/experience-notifications) **[[common-mistakes]]** Avoid purely informational notifications; prompt an immediate action like rejoining or responding to a challenge.
- [page](https://create.roblox.com/docs/production/promotion/experience-notifications) **[[common-mistakes]]** Don't use disguised ads, false time pressure, bait-and-switch free rewards, or pre-loaded purchases; these violate notification rules.
- [page](https://create.roblox.com/docs/production/promotion/experience-notifications) **[[core-loops-and-game-design]]** Never gate gameplay behind enabling notifications; players must be able to progress without opting in.
- [page](https://create.roblox.com/docs/production/promotion/experience-notifications) **[[ads-and-sponsored-experiences]]** Notifications are throttled by engagement: more clicks means more reach, so write high-CTR messages.
- [page](https://create.roblox.com/docs/production/promotion/experience-notifications) **[[analytics-metrics]]** Use a new notification string per variant to A/B test; the Analytics tab tracks each string as a separate row.
- [page](https://create.roblox.com/docs/production/promotion/experience-notifications) **[[first-session-onboarding]]** Trigger PromptOptIn in a contextually relevant moment; check CanPromptOptInAsync first, wrapped in pcall.
- [page](https://create.roblox.com/docs/production/promotion/experience-notifications) **[[analytics-metrics]]** Stats show only after 100 aggregate impressions; per-notification rows appear once they reach 100 impressions.

## Numbers
- [page](https://create.roblox.com/docs/production/promotion/experience-notifications) Minimum visits since launch to send notifications: **100**
- [page](https://create.roblox.com/docs/production/promotion/experience-notifications) Throttle: notifications per user per experience per day: **1**
- [page](https://create.roblox.com/docs/production/promotion/experience-notifications) Minimum aggregate impressions to show performance stats: **100**
- [page](https://create.roblox.com/docs/production/promotion/experience-notifications) Notification string character limit: **99 characters**
- [page](https://create.roblox.com/docs/production/promotion/experience-notifications) Launch data max size: **200 bytes**
- [page](https://create.roblox.com/docs/production/promotion/experience-notifications) Minimum age for opted-in notifications: **13+**
- [page](https://create.roblox.com/docs/production/promotion/experience-notifications) Dashboard stats tracked: **Opted-in Users, Impressions, Clicks, CTR, Turn Off rate, Dismiss rate**

## Tools
Creator Dashboard (notification strings, analytics), Open Cloud Luau package (OpenCloud.V2.UserNotification), ExperienceNotificationService (PromptOptIn, CanPromptOptInAsync), Player:GetJoinData()

## He points to
- Player invite prompts (docs)
- Open Cloud API

## Topics
[[ads-and-sponsored-experiences]] [[analytics-metrics]] [[common-mistakes]] [[core-loops-and-game-design]] [[first-session-onboarding]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
