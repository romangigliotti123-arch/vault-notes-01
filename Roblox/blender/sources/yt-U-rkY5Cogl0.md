---
type: research-source
id: yt-U-rkY5Cogl0
title: "Roblox Game Breaking? You're Organizing Scripts Wrong"
source_type: "youtube"
creator: "SmartyRBX"
url: "https://www.youtube.com/watch?v=U-rkY5Cogl0"
published: "2026-01-23"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 0
density: low
tags: ["research-source", "youtube", "other"]
---
# yt-U-rkY5Cogl0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox scripting architecture video, not Blender. Argues each game system needs a single owner, typically a ModuleScript in ReplicatedStorage or server code; server decides, client requests; avoid copy-pasted logic and over-modularizing. No Blender, bpy, blender-mcp, FBX/glTF, or asset pipeline content.

## Claims
- c1: [0:00] Roblox games break as features are added because scripts lack a single owner for each system, not because code is bad. *(opinion, medium; other)*
- c2: [2:14] Shared config data (e.g., currency config) belongs in a ModuleScript in ReplicatedStorage so server and client see the same values. *(opinion, medium; other)*
- c3: [4:27] Local scripts should request things and server scripts should decide things; the server holds the rules and truth. *(opinion, medium; other)*
- c4: [5:53] Copy-pasting logic across scripts causes later problems; keep functions and values in one module per system. *(opinion, medium; other)*
- c5: [6:34] Over-modularizing early is a failure mode; create a module only for permanent, cross-script functions or values, and modules can hold many functions. *(opinion, medium; other)*

## Techniques
- t1: **Single-owner ModuleScript pattern**: Put system logic (e.g., CurrencyService with add/remove/get) in a ModuleScript; other scripts call its functions and never modify the data directly. Shared config goes in ReplicatedStorage.

## Quotes (brief, for attribution)
> Every system needs to have a single owner. The owner is the only place that decides. Everything else asks, never decides.  (at 1:40, SmartyRBX)
> Local scripts should request things. Server scripts should decide things.  (at 4:27, SmartyRBX)
