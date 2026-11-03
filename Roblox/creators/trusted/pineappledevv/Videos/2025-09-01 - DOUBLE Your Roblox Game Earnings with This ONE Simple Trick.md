---
title: "DOUBLE Your Roblox Game Earnings with This ONE Simple Trick"
url: https://youtu.be/gXKoxaK6Ufg
creator: PineappleDev
official: false
advice_density: medium
date: 2025-09-01
views: 6802
transcript: auto-captions
confidence: medium
tags: [roblox, pineappledevv, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# DOUBLE Your Roblox Game Earnings with This ONE Simple Trick

[Watch](https://youtu.be/gXKoxaK6Ufg) | pineappledevv | 6,802 views | 2025-09-01

## Summary
Shows a cascading multiplier gamepass/devproduct chain: each purchase raises the player's money multiplier and the next tier's price. Claims ~9% conversion and large sales on a top game via analytics. Explains three components: product ID list, server-side increment on purchase, and client-side button/price display logic.

## Tips
- [0:41](https://youtu.be/gXKoxaK6Ufg?t=41) **[[monetisation-devproducts]]** Sell a cheap first multiplier (e.g. 1.1x for 9 Robux) so most players will buy it; escalate each tier's multiplier and price in a chain.
- [0:41](https://youtu.be/gXKoxaK6Ufg?t=41) **[[monetisation-devproducts]]** Keep multipliers modest (e.g. 1.1x steps) so the game does not become pay-to-win, per the speaker's reasoning.
- [2:09](https://youtu.be/gXKoxaK6Ufg?t=129) **[[monetisation-devproducts]]** Cascading tiered purchases can carry a weak monetising game; the speaker says monetisation is hard on Roblox and this lifted a game's revenue.
- [2:30](https://youtu.be/gXKoxaK6Ufg?t=150) **[[monetisation-devproducts]]** Implement with a product ID list ordered by tier; on ProcessReceipt, check if the ID is in the list and increment the player's saved multiplier count.
- [3:21](https://youtu.be/gXKoxaK6Ufg?t=201) **[[ui-ux-design]]** On the client, hide the buy button once all tiers are owned; otherwise prompt the next product ID indexed by owned count plus one.
- [4:03](https://youtu.be/gXKoxaK6Ufg?t=243) **[[scripting-and-performance]]** Fetch product info with MarketplaceService for the next tier's price using a retry loop so the displayed Robux price updates reliably.

## Numbers
- [1:27](https://youtu.be/gXKoxaK6Ufg?t=87) conversion rate: **almost 9% on a top earning game** (Speaker's top-earning game, stated as roughly 9% conversion)
- [1:27](https://youtu.be/gXKoxaK6Ufg?t=87) top product sales: **1,700 sales for almost 12,000 Robux** (Top-selling cascading devproduct in speaker's game)
- [2:09](https://youtu.be/gXKoxaK6Ufg?t=129) second product sales: **almost 500 sales for 8,000 Robux** (Second tier in the chain)
- [2:09](https://youtu.be/gXKoxaK6Ufg?t=129) third product sales: **almost 200 sales for 5,000 Robux** (Third tier in the chain)
- [0:00](https://youtu.be/gXKoxaK6Ufg?t=0) tier prices: **9 Robux (1.1x), 19 Robux (1.2x), 29 Robux (1.3x)** (Escalating price chain for multiplier tiers)

## Games
- **Stud Miner** [4:56](https://youtu.be/gXKoxaK6Ufg?t=296): Speaker's new simple mining game; promoted in video, no design lesson given.
- **Unnamed top-earning game** [1:27](https://youtu.be/gXKoxaK6Ufg?t=87): Uses cascading plus-carry devproducts; top-selling and top-grossing item; ~9% conversion.

## Tools
Roblox Studio, MarketplaceService

## Quotes
- [0:00](https://youtu.be/gXKoxaK6Ufg?t=0) "Basically nothing. Right now, if you want this to be better, you'll probably want to do 2x money so that it's more enticing to the player."
- [2:30](https://youtu.be/gXKoxaK6Ufg?t=150) "In my experience, it's pretty difficult to actually monetize Roblox games."

## Topics
[[monetisation-devproducts]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[pineappledevv - How to make successful Roblox games]]
