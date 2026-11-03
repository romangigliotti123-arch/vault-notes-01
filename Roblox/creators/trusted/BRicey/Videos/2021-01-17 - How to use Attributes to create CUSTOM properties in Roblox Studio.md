---
title: "How to use Attributes to create CUSTOM properties in Roblox Studio"
url: https://youtu.be/7BSYIEdo6E4
creator: B Ricey
official: false
advice_density: medium
date: 2021-01-17
views: 12845
transcript: auto-captions
confidence: high
tags: [roblox, bricey, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to use Attributes to create CUSTOM properties in Roblox Studio

[Watch](https://youtu.be/7BSYIEdo6E4) | BRicey | 12,845 views | 2021-01-17

## Summary
Tutorial on Roblox Studio Attributes (beta at the time): adding custom typed properties to instances via the Properties window, getting/setting them in Luau, detecting changes with GetAttributeChangedSignal, using script attributes as exposed config, and storing table data by JSON-encoding into a string attribute.

## Tips
- [1:14](https://youtu.be/7BSYIEdo6E4?t=74) **[[development-process-and-speed]]** Attributes were in beta in Jan 2021; enable them under File > Beta Features before use.
- [4:04](https://youtu.be/7BSYIEdo6E4?t=244) **[[scripting-and-performance]]** Access attributes with instance:GetAttribute(name) and SetAttribute(name, value), not instance.name; attributes are not properties.
- [6:10](https://youtu.be/7BSYIEdo6E4?t=370) **[[scripting-and-performance]]** Store attribute name strings in constants at the top of scripts; a typo silently creates a new attribute instead of erroring.
- [7:32](https://youtu.be/7BSYIEdo6E4?t=452) **[[scripting-and-performance]]** Setting an attribute to nil deletes it.
- [7:32](https://youtu.be/7BSYIEdo6E4?t=452) **[[scripting-and-performance]]** Use GetAttributeChangedSignal(name) to react to attribute changes, replacing clutter like extra NumberValues.
- [10:21](https://youtu.be/7BSYIEdo6E4?t=621) **[[core-loops-and-game-design]]** Use script attributes as designer-facing config (e.g. debug flag, wait times) so non-coders can tune values in the Properties window.
- [13:03](https://youtu.be/7BSYIEdo6E4?t=783) **[[data-persistence]]** Attributes cannot store tables; JSON-encode with HttpService:JSONEncode into a string attribute and decode with JSONDecode on read.
- [13:45](https://youtu.be/7BSYIEdo6E4?t=825) **[[scripting-and-performance]]** Keep JSON-encoded table data to numbers, strings, booleans and nested tables only; functions cannot be encoded.
- [15:47](https://youtu.be/7BSYIEdo6E4?t=947) **[[development-process-and-speed]]** Run one-off setup such as JSON-encoding table attributes from the command bar so values are baked in before runtime.
- [16:28](https://youtu.be/7BSYIEdo6E4?t=988) **[[scripting-and-performance]]** Prefer a few JSON-encoded attributes over hundreds of individual attributes for bulk data.

## Numbers
- [4:47](https://youtu.be/7BSYIEdo6E4?t=287) Attribute name length limit: **100 characters, no spaces** (Stated limit on attribute names in the video)
- [11:44](https://youtu.be/7BSYIEdo6E4?t=704) Debug wait time example: **1 second vs normal 5 seconds** (Script attribute example for fast iteration)

## Tools
Roblox Studio Attributes, HttpService JSONEncode/JSONDecode, Command Bar

## Topics
[[core-loops-and-game-design]] [[data-persistence]] [[development-process-and-speed]] [[scripting-and-performance]]

Back to [[BRicey - How to make successful Roblox games]]
