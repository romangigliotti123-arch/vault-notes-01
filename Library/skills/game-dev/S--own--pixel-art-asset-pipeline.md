---
id: "pixel-art-asset-pipeline"
type: skill
category: "game-dev"
source: "own"
license: "first-party"
repo_path: "skills/game-dev/pixel-art-asset-pipeline/SKILL.md"
description: "Plan and produce 2D game art (sprites, tilesets, UI icons) with consistent palette, size and export settings, using Aseprite or image-generation tools. Use when a 2D game needs coherent art quickly."
orig_name: "pixel-art-asset-pipeline"
tags: [lib/skill, cat/game-dev, src/own]
---

# pixel-art-asset-pipeline

> Plan and produce 2D game art (sprites, tilesets, UI icons) with consistent palette, size and export settings, using Aseprite or image-generation tools. Use when a 2D game needs coherent art quickly.

Type: skill | Category: [[categories/cat-game-dev|game-dev]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/game-dev/pixel-art-asset-pipeline/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# 2D asset pipeline

1. Style sheet first: grid size (16, 32 or 64 px), a limited palette (16-32 colours, saved as a .gpl/.hex file), outline rule, light direction, shading steps, animation frame counts and fps. Every asset must obey it.
2. Asset list: name | size | frames | usage | status. Group by character, enemy, tile, prop, UI, effect. Start with a vertical slice (one character, one tileset, one enemy, HUD).
3. Production: draw in Aseprite (CLI: `aseprite -b file.aseprite --sheet out.png --data out.json`) or generate with an image model and clean up (palette-map, down-scale with nearest neighbour, fix outlines). Never use copyrighted characters or styles of a living artist's named work; keep a log of generator, prompt and licence per asset.
4. Export: sprite sheets with JSON frames, power-of-two atlas sizes where the engine wants it, nearest-neighbour filtering, no mipmaps for pixel art, trim transparent borders, consistent pivot.
5. Naming: `category_name_action_frame` lowercase; folder per category; import presets saved in the engine.
6. QA: view at 1x, 2x and in-engine at target resolution; check palette violations with a script (count colours), seams in tiles, animation loops, readability on a phone.
7. Roblox note: upload decals/spritesheets through Creator Hub (moderated, may require Robux for some assets); decide image sizes within Roblox limits and verify in the current docs.
