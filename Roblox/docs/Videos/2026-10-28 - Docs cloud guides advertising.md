---
title: "Docs: cloud / guides / advertising"
url: https://create.roblox.com/docs/cloud/guides/advertising.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / guides / advertising

[Open](https://create.roblox.com/docs/cloud/guides/advertising.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox Cloud API docs for the Advertising API (Ads Management v1). Covers API key scopes, listing advertisable experiences, checking campaign eligibility, creating ENGAGEMENT campaigns with micro-USD budgets and targeting, polling delivery status, editing or cancelling campaigns, error codes, and a pointer to item advertising.

## Tips
- [page](https://create.roblox.com/docs/cloud/guides/advertising) **[[ads-and-sponsored-experiences]]** Before creating a campaign, call campaign-options for the universe to confirm eligibility; NO_PERMISSION or BLOCKED means it can't advertise.
- [page](https://create.roblox.com/docs/cloud/guides/advertising) **[[ads-and-sponsored-experiences]]** Send a UUID in x-idempotency-key on campaign creation; replaying the same key with an identical body within 24 hours returns the original campaign, avoiding duplicates.
- [page](https://create.roblox.com/docs/cloud/guides/advertising) **[[ads-and-sponsored-experiences]]** New campaigns start as IN_REVIEW until ad-policy review completes; poll campaigns:batchGetStatus (up to 100 IDs per call) until SERVING, NOT_SERVING or REJECTED.
- [page](https://create.roblox.com/docs/cloud/guides/advertising) **[[ads-and-sponsored-experiences]]** Use durationInDays, not endTime, to set campaign length; endTime returns a 400 in v1.
- [page](https://create.roblox.com/docs/cloud/guides/advertising) **[[ads-and-sponsored-experiences]]** Budget decreases on running campaigns apply at next midnight in the billing account time zone; increases apply immediately, so raise budgets carefully.
- [page](https://create.roblox.com/docs/cloud/guides/advertising) **[[ads-and-sponsored-experiences]]** Cancelling a campaign (status CANCELLED) is permanent; use PAUSED to temporarily stop spend and ACTIVE to resume.
- [page](https://create.roblox.com/docs/cloud/guides/advertising) **[[ads-and-sponsored-experiences]]** Use targeting arrays (ageGroups, countries, devices) to narrow audiences; an empty array means all for that dimension.
- [page](https://create.roblox.com/docs/cloud/guides/advertising) **[[ads-and-sponsored-experiences]]** Creatives must be Open Cloud image assets uploaded via the Assets API; reference their IDs in creativeAssetIds.
- [page](https://create.roblox.com/docs/cloud/guides/advertising) **[[analytics-metrics]]** Read campaign spend, impressions and plays through the Analytics API, not the Ads endpoints.
- [page](https://create.roblox.com/docs/cloud/guides/advertising) **[[ai-and-tools]]** Store the API key and send it in the x-api-key header; grant only ad.campaign:read, ad.campaign:write and ad.billing:read scopes.
- [page](https://create.roblox.com/docs/cloud/guides/advertising) **[[common-mistakes]]** paymentType and budget.type are fixed after creation; choose CREDIT_CARD/ADS_CREDIT/INVOICE and DAILY/LIFETIME deliberately.

## Numbers
- [page](https://create.roblox.com/docs/cloud/guides/advertising) Money unit: **Budget amounts in micro-USD strings; "5000000" = $5.00** (amountMicros field on budget object)
- [page](https://create.roblox.com/docs/cloud/guides/advertising) Max campaign duration: **3650 days** (schedule.durationInDays maximum)
- [page](https://create.roblox.com/docs/cloud/guides/advertising) Batch status limit: **100 campaigns per call** (campaigns:batchGetStatus)
- [page](https://create.roblox.com/docs/cloud/guides/advertising) Idempotency window: **24 hours** (identical body with same x-idempotency-key returns original campaign)
- [page](https://create.roblox.com/docs/cloud/guides/advertising) Targeting age groups: **AGE_13_17, AGE_18_24, AGE_25_PLUS** (targeting.ageGroups options)

## Tools
Roblox Ads Management API (v1), Open Cloud Assets API, Open Cloud Analytics API, curl, Sponsored Items Manager

## He points to
- Sponsored items (Roblox docs)
- Roblox DevForum (for API support posts)
- Roblox API reference: Advertising section (adconfiguration.roblox.com)

## Topics
[[ads-and-sponsored-experiences]] [[ai-and-tools]] [[analytics-metrics]] [[common-mistakes]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
