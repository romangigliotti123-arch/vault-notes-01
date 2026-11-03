---
type: research-source
id: web-014a1d2aa6
title: "Roblox docs: parts/textures-decals"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/parts/textures-decals.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0019
relevance: 1
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "mesh-texture-limits"]
---
# web-014a1d2aa6

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator docs on Texture vs Decal objects in Studio: Texture repeats per StudsPerTileU/V and supports OffsetStudsU/V and TweenService animation; Decal stretches. Covers ColorMapContent, Face selection, Color3 tint, Transparency, and texture streaming. Does not mention Blender, bpy, blender-mcp, FBX/glTF, or export settings.

## Claims
- c1: Roblox Texture objects repeat on a surface; Decal objects stretch to fit the surface area. *(doc, high; mesh-texture-limits)*
- c2: Texture scale is set by StudsPerTileU and StudsPerTileV (tile size in studs); part size only changes repeat count. *(doc, high; mesh-texture-limits)*
- c3: Texture streaming is enabled automatically and loads baseline textures first, then raises quality within device memory; supports MeshPart, SurfaceAppearance, Texture, Decal, MaterialVariant. *(doc, high; mesh-texture-limits)*
- c4: Best practice: prefer individual textures over atlases; an atlas requested at high resolution streams in entirely; use near-uniform texel density in UV meshes. *(doc, high; mesh-texture-limits)*
- c5: Textures can be animated by TweenService tweening OffsetStudsU/V and StudsPerTileU/V (example uses infinite-repeat tweens for fog). *(doc, high; automation-and-creator-workflows)*

## Numbers
- n1: **Color3 example**: [255, 0, 100] 
- n2: **Transparency range**: 0 (visible) to 1 (invisible) 
- n3: **Fog tween durations**: 8s and 7s, OffsetStudsV=50 

## Techniques
- t1: **Texture tiling and offset**: Set StudsPerTileU/V to tile size in studs; adjust OffsetStudsU/V to shift position; tween these for animated surfaces.

### Code: Tween two textures to simulate layered moving fog
```lua
local TweenService = game:GetService("TweenService")
local texture1 = script.Parent.Texture1
local texture2 = script.Parent.Texture2
local tweenInfo1 = TweenInfo.new(8, Enum.EasingStyle.Sine, Enum.EasingDirection.InOut, -1)
local tween1 = TweenService:Create(texture1, tweenInfo1, {OffsetStudsV=50})
local tweenInfo2 = TweenInfo.new(7, Enum.EasingStyle.Sine, Enum.EasingDirection.InOut, -1, true)
local tween2 = TweenService:Create(texture2, tweenInfo2, {OffsetStudsU=50, StudsPerTileU=55, StudsPerTileV=45})
tween1:Play()
tween2:Play()
```

## Quotes (brief, for attribution)
> A Class.Texture is an image you can place on any face of a part or union that repeats both horizontally and vertically on the size of the surface.  (create.roblox.com)

## Points to
- https://en.help.roblox.com/hc/articles/203313410
- https://en.help.roblox.com/hc/articles/115004647846
