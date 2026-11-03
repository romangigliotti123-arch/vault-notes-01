---
title: "Docs: resources / feature-packages / engagement-rewards"
url: https://create.roblox.com/docs/resources/feature-packages/engagement-rewards.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / feature-packages / engagement-rewards

[Open](https://create.roblox.com/docs/resources/feature-packages/engagement-rewards.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page for the Engagement Rewards feature package. Explains installing Core and Engagement Rewards packages, implementing rewardClaimedHandlerFunction, configuring Time and Daily reward tiers in EngagementRewardsConfig, and customizing the default UI.

## Tips
- [page](https://create.roblox.com/docs/resources/feature-packages/engagement-rewards) **[[retention-d1-d7]]** Use Time rewards at roughly 10, 30 and 60 minutes of play to give players reasons to stay in session longer.
- [page](https://create.roblox.com/docs/resources/feature-packages/engagement-rewards) **[[retention-d1-d7]]** Use Daily login streak rewards, starting with small consumables on day 1 and a durable item after seven straight days.
- [page](https://create.roblox.com/docs/resources/feature-packages/engagement-rewards) **[[retention-d1-d7]]** Set isAlignedToStreakResetTime to true if you want day-2 rewards available exactly 24 hours after day 1 claim, not at midnight.
- [page](https://create.roblox.com/docs/resources/feature-packages/engagement-rewards) **[[retention-d1-d7]]** Set isHiddenOnJoin to true if you don't want reward popups shown automatically when players join.
- [page](https://create.roblox.com/docs/resources/feature-packages/engagement-rewards) **[[core-loops-and-game-design]]** Write time thresholds as multiplication (e.g. 2 * 60 * 60) so values are readable; use tiny values only for testing.
- [page](https://create.roblox.com/docs/resources/feature-packages/engagement-rewards) **[[common-mistakes]]** Time reward progress resets to 0 each session, so players lose all progress toward Time rewards when they leave.
- [page](https://create.roblox.com/docs/resources/feature-packages/engagement-rewards) **[[common-mistakes]]** Do not ship the example rewardClaimedHandlerFunction; it only prints, so replace it with your real reward-granting logic.
- [page](https://create.roblox.com/docs/resources/feature-packages/engagement-rewards) **[[ui-ux-design]]** Use the tabDisplayName, tabOrder and description fields to customize reward tab labels and ordering without code changes.
- [page](https://create.roblox.com/docs/resources/feature-packages/engagement-rewards) **[[ui-ux-design]]** Modify Core objects with care, since changes to FeaturePackagesCore.Objects affect all feature packages.
- [page](https://create.roblox.com/docs/resources/feature-packages/engagement-rewards) **[[building-art-and-assets]]** Reward icons must be Roblox image asset IDs, not decal IDs.
- [page](https://create.roblox.com/docs/resources/feature-packages/engagement-rewards) **[[ui-ux-design]]** Set effect = Types.RewardEffect.Valuable to give high-value rewards a distinct background frame in the UI.

## Numbers
- [page](https://create.roblox.com/docs/resources/feature-packages/engagement-rewards) Example time reward thresholds: **10 min, 30 min, 1 hour** (Suggested thresholds for published game Time rewards)
- [page](https://create.roblox.com/docs/resources/feature-packages/engagement-rewards) Example daily streak milestone: **7 consecutive days** (Durable item suggested after seven straight daily logins)
- [page](https://create.roblox.com/docs/resources/feature-packages/engagement-rewards) Default requiredDaysVisitedStreak: **N/A (required)** (Consecutive daily logins needed; no default)
- [page](https://create.roblox.com/docs/resources/feature-packages/engagement-rewards) Default reward quantity: **1** (Quantity default when not specified)

## Tools
Roblox Studio Toolbox, Core feature package, Engagement Rewards feature package

## He points to
- Roblox Feature Packages docs (Core)

## Topics
[[building-art-and-assets]] [[common-mistakes]] [[core-loops-and-game-design]] [[retention-d1-d7]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
