---
title: "Docs: cloud / guides / experience-notifications"
url: https://create.roblox.com/docs/cloud/guides/experience-notifications.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / guides / experience-notifications

[Open](https://create.roblox.com/docs/cloud/guides/experience-notifications.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Cloud API docs for experience notifications: sending UserNotification via Open Cloud with API key, using notification string assets created in Creator Dashboard, parameters for personalization, launch/analytics data, and a one-notification-per-day-per-experience limit per user.

## Tips
- [page](https://create.roblox.com/docs/cloud/guides/experience-notifications) **[[updates-live-ops]]** Create the notification string in the Creator Dashboard first; there is no Open Cloud API to create it, so plan templates before scripting sends.
- [page](https://create.roblox.com/docs/cloud/guides/experience-notifications) **[[social-features-and-virality]]** Use parameters in notification strings (e.g. {userId-friend}, {points}) to personalize each recipient's message instead of sending generic text.
- [page](https://create.roblox.com/docs/cloud/guides/experience-notifications) **[[social-features-and-virality]]** Include launch_data in notifications to route joining users to a specific coordinate or personalize their join experience.
- [page](https://create.roblox.com/docs/cloud/guides/experience-notifications) **[[analytics-metrics]]** Set analytics_data category per notification type to segment and compare performance across notification categories.
- [page](https://create.roblox.com/docs/cloud/guides/experience-notifications) **[[retention-d1-d7]]** Target notifications at moments that matter (async activity, achievements, user mentions) so they bring players back via the Join button.
- [page](https://create.roblox.com/docs/cloud/guides/experience-notifications) **[[anti-exploit-and-security]]** Keep the Open Cloud API key secret; send requests server-side only, since the key is passed in the x-api-key header.

## Numbers
- [page](https://create.roblox.com/docs/cloud/guides/experience-notifications) Notification limit: **1 per user per day, per experience** (Throttle applies per user from a given experience; limit reached is reported back)
- [page](https://create.roblox.com/docs/cloud/guides/experience-notifications) Eligibility: **Opted-in users aged 13+** (Only opted-in users age 13+ receive experience notifications)

## Tools
Roblox Open Cloud UserNotification API, Creator Dashboard, curl

## He points to
- Delivery system (Engine guide)
- Experiences guide

## Topics
[[analytics-metrics]] [[anti-exploit-and-security]] [[retention-d1-d7]] [[social-features-and-virality]] [[updates-live-ops]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
