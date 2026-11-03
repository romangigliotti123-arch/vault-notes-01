---
title: "Docs: production / monetization / engagement-based-payouts"
url: https://create.roblox.com/docs/production/monetization/engagement-based-payouts.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / monetization / engagement-based-payouts

[Open](https://create.roblox.com/docs/production/monetization/engagement-based-payouts.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on engagement-based payouts (deprecated July 24, 2025, replaced by Creator Rewards). Explains Premium Playtime metrics in the Creator Dashboard and how to use the Premium purchase modal in-game, with best practices and Luau code for checking membership and prompting purchase.

## Tips
- [page](https://create.roblox.com/docs/production/monetization/engagement-based-payouts) **[[roblox-platform-changes]]** Engagement-Based Payouts was deprecated July 24, 2025 and replaced by the Creator Rewards program; don't build strategy around the old program.
- [page](https://create.roblox.com/docs/production/monetization/engagement-based-payouts) **[[monetisation-other]]** Engagement payouts were based on Premium subscribers' time in the game, regardless of game size, and were additional to Pass earnings.
- [page](https://create.roblox.com/docs/production/monetization/engagement-based-payouts) **[[analytics-metrics]]** Use Premium Playtime Score (daily Premium engagement time) for immediate feedback on new features; Premium Playtime Robux Earned aggregates 28 days, so it lags.
- [page](https://create.roblox.com/docs/production/monetization/engagement-based-payouts) **[[monetisation-other]]** Premium should not be a requirement to enjoy a game; don't show the Premium modal as a paywall to non-Premium players.
- [page](https://create.roblox.com/docs/production/monetization/engagement-based-payouts) **[[monetisation-other]]** Describe Premium benefits honestly in the game description and don't promise Robux or out-of-game rewards you don't control.
- [page](https://create.roblox.com/docs/production/monetization/engagement-based-payouts) **[[monetisation-other]]** Offer Premium perks as exclusive merch, not tactical gameplay advantages like ultra-powerful weapons non-Premium players can't match.
- [page](https://create.roblox.com/docs/production/monetization/engagement-based-payouts) **[[scripting-and-performance]]** Check player.MembershipType == Enum.MembershipType.Premium before scripting Premium logic or triggering the modal.
- [page](https://create.roblox.com/docs/production/monetization/engagement-based-payouts) **[[monetisation-other]]** Trigger MarketplaceService:PromptPremiumPurchase(player) in-game so players buy Premium and receive the initial Robux stipend without leaving the game.
- [page](https://create.roblox.com/docs/production/monetization/engagement-based-payouts) **[[scripting-and-performance]]** Debounce the Premium purchase modal (example: show at most once every 5 seconds) and handle Players.PlayerMembershipChanged to react to upgrades.

## Numbers
- [page](https://create.roblox.com/docs/production/monetization/engagement-based-payouts) Program deprecation date: **July 24, 2025** (Engagement-Based Payouts replaced by Creator Rewards)
- [page](https://create.roblox.com/docs/production/monetization/engagement-based-payouts) Premium Playtime Robux Earned window: **28 days** (aggregates each user's behavior over past 28 days)
- [page](https://create.roblox.com/docs/production/monetization/engagement-based-payouts) Example modal debounce: **5 seconds** (code sample shows modal at most once every few seconds)

## Tools
Creator Dashboard, MarketplaceService:PromptPremiumPurchase(), Players.PlayerMembershipChanged

## He points to
- Creator Rewards program (replacement for Engagement-Based Payouts)

## Topics
[[analytics-metrics]] [[monetisation-other]] [[roblox-platform-changes]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
