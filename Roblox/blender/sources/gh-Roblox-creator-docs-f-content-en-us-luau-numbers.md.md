---
type: research-source
id: gh-Roblox-creator-docs-f-content-en-us-luau-numbers.md
title: "Roblox/creator-docs/content/en-us/luau/numbers.md"
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/creator-docs/blob/HEAD/content/en-us/luau/numbers.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0166
relevance: 0
density: low
tags: ["research-source", "github", "other"]
---
# gh-Roblox-creator-docs-f-content-en-us-luau-numbers.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Luau number type reference: doubles, int/float/int64 classifications, literals, rounding. Off-topic for Blender/Claude/Roblox asset pipeline; only tangential relevance for Luau scripting (e.g., int64 IDs for asset/user IDs).

## Claims
- c1: Luau numbers are 64-bit doubles (~15 digits precision); API docs distinguish float (32-bit), int (32-bit), and int64 for ID-type arguments such as Player.UserId. *(doc, high; other)*

## Numbers
- n1: **int range**: -2^31 to 2^31-1 Roblox API integer type
- n2: **int64 range**: -2^63 to 2^63-1 used for Roblox website IDs
