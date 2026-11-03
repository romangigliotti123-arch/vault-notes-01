---
type: research-source
id: web-227ff5bc5d
title: "Roblox docs: workspace/streaming/index"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/workspace/streaming/index.md"
published: ""
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0615
relevance: 1
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "other"]
---
# web-227ff5bc5d

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox docs on instance streaming (Workspace.StreamingEnabled): how workspace content loads/unloads, streaming properties and recommended values, model streaming modes, replication foci, predictive streaming, pause handling, and debug overlays. Only tangentially relevant to Blender/Claude/export pipeline; matters for how imported MeshParts and models behave at runtime.

## Claims
- c1: Streaming applies only to Workspace descendants; models in ReplicatedStorage/ReplicatedFirst are not streamed, so atomic replication is not guaranteed there. *(doc, high; other)*
- c2: On join, BaseParts (Parts and MeshParts), Atomic/Persistent/PersistentPerPlayer models, and Nonatomic models under Improved ModelStreamingBehavior are deferred, not replicated immediately. *(doc, high; other)*
- c3: Assemblies stream in as complete units with Constraints and Attachments (anchored assemblies only stream parts within radius) and stream out only when all parts are eligible. Large moving assemblies can cause network/CPU spikes. *(doc, high; other)*
- c4: StreamingEnabled is enabled by default for new places and cannot be set from a script; the streaming properties are non-scriptable and set on Workspace in Studio. *(doc, high; other)*
- c5: Recommended settings: ModelStreamingBehavior Improved, StreamingIntegrityMode PauseOutsideLoadedArea, StreamOutBehavior Opportunistic, default StreamingMinRadius 64 and TargetRadius 1024. *(doc, high; other)*
- c6: StreamingTargetRadius should be larger than StreamingMinRadius, since the gap acts as a buffer; equal values risk more network pauses. *(doc, high; other)*
- c7: Workspace.EnableSLIMAvatars generates a SLIM level-of-detail model for avatar characters. Setting Model.LevelOfDetail to SLIM does the same for other models. *(doc, medium; avatar-ugc-accessories)*
- c8: Each additional replication focus raises server streaming workload: nine moving foci can cost about as much as ten players. Too many foci also make client OS memory kills more likely. *(doc, high; other)*
- c9: Persistent models are sent whole soon after join, before Workspace.PersistentLoaded fires, and never stream out. They are meant for rare cases and overuse hurts performance. *(doc, high; other)*
- c10: Streamed-out instances are parented to nil, not destroyed. Local-only property changes on the client can be lost when they stream back in. *(doc, high; other)*

## Numbers
- n1: **StreamingMinRadius default**: 64 recommended default, studs; highest-priority stream-in radius
- n2: **StreamingTargetRadius default**: 1024 recommended default; max stream-in distance
- n3: **Debug camera zoom example**: 1000 CameraMaxZoomDistance to view most of world while debugging streaming

## Techniques
- t1: **Streaming debug overlay**: Press Shift+F3 in a live experience, or Shift+Ctrl+F3 (Windows) or Shift+Cmd+F3 (Mac) in Studio playtest. Then press Shift+1 repeatedly to reach the 4th panel, the Streaming view, which colors regions by radius.
- t2: **Custom pause screen**: Keep StreamingIntegrityMode at PauseOutsideLoadedArea. Call GuiService:SetGameplayPausedNotificationEnabled(false), then connect Player:GetPropertyChangedSignal('GameplayPaused') to show or hide a custom GUI.
- t3: **Predictive streaming**: Set Workspace.PredictiveStreamingMode to Enabled. This adds temporary foci for spawn pre-fetching and CFrame-return areas, skips resource-constrained clients, and needs no code changes.

### Code: Custom pause GUI when streaming pauses gameplay
```lua
local Players = game:GetService("Players")
local GuiService = game:GetService("GuiService")
local player = Players.LocalPlayer
GuiService:SetGameplayPausedNotificationEnabled(false)
local function onPauseStateChanged()
	if player.GameplayPaused then
	else
	end
end
player:GetPropertyChangedSignal("GameplayPaused"):Connect(onPauseStateChanged)
```

## Points to
- https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/workspace/streaming/techniques.md
- https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/workspace/streaming/slim.md
