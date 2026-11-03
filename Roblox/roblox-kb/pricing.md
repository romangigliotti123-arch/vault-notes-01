---
title: Pricing
topic: pricing
theme: Monetisation
sources: 235 videos
creators: [1_Bruce, Alex Builds Games, AlvinBlox, ArTheDev, Arow, B Ricey, Bemmy, BrawlDev, BubuTheDev, ByteBlox, CORSO, CallMeDogey, Creators on the Blox, Cumin, Deconstructor of Fun, Duckable, Emancyphur, Erthlord, GameMakers, Generalist Programmer, GnomeCode, ItsZyonic, JustDucksey, Last Level Studios, Lnor Roblox, MonarchDev, MoseyTube, Mulch, Perstile, PineappleDev, PolarBear, ProjectSupreme, Raul, RoDev, RoWatcher (tracker blog), Roblox, Roblox Creator Docs, Roblox Creators, Roblox DevForum, Roblox public API, Seibo, SimTek Game Development, SmartyRBX, Stewiepfing, StudioKrew (agency blog, GGAID data), ThatGuyEvan, TheDankDeveloper, TheDevKing, Tizzy, Ventures, VuukStudios, Where The Money Went, Xaiyne, Yann, bubDEV, janisjanis01, kra_DeZ, rasdev, {EISABOOS} "RBX"]
source_dates: 2018-07-22 to 2026-11-01
tags: [roblox, knowledge-base, pricing]
---

# Pricing

_Robux price points, discounts, anchoring, conversion rate vs price._

Evidence base: 477 extracted items from 235 videos by 1_Bruce, Alex Builds Games, AlvinBlox, ArTheDev, Arow, B Ricey, Bemmy, BrawlDev, BubuTheDev, ByteBlox, CORSO, CallMeDogey, Creators on the Blox, Cumin, Deconstructor of Fun, Duckable, Emancyphur, Erthlord, GameMakers, Generalist Programmer, GnomeCode, ItsZyonic, JustDucksey, Last Level Studios, Lnor Roblox, MonarchDev, MoseyTube, Mulch, Perstile, PineappleDev, PolarBear, ProjectSupreme, Raul, RoDev, RoWatcher (tracker blog), Roblox, Roblox Creator Docs, Roblox Creators, Roblox DevForum, Roblox public API, Seibo, SimTek Game Development, SmartyRBX, Stewiepfing, StudioKrew (agency blog, GGAID data), ThatGuyEvan, TheDankDeveloper, TheDevKing, Tizzy, Ventures, VuukStudios, Where The Money Went, Xaiyne, Yann, bubDEV, janisjanis01, kra_DeZ, rasdev, {EISABOOS} "RBX" (2018-07-22 to 2026-11-01). Roblox changes quickly: check the date on each source and see Date context below.

## Overview
Pricing guidance now stresses audience geography and net revenue. One indie creator (VuukStudios, Oct 2026) reports that halving gamepass and developer product prices for lower-income audiences roughly doubled to about 5x revenue, while another (Perstile, May 2025) argues an underpriced 500 R$ bestseller should cost about 2x more. The evidence suggests the answer depends on who is buying. Developers keep about 70% of player spend, and DevEx cash-out values sit about 3:1 below buy prices, so model net Robux and verify the current DevEx rate. Price game passes above developer products, show localized prices through APIs, and treat 18+ DevEx audiences and temporary surge pricing as situational levers. Budget platform fixed costs (uploads, publishing fee, private servers) before launch.

## Rules and findings
- **There is no pricing formula: start, observe, adjust** (multiple-creators): Pick a starting price, lower it if few buy, raise it on the next version. Treat pricing as something you change. Older (2018) advice, but consistent with later official guidance to test. Sources: [Roblox 2018-07 26:51](https://youtu.be/DWUfL8azgIk?t=1611), [Roblox 2018-07 26:51](https://youtu.be/DWUfL8azgIk?t=1611), [Roblox 2018-07 3:14](https://youtu.be/DWUfL8azgIk?t=194), [Roblox 2024-09 16:58](https://youtu.be/ETDit6eO4sQ?t=1018). Newest source 2024-09-23.
- **Test prices with live data on your own audience** (multiple-creators): Don't copy competitor prices; test to maximise volume × price. Encounters' 650 Robux product converted worse than 400/300/250, yet revenue per user rose at lower prices. One 2018 example reports doubled revenue after changing price points over 3-6 months. Sources: [Roblox 2018-07 3:14](https://youtu.be/DWUfL8azgIk?t=194), [Roblox 2023-09 22:02](https://youtu.be/Z-ZKqBPdl44?t=1322), [Roblox 2024-09 16:58](https://youtu.be/ETDit6eO4sQ?t=1018), [Roblox Creators 2025-12 18:16](https://youtu.be/-CdXP025MvU?t=1096), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/experiments). Newest source 2026-10-28.
- **Use Price Optimization where eligible** (multiple-creators): It auto-tests prices on user subsets and applies prices only when incremental total revenue is positive. Adopt Me saw +3.5% over 12 weeks; Driving Empire saw no uplift because it was already at equilibrium from earlier manual tests. Roblox claims recommended prices come with no engagement loss. Sources: [Roblox 2024-09 31:23](https://youtu.be/ETDit6eO4sQ?t=1883), [Roblox 2024-09 32:44](https://youtu.be/ETDit6eO4sQ?t=1964), [Roblox 2025-09 5:06](https://youtu.be/MJ-zYfL10Ew?t=306), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/get-started/monetization), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/price-optimization). Newest source 2026-10-28.
- **Meet Price Optimization prerequisites and script prices correctly** (one-creator-repeated): Have about 60,000 transactions over the previous 30 days and include all passes and products. Script prices through MarketplaceService, not hard-coded, using GetProductInfo with Enum.InfoType.Product or GamePasses (default fetches assets). Use Dynamic Price Check with up to 5 test accounts to find hard-coded prices, and remove them before opting in. Don't hard-code, so Plus discounts display correctly. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/price-optimization), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/price-optimization), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/price-optimization), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/price-optimization), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/managed-pricing). Newest source 2026-10-28.
- **Know test mechanics** (one-creator-repeated): Tests take about 3 weeks (earlier talk said about 2 weeks) and run at least every 90 days. A 4-week price review period follows, with a 2% control group on original prices. You can stop a test anytime from Managed Pricing, and products revert. Tested prices can't be edited while a test runs. Bulk enable/disable and per-item opt-out are available. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/price-optimization), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/price-optimization), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/managed-pricing), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/price-optimization), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/price-optimization). Newest source 2026-10-28.
- **Set regional prices and mind the bounds** (multiple-creators): Regional pricing sets local prices from purchasing power. Regional prices never exceed your default and never drop more than 70% below it (a 100 Robux default gives a 30 Robux floor), so set the default carefully. Early tests showed spending gains in Mexico, Brazil and the Philippines. Over 5,000 experiences adopted it. Sources: [Roblox 2024-09 18:21](https://youtu.be/ETDit6eO4sQ?t=1101), [Roblox 2024-09 11:45](https://youtu.be/T7w3Q54JOPE?t=705), [Roblox 2025-09 5:06](https://youtu.be/MJ-zYfL10Ew?t=306), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/get-started/monetization), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/regional-pricing). Newest source 2026-10-28.
- **Offer a wide ladder of price points including very cheap ones** (multiple-creators): Many players can't pay much. Include very low options (Griffin's Destiny 35 Robux), cheap-to-very-high developer products (up to ~10,000 Robux), and low-amount currency bundles. Otherwise low-balance players spend Robux elsewhere. Sources: [Roblox Creators 2023-01 21:23](https://youtu.be/vQNJztcS2AI?t=1283), [Roblox Creators 2023-03 0:47](https://youtu.be/Cli3ogW-azk?t=47), [Roblox Creators 2023-03 0:47](https://youtu.be/Cli3ogW-azk?t=47), [CallMeDogey 2025-01 10:14](https://youtu.be/USJC5l_wpuY?t=614), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/analytics/monetization). Newest source 2026-10-28.
- **Keep early offers and impulse items cheap** (multiple-creators): New players rarely spend much in the first 10-30 minutes. Entry items go at roughly 50-400 Robux. Examples: 19 Robux for 2x offline earnings, Spongebob TD starter bundles from 25 to 99 Robux, a 3x speed product, and a tier-1 speed multiplier with 61,000 sales at 5 Robux (self-reported). Progress boosts in brain-rot games stay under 60 Robux (one creator's view). Sources: [Roblox DevForum 2023-12](https://devforum.roblox.com/t/understand-the-roblox-algorithm/2772921), [Tizzy 2026-06 13:50](https://youtu.be/zoz3PSMqets?t=830), [Roblox DevForum 2021-05](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207), [Roblox 2025-09 21:55](https://youtu.be/MJ-zYfL10Ew?t=1315), [Tizzy 2026-06 13:31](https://youtu.be/zoz3PSMqets?t=811). Newest source 2026-10-14.
- **Don't price so low that it breaks the economy** (multiple-creators): Avoid tiny prices like 9 Robux for a cash amount; consumables should earn well but not break the economy, ideally a no-brainer purchase. Sources: [Tizzy 2026-06 13:50](https://youtu.be/zoz3PSMqets?t=830), [MoseyTube 2026-07 2:32](https://youtu.be/-PoyiiGhoNo?t=152), [Tizzy 2026-06 12:09](https://youtu.be/zoz3PSMqets?t=729). Newest source 2026-07-14.
- **Tier prices by purpose and escalate** (single-mention): One DevForum guide: entry 50-400 Robux, gameplay items 400-6000, whale items above 6000. Escalating tiers double the previous price and add 100 (200 for the last), e.g. 450/1000/2200. Raise price per milestone offer. Unverified indie advice. Sources: [Roblox DevForum 2021-05](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207), [Roblox DevForum 2021-05](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207), [Roblox DevForum 2021-05](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207), [Roblox DevForum 2021-05](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207), [Roblox DevForum 2021-05](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207). Newest source 2021-05-17.
- **Keep most items affordable with few expensive exclusives** (multiple-creators): Make a small number of expensive or luxury items and keep the bulk affordable. Leave high-value tiers for scarcity-driven or trading items. Rare items are priced to represent rarity. Sources: [Roblox 2024-09 30:04](https://youtu.be/NEK7jq1LFu8?t=1804), [Roblox 2025-09 26:35](https://youtu.be/MJ-zYfL10Ew?t=1595), [Roblox Creators 2023-01 2:54](https://youtu.be/okAygI1sxsA?t=174), [Roblox Creators 2023-01 2:54](https://youtu.be/okAygI1sxsA?t=174), [Roblox Creators 2025-08 11:52](https://youtu.be/KSez8Ecq50A?t=712). Newest source 2025-09-26.
- **Anchor with an expensive item** (single-mention): Show a very expensive gamepass (e.g. 900 Robux) on join so 100-200 Robux items look like good deals. Stewiepfing cites Adopt Me; this is an indie claim. Sources: [Stewiepfing 2024-02 1:36](https://youtu.be/v8tFfBTr6M8?t=96), [Stewiepfing 2024-02 1:36](https://youtu.be/v8tFfBTr6M8?t=96), [Stewiepfing 2024-02 2:17](https://youtu.be/v8tFfBTr6M8?t=137). Newest source 2024-02-16.
- **Show value per Robux and highlight best value** (multiple-creators): Display effective currency per Robux per bundle (Emergency Response ~214 to ~571 units per Robux) and highlight the best-value bundle with bonus percentages, so players don't do the math. Sources: [Roblox Creators 2023-01 5:07](https://youtu.be/okAygI1sxsA?t=307), [Roblox Creators 2023-01 0:00](https://youtu.be/YdplC2WVkWc?t=0), [Roblox Creators 2023-01 6:32](https://youtu.be/okAygI1sxsA?t=392), [Roblox Creators 2023-01 0:00](https://youtu.be/YdplC2WVkWc?t=0), [Roblox Creators 2023-01 5:50](https://youtu.be/okAygI1sxsA?t=350). Newest source 2023-01-19.
- **Price by time-to-earn** (multiple-creators): Estimate how long an item takes to earn and price at what an hour of a player's time is worth. Price developer product bundles to skip about 3-6 hours of measured earnings. Price higher if you want grinding preferred. Sources: [Roblox Creators 2023-01 0:00](https://youtu.be/YdplC2WVkWc?t=0), [Roblox 2023-09 5:51](https://youtu.be/9eaev-ypgWo?t=351), [Roblox 2026-10 13:11](https://youtu.be/qLP05zvMsW0?t=791), [Roblox 2023-09 5:51](https://youtu.be/9eaev-ypgWo?t=351), [Roblox Creators 2023-01 12:10](https://youtu.be/vQNJztcS2AI?t=730). Newest source 2026-10-12.
- **Start from comparables, adjust for effort and value** (multiple-creators): Compare similar items in other games, your own catalog and what performs. Test new styles first. Price higher for items that took long to make or add a lot to the experience. Use rarity/community value for old items and lower prices for newer items. This only sets a starting point; don't copy comparables blindly (see disagreements). Sources: [Roblox Creators 2023-01 11:26](https://youtu.be/vQNJztcS2AI?t=686), [Roblox 2024-09 28:00](https://youtu.be/NEK7jq1LFu8?t=1680), [Roblox Creators 2023-01 2:54](https://youtu.be/okAygI1sxsA?t=174), [Roblox DevForum 2021-05](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207), [Roblox 2024-09 28:00](https://youtu.be/NEK7jq1LFu8?t=1680). Newest source 2024-09-23.
- **Show offers only when they're good value** (multiple-creators): A poor-value starter pack reduced total spend in Base Battles. Make the main subscription or offer the best on the platform, a no-brainer. Sources: [Roblox 2023-09 19:14](https://youtu.be/Z-ZKqBPdl44?t=1154), [Roblox 2023-09 19:14](https://youtu.be/Z-ZKqBPdl44?t=1154), [Roblox 2024-09 26:39](https://youtu.be/ETDit6eO4sQ?t=1599), [Roblox 2024-09 26:39](https://youtu.be/ETDit6eO4sQ?t=1599). Newest source 2024-09-23.
- **Test starter packs and measure payer conversion** (multiple-creators): Test starter pack price, contents and presentation. Track payer conversion, ARPU and ARPPU. Run welcome/first-purchase discounts to lower barriers. Tizzy reports a roll-teaser change raised pet conversion from 0.3% to 0.75% (self-reported). Sources: [Roblox Creators 2025-12 18:16](https://youtu.be/-CdXP025MvU?t=1096), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/experiments), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/analytics/monetization), [Tizzy 2026-07 16:44](https://youtu.be/nggNvUILQ1I?t=1004), [Tizzy 2026-07 17:26](https://youtu.be/nggNvUILQ1I?t=1046). Newest source 2026-10-28.
- **Keep sales rare and genuine** (multiple-creators): Tie big sales to holidays and pair them with free events for non-payers. Frequent sales train players to wait. Discounts must be genuine: an item permanently 'on sale' at the same price, or a very brief discount, is not allowed. Put slow sellers on limited sale. Don't cut prices just because players ask; respond when many request the same change. Sources: [Roblox 2018-07 15:12](https://youtu.be/DWUfL8azgIk?t=912), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization), [Roblox DevForum 2021-05](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207), [Roblox Creators 2023-01 9:47](https://youtu.be/vQNJztcS2AI?t=587). Newest source 2026-10-28.
- **Pick price by genre and audience** (multiple-creators): Estimate ARPPU by genre before greenlighting (hyper-casual ~$2, tower defense ~$20). Young or low-income audiences need very low prices to keep payer conversion up; target older, higher-income players. Regional bookings per player vary (~$40 US vs ~$6 lowest region). Sources: [Roblox 2025-09 29:17](https://youtu.be/MJ-zYfL10Ew?t=1757), [1_Bruce 2026-02 3:50](https://youtu.be/i3RQXxZeVYc?t=230), [Deconstructor of Fun 2025-04 6:20](https://youtu.be/v_0RADBCTlw?t=380). Newest source 2026-02-20.
- **Price top products to match Robux bundles** (single-mention): 1_Bruce prices top gamepass bundles to equal Robux from a Robux purchase (1,800 Robux for $20) and says it works efficiently (self-reported). Sources: [1_Bruce 2026-03 4:05](https://youtu.be/zgq6L4ZzCHs?t=245), [1_Bruce 2026-03 4:05](https://youtu.be/zgq6L4ZzCHs?t=245), [1_Bruce 2026-03 4:05](https://youtu.be/zgq6L4ZzCHs?t=245). Newest source 2026-03-15.
- **Use cheap rerolls** (single-mention): Offer rerolls at about 4-5 Robux on crates so players keep rerolling; Alex Builds Games says it was a main earner (self-reported). Crates observed from 199 to 1,900 Robux. Sources: [Alex Builds Games 2026-06 14:48](https://youtu.be/x_SflcuSi1w?t=888), [Alex Builds Games 2026-06 14:48](https://youtu.be/x_SflcuSi1w?t=888), [Alex Builds Games 2026-06 14:48](https://youtu.be/x_SflcuSi1w?t=888), [Alex Builds Games 2026-06 12:46](https://youtu.be/x_SflcuSi1w?t=766). Newest source 2026-06-16.
- **Prorate prices by progression** (multiple-creators): Scale soft-currency bundle and timer-skip prices down as players advance (e.g. 25 Robux early to 1 Robux at level 50, a hypothetical). To slow consumption, add level gates or raise soft-currency prices instead of blocking players. Sources: [Roblox Creators 2021-08 26:01](https://youtu.be/4-vZkSrGAxI?t=1561), [Roblox Creators 2021-10 57:57](https://youtu.be/d4g30UupgKw?t=3477), [Roblox Creators 2021-08 26:42](https://youtu.be/4-vZkSrGAxI?t=1602). Newest source 2021-10-21.
- **Price avatar/UGC items relative to the price floor** (multiple-creators): Price = floor + offset, with optional minimum sales price (both editable after creation). Rush prices at the floor because buyers compare; luxury items can be higher. Pricing above the floor can qualify for up to 70% revenue share instead of 30%. Emissive UGC has a higher floor by design. Buy multiple tokens for multiple price points. Until a publishing advance is recouped you earn 70%; a 1,500 Robux hat at 95 Robux needs about 22-23 sales. Sources: [Roblox 2024-09 7:26](https://youtu.be/NEK7jq1LFu8?t=446), [Roblox Creators 2025-08 11:52](https://youtu.be/KSez8Ecq50A?t=712), [Roblox Creators 2025-08 11:52](https://youtu.be/KSez8Ecq50A?t=712), [Roblox 2025-09 18:30](https://youtu.be/Tese1QLD3nU?t=1110), [Roblox 2026-10 18:23](https://youtu.be/gCp4zzjjJ14?t=1103). Newest source 2026-10-28.
- **Release a free hero item, price the recolor** (single-mention): Release one major item free to build hype and price a recolor, which Rush says often sells higher and lifts the set. Sources: [Roblox Creators 2025-08 11:52](https://youtu.be/KSez8Ecq50A?t=712). Newest source 2025-08-15.
- **Subscription pricing constraints** (multiple-creators): Pick a price you can hold (Adopt Me $2.99). Robux subscriptions: minimum 49 Robux, change once per 60 days, increases need 30 days' notice, decreases apply at next renewal. Local-currency tiers: $2.99, $4.99, $7.99, $9.99, $14.99; can't be changed, so delete and recreate. A price change cancels all active subscriptions (as listed in the docs). Sources: [Roblox 2024-09 26:39](https://youtu.be/ETDit6eO4sQ?t=1599), [Roblox DevForum 2026-04](https://devforum.roblox.com/t/let-your-players-pay-for-subscriptions-within-experiences-in-robux/4552995), [Roblox DevForum 2026-04](https://devforum.roblox.com/t/let-your-players-pay-for-subscriptions-within-experiences-in-robux/4552995), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/subscriptions), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/subscriptions). Newest source 2026-10-28.
- **Respect platform price limits** (one-creator-repeated): Developer products 1 to 1,000,000,000 Robux. Paid access 25-1000 Robux. Models $2.99-$49.99, plugins $4.99-$249.99. Discounts don't apply above 1,000,000 Robux. Promoted on-sale passes must be 50-800 Robux. Paid private server price determines per-sale earnings. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/developer-products), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/paid-access-robux), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/creator-store), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/private-servers), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/developer-products). Newest source 2026-10-28.
- **Price currency packs and guaranteed items consistently** (single-mention): Compare a new currency pack to existing Robux offerings for consistent relative value (doc calculation uses roughly $1 USD per Robux). For direct purchase for restricted users, price a guaranteed item at expected value: a 10 Robux box at 5% odds implies 200 Robux. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/game-design/subscription-design), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/game-design/subscription-design), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/game-design/subscription-design), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/paid-random-items), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/paid-random-items). Newest source 2026-10-28.
- **Set rewarded-ad reward value carefully** (multiple-creators): Around 3-10 Robux equivalent so players don't abandon mid-ad; 30 seconds of watching must feel worth it without cannibalising purchases. Sources: [Roblox Creators 2025-08 17:45](https://youtu.be/7AtvvUxvCaU?t=1065), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/promotion/rewarded-video-playbooks/tycoon), [Roblox Creators 2025-08 18:26](https://youtu.be/7AtvvUxvCaU?t=1106). Newest source 2026-10-28.
- **Constrain supply in trading games** (single-mention): Use pricing to limit supply so monetized items hold value; Adopt Me considers resale value. Example: legendary pet at 1,000 Robux. Sources: [Roblox 2025-09 25:54](https://youtu.be/MJ-zYfL10Ew?t=1554), [Roblox 2025-09 15:06](https://youtu.be/MJ-zYfL10Ew?t=906). Newest source 2025-09-26.
- **Run a half-price first week to read real conversion and ARPPU** (single-mention): Yann advises selling gamepasses and products at roughly half price in the first week to get a realistic payer conversion rate and ARPPU from ad traffic. Use it as a measurement window, then adjust toward the target price. Self-reported; no benchmark figures given. Sources: [Yann 2026-05 6:48](https://youtu.be/yw32DZtz4mQ?t=408). Newest source 2026-05-30.
- **Raise prices once demand is proven** (one-creator-repeated): Cheap early pricing boosts payer conversion, but Yann says at peak they could probably have doubled prices and sales would still have held. Once traffic and conversion are measured and stable, test higher prices rather than staying at launch-level prices. Sources: [Yann 2026-05 2:44](https://youtu.be/dbNA3K8lt2w?t=164), [Yann 2026-05 2:44](https://youtu.be/dbNA3K8lt2w?t=164). Newest source 2026-05-12.
- **Guarantee a minimum sale price with Do Not Price Below** (single-mention): Set price as Amount Above Price Floor (default 0 Robux, required) plus optional Do Not Price Below to guarantee a minimum sale price. Example: floor 50 plus 5 above floor gives a 55 Robux price. Official docs. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/marketplace/publish-to-marketplace), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/marketplace/publish-to-marketplace). Newest source 2026-10-28.
- **Model dev share and total cost before committing to a price** (multiple-creators): Speakers report only a fraction of spend reaches the developer (about 21% of a $5 purchase in one breakdown). A failed game cost about 38,000 Robux net (10,000 purchase plus 18,000 ads plus 10,000 developers). Work out net revenue and total cost, not gross Robux, before setting price or ad budget. Sources: [rasdev 2026-10 1:10](https://youtu.be/53OBGXktIPY?t=70), [janisjanis01 2025-09 13:47](https://youtu.be/YVKHlrlWn-k?t=827). Newest source 2026-10-20.
- **Price game passes above developer products** (single-mention): Game passes are bought once and must earn their lifetime revenue, so price them higher than consumable developer products. Keep cheap, repeatable developer products for impulse buys. This is consistent with tiering by purpose. Sources: [VuukStudios 2024-08 2:39](https://youtu.be/3J7Vp6NgYf4?t=159). Newest source 2024-08-30.
- **Match gamepass and dev product prices to the player country mix** (one-creator-repeated): Check which countries play most. If the audience is mostly lower-income or low-spending regions, high Robux prices cut conversion sharply. VuukStudios halved prices for a Mexico-heavy audience and saw about 5x revenue; another test saw over 2x. Test before committing, because one creator's data is not a universal rule. Sources: [VuukStudios 2026-08 7:22](https://youtu.be/aw0PmBkakb4?t=442), [VuukStudios 2026-08 9:42](https://youtu.be/Tk0qXybUK0E?t=582), [VuukStudios 2026-10 3:42](https://youtu.be/4vuXAQt0PuQ?t=222), [VuukStudios 2026-10 5:45](https://youtu.be/4vuXAQt0PuQ?t=345), [VuukStudios 2026-10 4:20](https://youtu.be/0ENzqNB_EUo?t=260). Newest source 2026-10-11.
- **Show per-player localized prices via API** (multiple-creators): Prices vary by region and subscription. Use GetSubscriptionProductInfoAsync from a LocalScript for subscription display prices, or Data.ObserveProductInfo for per-player product prices. Roblox Plus subscribers pay 10 to 20% less, and regional prices can drop to 30% of list (N5316). Example: $14.99 shown as $2.99 to a Canadian viewer. Sources: [ByteBlox 2024-04 5:15](https://youtu.be/7NRp4BEYrsQ?t=315), [Roblox DevForum 2026-07](https://devforum.roblox.com/t/scribe-v261-persistent-typed-auto-replicated-player-data-built-on-profilestore/4738905), [ByteBlox 2024-04 6:18](https://youtu.be/7NRp4BEYrsQ?t=378), [Roblox DevForum 2026-07](https://devforum.roblox.com/t/scribe-v261-persistent-typed-auto-replicated-player-data-built-on-profilestore/4738905). Newest source 2026-07-15.
- **Use an 18+ DevEx audience only if the game suits older players** (single-mention): 18+ DevEx-qualified users yield about 42% more per Robux than the standard rate, but the qualified audience is smaller. Choose it only when the game's content and audience actually fit. Weigh 42% uplift against lower player counts. Sources: [VuukStudios 2026-09 4:04](https://youtu.be/2Q4NqQikzsY?t=244), [VuukStudios 2026-09 4:04](https://youtu.be/2Q4NqQikzsY?t=244). Newest source 2026-09-01.
- **Raise prices temporarily during traffic surges, then revert** (single-mention): During a major promotion or push, raise gamepass and developer product prices to capture high-intent demand. Revert to normal prices once traffic settles so long-term conversion and player trust are preserved. Sources: [VuukStudios 2026-09 5:26](https://youtu.be/2Q4NqQikzsY?t=326). Newest source 2026-09-01.
- **Verify the current DevEx rate before modeling revenue** (multiple-creators): Indie reports disagree on DevEx value per Robux: about $12 per 5,000 R$ (mid-2024), about $1 per 1,000 R$ (late 2024), and about $380 per 100,000 R$ (mid-2026, roughly $0.0038 per R$). Pull the current rate from DevHub and model with it, not with older figures. Sources: [VuukStudios 2024-07 2:10](https://youtu.be/NfXvHlAdIsI?t=130), [VuukStudios 2024-12 12:06](https://youtu.be/xBPJnMgLoUE?t=726), [VuukStudios 2024-12 12:06](https://youtu.be/xBPJnMgLoUE?t=726), [Generalist Programmer 2026-07 0:00](https://youtu.be/vbzFbOUGERA?t=0), [Generalist Programmer 2026-07 5:53](https://youtu.be/9mV423C2aXU?t=353). Newest source 2026-07-03.
- **Model net Robux, not gross spend** (multiple-creators): Players spend Robux, but developers keep roughly 70% after the marketplace cut. A 1,000 R$ spend yields about 700 earned R$, about $2.66 at 2026 DevEx rates. Buying Robux costs about 1.25 cents per R$ (400 R$ for $4.99), versus DevEx payout about 3:1 lower. Price the item against net value. Sources: [Generalist Programmer 2026-07 5:23](https://youtu.be/CFohgybeybM?t=323), [Generalist Programmer 2026-07 5:23](https://youtu.be/CFohgybeybM?t=323), [Generalist Programmer 2026-07 0:59](https://youtu.be/vbzFbOUGERA?t=59), [Generalist Programmer 2026-07 2:06](https://youtu.be/vbzFbOUGERA?t=126), [Generalist Programmer 2026-07 0:00](https://youtu.be/vbzFbOUGERA?t=0). Newest source 2026-07-03.
- **Price commissions by hourly rate plus a complexity premium, then tune the rate** (multiple-creators): Use hourly rate x estimated hours x (1 + complexity premium). Example: $15/hr x 6 hrs with a 30% premium = $117 (about 30k R$). Then raise or lower the rate per job until total earnings and number of commissions are both maximized. Sources: [Roblox DevForum 2021-03](https://devforum.roblox.com/t/developing-expert-developers-advice-from-all-around-the-world/1134437), [Roblox DevForum 2021-03](https://devforum.roblox.com/t/developing-expert-developers-advice-from-all-around-the-world/1134437), [Arow 2025-05 0:45](https://youtu.be/JeBDqH7INjY?t=45), [VuukStudios 2026-02 10:53](https://youtu.be/JQqhUWZUGDQ?t=653). Newest source 2026-02-10.
- **Re-check best sellers for underpricing** (single-mention): A high-volume product may be underpriced. One creator says a 500 R$ double-size product should have cost more, estimating about 2x revenue at a higher price. Test a higher price on bulkier items before assuming current pricing is right. Sources: [Perstile 2025-05 2:14](https://youtu.be/ET3fRqaFmFc?t=134). Newest source 2025-05-30.
- **Budget platform fixed costs before launch** (multiple-creators): Known costs include a 2,000 R$ upload per video, a one-time refundable 1,000 R$ publishing fee per game (alternative to Plus/Premium for all-ages publishing), and private servers around $1 USD (about 100 R$) per month. Budget these before adding content or charging. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/ui/video-frames), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/ui/video-frames), [Roblox DevForum 2026-04](https://devforum.roblox.com/t/new-publishing-requirements-evaluation-process-for-games/4573166), [Roblox DevForum 2026-05](https://devforum.roblox.com/t/alternate-publishing-requirements-for-roblox-kids-and-select/4630944), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/education/educator-onboarding/3-setting-up-a-roblox-classroom). Newest source 2026-10-28.
- **Treat spend-linked odds as a pricing lever, with caution** (single-mention): One developer reduces chance for loyal spenders after about 4,000 R$ spent, a lever that shapes the spend curve. Before using it, check current Roblox policy on odds and disclosure. This is a single-source tactic. Sources: [ByteBlox 2025-02 16:44](https://youtu.be/o-8V99horro?t=1004). Newest source 2025-02-01.
- **Never change a VIP or private server price after sales start** (multiple-creators): Changing the price cancels existing subscriptions and upsets buyers. Mulch kept 50 Robux since launch for this reason. The minimum price is 10 Robux, and free has been allowed since a 2020 update (newer than the 2018 claim). Decide the price before the first sale. Sources: [Emancyphur 2018-07 7:15](https://youtu.be/RUqr6lj1UYI?t=435), [Mulch 2024-06 4:10](https://youtu.be/pqCXX06vlDw?t=250), [Mulch 2024-06 4:10](https://youtu.be/pqCXX06vlDw?t=250), [Emancyphur 2018-07 0:45](https://youtu.be/RUqr6lj1UYI?t=45), [Mulch 2024-06 3:28](https://youtu.be/pqCXX06vlDw?t=208). Newest source 2024-06-30.
- **Judge each price change by total revenue, not sales count** (single-mention): Track gamepass revenue day by day after any price cut or rise. A price change can raise sales but lower total Robux, or the reverse. Compare the days before and after the change. Sources: [Last Level Studios 2020-02 36:19](https://youtu.be/_LdpUJ41cso?t=2179). Newest source 2020-02-14.
- **Consider turning off regional pricing on donation-style passes** (one-creator-repeated): EISABOOS (2025-12, most recent) says regional pricing can misbehave and let some countries pay fewer Robux, e.g. 10 Robux US became 4 Robux in lower-income countries. Turn it off for donation passes if you want uniform prices. Keep it on only if broader affordability is the goal. Sources: [{EISABOOS} "RBX" 2025-08 1:28](https://youtu.be/5dfKSg_wqLA?t=88), [{EISABOOS} "RBX" 2025-12 3:02](https://youtu.be/skRRdrpf2F4?t=182), [{EISABOOS} "RBX" 2025-12 3:02](https://youtu.be/skRRdrpf2F4?t=182), [{EISABOOS} "RBX" 2025-08 1:00](https://youtu.be/5dfKSg_wqLA?t=60), [{EISABOOS} "RBX" 2025-12 3:02](https://youtu.be/skRRdrpf2F4?t=182). Newest source 2025-12-04.
- **Test odd-number price points as an experiment, not a default** (one-creator-repeated): PolarBear says 199 Robux looks cheaper and more appealing than 200 Robux. The claim is self-reported and untested against controlled data. Run an A/B-style comparison on your own audience before adopting it. Sources: [PolarBear 2024-02 2:02](https://youtu.be/nkmfdUbj4bQ?t=122), [PolarBear 2024-02 2:02](https://youtu.be/nkmfdUbj4bQ?t=122). Newest source 2024-02-02.
- **Compare real-dollar channels against Robux when developer share matters** (single-mention): One creator claims about 70% of proceeds from real-dollar sales (Creator Store, paid access) versus about 27% through DevEx. Treat as unverified. Verify the current DevEx rate and fees before choosing a channel. Sources: [Where The Money Went 2026-10 12:58](https://youtu.be/cJHug1Wnmhw?t=778). Newest source 2026-10-01.
- **Benchmark against live gamepass ladders, not a fixed floor** (one-creator-repeated): Public API snapshots show gamepass price ranges vary widely by game: 9–4999 (40 on sale), 19–2999 (46 on sale), 30–150, 49–399, and 50–999 (12 passes). Pull the list for your genre and set tiers from its clusters, not from one game's min or max. Sources: [Roblox public API 2026-11](https://www.roblox.com/games/95082159892680/), [Roblox public API 2026-11](https://www.roblox.com/games/114697347887839/), [Roblox public API 2026-11](https://www.roblox.com/games/119958473240233/), [Roblox public API 2026-11](https://www.roblox.com/games/95168737547508/), [Roblox public API 2026-11](https://www.roblox.com/games/121864768012064/). Newest source 2026-11-01.
- **Anchor gamepass tiers on the 75 / 99 / 149 clusters** (one-creator-repeated): Observed common tiers are 75 Robux (5 max-stat passes), 99 (2x Cash, 4th Tool Slot), and 149 (All Upgrades Maxed, 5th Tool Slot; a 2x Emotes pass also sold at 149). Start there, then test non-round neighbors as an experiment. Sources: [Roblox public API 2026-11](https://www.roblox.com/games/119958473240233/), [Roblox public API 2026-11](https://www.roblox.com/games/93978595733734/). Newest source 2026-11-01.
- **Price VIP in the 175–199 band with a top VIP+ near 888** (one-creator-repeated): Sampled VIP passes sit at 199 and 175 Robux. The most expensive gamepass seen was VIP+ at 888 Robux. Use a single mid-band VIP as the entry bundle, and add a higher VIP+ tier only if the game can deliver enough extra value to justify it. Never change VIP price after sales start (existing rule). Sources: [Roblox public API 2026-11](https://www.roblox.com/games/95168737547508/), [Roblox public API 2026-11](https://www.roblox.com/games/131623223084840/), [Roblox public API 2026-11](https://www.roblox.com/games/131623223084840/). Newest source 2026-11-01.
- **Price permanent stat boosts above the entry tiers** (single-mention): An indie tracker lists a permanent 150% luck boost at 545 Robux, well above the common 75–149 tiers. Treat permanent, high-impact boosts as premium items. This is a single self-reported data point, so validate it against your own conversion data. Sources: [RoWatcher (tracker blog) 2026-00](https://rowatcher.com/news/fish-it-reels-in-270k-players-inside-roblox-s-most-addictive-casual-game-of-2026). Newest source 2026-00-00.
- **Fund platform costs from wallet at the DevEx repurchase rate** (single-mention): Wallet holders can buy Robux at the DevEx rate of $0.0038/Robux to pay for publishing, testing and ads, instead of buying back at retail. Example: 10,000 Robux for $38; 30,000 Robux for $114, plus tax. This is a cost you pay, not your developer payout, so keep it separate when modeling net revenue. Sources: [Roblox DevForum 2026-09](https://devforum.roblox.com/t/introducing-roblox-wallet-and-card-get-paid-faster/4865505), [Roblox DevForum 2026-09](https://devforum.roblox.com/t/introducing-roblox-wallet-and-card-get-paid-faster/4865505). Newest source 2026-09-11.
- **Make each upgrade step's gain visible on its price** (single-mention): In progression upgrades (speed multipliers, earnings boosts), show the resulting earnings increase next to each tier so the player can see what each Robux step buys. The creator argues visible gains encourage spending on the next step. Sources: [Mulch 2026-09 1:18](https://youtu.be/WYODms_JMRA?t=78). Newest source 2026-09-12.
- **Price bulk and convenience actions above the single-unit price** (one-creator-repeated): In one indie game, a single pet/egg purchase cost 140 Robux and the bulk 'grow all' action cost 184 Robux (about 1.31x). The bulk action is priced as a premium convenience. Treat this as one data point, not a formula. Sources: [Mulch 2026-09 9:22](https://youtu.be/U2IjSOyNTB8?t=562), [Mulch 2026-09 10:44](https://youtu.be/U2IjSOyNTB8?t=644). Newest source 2026-09-09.
- **Do not use guessed or off-topic prices as benchmarks** (single-mention): Speaker-guessed prices for non-Roblox products (e.g., an amiibo guessed at ~$50) are not pricing data. Benchmark only against live Roblox listings, your own sales, or platform data. Sources: [Cumin 2026-09 0:00](https://youtu.be/kYwCqstp9eA?t=0). Newest source 2026-09-09.
- **Turn Sales on before entering a game pass price** (single-mention): To set a game pass price, open the pass in the Creator Dashboard, turn Sales on, then enter the price. This is a setup step, not a pricing decision. Confirm the toggle state in the current UI, since the dashboard layout changes over time. Sources: [ArTheDev 2025-02 3:14](https://youtu.be/JtZ8RzQaQco?t=194). Newest source 2025-02-06.
- **Keep item sell values in one shop items module** (single-mention): Store item sell values (for example Value in the shop items module) in one central config rather than hard-coding them per item. This makes it easier to rebalance the economy in one place when prices change. Sources: [GnomeCode 2025-05 6:22](https://youtu.be/2jcCCIcxvdk?t=382), [GnomeCode 2025-05 6:22](https://youtu.be/2jcCCIcxvdk?t=382). Newest source 2025-05-25.
- **Tune economy sources/sinks and difficulty alongside prices** (single-mention): GameMakers reports that sources/sinks and difficulty tuning gave LTV lifts of up to ~20% and ~10% for modest effort, and says to prioritise these tests. Run them before or alongside price tweaks, and judge both by LTV. Self-reported, one creator. Sources: [GameMakers 2022-08 30:52](https://youtu.be/JVCao-Yhu2M?t=1852), [GameMakers 2022-08 30:52](https://youtu.be/JVCao-Yhu2M?t=1852). Newest source 2022-08-30.
- **Start icon and thumbnail services at a flat per-deliverable price** (single-mention): PolarBear suggests starting icon design at ~250 Robux per icon and thumbnails at about 1000 Robux or $5 (a prior offer). Raise prices as the portfolio and reputation grow. This is a flat-rate method, unlike the hourly-plus-premium commission rule. Low-advice, one creator, 2024-07. Sources: [PolarBear 2024-07 7:28](https://youtu.be/tkAis2wTxms?t=448), [PolarBear 2024-07 7:28](https://youtu.be/tkAis2wTxms?t=448), [PolarBear 2024-07 6:48](https://youtu.be/tkAis2wTxms?t=408). Newest source 2024-07-19.
- **Sell currency in bundles that leave a surplus** (single-mention): Price bundles so a typical purchase leaves a small leftover. The speaker's view is that players tend to spend the remainder rather than let it go to waste. Example from the source: 1000 gems for 400 Robux, where spending 300 gems feels like nothing. Self-reported, not measured. Sources: [rasdev 2026-04 2:41](https://youtu.be/yFKY2FlwHjE?t=161), [rasdev 2026-04 2:41](https://youtu.be/yFKY2FlwHjE?t=161). Newest source 2026-04-30.
- **Fix a weak economy with a global multiplier buff before repricing** (one-creator-repeated): When the economy feels weak, raise most pet multipliers by about 25% (some by 10%, with a 30% target) rather than cutting prices. The speaker's stated reason is that the game 'could be balanced a little better.' Indie, self-reported, single case. Sources: [janisjanis01 2024-12 9:20](https://youtu.be/Jc7yQTMFexk?t=560), [janisjanis01 2024-12 9:20](https://youtu.be/Jc7yQTMFexk?t=560), [janisjanis01 2024-12 9:20](https://youtu.be/Jc7yQTMFexk?t=560). Newest source 2024-12-01.
- **Offer a direct Robux shortcut beside grindable or craftable items** (single-mention): Mulch quoted a Long Boy pet at 650 Robux as a direct purchase alternative to crafting it. Where an item takes long to craft or earn, a Robux option lets players skip the grind. Set the Robux price against the in-game grind time so the shortcut is worth buying but does not make the grind pointless. Sources: [Mulch 2024-11 1:23](https://youtu.be/axxmwooE-J0?t=83). Newest source 2024-11-23.

## Checklist
- [ ] Estimate cost, expected earnings and ARPPU for your genre before building
- [ ] Script all prices via MarketplaceService; never hard-code
- [ ] Fetch with InfoType.Product / InfoType.GamePasses
- [ ] Run Dynamic Price Check to find hard-coded prices
- [ ] Build a price ladder from very cheap (about 25-100 Robux) to whale tiers
- [ ] Add a very low entry option, e.g. 35 Robux or less
- [ ] Price entry items for new players' first 10-30 minutes
- [ ] Price bundles to skip about 3-6 hours of measured earnings
- [ ] Show currency per Robux and highlight the best-value bundle
- [ ] Consider an expensive anchor item shown early
- [ ] Compare similar games for a starting point, then test on your own audience
- [ ] Set the default global price carefully, since regional prices are 30-100% of it
- [ ] Opt in to regional pricing and review recommendations
- [ ] Reach about 60,000 transactions/30 days, then run Price Optimization with all products included
- [ ] Review results and the 4-week price review period
- [ ] Test starter pack price, contents and presentation
- [ ] Track payer conversion, ARPU and ARPPU
- [ ] Offer first-purchase welcome discounts
- [ ] Keep sales rare and tied to events; make discounts genuine
- [ ] Keep subscription price changes to once per 60 days with 30 days' notice for increases
- [ ] Use the 49 Robux minimum or approved local tiers for subscriptions
- [ ] For UGC, decide floor offset and minimum price; consider pricing above the floor for higher revenue share
- [ ] Check rewarded-ad value of 3-10 Robux
- [ ] Make sure low prices don't undercut the in-game economy
- [ ] Launch the first week at roughly half the target price for gamepasses and products to measure conversion and ARPPU from ad traffic (T6538).
- [ ] After conversion and ARPPU are stable at the test price, test a higher price to see whether sales hold (T6508, Q1032).
- [ ] When setting a guaranteed minimum sale price, use Amount Above Price Floor (default 0) plus Do Not Price Below.
- [ ] Keep animation pack prices at or above the 300 Robux marketplace floor (T9771, N3869).
- [ ] Set plugin prices at or above the $4.99 USD minimum (N3179).
- [ ] Before pricing an avatar item above its floor, check the progressive creator share table so the price step is worth the share gain (N3512, T8663).
- [ ] Remember that in-game sales stay at 30% creator share even when marketplace share rises (T8663).
- [ ] For Creator Store products, set Money exponent to -9 (N3322).
- [ ] Cap free Limited publishing at 50 per day when enabling free Limiteds on sale (N3800).
- [ ] Compare your price against comparable products in the same genre before setting a Robux price (N2408, N2487, N2652, N3260).
- [ ] Model dev share and total cost (ads plus purchase) before committing to a large buy-in (N2946, N2655).
- [ ] Pull player country breakdown from analytics before setting gamepass or dev product prices.
- [ ] If most players are from lower-income countries, test halved prices against current prices and compare revenue over at least 72 hours.
- [ ] Price game passes above developer products; keep developer products cheap and repeatable.
- [ ] Check current DevEx rate on DevHub and model revenue with it, not old figures.
- [ ] Calculate net earned Robux (about 70% of spend) before comparing prices.
- [ ] Compare the buy price (about 1.25 cents per R$ for standard packs) with DevEx payout (about 0.38 cents per R$ in 2026).
- [ ] Use GetSubscriptionProductInfoAsync or Data.ObserveProductInfo to show localized prices to each player.
- [ ] Check the Roblox Plus 10 to 20% discount when setting display prices.
- [ ] Decide on 18+ DevEx qualification only if game content suits older players, weighing 42% uplift against fewer players.
- [ ] Plan temporary price increases for big promotional traffic, with a scheduled reversion date.
- [ ] For commissions, compute hourly rate x hours x (1 + complexity premium) as a baseline.
- [ ] Adjust commission rates per job and track both total earnings and job count.
- [ ] Re-check your best seller for underpricing by testing a higher price on bulkier items.
- [ ] Budget 2,000 R$ per video upload and 1,000 R$ one-time publishing fee before adding content.
- [ ] Budget private server fees (about $1 per month) if offering them.
- [ ] Simulate progression and economy math before launch; a free egg was hit 130 times (about $6,500 in 30 seconds).
- [ ] Keep sales rare; a 25% sitewide discount is an example pattern from official docs.
- [ ] Use 1 R$ test gamepasses when testing purchase flows (existing mechanic, reconfirmed).
- [ ] Verify Premium Payouts rates on DevHub; they have changed multiple times.
- [ ] Check transfer caps (500 R$/day, 1,000 R$/month) if your game uses transfers.
- [ ] Track ARPDAU and conversion; one creator called 0.15 ARPDAU poor, but currency units were unclear.
- [ ] Check your competitor's price before pricing a kit or template (examples: $24 kit, $40 and $20 competitor products).
- [ ] Do not cut prices to match a competitor's free version without checking your own conversion data.
- [ ] Before changing a private server or VIP price, check whether servers exist; if they do, expect subscription cancellations.
- [ ] Set the private server or VIP price before launch and keep it fixed.
- [ ] Log gamepass revenue daily for at least several days before and after every price change.
- [ ] Audit the 'Use regional pricing' toggle on each donation-style game pass.
- [ ] Keep a cheap entry pass (around 29 Robux, e.g. a custom name pass) alongside larger passes.
- [ ] Keep most gamepasses in the roughly 10 to 150 Robux band; reserve high prices for a few exclusives.
- [ ] Test odd-number price points (e.g. 199) against round ones before adopting them.
- [ ] Turn off PBR in the generator before uploading to Roblox, since PBR costs extra Robux to upload.
- [ ] Check the current ad credit price before budgeting Ads Manager spend (speaker reported 285 Robux per credit in 2024).
- [ ] Start ad campaigns with a small test budget before a full send; one creator spent about 8,000 Robux over 6 days with no prior testing.
- [ ] Compare ad bids against Roblox's suggested range and your own test results rather than trusting the suggestion blindly.
- [ ] Verify the current DevEx rate before modelling real-dollar versus Robux revenue.
- [ ] Check whether real-dollar channels (Creator Store, paid access) suit your game before committing.
- [ ] Use per-item floors for small cosmetics (emotes reportedly have a 50 Robux minimum) and check current platform limits.
- [ ] Confirm rebirth or progression Robux costs step up gradually; one creator called +5 rebirth at 50 Robux too high versus +1 at 15 Robux.
- [ ] Before setting gamepass tiers, export the public gamepass list for 3–5 games in your genre and record the clustered price points, not just min and max.
- [ ] Start gamepass tiers at the 75 / 99 / 149 clusters where they fit your item value, then test one non-round neighbor per tier as an experiment.
- [ ] Price the main VIP pass at 175–199 Robux and decide whether a VIP+ tier (reference point 888) is justified by real extra value.
- [ ] Price permanent boosts above the entry band (reference point 545) and compare their total revenue against consumable boosts.
- [ ] Before modeling DevEx revenue, confirm the current rate on the Roblox DevEx page (0.0038 per earned Robux; 0.0054 for eligible 18+ US spend, effective June 8, 2026).
- [ ] If you need Robux for publishing, testing or ads, buy from the wallet at the DevEx repurchase rate ($0.0038/Robux) rather than at retail, and include tax in the budget (T17652, N7522).
- [ ] When budgeting UGC avatar item iteration, count 750 Robux per accessory test upload during plugin development (N7545).
- [ ] When modeling net revenue, track wallet repurchase spend as a cost separately from DevEx payout income.
- [ ] If your game has multi-tier speed or earnings multipliers, list each tier's Robux price and the earnings gain it provides before publishing.
- [ ] For bulk or convenience actions (grow all, open-all), compare the bulk price to the single-unit price and check it is priced as a premium, not a discount, unless you intend a bundle discount.
- [ ] Record real price points from live games in your genre as your comparables, rather than relying on speaker guesses.
- [ ] Open each game pass in the Creator Dashboard, turn Sales on, then enter the price (T18184).
- [ ] Keep in-game sell values (gold bar 50, coal 10) in the shop items module so they can be tuned in one place (N7805, N7806).
- [ ] Set in-game location prices in coins as a two-tier pair (Location 1 = 100, Location 2 = 250) and check the gap is intentional (N7809).
- [ ] Before pricing a Robux-denominated icon or thumbnail service, set a starting flat price (~250 Robux per icon) and note portfolio size so you can plan raises.
- [ ] Schedule an economy sources/sinks and difficulty tuning test before your next price change, and compare LTV across both.
- [ ] Re-check the DevEx rate from a current source at the time of modeling, and do not rely on a single creator's per-1K figure without recomputing it.
- [ ] If a Robux price feels wrong because the economy is weak, check reward multipliers first. One indie fix was a ~25% global pet-multiplier buff (T18842, N8088).
- [ ] Build currency bundles so the leftover after typical purchases is small but real, then watch whether leftovers drive a second purchase (T18937, N8138).
- [ ] Budget 100 Robux per badge created in launch costs (N8136).
- [ ] Limit gamepass discounts to a defined seasonal window (e.g., 50% off during a holiday) and return to full price afterward (T18855, N8096, N8092).
- [ ] If an item can be crafted or grinded, compare its Robux shortcut price with the in-game time or resource cost before setting it.
- [ ] When quoting in-game values for pricing reference, label them as indie self-reported figures unless verified in-game.

## Numbers and benchmarks

| Metric | Value | Context | Sources |
|---|---|---|---|
| Entry item price range | 50-400 Robux | DevForum indie guide (unverified) | [Roblox DevForum 2021-05](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207), [Roblox DevForum 2021-05](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207) |
| Gameplay item range / whale threshold | 400-6000 Robux / >6000 Robux | DevForum indie guide | [Roblox DevForum 2021-05](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207), [Roblox DevForum 2021-05](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207) |
| Escalating gun tiers | 450 / 1000 / 2200 Robux | double previous +100 (+200 last) | [Roblox DevForum 2021-05](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207), [Roblox DevForum 2021-05](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207) |
| Bundle pricing | about 3-6 hours of average earnings | Roblox official | [Roblox 2023-09 5:51](https://youtu.be/9eaev-ypgWo?t=351), [Roblox 2023-09 5:51](https://youtu.be/9eaev-ypgWo?t=351) |
| Currency per Robux | ~214 to ~571 | Emergency Response tiers | [Roblox Creators 2023-01 6:32](https://youtu.be/okAygI1sxsA?t=392), [Roblox Creators 2023-01 0:00](https://youtu.be/YdplC2WVkWc?t=0) |
| Lowest Robux option | 35 Robux | Griffin's Destiny | [Roblox Creators 2023-01 21:23](https://youtu.be/vQNJztcS2AI?t=1283), [Roblox Creators 2023-03 0:47](https://youtu.be/Cli3ogW-azk?t=47), [Roblox Creators 2023-01 21:23](https://youtu.be/vQNJztcS2AI?t=1283) |
| Price Optimization uplift | +3.5% over 12 weeks (Adopt Me); none for Driving Empire | official | [Roblox 2024-09 31:23](https://youtu.be/ETDit6eO4sQ?t=1883), [Roblox 2024-09 32:44](https://youtu.be/ETDit6eO4sQ?t=1964) |
| Larger cash packs revenue/user | +8% sustained | Driving Empire | [Roblox 2023-09 18:34](https://youtu.be/Z-ZKqBPdl44?t=1114) |
| Price optimization transactions threshold | 60,000 per previous 30 days | docs | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/price-optimization), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/price-optimization) |
| Test duration / frequency | ~3 weeks; at least every 90 days (earlier talk: ~2 weeks) | docs vs 2024 talk | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/price-optimization), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/price-optimization), [Roblox 2024-09 18:21](https://youtu.be/ETDit6eO4sQ?t=1101) |
| Price review period / control group | 4 weeks / 2% | docs | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/price-optimization), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/price-optimization) |
| Regional price bounds | 30%-100% of default; 5,000+ experiences adopted regional pricing | 100 default gives 30 floor | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/regional-pricing), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/regional-pricing), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/regional-pricing) |
| Developer product / paid access ranges | 1 to 1,000,000,000 Robux / 25-1000 Robux | docs | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/developer-products), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/developer-products), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/paid-access-robux) |
| Paid access price history | ~300 Robux at early access, lowered to 50, 25, 15-25 before going free; Bloxburg 2500 Robux (2018) | Emergency Response | [Roblox Creators 2023-01 0:00](https://youtu.be/YdplC2WVkWc?t=0), [Roblox 2018-07 44:54](https://youtu.be/DWUfL8azgIk?t=2694) |
| Subscription minimum / change | 49 Robux; every 60 days; 30 days' notice for increases | docs | [Roblox DevForum 2026-04](https://devforum.roblox.com/t/let-your-players-pay-for-subscriptions-within-experiences-in-robux/4552995), [Roblox DevForum 2026-04](https://devforum.roblox.com/t/let-your-players-pay-for-subscriptions-within-experiences-in-robux/4552995), [Roblox DevForum 2026-04](https://devforum.roblox.com/t/let-your-players-pay-for-subscriptions-within-experiences-in-robux/4552995) |
| Local-currency subscription tiers | $2.99, $4.99, $7.99, $9.99, $14.99 | docs | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/subscriptions), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/subscriptions) |
| Desktop paid-access rev share | $9.99 = 50%; $29.99 = 60%; $49.99 = 70% | before taxes/VAT | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/paid-access-local-currency), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/paid-access-local-currency), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/paid-access-local-currency) |
| Rev share above price floor | up to 70% (vs 30%) | avatar items | [Roblox 2025-09 18:30](https://youtu.be/Tese1QLD3nU?t=1110), [Roblox 2025-09 18:30](https://youtu.be/Tese1QLD3nU?t=1110) |
| Hat advance | 1,500 Robux; 95 Robux price; ~22-23 sales to recoup | UGC | [Roblox Creators 2025-04 2:53](https://youtu.be/Zb1BJow0NV4?t=173), [Roblox Creators 2025-04 2:53](https://youtu.be/Zb1BJow0NV4?t=173), [Roblox Creators 2025-04 2:53](https://youtu.be/Zb1BJow0NV4?t=173) |
| Model / plugin price range | $2.99-$49.99 / $4.99-$249.99 | docs | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/creator-store), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/creator-store) |
| Promoted on-sale pass range / discount cap | 50-800 Robux; no discount above 1,000,000 Robux | docs | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/passes), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/roblox-plus) |
| Rewarded value | 3-10 Robux | official | [Roblox Creators 2025-08 18:26](https://youtu.be/7AtvvUxvCaU?t=1106), [Roblox Creators 2025-08 17:45](https://youtu.be/7AtvvUxvCaU?t=1065) |
| Healthy conversion rates | 2-3% (PCR 2%, CVR 2%, QPTR 3%) | MoseyTube, self-reported | [MoseyTube 2026-08 4:26](https://youtu.be/xIBc5He_sy4?t=266), [MoseyTube 2026-08 4:26](https://youtu.be/xIBc5He_sy4?t=266) |
| Pet conversion rate | 0.3% to 0.75% after teaser change; US ~2% | Tizzy, self-reported | [Tizzy 2026-07 17:26](https://youtu.be/nggNvUILQ1I?t=1046), [Tizzy 2026-07 16:44](https://youtu.be/nggNvUILQ1I?t=1004) |
| Impulse prices | 19 Robux (2x offline); 5 Robux speed tier (61,000 sales); reroll 4-5 Robux | indie, self-reported | [Tizzy 2026-06 13:31](https://youtu.be/zoz3PSMqets?t=811), [Tizzy 2026-10 16:44](https://youtu.be/_JyiKfNNqls?t=1004), [Alex Builds Games 2026-06 14:48](https://youtu.be/x_SflcuSi1w?t=888) |
| Alex Builds Games examples | progress boost <60 Robux; $2.99 auto-collect; $3.99 VIP badge seen as overpriced; katana pack 279 Robux; crates 199-1,900 Robux | self-reported | [Alex Builds Games 2026-06 1:09](https://youtu.be/x_SflcuSi1w?t=69), [Alex Builds Games 2026-06 10:19](https://youtu.be/x_SflcuSi1w?t=619), [Alex Builds Games 2026-06 8:43](https://youtu.be/x_SflcuSi1w?t=523) |
| Starter bundles | 25 to 99 Robux (Spongebob TD); 3x speed $5 | official talk | [Roblox 2025-09 21:55](https://youtu.be/MJ-zYfL10Ew?t=1315), [Roblox 2025-09 25:13](https://youtu.be/MJ-zYfL10Ew?t=1513) |
| Anchor / bundle-matching examples | 900 Robux anchor vs 100-200 Robux items; 1,800 Robux bundle = $20 Robux package | Stewiepfing; 1_Bruce | [Stewiepfing 2024-02 1:36](https://youtu.be/v8tFfBTr6M8?t=96), [1_Bruce 2026-03 4:05](https://youtu.be/zgq6L4ZzCHs?t=245), [1_Bruce 2026-03 4:05](https://youtu.be/zgq6L4ZzCHs?t=245) |
| Regional and DevEx figures | Bookings ~$40 US vs ~$6 lowest region; DevEx $0.0038 standard, $0.0054 U.S. 18+ purchases | Deconstructor of Fun; docs | [Deconstructor of Fun 2025-04 6:20](https://youtu.be/v_0RADBCTlw?t=380), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/developer-exchange), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/monetization/18-plus-devex-rate) |
| Demo dev product price | 5 Robux | Demo 'More Money' product grants 1000 coins (self-reported, 2022). | [B Ricey 2022-04 0:35](https://youtu.be/5bI6l6SHBDU?t=35) |
| Walk pass price | 13 Robux | Temporary walk pass in a cage-escape paywall (self-reported, 2024). | [janisjanis01 2024-06 1:54](https://youtu.be/NWyK_PbFdxE?t=114) |
| Starter bundle price | 4,900 Robux | Low-advice; self-reported 2025. | [RoDev 2025-05 17:06](https://youtu.be/Gw2FwndwnOg?t=1026) |
| Starter bundle sample item prices | 49, 99, 149 Robux | Included items in the official starter bundle sample. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/resources/feature-packages/bundles) |
| Starter bundle example discount | Save 75% | Example metadata description in the official starter bundle sample. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/resources/feature-packages/bundles) |
| Daily reward skip item | 75 Robux | Sample monetisation plan; low-advice. | [rasdev 2026-05 6:32](https://youtu.be/N3L63uyLyQ8?t=392) |
| Exclusive weapon skin in starter loot bag | 75 Robux | Starter loot bag example (self-reported, 2026-06). | [rasdev 2026-06 7:09](https://youtu.be/TqjyNV9La5c?t=429) |
| Best crate price | 499 Robux | Self-reported best-performing crate price (2025). | [janisjanis01 2025-09 8:44](https://youtu.be/YVKHlrlWn-k?t=524) |
| Flyable boat price | 1,600 Robux | Boat bought by creator at Sky Crest; low-advice. | [ProjectSupreme 2026-10 1:16](https://youtu.be/6U55tBYn52I?t=76) |
| Bloxburg price paid by speaker | 25 Robux | Low-advice; single purchase example. | [rasdev 2026-06 6:00](https://youtu.be/8lWfkv6dmpo?t=360) |
| Animation pack marketplace price floor | 300 Robux | Minimum selling price; not an extra fee. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/avatar/animation-packs), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/avatar/animation-packs) |
| Progressive creator share (marketplace only) | 1x floor 30%; 2x 50%; 3x 62%; 5x 69%; 6x+ capped 70% | In-game sales stay at 30%; regional pricing does not change share (official, 2026-10). | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/marketplace/marketplace-fees-and-commissions), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/marketplace/marketplace-fees-and-commissions) |
| Amount Above Price Floor default | 0 Robux (required) | Example: floor 50 plus 5 gives 55 Robux (official). | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/marketplace/publish-to-marketplace) |
| Minimum plugin price | $4.99 USD | Official minimum (low-advice flag). | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/assets/monetize) |
| In-experience currency example price | 79 Gems | Sample pricing with CurrencyTypes.PriceType.InExperience (official). | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/resources/feature-packages/bundles) |
| Free Limited publish limit | 50 per day | Applies to free Limiteds on sale; paid Limiteds have no limit (official). | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/marketplace/publish-to-marketplace) |
| Dev share of a $5 purchase | about 21% reaches dev (70% dev share of Robux spend as stated) | Speaker's breakdown; treat as one creator's estimate, not an official figure. | [rasdev 2026-10 1:10](https://youtu.be/53OBGXktIPY?t=70) |
| Failed game total spend | ~38,000 Robux (10,000 purchase + 18,000 ads + 10,000 developers) | Net loss; 20 copies sold for the purchase (self-reported, 2025-09). | [janisjanis01 2025-09 13:47](https://youtu.be/YVKHlrlWn-k?t=827), [janisjanis01 2025-09 0:17](https://youtu.be/YVKHlrlWn-k?t=17) |
| Typical hit-game sale price | 1-12 months of earnings | Speaker's estimate; low-advice. | [rasdev 2026-10 1:49](https://youtu.be/4GEHEzhvhwI?t=109) |
| Standard Robux pack price | 400 R$ for $4.99 (~1.25 cents per R$) | Player purchase price at the Roblox store, July 2026. | [Generalist Programmer 2026-07 0:59](https://youtu.be/vbzFbOUGERA?t=59) |
| Developer net per 1,000 R$ spent | ~700 earned R$ worth ~$2.66 | After the marketplace cut, 2026-07 indie figure. | [Generalist Programmer 2026-07 5:23](https://youtu.be/CFohgybeybM?t=323), [Generalist Programmer 2026-07 5:23](https://youtu.be/CFohgybeybM?t=323) |
| Buy-to-cash-out gap | ~3:1 before fees | Player buy price vs developer DevEx payout. | [Generalist Programmer 2026-07 2:06](https://youtu.be/vbzFbOUGERA?t=126) |
| Bulk cash-out comparison | 100,000 R$ costs ~$1,000 to buy vs ~$380 to cash out | Same Robux amount at buy price vs DevEx rate, 2026-07. | [Generalist Programmer 2026-07 0:00](https://youtu.be/vbzFbOUGERA?t=0) |
| DevEx rate (2024-07 indie) | 5,000 R$ ≈ $12 | Rough conversion; conflicts with the 2024-12 figure. | [VuukStudios 2024-07 2:10](https://youtu.be/NfXvHlAdIsI?t=130) |
| DevEx rate (2024-12 indie) | 1,000 R$ ≈ $1 | Conflicts with 2024-07 and 2026-07 figures; verify on DevHub. | [VuukStudios 2024-12 12:06](https://youtu.be/xBPJnMgLoUE?t=726), [VuukStudios 2024-12 12:06](https://youtu.be/xBPJnMgLoUE?t=726) |
| 18+ DevEx uplift | ~42% more per Robux | For 18+ qualified users vs standard DevEx rate, Sept 2026. | [VuukStudios 2026-09 4:04](https://youtu.be/2Q4NqQikzsY?t=244), [VuukStudios 2026-09 4:04](https://youtu.be/2Q4NqQikzsY?t=244) |
| Regional pricing floor | As low as 30% of list price | Regional pricing example in DevForum docs, July 2026. | [Roblox DevForum 2026-07](https://devforum.roblox.com/t/scribe-v261-persistent-typed-auto-replicated-player-data-built-on-profilestore/4738905) |
| Roblox Plus discount | 10 to 20% less for subscribers | Per-player price display, July 2026. | [Roblox DevForum 2026-07](https://devforum.roblox.com/t/scribe-v261-persistent-typed-auto-replicated-player-data-built-on-profilestore/4738905) |
| Regional display example | $14.99 shown as $2.99 to a Canadian viewer | Speaker's example of regional display pricing, April 2024. | [ByteBlox 2024-04 6:18](https://youtu.be/7NRp4BEYrsQ?t=378) |
| Revenue after halving gamepass and dev product prices | ~600K to ~1.2 to 1.4M R$ per 72 hours (over 2x) | Mostly lower-income audience; one creator, Oct 2026. | [VuukStudios 2026-10 3:24](https://youtu.be/4vuXAQt0PuQ?t=204), [VuukStudios 2026-10 3:42](https://youtu.be/4vuXAQt0PuQ?t=222) |
| Revenue after halving prices (Mexico-heavy audience) | ~5x | Same creator; figure differs from the 2x result above. | [VuukStudios 2026-10 5:01](https://youtu.be/0ENzqNB_EUo?t=301), [VuukStudios 2026-10 4:20](https://youtu.be/0ENzqNB_EUo?t=260) |
| Spend before odds reduction | About 4,000 R$ | Example threshold for loyal spender reducing odds, Feb 2025. | [ByteBlox 2025-02 16:44](https://youtu.be/o-8V99horro?t=1004) |
| Timed unlock prices | Walk 20 R$ per 10 s; jump 30 R$ per 10 s; camera 50 R$ per 10 s | ByteBlox example; low-advice. | [ByteBlox 2024-11 17:27](https://youtu.be/Jl0SdXksQsI?t=1047), [ByteBlox 2024-11 17:27](https://youtu.be/Jl0SdXksQsI?t=1047), [ByteBlox 2024-11 17:27](https://youtu.be/Jl0SdXksQsI?t=1047) |
| Paid access price | 100 R$ | Used as a barrier to entry against exploiters, April 2022. | [Roblox DevForum 2022-04](https://devforum.roblox.com/t/developers-are-not-equipped-to-deal-with-exploiters/1770356) |
| Video upload cost | 2,000 R$ per upload | Roblox Creator Docs, Oct 2026. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/ui/video-frames), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/ui/video-frames) |
| Publishing fee | 1,000 R$ per game, one-time, refundable | Alternative to two months of Plus/Premium for all-ages publishing; proposed April 2026, official May 2026. | [Roblox DevForum 2026-04](https://devforum.roblox.com/t/new-publishing-requirements-evaluation-process-for-games/4573166), [Roblox DevForum 2026-04](https://devforum.roblox.com/t/ama-publishing-requirements-roblox-kids-select/4580953), [Roblox DevForum 2026-05](https://devforum.roblox.com/t/alternate-publishing-requirements-for-roblox-kids-and-select/4630944) |
| Private server fee | ~100 R$ (~$1 USD) per month | Set by individual developers, not Roblox; Oct 2026. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/education/educator-onboarding/3-setting-up-a-roblox-classroom), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/education/resources/frequently-asked-questions-education) |
| Transfers API caps | 500 R$/day; 1,000 R$/month | DevForum, May 2026. | [Roblox DevForum 2026-05](https://devforum.roblox.com/t/disabling-cross-game-sales-of-passes-and-dev-products-and-introducing-the-transfers-api/4618396), [Roblox DevForum 2026-05](https://devforum.roblox.com/t/disabling-cross-game-sales-of-passes-and-dev-products-and-introducing-the-transfers-api/4618396) |
| Commission example | $15/hr x 6 hrs + 30% premium = $117 (~30k R$) | Moderate-detail 100x100 lobby, March 2021. | [Roblox DevForum 2021-03](https://devforum.roblox.com/t/developing-expert-developers-advice-from-all-around-the-world/1134437), [Roblox DevForum 2021-03](https://devforum.roblox.com/t/developing-expert-developers-advice-from-all-around-the-world/1134437) |
| Student commission example | $175 = 32K R$ | Robux conversion stated, Feb 2026. | [VuukStudios 2026-02 10:53](https://youtu.be/JQqhUWZUGDQ?t=653) |
| UGC accessory price floor | 50 R$ minimum (creator-suggested) | Arow, Aug 2025. | [Arow 2025-08 1:22](https://youtu.be/yM28oinpQIo?t=82), [Arow 2025-08 1:22](https://youtu.be/yM28oinpQIo?t=82) |
| UGC hat initial price floor | 120 R$ at launch | Aug 2019; ceiling not stated. | [Roblox DevForum 2019-08](https://devforum.roblox.com/t/ugc-catalog-is-now-live/331405), [Roblox DevForum 2019-08](https://devforum.roblox.com/t/ugc-catalog-is-now-live/331405) |
| Outfit bundle prices | 100 to 164 R$ | Erthlord example, July 2026. | [Erthlord 2026-07 5:51](https://youtu.be/57GCHQtyuZQ?t=351) |
| Comparable product prices | Kit $24 (speaker's own); competitor skill tree $40; competitor asset pack $20 | Promotional and comparables, 2026. | [Generalist Programmer 2026-07 0:24](https://youtu.be/Oj0nbY61qsY?t=24), [Raul 2026-08 0:52](https://youtu.be/VQHtqIE31Pk?t=52), [Raul 2026-08 4:16](https://youtu.be/VQHtqIE31Pk?t=256) |
| Course price cut | $60 reduced to $30 | ByteBlox, Nov 2024; a 50% cut example. | [ByteBlox 2024-11 20:08](https://youtu.be/Jl0SdXksQsI?t=1208) |
| Economy example values | Starting coins 250; jump upgrade 5 coins; upgrade cost 500 to 1000; newMaxItems 10 to 15; bag spaces 6 to 10; sell multiplier 50 to 200 | Tutorial and official starting values, Oct 2026. | [Roblox DevForum 2023-07](https://devforum.roblox.com/t/the-best-and-easiest-way-to-save-and-load-data/2494650), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-an-upgrade-button), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/education/adventure-game-series/finishing-the-project) |
| Economy exploit example | Free egg hit 130 times (~$6,500 in 30 seconds) | MonarchDev, Oct 2026; drove rebuild of all rebirth prices. | [MonarchDev 2026-10 5:53](https://youtu.be/bbCmt98O9MA?t=353) |
| ARPDAU | 0.15 (creator called it poor) | Currency unit not clearly stated; Oct 2026. | [Seibo 2026-10 4:26](https://youtu.be/Fh0Xku6NwOQ?t=266) |
| Gamepass suggested price range | 10 to 150 Robux | Last Level Studios suggestion (2019-10); some games price passes up to 9,000 Robux. Indie self-reported. | [Last Level Studios 2019-10 23:29](https://youtu.be/vY0om5O-Oh8?t=1409), [Last Level Studios 2019-10 25:30](https://youtu.be/vY0om5O-Oh8?t=1530) |
| Gamepass sales by price (single game) | 75 Robux pass sold 38; 399 Robux pass sold 6; prices ranged 4.99 to 399 Robux | Mulch (2021-09). One game, small sample, low-advice. | [Mulch 2021-09 5:22](https://youtu.be/yG44d_Xnbwg?t=322) |
| High-price pass sales | About 1,000 Robux pass sold 5 vs 2 the day before | BubuTheDev (2024-12). Shows slow volume at high prices; low-advice. | [BubuTheDev 2024-12 1:16](https://youtu.be/82HrjFTdPkU?t=76) |
| VIP/private server minimum price | 10 Robux minimum; free allowed since 2020 update | Emancyphur (2018-07, updated by its own note). Check current rules. | [Emancyphur 2018-07 0:45](https://youtu.be/RUqr6lj1UYI?t=45) |
| Private server price in use | 50 Robux, unchanged since launch | Mulch (2024-06). | [Mulch 2024-06 3:28](https://youtu.be/pqCXX06vlDw?t=208), [Mulch 2024-06 4:10](https://youtu.be/pqCXX06vlDw?t=250) |
| Custom name gamepass price | 29 Robux | PolarBear (2024-02) cheap entry pass; low-advice. | [PolarBear 2024-02 4:07](https://youtu.be/nkmfdUbj4bQ?t=247), [PolarBear 2024-02 4:07](https://youtu.be/nkmfdUbj4bQ?t=247) |
| Story expansion pack price | 199 Robux | PolarBear (2024-02); used with odd-number pricing claim. | [PolarBear 2024-02 2:02](https://youtu.be/nkmfdUbj4bQ?t=122) |
| Rebirth price step | +1 rebirth = 15 Robux; +5 rebirth = 50 Robux (judged too high) | PolarBear (2024-03); low-advice. | [PolarBear 2024-03 1:22](https://youtu.be/Q-Wbi1an-ww?t=82) |
| Ad credit price | 1 credit = 285 Robux | PolarBear (2024-03); Ads Manager credit purchase. May be outdated. | [PolarBear 2024-03 1:51](https://youtu.be/bwMUqu-wWpw?t=111) |
| Ad spend example | About 8,000 Robux over about 6 days, 5 credits/day | Lnor Roblox (2026-05), full-send campaign with no prior testing. | [Lnor Roblox 2026-05 0:40](https://youtu.be/QOS7dQowyRk?t=40) |
| Per-game ad bid | Speaker used 0.01 to 0.03 Robux; Roblox suggests 0.04 to 0.25 Robux | BubuTheDev (2025-03); speaker claims suggested range is inflated. | [BubuTheDev 2025-03 2:04](https://youtu.be/0NK_JBYEILA?t=124) |
| Emote minimum price | 50 Robux | Xaiyne (2025-08). | [Xaiyne 2025-08 13:17](https://youtu.be/aqv5bLmqbzc?t=797) |
| DJ skin price | About $10 worth of Robux | CORSO (2024-09), speaker's characterisation. | [CORSO 2024-09 0:26](https://youtu.be/lFD1wKdwSUs?t=26) |
| Regional price example | 10 Robux (US) becomes 4 Robux (Afghanistan, Pakistan) | EISABOOS (2025-08 and 2025-12). Regional pricing scales by purchasing power. | [{EISABOOS} "RBX" 2025-08 1:00](https://youtu.be/5dfKSg_wqLA?t=60), [{EISABOOS} "RBX" 2025-12 3:02](https://youtu.be/skRRdrpf2F4?t=182), [{EISABOOS} "RBX" 2025-12 3:02](https://youtu.be/skRRdrpf2F4?t=182) |
| Proposed UGC item prices (2019) | 150, 500, 1,000, 5,000 Robux; stock 500,000 units | ThatGuyEvan (2019-08); proposals only, outdated, low-advice. | [ThatGuyEvan 2019-08 1:11](https://youtu.be/aOjCEe0LL6k?t=71), [ThatGuyEvan 2019-08 1:52](https://youtu.be/aOjCEe0LL6k?t=112), [ThatGuyEvan 2019-08 2:34](https://youtu.be/aOjCEe0LL6k?t=154) |
| Gift price range (2012) | 50 to 40,000 Robux | ThatGuyEvan (2022-08) historical; not a current benchmark. | [ThatGuyEvan 2022-08 4:23](https://youtu.be/APeSOO8WRPQ?t=263) |
| Dev share by channel (claimed) | About 70% real-dollar vs about 27% via DevEx | Where The Money Went (2026-10); unverified, low-advice. | [Where The Money Went 2026-10 12:58](https://youtu.be/cJHug1Wnmhw?t=778) |
| DevEx rate, general | $0.0038 per earned Robux | Effective June 8, 2026, per a secondary agency citation of the Roblox DevEx page. Verify on the primary page before modeling. | [StudioKrew (agency blog, GGAID data) 2026-08](https://studiokrew.com/blog/top-roblox-games-august-2026/) |
| DevEx rate, eligible 18+ US spend | $0.0054 per Robux | Applies only to eligible 18+ US spend; see existing rule on the 18+ audience. | [StudioKrew (agency blog, GGAID data) 2026-08](https://studiokrew.com/blog/top-roblox-games-august-2026/) |
| Gamepass price range (snapshot A) | 19–2999 Robux, 46 passes on sale | Cheapest Orange Trail, priciest InfinityTrail. Single-game snapshot dated 2026-11. | [Roblox public API 2026-11](https://www.roblox.com/games/95082159892680/) |
| Gamepass price range (snapshot B) | 9–4999 Robux, 40 passes on sale | Single-game snapshot dated 2026-11. | [Roblox public API 2026-11](https://www.roblox.com/games/114697347887839/) |
| Gamepass price range (snapshot C) | 30–150 Robux | Rescue Rope 30 up to Fall Pack 150. Single-game snapshot dated 2026-11. | [Roblox public API 2026-11](https://www.roblox.com/games/119958473240233/) |
| Gamepass price range (snapshot D) | 49–399 Robux | Auto Collect 49 up to Mastery Pass 399. Single-game snapshot dated 2026-11. | [Roblox public API 2026-11](https://www.roblox.com/games/95168737547508/) |
| Gamepass price range (snapshot E) | 50–999 Robux, 12 passes | Single-game snapshot dated 2026-11. | [Roblox public API 2026-11](https://www.roblox.com/games/121864768012064/) |
| Cheapest gamepass in one sampled list | 129 Robux (Speed Boost) | Shows that the floor depends on the game, not the platform. | [Roblox public API 2026-11](https://www.roblox.com/games/131623223084840/) |
| VIP gamepass price | 199 Robux | Top-end standard VIP in one sample dated 2026-11. | [Roblox public API 2026-11](https://www.roblox.com/games/95168737547508/) |
| Mid-tier VIP gamepass price | 175 Robux | Sampled mid-tier VIP pass. | [Roblox public API 2026-11](https://www.roblox.com/games/131623223084840/) |
| Most expensive gamepass in one sample | 888 Robux (VIP+) | Top-tier VIP bundle. | [Roblox public API 2026-11](https://www.roblox.com/games/131623223084840/) |
| Common gamepass price clusters | 75, 99, 149 Robux | 75 = 5 max-stat passes; 99 = 2x Cash and 4th Tool Slot; 149 = All Upgrades Maxed and 5th Tool Slot. | [Roblox public API 2026-11](https://www.roblox.com/games/119958473240233/) |
| Emotes gamepass price | 149 Robux | 2x Emotes pass. | [Roblox public API 2026-11](https://www.roblox.com/games/93978595733734/) |
| Odd-value gamepass price points in the wild | 399 (X2 MONEY) and 467 (X2 GROWTH SPEED) Robux | Non-round 467 appears alongside round 399; a sample of two, so treat as an experiment signal, not a default. | [Roblox public API 2026-11](https://www.roblox.com/games/107778070777162/), [Roblox public API 2026-11](https://www.roblox.com/games/107778070777162/) |
| Advanced Luck permanent boost gamepass | 545 Robux | Permanent 150% luck boost, indie tracker. | [RoWatcher (tracker blog) 2026-00](https://rowatcher.com/news/fish-it-reels-in-270k-players-inside-roblox-s-most-addictive-casual-game-of-2026) |
| Wallet Robux repurchase rate (DevEx rate) | $0.0038 per Robux | Official DevForum, 2026-09. Example: 10,000 Robux for $38; 30,000 Robux for $114, plus tax. This is what you pay to buy Robux back, not the developer payout rate. Verify the current figure before budgeting. | [Roblox DevForum 2026-09](https://devforum.roblox.com/t/introducing-roblox-wallet-and-card-get-paid-faster/4865505), [Roblox DevForum 2026-09](https://devforum.roblox.com/t/introducing-roblox-wallet-and-card-get-paid-faster/4865505) |
| UGC accessory test upload cost | 750 Robux per test upload | Official source tagged low-advice, 2026-09. Applies to test uploads during plugin/UGC accessory development, not to pricing of live items. | [Roblox 2026-09 23:38](https://youtu.be/HXZRH-2zurk?t=1418) |
| Speed multiplier price ladder (small) | x2 = 3 Robux, x4 = 9 Robux, x8 = 24 Robux | Treadmill speed upgrade tiers shown in-game by an indie creator; low-advice source, one game. | [Mulch 2026-09 5:08](https://youtu.be/U2IjSOyNTB8?t=308) |
| Speed multiplier price ladder (higher tiers) | 460, 600, 876, 1,268 Robux for 256 to 4,000 multiplier | Upper-tier treadmill speed upgrades from the same indie game; rising steps. | [Mulch 2026-09 1:18](https://youtu.be/WYODms_JMRA?t=78), [Mulch 2026-09 1:18](https://youtu.be/WYODms_JMRA?t=78) |
| Single pet/egg purchase price | 140 Robux | Single-unit purchase in an indie game. | [Mulch 2026-09 9:22](https://youtu.be/U2IjSOyNTB8?t=562) |
| Bulk 'grow all' price | 184 Robux (about 1.31x single pet price) | Bulk egg-open action in the same game. | [Mulch 2026-09 10:44](https://youtu.be/U2IjSOyNTB8?t=644) |
| Gold bar sell value (in-game, shop items module) | 50 | Self-reported indie value, in-game currency sell price, not Robux. | [GnomeCode 2025-05 6:22](https://youtu.be/2jcCCIcxvdk?t=382) |
| Coal sell value (in-game, shop items module) | 10 | Self-reported indie value; low-tier item in the same module as gold bar at 50, about 1:5 ratio. | [GnomeCode 2025-05 6:22](https://youtu.be/2jcCCIcxvdk?t=382) |
| Location 1 / Location 2 price (in-game coins) | 100 / 250 | Self-reported indie figures; in-game coins, not Robux. Second location costs 2.5x the first. | [ArTheDev 2025-06 9:39](https://youtu.be/2M8r1oU2k3U?t=579) |
| LTV lift from economy sources/sinks tuning | up to ~20% | GameMakers, 2022-08, self-reported; difficulty tuning reported at ~10%. | [GameMakers 2022-08 30:52](https://youtu.be/JVCao-Yhu2M?t=1852), [GameMakers 2022-08 30:52](https://youtu.be/JVCao-Yhu2M?t=1852) |
| DevEx rate (per Robux) | $0.0035 | PineappleDev, 2024-01, stated as about a third of a cent. Older baseline; verify before use. | [PineappleDev 2024-01 2:30](https://youtu.be/-LXvkK5YkNM?t=150) |
| DevEx rate (per 1K Robux, creator estimate) | ~$0.36 per 1K as stated; ~$3.60 per 1K implied by the $3,600 / 950K example | VuukStudios, 2026-01, conversion-site estimate; rate reported up ~15% from prior video. The stated $0.36/1K is inconsistent with the $3,600 for 950K example (about $3.79/1K). Treat as unverified. | [VuukStudios 2026-01 1:26](https://youtu.be/Iy5cO3Nanhc?t=86) |
| Icon starting price | ~250 Robux per icon | PolarBear, 2024-07, starting rate suggested by speaker; low-advice. | [PolarBear 2024-07 7:28](https://youtu.be/tkAis2wTxms?t=448), [PolarBear 2024-07 7:28](https://youtu.be/tkAis2wTxms?t=448) |
| Thumbnail service prior offer | 1000 Robux or $5 | PolarBear, 2024-07, example of a prior thumbnail offer; not a market benchmark. | [PolarBear 2024-07 6:48](https://youtu.be/tkAis2wTxms?t=408) |
| Expedited review fee | 100,000 Robux (~$1,000 USD) | Cumin, 2026-06, refundable after 90 days, 48-hour review. Low-advice and not verified against official docs; confirm before budgeting. | [Cumin 2026-06 5:58](https://youtu.be/FpC7qnwDMDQ?t=358) |
| Currency pack price points | 50 for 9 Robux; 1,500 for 99 Robux | Indie, self-reported, 2025-06. Ladder example for currency packs. | [janisjanis01 2025-06 2:47](https://youtu.be/B409dMcW-pw?t=167) |
| Currency bundle example | 1000 gems for 400 Robux | Indie, self-reported, 2026-04. Speaker says spending 300 gems feels like nothing. | [rasdev 2026-04 2:41](https://youtu.be/yFKY2FlwHjE?t=161) |
| Seasonal gamepass sale | 50% off all gamepasses; server luck pass 25 Robux during the sale | Indie, 2024-12 Christmas sale. Speaker calls it a one-off, not a standing price. | [janisjanis01 2024-12 13:40](https://youtu.be/HGobKizBHqQ?t=820), [janisjanis01 2024-12 13:53](https://youtu.be/HGobKizBHqQ?t=833), [janisjanis01 2024-12 13:40](https://youtu.be/HGobKizBHqQ?t=820) |
| Badge creation cost | 100 Robux per badge | Indie, self-reported, 2025-10. Platform cost to budget before launch. | [janisjanis01 2025-10 14:26](https://youtu.be/MML_z-jpmF4?t=866) |
| Exotic seed pack price | 199 Robux | Indie, 2025-06. Single item price point. | [janisjanis01 2025-06 6:18](https://youtu.be/B409dMcW-pw?t=378) |
| Group icon asking price | 250 Robux | Indie commissioner's asking price, 2024-07. Not a fixed market rate. | [PolarBear 2024-07 2:38](https://youtu.be/yYp23GK9RI4?t=158) |
| Pet multiplier buff | ~25% for most pets, 10% for some, 30% target | Indie, 2024-12. Economy balancing, not a Robux price. | [janisjanis01 2024-12 9:20](https://youtu.be/Jc7yQTMFexk?t=560), [janisjanis01 2024-12 9:20](https://youtu.be/Jc7yQTMFexk?t=560) |
| Own-site asset sale | 25% off, held at 25K subscribers | Indie promotional sale, 2025-03. Asset store, not Robux pricing. | [janisjanis01 2025-03 1:56](https://youtu.be/OAsW5osz46o?t=116) |
| In-game coin unlock costs | Area 10: 75M; Area 11: 100M; next: 200M; new egg: 50M; final area: 1B | In-game currency, not Robux, 2024-04. Shows escalating ladder shape only. | [janisjanis01 2024-04 3:38](https://youtu.be/7z8XlhAtGpQ?t=218), [janisjanis01 2024-04 4:30](https://youtu.be/7z8XlhAtGpQ?t=270) |
| Egg price | 5 million gems | In-game currency, 2024-11. Price of egg hatching a revived Huge dragon. | [janisjanis01 2024-11 19:49](https://youtu.be/vJekPDaIT30?t=1189) |
| Huge Jelly Axolotl unlock cost (Pets Go, in-game currency) | 500,000 | In-game currency cost, not Robux. Indie self-reported, low-advice source. | [Mulch 2024-11 0:00](https://youtu.be/SLrIagp7uHE?t=0) |
| Jelly Monkey pet quoted sale value (in-game currency) | 3.3 million | Quoted in-game value of one pet. Indie self-reported, low-advice source. | [Mulch 2024-11 6:10](https://youtu.be/SLrIagp7uHE?t=370) |
| Long Boy pet direct Robux price | 650 Robux | Price to buy the pet directly instead of crafting it. Indie self-reported, low-advice source. | [Mulch 2024-11 1:23](https://youtu.be/axxmwooE-J0?t=83) |
| Super Marettino weather event secret drop chance | 1 in 675 | Stated by presenter for the weather event. Relevant only as a drop-rate reference, not a spend-linked odds figure. Indie self-reported, low-advice source. | [Mulch 2025-09 1:22](https://youtu.be/5tyX4bVkpMQ?t=82) |

## Where creators agree
- Roblox official sources and indie creators (Tizzy, MoseyTube, CallMeDogey, DevForum) agree on offering a wide ladder of price points including cheap entry ones.
- Roblox official, Stewiepfing and 1_Bruce agree that price presentation (best value, anchors, bundle matching) drives conversion.
- Roblox official talks and docs agree that prices should be tested rather than guessed and must be scripted for optimization.
- Roblox official and Tizzy agree that cheap prices should not break the in-game economy.
- Roblox official speakers agree on time-to-earn pricing.
- Yann (T6508) and the existing cheap-early rule agree that low early prices drive payer conversion; Yann adds that prices may have been raisable at peak (Q1032).
- Developers keep only about 70% of player spend after the marketplace cut, so pricing must account for net Robux (T13500, N5274, N5248).
- Regional and per-player pricing matters: prices vary by region and subscription, and display prices should be localized (T12099, T13577, T13868).
- Game passes and developer products should be priced differently: higher for one-time passes, lower for repeatable purchases (T12289, aligned with existing tiering).
- Commission and service pricing should be set from hourly rate and effort, then tuned by observed volume (T10995, T12790).
- Platform fixed costs (uploads, publishing fee, private servers) should be budgeted before launch (T14327, N5136, N6048).
- Keeping a private server or VIP price fixed after sales avoids cancelling subscriptions (Emancyphur, Mulch).
- Higher gamepass prices tend to sell fewer copies in single-game data (Mulch, BubuTheDev), so cheap entry options matter (PolarBear, Last Level Studios).

## Where creators disagree
- **Copy comparables vs test own audience**
  - Roblox Creators (T922) and Roblox (T1576/Q289) say start from comparable items and market research
  - Roblox (T1481) says don't copy competitor prices and test on your own audience
  - DevForum (T3432) says check competitor prices and put slow sellers on sale
- **Price at the floor vs above it (UGC)**
  - Roblox Creators/Rush (T1981, Q379) price at the floor because buyers compare
  - Roblox (T2219) says pricing above the floor can qualify for up to 70% revenue share
- **Cheap vs expensive pricing**
  - Alex Builds Games and Tizzy favor very cheap impulse prices (under 60, 19, 4-5 Robux)
  - Stewiepfing favors showing a 900 Robux anchor first
  - Roblox (T1254) notes lower prices raised revenue per user, but the sweet spot varies
- **Sales frequency**
  - Roblox (T46) says keep sales rare
  - DevForum (T3432) says put slow sellers on limited sale
  - SmartyRBX (T1892) advocates urgency/scarcity
- **Price test duration**
  - 2024 Roblox talk: about 2 weeks (N481)
  - 2026 docs: about 3 weeks plus a 4-week review (N2098, N2102); prefer the newer docs
- **Raise or cut prices for a bestseller or audience**
  - Perstile (T12795, May 2025): an underpriced 500 R$ double-size product should cost more; estimates ~2x revenue at a higher price.
  - VuukStudios (T13867, T13930, N5490, Q1446, Oct 2026): halving gamepass and dev product prices doubled or 5x revenue for a lower-income audience.
  - VuukStudios (Q1453, Oct 2026): higher prices do not mean better revenue.
  - Reconciliation: the answer depends on audience location and purchasing power. Test with your own player data before choosing a direction.
- **Size of revenue lift after halving prices**
  - VuukStudios (N5490, Oct 2026): over 2x (~600K to 1.2-1.4M R$ per 72 hours).
  - VuukStudios (N5533, T13930, Oct 2026): about 5x for a Mexico-heavy audience.
  - Both are single-creator, unverified claims with unknown sample sizes.
- **DevEx value per Robux**
  - VuukStudios (N4633, July 2024): 5,000 R$ ≈ $12.
  - VuukStudios (N4751, T12498, Dec 2024): 1,000 R$ ≈ $1.
  - Generalist Programmer (N5254, N5274, July 2026): about $380 per 100,000 R$ (~$0.0038 per R$).
- **Regional pricing on game passes**
  - EISABOOS (2025-08, low-advice) says turn it off for maximum revenue from high-income regions and leave it on only for broader affordability.
  - EISABOOS (2025-12, more recent) says turn it off for donation-style passes because it can behave incorrectly and lower some countries' costs.
  - The existing knowledge rule 'Set regional prices and mind the bounds' assumes regional pricing is used deliberately; the newer EISABOOS guidance suggests off for donation passes. Prefer the newer guidance and verify in-game.
- **Real-dollar versus Robux sales**
  - Where The Money Went (2026-10, low-advice) says real-dollar sales keep about 70% versus about 27% via DevEx, so favor real-dollar channels.
  - Existing rules favor modelling net Robux and dev share before committing; this claim is a single, unverified figure that could change the decision.
- **Cheapest gamepass price floor**
  - Roblox public API (N7317): cheapest 19 Robux
  - Roblox public API (N7330): cheapest 9 Robux
  - Roblox public API (N7429): cheapest 30 Robux
  - Roblox public API (N7305): cheapest 49 Robux
  - Roblox public API (N7380): cheapest 50 Robux
  - Roblox public API (N7342): cheapest 129 Robux
- **Commission pricing method**
  - Existing knowledge-file rule: price commissions by hourly rate plus complexity premium, then tune the rate.
  - PolarBear (T18529, 2024-07): start icon/thumbnail services at a flat ~250 Robux per icon, then raise as reputation grows.
- **DevEx rate figures across creators**
  - PineappleDev (N7905, 2024-01): $0.0035 per Robux.
  - VuukStudios (N7972, 2026-01): stated ~$0.36 per 1K, but the $3,600 for 950K example implies ~$3.79 per 1K (~$0.0038 per Robux). The creator's own numbers do not reconcile; the newer figure is preferred but unverified.

## Date context (what may be outdated)
- 2018 advice (T37, T46, T52) is manual and formula-free; Price Optimization (2024) and Regional Pricing (2025) now automate testing.
- Price test duration: 2024 talk says about 2 weeks; 2026 docs say about 3 weeks plus a 4-week review. Prefer the newer docs.
- Expedited review fee was cut from 100,000 to 50,000 Robux (N1308, N2031).
- Revenue share above the price floor was previously 30% and is now up to 70%.
- DevEx rates and rev-share tiers are from 2026 docs; verify before relying on them.
- The 2018 Bloxburg paid access price (2500 Robux) is outdated against the current 25-1000 Robux paid access range.
- The 2021 DevForum tier ranges are older and unverified.
- 2026-10 official docs add a progressive creator share table (30% at 1x floor up to 70% cap at 6x) that refines any older flat 30% assumption; prefer the table for marketplace avatar items.
- 2026-10 official docs define Amount Above Price Floor and Do Not Price Below; prefer these over older legacy listing defaults.
- Yann's cheap-launch and raise-later advice is from 2026-05 and self-reported; it reflects one game's peak, so verify on your own audience.
- Robux price examples from 2021-2025 (N2408, N2487, N2568, N2648, N2652) are dated; use them as shape-of-catalogue examples, not current benchmarks.
- Cloud cost items (Extended Services budgets, data store and memory store pricing, TTS and STT request costs) are operating costs, not Robux pricing, and are out of scope for this topic.
- 2019: UGC hat floor was 120 R$ (N4124, T10547). In Aug 2025 a creator suggested a 50 R$ minimum for UGC accessories (N4966, T12932). Floors changed; check current platform rules.
- 2019 exchange rate of 100K R$ = $350 (N4114) is obsolete and should not be used.
- DevEx per-R$ values differ across 2024 to 2026 indie reports; verify the current rate on DevHub before modeling.
- Badge creation cost was 100 R$ before the Feb 2022 change (N4325). The current price is not in these sources.
- Premium Payouts rates changed multiple times (T10964); check current DevHub docs instead of old figures.
- Publishing fee: proposed as 1,000 R$ in April 2026 (N5143), then official in May 2026 as a one-time refundable alternative to two months of Plus/Premium (N5175), tied to the May 11 update.
- Transfers API caps (500 R$/day, 1,000 R$/month) were reported in May 2026 (N5163, N5164).
- Regional discount figures (30% floor, Plus 10 to 20%) are from mid-2026 (N5316, T13577).
- Halving-price evidence is from Oct 2026 and comes from one creator; treat as fresh but unverified.
- Private server fee: DevHub cites about $1 per month (N6020); a second Oct 2026 doc cites ~100 R$ per month (N6048). Both are developer-set.
- Newest guidance (2025-12 regional pricing, 2026-10 real-dollar channels and PBR upload cost) should take precedence over 2018 to 2021 items.
- VIP/private server minimum: 10 Robux (2018) became free-allowed after a 2020 update; use the 2020+ rule.
- Ad credit price (285 Robux, 2024-03) and ad bid suggestions (2025-03) may have changed; check Ads Manager before budgeting.
- UGC item price proposals (2019) and the gift price range (2012) are historical and no longer reliable benchmarks.
- DevEx rate changes over time; verify before modelling revenue (today is 2026-10-29).
- Regional pricing behaviour may change; the 2025-12 'behaves incorrectly' claim is self-reported and should be re-tested.
- The DevEx figure $0.0038 per earned Robux (and $0.0054 for eligible 18+ US spend) is effective June 8, 2026. Replace any older DevEx rate in the file with it, and re-check before each revenue model.
- Roblox API snapshots are dated 2026-11 (today is 2026-11-01). Gamepass prices and lists change, so re-pull before relying on them.
- The RoWatcher figure is dated 2026-00, which is not a valid date. Treat it as undated and unverified.
- The gamepass price 'ranges' are from different games at different times. They are not platform-wide limits, and they should not be read as a platform minimum or maximum.
- 2026-09 official DevForum post sets the wallet repurchase rate at $0.0038/Robux. Re-check before relying on it, since platform rates change.
- The existing rule 'Verify the current DevEx rate before modeling revenue' still applies. Do not confuse the repurchase rate with the developer payout rate.
- N7545 (750 Robux per UGC test upload) is tagged low-advice; treat it as platform-stated but lower-confidence guidance on cost, and verify in the Creator Hub.
- New items are from 2026-08 to 2026-09 and are indie, self-reported, and tied to one game. Treat their specific Robux values as examples of one game's ladder, not current platform norms.
- New sources are dated 2025-02 to 2025-06; today is 2026-11-01, so verify dashboard steps (game pass Sales toggle) and shop module structure against the current Creator Dashboard and Studio before relying on them.
- Coin and sell-value figures are game-specific examples from individual indie projects, not platform defaults.
- Current date is 2026-11-01. The newest DevEx figures (VuukStudios, 2026-01) are about 10 months old. Verify the rate from a current source before modeling.
- The DevEx rate was reported to have risen ~15% between videos (VuukStudios, 2026-01). Older figures (PineappleDev 2024-01 at $0.0035/Robux) are superseded.
- PolarBear's icon and thumbnail prices (2024-07) are older and tied to one creator's portfolio. Treat them as a starting point, not a current market rate.
- Expedited review fee (Cumin, 2026-06) is the newest item but is low-advice and unverified.
- Items in this batch span 2024-04 to 2026-07. The newest pricing tip is rasdev 2026-04 (T18937, N8138); the rest is 2024-2025 indie data that may be stale as of 2026-11.
- Sale figures (Christmas 2024 50% off, 25-Robux server luck pass) were explicitly one-off; do not treat them as standing prices (T18855).
- Badge cost (100 Robux, 2025-10) and other platform costs are indie-reported; re-verify on the Creator Hub before budgeting.
- GTA 6 / console game price items (N8150-N8153, Q1972, Q1973, dated 2026-07) are off-topic for Roblox and should not inform Roblox pricing.
- The new Mulch items are dated 2024-11 (N8193, N8195, N8196) and 2025-09 (N8199). With today at 2026-11-01, these figures are at least a year old and pet values, unlock costs, and drop rates may have changed. Re-check live before using them.
- The Robux price for the Long Boy pet (N8196) is a 2024-11 figure and may no longer match the current Pets Go price.

## Instructions for an agent using this file
- If a game has no pricing data, then start from comparable items and time-to-earn, launch, and iterate (lower if few buy, raise next version).
- If the user hard-codes prices, then switch them to MarketplaceService lookups (InfoType.Product or GamePasses) before any optimization or regional pricing.
- If the game has about 60,000 or more transactions per 30 days, then recommend Price Optimization with all products included; if fewer, then recommend manual A/B tests.
- If designing a shop, then include a very cheap entry tier (about 25-100 Robux, even 35), mid tiers, and a few high or whale tiers; add value-per-Robux labels and highlight the best bundle.
- If an offer is poor value or aimed at new players in the first 10-30 minutes, then make it cheap or hide it.
- If setting a default price, then remember regional prices run 30-100% of it; choose it with the 70% max discount in mind.
- If the user wants a sale, then make it genuine, time-bound, event-tied and infrequent; never label a permanent price 'on sale'.
- If pricing subscriptions, then use at least 49 Robux or an approved local tier; warn that changes are limited to once per 60 days and increases need 30 days' notice.
- If a creator-claimed number (conversion rate, sales) is cited, then label it self-reported and unverified; prefer official docs on platform mechanics.
- If pricing UGC, then decide between the floor (volume) and above the floor (higher revenue share), and note the advance recoup math.
- If a user asks about launch pricing, recommend a half-price first-week test to measure conversion and ARPPU, labelled as a self-reported method (T6538).
- If conversion is stable at a cheap price, suggest a controlled test upward rather than staying at launch-level prices (T6508, Q1032).
- If a user asks about a guaranteed minimum sale price, explain Amount Above Price Floor plus Do Not Price Below (T9593, N3803).
- If a user prices an avatar item above floor, use the progressive share table and note in-game sales stay at 30% (N3512, T8663).
- If a user prices an animation pack, enforce the 300 Robux marketplace floor (T9771).
- If a user prices a plugin, enforce the $4.99 minimum (N3179).
- If a user asks whether a specific Robux price is 'good', compare to other examples in the same genre and label examples as self-reported and dated (N2408, N2487, N2652, N3260).
- When citing indie figures (dev share, failed game totals), label them as one creator's estimate, not a benchmark (N2946, N2655).
- Do not mix cloud/Extended Services budgets into Robux pricing answers (T8149, N3352-N3360).
- If the user's question is about regional pricing or price floors, cross-check with the existing regional and bounds rules before answering.
- If the player country mix is mostly lower-income regions, test halved gamepass and developer product prices against current prices before committing.
- If the audience is mostly US or Canada (higher spend), higher prices are viable; check current conversion data first.
- If pricing a game pass versus a developer product, price the pass higher.
- If modeling revenue, use the current DevEx rate from DevHub and net out the ~70% share before comparing.
- If a game targets 18+ DevEx users, expect ~42% more per Robux but fewer players; choose only if content fits.
- If a traffic spike or big promotion is planned, raise prices temporarily and set a reversion date.
- If pricing commissions, start with hourly rate x hours x (1 + complexity premium), then adjust the rate by observed job volume.
- If a bestseller is high-volume, test a higher price on bulkier items before assuming current pricing is right.
- If a timed or gated feature is planned, budget platform costs (uploads, publishing fee, private servers) before shipping.
- Do not cite 2019 or 2024 DevEx figures as current; they conflict with each other and with 2026 data.
- If asked to change a VIP or private server price that already has sales, warn that existing subscriptions will be cancelled and advise keeping the price fixed.
- If a game uses donation-style passes, recommend checking and likely disabling 'Use regional pricing', then verify the result in-game.
- If asked about odd versus round price points, present the 199 vs 200 claim as an untested hypothesis from one creator and suggest an A/B test.
- If asked about developer share by channel, cite the 70% vs 27% figure only as an unverified claim and recommend checking current DevEx terms.
- If asked about ad budgets, recommend a small test spend before a full campaign and cite the 8,000-Robux no-testing example as the cautionary case.
- If asked about asset upload costs, advise turning off PBR in the generator to avoid extra Robux charges.
- If asked for current prices (ad credits, DevEx, gamepass norms), prefer newer sources and tell the user figures may be outdated.
- Treat all single-creator claims as hypotheses, not benchmarks.
- If a user asks what a gamepass should cost, pull or cite genre-level price clusters (75 / 99 / 149 and the VIP band of 175–199) instead of one game's min or max.
- If you cite an API price range, label it as a single-game snapshot dated 2026-11, and do not present it as a platform floor.
- If you model DevEx revenue, use $0.0038 per earned Robux (and $0.0054 for eligible 18+ US spend), state that these are effective June 8, 2026, and tell the user to confirm on the primary Roblox DevEx page.
- If the user wants a VIP pass, suggest 175–199 Robux as the starting band. Only suggest a VIP+ tier if the game can deliver clearly distinct value, and never recommend changing VIP price after sales begin.
- If the user asks about a permanent boost, note that the 545 Robux indie data point is single-source and recommend a test against their own conversion data.
- Do not infer conversion rates or revenue impact from these price lists. They show what is listed, not what sells.
- If a user asks how to fund publishing, testing or ads with Robux, cite the wallet repurchase rate of $0.0038/Robux (N7522) and note tax applies.
- Do not treat the $0.0038 repurchase rate as the developer payout (DevEx) rate. Verify payout separately before modeling net revenue.
- When estimating UGC avatar item test costs, include 750 Robux per test upload (N7545) and flag that the figure is lower-confidence.
- When advising on net revenue, subtract any Robux bought for platform costs as an expense, not as sales income.
- If a source gives an upgrade ladder with specific Robux steps, use it as an example of tiered escalation, not as a price to copy.
- If a source's price is a guess or refers to a non-Roblox product, exclude it from pricing benchmarks.
- If you add bulk-action prices, cite that they come from a single indie game unless corroborated.
- If asked how to set a game pass price, give the Sales-on-then-enter-price steps (T18184) and remind the user to check the current dashboard UI.
- If asked for example in-game item or location values, cite the indie figures (N7805, N7806, N7809) as self-reported examples, not benchmarks.
- Do not treat in-game coin or sell values as Robux price points; keep currency types separate when recommending prices.
- If a creator-quoted DevEx figure per Robux or per 1K does not reconcile with its own example, recompute it and flag the inconsistency. Example: $3,600 for 950K Robux is about $3.79 per 1K, not $0.36 per 1K.
- Prefer the most recent DevEx figure, but flag it as unverified if it is only a creator or third-party estimate.
- Exclude off-topic benchmarks, such as Fortnite battle pass prices (N7932), from Roblox pricing decisions.
- Do not use tutorial example prices (N7855 at 50 Robux, N7859 at 49 Robux) as market benchmarks. They are illustrative only.
- Mark single-creator and low-advice figures as self-reported when you cite them.
- For icon or thumbnail service pricing, start from the flat per-deliverable benchmark, then adjust for portfolio and turnaround. Do not replace it with the hourly-plus-premium model without noting the difference.
- Treat the expedited review fee (N8014) as unverified. Check official Roblox documentation before budgeting for it.
- Treat every item in this batch as indie, self-reported. None are tagged OFFICIAL.
- Do not use console game prices (GTA 6 $80/$100, GTA 5 $60, $70 console standard) as Roblox benchmarks. They are off-topic (N8150-N8153, Q1972, Q1973).
- Do not convert in-game currency costs (coins, gems) into Robux benchmarks (N8053, N8054, N8086). Use them only to show ladder shape.
- Treat 2024-2025 sale and price-point figures as dated; verify live prices before quoting them.
- When a sale is described as one-off or seasonal, do not generalize it into a permanent price (T18855).
- Do not use the Mulch in-game currency figures (N8193, N8195) as pricing benchmarks for Robux. They are in-game values, not Robux prices.
- Treat the Mulch figures (N8193, N8195, N8196, N8199) as indie self-reported and dated. Cite them only as examples, not as current benchmarks.
- When suggesting a Robux shortcut for a grindable item, compare it against the item's grind cost first, and do not set a shortcut that makes the grind pointless.

## Not covered here (research elsewhere)
- No rigorous data on price elasticity or conversion by price point beyond a few anecdotes.
- No official benchmark for payer conversion rate by genre; 2-3% figures are indie self-reports.
- The actual Robux/USD purchase tiers and current Premium/Plus discount percentages are not covered.
- No guidance on price changes for existing gamepasses (fairness to prior buyers).
- Little on A/B testing methodology without Price Optimization.
- No detail on sale mechanics (how to run discounts via the platform) or limited-item pricing.
- Freelance/commission and template pricing (SmartyRBX T1865, T1892, T1328, N676, N689) is only lightly covered: undercharging a 35,000 Robux job, ~30-buyer cap on a ~$200 template.
- No measured payer conversion, ARPPU, or elasticity benchmarks from any creator; Yann's test-price advice is self-reported without numbers.
- No evidence on how long the half-price first-week test should run or what sample size is needed.
- No current Robux-to-USD rate or revenue-per-Robux figure to convert the price examples.
- The 70% dev share figure (N2946) conflicts with the official 30%-70% creator share table; not reconciled.
- No Price Optimization test results or how it changes price points.
- No data on starter pack conversion rates or how bundle discount depth affects conversion.
- No evidence on whether raising prices reduces repeat purchases or retention; only Yann's single-sale observation.
- No comparison of price points across genres or audiences beyond scattered examples.
- Current official DevEx rate per Robux (sources conflict across 2024 to 2026).
- Current badge creation price after the Feb 2022 change.
- Roblox policy on odds disclosure and spend-linked odds reduction (N4764 is a single-source example).
- Whether the publishing fee is final and in effect for all developers after May 2026.
- Sample sizes, test durations, and confidence for the halved-price revenue claims.
- ARPDAU currency unit and what a healthy ARPDAU is by genre.
- How price cuts affect cannibalization between gamepasses and developer products.
- Effect of regional tax and fees on display prices by country.
- Price elasticity by genre and age group beyond the single 18+ uplift figure.
- Subscription pricing details and conversion (Academy $20 to 50/month is promotional, self-reported).
- Exchange rate or timing of Robux price changes after Oct 2026.
- No official Roblox documentation in these items on regional pricing mechanics, price bounds, or how the setting changes purchasing behaviour.
- No controlled conversion data comparing odd versus round price points or regional versus uniform pricing.
- The 70% vs 27% developer share figure is unverified; check current DevEx rate and fees on official sources.
- Current ad credit price, ad bid ranges, and minimum bids are not confirmed by official sources here.
- The PBR upload Robux cost amount is not given.
- Current private server and VIP price rules beyond the 2020 free-allowed change are not documented here.
- Cumin's console and game price items (N6560 to N6566) and Q1592 concern non-Roblox game and hardware prices, so they were excluded as off-topic.
- N6431 (emissive strength) and N6482 (vague developer underpayment) were excluded as not pricing guidance or too vague.
- No data on Robux-to-USD conversion rates or how they affect price points for different countries.
- No conversion-rate or sales-volume data tied to these specific price points (75, 99, 149, 175, 199, 467, 545).
- No genre breakdown showing which price clusters are typical for which genre.
- No evidence on whether the 467 (non-round) price converted better or worse than 399 or 500.
- No regional or currency-by-country price data for these gamepasses.
- No ARPPU or payer-conversion benchmarks; the list data does not show how many players bought each pass.
- The DevEx rate comes from a secondary agency citation. Verify it on the primary Roblox DevEx page.
- The RoWatcher source has an invalid date (2026-00), so its timing relative to other sources is unknown.
- Max players per server (N7363, 35) is not pricing-related and was excluded.
- No pricing data from these items: no conversion rate, price-point, or elasticity evidence.
- Tax rates on wallet Robux purchases are not specified; they vary by region and are only noted as 'plus tax'.
- No information on whether the repurchase rate differs by region or payment method.
- No information on whether the 750 Robux test-upload cost changes over time or by account type.
- No guidance on how these costs compare to revenue for a given game size or genre.
- No data on conversion rate or revenue impact of the speed-multiplier ladder or the bulk-action price.
- No official Roblox guidance on upgrade-ladder design in these new items.
- Egg hatch timing (N7623) is not pricing and was not merged.
- Amiibo price (N7643) is a speaker guess for a non-Roblox product and was not merged as a benchmark.
- No source explains how in-game sell values relate to Robux purchase prices or conversion rates.
- No official Roblox documentation was cited for the shop items module or the Sales toggle; verify against DevHub and the Creator Dashboard.
- No data on whether a 1:2.5 location price step or a 1:5 sell-value ratio improves player progression or spending.
- No conversion-rate data by price point, sample sizes, or A/B test results in these additions. Ground any conversion claim in your own live tests.
- No official Roblox confirmation of the current DevEx rate or of the expedited review fee. Check the DevForum and developer documentation.
- No data on icon or thumbnail pricing outside PolarBear's portfolio, or on other service niches (UI, models, animation).
- No evidence on how economy tuning interacts with price changes in the same test window.
- Battle pass and other non-Roblox pricing is off-topic and was not used. Roblox-native subscription or battle-pass benchmarks are missing.
- No conversion-rate, ARPPU, or sale-lift measurements in this batch; cannot confirm whether surplus bundles or seasonal discounts raise revenue.
- Surplus-bundle claim (T18937) is the speaker's view only, with no test data.
- No DevEx, net-Robux, or dev-share figures; check official docs for current DevEx rate.
- No evidence on whether economy multiplier buffs (T18842) change retention or Robux spend.
- No official Roblox documentation in this batch; platform costs and sale rules need verification elsewhere.
- Area and egg prices are in-game currency with no Robux conversion.
- No official or verified source on how in-game currency converts to Robux or how it affects player spend.
- No conversion or sales data showing whether a Robux shortcut price increases payer conversion.
- No current (2026) Pets Go price or value data to confirm the 2024-11 and 2025-09 figures.
- No official data on drop-rate disclosure requirements for weather or secret-drop events.

## Quotes (near-verbatim)
- "there is no right answer to that question and it's I think the only way you can recover from it is to say that pricing is going to be something that we change" ([Roblox 2018-07 26:51](https://youtu.be/DWUfL8azgIk?t=1611))
- "Usually their core and only KPI is how much money they can bring in in a given year." ([Roblox Creators 2022-05 33:29](https://youtu.be/14RMDByrG1U?t=2009))
- "we want those to kind of represent the Rarity through their price" ([Roblox Creators 2023-01 2:54](https://youtu.be/okAygI1sxsA?t=174))
- "helping them make that decision by doing the math for them" ([Roblox Creators 2023-01 5:50](https://youtu.be/okAygI1sxsA?t=350))
- "Don't be ashamed of putting on those really low numbers, especially if it's a lower amount of currency" ([Roblox Creators 2023-03 0:07](https://youtu.be/Cli3ogW-azk?t=7))
- "Only show offers and only offer Dev products game passes to our players when they're good value." ([Roblox 2023-09 19:14](https://youtu.be/Z-ZKqBPdl44?t=1154))
- "if you make it 200 then it just doesn't look appealing... 199 that looks like eh I can probably spend that money" ([PolarBear 2024-02 2:02](https://youtu.be/nkmfdUbj4bQ?t=122))
- "Anchor pricing... prompt them with something that is very expensive or above the average price... then when they see a lower price and it's a really good deal, they will want to spend that money." ([Stewiepfing 2024-02 2:17](https://youtu.be/v8tFfBTr6M8?t=137))
- "I was absolutely blown away by this like bro it's actually like decent like good quality" ([ItsZyonic 2024-03 5:08](https://youtu.be/INsV8HkDHIA?t=308))
- "If I do, it will cancel everybody's private server subscription." ([Mulch 2024-06 4:10](https://youtu.be/pqCXX06vlDw?t=250))
- "it had to be just a no-brainer if you are spending on Roblox... it has to be the best offering" ([Roblox 2024-09 26:39](https://youtu.be/ETDit6eO4sQ?t=1599))
- "we did the 12-week trial of price optimization and I am a huge evangelist for it now" ([Roblox 2024-09 31:23](https://youtu.be/ETDit6eO4sQ?t=1883))
- "We spend a lot of time doing market research... we look at comparables we look at our own catalog like what is performing" ([Roblox 2024-09 28:00](https://youtu.be/NEK7jq1LFu8?t=1680))
- "There's an optimal price point for each item in different regions of the world." ([Roblox 2024-09 12:25](https://youtu.be/T7w3Q54JOPE?t=745))
- "My game could be balanced a little better, so I'm going to buff the pet multipliers by 30%." ([janisjanis01 2024-12 9:20](https://youtu.be/Jc7yQTMFexk?t=560))
- "I think this should not be a 10,000 Robux unit." ([Bemmy 2025-06 10:29](https://youtu.be/-Z0C5YJtnqY?t=629))
- "I'm almost always pricing at the price floor, because everybody's comparing themselves." ([Roblox Creators 2025-08 11:52](https://youtu.be/KSez8Ecq50A?t=712))
- "Brand new Roblox games are typically valued a lot lower than a game that is established." ([Roblox 2025-09 13:38](https://youtu.be/Z3T33q4-Y_A?t=818))
- "I price our top products based off of Robux bundles." ([1_Bruce 2026-03 4:05](https://youtu.be/zgq6L4ZzCHs?t=245))
- "We decided to set our prices extremely cheap just to boost like payer conversion rate, but honestly, during the peak of the game we probably could have doubled all these prices" ([Yann 2026-05 2:44](https://youtu.be/dbNA3K8lt2w?t=164))
- "You don't want to just make it like one bill money is like nine Robux. Like, that's going to cook you." ([Tizzy 2026-06 12:09](https://youtu.be/zoz3PSMqets?t=729))
- "give them the option to reroll for cheaper for like four or five Robux, and they keep rerolling" ([Alex Builds Games 2026-06 14:48](https://youtu.be/x_SflcuSi1w?t=888))
- "If you lock content behind day one DLC or special editions of the game, that means that was already done by the game's release." ([Cumin 2026-06 9:10](https://youtu.be/KNKxJ06w1Uo?t=550))
- "It's all about the timing and placement in the psychological levers that you're pulling at the exact right time." ([Tizzy 2026-07 17:26](https://youtu.be/nggNvUILQ1I?t=1046))
- "GTA can price whatever they want. Like this could have easily been 100, and would still sell absolutely well." ([Deconstructor of Fun 2026-07 3:33](https://youtu.be/i6F_0YVzhz8?t=213))
- "I think a lot of people are out there basically bitching because they left money on the table by not having a $100 SKU." ([Deconstructor of Fun 2026-07 5:35](https://youtu.be/i6F_0YVzhz8?t=335))
- "These offers are provided entirely by Roblox. Creators will continue to receive the normal payout based on the item's undiscounted price." ([Roblox DevForum 2026-09 ](https://devforum.roblox.com/t/roblox-provided-discounts-on-in-game-items/4861443))
- "We cut the prices of every game pass and dev product by half. What happened? Our revenue doubled." ([VuukStudios 2026-10 3:42](https://youtu.be/4vuXAQt0PuQ?t=222))
- "Higher prices does not mean better revenue." ([VuukStudios 2026-10 5:01](https://youtu.be/0ENzqNB_EUo?t=301))
- "Time is the big variable we use. We price what an hour of their time is worth to a paying user." ([Roblox 2026-10 13:11](https://youtu.be/qLP05zvMsW0?t=791))
- "A discount is not genuine if an item is always 'on sale' for the same amount of Robux." ([Roblox Creator Docs 2026-10 ](https://create.roblox.com/docs/production/monetization))

## Verified additions

_Hand-added, labelled and sourced rows kept in `youtube-learn/supplements/topics/pricing.md`; they survive rebuilds._

- **Expedited review costs 50,000 Robux per game (not 100,000)** (official, 2026-11-01): Current docs: one-time, refundable, auto-refunded 90 days after the game becomes eligible (or 90 days after payment if never eligible), forfeited only if permanently removed for Community Standards violations. 100,000 was the June 2026 launch price (creator Yann 'I would have paid the 100,000 Robux fee' is the older price). Review takes up to 48h; minor violations restart the clock. Sources: [Roblox Creator Docs kids-and-select 2026-11-01](https://create.roblox.com/docs/production/publishing/kids-and-select), [DevForum staff 2026-08-19](https://devforum.roblox.com/t/highly-engaged-player-threshold-drops-to-250/4820164), [DevForum Kids/Select launch 2026-06](https://devforum.roblox.com/t/roblox-kids-and-select-global-launch-upcoming-updates-to-eligibility-ads-manager-and-expedited-review/4685717). Newest source 2026-11-01.
- **Creator said $0.038 per Robux (WTMW20 'Where The Money Went', 2026-10); official DevEx rate is $0.0038 [OFFICIAL, docs 2026-11-01]; the $0.054 verified 18+ US figure is really $0.0054** (official): 10x error. Check: 700 Robux x $0.0038 = $2.66. Sources: [Roblox Creator Docs developer-exchange 2026-11-01](https://create.roblox.com/docs/production/monetization/developer-exchange). Newest source 2026-11-01.
- **Creator Rewards rules (replaces Premium/Engagement-Based Payouts since 2025-07-24)** (official, 2026-11-01): Daily Engagement = 5 Robux per Active Spender ($9.99+ qualifying purchases in 60 days) who plays 10+ min in one of their first 3 experiences that day; open to all creators, no enrolment. Audience Expansion = 35% of a new/reactivated user's first $100 of purchases in 60 days; needs an ID-verified account and the experience averaging 100+ DAU for 60 days. Rewards are Earned Robux with a 60-day hold; cash-out is under DevEx terms. Docs publish no per-minute Premium rate, so older Premium-payout figures (e.g. 5 Robux per 10 minutes, Mulch/PineappleDev 2020-2024) are historical. Sources: [Roblox Creator Docs creator-rewards 2026-11-01](https://create.roblox.com/docs/creator-rewards), [engagement-based-payouts](https://create.roblox.com/docs/production/monetization/engagement-based-payouts). Newest source 2025-07-24.

## Appendix: every extracted tip on this topic

- 2018-07-22 Emancyphur [7:15](https://youtu.be/RUqr6lj1UYI?t=435): Do not change the VIP server price while servers exist; changing it cancels existing subscriptions and can upset buyers.
- 2018-07-24 Roblox [3:14](https://youtu.be/DWUfL8azgIk?t=194): Test prices with live data: Alex changed coin-to-Robux price points over three to six months and doubled revenue.
- 2018-07-24 Roblox [15:12](https://youtu.be/DWUfL8azgIk?t=912): Tie big sales to national holidays, pair them with free limited events for non-payers, and keep sales rare so players don't wait for discounts.
- 2018-07-24 Roblox [26:51](https://youtu.be/DWUfL8azgIk?t=1611): There is no formula for pricing; start at a price, lower it if few buy, and raise it on the next version.
- 2018-08-07 AlvinBlox [26:40](https://youtu.be/h92s4Xn26oc?t=1600): In the speaker's example, 100 cash was priced at 10 Robux; set Developer Product prices in the Configure Place Developer Products tab.
- 2019-08-15 Roblox DevForum [page](https://devforum.roblox.com/t/ugc-catalog-is-now-live/331405): Initial UGC Hat price floor was 120 R$; floors and ceilings were set from price ranges Roblox saw the most success with and could change.
- 2019-10-11 Last Level Studios [23:29](https://youtu.be/vY0om5O-Oh8?t=1409): Keep game pass and product prices roughly 10 to 150 Robux, since most players have little Robux.
- 2020-02-14 Last Level Studios [36:19](https://youtu.be/_LdpUJ41cso?t=2179): Track gamepass price changes day by day to see whether a price cut or rise increases total revenue, not just sales.
- 2021-02-26 Roblox DevForum [page](https://devforum.roblox.com/t/increasing-premium-payouts-starting-today/1072865): Premium Payouts pay developers based on engagement scores of Premium users; the rate per Robux changed multiple times, so check current DevHub docs rather than old figures.
- 2021-03-27 Roblox DevForum [page](https://devforum.roblox.com/t/developing-expert-developers-advice-from-all-around-the-world/1134437): Price commissions by hourly rate plus a complexity premium, e.g. $15/hr x 6 hrs with a 30% premium for moderate detail.
- 2021-05-17 Roblox DevForum [page](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207): Price entry items around 50-400 Robux, gameplay items 400-6000, and whale items above 6000; increase price per milestone offer.
- 2021-05-17 Roblox DevForum [page](https://devforum.roblox.com/t/roblox-game-monetization-guide/1235207): Price escalating tiers as: 450, 1000, 2200 by doubling the previous price and adding 100 (or 200 for the last one). Check competitor prices and put slow sellers on limited sale.
- 2021-08-12 Roblox Creators [26:01](https://youtu.be/4-vZkSrGAxI?t=1561): Prorate prices by progression: scale soft-currency bundle costs and timer-skip prices down as players advance, if your platform allows it.
- 2021-09-05 Mulch [5:22](https://youtu.be/yG44d_Xnbwg?t=322): Game pass prices varied from 4.99 to 399 Robux; the 75 Robux pass sold most (38), while the 399 Robux pass sold only 6.
- 2021-10-21 Roblox Creators [57:57](https://youtu.be/d4g30UupgKw?t=3477): To slow consumption, add player-level gates or raise soft-currency prices instead of blocking players entirely.
- 2022-08-30 GameMakers [30:52](https://youtu.be/JVCao-Yhu2M?t=1852): Economy sources/sinks and difficulty tuning can yield large LTV lifts (reported up to ~20% and ~10%) for modest effort; prioritise these tuning tests.
- 2023-01-12 Roblox Creators [2:54](https://youtu.be/okAygI1sxsA?t=174): Price rare items higher based on how the community already values them; price newer items lower so their value can saturate naturally.
- 2023-01-12 Roblox Creators [5:07](https://youtu.be/okAygI1sxsA?t=307): Show the effective in-game currency per Robux for each bundle tier so players can see value rising with bigger bundles.
- 2023-01-19 Roblox Creators [0:00](https://youtu.be/YdplC2WVkWc?t=0): Price items by time-to-earn: compare what a free player grinds for (e.g. 8 hours) against the Robux price, then price higher if you want grinding preferred.
- 2023-01-19 Roblox Creators [0:00](https://youtu.be/YdplC2WVkWc?t=0): Highlight the best-value bundle and show per-Robux value or bonus percentages so players don't have to do the math.
- 2023-01-26 Roblox Creators [9:47](https://youtu.be/vQNJztcS2AI?t=587): Don't cut prices just because players ask; respond when many players request the same change, and keep prices fair for your team.
- 2023-01-26 Roblox Creators [11:26](https://youtu.be/vQNJztcS2AI?t=686): Start prices by comparing similar items in other games, then adjust for time invested and how much the item adds to the experience.
- 2023-01-26 Roblox Creators [21:23](https://youtu.be/vQNJztcS2AI?t=1283): Offer a wide range of Robux price points, including very low ones (Griffin's Destiny has a 35 Robux option), since many players can't pay much.
- 2023-03-09 Roblox Creators [0:47](https://youtu.be/Cli3ogW-azk?t=47): Include very low Robux price points (e.g. 35 Robux in Griffin's Destiny) so players with little Robux can convert.
- 2023-03-09 Roblox Creators [0:47](https://youtu.be/Cli3ogW-azk?t=47): Offer low-amount currency bundles rather than being ashamed of small numbers; otherwise low-balance players spend Robux elsewhere.
- 2023-08-18 SimTek Game Development [2:46](https://youtu.be/U22nZqDmTXI?t=166): Set the gamepass price to 1 Robux while testing to limit cost; the speaker notes Roblox takes 70% of sales.
- 2023-09-19 Roblox [5:51](https://youtu.be/9eaev-ypgWo?t=351): Use measured earnings per hour to price developer products, e.g. price a bundle to skip roughly 3 to 6 hours of in-game earning.
- 2023-09-19 Roblox [19:14](https://youtu.be/Z-ZKqBPdl44?t=1154): Only show offers and dev products/game passes when they're good value; a poor-value starter pack reduced total spend in Base Battles.
- 2023-09-19 Roblox [22:02](https://youtu.be/Z-ZKqBPdl44?t=1322): Test price points: Encounters' 650 Robux product converted worse than 400/300/250, but revenue per user rose at lower prices; find the sweet spot.
- 2023-10-23 SmartyRBX [10:18](https://youtu.be/vemqKJ-5yRE?t=618): Estimate build cost and realistic earnings upfront so you don't start a project that needs more money than it can return.
- 2023-12-31 Roblox DevForum [page](https://devforum.roblox.com/t/understand-the-roblox-algorithm/2772921): Keep early offers cheap: new players rarely spend much Robux in their first 10-30 minutes.
- 2024-02-02 PolarBear [2:02](https://youtu.be/nkmfdUbj4bQ?t=122): Price gamepasses at odd numbers like 199 Robux rather than round 200; speaker argues it looks like a cheaper, more appealing price.
- 2024-02-02 PolarBear [4:07](https://youtu.be/nkmfdUbj4bQ?t=247): Set a cheap entry gamepass (custom name at 29 Robux) to lower the barrier to a first purchase.
- 2024-02-16 Stewiepfing [1:36](https://youtu.be/v8tFfBTr6M8?t=96): Show a very expensive gamepass (e.g. 900 Robux) as soon as players join so cheaper items (100-200 Robux) look like good deals.
- 2024-04-06 ByteBlox [5:15](https://youtu.be/7NRp4BEYrsQ?t=315): Use GetSubscriptionProductInfoAsync from a LocalScript (run context client) to show localized display price, since prices vary by region.
- 2024-06-30 Mulch [4:10](https://youtu.be/pqCXX06vlDw?t=250): Avoid lowering private server price once sold; changing it cancels existing subscriptions. Price was kept at 50 Robux since launch.
- 2024-07-19 PolarBear [7:28](https://youtu.be/tkAis2wTxms?t=448): Start icon/thumbnail design services around 200-250 Robux per icon, then raise prices as your portfolio and reputation grow.
- 2024-08-30 VuukStudios [2:39](https://youtu.be/3J7Vp6NgYf4?t=159): Price game passes higher than developer products, since each is bought once and must earn its lifetime revenue.
- 2024-09-23 Roblox [26:39](https://youtu.be/ETDit6eO4sQ?t=1599): Pick a subscription price you can hold long-term (Adopt Me chose $2.99 and won't raise it) and make it the best offer on the platform.
- 2024-09-23 Roblox [31:23](https://youtu.be/ETDit6eO4sQ?t=1883): Use Price Optimization to test dev product and gamepass prices over about 2 weeks and apply suggested prices with one click; Adopt Me saw +3.5% revenue over 12 weeks.
- 2024-09-23 Roblox [16:58](https://youtu.be/ETDit6eO4sQ?t=1018): Do not copy competitor prices; test prices on your own audience to maximise volume times price.
- 2024-09-23 Roblox [18:21](https://youtu.be/ETDit6eO4sQ?t=1101): Set item prices per region to reflect purchasing power; Roblox will offer regional recommendations, with you keeping final say.
- 2024-09-23 Roblox [32:44](https://youtu.be/ETDit6eO4sQ?t=1964): Manual price testing is a lot of work (setup, run, analysis); automated optimization saves that time, though it may find no uplift if you are already at equilibrium.
- 2024-09-23 Roblox [7:26](https://youtu.be/NEK7jq1LFu8?t=446): Set price relative to dynamic price floor: price = floor + your offset. Optionally set a minimum sales price so the floor cannot drag your item below it.
- 2024-09-23 Roblox [28:00](https://youtu.be/NEK7jq1LFu8?t=1680): Price by market research: compare comparables and your own catalog, test new styles first, and price higher for items that took long to make.
- 2024-09-23 Roblox [30:04](https://youtu.be/NEK7jq1LFu8?t=1804): Keep most items affordable for typical players and make only a few expensive exclusives.
- 2024-09-23 Roblox [11:45](https://youtu.be/T7w3Q54JOPE?t=705): Prepare for experience price optimization and future regional pricing; set different virtual item price points per market rather than one global price.
- 2024-12-01 janisjanis01 [9:20](https://youtu.be/Jc7yQTMFexk?t=560): Balance pet multipliers with a global buff when the economy feels weak; the speaker raised most pet multipliers by about 25%.
- 2024-12-12 VuukStudios [12:06](https://youtu.be/xBPJnMgLoUE?t=726): Expect payouts in DevEx rates, far below Robux purchase value; 1,000 Robux is roughly one dollar at DevEx rates, so price work accordingly.
- 2024-12-15 janisjanis01 [13:40](https://youtu.be/HGobKizBHqQ?t=820): Run a seasonal sale with gamepasses at 50% off and a discounted server luck pass (25 Robux); the speaker says this is a one-off.
- 2025-01-15 CallMeDogey [10:14](https://youtu.be/USJC5l_wpuY?t=614): Price developer products across spending levels (cheap to ~10,000 Robux) so both low and high spenders have an option.
- 2025-02-06 ArTheDev [3:14](https://youtu.be/JtZ8RzQaQco?t=194): Set a game pass price by opening the pass, turning Sales on, and entering the price.
- 2025-04-17 Roblox Creators [2:53](https://youtu.be/Zb1BJow0NV4?t=173): Publishing advance: until recouped, your item earns 70% of Robux instead of 30%. A 1,500 Robux hat at 95 Robux needs about 22-23 sales to recoup.
- 2025-05-21 {EISABOOS} "RBX" [1:35](https://youtu.be/Q2qfVxcGat4?t=95): Uncheck regional pricing on the pass sales settings so one Robux price applies everywhere.
- 2025-05-28 Arow [0:45](https://youtu.be/JeBDqH7INjY?t=45): Set a rate you charge per job, then raise or lower it until you find the price that maximises both total earnings and number of commissions.
- 2025-05-30 Perstile [2:14](https://youtu.be/ET3fRqaFmFc?t=134): Underpriced best seller: creator says the 500-Robux double-size product should have cost more; he estimates roughly 2x revenue at a higher price.
- 2025-06-09 Roblox Creators [41:10](https://youtu.be/D_YmdVZxIZw?t=2470): Start with a budget you're comfortable with; increase only if cost per play matches your goals, since there is no max bid in the new flow.
- 2025-06-28 SmartyRBX [1:05](https://youtu.be/Lplz7ZFcKlQ?t=65): Charge what your work is worth and set revision limits and scope in writing before starting any commission; he undercharged and overworked on a 35,000 Robux job.
- 2025-07-06 SmartyRBX [8:34](https://youtu.be/Gml4to_jXQ0?t=514): Use scarcity and urgency when selling templates or packs, e.g. capping buyers to around 30, to speed purchases.
- 2025-08-15 Roblox Creators [11:52](https://youtu.be/KSez8Ecq50A?t=712): Price at the price floor rather than high, since buyers compare prices and undercutting happens often. Luxury items can be priced higher.
- 2025-08-15 Roblox Creators [11:52](https://youtu.be/KSez8Ecq50A?t=712): Release one major item free to build hype, and price a recolor of it, which Rush says often sells higher and lifts the rest of the set.
- 2025-08-25 {EISABOOS} "RBX" [1:28](https://youtu.be/5dfKSg_wqLA?t=88): Turn off regional pricing on game passes if you want uniform prices and maximum revenue from high-income regions; leave it on only if you want broader affordability.
- 2025-08-26 Arow [1:22](https://youtu.be/yM28oinpQIo?t=82): Set UGC accessory prices to a minimum of 50 Robux, per the creator's advice.
- 2025-08-29 Roblox Creators [17:45](https://youtu.be/7AtvvUxvCaU?t=1065): Set rewarded reward value around 3-10 Robux equivalent so players don't abandon mid-ad; experiment from there.
- 2025-09-26 Roblox [5:06](https://youtu.be/MJ-zYfL10Ew?t=306): Use price optimization and regional pricing rather than guessing; Roblox says recommended prices come with no engagement loss.
- 2025-09-26 Roblox [25:54](https://youtu.be/MJ-zYfL10Ew?t=1554): Constrain supply through pricing in trading games so monetized items hold value; Adopt Me considers future resale value, not just the purchase price.
- 2025-09-26 Roblox [26:35](https://youtu.be/MJ-zYfL10Ew?t=1595): Set entry-level prices so spenders with small budgets still get value, leaving high-value tiers for scarcity-driven trading items.
- 2025-09-26 Roblox [29:17](https://youtu.be/MJ-zYfL10Ew?t=1757): Estimate average revenue per paying user by genre before greenlighting; hyper-casual may be about $2 ARPPU while tower defense may be near $20.
- 2025-09-26 Roblox [18:30](https://youtu.be/Tese1QLD3nU?t=1110): Price avatar items above the price floor to qualify for higher revenue share: up to 70% instead of the standard 30%, visible on the creator dashboard.
- 2025-12-01 Roblox Creators [18:16](https://youtu.be/-CdXP025MvU?t=1096): Test starter pack prices, included items and presentation; payer conversion rate is a key metric to watch.
- 2025-12-04 {EISABOOS} "RBX" [3:02](https://youtu.be/skRRdrpf2F4?t=182): Turn off 'Use regional pricing' for donation-style game passes; the speaker says regional pricing can behave incorrectly and may let players in some countries pay fewer Robux.
- 2025-12-04 {EISABOOS} "RBX" [3:02](https://youtu.be/skRRdrpf2F4?t=182): Regional pricing adjusts a pass's Robux cost by country purchasing power; a 10 Robux default may cost only 4 Robux in lower-income regions.
- 2025-12-18 Ventures [20:47](https://youtu.be/Nb50UhXcpRM?t=1247): Brand integrations can cut revenue. Developers have seen a 4-week sponsorship make less than leaving the game alone, because players dislike diluted experiences.
- 2026-01-29 VuukStudios [1:26](https://youtu.be/Iy5cO3Nanhc?t=86): Check current DevEx rate (e.g. via a Robux-to-USD calculator site) before cashing out; rate rose ~15% per the creator.
- 2026-02-20 1_Bruce [3:50](https://youtu.be/i3RQXxZeVYc?t=230): If your audience is young or low-income, price items very low to keep payer conversion up. Target older, higher-income players where possible.
- 2026-03-15 1_Bruce [4:05](https://youtu.be/zgq6L4ZzCHs?t=245): Price top products to match Robux bundles, e.g. a 1,800 Robux gamepass bundle equal to the Robux received for a $20 Robux purchase. Speaker says this worked very efficiently.
- 2026-04-01 Roblox DevForum [page](https://devforum.roblox.com/t/let-your-players-pay-for-subscriptions-within-experiences-in-robux/4552995): Robux subscriptions can start at 49 Robux, lowering the price floor to reach more players.
- 2026-04-01 Roblox DevForum [page](https://devforum.roblox.com/t/let-your-players-pay-for-subscriptions-within-experiences-in-robux/4552995): Price changes are allowed every 60 days. Price increases give subscribers 30 days' notice; decreases apply at next renewal.
- 2026-04-30 rasdev [2:41](https://youtu.be/yFKY2FlwHjE?t=161): Sell currency in bundle amounts that leave a surplus, since players tend to spend the leftover rather than let it go to waste.
- 2026-05-12 Yann [2:44](https://youtu.be/dbNA3K8lt2w?t=164): Price cheap early to boost payer conversion; the creator says at peak they could have doubled prices and sales would still have held.
- 2026-05-30 Yann [6:48](https://youtu.be/yw32DZtz4mQ?t=408): In the first week, sell gamepasses and products at roughly half price to get a realistic payer conversion rate and ARPPU from ad traffic.
- 2026-06-15 Tizzy [13:50](https://youtu.be/zoz3PSMqets?t=830): Keep impulse items cheap (19 Robux for 2x offline earnings), but avoid very low prices like 9 Robux on cash that undercut your economy.
- 2026-06-16 Alex Builds Games [14:48](https://youtu.be/x_SflcuSi1w?t=888): Offer cheaper rerolls (about 4-5 Robux) on crates so players keep rerolling; speaker says this was a main earner in a past game.
- 2026-07-03 Generalist Programmer [5:23](https://youtu.be/CFohgybeybM?t=323): Remember players pay Robux but developers keep only ~70% after the marketplace cut; a 1,000 Robux spend yields ~700 earned Robux (~$2.66).
- 2026-07-13 Tizzy [16:44](https://youtu.be/nggNvUILQ1I?t=1004): Show a teaser of rare pets on the first roll. Changing roll teases raised PCR from 0.3% to 0.75% per the creator.
- 2026-07-14 MoseyTube [2:32](https://youtu.be/-PoyiiGhoNo?t=152): Price consumables high enough to earn but low enough not to break the in-game economy; aim for a no-brainer purchase price.
- 2026-07-15 Roblox DevForum [page](https://devforum.roblox.com/t/scribe-v261-persistent-typed-auto-replicated-player-data-built-on-profilestore/4738905): Show per-player prices via Data.ObserveProductInfo, since Roblox Plus subscribers pay 10 to 20% less and regional pricing can be 30% of list.
- 2026-07-24 MoseyTube [3:47](https://youtu.be/a170E9klbP4?t=227): Offer multiple price points within one system, e.g. cosmetic chairs from $100 up to a $150 gaming chair.
- 2026-08-06 VuukStudios [7:22](https://youtu.be/aw0PmBkakb4?t=442): Do not set high Robux prices if your community is mostly from low-spending regions; expensive items cut conversion sharply.
- 2026-08-16 VuukStudios [9:42](https://youtu.be/Tk0qXybUK0E?t=582): Check which regions play most and set gamepass prices accordingly; North American players can support higher prices than Asian or South American markets.
- 2026-08-25 MoseyTube [4:26](https://youtu.be/xIBc5He_sy4?t=266): Aim for purchase conversion and conversion rates around 2-3%, which he calls healthy for this monetization setup.
- 2026-09-01 VuukStudios [4:04](https://youtu.be/2Q4NqQikzsY?t=244): Choose 18+ DevEx-qualified audience only if your game suits older players; it pays ~42% more per Robux but yields fewer players.
- 2026-09-01 VuukStudios [5:26](https://youtu.be/2Q4NqQikzsY?t=326): Raise gamepass and dev product prices during a big push, then revert to normal prices when traffic settles.
- 2026-09-09 Roblox DevForum [page](https://devforum.roblox.com/t/roblox-provided-discounts-on-in-game-items/4861443): Roblox-funded discounts do not reduce your payout: you still earn based on the item's undiscounted price, so discounts cost you nothing.
- 2026-09-11 Roblox DevForum [page](https://devforum.roblox.com/t/introducing-roblox-wallet-and-card-get-paid-faster/4865505): Wallet holders can buy Robux at the DevEx rate ($0.0038/Robux) to fund publishing, testing and ads without buying back at retail price.
- 2026-09-12 Mulch [1:18](https://youtu.be/WYODms_JMRA?t=78): Speed multiplier upgrades form a Robux ladder (460, 600, 876, 1,268 Robux) with rising tiers; each step visibly boosts earnings, which encourages spending.
- 2026-10-01 Where The Money Went [12:58](https://youtu.be/cJHug1Wnmhw?t=778): Selling in real dollars (Creator Store, paid access) keeps far more revenue than Robux: about 70% of proceeds versus about 27% through DevEx.
- 2026-10-03 VuukStudios [3:42](https://youtu.be/4vuXAQt0PuQ?t=222): Check your player country breakdown and set gamepass/devproduct prices for that audience; creator halved all prices and revenue reportedly doubled.
- 2026-10-03 VuukStudios [5:45](https://youtu.be/4vuXAQt0PuQ?t=345): Don't use US-level prices if most players are from lower-income countries; players there often can't afford 300 Robux passes but can afford ~100.
- 2026-10-03 MonarchDev [5:53](https://youtu.be/bbCmt98O9MA?t=353): Simulate progression math before launch. A free egg was hit 130 times (about $6,500 in 30 seconds), so every rebirth price was rebuilt.
- 2026-10-11 VuukStudios [4:20](https://youtu.be/0ENzqNB_EUo?t=260): Check your actual player country breakdown and price for it; he halved dev product and gamepass prices for a mostly Mexico audience and revenue rose about 5x.
- 2026-10-12 Xaiyne [2:48](https://youtu.be/KhKOSmdX8sc?t=168): Turn off PBR in the generator when uploading to Roblox, since PBR costs extra Robux to upload.
- 2026-10-12 Roblox [18:23](https://youtu.be/gCp4zzjjJ14?t=1103): Emissive UGC has a higher price floor by design, to protect the novelty of the new tech from being washed out.
- 2026-10-12 Roblox [13:11](https://youtu.be/qLP05zvMsW0?t=791): Balance free and paying players by time: estimate how long something takes to earn and price it at what an hour of the player's time is worth.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/education/adventure-game-series/finishing-the-project): Set player bag Spaces to 6-10 as a starting point, then playtest to find the right number.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/roblox-plus): Don't hard-code prices; use GetProductInfoAsync and GetDeveloperProductsAsync so Plus subscribers see the discounted price, avoiding UI mismatch.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/analytics/monetization): Sell items across a wide range of Robux price points to fit users with different spending habits.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/analytics/monetization): Offer welcome offers and discounts for first-time purchasers to lower the barrier to trying paid content.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/get-started/monetization): Use Price Optimization to auto-test price points on user subsets and find the revenue-maximizing price.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/get-started/monetization): Use Regional Pricing to auto-set local item prices; early tests showed spending gains in Mexico, Brazil and the Philippines.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/ui/video-frames): Each video upload costs 2,000 Robux, so budget for upload costs before adding video content.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/ai/build): Purchased Build credits (bought with Robux) do not expire; free prompts reset daily.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/paid-access-local-currency): Desktop local-currency paid access revenue share tiers: $9.99 gives 50%, $29.99 gives 60%, $49.99 gives 70%, before taxes/VAT.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/subscriptions): Robux subscriptions must be at least 49 Robux; local-currency subscriptions must use one of $2.99, $4.99, $7.99, $9.99, or $14.99.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/subscriptions): Robux subscription price can only change once every 60 days, and increases need 30 days' notice. Local-currency prices cannot be changed; delete and recreate instead.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization): Discounts must be genuine and fair: an item permanently 'on sale' at the same price, or a discount lasting only briefly, is not allowed.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud-services/extended-services): Set a monthly budget per resource; billing occurs at month end or when usage reaches $10 USD, whichever comes first. Minimum budget is $0.50 USD.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/private-servers): The Robux price you set for paid private servers directly determines how much you earn per sale.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/game-design/subscription-design): When pricing currency packs, compare the new pack's contents to existing single-purchase Robux offerings to keep relative value consistent.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/commerce-products): Product detail page supports up to five Additional Information accordions via Shopify metafields in the Roblox.pdp_info_ namespace.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/promotion/ad-integrations): From 2027, cap campaign cost by shortening duration or toggling the campaign off once impression targets are reached; deals are capped at $400,000.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/experiments): Use shop visibility, starter pack type and pricing as monetisation experiment candidates, measured by ARPU, ARPPU and payer conversion rate.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/marketplace/marketplace-fees-and-commissions): Price avatar items above the asset type's floor to earn more: at 2x the floor creators get 50% instead of 30%. Marketplace only; in-game sales stay at 30%.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/regional-pricing): Set your default global price carefully: regional prices never exceed it and never drop more than 70% below it (100 Robux default means a 30 Robux floor).
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/publishing/kids-and-select): Use the expedited review fee (50,000 Robux, refundable) only for timed launches or off-platform campaigns that need a guaranteed all-ages date.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/avatar-creation-token): To offer different price points for same-type items in your game, purchase multiple tokens rather than one.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/avatar-creation-token): Set the Amount Above Price Floor and optional Do not price below minimum; both can be modified after creation.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/creator-store): Set model prices between $2.99 and $49.99 and plugin prices between $4.99 and $249.99 in USD.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/paid-access-robux): The price you set directly determines how many Robux you earn per sale. Choose it within the 25 to 1000 Robux range.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/price-optimization): Make sure product prices are scripted via MarketplaceService (not hard-coded) before price optimization; hard-coded prices can't be tested or changed.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/price-optimization): Run the Dynamic Price Check tool with test accounts to find which prices are hard-coded: if the price changes on the fake price, it's scripted; if not, it's hard-coded.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/price-optimization): Only run price optimization once the game has about 60,000 transactions over the previous 30 days, so the test produces significant data.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/price-optimization): Include all passes and developer products in the test for best results.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/price-optimization): Review the results after the test; optimized prices are applied only when they produce positive incremental total revenue.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/price-optimization): Use the price review period afterward to track long-term revenue impact of price changes.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/price-optimization): Stop a test anytime from Managed Pricing; products revert to original prices. Prices of tested products can't be edited while a test runs.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/price-optimization): Use GetProductInfo with Enum.InfoType.Product for developer products and Enum.InfoType.GamePasses for passes when scripting prices, since the default InfoType fetches assets.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/marketplace/publish-to-marketplace): Set price as Amount Above Price Floor (can be 0) plus optional Do Not Price Below floor to guarantee a minimum sale price.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/managed-pricing): Before opting in, remove hard-coded prices from your game; managed pricing prompts you to fix them first.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/managed-pricing): Regional prices are bounded between 30% and 100% of the default price; expect discounts up to 70% for lower-purchasing-power regions.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/managed-pricing): Use the Managed Pricing tab's bulk enable/disable and per-item opt-out to control which passes and products are tested.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/avatar/animation-packs): Marketplace price floor for animation packs is 300 Robux; this is the minimum selling price, not an extra fee.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/developer-products): Developer product prices must be between 1 and 1,000,000,000 Robux.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/promotion/rewarded-video-playbooks/tycoon): Balance reward value: enough that 30 seconds of watch time feels worth it, but not so generous it cannibalises in-game purchases or breaks the economy.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/education/resources/frequently-asked-questions-education): Private servers are set by individual developers, often around $1 USD per month, not by Roblox.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/monetization/paid-random-items): When offering direct purchase to restricted users, price the guaranteed item at its expected value; e.g. a 10 Robux box with 5% odds for a rare sword implies 200 Robux.

Index: [[README]] | Master: [[master-playbook]]
