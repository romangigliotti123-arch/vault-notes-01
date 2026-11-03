---
title: "Docs: luau / numbers"
url: https://create.roblox.com/docs/luau/numbers.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: luau / numbers

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/luau/numbers.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Luau docs page on the number type: double-precision range and precision, signed zero, float/int/int64 classifications, literal notations (decimal, scientific, hex, binary, underscores), type introspection, and rounding functions math.floor/ceil/modf.

## Tips
- [page](https://create.roblox.com/docs/luau/numbers) **[[luau-language-and-types]]** Use int64 types for Roblox IDs such as Player.UserId; MarketplaceService:PromptPurchase() and TeleportService:Teleport() expect int64 arguments.
- [page](https://create.roblox.com/docs/luau/numbers) **[[luau-language-and-types]]** Check whether a number is an integer with math.floor(x) == x.
- [page](https://create.roblox.com/docs/luau/numbers) **[[luau-language-and-types]]** Integer-expecting properties and functions may silently round or raise errors on non-integer input; pass whole numbers explicitly.
- [page](https://create.roblox.com/docs/luau/numbers) **[[luau-language-and-types]]** Use math.modf() to round toward zero; it also returns the fractional part as a second result.

## Numbers
- [page](https://create.roblox.com/docs/luau/numbers) Number precision: **64-bit double, about 15 digits, range ±1.7e308** (Luau number type is double-precision floating point)
- [page](https://create.roblox.com/docs/luau/numbers) int range: **-2^31 to 2^31 - 1** (32-bit integer type named int)
- [page](https://create.roblox.com/docs/luau/numbers) int64 range: **-2^63 to 2^63 - 1** (Signed 64-bit integer, used for Roblox website IDs)
- [page](https://create.roblox.com/docs/luau/numbers) float precision: **32-bit single precision** (Float type is less precise but uses less memory)

## Tools
Luau

## Topics
[[luau-language-and-types]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
