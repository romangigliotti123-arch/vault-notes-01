---
title: "Docs: cloud / reference / types"
url: https://create.roblox.com/docs/cloud/reference/types.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / reference / types

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/cloud/reference/types.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Open Cloud API reference on JSON type encodings: timestamps (RFC 3339), durations, bytes (base64), FieldMask for updateMask, and Money/Decimal formats including Creator Store's required exponent of -9.

## Tips
- [page](https://create.roblox.com/docs/cloud/reference/types) **[[ugc-and-avatar-economy]]** Creator Store products require Money quantity exponent of -9 (e.g. $17.99 = significand 17990000000, exponent -9), not the standard -2.
- [page](https://create.roblox.com/docs/cloud/reference/types) **[[client-server-and-remotes]]** Open Cloud update methods accept an updateMask parameter; list only the fields to change, comma-separated (e.g. 'foo.b, bar'), so other fields are untouched.
- [page](https://create.roblox.com/docs/cloud/reference/types) **[[scripting-and-performance]]** Duration values must be strings ending in 's' with at most nanosecond precision, within ±315,576,000,000 seconds.

## Numbers
- [page](https://create.roblox.com/docs/cloud/reference/types) Creator Store Money exponent: **-9 required** (Creator Store products require exponent -9 in Money quantity)
- [page](https://create.roblox.com/docs/cloud/reference/types) Duration range: **-315,576,000,000 to 315,576,000,000 seconds** (Inclusive range for Open Cloud Duration type)
- [page](https://create.roblox.com/docs/cloud/reference/types) Duration fractional digits: **0, 3, 6, or 9 in output** (Generated output fractional digits; nanosecond precision max)
- [page](https://create.roblox.com/docs/cloud/reference/types) Timestamp fractional digits: **0, 3, 6, or 9** (RFC 3339 generated output, Z-normalized)

## Tools
Roblox Open Cloud API

## Topics
[[client-server-and-remotes]] [[scripting-and-performance]] [[ugc-and-avatar-economy]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
