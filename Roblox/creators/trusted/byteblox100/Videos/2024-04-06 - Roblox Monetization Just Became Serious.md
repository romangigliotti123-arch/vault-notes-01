---
title: "Roblox Monetization Just Became Serious"
url: https://youtu.be/7NRp4BEYrsQ
creator: ByteBlox
official: false
advice_density: medium
date: 2024-04-06
views: 25754
transcript: auto-captions
confidence: medium
tags: [roblox, byteblox100, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Roblox Monetization Just Became Serious

[Watch](https://youtu.be/7NRp4BEYrsQ) | byteblox100 | 25,754 views | 2024-04-06

## Summary
Walkthrough of Roblox's subscription feature: creating a subscription in Creator Hub (product type durable/consumable/currency, price, period), prompting purchases and checking status via MarketplaceService from server scripts, retrieving localized price info from a client script, and the creator's complaints about the UI, prompt-only access, and lack of perks.

## Tips
- [1:15](https://youtu.be/7NRp4BEYrsQ?t=75) **[[monetisation-other]]** Set subscription product type to durable if players keep items after cancelling; use consumable if items should be removed when the subscription lapses.
- [2:05](https://youtu.be/7NRp4BEYrsQ?t=125) **[[monetisation-other]]** Activate the subscription in Creator Hub before prompting; an inactive subscription won't show for purchase.
- [2:05](https://youtu.be/7NRp4BEYrsQ?t=125) **[[scripting-and-performance]]** Call MarketplaceService:PromptSubscriptionPurchase from a server Script, passing the player and subscription ID.
- [3:08](https://youtu.be/7NRp4BEYrsQ?t=188) **[[monetisation-other]]** Check GetUserSubscriptionStatusAsync on the server to gate subscriber-only benefits; it returns subscribed and renewing flags.
- [5:15](https://youtu.be/7NRp4BEYrsQ?t=315) **[[pricing]]** Use GetSubscriptionProductInfoAsync from a LocalScript (run context client) to show localized display price, since prices vary by region.
- [6:59](https://youtu.be/7NRp4BEYrsQ?t=419) **[[client-server-and-remotes]]** Keep payment-related calls (prompt, status, details, history) on the server; they fail or are unavailable in LocalScripts.
- [8:28](https://youtu.be/7NRp4BEYrsQ?t=508) **[[monetisation-other]]** Consider a subscription tied to in-game progress gating, since the speaker suggests this is not currently supported natively.

## Numbers
- [3:08](https://youtu.be/7NRp4BEYrsQ?t=188) Subscription price example: **$14.99 in Creator Hub (shown as local currency per region)**
- [6:18](https://youtu.be/7NRp4BEYrsQ?t=378) Regional display price example: **$14.99 shown as $2.99 for a Canadian viewer, per speaker**

## Tools
Creator Hub, MarketplaceService

## Quotes
- [8:04](https://youtu.be/7NRp4BEYrsQ?t=484) "Subscriptions can only be prompted, so the speaker wants a subscriptions button in the menu."

## Topics
[[client-server-and-remotes]] [[monetisation-other]] [[pricing]] [[scripting-and-performance]]

Back to [[byteblox100 - How to make successful Roblox games]]
