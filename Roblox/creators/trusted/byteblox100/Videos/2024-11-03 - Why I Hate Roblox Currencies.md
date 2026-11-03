---
title: "Why I Hate Roblox Currencies"
url: https://youtu.be/4yIjd9Xn9sE
creator: ByteBlox
official: false
advice_density: medium
date: 2024-11-03
views: 20734
transcript: auto-captions
confidence: medium
tags: [roblox, byteblox100, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Why I Hate Roblox Currencies

[Watch](https://youtu.be/4yIjd9Xn9sE) | byteblox100 | 20,734 views | 2024-11-03

## Summary
Scripted tutorial building a Roblox cash system: leaderstats currency, click-to-give/take parts, cash dropped on death, walk speed slowed by cash, inflation loop, and color shift toward green as cash approaches 1,000. Mostly entertainment with a design-idea pitch against boring currencies.

## Tips
- [2:22](https://youtu.be/4yIjd9Xn9sE?t=142) **[[client-server-and-remotes]]** Create an IntValue named cash under the player, then parent it to a Folder named leaderstats so it appears on the default leaderboard.
- [4:02](https://youtu.be/4yIjd9Xn9sE?t=242) **[[scripting-and-performance]]** Guard currency deductions with a check (if cash < 1 then return) to prevent negative balances.
- [8:31](https://youtu.be/4yIjd9Xn9sE?t=511) **[[combat-and-gameplay-systems]]** Use CharacterAdded to rebuild per-character effects on respawn, since the character is reset while the Player object persists.
- [11:58](https://youtu.be/4yIjd9Xn9sE?t=718) **[[scripting-and-performance]]** Use task.spawn for each dropped item so all drops appear at once and despawn together, instead of a loop that waits per item.
- [14:30](https://youtu.be/4yIjd9Xn9sE?t=870) **[[player-psychology-and-game-feel]]** Tie a currency to a gameplay effect such as walk speed so holding money has a cost and encourages spending.
- [16:29](https://youtu.be/4yIjd9Xn9sE?t=989) **[[player-psychology-and-game-feel]]** Add a periodic percentage-based deduction (e.g. 10% per second) as inflation to keep money flowing; note Roblox rounds integers, so small balances may not decrease.
- [18:51](https://youtu.be/4yIjd9Xn9sE?t=1131) **[[ui-ux-design]]** Give visual feedback on currency progress, e.g. lerp character color from gray to green as balance approaches a target (clamp percentage to 1).

## Numbers
- [17:10](https://youtu.be/4yIjd9Xn9sE?t=1030) Rounding behaviour: **Roblox rounds integers: 10% deduction does nothing for cash values below about 5** (Percentage deduction on IntValue fails at low balances)
- [19:32](https://youtu.be/4yIjd9Xn9sE?t=1172) Color threshold: **Character color scales from gray (127,127,127) to green at 1,000 cash** (Clamped percentage = cash / 1000)
- [15:54](https://youtu.be/4yIjd9Xn9sE?t=954) Walk speed penalty: **Speed = 16 - 0.1 * cash; reaches zero at 160 cash** (Example implementation from video)

## Games
- **Doris** [22:53](https://youtu.be/4yIjd9Xn9sE?t=1373): Mentioned as an example of a game that innovated beyond standard currency systems and grew nearly overnight.

## Tools
Roblox Studio, Luau, Toolbox

## Quotes
- [22:53](https://youtu.be/4yIjd9Xn9sE?t=1373) "Standard cash systems are boring and not innovative; innovate your game and you'll get all of the rewards for it."
- [14:30](https://youtu.be/4yIjd9Xn9sE?t=870) "A good economy always has money flowing; no one got rich from just saving their money."

## Topics
[[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[player-psychology-and-game-feel]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[byteblox100 - How to make successful Roblox games]]
