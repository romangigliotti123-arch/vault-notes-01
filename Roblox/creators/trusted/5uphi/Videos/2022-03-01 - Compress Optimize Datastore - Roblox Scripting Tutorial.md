---
title: "Compress / Optimize Datastore  - Roblox Scripting Tutorial"
url: https://youtu.be/ws3-gfJXw_U
creator: Suphi Kaner
official: false
advice_density: high
date: 2022-03-01
views: 24120
transcript: auto-captions
confidence: high
tags: [roblox, 5uphi, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.8
---

> [!note] Trust: TRUSTED (credibility audit score 8.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Compress / Optimize Datastore  - Roblox Scripting Tutorial

[Watch](https://youtu.be/ws3-gfJXw_U) | 5uphi | 24,120 views | 2022-03-01

## Summary
Tutorial on compressing DataStore data to fit more into one key (4M character limit). Measures JSON size with JSONEncode, rounds floats to integers, drops brackets, encodes values in base 90 via a ModuleScript, and joins with table.concat. Raises capacity from about 70k parts to about 297k parts.

## Tips
- [1:36](https://youtu.be/ws3-gfJXw_U?t=96) **[[data-persistence]]** Measure save size with HttpService:JSONEncode and string length against the 4,000,000-character per-key limit before optimizing.
- [8:29](https://youtu.be/ws3-gfJXw_U?t=509) **[[data-persistence]]** Store positions as integers by multiplying by 1000 and rounding instead of storing 3 decimals; removes float noise and raised capacity from 133k to 176k parts.
- [12:38](https://youtu.be/ws3-gfJXw_U?t=758) **[[data-persistence]]** Flatten x,y,z into one array instead of nested tables; removing brackets raised capacity to about 193k parts.
- [15:18](https://youtu.be/ws3-gfJXw_U?t=918) **[[data-persistence]]** Encode numbers in a higher base (e.g. base 90 with a custom character set) to shorten each value; base 90 gives 4 chars for ~65 million values.
- [21:33](https://youtu.be/ws3-gfJXw_U?t=1293) **[[data-persistence]]** Exclude the double-quote character from encoding alphabets because JSONEncode escapes it with a backslash, costing two characters.
- [37:30](https://youtu.be/ws3-gfJXw_U?t=2250) **[[data-persistence]]** Join encoded values with table.concat using commas instead of passing a table of strings to JSONEncode, which adds quote characters; this raised capacity to about 297k parts.
- [36:06](https://youtu.be/ws3-gfJXw_U?t=2166) **[[data-persistence]]** Only encode whole numbers in the custom base encoder; fractional values are not supported.

## Numbers
- [0:00](https://youtu.be/ws3-gfJXw_U?t=0) DataStore key character limit: **4,000,000 characters**
- [4:41](https://youtu.be/ws3-gfJXw_U?t=281) Parts storable, naive JSON of x/y/z tables: **~70,000**
- [8:29](https://youtu.be/ws3-gfJXw_U?t=509) Parts storable after integer rounding: **~176,000**
- [13:20](https://youtu.be/ws3-gfJXw_U?t=800) Parts storable after removing brackets: **~193,000**
- [37:30](https://youtu.be/ws3-gfJXw_U?t=2250) Parts storable after base-90 encoding and removing quotes: **~297,000**
- [18:47](https://youtu.be/ws3-gfJXw_U?t=1127) Value range: base 10 vs base 16, 3 characters: **1,000 vs 4,096**
- [19:28](https://youtu.be/ws3-gfJXw_U?t=1168) Base 90 value range, 4 characters: **65,610,000**

## Tools
HttpService:JSONEncode, table.concat, ModuleScript

## He points to
- ipairs vs pairs video by the same creator
- modulus operator video by the same creator

## Topics
[[data-persistence]]

Back to [[5uphi - How to make successful Roblox games]]
