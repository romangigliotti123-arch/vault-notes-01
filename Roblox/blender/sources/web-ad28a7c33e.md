---
type: research-source
id: web-ad28a7c33e
title: "Roblox docs: art/characters/creating/modeling-best-practices"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/characters/creating/modeling-best-practices.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0014
relevance: 2
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "other", "rigging-animation"]
---
# web-ad28a7c33e

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator docs page on modeling (sculpting) best practices for avatar head/body templates. Core rule: edit templates non-destructively by moving existing vertices only, never adding or deleting vertices, to preserve skinning and facial animation data. Covers edge flow around forehead, mouth, eyes, and eyelid/eyebrow spacing. Does not mention Blender, bpy, MCP, or export settings.

## Claims
- c1: When editing Roblox character templates, do not delete or add vertices to the character body; this keeps skinning and facial animation data functional. *(doc, high; avatar-ugc-accessories)*
- c2: Non-destructive sculpting means changing only vertex positions of existing vertices, e.g. with Blender sculpting tools, so weights and animation data stay attached. *(doc, high; avatar-ugc-accessories)*
- c3: Extreme geometric changes, even without deleting vertices, can still harm rigging and skinning; pick a starting template close to the final design and sculpt proportionally. *(doc, high; rigging-animation)*
- c4: Mouth and eye topology should generally not be modified in the tutorial because it can break tongue, jaw, eyeball, and saved facial data; a sculpting mask can protect these areas. *(doc, high; rigging-animation)*
- c5: Eyelids and eyebrows need natural spacing; if improperly modeled they can clash during facial poses. *(doc, medium; rigging-animation)*
- c6: Topology collisions (e.g. upper and lower eyelids passing through each other when closing) cause jagged artifacts and may require manual rig, skinning, or facial data fixes. *(doc, high; avatar-ugc-accessories)*
- c7: Page recommends checking the blender-configurations page before modeling and links to modeling-tips as the next step. *(doc, low; other)*

## Techniques
- t1: **Non-destructive template sculpting**: Use Blender sculpt brushes to move existing vertices only. Avoid delete/add-vertex operations on the body. Use a sculpting mask over face areas that must not change (mouth, eyes).
- t2: **Edge-flow preservation**: Keep vertices a proportionate distance apart, follow muscle and contour lines, and keep forehead wrinkle and nasolabial edges in their original relative positions.

## Quotes (brief, for attribution)
> When editing templates, don't delete or add vertices to your character body. This ensures that your character's skinning and facial animation data remains unaltered and fully functional.  (create.roblox.com)

## Points to
- /art/characters/creating/blender-configurations
- /art/characters/creating/modeling-tips
