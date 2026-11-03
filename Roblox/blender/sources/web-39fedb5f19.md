---
type: research-source
id: web-39fedb5f19
title: "Roblox docs: workspace/streaming/techniques"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/workspace/streaming/techniques.md"
published: ""
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0681
relevance: 1
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "mesh-texture-limits", "other"]
---
# web-39fedb5f19

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox docs on converting games to instance streaming: recommended Workspace streaming properties, SLIM model LOD, model structure, script patterns that break under streaming, and an AI streaming skill (rbx-convert-to-streaming) runnable via Studio Assistant or any LLM through Studio's MCP server. Little on Blender; relevant only to MCP-driven Studio automation and model sizing/LOD.

## Claims
- c1: Roblox offers an AI streaming conversion skill (rbx-convert-to-streaming) that can run in Studio Assistant or via any LLM connected through Studio's MCP server. *(doc, high; automation-and-creator-workflows)*
- c2: A typical frontier-model streaming conversion takes about 20-30 minutes and roughly 200,000 tokens of context; large-context models are recommended. Back up the game first (File > Publish to Roblox As). *(doc, high; automation-and-creator-workflows)*
- c3: The skill sets recommended streaming properties, assigns SLIM LOD, refactors model structure, adds WaitForChild/nil checks, adds prefetches/replication foci, runs a playability check, and saves a change log file. *(doc, high; automation-and-creator-workflows)*
- c4: Set Model.LevelOfDetail to SLIM only on models with static meshes/parts; models modified at runtime or animated are not supported. *(doc, high; mesh-texture-limits)*
- c5: Keep each model's spatial extent under ~64 cubic studs so the whole model likely streams in together; split large models into smaller modular ones, each with its own LevelOfDetail. *(doc, medium; mesh-texture-limits)*
- c6: SLIM avatars support R15 player characters with body, dynamic head, standard or advanced R15 rig, and rigid/layered accessories. R6, NPCs and custom-proportion avatars are excluded. *(doc, high; avatar-ugc-accessories)*
- c7: Recommended streaming settings: EnableSLIMAvatars Enabled, ModelStreamingBehavior Improved, StreamingIntegrityMode PauseOutsideLoadedArea, StreamingMinRadius 64, StreamingTargetRadius 1024, StreamOutBehavior Opportunistic. *(doc, high; other)*
- c8: Atomic model guarantees apply only at initial replication; later-added instances stream normally. Persistent models never stream out and occupy memory permanently, so use sparingly. Persistent inside atomic makes the atomic model behave as persistent. *(doc, high; other)*
- c9: Decompose huge container models (many NPCs/props) into smaller spatially or logically grouped models for better streaming and LOD. *(doc, high; other)*
- c10: Test streaming with StreamingTargetRadius set to 64, and use the streaming debug overlay; watch for 'attempt to index nil with ...' errors indicating missing WaitForChild. *(doc, high; other)*

## Numbers
- n1: **Max model spatial extent for co-streaming**: ~64 cubic studs Recommended per-model extent so the whole model streams together
- n2: **StreamingMinRadius**: 64 (default) Recommended
- n3: **StreamingTargetRadius**: 1024 (default) Recommended; test at 64 minimum
- n4: **AI conversion time**: 20-30 minutes Typical frontier model run
- n5: **AI conversion context**: ~200,000 tokens Typical conversion

## Techniques
- t1: **Run streaming conversion skill via MCP**: Enable and connect the MCP server in Studio; open the game; in Assistant Settings > Skills ensure rbx-convert-to-streaming is on; prompt Assistant or the MCP-connected LLM to use the skill. Back up first.
- t2: **Prefetch before teleport**: Server calls player:RequestStreamAroundAsync(target) before PivotTo; use Player:AddReplicationFocus sparingly for areas that must stay loaded.
- t3: **Tag-based stream in/out detection**: Tag objects with CollectionService; use GetTagged plus GetInstanceAddedSignal/GetInstanceRemovedSignal on the client; use a Spawned attribute to avoid replaying spawn effects.

### Code: Prefetch area before teleporting character
```lua
local function teleportPlayer(player, teleportTarget)
	player:RequestStreamAroundAsync(teleportTarget)
	local character = player.Character
	if character and character.Parent then
		local currentPivot = character:GetPivot()
		character:PivotTo(currentPivot * CFrame.new(teleportTarget))
	end
end
```

## Points to
- Studio MCP server (studio/mcp.md)
- SLIM docs (workspace/streaming/slim.md)
- Roblox Assistant Skills
