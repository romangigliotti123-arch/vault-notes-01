<!-- cold: rbx-thumbnail/blender.md | read when: the user wants rendered 3D GFX for an icon or thumbnail and Blender may be installed (optional; never required). -->

# Blender GFX renders (optional, UNTESTED LIVE)

Status: written from the Blender manual and creator videos; Blender was not installed on the build host, so no real render has run. Treat every recipe and every open question below as UNTESTED LIVE and report what you saw on the first real run.

Cost: the user's own free Blender install and local compute; moderate use (about 12 renders per session, 3 render-score-fix rounds per concept); zero standing tokens. Vetoed: Blender MCP (needs an add-on, a socket and a live GUI), AI texture/HDRI generation, ComfyUI or AI upscaling inside Blender, asset or HDRI downloads, add-ons such as Starter Rigs. Never install or download anything; if Blender is missing, say the one line from `detect` and use the checklist and prompts only.

## Pipeline
`T="bash .rbx/claude-kit/tools/pyrun .rbx/claude-kit/vault-mode/.claude/skills/rbx-thumbnail/scripts/blender_gfx.py"`
1. `$T detect` : Blender on PATH, `BLENDER_BIN`, or the standard Windows, macOS, Linux and Steam folders (Flatpak is not probed). Exit 3 + the missing line when absent.
2. `$T gen --recipe icon|portrait|action|scene|variants --subject primitive:gem|FILE --name N --project DIR [--palette warm|cool|comp] [--hero-color RRGGBB] [--flat-color RRGGBB[,..]] [--outline] [--glow] [--pose part=rx,ry,rz] [--size icon|thumb|WxH] [--brief b.json]` writes `renders/_scripts/N_<recipe>.py` (+ `.json` sidecar), a GPL-2.0-or-later bpy script (blender.org requires a GPL-compatible licence for published Blender-API scripts; the renders are the user's).
3. `$T check SCRIPT` : ast refusal. `$T run SCRIPT [--engine eevee|cycles] [--samples N] [--allow-high] [--timeout S]` runs `blender -b --factory-startup [--offline-mode] --python-exit-code 1 -P SCRIPT -- --out-dir renders --engine E --samples N --time-limit 120 [--subject F]` (the exit-code flag must precede `-P`), cwd and outputs = `<project>/renders/`, prints `OUTPUT <png> WxH`.
4. Score each PNG like any candidate source (`thumb_score.py inspect`, rubric.md), 2-5 clearly different variants for personalization (vary element, setting, colour, not just brightness). Records `<png>.json` = provenance.

## Recipes (all: 3-point light with a contrasting rim, world gradient, camera fitted from bounds, hero objects named `hero_*`, background objects `bg_*`, no text objects)
- icon (A): 1024 square, hero 70-80% of the frame, focal 55, three-quarter view; renders transparent, gradient and complementary-colour variants.
- portrait (B): 1024x1280, focal 80, depth of field f/4 on the face, warm key front-left, cool rim, small point light near the face, dark gradient.
- action (C): 1920x1080, focal 28, low camera, roll 10 degrees, hero on the left third, optional `--pose`.
- scene (D): hero left third + one secondary element right third + ground + gradient; 2-4 elements, no text.
- variants (E): scene rendered in warm, cool and complementary palettes: `N_variants_<palette>.png`.
Thumbnails shift the subject up so the bottom 15% stays free of key content (player-count overlay). `--flat-color` overrides untextured Studio exports (Studio OBJ carries geometry only; textures and SurfaceAppearance are not exported), `--outline` is an inverted-hull toon outline, `--glow` is an optional compositor glare that is skipped on error.

## Subjects
Primitives always work (cube, sphere, cone, cylinder, torus, gem). Models: an OBJ/FBX/GLB the user exports from Studio or their modelling tool and puts INSIDE the project folder; it is scaled to a unit radius. Only render models the user made or has rights to; third-party or Marketplace assets and brands need their own permission (Roblox IP guidelines). The official Roblox terms for third-party avatar renders in thumbnails were not retrievable: OPEN, do not assert. Renders must still pass gates G1-G3 (show only what the game has).

## Versions (the generator bakes the target; the script also tries/excepts at run time)
| Topic | 3.x | 4.0-4.1 | 4.2-4.5 | 5.0+ |
|---|---|---|---|---|
| EEVEE id | BLENDER_EEVEE | BLENDER_EEVEE | BLENDER_EEVEE_NEXT | BLENDER_EEVEE |
| OBJ import | import_scene.obj before 3.2, wm.obj_import after | wm.obj_import | same | same |
| Material/world use_nodes | needed | needed | needed | deprecated, skipped |
| Compositor | scene.node_tree | same | same (EEVEE bloom removed) | compositing_node_group |
`--version` gives the target; without Blender the default target is 4.5.

## Limits and safety
EEVEE 64 samples (timeout 180 s); Cycles CPU 128 with denoise (timeout 420 s); hard cap 256 only with `--allow-high`; per side 512..4096. Ladder: EEVEE, then Cycles CPU 64 once, then report "render failed" and stop. Success = exit 0 + PNG of the declared size under `renders/`. `check` is an allow-list ast refusal: only bpy, bmesh, mathutils, math, random, colorsys, sys.argv; refuses os, subprocess, socket, shutil, ctypes, urllib, http, requests, importlib, pathlib, eval, exec, compile, open, getattr, `__import__`, dunder attributes, file saves, preferences, bpy.utils, save_render and path-like strings (paths arrive only as `--out-dir`/`--subject`). It is best effort, not a sandbox: run only scripts you or the vault generated, and give pasted third-party scripts the same check. The environment is reduced to a short whitelist, no add-ons, no `-y`.
LLM-written bpy is fine (the AI part of this pipeline): describe the scene, write plain bpy, run it through `check` then `run`; stale API names are the common failure, the table above is the fix.

## Open questions (UNTESTED LIVE; answer on the first real run)
1. Does EEVEE render with `-b` on this GPU/driver; Cycles CPU time at 1920x1080 and 128 samples.
2. `write_still` file naming (extension, no `####`) per version.
3. Camera distance with sensor fit AUTO for 16:9 and 1:1; world gradient direction; `shift_x/shift_y` sign (left-third placement).
4. Property names: Glare node, `use_backface_culling`, `--offline-mode` presence, Principled emission sockets on 3.6.
5. Studio OBJ look and scale after import (axes, white parts) and whether the unit-radius scaling is right.
6. Whether 5.x deprecation warnings trip `--python-exit-code`.
