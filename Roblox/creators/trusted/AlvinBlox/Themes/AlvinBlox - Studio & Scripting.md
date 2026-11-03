---
title: AlvinBlox - Studio & Scripting
creator: AlvinBlox
tags: [roblox, alvinblox, theme]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# AlvinBlox: Studio & Scripting

All AlvinBlox tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[scripting-and-performance]]
- 2018-08-07 [2:31](https://youtu.be/h92s4Xn26oc?t=151) Name the folder exactly 'leaderstats' (lowercase l, correct casing) or the leaderboard will not appear in the top-right corner. ([[2018-08-07 - Roblox Currency Script System Tutorial - Monetise your Game|Roblox Currency Script System Tutorial - Monetise ]])
- 2018-08-07 [5:12](https://youtu.be/h92s4Xn26oc?t=312) Use the player's UserId in the DataStore key, not their name, and never rename the DataStore after publishing or player data gets wiped. ([[2018-08-07 - Roblox Currency Script System Tutorial - Monetise your Game|Roblox Currency Script System Tutorial - Monetise ]])
- 2018-08-07 [9:17](https://youtu.be/h92s4Xn26oc?t=557) Wrap DataStore GetAsync in pcall so a DataStore error is handled instead of breaking the whole script. ([[2018-08-07 - Roblox Currency Script System Tutorial - Monetise your Game|Roblox Currency Script System Tutorial - Monetise ]])
- 2018-08-07 [12:58](https://youtu.be/h92s4Xn26oc?t=778) Save player data in PlayerRemoving and kick all players in BindToClose with a short wait, so the last player's data is saved before the server shuts down. ([[2018-08-07 - Roblox Currency Script System Tutorial - Monetise your Game|Roblox Currency Script System Tutorial - Monetise ]])
- 2018-08-07 [20:37](https://youtu.be/h92s4Xn26oc?t=1237) Enable Studio Access to API Services in game config to test DataStores in Play Solo; note Studio writes to the live DataStore used by real servers. ([[2018-08-07 - Roblox Currency Script System Tutorial - Monetise your Game|Roblox Currency Script System Tutorial - Monetise ]])
- 2018-08-07 [31:31](https://youtu.be/h92s4Xn26oc?t=1891) In ProcessReceipt, store each PurchaseId in a DataStore and check it before granting, so a purchase is never granted twice; return PurchaseGranted only after rewards are saved. ([[2018-08-07 - Roblox Currency Script System Tutorial - Monetise your Game|Roblox Currency Script System Tutorial - Monetise ]])
- 2018-08-07 [35:45](https://youtu.be/h92s4Xn26oc?t=2145) If the buyer has left before ProcessReceipt fires, return NotProcessedYet so the reward is granted when they rejoin. ([[2018-08-07 - Roblox Currency Script System Tutorial - Monetise your Game|Roblox Currency Script System Tutorial - Monetise ]])
- 2020-06-01 [8:18](https://youtu.be/spFZ44yqIII?t=498) Countdown to an event: subtract os.time() from the start timestamp to get seconds remaining. ([[2020-06-01 - How to make a LIVE EVENT - Roblox Tutorial|How to make a LIVE EVENT - Roblox Tutorial]])
- 2021-01-23 [0:31](https://youtu.be/fivk8yp-VT4?t=31) Learn by picking apart free models and open-source code to see why developers made their scripting decisions, not just copying them. ([[2021-01-23 - How pro Roblox developers learnt to script|How pro Roblox developers learnt to script]])
- 2021-01-23 [0:31](https://youtu.be/fivk8yp-VT4?t=31) When stuck, google the exact error message or API name instead of blindly following tutorials, so you learn how the code works. ([[2021-01-23 - How pro Roblox developers learnt to script|How pro Roblox developers learnt to script]])
- 2021-01-23 [2:24](https://youtu.be/fivk8yp-VT4?t=144) Read every line of a reference script and look up each unfamiliar call in the API reference until you understand what it does. ([[2021-01-23 - How pro Roblox developers learnt to script|How pro Roblox developers learnt to script]])
- 2021-01-23 [3:45](https://youtu.be/fivk8yp-VT4?t=225) Before using a new API or mechanic, find a practical example of someone else using it, then check the API docs with that context. ([[2021-01-23 - How pro Roblox developers learnt to script|How pro Roblox developers learnt to script]])
- 2021-01-23 [1:14](https://youtu.be/fivk8yp-VT4?t=74) Learn what code elements do rather than only how to make one thing, so you can plan new scripts yourself. ([[2021-01-23 - How pro Roblox developers learnt to script|How pro Roblox developers learnt to script]])
- 2024-06-04 [2:32](https://youtu.be/5YNFRCD0pd0?t=152) Process purchases on the server in MarketplaceService.ProcessReceipt because server handling is authoritative and cannot be exploited by clients. ([[2024-06-04 - Make MONEY on Roblox with Developer Products - Roblox Scripting Tutori|Make MONEY on Roblox with Developer Products - Rob]])
- 2024-06-04 [4:31](https://youtu.be/5YNFRCD0pd0?t=271) Return Enum.ProductPurchaseDecision.PurchaseGranted only after delivering goods; return NotProcessedYet if the player is missing so the purchase is retried next join. ([[2024-06-04 - Make MONEY on Roblox with Developer Products - Roblox Scripting Tutori|Make MONEY on Roblox with Developer Products - Rob]])
- 2024-06-04 [7:17](https://youtu.be/5YNFRCD0pd0?t=437) Check the player exists with Players:GetPlayerByUserId before granting items, since they may have left mid-purchase. ([[2024-06-04 - Make MONEY on Roblox with Developer Products - Roblox Scripting Tutori|Make MONEY on Roblox with Developer Products - Rob]])
- 2024-06-04 [8:36](https://youtu.be/5YNFRCD0pd0?t=516) Store one handler function per product ID in a table and dispatch by ID, so adding products means adding a table entry instead of more if/elseif branches. ([[2024-06-04 - Make MONEY on Roblox with Developer Products - Roblox Scripting Tutori|Make MONEY on Roblox with Developer Products - Rob]])

## [[building-art-and-assets]]
- 2025-03-22 [5:35](https://youtu.be/dtRGRx-2WNg?t=335) Sell assets that solve a pain point (environment packs, UI kits) since they can be created once and sold repeatedly. ([[2025-03-22 - 4 Ways to Earn REAL MONEY from Roblox Games|4 Ways to Earn REAL MONEY from Roblox Games]])

Up: [[AlvinBlox - How to make successful Roblox games]]
