---
type: research-source
id: yt-q9Z7hpQHQKY
title: "Make a REAL Cash System + Shop in Roblox Studio (Beginner Friendly!)"
source_type: "youtube"
creator: "Rool-Studio"
url: "https://www.youtube.com/watch?v=q9Z7hpQHQKY"
published: "2025-11-26"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 0
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "other"]
---
# yt-q9Z7hpQHQKY

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner tutorial on building a cash system and shop in Roblox Studio (Lua scripting only). Covers leaderstats creation on server, a GUI label bound to cash, a button firing a RemoteEvent with cooldown, server-side purchase check, and a ProximityPrompt opening the shop. Contains no Blender, bpy, blender-mcp, or asset-pipeline content, so it is off-topic for the requested subject.

## Claims
- c1: Source covers Roblox Studio Lua cash/shop systems only; no Blender, Claude, bpy, or Blender-to-Roblox export content. *(doc, high; other)*
- c2: [0:40] Tutorial says cash logic belongs in a server script in ServerScriptService so players cannot change money on the client. *(opinion, high; automation-and-creator-workflows)*
- c3: [1:20] Leaderstats folder with an IntValue named cash, starting at 100, is shown automatically on the leaderboard. *(doc, high; other)*

## Numbers
- n1: **starting cash value**: 100 

## Techniques
- t1: **Leaderstats setup**: On Players.PlayerAdded, create Folder named leaderstats parented to player; add IntValue named cash set to 100 inside it.
- t2: **Server-validated purchase**: Client fires RemoteEvent with price; server compares to leaderstats cash, subtracts if affordable, then clones tool from ReplicatedStorage.

### Code: Create leaderstats folder with cash IntValue on join (as described; exact code not shown in transcript)
```lua
game.Players.PlayerAdded:Connect(function(player)
	local leaderstats = Instance.new("Folder")
	leaderstats.Name = "leaderstats"
	leaderstats.Parent = player
	local cash = Instance.new("IntValue")
	cash.Name = "cash"
	cash.Value = 100
	cash.Parent = leaderstats
end)
```

## Quotes (brief, for attribution)
> Roblox automatically shows any values inside a folder named leaderstats on the leaderboard. That's why the name is important.  (at 1:20, Rool-Studio)
