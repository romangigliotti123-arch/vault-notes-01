---
title: "Docs: production / monetization / commerce-products"
url: https://create.roblox.com/docs/production/monetization/commerce-products.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / monetization / commerce-products

[Open](https://create.roblox.com/docs/production/monetization/commerce-products.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs on Commerce products: importing real-world Shopify catalog items, bundling digital benefits (eligibility thresholds), creating/moderating/selling commerce products, implementing purchases via CommerceService, handling grants/refunds via webhooks, and Product Detail Page customization.

## Tips
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) **[[monetisation-other]]** Commerce products require creator 18+, ID and email verification, 2-step verification, and submitted Business Information before you can sell them.
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) **[[monetisation-other]]** Only US-based users can purchase commerce products; users must be 13+ (18+ in Texas). Verify with PolicyService.
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) **[[monetisation-other]]** Game must be public, have content maturity labels, and comply with Community, Advertising and Commerce Standards on an ongoing basis.
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) **[[common-mistakes]]** Changing a Shopify item's price takes all associated bundles off sale and resubmits them for bundling fee processing.
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) **[[common-mistakes]]** Deleting an imported catalog item automatically deletes all commerce products containing it; you must re-import and recreate them.
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) **[[common-mistakes]]** Roblox does not auto-revoke developer products granted as digital benefits on refund; handle revocation via CommerceProductOrderRefunded webhook.
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) **[[monetisation-other]]** Digital benefit bundling requires >100,000 average DAU over 90 days, or >1,000,000 Robux average monthly earnings over 90 days, plus a bundle sold within 3 months of approval (or a $50,000 USD/year ad spend agreement).
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) **[[monetisation-other]]** Bundled digital benefits must not be previously sold items, Robux, currency, random/chance-based items, or require extra steps after payment.
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) **[[monetisation-other]]** Avatar items cannot be created inside the commerce product flow; create the avatar item first, then bundle it.
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) **[[common-mistakes]]** Two identical catalog items cannot be on sale at once; take the existing bundle off sale before listing another with the same item.
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) **[[monetisation-other]]** Limits: 500 commerce products per game, and at most 100 products on sale at once per game.
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) **[[first-session-onboarding]]** On Android the commerce flow forces portrait mode; use PromptCommerceProductPurchaseFinished to reorient the player after the webview closes.
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) **[[common-mistakes]]** PromptCommerceProductPurchaseFinished fires when the prompt closes and does not indicate a successful purchase; confirm via receipts or order events.
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) **[[monetisation-other]]** Product descriptions must be complete (functionality, specs, returns, origin) in Shopify, or the product will not be approved for sale.
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) **[[team-and-budget]]** Group-owned commerce stores require Configure and spend group revenue and Create and edit community experiences permissions; group ownership transfer is blocked while the group owns commerce items.
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) **[[common-mistakes]]** Shopify content edits (name, images, description, variants) go through moderation; the live listing keeps showing the previously approved version until approval.
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) **[[pricing]]** Product detail page supports up to five Additional Information accordions via Shopify metafields in the Roblox.pdp_info_ namespace.

## Numbers
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) Max commerce products per game: **500**
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) Max products on sale at once per game: **100**
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) Bundling eligibility: average daily active users (90 days): **>100,000**
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) Bundling eligibility: average monthly Robux earnings (90 days): **>1,000,000 Robux**
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) Time to sell first bundle after bundling approval: **within 3 months**
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) Alternative bundling eligibility: written ad spend agreement: **$50,000 USD in one year**
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) Minimum user age (Texas): **18+**
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) Minimum user age (other US states): **13+**
- [page](https://create.roblox.com/docs/production/monetization/commerce-products) Product Detail Page additional info accordions: **up to 5**

## Tools
Creator Hub / Creator Dashboard, Shopify (Roblox sales channel), Class.CommerceService, Class.MarketplaceService.ProcessReceipt, Class.PolicyService, Roblox webhooks (CommerceProductOrderPaid / CommerceProductOrderRefunded)

## He points to
- Roblox Commerce Standards
- Roblox Community Standards
- Roblox Advertising Standards
- Customizing the Product Detail Page (Roblox docs)

## Topics
[[common-mistakes]] [[first-session-onboarding]] [[monetisation-other]] [[pricing]] [[team-and-budget]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
