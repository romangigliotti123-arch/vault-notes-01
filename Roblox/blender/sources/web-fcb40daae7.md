---
type: research-source
id: web-fcb40daae7
title: "Roblox docs: avatar/character-bodies/test-studio"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/character-bodies/test-studio.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 3
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "other", "rigging-animation"]
---
# web-fcb40daae7

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator docs page on testing imported character bodies in Studio using the Avatar test place. Covers setup (rename model to StarterCharacter under StarterPlayer), the test UI menus (avatar swap, emotes, skin tone, clothing, movement, body proportions, lighting), and checklists for movement, lighting/color, and clothing/accessory fit. Says to revisit rigging or caging when behavior is wrong. Does not cover Blender, bpy, MCP, or FBX/glTF export settings.

## Claims
- c1: Testing workflow: after importing a custom character body, rename the model to StarterCharacter and drag it into StarterPlayer, deleting any existing StarterCharacter. *(doc, high; blender-roblox-export-import)*
- c2: Avatar test place checklist covers walking, sitting, climbing, swimming, jumping, dying (ragdoll), facial animation, and emotes. *(doc, high; avatar-ugc-accessories)*
- c3: Clothing that fits wrong suggests caging or attachment point problems to fix in the 3D modeling tool; layered clothing can stack in unconventional orders. *(doc, medium; avatar-ugc-accessories)*
- c4: Unexpected movement behavior suggests rigging or skinning problems to revisit in the modeling software. *(doc, high; rigging-animation)*
- c5: Page does not mention Blender, bpy, blender-mcp, or FBX/glTF export settings; it only links to a separate test-blender page and an import page. *(doc, high; other)*

## Techniques
- t1: **Avatar test place setup**: Download test place, import body via import.md, rename model to StarterCharacter, drag into StarterPlayer, playtest, use right-side UI menus to test.

## Quotes (brief, for attribution)
> Verify the important aspects of your character model in a custom Studio test game.  (create.roblox.com)

## Points to
- https://www.roblox.com/games/95623161111019/Avatar-Test-Place
- ./test-blender.md
- ./import.md
- ../../avatar-setup/
- ../../art/characters/creating/blender-configurations.md#custom-skin-tones
