---
type: research-source
id: web-ff5a806f78
title: "Roblox docs: art/characters/facial-animation/moods"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/characters/facial-animation/moods.md"
published: ""
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0316
relevance: 1
density: low
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "rigging-animation"]
---
# web-ff5a806f78

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox doc on facial-animation "moods" for dynamic heads: looping face animations created in Studio's Face Animation Editor, set via the Animate script's mood StringValue or HumanoidDescription, or disabled by destroying it. Blender is mentioned only as a tool to build animatable heads. No Claude/MCP/bpy content.

## Claims
- c1: A mood is a looping facial animation for dynamic heads; it plays alongside default animations (walk, climb, swim) and blends with them if they contain facial animation. *(doc, high; avatar-ugc-accessories)*
- c2: Custom character models with animatable heads can be built or modified in third-party software such as Blender or Maya; reference models are Blocky (FBX) and Goblin (zip). Details are in the 'Create basic heads' doc. *(doc, high; rigging-animation)*
- c3: Moods are authored in Studio: Avatar tab > Clip Editor > select the rig > Face button opens the Face Animation Editor with sliders. Save via the '…' menu; the animation appears under AnimSaves in the rig. *(doc, high; rigging-animation)*
- c4: To reuse a mood across games, right-click the animation in Explorer, choose Save to Roblox, and fill in the Asset Configuration; the result is an AnimationID. *(doc, high; automation-and-creator-workflows)*
- c5: Each animatable-head character has Animate LocalScript > mood StringValue. Its default AnimationId is a smile. The playback code is in a hidden internal script, so only the StringValue can be used to customize it. *(doc, high; avatar-ugc-accessories)*
- c6: A mood can be changed by setting animateScript.mood.Animation1.AnimationId, or via HumanoidDescription (e.g., IdleAnimation) and ApplyDescription. Moods can be disabled by destroying the mood object. *(doc, high; avatar-ugc-accessories)*

## Techniques
- t1: **Author a mood in Studio**: Add the head rig to the viewport, open Clip Editor, select the rig, click Face, adjust sliders, then Save. Optionally Save to Roblox to get an AnimationID.
- t2: **Apply a mood via HumanoidDescription**: Call humanoid:GetAppliedDescription(), set IdleAnimation to the animation asset ID, then call humanoid:ApplyDescription(clone).

### Code: Set a mood AnimationId when a character's appearance loads
```lua
local function onCharacterAdded(character)
	local humanoid = character:WaitForChild("Humanoid")
	local animateScript = character:WaitForChild("Animate")
	animateScript.mood.Animation1.AnimationId = "rbxassetid://7715145252" -- Mood
end

local function onPlayerAdded(player)
	player.CharacterAppearanceLoaded:Connect(onCharacterAdded)
end
```

### Code: Change the idle mood through HumanoidDescription
```lua
local descriptionClone = humanoid:GetAppliedDescription()
descriptionClone.IdleAnimation = 10725833199
humanoid:ApplyDescription(descriptionClone)
```

## Points to
- Create basic heads (art/characters/facial-animation/create-basic-heads)
- Animate heads / Face Animation Editor
- BlockyCharacter.fbx and GoblinCharacter.zip reference files
- dynamic-heads docs
