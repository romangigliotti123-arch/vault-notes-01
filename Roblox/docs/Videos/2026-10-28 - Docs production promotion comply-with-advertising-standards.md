---
title: "Docs: production / promotion / comply-with-advertising-standards"
url: https://create.roblox.com/docs/production/promotion/comply-with-advertising-standards.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / promotion / comply-with-advertising-standards

[Open](https://create.roblox.com/docs/production/promotion/comply-with-advertising-standards.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on advertising standards for games with ads. Covers content rules (no child endangerment, violence, PII), disclosure requirements (clear ad label, must not mimic Roblox official ad disclosures), data privacy (no third-party ad server calls, only self-uploaded ad content), user safety (check PolicyService AreAdsAllowed and hide/replace/block ads for ineligible users), and ad system integrity (no bots, misclassified metadata, or hidden disclosures). Violations may lead to suspension.

## Tips
- [page](https://create.roblox.com/docs/production/promotion/comply-with-advertising-standards) **[[ads-and-sponsored-experiences]]** Ensure all ad content is policy-compliant and clearly disclosed as advertising in users' language; do not mimic Roblox's official ad disclosures (different font/color).
- [page](https://create.roblox.com/docs/production/promotion/comply-with-advertising-standards) **[[ads-and-sponsored-experiences]]** Only serve ad content you uploaded yourself inside your game; do not call third-party ad servers, even for analytics.
- [page](https://create.roblox.com/docs/production/promotion/comply-with-advertising-standards) **[[ads-and-sponsored-experiences]]** Call PolicyService:GetPolicyInfoForPlayerAsync per player and check AreAdsAllowed; if false, hide, replace, or block ads for that user.
- [page](https://create.roblox.com/docs/production/promotion/comply-with-advertising-standards) **[[ads-and-sponsored-experiences]]** If the whole game is an ad, block ineligible users (AreAdsAllowed false) from entering, e.g. kick with a message.
- [page](https://create.roblox.com/docs/production/promotion/comply-with-advertising-standards) **[[common-mistakes]]** Do not use bots or large engagement campaigns to fake ad impressions, misclassify metadata to boost ad delivery, or obscure ad disclosures; these risk suspension and payout revocation.
- [page](https://create.roblox.com/docs/production/promotion/comply-with-advertising-standards) **[[ads-and-sponsored-experiences]]** Use Roblox localization tools to make ad disclosures readable across languages.
- [page](https://create.roblox.com/docs/production/promotion/comply-with-advertising-standards) **[[common-mistakes]]** Do not include phone numbers or other PII in ad content that leads users off-platform; this violates ad standards.

## Tools
PolicyService, Players:Kick

## He points to
- Advertising Standards: Prohibited Advertising Practices and Content
- Advertising Standards: Publisher Integrity
- Independent Advertising Policy
- Roblox localization tools

## Topics
[[ads-and-sponsored-experiences]] [[common-mistakes]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
