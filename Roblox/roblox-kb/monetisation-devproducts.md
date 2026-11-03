---
title: Monetisation Devproducts
topic: monetisation-devproducts
theme: Monetisation
sources: 140 videos
creators: [1Coal, 1_Bruce, Alex Builds Games, AlvinBlox, ArTheDev, Arow, B Ricey, Bemmy, BrawlDev, BubuTheDev, ByteBlox, CallMeDogey, Crusherfire, Deconstructor of Fun, GameMakers, Generalist Programmer, GuideRealm, Izzzyzzz, JustDucksey, Lnor Roblox, LovJak, Matt The Method, MonarchDev, MonzterDEV, MoseyTube, Mulch, Perstile, PineappleDev, PolarBear, Quez, Rapstrike GFX, RoDev, RoTrends (tracker), Roblox, Roblox Creator Docs, Roblox Creators, Roblox DevForum, RoyalDev, Seibo, Suphi Kaner, ThatGuyEvan, TheDevKing, ThePurpleGuy, Tizzy, VuukStudios, Yann, bubDEV, janisjanis01, kra_DeZ, rasdev]
source_dates: 2018-08-07 to 2026-10-28
tags: [roblox, knowledge-base, monetisation-devproducts]
---

# Monetisation Devproducts

_developer products, consumables, offers, limited-time deals._

Evidence base: 327 extracted items from 140 videos by 1Coal, 1_Bruce, Alex Builds Games, AlvinBlox, ArTheDev, Arow, B Ricey, Bemmy, BrawlDev, BubuTheDev, ByteBlox, CallMeDogey, Crusherfire, Deconstructor of Fun, GameMakers, Generalist Programmer, GuideRealm, Izzzyzzz, JustDucksey, Lnor Roblox, LovJak, Matt The Method, MonarchDev, MonzterDEV, MoseyTube, Mulch, Perstile, PineappleDev, PolarBear, Quez, Rapstrike GFX, RoDev, RoTrends (tracker), Roblox, Roblox Creator Docs, Roblox Creators, Roblox DevForum, RoyalDev, Seibo, Suphi Kaner, ThatGuyEvan, TheDevKing, ThePurpleGuy, Tizzy, VuukStudios, Yann, bubDEV, janisjanis01, kra_DeZ, rasdev (2018-08-07 to 2026-10-28). Roblox changes quickly: check the date on each source and see Date context below.

## Overview
Creators and Roblox staff agree that developer products (repeatable, consumable purchases) should be the backbone of Roblox monetisation. They cover currency, boosts, offline-earnings doubling, hints, streak recovery, and cheap fun items. They out-earn one-time game passes because spend is uncapped. Key practices: get the first purchase early with a cheap starter pack (after the tutorial or a milestone, often time-limited). Show offers at the moment of need. Offer many price tiers and highlight the best-value bundle. Make purchase entry points plentiful. Sell sparingly (a few sales per year), and protect the economy with scarce hard currency, event currency and limited items. Technically: implement ProcessReceipt correctly, list products in Shop with icons, track purchases yourself, and use segments, Experiments and Configs for personalisation and testing. Indie revenue claims are self-reported and unverified.

## Rules and findings
- **Use developer products for anything repeatable; game passes for one-time perks** (multiple-creators): Dev products can be bought many times, so spend is uncapped. Passes are one-time. Use products for currency, boosts, ammo, potions and consumables. Official docs say they generally monetise better. Indie claims: CallMeDogey 1.9M vs 841k Robux, kra_DeZ products earned most while passes earned almost nothing, 1_Bruce products drove most revenue (all self-reported). Sources: [AlvinBlox 2018-08 26:40](https://youtu.be/h92s4Xn26oc?t=1600), [AlvinBlox 2024-06 12:03](https://youtu.be/5YNFRCD0pd0?t=723), [AlvinBlox 2018-08 25:18](https://youtu.be/h92s4Xn26oc?t=1518), [AlvinBlox 2024-06 0:00](https://youtu.be/5YNFRCD0pd0?t=0), [kra_DeZ 2026-09 13:51](https://youtu.be/cJ-YzHHhQs8?t=831). Newest source 2026-10-28.
- **Convert one-time passes into consumables where possible** (multiple-creators): Turn permanent perks such as 2x offline earnings into a rebuyable product, so it recurs every login/day. Tizzy's 24-hour base lock became his top seller within about 2 days. Roblox also warns permanent boosts (permanent double cash) are risky to balance. Sources: [Tizzy 2026-06 5:24](https://youtu.be/zoz3PSMqets?t=324), [MoseyTube 2026-07 4:36](https://youtu.be/-PoyiiGhoNo?t=276), [Tizzy 2026-06 4:02](https://youtu.be/zoz3PSMqets?t=242), [Tizzy 2026-06 5:24](https://youtu.be/zoz3PSMqets?t=324), [Tizzy 2026-06 4:42](https://youtu.be/zoz3PSMqets?t=282). Newest source 2026-07-14.
- **Drive the first purchase** (multiple-creators): Players who have bought once are far likelier to buy again, so design progression and offers around the first purchase. Use low-entry products and starter packs, and stack cheap tiers (e.g. 5 and 9 Robux) to get past the threshold. Sources: [TheDevKing 2020-05 8:33](https://youtu.be/Zqz_gclwM0M?t=513), [TheDevKing 2020-05 8:33](https://youtu.be/Zqz_gclwM0M?t=513), [Roblox DevForum 2022-06](https://devforum.roblox.com/t/introducing-monetization-metrics-for-the-analytics-dashboard/1826688), [Tizzy 2026-10 16:44](https://youtu.be/_JyiKfNNqls?t=1004), [Roblox 2025-09 23:49](https://youtu.be/MJ-zYfL10Ew?t=1429). Newest source 2026-10-14.
- **Offer a starter pack at the right time** (multiple-creators): Show a cheap, discounted bundle after the tutorial or a first milestone (about 20-60 min in), not in the first 30 seconds. Time-limited (e.g. 24h) creates urgency. Price like a cup of coffee. Test product type, price, art, prompt timing and duration. Sources: [Roblox DevForum 2019-03](https://devforum.roblox.com/t/monetisation-101-how-to-effectively-generate-revenue-in-your-roblox-game/246902), [Roblox DevForum 2019-03](https://devforum.roblox.com/t/monetisation-101-how-to-effectively-generate-revenue-in-your-roblox-game/246902), [TheDevKing 2020-05 9:57](https://youtu.be/Zqz_gclwM0M?t=597), [Roblox DevForum 2023-12](https://devforum.roblox.com/t/understand-the-roblox-algorithm/2772921), [Roblox DevForum 2023-12](https://devforum.roblox.com/t/understand-the-roblox-algorithm/2772921). Newest source 2026-10-28.
- **Use personalised time-limited offers at progression points** (multiple-creators): Offers shown before the first, second and third dungeon gave Dungeon Quest +180% payer conversion on day one (official). Escalate bundle prices gradually at later milestones, hours apart, without frustrating players. Sources: [Roblox 2024-09 16:08](https://youtu.be/QC6XWgJRJEM?t=968), [Roblox 2024-09 16:08](https://youtu.be/QC6XWgJRJEM?t=968), [Roblox DevForum 2019-03](https://devforum.roblox.com/t/monetisation-101-how-to-effectively-generate-revenue-in-your-roblox-game/246902). Newest source 2024-09-23.
- **Segment offers by player type** (multiple-creators): Cheap starter for new players, mid-tier upgrade for casuals, limited high-priced offers for high spenders. Use GetPlayerSegmentsAsync to show low-cost items to non-spenders and bundles to those with purchase history. Unlock elite and private offers at spending thresholds. Sources: [Roblox 2025-09 3:29](https://youtu.be/MJ-zYfL10Ew?t=209), [Roblox 2025-09 21:14](https://youtu.be/MJ-zYfL10Ew?t=1274), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/analytics). Newest source 2026-10-28.
- **Show the offer at the moment of need** (multiple-creators): When a player can't afford something, offer the exact currency/Robux amount needed. Show the 2x offline prompt when collecting offline earnings. Tizzy: show the error first and open the cash shop directly on the third failed attempt, not immediately. Sources: [TheDevKing 2020-05 12:36](https://youtu.be/Zqz_gclwM0M?t=756), [Tizzy 2026-06 13:31](https://youtu.be/zoz3PSMqets?t=811), [Tizzy 2026-06 8:15](https://youtu.be/zoz3PSMqets?t=495), [Tizzy 2026-07 18:56](https://youtu.be/nggNvUILQ1I?t=1136), [Tizzy 2026-06 8:56](https://youtu.be/zoz3PSMqets?t=536). Newest source 2026-10-28.
- **Solve a real pain point** (multiple-creators): Best sellers address pains players already feel: grinding (speed, cash), AFK theft (base lock), missing out (offline earnings), manual collection (auto collect), being stuck (hints) or losing progress (streak recovery). Products should be must-haves, not nice-to-haves. Sources: [Tizzy 2026-06 11:27](https://youtu.be/zoz3PSMqets?t=687), [Tizzy 2026-06 14:12](https://youtu.be/zoz3PSMqets?t=852), [MoseyTube 2026-07 1:51](https://youtu.be/-PoyiiGhoNo?t=111), [MoseyTube 2026-07 1:51](https://youtu.be/-PoyiiGhoNo?t=111), [MoseyTube 2026-07 2:35](https://youtu.be/a170E9klbP4?t=155). Newest source 2026-07-24.
- **Provide many entry points to the shop** (multiple-creators): Add HUD shop button, a plus button beside the currency counter, in-world NPCs/buttons, and place products where players walk (base entrance, spawn). CallMeDogey's spawn-placed pet products drove most repeat purchases. Make the store easy to reach and route players there for free rewards. Enable in-game Robux shopping so players needn't leave. Sources: [Tizzy 2026-06 6:52](https://youtu.be/zoz3PSMqets?t=412), [MoseyTube 2026-07 3:44](https://youtu.be/-PoyiiGhoNo?t=224), [Tizzy 2026-06 10:20](https://youtu.be/zoz3PSMqets?t=620), [CallMeDogey 2025-01 10:14](https://youtu.be/USJC5l_wpuY?t=614), [CallMeDogey 2025-01 10:14](https://youtu.be/USJC5l_wpuY?t=614). Newest source 2026-10-12.
- **Offer many price tiers** (multiple-creators): Cover different spend levels. MoseyTube recommends 20-30 products (he built 59, admitting that may be excessive). Offer a mix of consumable and durable items, multiple price points, and expand offerings of top sellers. Give free players options to try spending. Sources: [MoseyTube 2026-06 5:13](https://youtu.be/Kh_XKYw8ocU?t=313), [MoseyTube 2026-06 5:13](https://youtu.be/Kh_XKYw8ocU?t=313), [MoseyTube 2026-04 2:44](https://youtu.be/sFr7htxsnR4?t=164), [MoseyTube 2026-04 3:25](https://youtu.be/sFr7htxsnR4?t=205), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/get-started/strategies). Newest source 2026-10-28.
- **Structure currency packs with value cues** (multiple-creators): Discount larger bundles, add bonus amounts (e.g. 10% more free), tag the best-value pack and make it visually largest. Use uneven tiers (100, 2000, 7600, 10200). Larger cash packs with better value lifted Driving Empire revenue per user 8% (official). Sources: [Roblox Creators 2023-01 4:25](https://youtu.be/okAygI1sxsA?t=265), [Roblox Creators 2023-01 4:25](https://youtu.be/okAygI1sxsA?t=265), [Roblox Creators 2023-08 4:39](https://youtu.be/lOOvOIJoMi4?t=279), [Roblox DevForum 2021-05](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207), [Roblox 2023-09 18:34](https://youtu.be/Z-ZKqBPdl44?t=1114). Newest source 2023-09-19.
- **Extend top tiers above your best seller** (multiple-creators): Sort products by sales descending and add higher tiers above the best seller (e.g. +30 and +100 speed above +10). 10,000 Robux products can sell: CallMeDogey's was bought by 9 people; 1_Bruce's sold 640 times (self-reported). Sources: [Tizzy 2026-06 0:50](https://youtu.be/zoz3PSMqets?t=50), [CallMeDogey 2025-01 10:14](https://youtu.be/USJC5l_wpuY?t=614), [1_Bruce 2025-12 7:02](https://youtu.be/wKI3PBO3bB0?t=422). Newest source 2026-06-15.
- **Deliver instant satisfaction and clear feedback** (multiple-creators): A product should satisfy within the first minute. Give visual/audio reward feedback and confirm inventory receipt to prevent scam complaints. Avoid overpriced products with brief payoff; reserve high Robux prices for currency. Add recurring products players naturally repeat (e.g. bail-out). Sources: [Roblox DevForum 2021-05](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207), [Roblox DevForum 2021-05](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207), [Roblox Creators 2023-02 41:16](https://youtu.be/BsyU-SJ9L-c?t=2476), [Roblox DevForum 2021-05](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207), [Roblox DevForum 2021-05](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207). Newest source 2023-02-23.
- **Keep hard currency scarce and protect the economy** (multiple-creators): Let players earn small amounts slowly. Use event-specific currency so hoarders can't buy out event content on day one. Don't make top items too OP or sell cash packs early (Tizzy believes this fried his economy). Rotating shop with rising prices can sink currency. Let players sample paid items with earned currency. Sources: [Roblox DevForum 2019-03](https://devforum.roblox.com/t/monetisation-101-how-to-effectively-generate-revenue-in-your-roblox-game/246902), [Roblox DevForum 2019-03](https://devforum.roblox.com/t/monetisation-101-how-to-effectively-generate-revenue-in-your-roblox-game/246902), [Roblox Creators 2023-01 0:00](https://youtu.be/YdplC2WVkWc?t=0), [Tizzy 2026-10 15:20](https://youtu.be/_JyiKfNNqls?t=920), [Roblox Creators 2023-01 0:00](https://youtu.be/YdplC2WVkWc?t=0). Newest source 2026-10-14.
- **Run sales rarely and check health first** (multiple-creators): Run sales a handful of times per year at consistent cadence; frequent sales train players to wait. Emergency Response saw 2-4x revenue spikes from 25-30% sales. Use Configs for flash sales without restarting servers. Sources: [Roblox Creators 2023-01 0:00](https://youtu.be/YdplC2WVkWc?t=0), [Roblox Creators 2023-01 0:00](https://youtu.be/YdplC2WVkWc?t=0), [Roblox Creators 2023-01 0:00](https://youtu.be/YdplC2WVkWc?t=0), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/game-design/balance-virtual-economies), [Roblox DevForum 2019-03](https://devforum.roblox.com/t/monetisation-101-how-to-effectively-generate-revenue-in-your-roblox-game/246902). Newest source 2026-10-28.
- **Use scarcity and limited items** (multiple-creators): Make the most powerful item scarce and pricier; Tizzy's limited 1,000 Robux item (1,000 stock) sold well and he advises launching limited/whale products from the start. Limited-stat products like global runes also sell. Limited supply supports resale value (Adopt Me). Sources: [Tizzy 2026-10 14:36](https://youtu.be/_JyiKfNNqls?t=876), [Tizzy 2026-10 14:36](https://youtu.be/_JyiKfNNqls?t=876), [Tizzy 2026-10 16:01](https://youtu.be/_JyiKfNNqls?t=961), [1_Bruce 2025-12 6:19](https://youtu.be/wKI3PBO3bB0?t=379), [Roblox 2025-09 26:35](https://youtu.be/MJ-zYfL10Ew?t=1595). Newest source 2026-10-28.
- **Sell fun, social and cheap novelty items** (multiple-creators): Items beyond progression sell: Nuke All (kills all players), jump scares in a horror game, a four-bullet gun. Self-reported: Nuke All earned 19,349 Robux in 90 days. Sources: [MoseyTube 2026-08 4:26](https://youtu.be/xIBc5He_sy4?t=266), [kra_DeZ 2026-09 7:35](https://youtu.be/ZradA-cygP0?t=455), [kra_DeZ 2026-10 4:07](https://youtu.be/dE0njfPNsdY?t=247), [kra_DeZ 2026-09 7:55](https://youtu.be/ZradA-cygP0?t=475). Newest source 2026-10-11.
- **Be cautious with plain currency packs** (single-mention): Alex Builds Games rates currency packs D tier ('mid'); buyers prefer direct items. This conflicts with Roblox and TheDevKing advising currency sales, though official examples sell currency to buy items. Sources: [Alex Builds Games 2026-06 4:24](https://youtu.be/x_SflcuSi1w?t=264), [Alex Builds Games 2026-06 4:24](https://youtu.be/x_SflcuSi1w?t=264), [TheDevKing 2020-05 6:06](https://youtu.be/Zqz_gclwM0M?t=366), [Roblox Creators 2023-01 13:31](https://youtu.be/vQNJztcS2AI?t=811), [Roblox Creators 2023-01 2:54](https://youtu.be/vQNJztcS2AI?t=174). Newest source 2026-06-16.
- **Monetise convenience, not basic movement** (multiple-creators): Monetise speed/convenience in the core loop. Spongebob TD gave 2x free to group members, converting a $5 3x-speed product. Sell core perks as products and put exclusives behind subscriptions (Adopt Me: 250 Robux for two equipped pets). Sources: [Roblox 2025-09 25:13](https://youtu.be/MJ-zYfL10Ew?t=1513), [Roblox 2024-09 26:39](https://youtu.be/ETDit6eO4sQ?t=1599), [Roblox 2026-10 14:32](https://youtu.be/qLP05zvMsW0?t=872). Newest source 2026-10-12.
- **Tie offers to events; avoid popup spam** (multiple-creators): Launch themed items and first-purchase bonuses with events, accessible to all levels; a one-time first-purchase bonus per Premium currency tier drove a 50% lift for two weeks (official). Don't stack offers after the first purchase; Tizzy's cash-shop redirect appeared about 3-5 times per session. Sources: [Roblox 2024-09 15:26](https://youtu.be/QC6XWgJRJEM?t=926), [Roblox 2024-09 18:08](https://youtu.be/QC6XWgJRJEM?t=1088), [Roblox 2024-09 18:49](https://youtu.be/QC6XWgJRJEM?t=1129), [Roblox 2025-09 23:49](https://youtu.be/MJ-zYfL10Ew?t=1429), [Tizzy 2026-06 8:56](https://youtu.be/zoz3PSMqets?t=536). Newest source 2026-06-15.
- **Introduce new products and price points; copy and test** (multiple-creators): Add products, gamepasses or subscriptions and make purchases worth the price. If users aren't buying resources via IAP, lower prices or add options. Copy repeated competitor patterns (e.g. Sell Lemons' 2x offline earnings) and test them. Sources: [Roblox DevForum 2024-02](https://devforum.roblox.com/t/discovery-on-roblox-past-present-and-future-vision/2859111), [MonzterDEV 2024-03 13:44](https://youtu.be/em15yK5RjBk?t=824), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/analytics/economy-events), [Tizzy 2026-06 6:05](https://youtu.be/zoz3PSMqets?t=365). Newest source 2026-10-28.
- **Implement ProcessReceipt correctly** (multiple-creators): Use ProcessReceipt, never PromptProductPurchaseFinished, to grant items. Set the callback once from a single server Script. Return PurchaseGranted only after granting, else NotProcessedYet to retry. Required before listing products. Flagged products drop off external surfaces until fixed. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/shop), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/developer-products), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/developer-products), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/developer-products), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/developer-products). Newest source 2026-10-28.
- **Prompt purchases and set up products properly** (one-creator-repeated): Publish the game, create the product in Creator Hub, copy the ID, and call MarketplaceService:PromptProductPurchase from a LocalScript (e.g. button click). Grant on the server. Sources: [AlvinBlox 2024-06 0:36](https://youtu.be/5YNFRCD0pd0?t=36), [AlvinBlox 2024-06 1:12](https://youtu.be/5YNFRCD0pd0?t=72), [AlvinBlox 2024-06 11:22](https://youtu.be/5YNFRCD0pd0?t=682), [AlvinBlox 2024-06 13:16](https://youtu.be/5YNFRCD0pd0?t=796). Newest source 2024-06-04.
- **List products in Shop with icons** (one-creator-repeated): Listed products can be surfaced by Roblox outside your game. Add a custom icon (max 512x512, key details inside the circle; jpg/png/bmp) or a default is used. Unlisted products still work in-game. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/shop), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/developer-products), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/developer-products). Newest source 2026-10-28.
- **Track purchases and use recommendation APIs sensibly** (one-creator-repeated): Roblox doesn't record per-user developer product purchase history; save it in DataStoreService. Call RankProductsAsync once on join (strict rate limit). Wrap RecommendTopProductsAsync (up to 50 results) in task.spawn and filter unbuyable items. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/developer-products), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/developer-products), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/developer-products), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/developer-products). Newest source 2026-10-28.
- **Script prices dynamically; test pricing with Experiments** (one-creator-repeated): Use MarketplaceService for prices rather than hard-coding UI before enabling Managed Pricing. A/B test price points and discounts with Experiments; Product analytics can show up to 8 top sellers. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/regional-pricing), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/game-design/balance-virtual-economies), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/developer-products). Newest source 2026-10-28.
- **Offer reward-style items at 3-10 Robux value** (one-creator-repeated): For rewarded offers: boosters, currency, extra lives, temporary privileges worth about 3-10 Robux; not randomized items. Make them relevant, scaled to progression, limited/rare, and offered at strategic moments. Cap rewarded item value near 100x earnings per ad view and estimate cannibalisation conservatively. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/promotion/rewarded-video-ads), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/promotion/rewarded-video-ads), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/promotion/rewarded-video-ads), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/promotion/rewarded-video-ads), [Roblox Creators 2025-08 22:35](https://youtu.be/7AtvvUxvCaU?t=1355). Newest source 2026-10-28.
- **Handle misissued products** (single-mention): Use purchase data to find affected buyers in the time window and compensate them. Sources: [Roblox Creators 2023-06 0:48](https://youtu.be/yn4V-fBdUm8?t=48). Newest source 2023-06-01.
- **Grant only server-side, only inside ProcessReceipt** (multiple-creators): Never grant passes or products from client prompt events such as PromptProductPurchaseFinished; they can be spoofed. Grant from a server script that owns the grant. Route every currency change through one player-manager setter instead of editing leaderstats directly. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/scripting/security/client-server-boundary), [B Ricey 2022-04 5:45](https://youtu.be/5bI6l6SHBDU?t=345), [janisjanis01 2023-09 5:31](https://youtu.be/9aQpeTCZ7yM?t=331). Newest source 2026-10-28.
- **Save before you grant; gate purchases on load success** (multiple-creators): Check hasErrored before allowing purchases, since saves fail after a failed data load. Grant only after the data save succeeds, or a failed save gives the item free. If the save fails, return NotProcessedYet. On retry, check the stored PurchaseId and return PurchaseGranted to avoid double awards. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing), [B Ricey 2022-04 9:51](https://youtu.be/5bI6l6SHBDU?t=591). Newest source 2026-10-28.
- **Create a unique developer product for each bundle** (single-mention): Make a new product per bundle so its sales can be tracked separately. This lets you judge each offer on its own sales and run sales-health checks before changing prices. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/resources/feature-packages/bundles), [GuideRealm 2026-10 6:37](https://youtu.be/ltbZzXRrDF8?t=397). Newest source 2026-10-28.
- **Sell pass-style perks as developer products** (multiple-creators): Roblox cannot gift game passes directly. Sell a developer product that acts as the pass, record ownership in a DataStore, and purchases stack and can be gifted. Bundling gamepass-style perks into one product lifted a single high-value purchase; Yann's 500-coin product was his best seller. Sources: [Crusherfire 2025-12 5:40](https://youtu.be/6Q_p2ObUXSo?t=340), [Yann 2026-05 3:25](https://youtu.be/dbNA3K8lt2w?t=205), [Yann 2026-05 2:44](https://youtu.be/dbNA3K8lt2w?t=164). Newest source 2026-05-12.
- **Add skip buttons at progression walls** (multiple-creators): In obbies, a skip-stage button is where the creator says most obby money comes from. In rebirth-style games, rebirth-skip products also sold well. Sell skips as repeatable developer products so players can buy them again. Sources: [1Coal 2023-05 1:20](https://youtu.be/JzB8fpyofnw?t=80), [Yann 2026-07 2:53](https://youtu.be/Bw2ty2T46z4?t=173). Newest source 2026-07-23.
- **Offer a cheap early boost consumable** (one-creator-repeated): A 5-Robux 1.5x cash boost is simple to script and was used to lift per-conversion rate early in monetisation. It reflects one creator's experience, so test it against your own conversion before relying on it. Sources: [janisjanis01 2025-11 10:16](https://youtu.be/QnAoCsC-4ig?t=616), [janisjanis01 2026-05 8:37](https://youtu.be/BLOToGi2Qt4?t=517), [janisjanis01 2025-11 10:16](https://youtu.be/QnAoCsC-4ig?t=616), [janisjanis01 2026-05 8:37](https://youtu.be/BLOToGi2Qt4?t=517). Newest source 2026-05-10.
- **Place a high-value consumable inside the spin or shop loop** (multiple-creators): Yann said a spin that rewards top dragons was his top earner. rasdev says repeat consumables (spins, boosts, restocks, eggs) drive recurring revenue. Put high-value items where the player's loop already brings them back. Sources: [Yann 2026-07 2:53](https://youtu.be/Bw2ty2T46z4?t=173), [rasdev 2026-10 2:02](https://youtu.be/53OBGXktIPY?t=122). Newest source 2026-10-20.
- **Use bulk-bundle discounts on repeat-buy items** (one-creator-repeated): One crate was 349 Robux; bulk bundles showed about 174 Robux per crate, roughly 50% off. Bemmy says the bulk discount pushed spending. This is one game's anecdote, so A/B test the discount tiers before committing. Sources: [Bemmy 2025-06 0:00](https://youtu.be/-Z0C5YJtnqY?t=0), [Bemmy 2025-06 5:06](https://youtu.be/-Z0C5YJtnqY?t=306), [Bemmy 2025-06 3:57](https://youtu.be/-Z0C5YJtnqY?t=237). Newest source 2025-06-28.
- **Sell random drops only with disclosed odds and a guaranteed path** (multiple-creators): Random products sell well (Yann's lucky-block style). Pair them with a guaranteed option: janisjanis01 sold a guaranteed mutation and a 499-Robux high-tier crate. Bemmy framed a 1.78% exotic as a 'secret-tier pull'; show true odds so buyers are not misled and to reduce policy risk. Sources: [Yann 2026-05 4:48](https://youtu.be/dbNA3K8lt2w?t=288), [janisjanis01 2025-09 8:44](https://youtu.be/YVKHlrlWn-k?t=524), [Bemmy 2025-06 3:57](https://youtu.be/-Z0C5YJtnqY?t=237), [Bemmy 2025-06 0:00](https://youtu.be/-Z0C5YJtnqY?t=0), [Bemmy 2025-06 1:08](https://youtu.be/-Z0C5YJtnqY?t=68). Newest source 2026-05-12.
- **Keep purchase prompts small during play** (single-mention): rasdev says a giant purchase button on screen during play hurts retention and discovery. Use small, contextual prompts shown at the moment of need instead of persistent overlays. Sources: [rasdev 2026-04 3:22](https://youtu.be/G15TVsyC61g?t=202). Newest source 2026-04-30.
- **Add products with addItemAsync and dashboard IDs** (multiple-creators): Add products with addItemAsync(id, Enum.InfoType.Product); IDs come from Creator Dashboard > Developer Products. Replace every placeholder ID before release and test data saving in a published test place. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/resources/modules/merch-booth), [GuideRealm 2026-10 6:37](https://youtu.be/ltbZzXRrDF8?t=397). Newest source 2026-10-28.
- **Route ProcessReceipt through a product-ID table** (multiple-creators): Map each developer product ID to its handler in one table, so adding a product means adding one function rather than another branch. For tiered multiplier chains, keep an ordered ID list and increment the player's saved count when a receipt for that ID is granted. Sources: [Suphi Kaner 2023-06 52:26](https://youtu.be/UAdE8-AfuMo?t=3146), [PineappleDev 2025-09 2:30](https://youtu.be/gXKoxaK6Ufg?t=150). Newest source 2025-09-01.
- **Centralise all product and pass IDs in one shared module** (single-mention): Store every gamepass and developer product ID in one ReplicatedStorage module, grouped by category. Client UI and server scripts then read the same source and cannot drift apart. Sources: [Roblox DevForum 2023-11](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585). Newest source 2023-11-02.
- **Roll back and defer when the save fails** (single-mention): Force DataStore:save() before granting. If the save fails, deduct the amount you already granted and return NotProcessedYet, so Roblox retries the receipt and the player cannot keep the item for free. Sources: [Suphi Kaner 2023-06 57:14](https://youtu.be/UAdE8-AfuMo?t=3434). Newest source 2023-06-15.
- **Make each purchase idempotent with an IdempotencyKey** (single-mention): Pass an IdempotencyKey on purchase requests and use Client.RequestOnce, so retried commands or purchases apply at most once. This prevents double grants when networks retry. Sources: [Roblox DevForum 2026-07](https://devforum.roblox.com/t/scribe-v261-persistent-typed-auto-replicated-player-data-built-on-profilestore/4738905). Newest source 2026-07-15.
- **Set every new developer product to Listed** (single-mention): New developer products default to Not Listed and will not appear in the Shop until set to Listed. Check the status of each product when you create it or republish it. Sources: [Roblox DevForum 2026-06](https://devforum.roblox.com/t/introducing-shop-a-personalized-in-game-storefront/4701505). Newest source 2026-06-24.
- **Treat correct ProcessReceipt as a launch gate** (single-mention): Per the DevForum post, correct ProcessReceipt handling is required for eligibility for external surfacing and ensures purchases are delivered immediately. Finish and test it before expecting external promotion. Sources: [Roblox DevForum 2026-06](https://devforum.roblox.com/t/introducing-shop-a-personalized-in-game-storefront/4701505). Newest source 2026-06-24.
- **Sell paid revives, difficulty potions and mass-grow consumables** (multiple-creators): In one game, paid revives and difficulty potions were the main developer-product earners. In another, seeds, grow-all-flowers, gear and starter/super packs drove nearly all revenue. Sell the consumable players will repeat at a failure or friction point. Sources: [PineappleDev 2025-03 0:32](https://youtu.be/a4PQqMC8ruA?t=32), [Quez 2025-06 0:34](https://youtu.be/WOG3Rttf-V4?t=34), [Quez 2025-06 1:58](https://youtu.be/WOG3Rttf-V4?t=118). Newest source 2025-06-21.
- **Time-limit the starter pack to about 15 minutes** (multiple-creators): A 79-Robux starter pack with a 15-minute window reportedly roughly doubled to tripled revenue (self-reported). Quez reported a starter pack among the top three sellers. Set a short window so the offer creates urgency. Sources: [1Coal 2024-03 2:25](https://youtu.be/gWNOANEPYLY?t=145), [1Coal 2024-03 2:25](https://youtu.be/gWNOANEPYLY?t=145), [Quez 2025-06 1:58](https://youtu.be/WOG3Rttf-V4?t=118). Newest source 2025-06-21.
- **Add a donation board for players who won't buy passes** (single-mention): In Idle Dice a donation board brought 216 Robux from developer products alone, plus 41 Robux premium payouts. It reaches players who will not buy gamepasses. Sources: [PineappleDev 2024-09 2:25](https://youtu.be/UBs1bebPu0s?t=145), [PineappleDev 2024-09 3:52](https://youtu.be/UBs1bebPu0s?t=232). Newest source 2024-09-06.
- **Chain escalating multiplier tiers from a cheap first step** (one-creator-repeated): Sell a cheap first multiplier (1.1x for 9 Robux) so most players buy it, then escalate multiplier and price per tier (1.2x/19, 1.3x/29). In the top-earning game the first step sold about 1,700 times for about 12,000 Robux. Sources: [PineappleDev 2025-09 0:41](https://youtu.be/gXKoxaK6Ufg?t=41), [PineappleDev 2025-09 2:09](https://youtu.be/gXKoxaK6Ufg?t=129), [PineappleDev 2025-09 2:30](https://youtu.be/gXKoxaK6Ufg?t=150), [PineappleDev 2025-09 1:27](https://youtu.be/gXKoxaK6Ufg?t=87), [PineappleDev 2025-09 1:27](https://youtu.be/gXKoxaK6Ufg?t=87). Newest source 2025-09-01.
- **Keep multipliers modest to avoid pay-to-win** (single-mention): Use small steps such as 1.1x so paid multipliers do not make free play pointless. This is the speaker's reasoning, not measured data. Sources: [PineappleDev 2025-09 0:41](https://youtu.be/gXKoxaK6Ufg?t=41). Newest source 2025-09-01.
- **Check ARPU before pricing developer products very cheaply** (one-creator-repeated): Very cheap developer products drag down average revenue per user, per one creator who blames cheap prices for low per-user earnings. Check ARPU before adding very cheap items; the 3-10 Robux reward-style guidance is the floor to test against. Sources: [Arow 2025-07 1:09](https://youtu.be/KsaRtStNO3s?t=69), [Arow 2025-07 1:09](https://youtu.be/KsaRtStNO3s?t=69), [Arow 2025-07 1:09](https://youtu.be/KsaRtStNO3s?t=69). Newest source 2025-07-13.
- **Make the offer feel clearly worth it** (multiple-creators): Players won't buy an offer that seems just okay. Frame the value yourself (e.g. 99 Robux for auto-skip) so the player feels they get the better end. One creator suggests doubling the in-game value to make it more enticing. Sources: [VuukStudios 2026-09 6:47](https://youtu.be/2Q4NqQikzsY?t=407), [VuukStudios 2026-09 6:47](https://youtu.be/2Q4NqQikzsY?t=407), [PineappleDev 2025-09 0:00](https://youtu.be/gXKoxaK6Ufg?t=0). Newest source 2026-09-01.
- **Measure prompt-to-purchase conversion before adding products** (single-mention): One game had about 7,000 Robux prompts and about 100 purchases (about 1%). Investigate prompt placement and offer value first. Another top earner reported about 9% conversion, so compare only like-for-like definitions. Sources: [Seibo 2026-10 4:19](https://youtu.be/Fh0Xku6NwOQ?t=259), [Seibo 2026-10 3:36](https://youtu.be/Fh0Xku6NwOQ?t=216), [Seibo 2026-10 3:36](https://youtu.be/Fh0Xku6NwOQ?t=216), [PineappleDev 2025-09 1:27](https://youtu.be/gXKoxaK6Ufg?t=87). Newest source 2026-10-02.
- **Clamp multi-purchase quantities on the server** (single-mention): For multi-summon style purchases, the server rejects amounts above 10 or below 1. The single summon at default setting cost 200 gems. Validate the requested count server-side before granting. Sources: [ArTheDev 2026-04 9:26](https://youtu.be/Iy9xuT1bpY4?t=566), [ArTheDev 2026-04 0:52](https://youtu.be/Iy9xuT1bpY4?t=52). Newest source 2026-04-18.
- **Cap dependence on any single product** (one-creator-repeated): Track each product's share of developer-product revenue monthly. Rapstrike's top item made ~9,000 units and ~220K Robux, about 40% of income, and dev products were 120K of 150K Robux over 3 days. If one item passes ~40%, build substitutes or adjacent products rather than discounting the hero item. Sources: [Rapstrike GFX 2026-10 1:22](https://youtu.be/6EoiHRT4dAA?t=82), [Rapstrike GFX 2026-10 0:41](https://youtu.be/6EoiHRT4dAA?t=41), [Rapstrike GFX 2026-10 3:24](https://youtu.be/6EoiHRT4dAA?t=204). Newest source 2026-10-25.
- **Launch a low-price hero deal near 30 Robux** (one-creator-repeated): BubuTheDev's 'Amazing Deal' (~30 Robux) sold 155 times for 3,234 Robux, the top developer product. Use a low-price bundle as the volume entry point. It sits above the 3-10 Robux reward band, so package it as a bundle, and track its unit sales. Single-creator, flagged low-advice. Sources: [BubuTheDev 2024-12 2:07](https://youtu.be/82HrjFTdPkU?t=127), [BubuTheDev 2024-12 2:07](https://youtu.be/82HrjFTdPkU?t=127). Newest source 2024-12-03.
- **Add developer products in the first playable build** (one-creator-repeated): PolarBear added dev products to a small game early and earned 257 Robux from 2 purchases among 3 players (purchases of 325 and 43 Robux). Even a tiny player base can produce purchases, so ship at least one cheap product before launch. Sample size is very small. Sources: [PolarBear 2024-02 0:41](https://youtu.be/SNauF9OES7E?t=41), [PolarBear 2024-02 1:23](https://youtu.be/SNauF9OES7E?t=83), [PolarBear 2024-02 2:49](https://youtu.be/tNkQSpq2SXg?t=169). Newest source 2024-02-08.
- **Archive sales data outside the dashboard** (one-creator-repeated): Mulch reports the developer-products dashboard only lets you go back a couple of months. Export sales CSVs regularly and keep your own history so you can compute totals and trends later. Sources: [Mulch 2023-04 5:30](https://youtu.be/6perjdMg3T4?t=330), [Mulch 2023-04 5:30](https://youtu.be/6perjdMg3T4?t=330). Newest source 2023-04-12.
- **Write a monetisation strategy into the design doc** (single-mention): RoyalDev includes a monetisation section in the design doc. His Hidden Anomaly game uses a cheap starter pack, small power purchases, and some larger bat purchases. Plan price tiers and purchase roles before building UI. Sources: [RoyalDev 2026-10 2:03](https://youtu.be/DLqlgL_7XrY?t=123). Newest source 2026-10-10.
- **Plan revenue net of the platform cut** (multiple-creators): Figures imply about a 30% deduction: 3,234 Robux from 155 sales at 30 Robux each is about 21 Robux per sale. Model earnings after tax, not gross Robux. ThePurpleGuy also reports Robux 'after taxes'. Sources: [BubuTheDev 2024-12 2:07](https://youtu.be/82HrjFTdPkU?t=127), [ThePurpleGuy 2026-05 1:22](https://youtu.be/JXg2ACdk_wM?t=82). Newest source 2026-05-13.
- **Verify every pass and product works in-game after edits** (single-mention): LovJak updated developer product prices and UI, replaced gamepass icons, and checked that gamepasses work in-game. Re-test the full purchase-to-reward path after any price, icon, or UI change. Sources: [LovJak 2026-05 4:05](https://youtu.be/FpbZRgRHYjQ?t=245). Newest source 2026-05-01.
- **Verify a new cheap price point grants the intended effect before shipping** (single-mention): PolarBear tested a 15 Robux '+1 rebirth' developer product but did not verify it worked, and marked it low-advice. Confirm the grant in-game (and in ProcessReceipt) before listing any new cheap product. Sources: [PolarBear 2024-03 1:22](https://youtu.be/Q-Wbi1an-ww?t=82), [PolarBear 2024-03 4:26](https://youtu.be/bwMUqu-wWpw?t=266). Newest source 2024-03-25.
- **Consider selling progression items for Robux directly in the shop** (single-mention): LovJak offers Robux purchases directly in the shop (e.g. buying seeds with Robux) as a core monetisation path. Treat it as a single-creator, low-advice route. Validate it with prompt-to-purchase conversion data before making it the main path. Sources: [LovJak 2026-06 6:17](https://youtu.be/ImcICq5XfL8?t=377). Newest source 2026-06-19.
- **Automate bulk developer product creation and ID copying** (single-mention): Creating and naming dozens of developer products by hand, then copying each ID into Studio, is slow and error-prone. The speaker estimates about 2 hours of manual work for roughly 50 products. Script or tool the setup, then sync IDs into the shared product-ID module instead of pasting them one by one. Sources: [Roblox 2026-04 18:37](https://youtu.be/8IcYpOl4Sdk?t=1117), [Roblox 2026-04 18:37](https://youtu.be/8IcYpOl4Sdk?t=1117). Newest source 2026-04-16.
- **Make items giftable where the platform allows** (single-mention): One claimed partnership (Marvel Rivals, not a Roblox game) reported 41% of purchases were gifts from friends. Treat gifting as a possible revenue lever for social items. Confirm Roblox supports gifting for developer products before designing around it. Sources: [Deconstructor of Fun 2026-10 29:59](https://youtu.be/NW4EShVGPYs?t=1799), [Deconstructor of Fun 2026-10 29:59](https://youtu.be/NW4EShVGPYs?t=1799). Newest source 2026-10-26.
- **Offer a one-tap bulk action for stacked items** (single-mention): Let players act on everything they hold at once (example: grow all eggs for 184 Robux) to convert players who have many unopened or ungrown items. Pair with server-side quantity clamping. Price the bulk option so it is clearly cheaper than repeated single buys. Sources: [Mulch 2026-09 9:22](https://youtu.be/U2IjSOyNTB8?t=562). Newest source 2026-09-09.
- **Don't expect hub offers to carry revenue without conversion** (single-mention): Starter-style offers in a hub earned only about 70 Robux total, with spend exceeding earnings (self-reported). Before building more offers, measure prompt-to-purchase conversion and net revenue against promotional cost. Fix conversion first. Sources: [MonarchDev 2026-08 4:06](https://youtu.be/jX3E9OHBeTg?t=246), [MonarchDev 2026-08 4:06](https://youtu.be/jX3E9OHBeTg?t=246), [MonarchDev 2026-08 4:47](https://youtu.be/jX3E9OHBeTg?t=287). Newest source 2026-08-23.
- **Return NotProcessedYet when the player is nil in ProcessReceipt** (single-mention): If the buyer has left the server, do not grant and do not fail. Return Enum.ProductPurchaseDecision.NotProcessedYet so Roblox calls the callback again when the player rejoins, then grant on that later call. Only return PurchaseGranted after the reward is actually given. Sources: [TheDevKing 2019-12 11:36](https://youtu.be/QC2bDZsFiz4?t=696), [TheDevKing 2019-12 8:11](https://youtu.be/QC2bDZsFiz4?t=491). Newest source 2019-12-01.
- **Retarget lapsed players with creator giveaways** (single-mention): Use creator giveaway events aimed at churned and existing players rather than only acquiring new users. One indie report found re-engaged players had about 6x the in-app purchase rate of new creator-acquired users in a lapsed-player giveaway race. Treat as a single self-reported result and test before scaling. Sources: [Deconstructor of Fun 2026-06 23:58](https://youtu.be/2BsMLCk8FEU?t=1438), [Deconstructor of Fun 2026-06 23:58](https://youtu.be/2BsMLCk8FEU?t=1438). Newest source 2026-06-01.
- **Sell stacking server-wide boosts, priced to effect** (one-creator-repeated): A server-wide luck boost benefits everyone in the server and stacks by purchase, adding 1 hour per buy (one creator reported a 1,240x luck tier). Double the price per repeat purchase, and cap or re-price high multipliers, because one creator found the boost too strong at high levels. Sources: [janisjanis01 2024-11 9:47](https://youtu.be/vJekPDaIT30?t=587), [janisjanis01 2024-11 2:22](https://youtu.be/vJekPDaIT30?t=142), [janisjanis01 2024-11 2:22](https://youtu.be/vJekPDaIT30?t=142), [janisjanis01 2024-11 9:47](https://youtu.be/vJekPDaIT30?t=587). Newest source 2024-11-17.
- **Use a reveal animation for mystery packs** (single-mention): A crate-opening animation that reveals the rolled item was paired with a 199 Robux mystery seed pack. Keep disclosed odds and a guaranteed path, as already required for random drops. Sources: [janisjanis01 2025-06 6:18](https://youtu.be/B409dMcW-pw?t=378). Newest source 2025-06-01.
- **Run very short special deals for urgency** (single-mention): One creator used 5-minute special deals to create urgency. Use this for limited-time pushes, and measure conversion per deal rather than assuming it works. Sources: [janisjanis01 2025-06 12:35](https://youtu.be/W9JYImC0FBg?t=755). Newest source 2025-06-15.
- **Price tiered bundles below the à-la-carte sum** (single-mention): Starter, pro and god packs should give clearly better value than buying the same items separately. This is the bundle mechanism that raised payer conversion for one creator. Sources: [janisjanis01 2025-07 13:10](https://youtu.be/pD8fKkzF8O8?t=790). Newest source 2025-07-13.
- **Don't assume cheap boosts alone fix weak conversion** (single-mention): Cheap temporary boost products were tried to lift conversion, but the creator still reported weak monetisation. Test price and placement, and check the prompt-to-purchase rate before adding more cheap items. Sources: [janisjanis01 2025-09 6:16](https://youtu.be/uNLDi_GO2MA?t=376). Newest source 2025-09-21.
- **Use cheap entry currency packs to convert new players, with caution** (single-mention): Example price points: 50 currency for 9 Robux and 1,500 for 99 Robux. Use these only as a test, since the existing file advises caution with plain currency packs. Check ARPU before rolling out widely. Sources: [janisjanis01 2025-06 2:47](https://youtu.be/B409dMcW-pw?t=167). Newest source 2025-06-01.
- **Sell items in soft currency where possible** (single-mention): Charge in in-game currency rather than Robux per item to create distance from real money. This is the most recent advice (2026-04) and conflicts with the existing 'sell progression items for Robux directly' rule, so test both. Sources: [rasdev 2026-04 2:41](https://youtu.be/yFKY2FlwHjE?t=161). Newest source 2026-04-30.
- **Separate sponsored from organic revenue** (single-mention): One creator earned 280 Robux in 72 hours, mostly from sponsored traffic and not the algorithm. Tag revenue by traffic source before judging whether a product or offer works. Sources: [janisjanis01 2025-06 14:29](https://youtu.be/W9JYImC0FBg?t=869). Newest source 2025-06-15.

## Checklist
- [ ] Create products on a published game and copy IDs
- [ ] Implement ProcessReceipt on one server Script; grant before returning PurchaseGranted
- [ ] Save purchase history in DataStores
- [ ] Make a cheap starter pack shown after tutorial/first milestone
- [ ] Add 20-30 products across price tiers
- [ ] Add tiers above your best seller
- [ ] Convert passes like 2x offline earnings to consumables
- [ ] Add HUD shop button, plus button by currency, and in-world prompts
- [ ] Place products at spawn or high-traffic points
- [ ] Show offers at moments of need (can't afford, offline collection)
- [ ] Tag best-value pack and add bonus amounts
- [ ] Give purchase feedback (sound, VFX, inventory confirmation)
- [ ] Add limited/scarce premium items from launch
- [ ] Use event currency for events
- [ ] Limit sales to a few per year
- [ ] Avoid popup stacking
- [ ] List products in Shop with 512x512 icons
- [ ] Segment offers with GetPlayerSegmentsAsync
- [ ] A/B test prices with Experiments
- [ ] Use Configs for flash sales
- [ ] Script prices dynamically before Managed Pricing
- [ ] Offer a free earnable path to sample paid items
- [ ] Review analytics for top sellers and expand them
- [ ] Confirm all grants happen server-side inside ProcessReceipt; no client-side grants.
- [ ] Check hasErrored before allowing any purchase.
- [ ] Save data before granting; if the save fails, return NotProcessedYet.
- [ ] On retries, check the stored PurchaseId and return PurchaseGranted without granting twice.
- [ ] Create a new developer product for each bundle so sales are tracked separately.
- [ ] Replace all placeholder product IDs with dashboard IDs before release.
- [ ] Test data saving in a published test place, not just in Studio.
- [ ] Route all currency changes through one player-manager setter.
- [ ] Add a skip button at obby-style stage gates or rebirth walls.
- [ ] Consider a cheap early boost consumable (e.g. 5 Robux for 1.5x) and test its conversion.
- [ ] Bundle pass-style perks into one developer product; record ownership in a DataStore if the perk can be gifted.
- [ ] Keep purchase prompts small and contextual; avoid large on-screen buttons during play.
- [ ] For random crates, show true odds and include a guaranteed or high-tier option.
- [ ] Test bulk-discount tiers with Experiments before rolling them out.
- [ ] Put high-value consumables inside spin and shop loops where players return.
- [ ] Build one product-ID table and one dispatch path for ProcessReceipt; add new products by adding one handler function.
- [ ] Keep all gamepass and product IDs in one shared ReplicatedStorage module grouped by category.
- [ ] Force DataStore save before granting; on failure deduct the granted amount and return NotProcessedYet.
- [ ] Pass an IdempotencyKey on every purchase and use Client.RequestOnce for retried commands.
- [ ] Verify every new developer product is set to Listed before shipping.
- [ ] Confirm ProcessReceipt is correct and tested before expecting external surfacing.
- [ ] Test a time-limited starter pack (79 Robux-style, about 15-minute window) and track revenue change.
- [ ] Add a donation board as an option for players who won't buy gamepasses.
- [ ] Build escalating multiplier tiers (e.g. 9/19/29 Robux for 1.1x/1.2x/1.3x) with an ordered ID list.
- [ ] Track prompt views versus purchases; if conversion is around 1%, audit prompt placement and offer value.
- [ ] Clamp multi-buy quantities to 1-10 on the server and reject values outside the range.
- [ ] Before launch, simulate free-reward farming to find economy leaks (MonarchDev: 130 free egg hits were worth about $6,500 in 30 seconds before balancing).
- [ ] Check ARPU before lowering developer product prices.
- [ ] Phrase each offer's value explicitly so the player sees it as a good deal.
- [ ] Add at least one cheap developer product before the first public playtest.
- [ ] Track each product's share of total developer-product Robux monthly; flag any item above ~40%.
- [ ] Export sales data (CSV) regularly and store it outside the dashboard.
- [ ] Include a monetisation section in the design doc listing starter, power, and bundle products.
- [ ] Test every new cheap product's in-game effect before listing it.
- [ ] Re-test gamepass and dev-product grants after changing prices, icons, or UI.
- [ ] Model earnings net of the platform cut (about 30% implied) rather than gross Robux.
- [ ] Create one low-price (~30 Robux) hero bundle and track its unit sales.
- [ ] Track prompt-to-purchase conversion before making Robux-only shop items the core path.
- [ ] If you have dozens of developer products, automate creation, naming and ID export from Creator Hub rather than doing it manually (about 2 hours for ~50 products by the speaker's estimate).
- [ ] After any bulk product creation, paste or sync the new IDs into the single shared product-ID module and re-verify each one in-game.
- [ ] Track gifted versus self-bought purchases if gifting is available, to measure the share of gifts.
- [ ] Add a one-tap open-all or grow-all option for players with large stacks of items, priced below single buys.
- [ ] Measure offer earnings against promotional spend before adding more offers.
- [ ] Plan player communication before removing limited items in an update, since players may rush to buy them beforehand.
- [ ] Keep the per-item price of limited bulk items visible so players can compare value (e.g. 50 eggs for 2,800 Robux is about 56 Robux per egg).
- [ ] In ProcessReceipt, if the player is nil, return NotProcessedYet and grant on rejoin (T18406).
- [ ] Verify the buy-to-grant flow with Studio test purchases before going live; Studio test purchases are not charged (N7858, T18408).
- [ ] Plan a creator giveaway for churned or lapsed players and track in-app purchase rate against new creator-acquired users (T18656, N8001).
- [ ] Set a boost duration per purchase (e.g. 1 hour stacking) and test the total stacked effect before shipping.
- [ ] Double the price on each repeat purchase of a stacking boost, and check it is not overpowered at high multipliers.
- [ ] Add a crate-open reveal for mystery packs and show odds next to the purchase.
- [ ] Run 5-minute special deals for urgency and measure conversion per deal.
- [ ] Price starter, pro and god bundles below the sum of their items bought separately.
- [ ] Test cheap boost products by price and placement before concluding they lift conversion.
- [ ] Tag purchase revenue by traffic source (sponsored vs organic) in your analytics.
- [ ] Trial cheap currency packs (e.g. 50 for 9 Robux) on new players and check ARPU before scaling.

## Numbers and benchmarks

| Metric | Value | Context | Sources |
|---|---|---|---|
| Dungeon Quest personalised offer payer conversion lift | +180% day one | Official | [Roblox 2024-09 16:08](https://youtu.be/QC6XWgJRJEM?t=968), [Roblox 2024-09 16:08](https://youtu.be/QC6XWgJRJEM?t=968) |
| Event first-purchase bonus lift | 50% for two weeks | World Zero, official | [Roblox 2024-09 18:49](https://youtu.be/QC6XWgJRJEM?t=1129), [Roblox 2024-09 18:08](https://youtu.be/QC6XWgJRJEM?t=1088) |
| Royal Egg starter pack (Adopt Me) | +6% new-user ARPU and conversion, +2% D7 retention | Took over a month for stat-sig | [Roblox 2025-09 29:10](https://youtu.be/j6OPA95-1O0?t=1750), [Roblox 2025-09 28:29](https://youtu.be/j6OPA95-1O0?t=1709) |
| Driving Empire larger cash packs | +8% revenue per user | Official | [Roblox 2023-09 18:34](https://youtu.be/Z-ZKqBPdl44?t=1114) |
| Sale revenue spike | 2-4x from 25-30% sales | Emergency Response | [Roblox Creators 2023-01 0:00](https://youtu.be/YdplC2WVkWc?t=0), [Roblox Creators 2023-01 0:00](https://youtu.be/YdplC2WVkWc?t=0) |
| Bundle example | 20% off, 5-hour window | Official 2019 | [Roblox DevForum 2019-03](https://devforum.roblox.com/t/monetisation-101-how-to-effectively-generate-revenue-in-your-roblox-game/246902) |
| Starter pack expiry | 24 hours | Indie | [Roblox DevForum 2023-12](https://devforum.roblox.com/t/understand-the-roblox-algorithm/2772921), [Roblox DevForum 2023-12](https://devforum.roblox.com/t/understand-the-roblox-algorithm/2772921) |
| Timing of first offer | 20-60 minutes in | Not in first 30 seconds | [Roblox DevForum 2019-03](https://devforum.roblox.com/t/monetisation-101-how-to-effectively-generate-revenue-in-your-roblox-game/246902), [TheDevKing 2020-05 9:57](https://youtu.be/Zqz_gclwM0M?t=597) |
| Reward value | 3-10 Robux | Official docs | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/promotion/rewarded-video-ads), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) |
| Rewarded item cap | ~100x earnings per ad view | Heuristic | [Roblox Creators 2025-08 22:35](https://youtu.be/7AtvvUxvCaU?t=1355), [Roblox Creators 2025-08 22:35](https://youtu.be/7AtvvUxvCaU?t=1355) |
| Currency ratio | ~1 currency : 0.15 Robux | Creatures of Sonaria | [Roblox Creators 2023-01 0:00](https://youtu.be/YdplC2WVkWc?t=0) |
| Rotating shop cycle | 6 or 12 hours, price rises per purchase | Currency sink | [Roblox Creators 2023-01 0:00](https://youtu.be/YdplC2WVkWc?t=0) |
| CallMeDogey dev product Robux | 1.9M vs 841k passes | Self-reported | [CallMeDogey 2025-01 8:08](https://youtu.be/USJC5l_wpuY?t=488), [CallMeDogey 2025-01 10:14](https://youtu.be/USJC5l_wpuY?t=614) |
| CallMeDogey top product | 10,000 Robux, 9 buyers | Self-reported | [CallMeDogey 2025-01 10:14](https://youtu.be/USJC5l_wpuY?t=614) |
| Energy Incremental top product | 10,000 Robux sold 640 times, ~500k Robux | Self-reported | [1_Bruce 2025-12 7:02](https://youtu.be/wKI3PBO3bB0?t=422) |
| 1_Bruce total revenue | ~23-24M Robux in about a month; peak 1.3M/day | Self-reported, some investment | [1_Bruce 2026-03 0:00](https://youtu.be/zgq6L4ZzCHs?t=0), [1_Bruce 2026-03 2:48](https://youtu.be/zgq6L4ZzCHs?t=168) |
| Product counts | 59 (MoseyTube built); 20-30 recommended | Self-reported | [MoseyTube 2026-04 3:25](https://youtu.be/sFr7htxsnR4?t=205), [MoseyTube 2026-06 5:13](https://youtu.be/Kh_XKYw8ocU?t=313), [MoseyTube 2026-06 5:13](https://youtu.be/Kh_XKYw8ocU?t=313) |
| Tizzy offline double price | 19 Robux | Self-reported | [Tizzy 2026-06 3:27](https://youtu.be/HFcegpPPvpI?t=207), [Tizzy 2026-06 3:27](https://youtu.be/HFcegpPPvpI?t=207) |
| 24h base lock | top seller in ~2 days | Self-reported | [Tizzy 2026-06 4:42](https://youtu.be/zoz3PSMqets?t=282) |
| Cash-shop redirect frequency | 3-5 per session | Self-reported | [Tizzy 2026-06 8:56](https://youtu.be/zoz3PSMqets?t=536) |
| Limited locust | 1,000 Robux, 1,000 stock | Self-reported | [Tizzy 2026-10 14:36](https://youtu.be/_JyiKfNNqls?t=876) |
| Slapper prices | 90/200/450 Robux | Steal a Superstar | [MoseyTube 2026-08 4:26](https://youtu.be/xIBc5He_sy4?t=266) |
| kra_DeZ earnings | max 97,000/day; ~1.39M over 56 days; Nuke All 19,349 in 90 days | Self-reported, low-advice | [kra_DeZ 2026-09 3:55](https://youtu.be/ZradA-cygP0?t=235), [kra_DeZ 2026-09 4:36](https://youtu.be/ZradA-cygP0?t=276), [kra_DeZ 2026-09 7:55](https://youtu.be/ZradA-cygP0?t=475) |
| BrawlDev pay-per-jump | 5 Robux/jump; 7,614 Robux total | Low-advice test | [BrawlDev 2025-11 0:00](https://youtu.be/YGmO7BXSwVg?t=0), [BrawlDev 2025-11 7:32](https://youtu.be/YGmO7BXSwVg?t=452) |
| Icon size | 512x512 max | Official | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/developer-products) |
| RecommendTopProductsAsync | up to 50 items | Official | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/developer-products) |
| Analytics showcase | up to 8 top items | Official | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/developer-products) |
| Example currency grant / speed boost | 100 cash; speed 50 for 5s then 16 | AlvinBlox tutorial | [AlvinBlox 2024-06 11:22](https://youtu.be/5YNFRCD0pd0?t=682), [AlvinBlox 2024-06 13:16](https://youtu.be/5YNFRCD0pd0?t=796) |
| Limited supply example | 30,000 buyers | Adopt Me | [Roblox 2025-09 26:35](https://youtu.be/MJ-zYfL10Ew?t=1595) |
| Double XP booster example | $5 | Illustrative | [Roblox 2026-10 14:32](https://youtu.be/qLP05zvMsW0?t=872) |
| Crate price (single) | 349 Robux | Single sand crate in one game, June 2025; game-specific and dated. | [Bemmy 2025-06 0:00](https://youtu.be/-Z0C5YJtnqY?t=0), [Bemmy 2025-06 0:00](https://youtu.be/-Z0C5YJtnqY?t=0) |
| Bulk crate price | ~174 Robux per crate (about 50% off single) | Bulk purchase price shown by Bemmy; anecdote. | [Bemmy 2025-06 5:06](https://youtu.be/-Z0C5YJtnqY?t=306), [Bemmy 2025-06 0:00](https://youtu.be/-Z0C5YJtnqY?t=0) |
| Exotic drop chance per crate | 1.78% | Odds of the target exotic from one crate; a low-odds framing to disclose clearly. | [Bemmy 2025-06 0:00](https://youtu.be/-Z0C5YJtnqY?t=0) |
| Secret-tier chance per crate | 20% | Secret-tier share within the crate, per video text. | [Bemmy 2025-06 1:08](https://youtu.be/-Z0C5YJtnqY?t=68) |
| High-tier crate price | 499 Robux | Guaranteed-mutation and high-tier offer, Sept 2025. | [janisjanis01 2025-09 8:44](https://youtu.be/YVKHlrlWn-k?t=524) |
| Cash boost price and effect | 5 Robux for 1.5x cash (20% more cash in earlier version) | janisjanis01, May 2026; one creator's offer. | [janisjanis01 2026-05 8:37](https://youtu.be/BLOToGi2Qt4?t=517), [janisjanis01 2025-11 10:16](https://youtu.be/QnAoCsC-4ig?t=616), [janisjanis01 2026-05 8:37](https://youtu.be/BLOToGi2Qt4?t=517) |
| Rainbow ore price | 199 Robux | Single item price, May 2025; not a benchmark for other games. | [RoDev 2025-05 6:36](https://youtu.be/Gw2FwndwnOg?t=396) |
| Top product (500 coins) revenue | 200K Robux | Brain Rot Tag top product, May 2026; cumulative figure as reported. | [Yann 2026-05 2:44](https://youtu.be/dbNA3K8lt2w?t=164) |
| Nuke troll product | 80K Robux at 199 Robux | Brain Rot Tag, May 2026. | [Yann 2026-05 2:44](https://youtu.be/dbNA3K8lt2w?t=164) |
| Starter pack creator spend | 750 Robux | Creator's own purchases shown while promoting starter packs; not a conversion benchmark. | [janisjanis01 2025-07 7:18](https://youtu.be/Sgs36l6K5EU?t=438) |
| Robux earned in 72 hours | 109,000 Robux (~$400) | bubDEV, Oct 2025; self-reported. | [bubDEV 2025-10 7:35](https://youtu.be/N-u2gI4DUyw?t=455) |
| Developer product revenue total | 732,550 Robux (~$2,778) | bubDEV, Oct 2025; implies about $0.0037–0.0038 per Robux (derived from the creator's own conversions). | [bubDEV 2025-10 8:58](https://youtu.be/N-u2gI4DUyw?t=538) |
| Cumulative spend (crate example) | Over 10,000 Robux | Bemmy's own spend on sand crates; shows how heavy repeat-buy spending can be. | [Bemmy 2025-06 9:49](https://youtu.be/-Z0C5YJtnqY?t=589) |
| Low starter pack price tested | 9 Robux | Yann pushed it on screen but noted it still needs testing. | [Yann 2026-07 3:34](https://youtu.be/Bw2ty2T46z4?t=214) |
| High starter bundle example | 4,900 Robux | RoDev stream; conversion not measured. | [RoDev 2025-05 17:06](https://youtu.be/Gw2FwndwnOg?t=1026) |
| Starter pack price and window | 79 Robux, 15-minute window | 1Coal, March 2024; self-reported. | [1Coal 2024-03 2:25](https://youtu.be/gWNOANEPYLY?t=145), [1Coal 2024-03 2:25](https://youtu.be/gWNOANEPYLY?t=145) |
| Revenue change after adding starter pack | roughly 2x to 3x | Self-reported; single game. | [1Coal 2024-03 2:25](https://youtu.be/gWNOANEPYLY?t=145), [1Coal 2024-03 2:25](https://youtu.be/gWNOANEPYLY?t=145) |
| Donation board developer-product Robux | 216 Robux | Idle Dice, Sept 2024; plus 41 Robux premium payouts. | [PineappleDev 2024-09 2:25](https://youtu.be/UBs1bebPu0s?t=145), [PineappleDev 2024-09 3:52](https://youtu.be/UBs1bebPu0s?t=232) |
| Multiplier tier prices | 9 Robux (1.1x), 19 Robux (1.2x), 29 Robux (1.3x) | PineappleDev cascading chain, Sept 2025. | [PineappleDev 2025-09 0:00](https://youtu.be/gXKoxaK6Ufg?t=0), [PineappleDev 2025-09 0:41](https://youtu.be/gXKoxaK6Ufg?t=41) |
| Top cascade tier sales | about 1,700 sales for about 12,000 Robux | Top-selling tier in the chain. | [PineappleDev 2025-09 1:27](https://youtu.be/gXKoxaK6Ufg?t=87) |
| Second cascade tier sales | about 500 sales for 8,000 Robux | Second tier. | [PineappleDev 2025-09 2:09](https://youtu.be/gXKoxaK6Ufg?t=129) |
| Third cascade tier sales | about 200 sales for 5,000 Robux | Third tier. | [PineappleDev 2025-09 2:09](https://youtu.be/gXKoxaK6Ufg?t=129) |
| Conversion on top earning game | about 9% | PineappleDev; stated as roughly 9% on the speaker's top game. | [PineappleDev 2025-09 1:27](https://youtu.be/gXKoxaK6Ufg?t=87) |
| Robux purchase conversion (prompt to buy) | about 1% (about 7,000 saw the prompt, about 100 bought) | Seibo, Oct 2026; self-reported. | [Seibo 2026-10 3:36](https://youtu.be/Fh0Xku6NwOQ?t=216), [Seibo 2026-10 3:36](https://youtu.be/Fh0Xku6NwOQ?t=216), [Seibo 2026-10 4:19](https://youtu.be/Fh0Xku6NwOQ?t=259) |
| Developer product vs gamepass Robux | about 31,000 dev product Robux vs about 23,000 gamepass Robux | Matt The Method game, Feb 2026; developer products were the largest source. | [Matt The Method 2026-02 1:12](https://youtu.be/TEENlwjuKWI?t=72), [Matt The Method 2026-02 1:12](https://youtu.be/TEENlwjuKWI?t=72) |
| Peak CCU for that game | about 30 | Revenue was earned at low concurrency; now zero after updates stopped. | [Matt The Method 2026-02 0:00](https://youtu.be/TEENlwjuKWI?t=0) |
| Developer product Robux, last 90 days, no ads | about 300,000 Robux | Arow, July 2025; self-reported. | [Arow 2025-07 1:09](https://youtu.be/KsaRtStNO3s?t=69) |
| Best-selling developer product | 500 Robux poop size double | Perstile, May 2025; high-ticket novelty outsold cheap items in this game. | [Perstile 2025-05 1:57](https://youtu.be/ET3fRqaFmFc?t=117) |
| Summon price | 200 gems single summon at default; 50 gems at price tier 1 (example) | ArTheDev, April 2026; demo started with 600 gems. | [ArTheDev 2026-04 0:52](https://youtu.be/Iy9xuT1bpY4?t=52) |
| Multi-summon quantity limit | min 1, max 10 per request | Server rejects amounts outside the range. | [ArTheDev 2026-04 9:26](https://youtu.be/Iy9xuT1bpY4?t=566) |
| Free egg hits before balancing | 130 hits, about $6,500 in 30 seconds | MonarchDev, Oct 2026; economy leak example. | [MonarchDev 2026-10 1:32](https://youtu.be/bbCmt98O9MA?t=92) |
| Robux from sales after one week | 5,125 Robux | MonarchDev, Oct 2026; self-reported. | [MonarchDev 2026-10 12:10](https://youtu.be/bbCmt98O9MA?t=730) |
| Test product price | 100 Robux | Demo coin developer product test, June 2023. | [Suphi Kaner 2023-06 48:20](https://youtu.be/UAdE8-AfuMo?t=2900) |
| Top developer product (low-price deal) | ~30 Robux, 155 sales, 3,234 Robux earned | BubuTheDev, 2024-12; self-reported; ~21 Robux net per sale | [BubuTheDev 2024-12 2:07](https://youtu.be/82HrjFTdPkU?t=127), [BubuTheDev 2024-12 2:07](https://youtu.be/82HrjFTdPkU?t=127) |
| Single item share of income | ~40% | Rapstrike GFX, 2026-10; top item ~9,000 units, ~220K Robux, ~$1.2K | [Rapstrike GFX 2026-10 3:24](https://youtu.be/6EoiHRT4dAA?t=204), [Rapstrike GFX 2026-10 1:22](https://youtu.be/6EoiHRT4dAA?t=82) |
| Dev product share of 3-day revenue | 120K of 150K Robux (~80%) | Rapstrike GFX, 2026-10; gamepasses were 30K | [Rapstrike GFX 2026-10 0:41](https://youtu.be/6EoiHRT4dAA?t=41) |
| Early small-game dev product sales | 257 Robux from 2 sales; 2 of 3 players purchased | PolarBear, 2024-02; tiny sample, self-reported | [PolarBear 2024-02 1:23](https://youtu.be/SNauF9OES7E?t=83), [PolarBear 2024-02 2:49](https://youtu.be/tNkQSpq2SXg?t=169) |
| Rebirth-style 15 Robux product | ~80 purchases, ~700 Robux gross, ~450-500 net attributed | PolarBear, 2024-03; sponsor run; low-advice, effect not verified | [PolarBear 2024-03 4:26](https://youtu.be/bwMUqu-wWpw?t=266), [PolarBear 2024-03 1:22](https://youtu.be/Q-Wbi1an-ww?t=82) |
| BubuTheDev all-time dev product revenue | 2,500 Robux in 72h; 5,500 all time | 2024-12; self-reported | [BubuTheDev 2024-12 0:47](https://youtu.be/82HrjFTdPkU?t=47), [BubuTheDev 2024-12 2:07](https://youtu.be/82HrjFTdPkU?t=127) |
| LovJak dev product revenue | 3,700 Robux over 28 days | 2026-07; self-reported | [LovJak 2026-07 7:29](https://youtu.be/Y602HH_KdOc?t=449) |
| Mulch dev product revenue, 4 days gross | ~8,021 Robux | 2021-09; daily sales summed | [Mulch 2021-09 7:56](https://youtu.be/yG44d_Xnbwg?t=476) |
| Mulch dev product estimate (CSV-based) | 10,000-15,000 Robux, 15,000 used in final total | 2023-04 | [Mulch 2023-04 5:30](https://youtu.be/6perjdMg3T4?t=330) |
| Mulch dev product revenue (skip-stage and donation products) | ~3,000 Robux | 2024-06; not comparable to earlier windows | [Mulch 2024-06 2:05](https://youtu.be/pqCXX06vlDw?t=125), [Mulch 2024-06 1:23](https://youtu.be/pqCXX06vlDw?t=83) |
| Implied Robux-to-USD (Rapstrike's own calc) | ~$0.0038 per Robux ($570 / 150K) | Derived from creator's stated figures; the top-item figure ($1.2K for 220K Robux) implies a different rate, so verify before use | [Rapstrike GFX 2026-10 0:41](https://youtu.be/6EoiHRT4dAA?t=41) |
| Net per sale after ~30% cut | ~21 Robux for a 30 Robux product | Derived from BubuTheDev totals; inference, not official | [BubuTheDev 2024-12 2:07](https://youtu.be/82HrjFTdPkU?t=127) |
| Developer products in one tracked game | 21 | Single self-reported count from RoTrends (tracker), indie, low-advice, dated 2026-10. The game, genre, player count and revenue are not stated, so it is a catalogue-size data point, not a recommended target. | [RoTrends (tracker) 2026-10](https://www.rotrends.com/game/6739698191/BUTCHER-x-Violence-District) |
| Manual developer product setup/update time | ~2 hours for ~50 products | Speaker's example of Creator Hub busywork (creating, naming, copying IDs into Studio). Illustrative, not a measured benchmark. | [Roblox 2026-04 18:37](https://youtu.be/8IcYpOl4Sdk?t=1117) |
| Total Robux earned from hub offers | ~70 Robux | MonarchDev, self-reported, Aug 2026; spend exceeded earnings. | [MonarchDev 2026-08 4:06](https://youtu.be/jX3E9OHBeTg?t=246), [MonarchDev 2026-08 4:06](https://youtu.be/jX3E9OHBeTg?t=246) |
| Gift share of purchases | 41% | Claimed by Deconstructor of Fun for Marvel Rivals (not Roblox), Oct 2026. | [Deconstructor of Fun 2026-10 29:59](https://youtu.be/NW4EShVGPYs?t=1799), [Deconstructor of Fun 2026-10 29:59](https://youtu.be/NW4EShVGPYs?t=1799) |
| One-tap bulk action price | 184 Robux (grow all eggs) | Mulch, self-reported, Sep 2026; example bulk price for many eggs. | [Mulch 2026-09 9:22](https://youtu.be/U2IjSOyNTB8?t=562) |
| Limited monster egg bundle | 50 eggs for 2,800 Robux (~56 Robux per egg) | Mulch, Sep 2026; bought before an update removed limited eggs. | [Mulch 2026-09 1:59](https://youtu.be/WYODms_JMRA?t=119) |
| Treadmill upgrade price | 1,000 Robux per step | Mulch, Sep 2026; upgrade button in Steal an Egg. | [Mulch 2026-09 0:00](https://youtu.be/WYODms_JMRA?t=0) |
| Single high-value opening purchase | 1,000 Robux (black hole goat) | Creator's own spend in Aug 2026 video; an anecdote, not a benchmark. | [Mulch 2026-08 0:00](https://youtu.be/heoowJH9hso?t=0) |
| In-app purchase rate of re-engaged (lapsed) users vs new creator-acquired users in creator giveaway | ~6x higher | Match Masters giveaway race for lapsed players; single indie self-reported result (Deconstructor of Fun, 2026-06). Sample size not given. | [Deconstructor of Fun 2026-06 23:58](https://youtu.be/2BsMLCk8FEU?t=1438), [Deconstructor of Fun 2026-06 23:58](https://youtu.be/2BsMLCk8FEU?t=1438) |
| Studio test purchase charge | Not charged | Studio prompt states the account will not be charged; use for flow testing (TheDevKing, 2019-12). | [TheDevKing 2019-12 8:11](https://youtu.be/QC2bDZsFiz4?t=491) |
| Example dev product price in tutorial | 1000 Robux | Illustrative tutorial price for a sword dev product, not a pricing benchmark (TheDevKing, 2019-12). | [TheDevKing 2019-12 1:12](https://youtu.be/QC2bDZsFiz4?t=72) |
| Server luck boost multiplier tier | 1,240x | Tier mentioned while hatching in a server; creator felt high multipliers were too strong. | [janisjanis01 2024-11 2:22](https://youtu.be/vJekPDaIT30?t=142) |
| Server boost duration | 1 hour per purchase, stacking | Buying again adds 1 hour. | [janisjanis01 2024-11 9:47](https://youtu.be/vJekPDaIT30?t=587) |
| Boost price scaling | Price doubles per purchase | Server-wide stacking boost. | [janisjanis01 2024-11 9:47](https://youtu.be/vJekPDaIT30?t=587) |
| Cheap currency pack examples | 50 currency for 9 Robux; 1,500 for 99 Robux | Entry packs to convert new players. | [janisjanis01 2025-06 2:47](https://youtu.be/B409dMcW-pw?t=167) |
| Mystery seed pack price | 199 Robux | With crate-opening reveal. | [janisjanis01 2025-06 6:18](https://youtu.be/B409dMcW-pw?t=378) |
| Special deal duration | 5 minutes | Urgency-based limited-time deal. | [janisjanis01 2025-06 12:35](https://youtu.be/W9JYImC0FBg?t=755) |
| Early revenue, sponsored traffic | 280 Robux in 72 hours | Mostly sponsored traffic, not algorithm; indie self-reported. | [janisjanis01 2025-06 14:29](https://youtu.be/W9JYImC0FBg?t=869) |
| In-game currency price of a Jelly Hoverboard skin (soft-currency cosmetic) | 50 million | Shown in the presents shop, priced in in-game currency rather than Robux. Self-reported indie example of a high soft-currency price on a cosmetic. Not a developer product price; no Robux equivalent or sales data is given. | [Mulch 2024-11 5:29](https://youtu.be/SLrIagp7uHE?t=329) |

## Where creators agree
- Developer products beat game passes for repeatable value (AlvinBlox, TheDevKing, MoseyTube, Tizzy, kra_DeZ, CallMeDogey, 1_Bruce, Roblox official).
- First purchase is the key conversion step (TheDevKing, Roblox DevForum, Roblox).
- Cheap starter packs timed after a milestone or tutorial (Roblox, TheDevKing, DevForum).
- Show offers at moments of need and in multiple places (Tizzy, MoseyTube, TheDevKing).
- Use scarcity and limited items (Roblox, Tizzy, 1_Bruce).
- Developer products are the right vehicle for repeatable consumables and pass-style perks (T5684, T6874, T6376).
- Starter packs are a strong seller and deserve prominent placement (T6269, T6514, N2610).
- Cheap boosts and consumables help conversion (T6350, T6501).
- Grants must happen server-side inside ProcessReceipt (T7474, T5686, T5687).
- Developer products are the main revenue source versus gamepasses across several creators' games (Matt The Method, Quez, Arow, PineappleDev, Generalist Programmer, VuukStudios).
- Repeatable purchases belong in developer products; one-time unlocks belong in gamepasses (VuukStudios T12287, ByteBlox T12468).
- Monetising Roblox games is hard and needs deliberate offer design (PineappleDev Q1336, T12936).
- Offer value perception drives purchases; players must feel they get a good deal (VuukStudios T13769, Q1427).
- Developer products generate most of the Robux in these indie games (Rapstrike, LovJak, Mulch, PolarBear).
- Developer products can earn in small games early, not only at scale (PolarBear, 2024; Mulch, 2021).
- Low-price bundles drive volume (BubuTheDev with the ~30 Robux deal; Rapstrike with a single high-volume item).

## Where creators disagree
- **Selling currency packs**
  - TheDevKing, Roblox Creators, Roblox DevForum: sell spendable currency, tiered with best-value tags.
  - Alex Builds Games: currency packs are weak (D tier); sell direct items instead.
  - Tizzy: selling cash packs early likely hurt his economy.
- **Number of products**
  - MoseyTube: 20-30 recommended, though he built 59 and admits it may be excessive.
  - Roblox official: offer multiple price points without a specific count.
- **When to open the shop on failed purchase**
  - TheDevKing: prompt the exact currency amount immediately.
  - Tizzy: show the error first, open the shop on the third attempt.
- **Timing of launching premium/whale products**
  - Tizzy: launch limited and whale products from the start.
  - Roblox official: escalate prices gradually at milestones and keep first offers small.
- **Starter pack price point**
  - Yann (T6662) pushed a 9-Robux starter pack on screen but says it still needs testing.
  - RoDev (T6193) showed a 4,900-Robux starter bundle as a plausible starter buy; conversion not measured.
- **Limited-time gameplay boosts versus the existing rule to monetise convenience, not basic movement**
  - janisjanis01 (T6626, low-advice) says limited-time speed skins with real boosts beat cosmetics.
  - Existing knowledge-file rule says monetise convenience, not basic movement. Present both and test before selling movement boosts.
- **Pass vs consumable for one-time perks**
  - ByteBlox (T12468): gamepasses for one-time unlocks, products for repeat buys.
  - PineappleDev (T12625) and Quez (T12804): sell paid revives, potions and seeds as developer products, which the existing file's pass-to-consumable rule already supports.
- **Breadth of the store**
  - Generalist Programmer (T13554): sell only a few products and passes; don't overload the store.
  - Existing guidance: offer many price tiers and many shop entry points (not from these sources).
- **Price floor for developer products**
  - Arow (T12835, Q1325): very cheap developer products drag down ARPU.
  - Existing guidance: offer reward-style items at 3-10 Robux value.
- **Conversion benchmark**
  - Seibo (T13866, N5484): about 1% of prompt views became purchases.
  - PineappleDev (N4967): about 9% on a top earning game. Definitions and game types differ, so do not compare directly.
- **Price ceiling for novelty items**
  - Perstile (N4882): the best-seller was a 500-Robux novelty item.
  - Existing guidance: sell cheap novelty items. Test both; the sources conflict.
- **Whether gamepasses are worth keeping alongside developer products**
  - PolarBear (Q1519, 2024-03): the game has no gamepasses, only developer products, and the pass system is 'kind of broken'; he relies on dev products alone.
  - LovJak (T16471, 2026-05) and Rapstrike GFX (N6707, 2026-10): keep gamepasses and fix them (icons, in-game function); gamepasses bring in a real share of income (Rapstrike: 30K of 150K Robux).
- **Selling progression items for Robux directly vs in-game currency**
  - rasdev (T18936, 2026-04, newest): sell purchases in in-game currency rather than charging Robux per item, to create distance from real money.
  - Existing file rule: consider selling progression items for Robux directly in the shop.
- **Cheap plain currency packs**
  - janisjanis01 (T18872, 2025-06): offer cheap packs (50 for 9 Robux, 1,500 for 99 Robux) to convert new players.
  - Existing file rule: be cautious with plain currency packs.

## Date context (what may be outdated)
- 2018-2021 advice (AlvinBlox, DevForum, TheDevKing) is foundational; the 2023-2025 official talks add data and segmentation, and the 2026 docs add ProcessReceipt requirements, Shop listing, recommendation APIs, Experiments and Configs.
- Docs say listing in Shop and correct ProcessReceipt are needed for external surfacing; prefer these over older tutorials that may use PromptProductPurchaseFinished.
- Indie revenue figures from 2025-2026 are self-reported and unverified.
- Older 2019 first-offer pricing advice ('cup of coffee') remains consistent with the 2025 starter pack guidance.
- Official ProcessReceipt guidance (T7474, T7475, T9844 to T9846; Oct 2026) is current. Prefer it over the 2022 indie notes (T5686 to T5688), which lack the save-before-grant and hasErrored checks.
- Developer product setup in Game Settings > Monetization (T5684, 2022) is older; the Creator Dashboard > Developer Products path with addItemAsync (T10030, 2026) is newer.
- Crate and price figures come from June 2025 (Bemmy), Sept 2025 (janisjanis01), Oct 2025 (bubDEV) and May 2026 (Yann, janisjanis01). Treat them as dated, game-specific benchmarks.
- Limited-time boost and random-crate tactics are 2025 to 2026 anecdotes with no published conversion data.
- DevForum (T13456, June 2026): new developer products default to Not Listed; the Listed-status review deadline was July 7, 2026. That deadline has passed as of 2026-10-29, so verify each product's status now rather than assuming it was handled.
- DevForum (T13457, June 2026): correct ProcessReceipt is required for external surfacing eligibility, a 2026 platform-level condition.
- IdempotencyKey and Client.RequestOnce (T13585, July 2026) are the newest request-safety guidance; the 2023 DataStore save pattern (T11724) is still valid but predates it.
- Most revenue figures are 2024-2025 and self-reported; prices and conversion benchmarks drift. The 79-Robux starter pack figure is from March 2024.
- Several games cited (e.g. the Matt The Method game, peak 30 CCU) have stopped updating; their revenue is historical, not current.
- Newest items are 2026-10 (Rapstrike GFX, RoyalDev); these reflect current advice. Prefer them over 2020-2024 items where they conflict.
- Q1511 (Mulch, 2023) says the dashboard only shows a couple of months of developer-product history. This may have changed; verify the current window before relying on it.
- Q1519 (PolarBear, 2024-03) says gamepasses were 'kind of broken'. Later 2026 creators still build and fix gamepasses, so treat the 2024 claim as likely outdated and unverified.
- Mulch's revenue figures (8,021 in 4 days in 2021; 10-15K estimate in 2023; ~3,000 in 2024) cover different windows and methods and are not directly comparable.
- All indie revenue figures are self-reported and gross or net is often unstated; check the basis before comparing.
- N7294 (2026-10) is the most recent item; it is a count only and does not change any existing advice on dated platform behaviour.
- Source is dated 2026-04 and comes from Roblox [OFFICIAL] content. As of 2026-11, check that the automation method still matches current Creator Hub tooling and any API changes before relying on it.
- Items in this batch are dated Aug to Oct 2026; prices and tiers are creator-specific snapshots and may have changed.
- Sep 2026: limited monster eggs were removed by an update (N7646), so limited-item availability should be checked against the current game before citing.
- The 41% gift share (Oct 2026) comes from Marvel Rivals, not Roblox; do not generalise it to Roblox without Roblox-specific evidence.
- All figures here are indie self-reported; no official Roblox source in this batch.
- TheDevKing material is from 2019-12 and may predate current Creator Dashboard menus and prompt wording; re-verify paths such as Configure > Developer Products before relying on them.
- The ~6x re-engagement figure is from 2026-06, the most recent input in this batch, and is a single self-reported case.
- New items span 2024-11 to 2026-04; all are indie, self-reported, and some are tagged low-advice. Today is 2026-11, so prices, boost values and deal behaviour may have changed.
- On conflicts, prefer the more recent advice: the 2026-04 soft-currency point (T18936) and the 2025-09 finding that cheap boosts did not fix conversion (T18917) take precedence over the 2024-11 boost enthusiasm (T18823, N8084).
- Verify current Robux price rules and any platform policy on server-wide boosts or random-item disclosure before shipping.
- N8194 is dated 2024-11, so the price reflects that period and may have changed by 2026-11.

## Instructions for an agent using this file
- If a product is repeatable (currency, boost, potion, hint), then make it a developer product, not a game pass.
- If designing a perk like 2x offline earnings, then sell it as a consumable prompt at collection time.
- If a player fails to afford an item, then show the error first and offer the shop/exact amount, opening the shop directly on repeat attempts.
- If adding a starter pack, then show it after the tutorial or first milestone with a 24h timer and low price, and A/B test variables.
- If writing purchase code, then use a single server ProcessReceipt that returns PurchaseGranted only after granting; never rely on PromptProductPurchaseFinished.
- If building the shop, then include 20-30 tiered products, best-value tag, higher tiers above the best seller and several entry points.
- If planning sales, then keep them to a few per year, after confirming healthy metrics.
- If the economy has hard currency, then keep it scarce and use event-specific currency for events.
- If asked for revenue claims, then label indie figures as self-reported, unverified.
- If enabling Managed Pricing or Shop listing, then script prices dynamically, add icons and fix ProcessReceipt issues first.
- If the task involves ProcessReceipt or purchase grants, follow the official rules (T7474, T9844 to T9846) over older indie guidance.
- If a user asks for a specific price, cite the creator's price as an example only and recommend an Experiments A/B test rather than copying it.
- If a random or crate product is proposed, require disclosed odds and a guaranteed or high-tier alternative; flag misleading 'secret' framing.
- Treat [low-advice] items (T6230, T6231, T6308, T6626, T6515) as anecdote; do not present their numbers as benchmarks.
- When boost tips conflict with the convenience-not-movement rule, present both sides and recommend testing.
- Never recommend large persistent purchase buttons during play (T6457).
- Omit N2956 (no data provided).
- Always create a new product per bundle for tracking (T7808).
- If a player's receipt is granted but the save fails, deduct the granted amount and return NotProcessedYet (T11724).
- If adding a new developer product, add one handler to the product-ID table rather than a new branch (T11725).
- If creating or republishing a developer product, confirm its Listed status before assuming it shows in the Shop (T13456).
- If a purchase can be retried by the network, attach an IdempotencyKey and use Client.RequestOnce (T13585).
- If a multi-buy request arrives, reject quantities below 1 or above 10 on the server (N5149).
- If prompt-to-purchase conversion is around 1%, audit prompt placement and offer value before adding more products (T13866).
- If designing a multiplier chain, use small steps (1.1x) and escalate price per tier (N4971, T12935).
- If considering very cheap developer products, check ARPU first (T12835).
- Do not cite the 2024-2025 figures as current benchmarks without noting the date and self-reported source.
- If one developer product exceeds ~40% of dev-product revenue, add substitutes or adjacent bundles rather than discounting it.
- If the game is early or small, add at least one cheap developer product before launch to test purchase behaviour.
- When estimating earnings, model net of the ~30% platform cut and label the basis (gross vs net).
- Before listing a new cheap price point, verify in-game that its grant works, including ProcessReceipt behaviour.
- Keep sales exports outside the dashboard so history is not lost.
- Treat all indie figures as self-reported. Use them as directional signal, not benchmarks, unless multiple sources agree.
- Prefer 2026 items over 2020-2024 items when they conflict, and note the conflict in the output.
- When citing N7294, label it as a single indie, self-reported count from a tracker, not as a benchmark for what a healthy catalogue looks like.
- Do not add a rule or target for product count based on N7294 alone; treat it as context only.
- If the user manages many developer products and describes manual creation or ID copying, suggest automating setup and ID export before adding more products.
- Keep product IDs in one shared module even when they are generated automatically, so ProcessReceipt routing still uses a single ID table.
- If hub or offer revenue stays near zero after a test period, do not add more offer types; first diagnose prompt-to-purchase conversion.
- If asked whether developer products can be gifted on Roblox, state that these sources do not cover gifting and that it must be verified in official docs.
- Cite all figures from this batch as indie self-reported, not as platform benchmarks.
- Do not treat a creator's personal single purchase (e.g. 1,000 Robux goat) as a market benchmark.
- When recommending a bulk action, also enforce quantity limits server-side in ProcessReceipt-linked grants.
- When a limited item is about to be removed, advise planning communication, since sales spike before removal.
- If ProcessReceipt finds the player is nil, return NotProcessedYet and do not grant; grant only on the later callback after rejoin.
- Only return PurchaseGranted after the reward has been applied and saved.
- When planning re-engagement, target churned and existing players, and measure in-app purchase rate against new creator-acquired users before scaling.
- Treat the 6x re-engagement figure as a self-reported single case; validate with your own test before budgeting around it.
- Use Studio test purchases (not charged) to validate the grant flow, then confirm in the live game before launch.
- Do not cite the 2019 tutorial prices as current pricing guidance.
- If the user asks about server-wide or stacking boosts, cite that the effect must be priced to scale and capped at high multipliers (T18838, N8084).
- If choosing between Robux-per-item and in-game currency for progression items, present both (T18936 vs existing rule) and recommend A/B testing rather than picking one.
- If recommending cheap currency packs, pair the recommendation with an ARPU check and a caution note (T18872).
- If judging early revenue, separate sponsored traffic from organic before drawing conclusions (N8111).
- Treat all items here as indie self-reported; do not present them as platform ground truth.
- Do not assume cheap boosts alone raise conversion; check placement and prompt-to-purchase rate first (T18917).
- When citing N8194, label it as a single indie, self-reported example of a soft-currency cosmetic price, not a platform benchmark or a Robux price point.

## Not covered here (research elsewhere)
- No data on optimal price points by genre or Robux amounts for starter packs.
- Limited coverage of regional pricing, Managed Pricing outcomes and Shop surfacing impact.
- No benchmarks for conversion rates or ARPPU beyond a few official case studies.
- No guidance on policy limits for randomised items and time-limited offers beyond reward rules.
- Little on subscriptions, Premium payouts and ad rewards interplay with products.
- Code details (DataStore idempotency, retry patterns) are not covered in depth.
- Legal and platform policy for random item disclosure, age ratings and random-drop rules (not covered by these sources).
- Measured conversion or ARPDU for starter packs, bulk discounts, cash boosts and skip products (sources report none).
- Refund and chargeback handling, including whether to revoke items on refund.
- How ProcessReceipt interacts with subscriptions or Premium-style benefits.
- Exact DevEx conversion rate (only creator-derived ratios are available).
- Concrete DataStore schema for pass-ownership records used with gifting.
- Scope and return behaviour of addItemAsync (T10030 gives only the call signature).
- Specific sales-health check criteria before running a sale.
- No official Roblox documentation was cited for Client.RequestOnce, IdempotencyKey, or NotProcessedYet behaviour; verify against current API docs before shipping.
- Nothing on how external surfacing eligibility is calculated beyond ProcessReceipt correctness.
- No refund, chargeback or receipt-dispute handling covered.
- No controlled A/B data comparing prices, tiers or conversion; all figures are self-reported single-game results.
- No retention or player-sentiment impact data for donation boards, paid revives or cascading multipliers.
- No ARPU or ARPPU benchmarks for typical genres.
- Premium payouts and their interaction with developer product revenue are only mentioned in passing (N4668).
- Legal and regional rules for cascading or paid-advantage mechanics are not covered.
- No [OFFICIAL] docs were included in this batch; platform fee, ProcessReceipt behaviour, and dashboard history limits need confirming from official DevForum or Creator Hub sources.
- No conversion or pricing-elasticity data beyond very small samples (e.g. 2 of 3 players).
- No comparisons across genres, game sizes, or audience sizes.
- No data on limited-time offer timing, sale frequency, or their effect on revenue.
- No data on bulk-bundle discount effects or repeat-purchase behaviour.
- Robux-to-USD conversion is inconsistent across sources; verify the current DevEx rate before estimating dollar revenue.
- No details on how ProcessReceipt was implemented in these creators' games, so the idempotency and save-before-grant claims are unverified here.
- N7294 gives no game context (genre, audience size, revenue, or how many of the 21 products are active versus retired), so it cannot show whether 21 products is high, low, or healthy.
- No conversion, revenue-per-product, or catalogue-versus-revenue data is available from the new item; research these from other sources.
- The source does not name the specific automation method, plugin, API or script used to create or name products.
- No detail on how to verify that automatically created products have the correct prices, icons or Listed status.
- No guidance on automation limits, rate limits or permissions for bulk creation.
- No official Roblox documentation on gifting developer products or gift purchase flows.
- No conversion rates, sample sizes, or A/B results for hub offers or starter-style offers.
- No data comparing bulk-action uptake against single-item purchases.
- No data on how removing limited items affects later sales or player retention.
- Revenue net of the platform cut is not quantified in this batch.
- No official Roblox documentation pages are cited in this batch; NotProcessedYet and retry behavior should be confirmed against current DevHub ProcessReceipt docs.
- Sample size, event length, and giveaway cost or prize structure behind the ~6x figure are not provided.
- No data on return on giveaway spend (Robux or items) versus incremental revenue.
- No guidance on how to detect and handle a lapsed player in your own analytics before running a retargeting event.
- Current Creator Dashboard UI and prompt wording for developer products are not covered by the 2019 source.
- No official documentation on server-wide boost fairness or policy.
- No conversion, ARPU or retention figures for the 5-minute deals, the reveal pack, or the bundle tiers.
- No sample sizes or time windows for the cheap pack and boost tests.
- No details on how stacking boosts were implemented or how their stacked timers were stored and granted.
- No exact odds or disclosure wording for the mystery seed pack.
- No cost or conversion data for sponsored traffic compared with organic.
- No comparison of soft-currency vs Robux-direct sales results in the same game.
- N8194 gives no Robux equivalent, conversion rate, or sales or conversion results for the Jelly Hoverboard skin, so it cannot show whether the price worked.

## Quotes (near-verbatim)
- "A developer product can be bought multiple times, so it's a great way to monetize your game along with game passes." ([AlvinBlox 2018-08 25:18](https://youtu.be/h92s4Xn26oc?t=1518))
- "Hard currencies must be carefully designed so that they remain rare." ([Roblox DevForum 2019-03 ](https://devforum.roblox.com/t/monetisation-101-how-to-effectively-generate-revenue-in-your-roblox-game/246902))
- "players that have purchased something in a game are more likely to purchase something again and that is a fact" ([TheDevKing 2020-05 8:33](https://youtu.be/Zqz_gclwM0M?t=513))
- "If your Dev Product does not satisfy the player within the first minute, you most likely failed." ([Roblox DevForum 2021-05 ](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207))
- "Whenever we do sales maybe like a 25, 30% sell off, we see a huge spike, two, three, four times increase in revenue." ([Roblox Creators 2023-01 0:00](https://youtu.be/YdplC2WVkWc?t=0))
- "for some reason you can only go back a couple months on developer products" ([Mulch 2023-04 5:30](https://youtu.be/6perjdMg3T4?t=330))
- "it has no game passes it just has developer products which they are kind of broken a little bit" ([PolarBear 2024-03 0:00](https://youtu.be/Q-Wbi1an-ww?t=0))
- "We ended up adding this starter pack for 79 Robux... And as soon as we added this into the game, the game started making two to three times more money." ([1Coal 2024-03 2:25](https://youtu.be/gWNOANEPYLY?t=145))
- "a developer product can be purchased over and over again unlike a Game Pass which can only be purchased once" ([AlvinBlox 2024-06 0:00](https://youtu.be/5YNFRCD0pd0?t=0))
- "they're all at spawn so you're immediately aware of these things which is what makes them purchased so many times" ([CallMeDogey 2025-01 10:14](https://youtu.be/USJC5l_wpuY?t=614))
- "Super Pack, Starter Pack, and Grower Flowers are the top three." ([Quez 2025-06 1:58](https://youtu.be/WOG3Rttf-V4?t=118))
- "I've spent well over 10,000 Robux. What's the point?" ([Bemmy 2025-06 9:49](https://youtu.be/-Z0C5YJtnqY?t=589))
- "all the like dev products are really, really cheap" ([Arow 2025-07 1:09](https://youtu.be/KsaRtStNO3s?t=69))
- "You certainly shouldn't think every single ad is stealing someone away who was going to buy it." ([Roblox Creators 2025-08 22:35](https://youtu.be/7AtvvUxvCaU?t=1355))
- "Basically nothing. Right now, if you want this to be better, you'll probably want to do 2x money so that it's more enticing to the player." ([PineappleDev 2025-09 0:00](https://youtu.be/gXKoxaK6Ufg?t=0))
- "In my experience, it's pretty difficult to actually monetize Roblox games." ([PineappleDev 2025-09 2:30](https://youtu.be/gXKoxaK6Ufg?t=150))
- "Products should feel like a must-have, not a nice-to-have... they should be solving a pain." ([Tizzy 2026-06 14:12](https://youtu.be/zoz3PSMqets?t=852))
- "Consumables really pump this stat because they can buy the 24-hour lock today, tomorrow, the next day." ([Tizzy 2026-06 5:24](https://youtu.be/zoz3PSMqets?t=324))
- "Sell other things instead of currency packs cuz I'm not going to lie, that's just mid." ([Alex Builds Games 2026-06 4:24](https://youtu.be/x_SflcuSi1w?t=264))
- "Your best-selling products are always going to be the ones that solve a specific pain that your players are already feeling, not features that are nice to have." ([MoseyTube 2026-07 1:51](https://youtu.be/-PoyiiGhoNo?t=111))
- "Right now I'm spending more than I'm truly making." ([MonarchDev 2026-08 4:47](https://youtu.be/jX3E9OHBeTg?t=287))
- "You create the worth yourself. The player has to think they're getting the better end of the deal." ([VuukStudios 2026-09 6:47](https://youtu.be/2Q4NqQikzsY?t=407))
- "Dev products is like items that you can buy anytime. But game passes are items that you can literally only buy once." ([kra_DeZ 2026-09 13:51](https://youtu.be/cJ-YzHHhQs8?t=831))
- "Robux purchase conversion rate is 1%... 7,000 players saw the Robux prompt, but only a 100 bought it" ([Seibo 2026-10 3:36](https://youtu.be/Fh0Xku6NwOQ?t=216))
- "Dev Products generally monetize better, as they can be repeatedly purchased." ([Roblox Creator Docs 2026-10 ](https://create.roblox.com/docs/get-started/monetization))
- "Do not use the PromptProductPurchaseFinished event to process purchases. You must use the ProcessReceipt callback instead." ([Roblox Creator Docs 2026-10 ](https://create.roblox.com/docs/production/monetization/developer-products))
- "The functions for handling each product ID must return true for the transaction to be successful." ([Roblox Creator Docs 2026-10 ](https://create.roblox.com/docs/production/monetization/developer-products))

## Verified additions

_Hand-added, labelled and sourced rows kept in `youtube-learn/supplements/topics/monetisation-devproducts.md`; they survive rebuilds._

- **Creator said $0.038 per Robux (WTMW20 'Where The Money Went', 2026-10); official DevEx rate is $0.0038 [OFFICIAL, docs 2026-11-01]; the $0.054 verified 18+ US figure is really $0.0054** (official): 10x error. Check: 700 Robux x $0.0038 = $2.66. Sources: [Roblox Creator Docs developer-exchange 2026-11-01](https://create.roblox.com/docs/production/monetization/developer-exchange). Newest source 2026-11-01.
- **Creator Rewards rules (replaces Premium/Engagement-Based Payouts since 2025-07-24)** (official, 2026-11-01): Daily Engagement = 5 Robux per Active Spender ($9.99+ qualifying purchases in 60 days) who plays 10+ min in one of their first 3 experiences that day; open to all creators, no enrolment. Audience Expansion = 35% of a new/reactivated user's first $100 of purchases in 60 days; needs an ID-verified account and the experience averaging 100+ DAU for 60 days. Rewards are Earned Robux with a 60-day hold; cash-out is under DevEx terms. Docs publish no per-minute Premium rate, so older Premium-payout figures (e.g. 5 Robux per 10 minutes, Mulch/PineappleDev 2020-2024) are historical. Sources: [Roblox Creator Docs creator-rewards 2026-11-01](https://create.roblox.com/docs/creator-rewards), [engagement-based-payouts](https://create.roblox.com/docs/production/monetization/engagement-based-payouts). Newest source 2025-07-24.

_Chunk 16 (2026-11-01)._

- **Prompt purchases only for the current game's products** (OFFICIAL, Creator Docs reference, 2026-10-29): MarketplaceService:PromptProductPurchase fails for a developer product from another game, even if you own both; Studio mock purchases do not check this, so verify the productId belongs to the current game before publishing. Same rule for PromptGamePassPurchase. Source: [MarketplaceService reference](https://create.roblox.com/docs/reference/engine/classes/MarketplaceService).

## Appendix: every extracted tip on this topic

- 2018-08-07 AlvinBlox [26:40](https://youtu.be/h92s4Xn26oc?t=1600): Use Developer Products (not gamepasses) for consumable currency, since they can be bought repeatedly; gamepasses are one-time purchases.
- 2019-03-01 Roblox DevForum [page](https://devforum.roblox.com/t/monetisation-101-how-to-effectively-generate-revenue-in-your-roblox-game/246902): Show a personal, time-limited bundle about 30-60 minutes in, right after a milestone, when the player is engaged enough to buy.
- 2019-03-01 Roblox DevForum [page](https://devforum.roblox.com/t/monetisation-101-how-to-effectively-generate-revenue-in-your-roblox-game/246902): Price first offers like a cup of coffee (a couple of dollars); first purchases should be small.
- 2019-03-01 Roblox DevForum [page](https://devforum.roblox.com/t/monetisation-101-how-to-effectively-generate-revenue-in-your-roblox-game/246902): Escalate bundle prices gradually at each new milestone, a couple of hours apart, without frustrating players.
- 2019-03-01 Roblox DevForum [page](https://devforum.roblox.com/t/monetisation-101-how-to-effectively-generate-revenue-in-your-roblox-game/246902): Make the store easy to reach and route players to it for free rewards so they see every sale and event.
- 2019-03-01 Roblox DevForum [page](https://devforum.roblox.com/t/monetisation-101-how-to-effectively-generate-revenue-in-your-roblox-game/246902): Keep the hard currency scarce; let players earn small amounts slowly so they buy meaningful items with real money.
- 2019-12-01 TheDevKing [1:12](https://youtu.be/QC2bDZsFiz4?t=72): Create dev products under Creator Dashboard > game > Configure > Developer Products; dev products are repeatable purchases, unlike one-time game passes.
- 2019-12-01 TheDevKing [8:11](https://youtu.be/QC2bDZsFiz4?t=491): Set MarketplaceService.ProcessReceipt to a function and return Enum.ProductPurchaseDecision.PurchaseGranted only after the reward is actually given; otherwise Roblox retries.
- 2019-12-01 TheDevKing [11:36](https://youtu.be/QC2bDZsFiz4?t=696): If the player is nil in ProcessReceipt (player left), return NotProcessedYet so Roblox calls the callback again when they rejoin.
- 2019-12-01 TheDevKing [16:13](https://youtu.be/QC2bDZsFiz4?t=973): Check receipt.ProductId against each dev product ID inside ProcessReceipt before granting, so one product's handler doesn't fire for another product.
- 2019-12-01 TheDevKing [4:22](https://youtu.be/QC2bDZsFiz4?t=262): Use a LocalScript to call MarketplaceService:PromptProductPurchase(player, productId) to show the buy prompt, and handle granting on the server.
- 2020-05-12 TheDevKing [9:57](https://youtu.be/Zqz_gclwM0M?t=597): Offer a cheap starter bundle (coins, items, extra level) when a player hits a milestone around 20-30 minutes in; don't prompt purchases in the first 30 seconds.
- 2020-05-12 TheDevKing [12:36](https://youtu.be/Zqz_gclwM0M?t=756): When a player can't afford an item, show a developer product prompt to buy the exact currency amount needed instead of just saying they can't buy it.
- 2020-05-12 TheDevKing [6:06](https://youtu.be/Zqz_gclwM0M?t=366): Sell a spendable in-game currency; developer products generally earn as much or more than game passes for most games.
- 2020-05-12 TheDevKing [8:33](https://youtu.be/Zqz_gclwM0M?t=513): Target the first purchase: a player who has bought once is far more likely to buy again, so the first purchase is the key conversion step.
- 2021-05-17 Roblox DevForum [page](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207): Use Dev Products for consumables and economy currency, and for instant-satisfaction boosts that pay off within the first minute.
- 2021-05-17 Roblox DevForum [page](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207): Sell currency in uneven tiers (e.g. 100, 2000, 7600, 10200) rather than round numbers, and discount larger bundles; highlight a 'best seller'.
- 2021-05-17 Roblox DevForum [page](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207): Create recurring Dev Products (e.g. a bail-out purchase) players naturally repeat, since repeat purchases feel reliable.
- 2021-05-17 Roblox DevForum [page](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207): Avoid overpriced Dev Products that give only brief satisfaction; reserve high Robux prices for currency.
- 2022-04-30 B Ricey [0:35](https://youtu.be/5bI6l6SHBDU?t=35): Create developer products in Game Settings > Monetization > Developer Products; unlike game passes they can be bought repeatedly, so use them for consumables like currency.
- 2022-04-30 B Ricey [5:45](https://youtu.be/5bI6l6SHBDU?t=345): Grant the item by calling your existing player-manager setter rather than editing leaderstats directly, so all currency changes go through one function.
- 2022-04-30 B Ricey [8:29](https://youtu.be/5bI6l6SHBDU?t=509): In ProcessReceipt, return NotProcessedYet if the player is not in the server; Roblox will retry later, preventing players from paying without receiving the item.
- 2022-04-30 B Ricey [9:51](https://youtu.be/5bI6l6SHBDU?t=591): Wrap the product grant function in pcall; if it errors, return NotProcessedYet so the purchase is not charged without being granted.
- 2022-04-30 B Ricey [10:32](https://youtu.be/5bI6l6SHBDU?t=632): Only return PurchaseGranted after the grant succeeds; this is what tells Roblox the purchase completed.
- 2022-06-08 Roblox DevForum [page](https://devforum.roblox.com/t/introducing-monetization-metrics-for-the-analytics-dashboard/1826688): Design progression and economy so players make a first purchase, since first-purchase conversion drives longer-term paying users.
- 2023-01-12 Roblox Creators [4:25](https://youtu.be/okAygI1sxsA?t=265): Highlight the best-value currency bundle with a tag and show bonus amounts (e.g. 10% more free) to steer buyers toward larger purchases.
- 2023-01-19 Roblox Creators [0:00](https://youtu.be/YdplC2WVkWc?t=0): Use in-game currency as a free-to-play path and as a sample: let players trial paid items with earned currency to convert hesitant buyers.
- 2023-01-19 Roblox Creators [0:00](https://youtu.be/YdplC2WVkWc?t=0): Create event-specific currency for limited events so rich hoarders cannot buy out event content on day one and participation is required.
- 2023-01-19 Roblox Creators [0:00](https://youtu.be/YdplC2WVkWc?t=0): Run sales only a handful of times per year at a consistent but infrequent cadence; frequent sales train players to wait and buy only on sale.
- 2023-01-19 Roblox Creators [0:00](https://youtu.be/YdplC2WVkWc?t=0): Check monetization graphs are healthy before running a sale; Emergency Response saw 2-4x revenue spikes from 25-30% sales.
- 2023-01-26 Roblox Creators [2:54](https://youtu.be/vQNJztcS2AI?t=174): Make dev products (buying currency with Robux) your main revenue source; permanent gamepasses like permanent double cash are risky to balance.
- 2023-01-26 Roblox Creators [13:31](https://youtu.be/vQNJztcS2AI?t=811): Selling in-game currency for Robux lets players buy items like tractors with it; this is comparable to selling the item directly.
- 2023-02-23 Roblox Creators [41:16](https://youtu.be/BsyU-SJ9L-c?t=2476): Give visual and audio reward feedback on purchase (e.g., coins raining down) and confirm items landed in inventory to avoid scam complaints.
- 2023-03-09 Roblox Creators [0:07](https://youtu.be/Cli3ogW-azk?t=7): Accept that not all players can pay; offer a wide range of purchasable options so free players can try spending.
- 2023-05-07 1Coal [1:20](https://youtu.be/JzB8fpyofnw?t=80): In obbies, offer a skip-stage button; the speaker says this is where most obby money comes from.
- 2023-06-01 Roblox Creators [0:48](https://youtu.be/yn4V-fBdUm8?t=48): If a developer product is misissued, use purchase data to find affected buyers in the time window and compensate them.
- 2023-06-15 Suphi Kaner [57:14](https://youtu.be/UAdE8-AfuMo?t=3434): For purchases, force DataStore:save() before granting the item; if save fails, deduct the granted amount and return NotProcessedYet so the player can't get it free later.
- 2023-06-15 Suphi Kaner [52:26](https://youtu.be/UAdE8-AfuMo?t=3146): Route ProcessReceipt through a table keyed by product ID to add new products by adding one function.
- 2023-08-25 Roblox Creators [4:39](https://youtu.be/lOOvOIJoMi4?t=279): In shop UI, use empty space, size and color to make the largest, most valuable bundle stand out; add a best-value banner.
- 2023-08-29 janisjanis01 [2:59](https://youtu.be/fRBNHaMtvFs?t=179): If the game has currency, add developer products so players can buy it with Robux.
- 2023-09-12 janisjanis01 [5:31](https://youtu.be/9aQpeTCZ7yM?t=331): Developer products need their own server script to grant currency; a GUI button alone sells nothing.
- 2023-09-19 Roblox [18:34](https://youtu.be/Z-ZKqBPdl44?t=1114): Offer larger cash packs with better Robux-to-cash value; Driving Empire saw an 8% sustained revenue-per-user increase.
- 2023-11-02 Roblox DevForum [page](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585): Store all gamepass and product IDs in one ReplicatedStorage module grouped by category so clients and server scripts share one source.
- 2023-12-31 Roblox DevForum [page](https://devforum.roblox.com/t/understand-the-roblox-algorithm/2772921): Use a cheap starter pack that expires in 24 hours to create urgency and break new players' no-spend mindset.
- 2024-02-08 PolarBear [0:41](https://youtu.be/SNauF9OES7E?t=41): Add developer product purchases to a small game early; the speaker earned 257 Robux from 2 purchases among 3 players.
- 2024-02-28 Roblox DevForum [page](https://devforum.roblox.com/t/discovery-on-roblox-past-present-and-future-vision/2859111): Introduce new products and price points via dev products, gamepasses or subscriptions to improve monetisation and retention.
- 2024-03-01 MonzterDEV [13:44](https://youtu.be/em15yK5RjBk?t=824): Introduce new products and price points with developer products, gamepasses and subscriptions, and make purchases worth the price.
- 2024-03-06 PolarBear [1:22](https://youtu.be/Q-Wbi1an-ww?t=82): Sell a 15 Robux rebirth-style developer product as a shortcut; the speaker tested a +1 rebirth purchase but did not verify it worked.
- 2024-03-14 1Coal [2:25](https://youtu.be/gWNOANEPYLY?t=145): Add a time-limited starter pack (79 Robux, 15-minute window) to convert players; revenue roughly doubled to tripled after adding it.
- 2024-06-04 AlvinBlox [0:36](https://youtu.be/5YNFRCD0pd0?t=36): Create the developer product in game settings Monetization or create.roblox.com, then copy its product ID for scripting; the game must be published first.
- 2024-06-04 AlvinBlox [1:12](https://youtu.be/5YNFRCD0pd0?t=72): Prompt purchases from a LocalScript using MarketplaceService:PromptProductPurchase with the local player and product ID, e.g. on a button click.
- 2024-06-04 AlvinBlox [12:03](https://youtu.be/5YNFRCD0pd0?t=723): Developer products are consumable and can be bought repeatedly, unlike gamepasses; use them for currency or temporary boosts.
- 2024-06-30 Mulch [1:23](https://youtu.be/pqCXX06vlDw?t=83): Use a donation board and skip-stage dev products; they earned ~3,000 Robux combined.
- 2024-08-30 VuukStudios [1:59](https://youtu.be/3J7Vp6NgYf4?t=119): Sell repeatable consumables (e.g. coins) as developer products; use them for purchases players make again and again.
- 2024-09-06 PineappleDev [2:25](https://youtu.be/UBs1bebPu0s?t=145): Add a donation board; in Idle Dice it brought 216 Robux from developer products alone, useful for players who won't buy gamepasses.
- 2024-09-23 Roblox [16:14](https://youtu.be/DxrLfwsfV1I?t=974): Show a discounted starter pack bundle right after the tutorial completes to lift paying-user conversion.
- 2024-09-23 Roblox [26:39](https://youtu.be/ETDit6eO4sQ?t=1599): Sell a core perk as a dev product (Adopt Me: 250 Robux for two equipped pets) and put extra exclusives, like a monthly pet, behind the subscription.
- 2024-09-23 Roblox [15:26](https://youtu.be/QC6XWgJRJEM?t=926): Launch themed items and first-time purchase bonuses with major events and updates to ride the hype.
- 2024-09-23 Roblox [16:08](https://youtu.be/QC6XWgJRJEM?t=968): Use personalized, time-limited offers shown before the first, second and third dungeon; Dungeon Quest got +180% payer conversion on day one.
- 2024-09-23 Roblox [18:08](https://youtu.be/QC6XWgJRJEM?t=1088): For events, make them accessible to all levels and add one-time first-purchase bonus per Premium currency tier; drove purchases and 50% lift for two weeks.
- 2024-11-17 janisjanis01 [9:47](https://youtu.be/vJekPDaIT30?t=587): Sell a server-wide luck boost that stacks by purchase time and benefits everyone in the server; price doubles per purchase, but watch it isn't overpowered.
- 2024-11-17 janisjanis01 [2:22](https://youtu.be/vJekPDaIT30?t=142): Design boost prices to scale with effect; the speaker felt the luck boost was too strong at high multipliers.
- 2024-11-20 ByteBlox [2:03](https://youtu.be/Jl0SdXksQsI?t=123): Use developer products for repeatable purchases and gamepasses for one-time unlocks. Products can be bought many times; gamepasses only once.
- 2024-12-01 Mulch [43:58](https://youtu.be/tdnhCXx3srA?t=2638): Creator notes paid eggs and paid event items cost hundreds of Robux per session, and a price-per-egg increase after a few hatches feels exploitative to players.
- 2024-12-01 Mulch [2:14:32](https://youtu.be/tdnhCXx3srA?t=8072): Fixed-price exclusive egg bundles and forever packs are a repeated revenue pattern; the creator frequently spent 400+ Robux per update.
- 2024-12-03 BubuTheDev [2:07](https://youtu.be/82HrjFTdPkU?t=127): Amazing Deal (~30 Robux) sold 155 times, the best developer product; a low-price offer drives volume.
- 2025-01-15 CallMeDogey [10:14](https://youtu.be/USJC5l_wpuY?t=614): Place cheap-to-expensive pet developer products right at spawn so players see them immediately; that drove most repeat purchases.
- 2025-01-15 CallMeDogey [10:14](https://youtu.be/USJC5l_wpuY?t=614): Developer products out-earned game passes for him (1.9M vs 841k Robux) because players buy pet products multiple times.
- 2025-01-17 PineappleDev [7:15](https://youtu.be/OzqyuEoN7t8?t=435): Avoid letting a currency be earned and spent infinitely without cost; the speaker's cheeseburger items did not consume summits, which removes the reason to spend.
- 2025-02-04 GameMakers [3:40](https://youtu.be/qZRNpN5M8jA?t=220): Tie offers to player milestones that were hard to reach. Players feel emotional highs at achievements, so offers there convert best.
- 2025-03-16 PineappleDev [0:32](https://youtu.be/a4PQqMC8ruA?t=32): Sell paid revives and difficulty potions; these were the main developer-product earners in this game, per the creator.
- 2025-05-23 RoDev [17:06](https://youtu.be/Gw2FwndwnOg?t=1026): Bundle starter packs as a high-value offer; the stream showed a 4,900 Robux bundle as a plausible starter buy, though its conversion was not measured.
- 2025-05-25 Arow [0:53](https://youtu.be/cqi75Z70Urk?t=53): Include developer products alongside gamepasses (about five total in the speaker's game) as ongoing purchase options.
- 2025-06-01 janisjanis01 [2:47](https://youtu.be/B409dMcW-pw?t=167): Offer cheap currency packs (e.g. 50 currency for 9 Robux, 1,500 for 99 Robux) to convert new players.
- 2025-06-01 janisjanis01 [6:18](https://youtu.be/B409dMcW-pw?t=378): Sell a mystery seed pack (e.g. 199 Robux) with a crate-opening animation that reveals the rolled item.
- 2025-06-15 janisjanis01 [12:35](https://youtu.be/W9JYImC0FBg?t=755): Offer time-limited special deals (5 minutes) to create urgency for purchases.
- 2025-06-21 Quez [0:34](https://youtu.be/WOG3Rttf-V4?t=34): Sell consumables via developer products (seeds, growing all flowers, gear, starter/super packs); in this game these drove nearly all revenue.
- 2025-06-28 Bemmy [0:00](https://youtu.be/-Z0C5YJtnqY?t=0): Crate pricing: single crate 349 Robux; buying in bulk shows a discount (e.g. ~174 Robux per crate in bundles). Bulk-bundle discounts were shown to push spending.
- 2025-06-28 Bemmy [3:57](https://youtu.be/-Z0C5YJtnqY?t=237): Limited-time/update-day crate offers and bulk purchase prompts were used to encourage spending; a 1% exotic-odds crate was reportedly framed as a secret-tier pull.
- 2025-07-13 Arow [1:09](https://youtu.be/KsaRtStNO3s?t=69): Developer products priced very cheaply drag down average revenue per user; the speaker blames cheap dev product prices for low per-user earnings.
- 2025-07-13 janisjanis01 [12:29](https://youtu.be/pD8fKkzF8O8?t=749): Sell instant-growth and similar consumables as developer products; use separate variables per product to avoid mixing up purchases.
- 2025-07-13 janisjanis01 [13:10](https://youtu.be/pD8fKkzF8O8?t=790): Bundle starter, pro and god packs that give better value than buying items separately to raise payer conversion.
- 2025-07-27 janisjanis01 [7:18](https://youtu.be/Sgs36l6K5EU?t=438): Put starter packs prominently; creator considered them the main revenue source.
- 2025-08-29 Roblox Creators [22:35](https://youtu.be/7AtvvUxvCaU?t=1355): Estimate cannibalisation of payers conservatively: cap the value of a rewarded item at roughly 100x earnings per ad view; track earnings per ad view in Creator Hub.
- 2025-09-01 PineappleDev [0:41](https://youtu.be/gXKoxaK6Ufg?t=41): Sell a cheap first multiplier (e.g. 1.1x for 9 Robux) so most players will buy it; escalate each tier's multiplier and price in a chain.
- 2025-09-01 PineappleDev [0:41](https://youtu.be/gXKoxaK6Ufg?t=41): Keep multipliers modest (e.g. 1.1x steps) so the game does not become pay-to-win, per the speaker's reasoning.
- 2025-09-01 PineappleDev [2:09](https://youtu.be/gXKoxaK6Ufg?t=129): Cascading tiered purchases can carry a weak monetising game; the speaker says monetisation is hard on Roblox and this lifted a game's revenue.
- 2025-09-01 PineappleDev [2:30](https://youtu.be/gXKoxaK6Ufg?t=150): Implement with a product ID list ordered by tier; on ProcessReceipt, check if the ID is in the list and increment the player's saved multiplier count.
- 2025-09-07 janisjanis01 [8:44](https://youtu.be/YVKHlrlWn-k?t=524): Offer a guaranteed-mutation purchase (gold crate yields golden crop) and a high-tier crate for 499 Robux to drive conversion.
- 2025-09-21 janisjanis01 [6:16](https://youtu.be/uNLDi_GO2MA?t=376): Cheap temporary boost developer products were used to try to lift conversion; creator still reported weak monetisation, so test pricing and placement.
- 2025-09-26 Roblox [3:29](https://youtu.be/MJ-zYfL10Ew?t=209): Tailor offers by player segment: cheap starter pack for new players, mid-tier upgrade for casuals, limited high-price offer for high spenders.
- 2025-09-26 Roblox [23:49](https://youtu.be/MJ-zYfL10Ew?t=1429): Avoid popup spam of stacked offers after first purchase; aim to convert new players to a first purchase quickly.
- 2025-09-26 Roblox [25:13](https://youtu.be/MJ-zYfL10Ew?t=1513): Monetize speed or convenience in the core loop, not basic movement; Spongebob TD gave 2x free to group members, converting a $5 3x-speed product.
- 2025-09-26 Roblox [21:14](https://youtu.be/MJ-zYfL10Ew?t=1274): Build low-entry starter bundles, scale them for repeat buyers, then unlock elite bundles and private offers as spending thresholds are reached.
- 2025-09-26 Roblox [27:07](https://youtu.be/j6OPA95-1O0?t=1627): Test starter pack variables: product type, price, presentation art, prompt timing, and offer duration (FOMO timer vs longer window).
- 2025-09-26 Roblox [28:29](https://youtu.be/j6OPA95-1O0?t=1709): Use recognizable value language like 'guaranteed uncommon or better' and a relevant icon; Adopt Me's royal egg beat the cracked egg by +6% new-user conversion.
- 2025-10-19 bubDEV [7:14](https://youtu.be/N-u2gI4DUyw?t=434): Add a limited-time purchasable item to the game; the speaker says the template lacked one and he expects it to lift ARPDU.
- 2025-11-02 janisjanis01 [10:16](https://youtu.be/QnAoCsC-4ig?t=616): Add a cheap consumable like a cash boost (20% more cash) to lift conversion; it is simple to script.
- 2025-12-01 Matt The Method [2:04](https://youtu.be/MPHPumDvMIs?t=124): Developer products (currency purchases) are usually the most rewarding of the three revenue streams, per creator.
- 2025-12-13 Crusherfire [5:40](https://youtu.be/6Q_p2ObUXSo?t=340): Roblox can't gift game passes directly. Sell a developer product, treat it as a pass, and record ownership in a DataStore. Purchases stack and can be gifted.
- 2025-12-24 1_Bruce [6:19](https://youtu.be/wKI3PBO3bB0?t=379): Sell limited-stat developer products like 'global runes' that give a stat to every online player; these sell well.
- 2026-02-02 Matt The Method [1:12](https://youtu.be/TEENlwjuKWI?t=72): Developer products brought in most revenue (~31k Robux), ahead of gamepasses (~23k Robux) in this game.
- 2026-03-15 1_Bruce [4:46](https://youtu.be/zgq6L4ZzCHs?t=286): Use bundled consumables like a potion bundle as a top seller; developer products drove most Robux revenue.
- 2026-03-15 1_Bruce [3:25](https://youtu.be/zgq6L4ZzCHs?t=205): Developer products generated most of the Robux revenue in this game; prioritize consumable products over other monetisation.
- 2026-04-16 Roblox [18:37](https://youtu.be/8IcYpOl4Sdk?t=1117): Automate repetitive Creator Hub chores such as creating and naming dozens of developer products and copying IDs into Studio, which the speaker says can take about 2 hours manually.
- 2026-04-30 rasdev [3:22](https://youtu.be/G15TVsyC61g?t=202): Keep purchase prompts small and unobtrusive; a giant purchase button on screen during play hurts retention and the algorithm.
- 2026-04-30 MoseyTube [2:44](https://youtu.be/sFr7htxsnR4?t=164): Offer many developer product options (he used 59) so players have more chances to spend Robux; he admits this may be excessive.
- 2026-04-30 rasdev [2:41](https://youtu.be/yFKY2FlwHjE?t=161): Sell purchases in in-game currency rather than charging Robux per item, to create distance from real money.
- 2026-05-01 LovJak [4:05](https://youtu.be/FpbZRgRHYjQ?t=245): Set developer product prices and update their UI; likewise replace gamepass icons and make the gamepasses work in-game.
- 2026-05-10 janisjanis01 [8:37](https://youtu.be/BLOToGi2Qt4?t=517): Offer a cheap boost (e.g. 1.5x cash for 5 Robux) to improve per-conversion rate in early monetisation.
- 2026-05-12 Yann [3:25](https://youtu.be/dbNA3K8lt2w?t=205): Bundle gamepass-style perks (e.g. exclusive packs) into one developer product; their 500-coin product was their best seller.
- 2026-05-12 Yann [4:48](https://youtu.be/dbNA3K8lt2w?t=288): Offer a starter pack aimed at new players; it was a strong seller in Grow Bamboo for Pandas.
- 2026-05-12 Yann [4:48](https://youtu.be/dbNA3K8lt2w?t=288): Random gambling-style products (like lucky-block-style random secrets) sell well in the creator's experience.
- 2026-06-01 Deconstructor of Fun [23:58](https://youtu.be/2BsMLCk8FEU?t=1438): Retarget churned and existing players with creator giveaways. Re-engaged players spent about 6x more than new creator-acquired users in those events.
- 2026-06-10 Tizzy [3:27](https://youtu.be/HFcegpPPvpI?t=207): Sell a cheap repeatable consumable, e.g. offer to double offline earnings for 19 Robux when collecting; drastically raised payer conversion.
- 2026-06-15 Tizzy [0:50](https://youtu.be/zoz3PSMqets?t=50): Sort your dev products by sales in descending order, then add higher tiers above your best seller (e.g. +30 and +100 speed on top of +10).
- 2026-06-15 Tizzy [4:02](https://youtu.be/zoz3PSMqets?t=242): Sell repeatable consumables as dev products, not gamepasses. A 24-hour base lock became his top seller within 2 days.
- 2026-06-15 Tizzy [5:24](https://youtu.be/zoz3PSMqets?t=324): Turn 2x offline earnings from a gamepass into a consumable; one-time passes cap repeat spend, consumables recur daily.
- 2026-06-15 Tizzy [6:05](https://youtu.be/zoz3PSMqets?t=365): Copy competitor monetization patterns you see repeated (e.g. Sell Lemons' 2x offline earnings), then test them in your game.
- 2026-06-15 Tizzy [6:52](https://youtu.be/zoz3PSMqets?t=412): Add multiple purchase pathways to the same product: HUD shop icon, a plus button beside cash, and in-world prompts. He said more pathways is usually better.
- 2026-06-15 Tizzy [8:15](https://youtu.be/zoz3PSMqets?t=495): When a player can't afford an item, show the error first; on the third attempt open the cash shop directly. Opening it immediately was advised against.
- 2026-06-15 Tizzy [10:20](https://youtu.be/zoz3PSMqets?t=620): Place dev products at points of interest where players walk most, like the base entrance, not in a rarely visited corner.
- 2026-06-15 Tizzy [11:27](https://youtu.be/zoz3PSMqets?t=687): Make products solve a pain: grinding (speed, cash), theft while AFK (base lock), missing out (offline earnings), or looking casual (cosmetics).
- 2026-06-15 Tizzy [13:31](https://youtu.be/zoz3PSMqets?t=811): Show the offer at the moment of need, e.g. the 2x offline earnings prompt when the player collects offline earnings.
- 2026-06-16 Alex Builds Games [4:24](https://youtu.be/x_SflcuSi1w?t=264): Don't rely on currency packs; speaker found them weakest (D tier) in most genres, with buyers preferring direct item purchases.
- 2026-06-19 LovJak [6:17](https://youtu.be/ImcICq5XfL8?t=377): Offer Robux purchases directly in the shop (e.g. buy seeds with Robux) as the core monetisation path.
- 2026-06-24 Roblox DevForum [page](https://devforum.roblox.com/t/introducing-shop-a-personalized-in-game-storefront/4701505): Review developer product Listed/Not Listed status before July 7; new developer products default to Not Listed and won't appear in Shop until set to Listed.
- 2026-06-24 Roblox DevForum [page](https://devforum.roblox.com/t/introducing-shop-a-personalized-in-game-storefront/4701505): Implement ProcessReceipt properly for developer products; required for eligibility for external surfacing and ensures purchases are delivered immediately.
- 2026-06-29 MoseyTube [5:13](https://youtu.be/Kh_XKYw8ocU?t=313): Offer 20-30 developer products across different price points so players with different spend levels all have an option.
- 2026-07-05 janisjanis01 [5:22](https://youtu.be/OL1FJ17wzZE?t=322): Limited-time items with real gameplay boosts (speed skins) were used to push monetisation; the creator called them better than cosmetics.
- 2026-07-07 Generalist Programmer [2:28](https://youtu.be/pbt3ui5om8I?t=148): Developer products have the higher ceiling because hooked players can buy them repeatedly. Sell only a few products and passes, don't overload the store.
- 2026-07-13 Tizzy [18:56](https://youtu.be/nggNvUILQ1I?t=1136): Offer a Robux option for upgrades you can't afford in-game. This gives a clear purchase path at the moment of need.
- 2026-07-14 MoseyTube [0:50](https://youtu.be/-PoyiiGhoNo?t=50): Use developer products (consumables) instead of game passes for most items, since players can rebuy them every session rather than buying once.
- 2026-07-14 MoseyTube [1:51](https://youtu.be/-PoyiiGhoNo?t=111): Design products around a specific pain point players already feel, such as slow movement (speed boost), grinding (5x cash), or manual collection (auto collect).
- 2026-07-14 MoseyTube [3:44](https://youtu.be/-PoyiiGhoNo?t=224): Offer purchase entry points in multiple places: HUD shop button, a plus icon beside the currency counter, and in-world NPCs or buttons where players spend time.
- 2026-07-14 MoseyTube [4:36](https://youtu.be/-PoyiiGhoNo?t=276): Sell 2x offline earnings as a developer product rather than a game pass, since players will rebuy it every time they log back in.
- 2026-07-15 Roblox DevForum [page](https://devforum.roblox.com/t/scribe-v261-persistent-typed-auto-replicated-player-data-built-on-profilestore/4738905): Pass an IdempotencyKey on purchases and use Client.RequestOnce so retried commands or purchases apply at most once.
- 2026-07-23 Yann [2:53](https://youtu.be/Bw2ty2T46z4?t=173): Put a high-value consumable on the wheel spin/shop (e.g. spins giving best dragons); it was the top earner, and rebirth-skip products also sold well.
- 2026-07-23 Yann [3:34](https://youtu.be/Bw2ty2T46z4?t=214): Push a low-price starter pack on screen; the creator noted it was pushed heavily but at only 9 Robux it still needs testing.
- 2026-07-24 MoseyTube [2:35](https://youtu.be/a170E9klbP4?t=155): Let players pay Robux to recover a broken streak; players will pay to avoid losing progress they already built.
- 2026-07-24 MoseyTube [3:47](https://youtu.be/a170E9klbP4?t=227): Sell consumable hints (reveal job, reveal one letter) to stuck players who want to avoid losing.
- 2026-08-23 MonarchDev [4:06](https://youtu.be/jX3E9OHBeTg?t=246): Starter-pack style offers in the hub sold only ~70 Robux total; offer-based revenue is small without strong conversion.
- 2026-08-25 MoseyTube [4:26](https://youtu.be/xIBc5He_sy4?t=266): Sell fun, social items beyond progression; example: Nuke All developer product that kills all players on the server.
- 2026-09-01 VuukStudios [6:47](https://youtu.be/2Q4NqQikzsY?t=407): Offers must feel clearly worth it to players (e.g. 99 Robux for auto skip); players won't buy something that seems just okay.
- 2026-09-06 kra_DeZ [13:51](https://youtu.be/cJ-YzHHhQs8?t=831): Build many dev products and microtransactions; he argues they earn more Robux than gamepasses since they can be bought repeatedly.
- 2026-09-09 Mulch [9:22](https://youtu.be/U2IjSOyNTB8?t=562): Offer a one-tap bulk action (e.g. grow all for 184 Robux) to convert players who have many eggs to open.
- 2026-09-09 Roblox DevForum [page](https://devforum.roblox.com/t/roblox-provided-discounts-on-in-game-items/4861443): Make developer products eligible for the in-game Shop to be included in Roblox-provided discount offers.
- 2026-09-17 Roblox [44:33](https://youtu.be/3a2RbLOAl4A?t=2673): Developer products can be edited live from mobile tooling, letting you adjust prices without a code update.
- 2026-09-22 Roblox DevForum [page](https://devforum.roblox.com/t/players-can-now-find-in-game-items-outside-your-game/4888425): List every pass and developer product in Creator Hub > Monetization > Shop; Listed status is the first requirement for appearing outside your game.
- 2026-09-22 Roblox DevForum [page](https://devforum.roblox.com/t/players-can-now-find-in-game-items-outside-your-game/4888425): Implement ProcessReceipt correctly for every developer product, both in-game and outside it, or the item may not be granted and cannot be sold externally.
- 2026-09-22 Roblox DevForum [page](https://devforum.roblox.com/t/players-can-now-find-in-game-items-outside-your-game/4888425): Check Creator Hub > Monetization > Shop for the ProcessReceipt report banner; no banner means no products need fixing.
- 2026-09-22 Roblox DevForum [page](https://devforum.roblox.com/t/players-can-now-find-in-game-items-outside-your-game/4888425): After fixing ProcessReceipt in Studio and publishing, select the items in the report and click Mark as fixed to make them eligible externally.
- 2026-09-22 Roblox DevForum [page](https://devforum.roblox.com/t/players-can-now-find-in-game-items-outside-your-game/4888425): Add custom icons to developer products so players recognise them; otherwise a default icon is shown.
- 2026-09-23 Lnor Roblox [3:39](https://youtu.be/gSFxStWqmgM?t=219): Offer a starter pack and boost potions (double money, luck, aura) as early purchasable boosts.
- 2026-09-25 kra_DeZ [7:35](https://youtu.be/ZradA-cygP0?t=455): Sell consumable developer products rather than gamepasses; in his game devproducts earned most Robux while gamepasses earned almost nothing.
- 2026-09-25 kra_DeZ [7:35](https://youtu.be/ZradA-cygP0?t=455): Make cheap, fun-themed items (e.g. a four-bullet gun) as devproducts; he plans more of these because they sell.
- 2026-09-25 Roblox DevForum [page](https://devforum.roblox.com/t/weekly-recap-september-21-25-2026/4894110): Use the Transaction Refunded webhook (Open Cloud) to revoke granted benefits when a Robux purchase is refunded or charged back.
- 2026-10-02 Seibo [4:19](https://youtu.be/Fh0Xku6NwOQ?t=259): Check the funnel gap: ~7,000 saw the Robux prompt but only ~100 bought (about 1%). Investigate prompt placement and offer value.
- 2026-10-10 RoyalDev [2:03](https://youtu.be/DLqlgL_7XrY?t=123): Include a monetization strategy in the design doc; his Hidden Anomaly game uses a cheap starter pack and small power purchases with some larger bat purchases.
- 2026-10-11 kra_DeZ [4:07](https://youtu.be/dE0njfPNsdY?t=247): In a horror game, a jump-scare developer product was the top seller, showing that scare-themed purchases can work even if the game as a whole doesn't.
- 2026-10-12 Roblox [5:42](https://youtu.be/hoMbv_R8AMU?t=342): Enable in-game Robux shopping so players can buy Robux and deals without leaving your game, since they often spend it in the same game.
- 2026-10-14 Tizzy [14:36](https://youtu.be/_JyiKfNNqls?t=876): Launch limited/whale products and consumables from the start, not two weeks in. A 1,000 Robux limited with fake scarcity sold well.
- 2026-10-14 Tizzy [15:20](https://youtu.be/_JyiKfNNqls?t=920): Don't make top-tier items too OP or sell cash packs early. Both likely fried the in-game economy and shortened the game's life.
- 2026-10-14 Tizzy [16:01](https://youtu.be/_JyiKfNNqls?t=961): Make the most powerful food scarce and priced higher. It became the best-selling food because it was limited.
- 2026-10-14 Tizzy [16:44](https://youtu.be/_JyiKfNNqls?t=1004): Stack cheap entry-level products (loss-leader style, e.g. 5 and 9 Robux speed tiers) to push players past the first-purchase threshold.
- 2026-10-17 GuideRealm [6:37](https://youtu.be/ltbZzXRrDF8?t=397): Replace all placeholder product IDs with real ones before release, and test data saving in a published test environment.
- 2026-10-20 rasdev [2:02](https://youtu.be/53OBGXktIPY?t=122): Sell repeatable consumables (spins, boosts, restocks, eggs) alongside one-time passes, since repeat purchases drive recurring revenue.
- 2026-10-25 Rapstrike GFX [1:22](https://youtu.be/6EoiHRT4dAA?t=82): Check how much revenue depends on one item; the creator notes ~40% of income came from a single dev product, a concentration risk.
- 2026-10-26 Deconstructor of Fun [29:59](https://youtu.be/NW4EShVGPYs?t=1799): Offer gifting: in one partnership 41% of Marvel Rivals purchases were gifts from friends (claimed), so make items giftable.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/analytics/monetization): Offer a mix of consumable and durable items so both short-term and long-term players have purchase options.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/analytics/monetization): Expand offerings of your top-selling items, since limited catalogs leave players with nothing new to buy.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/scripting/security/client-server-boundary): Grant passes and developer products only inside ProcessReceipt on the server; never trust PromptProductPurchaseFinished, which can be spoofed.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/scripting/security/client-server-boundary): In ProcessReceipt, handle repeat receipts: a product may already have been granted for a given receipt.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/get-started/monetization): Use Dev Products for repeatable purchases (boosts, consumables) since they can be bought many times and generally monetize better than one-time passes.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/resources/feature-packages/bundles): Use a new, unique developer product for each bundle so its sales can be tracked separately.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization): Use developer products for repeatable purchases such as currency, ammo, or potions; record purchases yourself with DataStoreService to avoid data loss.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/shop): Implement ProcessReceipt so players receive purchases immediately; required for eligibility for external surfacing of listed developer products, including Shop and other Roblox surfaces.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/shop): List developer products in Shop to let Roblox surface them outside your game, creating more purchase opportunities. Unlisted products remain purchasable via your own in-game flows.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production): Use Developer Products for repeatable purchases such as in-game currency, since users can buy them multiple times.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/regional-pricing): Before enabling Managed Pricing on developer products, make sure their prices are dynamically scripted via MarketplaceService, not hard-coded in UI.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads): Offer rewards worth roughly 3 to 10 Robux (boosters, currency, extra lives, temporary privileges). Rewards cannot be randomized items.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads): Make rewards relevant to core mechanics, scaled to stay valuable as players progress, and limited-time or rare to boost engagement.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads): Offer rewards at strategic moments such as after losing a life or completing a hard level, at intervals that do not trivialize progression.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/analytics/economy-events): If users aren't sourcing resources from IAP, consider reducing prices or offering new purchase options.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing): Handle purchases atomically: verify, award, and record in ProcessReceipt. Grant the item only after the data save succeeds, or the player gets it free if the save fails.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing): In ProcessReceipt, return NotProcessedYet if the save fails; on the next call check the stored PurchaseId and return PurchaseGranted to avoid double awards.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing): Check hasErrored before allowing purchases, since purchases cannot be saved when the initial data load failed.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/developer-products): Use developer products for repeatable purchases (currency, ammo, potions); use game passes for one-time purchases.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/developer-products): Upload product icons at max 512x512, keep key details inside the circular boundary, and use .jpg, .png or .bmp format.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/developer-products): Implement ProcessReceipt correctly before listing products; do not rely on PromptProductPurchaseFinished to grant items.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/developer-products): In ProcessReceipt, return PurchaseGranted only after the item is actually granted; otherwise return NotProcessedYet so it retries on next join.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/developer-products): Set the ProcessReceipt callback from a single server Script, since it can only be assigned once.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/developer-products): Mark products Listed in Shop and add a custom icon so players recognize them on external surfaces; otherwise Roblox shows a default icon.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/developer-products): Listed products that Roblox flags for ProcessReceipt issues drop out of external surfaces until fixed and marked as fixed in the report.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/developer-products): Call RankProductsAsync once at game join, not repeatedly, because it has a strict rate limit.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/developer-products): Wrap RecommendTopProductsAsync in task.spawn to avoid blocking; filter out products the user can no longer buy.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/developer-products): Track per-user purchase history yourself; Roblox does not record it for developer products.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/resources/modules/merch-booth): Add developer products with addItemAsync(id, Enum.InfoType.Product); product IDs come from Creator Dashboard > Developer Products.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/get-started/strategies): Offer virtual items at multiple price points and a starter pack aimed at new players.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/get-started/strategies): Favor repeatable purchases (consumables) over one-time purchases since spending is not capped.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/analytics): Use GetPlayerSegmentsAsync to show low-cost items to non-spenders and bundles or upgrades to players with purchase history.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/game-design/balance-virtual-economies): A/B test price points and discount strategies with Experiments to find the shop's optimal price zone.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/game-design/balance-virtual-economies): Use Configs to trigger flash sales or adjust economy values in real time without restarting servers.

Index: [[README]] | Master: [[master-playbook]]
