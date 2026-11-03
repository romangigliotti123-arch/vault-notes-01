---
title: "How Video Game Economies are Designed"
url: https://youtu.be/Zrf1cou_yVo
creator: Game Maker's Toolkit
official: false
advice_density: medium
date: 2022-04-25
views: 1269805
transcript: manual-subs
confidence: high
tags: [roblox, leads, youtube-learn]
---

# How Video Game Economies are Designed

[Watch](https://youtu.be/Zrf1cou_yVo) | leads | 1,269,805 views | 2022-04-25

## Summary
Mark Brown's crash course on video game economy design. Maps five entities: taps (resource generation), inventories (storage limits), converters (exchanging resources, shops, crafting, XP), drains (permanent resource removal), and traders (NPC buyers/sellers with supply/demand). Covers grind management via puzzle-ification, negative feedback loops, drains for risk, and trader market dynamics to prevent exploits.

## Tips
- [0:44](https://youtu.be/Zrf1cou_yVo?t=44) **[[core-loops-and-game-design]]** Design economy entities deliberately: taps create resources, inventories store them, converters spend them, drains remove them, traders trade them. Map your loop against these.
- [1:54](https://youtu.be/Zrf1cou_yVo?t=114) **[[core-loops-and-game-design]]** Use taps to incentivise behaviour: put loot on enemies to encourage fighting, unique materials per biome to encourage exploration.
- [3:04](https://youtu.be/Zrf1cou_yVo?t=184) **[[core-loops-and-game-design]]** Set inventory upper limits to force meaningful choices and stop players hoarding resources they never use.
- [4:29](https://youtu.be/Zrf1cou_yVo?t=269) **[[core-loops-and-game-design]]** Control progression pace by tuning converter costs or tap output; XP cost vs. XP per kill tells you roughly how many kills before a power-up.
- [5:13](https://youtu.be/Zrf1cou_yVo?t=313) **[[core-loops-and-game-design]]** Fewer currencies or shared crafting materials create harder decisions; separate per-upgrade materials remove decisions.
- [6:45](https://youtu.be/Zrf1cou_yVo?t=405) **[[core-loops-and-game-design]]** Positive power-creep loops are addictive but become grind; add a negative feedback loop or puzzle depth to avoid tedium.
- [8:16](https://youtu.be/Zrf1cou_yVo?t=496) **[[genre-mechanics]]** Turn power growth into a puzzle of optimisation (Factorio, Satisfactory style) so progression rewards planning rather than repetition.
- [8:58](https://youtu.be/Zrf1cou_yVo?t=538) **[[core-loops-and-game-design]]** Scale conversion cost with level (Elden Ring rune curve) so farming trivial enemies is ineffective and players explore harder areas.
- [9:49](https://youtu.be/Zrf1cou_yVo?t=589) **[[core-loops-and-game-design]]** Add drains (breakage, upkeep, spoilage, ammo use) to slow power growth and force players to re-engage with the economy.
- [10:34](https://youtu.be/Zrf1cou_yVo?t=634) **[[player-psychology-and-game-feel]]** Use drains to add risk: losing carried currency on death (Elden Ring) makes exploring new areas feel dangerous as holdings grow.
- [12:09](https://youtu.be/Zrf1cou_yVo?t=729) **[[core-loops-and-game-design]]** Add trader NPCs with their own stock and prices by location so players profit from arbitrage, creating trade-route puzzles.
- [12:53](https://youtu.be/Zrf1cou_yVo?t=773) **[[core-loops-and-game-design]]** Model supply and demand (Moonlighter: flooding a market drops price) so repeated sales cannot be farmed infinitely.
- [13:37](https://youtu.be/Zrf1cou_yVo?t=817) **[[core-loops-and-game-design]]** Add price volatility with risk and reward (Animal Crossing turnips) to fix exploits and add decisions about how much to risk.
- [0:01](https://youtu.be/Zrf1cou_yVo?t=1) **[[common-mistakes]]** Test for infinite-resource exploits before launch; a repeatable tap (e.g. respawning cows) can let players farm unlimited wealth early.
- [7:30](https://youtu.be/Zrf1cou_yVo?t=450) **[[common-mistakes]]** Patching an exploit with a punishing spawn can create a new exploit; CD Projekt Red's fix (level 27 monster spawn) was itself farmed for heads, requiring a second patch.
- [15:07](https://youtu.be/Zrf1cou_yVo?t=907) **[[playtesting-and-feedback]]** Watch higher-level players for exploit discovery after patches; they find economy breaks that early testers miss.

## Numbers
- [0:01](https://youtu.be/Zrf1cou_yVo?t=1) Witcher 3 cow exploit: **Infinite wealth** (Killing cows then meditating respawns them, enabling infinite leather sales)
- [7:30](https://youtu.be/Zrf1cou_yVo?t=450) Witcher 3 fix trigger: **6 cows** (BDFI spawns level 27 monster after killing six cows)
- [9:49](https://youtu.be/Zrf1cou_yVo?t=589) Elden Ring rune scaling: **~10 vs hundreds of kills** (Level 9 to 10 needs about 10 guards; level 49 to 50 needs hundreds)
- [5:13](https://youtu.be/Zrf1cou_yVo?t=313) Ghost of Tsushima crafting materials: **13** (Roughly 13 different crafting materials, mostly tied to one upgrade each)
- [5:13](https://youtu.be/Zrf1cou_yVo?t=313) Metro Exodus crafting materials: **2** (Only two materials, nearly every craft needs both)
- [13:37](https://youtu.be/Zrf1cou_yVo?t=817) Animal Crossing turnip market: **1 week cycle** (Turnips bought Sunday, price changes daily that week, drain after week)

## Games
- **The Witcher 3** [0:01](https://youtu.be/Zrf1cou_yVo?t=1): Cow-farming exploit showed infinite-resource risk; merchants with separate prices by location create arbitrage.
- **Factorio** [7:30](https://youtu.be/Zrf1cou_yVo?t=450): Power-growth loop turned into an optimisation puzzle rather than simple repetition.
- **Satisfactory** [8:16](https://youtu.be/Zrf1cou_yVo?t=496): Efficiency and automation challenges keep players engaged with the economy.
- **Stardew Valley** [8:16](https://youtu.be/Zrf1cou_yVo?t=496): Optimisation challenges and deadlines make progression feel like problem-solving.
- **Elden Ring** [8:58](https://youtu.be/Zrf1cou_yVo?t=538): Rune cost scaling with level discourages grinding weak enemies and pushes exploration.
- **Death Stranding** [11:17](https://youtu.be/Zrf1cou_yVo?t=677): Carrying more boxes raises the risk of losing them, balancing reward against danger.
- **Moonlighter** [12:53](https://youtu.be/Zrf1cou_yVo?t=773): Flooding a market lowers item prices, preventing infinite repeated sales.
- **Animal Crossing** [13:37](https://youtu.be/Zrf1cou_yVo?t=817): Daily fluctuating turnip prices add risk and a mini stock-market decision.
- **Ghost of Tsushima** [4:29](https://youtu.be/Zrf1cou_yVo?t=269): Dedicated crafting materials per upgrade remove decisions about resource allocation.
- **Metro Exodus** [5:13](https://youtu.be/Zrf1cou_yVo?t=313): Shared crafting materials force intentional crafting choices.

## He points to
- XCOM video by Game Maker's Toolkit (losing units)

## Quotes
- [5:53](https://youtu.be/Zrf1cou_yVo?t=353) "If you want to create difficult decisions for the player, have fewer currencies that can be spent on lots of different things."
- [13:37](https://youtu.be/Zrf1cou_yVo?t=817) "By adding a sense of risk and reward, we not only go some way towards fixing the exploit, but we add extra decision making."

## Topics
[[common-mistakes]] [[core-loops-and-game-design]] [[genre-mechanics]] [[player-psychology-and-game-feel]] [[playtesting-and-feedback]]

Back to [[leads - How to make successful Roblox games]]
