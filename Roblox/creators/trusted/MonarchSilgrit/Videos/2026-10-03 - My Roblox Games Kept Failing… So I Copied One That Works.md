---
title: "My Roblox Games Kept Failing… So I Copied One That Works"
url: https://youtu.be/bbCmt98O9MA
creator: MonarchDev
official: false
advice_density: medium
date: 2026-10-03
views: 26287
transcript: auto-captions
confidence: medium
tags: [roblox, monarchsilgrit, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# My Roblox Games Kept Failing… So I Copied One That Works

[Watch](https://youtu.be/bbCmt98O9MA) | MonarchSilgrit | 26,287 views | 2026-10-03

## Summary
Creator copies the core loop of the grow game Greedy Growers for a 7-day experiment: map, pets, pads, animations, menus, monetization, open beta, bug fixes, then Robux-funded ads. After one week: 1,775 visits, 5,125 Robux from sales, about 385 Robux from creator awards, 180 players toward the 250-player gate.

## Tips
- [2:14](https://youtu.be/bbCmt98O9MA?t=134) **[[building-art-and-assets]]** Settle on one art style early. Mismatched assets forced a full rebuild to blocky style, and a bad sky tint turned the whole map blue.
- [3:12](https://youtu.be/bbCmt98O9MA?t=192) **[[anti-exploit-and-security]]** Protect growing pets and cash from raids. Add a one-button stop so players feel safe in their base.
- [5:12](https://youtu.be/bbCmt98O9MA?t=312) **[[ui-ux-design]]** Replace placeholder emojis with real art early so menus match the game style instead of being rebuilt later.
- [5:53](https://youtu.be/bbCmt98O9MA?t=353) **[[pricing]]** Simulate progression math before launch. A free egg was hit 130 times (about $6,500 in 30 seconds), so every rebirth price was rebuilt.
- [6:34](https://youtu.be/bbCmt98O9MA?t=394) **[[monetisation-gamepasses]]** Test gamepass effects before shipping. A supporter crown meant to spin at 35 degrees per second spun at about 275.
- [6:34](https://youtu.be/bbCmt98O9MA?t=394) **[[monetisation-gamepasses]]** Show paid prize wheel odds before spinning to stay compliant with Roblox rules.
- [7:15](https://youtu.be/bbCmt98O9MA?t=435) **[[playtesting-and-feedback]]** Run a public beta with a Discord community to find bugs. Testers unlocked everything in about 5 minutes, exposing weak progression pacing.
- [7:15](https://youtu.be/bbCmt98O9MA?t=435) **[[data-persistence]]** If a save fails to load, retry, then kick the player with a 'progress is safe' message. Never create a fresh save that overwrites real data.
- [7:56](https://youtu.be/bbCmt98O9MA?t=476) **[[anti-exploit-and-security]]** Check anti-cheat false positives. Teleport buttons triggered the speed/spawn detector after three uses in a minute.
- [7:56](https://youtu.be/bbCmt98O9MA?t=476) **[[testing-debugging-and-qa]]** Test with non-dev accounts. Dev accounts are exempt from anti-cheat, which hid the teleport false positive.
- [8:39](https://youtu.be/bbCmt98O9MA?t=519) **[[testing-debugging-and-qa]]** Keep a folder of reported bugs and fix them in a dedicated pass. Examples: spawn facing away from the free egg, selling during respawn duplicating pets.
- [9:19](https://youtu.be/bbCmt98O9MA?t=559) **[[first-session-onboarding]]** Make sure the first free egg is visible on spawn. Eight players quit at tutorial step one because they spawned facing away from it.
- [10:36](https://youtu.be/bbCmt98O9MA?t=636) **[[ads-and-sponsored-experiences]]** Set explicit win criteria before ads go live: beat the Robux spend, get players returning, and pay back ad spend.
- [10:36](https://youtu.be/bbCmt98O9MA?t=636) **[[ads-and-sponsored-experiences]]** Ad credits can be bought with Robux, about 1,000 Robux for roughly $3.80 in ad credits. Small budgets buy few players.
- [11:17](https://youtu.be/bbCmt98O9MA?t=677) **[[retention-d1-d7]]** Track day-1 return rate. Creator's prior game had 1 in 400 players return the next day; top games reportedly get about 1 in 10.
- [12:51](https://youtu.be/bbCmt98O9MA?t=771) **[[discovery-algorithm]]** Reach the roughly 250 highly engaged players Roblox needs before the game is shown broadly to everyone.
- [12:10](https://youtu.be/bbCmt98O9MA?t=730) **[[business-and-payouts]]** Track creator awards alongside sales; they pay for returning players and grew to about 385 Robux in a week.
- [1:21](https://youtu.be/bbCmt98O9MA?t=81) **[[development-process-and-speed]]** Split the build into ordered objectives (map, pets, animations, menus, monetization, beta, ads) to avoid a low-effort game.
- [4:09](https://youtu.be/bbCmt98O9MA?t=249) **[[3d-modeling-rigging-and-animation]]** Give every pet at least a basic animation. Triage with simple rules like legs-or-wings to cut complicated rigs fast.
- [0:00](https://youtu.be/bbCmt98O9MA?t=0) **[[game-ideas-and-genres]]** Copy a proven loop from a working game (Greedy Growers) and add a twist, such as lightning that can turn pets into steak.
- [2:32](https://youtu.be/bbCmt98O9MA?t=152) **[[core-loops-and-game-design]]** Give the core loop a clear risk decision: cash out now or wait for a bigger payout.
- [4:50](https://youtu.be/bbCmt98O9MA?t=290) **[[combat-and-gameplay-systems]]** Use the steak as a feed mechanic so failed pets are not wasted, a loop that rewards failure.

## Numbers
- [0:00](https://youtu.be/bbCmt98O9MA?t=0) Prior three games total revenue: **$2**
- [1:32](https://youtu.be/bbCmt98O9MA?t=92) Free egg hits before balancing: **130 (about $6,500 in 30 seconds)**
- [5:53](https://youtu.be/bbCmt98O9MA?t=353) Simulated time to finish all 10 rebirths: **about 46 minutes**
- [3:24](https://youtu.be/bbCmt98O9MA?t=204) Pet eggs and rarity tiers: **28 eggs, 12 rarity levels**
- [4:50](https://youtu.be/bbCmt98O9MA?t=290) Animals cut from pack: **16 of 32 removed**
- [6:34](https://youtu.be/bbCmt98O9MA?t=394) Supporter pass price: **about 99 Robux**
- [10:36](https://youtu.be/bbCmt98O9MA?t=636) Ad credit rate: **1,000 Robux = about $3.80 in ad credits**
- [10:36](https://youtu.be/bbCmt98O9MA?t=636) Prior campaign: **$130 of ads gave 8,800 players, almost none returned**
- [11:17](https://youtu.be/bbCmt98O9MA?t=677) Prior game next-day return: **1 in 400 players**
- [11:17](https://youtu.be/bbCmt98O9MA?t=677) Top Roblox game next-day return (reported): **about 1 in 10, top 1% just over 1 in 5**
- [12:10](https://youtu.be/bbCmt98O9MA?t=730) Visits after one week: **1,775**
- [12:10](https://youtu.be/bbCmt98O9MA?t=730) Robux from sales after one week: **5,125**
- [12:10](https://youtu.be/bbCmt98O9MA?t=730) Creator awards Robux: **about 385**
- [12:51](https://youtu.be/bbCmt98O9MA?t=771) Players needed before broad recommendation: **250 highly engaged (currently 180)**

## Games
- **Greedy Growers** [0:41](https://youtu.be/bbCmt98O9MA?t=41): Proven loop copied: pets grow on a pad and gain value, with a cash-out-or-wait risk decision.
- **Grow Garden** [0:00](https://youtu.be/bbCmt98O9MA?t=0): Referenced as the genre example for the grow-style game concept.
- **Pet Simulator** [5:53](https://youtu.be/bbCmt98O9MA?t=353): Buddies that follow players and give bonuses are a familiar simulator pattern.

## Tools
Roblox Studio, Claude (AI for placeholder UI), Discord

## He points to
- Ice (collaborator, shared Discord server)

## Quotes
- [0:41](https://youtu.be/bbCmt98O9MA?t=41) "We did not want to make another low-effort slob game. God knows the platform already has millions of those."
- [9:19](https://youtu.be/bbCmt98O9MA?t=559) "Eight players quit in the first step of the tutorial because they spawned facing away from their free egg."

## Topics
[[3d-modeling-rigging-and-animation]] [[ads-and-sponsored-experiences]] [[anti-exploit-and-security]] [[building-art-and-assets]] [[business-and-payouts]] [[combat-and-gameplay-systems]] [[core-loops-and-game-design]] [[data-persistence]] [[development-process-and-speed]] [[discovery-algorithm]] [[first-session-onboarding]] [[game-ideas-and-genres]] [[monetisation-gamepasses]] [[playtesting-and-feedback]] [[pricing]] [[retention-d1-d7]] [[testing-debugging-and-qa]] [[ui-ux-design]]

Back to [[MonarchSilgrit - How to make successful Roblox games]]
