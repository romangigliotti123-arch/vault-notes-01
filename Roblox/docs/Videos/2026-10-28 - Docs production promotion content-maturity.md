---
title: "Docs: production / promotion / content-maturity"
url: https://create.roblox.com/docs/production/promotion/content-maturity.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / promotion / content-maturity

[Open](https://create.roblox.com/docs/production/promotion/content-maturity.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on the Maturity & Compliance questionnaire: how content maturity labels (Minimal, Mild, Moderate, Restricted) and content descriptors are generated, which age groups each label reaches, and the obligations to answer accurately, update answers after changes, and use PolicyService for regional restrictions on paid random items and paid item trading.

## Tips
- [page](https://create.roblox.com/docs/production/promotion/content-maturity) **[[monetisation-other]]** If a game lacks content maturity info, Roblox restricts its playability for all players. Complete the questionnaire for every game to reach the largest appropriate audience.
- [page](https://create.roblox.com/docs/production/promotion/content-maturity) **[[common-mistakes]]** Base questionnaire answers on the most mature or extreme content players can encounter, not the average. Inaccurate answers can lead to game and account moderation.
- [page](https://create.roblox.com/docs/production/promotion/content-maturity) **[[development-process-and-speed]]** Re-take the questionnaire and resubmit whenever an update changes any answer; this is required to remain compliant with Community Standards.
- [page](https://create.roblox.com/docs/production/promotion/content-maturity) **[[common-mistakes]]** Do not add age-restricted content before receiving the Moderate or Restricted label; the label must be granted first.
- [page](https://create.roblox.com/docs/production/promotion/content-maturity) **[[common-mistakes]]** Title or description containing social hangout references will classify the game as a social hangout; keep titles and descriptions accurate.
- [page](https://create.roblox.com/docs/production/promotion/content-maturity) **[[monetisation-other]]** For games with paid random items or paid item trading, call PolicyService.GetPolicyInfoForPlayerAsync and hide, replace or block those features when ArePaidRandomItemsRestricted or IsPaidItemTradingAllowed indicate restriction.
- [page](https://create.roblox.com/docs/production/promotion/content-maturity) **[[common-mistakes]]** Genre selection does not determine maturity. Answer the questionnaire from actual in-game content even when it overlaps a genre.
- [page](https://create.roblox.com/docs/production/promotion/content-maturity) **[[common-mistakes]]** Asset uploads (images, meshes, audio) are subject to moderation regardless of the maturity label if they show realistic violence, blood, crude humor or romantic themes.
- [page](https://create.roblox.com/docs/production/promotion/content-maturity) **[[ai-and-tools]]** Answer the AI interaction question based on whether players can interact with generative AI in the game, not on whether AI was used in development.

## Numbers
- [page](https://create.roblox.com/docs/production/promotion/content-maturity) Label access: Minimal/Mild: **Roblox Kids (ages 5–8) and Select (ages 9–15)** (Default age access by content maturity label)
- [page](https://create.roblox.com/docs/production/promotion/content-maturity) Label access: Moderate: **Roblox Select (9–15) and standard Roblox (16+)** (Default age access by content maturity label)
- [page](https://create.roblox.com/docs/production/promotion/content-maturity) Label access: Content May Vary: **Age-checked users 16+ only** (Default age access by content maturity label)
- [page](https://create.roblox.com/docs/production/promotion/content-maturity) Label access: Restricted: **Age-verified users 18+ only** (Default age access by content maturity label)
- [page](https://create.roblox.com/docs/production/promotion/content-maturity) Social hangouts without private spaces: **Players 16+** (Minimum age for social hangout games)
- [page](https://create.roblox.com/docs/production/promotion/content-maturity) Social hangouts with private spaces: **Age-verified 18+** (Minimum age for social hangouts with private spaces)
- [page](https://create.roblox.com/docs/production/promotion/content-maturity) Free-form user creation: **Players 16+** (Minimum age for games with free-form user creation)
- [page](https://create.roblox.com/docs/production/promotion/content-maturity) Sensitive issue primary theme: **Players 16+, not recommended unless age-verified** (Minimum age for games primarily themed on sensitive issues)

## Tools
Maturity & Compliance Questionnaire (Creator Dashboard), Class.PolicyService, PolicyService.GetPolicyInfoForPlayerAsync

## He points to
- Roblox Kids and Select
- Age-Restricted Content Policy
- Roblox Community Standards
- Class.PolicyService API reference

## Quotes
- [page](https://create.roblox.com/docs/production/promotion/content-maturity) "If your game contains inaccurate content maturity information, your game and account are subject to moderation."
- [page](https://create.roblox.com/docs/production/promotion/content-maturity) "Base your answers on the most mature or extreme content players can encounter within your game."

## Topics
[[ai-and-tools]] [[common-mistakes]] [[development-process-and-speed]] [[monetisation-other]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
