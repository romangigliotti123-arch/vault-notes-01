---
title: "Disabling Cross-Game Sales of Passes and Dev Products and Introducing the Transfers API"
url: https://devforum.roblox.com/t/disabling-cross-game-sales-of-passes-and-dev-products-and-introducing-the-transfers-api/4618396
creator: Roblox DevForum
official: false
advice_density: medium
date: 2026-05-04
views: 6294
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Disabling Cross-Game Sales of Passes and Dev Products and Introducing the Transfers API

[Open](https://devforum.roblox.com/t/disabling-cross-game-sales-of-passes-and-dev-products-and-introducing-the-transfers-api/4618396) | Roblox DevForum | 6,294 views | 2026-05-04

## Summary
Roblox DevForum announcement: cross-game sales of developer products and passes end May 29 (2026) to curb fraud. Introduces the Transfers API (PromptRobuxTransferAsync, BindReceiptHandler) for in-game Robux transfers: creators earn 10%, recipients 90%, Plus subscription required for senders, age checks and parental approval rules apply, with daily/monthly limits.

## Tips
- [page](https://devforum.roblox.com/t/disabling-cross-game-sales-of-passes-and-dev-products-and-introducing-the-transfers-api/4618396) **[[monetisation-other]]** Migrate tipping/donation mechanics to the Transfers API before May 29 or they stop working when cross-game DevProduct/pass sales are disabled.
- [page](https://devforum.roblox.com/t/disabling-cross-game-sales-of-passes-and-dev-products-and-introducing-the-transfers-api/4618396) **[[monetisation-other]]** Implement transfers with PromptRobuxTransferAsync, then process the result in BindReceiptHandler to confirm the transfer and grant rewards.
- [page](https://devforum.roblox.com/t/disabling-cross-game-sales-of-passes-and-dev-products-and-introducing-the-transfers-api/4618396) **[[monetisation-other]]** Let your game control amount selection (buttons, sliders, input); the amount is fixed once the Roblox Transfer UI opens.
- [page](https://devforum.roblox.com/t/disabling-cross-game-sales-of-passes-and-dev-products-and-introducing-the-transfers-api/4618396) **[[testing-debugging-and-qa]]** For testing cross-sold items in a private copy, use Studio's free purchase feature; for collaborator testing, use a separate game copy with test IDs.
- [page](https://devforum.roblox.com/t/disabling-cross-game-sales-of-passes-and-dev-products-and-introducing-the-transfers-api/4618396) **[[business-and-payouts]]** Transfers API creator commission (10%) is DevEx-eligible but held on standard hold and can be rolled back if the game is moderated; the API cannot be used to pay people.
- [page](https://devforum.roblox.com/t/disabling-cross-game-sales-of-passes-and-dev-products-and-introducing-the-transfers-api/4618396) **[[business-and-payouts]]** Use group payouts, not the Transfers API, to pay collaborators.
- [page](https://devforum.roblox.com/t/disabling-cross-game-sales-of-passes-and-dev-products-and-introducing-the-transfers-api/4618396) **[[age-ratings-moderation-and-tos]]** Expect transfers to require age checks and, for under-18 users, parental approval per transfer; transfers pending safety steps are canceled and refunded after 7 days.
- [page](https://devforum.roblox.com/t/disabling-cross-game-sales-of-passes-and-dev-products-and-introducing-the-transfers-api/4618396) **[[monetisation-other]]** Transfers API has a 0% platform fee, so recipients get 90% versus 60% via cross-game passes (Roblox takes 30%, affiliate creator 10%).

## Numbers
- [page](https://devforum.roblox.com/t/disabling-cross-game-sales-of-passes-and-dev-products-and-introducing-the-transfers-api/4618396) Transfers API creator commission: **10% of transfer (DevEx-eligible)**
- [page](https://devforum.roblox.com/t/disabling-cross-game-sales-of-passes-and-dev-products-and-introducing-the-transfers-api/4618396) Recipient share via Transfers API: **90% (no platform fee)**
- [page](https://devforum.roblox.com/t/disabling-cross-game-sales-of-passes-and-dev-products-and-introducing-the-transfers-api/4618396) Recipient share via cross-game passes/DevProducts: **60% (Roblox fee 30%, affiliate 10%)**
- [page](https://devforum.roblox.com/t/disabling-cross-game-sales-of-passes-and-dev-products-and-introducing-the-transfers-api/4618396) Transfers API daily limit: **500 Robux/day**
- [page](https://devforum.roblox.com/t/disabling-cross-game-sales-of-passes-and-dev-products-and-introducing-the-transfers-api/4618396) Transfers API monthly limit: **1000 Robux/month**
- [page](https://devforum.roblox.com/t/disabling-cross-game-sales-of-passes-and-dev-products-and-introducing-the-transfers-api/4618396) Pending transfer auto-cancel window: **7 days**
- [page](https://devforum.roblox.com/t/disabling-cross-game-sales-of-passes-and-dev-products-and-introducing-the-transfers-api/4618396) Transfers API launch date / cross-game sales cutoff: **Transfers API May 4; cross-game sales disabled May 29**

## Tools
PromptRobuxTransferAsync, BindReceiptHandler, Studio free purchase feature

## He points to
- Roblox DevForum post by dinobotsnarl824 (May 2026)
- Transfers API documentation (linked by Roblox)

## Quotes
- [page](https://devforum.roblox.com/t/disabling-cross-game-sales-of-passes-and-dev-products-and-introducing-the-transfers-api/4618396) "Creators have used developer products and passes to facilitate Robux donations and tipping in games. However, these tools were never designed for peer-to-peer Robux transfers."
- [page](https://devforum.roblox.com/t/disabling-cross-game-sales-of-passes-and-dev-products-and-introducing-the-transfers-api/4618396) "For each transfer, Roblox doesn't take a platform fee. Creators using the API earn a 10% commission and recipients receive 90%."

## Topics
[[age-ratings-moderation-and-tos]] [[business-and-payouts]] [[monetisation-other]] [[testing-debugging-and-qa]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
