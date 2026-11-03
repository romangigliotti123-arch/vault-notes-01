---
title: BRicey - Monetisation
creator: BRicey
tags: [roblox, bricey, theme]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# BRicey: Monetisation

All BRicey tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[monetisation-gamepasses]]
- 2022-04-16 [1:34](https://youtu.be/TmiU5CY6BW0?t=94) Gamepasses apply globally across the game, so they suit permanent boosts like a money multiplier rather than consumable items. ([[2022-04-16 - How to make a Tycoon in Roblox 11 - Gamepasses|How to make a Tycoon in Roblox #11 - Gamepasses]])
- 2022-04-16 [2:14](https://youtu.be/TmiU5CY6BW0?t=134) Copy the gamepass ID from the URL (roblox.com/game-pass/ID/...). It is needed to prompt purchases in-game. ([[2022-04-16 - How to make a Tycoon in Roblox 11 - Gamepasses|How to make a Tycoon in Roblox #11 - Gamepasses]])

## [[monetisation-devproducts]]
- 2022-04-30 [0:35](https://youtu.be/5bI6l6SHBDU?t=35) Create developer products in Game Settings > Monetization > Developer Products; unlike game passes they can be bought repeatedly, so use them for consumables like currency. ([[2022-04-30 - How to make a Tycoon in Roblox Studio 12 - Dev Products|How to make a Tycoon in Roblox Studio #12 - Dev Pr]])
- 2022-04-30 [5:45](https://youtu.be/5bI6l6SHBDU?t=345) Grant the item by calling your existing player-manager setter rather than editing leaderstats directly, so all currency changes go through one function. ([[2022-04-30 - How to make a Tycoon in Roblox Studio 12 - Dev Products|How to make a Tycoon in Roblox Studio #12 - Dev Pr]])
- 2022-04-30 [8:29](https://youtu.be/5bI6l6SHBDU?t=509) In ProcessReceipt, return NotProcessedYet if the player is not in the server; Roblox will retry later, preventing players from paying without receiving the item. ([[2022-04-30 - How to make a Tycoon in Roblox Studio 12 - Dev Products|How to make a Tycoon in Roblox Studio #12 - Dev Pr]])
- 2022-04-30 [9:51](https://youtu.be/5bI6l6SHBDU?t=591) Wrap the product grant function in pcall; if it errors, return NotProcessedYet so the purchase is not charged without being granted. ([[2022-04-30 - How to make a Tycoon in Roblox Studio 12 - Dev Products|How to make a Tycoon in Roblox Studio #12 - Dev Pr]])
- 2022-04-30 [10:32](https://youtu.be/5bI6l6SHBDU?t=632) Only return PurchaseGranted after the grant succeeds; this is what tells Roblox the purchase completed. ([[2022-04-30 - How to make a Tycoon in Roblox Studio 12 - Dev Products|How to make a Tycoon in Roblox Studio #12 - Dev Pr]])

## [[monetisation-other]]
- 2022-05-28 [2:26](https://youtu.be/T0xqkYODIl0?t=146) Create badges at zero Robux price; the speaker says badge creation should always be zero cost, with possible charges only above very high creation rates. ([[2022-05-28 - How to use Badges in Roblox! (Plus some scripting tips)|How to use Badges in Roblox! (Plus some scripting ]])

Up: [[BRicey - How to make successful Roblox games]]
