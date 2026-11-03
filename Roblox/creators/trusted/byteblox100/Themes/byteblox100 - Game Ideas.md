---
title: byteblox100 - Game Ideas
creator: byteblox100
tags: [roblox, byteblox100, theme]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# byteblox100: Game Ideas

All byteblox100 tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[game-ideas-and-genres]]
- 2024-06-24 [0:46](https://youtu.be/ekM2z9FMhZc?t=46) Incremental/tycoon games with a simple buy-button loop are very quick to build; the core mechanic can be done with basic UI and a few scripts. ([[2024-06-24 - How to Make a Game Addictive in 15 Minutes|How to Make a Game Addictive in 15 Minutes]])

## [[core-loops-and-game-design]]
- 2024-05-11 [5:07](https://youtu.be/UUgj-hmX2LM?t=307) Define rarity as weights summing to 100 (e.g. legendary 1, epic 19, rare 30, common 50) so the odds are easy to read and tune. ([[2024-05-11 - Programming Rarity is Harder Than You Think|Programming Rarity is Harder Than You Think]])
- 2024-05-11 [9:13](https://youtu.be/UUgj-hmX2LM?t=553) Removing the spawn delay produced several legendaries quickly in testing; a spawn-rate change visibly alters how often rare items appear. ([[2024-05-11 - Programming Rarity is Harder Than You Think|Programming Rarity is Harder Than You Think]])
- 2024-06-10 [0:41](https://youtu.be/_rksdF5JoHo?t=41) Make death meaningful: harsh-but-fair death makes the risk-taking before it interesting, as in Minecraft. Trivial respawns remove the tension that gives earlier play its stakes. ([[2024-06-10 - Why Do Most Games Make Death Boring|Why Do Most Games Make Death Boring?]])
- 2024-06-10 [11:16](https://youtu.be/_rksdF5JoHo?t=676) Give dead players something to do: ghost states that unlock abilities or new interactions keep them playing 24/7 instead of waiting for respawn. Roblox games should always have an activity available. ([[2024-06-10 - Why Do Most Games Make Death Boring|Why Do Most Games Make Death Boring?]])
- 2024-06-10 [19:31](https://youtu.be/_rksdF5JoHo?t=1171) Consider a death-loop structure: death resets the world but keeps the player's knowledge, so later runs go further. Outer Wilds and Undertale show this, and Doors teaches cues through death. ([[2024-06-10 - Why Do Most Games Make Death Boring|Why Do Most Games Make Death Boring?]])
- 2024-06-10 [22:54](https://youtu.be/_rksdF5JoHo?t=1374) Store player knowledge in a persistent ship-log-style UI so information gained across loops stays visible and players can solve clues without re-reading everything. ([[2024-06-10 - Why Do Most Games Make Death Boring|Why Do Most Games Make Death Boring?]])
- 2024-06-24 [4:19](https://youtu.be/ekM2z9FMhZc?t=259) Store per-item data (cost, cash per second, owned amount) as Attributes on a template frame and clone it, so each item shares structure but has different values. ([[2024-06-24 - How to Make a Game Addictive in 15 Minutes|How to Make a Game Addictive in 15 Minutes]])
- 2024-06-24 [11:53](https://youtu.be/ekM2z9FMhZc?t=713) Run a task.wait(1) loop that iterates owned items and adds amount x cash-per-second to the player's total each tick to create passive income. ([[2024-06-24 - How to Make a Game Addictive in 15 Minutes|How to Make a Game Addictive in 15 Minutes]])
- 2024-09-24 [5:16](https://youtu.be/Issrodr_wK8?t=316) Add small juice to even a trivial game (bounce, color change, progress, aura); the speaker says it takes about 20-30 minutes for a beginner. ([[2024-09-24 - Every Game is Soulless; And There's a Really Easy Fix|Every Game is Soulless; And There's a Really Easy ]])
- 2024-09-29 [16:48](https://youtu.be/Nzrtg8SGOY0?t=1008) Only add a progress bar (durability, hunger, oxygen) if it ties into other systems and creates meaningful decisions; a bar that only punishes with no reward is just annoying. ([[2024-09-29 - 7 Things I'll Never Add as a Roblox Developer|7 Things I'll Never Add as a Roblox Developer]])
- 2024-09-29 [21:43](https://youtu.be/Nzrtg8SGOY0?t=1303) Don't fake progression with exponentially growing numbers (x2/x3 costs) when you have little content; use flat difficulty increases and add new content for each stage. ([[2024-09-29 - 7 Things I'll Never Add as a Roblox Developer|7 Things I'll Never Add as a Roblox Developer]])
- 2024-09-29 [30:08](https://youtu.be/Nzrtg8SGOY0?t=1808) Replace currency-locked walls with natural gates such as vehicle or equipment limits (Subnautica crush depth, jetpack fuel) so the world feels open and unrestricted. ([[2024-09-29 - 7 Things I'll Never Add as a Roblox Developer|7 Things I'll Never Add as a Roblox Developer]])
- 2024-09-29 [38:35](https://youtu.be/Nzrtg8SGOY0?t=2315) Avoid soft-locks from nonrenewable items; provide an in-game way to restart or access all content (Grounded-style restart keeping progress) instead of requiring a new save. ([[2024-09-29 - 7 Things I'll Never Add as a Roblox Developer|7 Things I'll Never Add as a Roblox Developer]])
- 2024-09-29 [41:43](https://youtu.be/Nzrtg8SGOY0?t=2503) Give every upgradeable feature real upgrade tiers and playtest them at the relevant progression level so players don't hit a capped, tedious baseline. ([[2024-09-29 - 7 Things I'll Never Add as a Roblox Developer|7 Things I'll Never Add as a Roblox Developer]])
- 2024-09-29 [47:10](https://youtu.be/Nzrtg8SGOY0?t=2830) In tycoons, don't attach cash rewards to manual minigames like obbies; it forces players to stay engaged when the point is automation. ([[2024-09-29 - 7 Things I'll Never Add as a Roblox Developer|7 Things I'll Never Add as a Roblox Developer]])
- 2025-02-01 [4:06](https://youtu.be/o-8V99horro?t=246) Roll rarity from the rarest tier down: check legendary first, then epic, rare, common, using one random number from 1 to chance. Checking common first breaks the odds. ([[2025-02-01 - Why Roblox Simulators Punish Players Who Spend Money|Why Roblox Simulators Punish Players Who Spend Mon]])
- 2025-03-15 [21:14](https://youtu.be/3rxZj5-Qx30?t=1274) Look into lag compensation / rollback techniques if building precise combat, since the server must validate hits against where the target was in the past. ([[2025-03-15 - Roblox Has Very Bad Hitboxes & It's Not Their Fault|Roblox Has Very Bad Hitboxes & It's Not Their Faul]])

## [[genre-mechanics]]
- 2024-11-17 [25:31](https://youtu.be/1KKQ6YrktTk?t=1531) In combat games, mouse/keyboard players beat mobile players at equal skill; consider mobile-only lobbies, as Blade Ball reportedly does. ([[2024-11-17 - Roblox Mobile Developers Are Insanely Lazy|Roblox Mobile Developers Are Insanely Lazy]])

Up: [[byteblox100 - How to make successful Roblox games]]
