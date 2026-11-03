---
title: "Docs: production / publishing / account-verification"
url: https://create.roblox.com/docs/production/publishing/account-verification.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / publishing / account-verification

[Open](https://create.roblox.com/docs/production/publishing/account-verification.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on account verification. Covers verifying identity via age check or government ID (requirements: 13+, photo ID, mobile camera; steps in Settings > Account Info), what verification unlocks (more asset distribution, audio under 10 seconds, plugin monetisation, voice chat, selling priced assets), and checking verification status in scripts with Player:IsVerified() and VerifiedLevel Low/High gating.

## Tips
- [page](https://create.roblox.com/docs/production/publishing/account-verification) **[[scripting-and-performance]]** Use Player:IsVerified(Enum.VerifiedLevel.High) to gate ranked matchmaking queues; verified users are less likely to cheat, spam, or get blocked.
- [page](https://create.roblox.com/docs/production/publishing/account-verification) **[[common-mistakes]]** Don't use High verification for everyday features; use Enum.VerifiedLevel.Low (the default) for standard features like in-game trading to deter alternate accounts.
- [page](https://create.roblox.com/docs/production/publishing/account-verification) **[[business-and-payouts]]** Complete government ID verification and create a seller account before selling priced assets on the Creator Store.
- [page](https://create.roblox.com/docs/production/publishing/account-verification) **[[monetisation-other]]** Verify your account to monetise plugins and distribute more assets, which are unavailable otherwise.

## Numbers
- [page](https://create.roblox.com/docs/production/publishing/account-verification) Minimum age for government ID verification: **13 years** (Required to verify via government-issued photo ID)
- [page](https://create.roblox.com/docs/production/publishing/account-verification) Maximum audio length for verified accounts: **Under 10 seconds** (Verified accounts can distribute audio assets under 10 seconds)

## Tools
Roblox Studio, Roblox app / roblox.com Settings, Age ID verification flow

## He points to
- Age ID Verification FAQs
- Roblox Privacy Policy
- Roblox Facial Media Capture Notice
- Creator Store - Distribute and sell assets

## Topics
[[business-and-payouts]] [[common-mistakes]] [[monetisation-other]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
