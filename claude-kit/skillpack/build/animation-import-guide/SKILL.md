---
name: animation-import-guide
description: "Walk the whole animation path - rig, export from Blender or Maya, upload, publish, reference by id, play on the right rig - with the settings that break imports, and finish with a Play test that loads the clip and reports length, looping, priority and keyframes. Use when an exported animation is missing, T-poses, deforms, or will not play."
category: build
tags: animation, import, export, fbx, blender, maya, upload, publish, animator, rig, keyframe
kb: Roblox/roblox-kb/3d-modeling-rigging-and-animation.md, Roblox/roblox-kb/ugc-and-avatar-economy.md, Roblox/roblox-kb/tools-and-resources.md
related: rig-checker, animation-priority-checker, accessory-fitting-guide, tween-helper-builder, asset-license-checker
---

# animation-import-guide

Most failed animation imports are one of five things: a non-standard rig, wrong export scale or axes, more than one animation per file, an unpublished or foreign asset id, or the wrong Animator. This is the checklist in order, with a verification script at the end. The upload itself is the owner's action in Studio's animation tools; this skill prepares and checks.

## When to use
First time wiring animations, a clip that exports but does not appear, a rig that deforms after import, or setting up a repeatable pipeline. Not for: priority and looping fixes (`animation-priority-checker`), or rig validation (`rig-checker`).

## Inputs (max 2)
1. The source: made in Studio's Animation Editor, or exported from Blender/Maya. 2. The target: player character, NPC, or custom skeleton (default: R15 NPC).

## Procedure
1. Rig first: run `rig-checker` on the target rig. Start from the official R15 templates, not from scratch; standard bone hierarchy and names, unique mesh and bone names.
2. If animating outside Studio, export per the vault: Blender 3.4 or newer, Apply Scalings = FBX Unit Scale, Add Leaf Bones off, Path Mode Copy with Embed Textures, Forward = Z and Up = Y, Limit to Selected Objects; Maya: Up Axis Y, Units Automatic, Animation on. Bake Animation only for keyframed clips. One animation track per file, 30 FPS or higher, one `.fbx` per animation from the same rig. Remove `.001` suffixes.
3. Check the transforms before skinning or exporting: mesh scale 1 and rotation 0, joints at scale 1 and rotation 0, bind pose frozen, at most 4 bone influences per vertex. A deforming limb is almost always an unfrozen transform.
3b. Clip rules (official, Creator Docs animation/editor and avatar/emotes/import; `Roblox/blender/blender-cheat-sheet-claude-blender-roblox.md` section 4): a looping clip needs the first pose copied to the final frame and Loop on; a clip that replaces the default jump or run needs its last keyframe named exactly `End` (case-sensitive) and must be published first; an emote needs an R15 rig converted to a CurveAnimation (Curve Editor), not a KeyframeSequence; expect AnimationConstraint rather than Motor6D under the Avatar Joint Upgrade.
4. Import in Studio (Animation Editor import, or the Avatar importer), then PUBLISH the animation to Roblox. Saved-but-unpublished animations stay local and do not replicate or load for other clients.
5. Reference by id: `rbxassetid://<number>`, owned by the same creator (account or group) as the experience, otherwise it will not load.
6. Verify with `scripts/play_test_animation.luau` in Play (server): set `ANIMATION_ID`, run it. It loads the clip on the rig's Animator, plays for 0.6 s, and prints length, looped, priority, whether time advanced, and keyframe names, then cleans up. An empty id is rejected on purpose.
7. If it plays but loses to another clip, hand over to `animation-priority-checker`. If limbs detach or deform, go back to steps 1 and 3.
8. Record the final ids in a module (`Animations.luau` with name -> id) so scripts never hard-code numbers; ids are the owner's, never invented.

## Studio MCP path
`list_roblox_studios` -> `start_stop_play` -> `execute_luau` (datamodel_type Server) with `scripts/play_test_animation.luau` after setting `ANIMATION_ID` -> `get_console_output` -> `screen_capture` of the posed rig -> `start_stop_play` (stop).

## Fallback
Without Studio you can still check the export settings list and the file layout (one track per file, names unique). The play test needs the engine: `untested`.

## Evidence
`Roblox/roblox-kb/3d-modeling-rigging-and-animation.md` (official templates; FBX scale, orientation and bones; bake animation only when exporting animation; one track per file at 30 FPS or higher; unique standard names; freeze transforms; 4 influences max; publish before referencing; animations replicate without extra remotes), `Roblox/roblox-kb/ugc-and-avatar-economy.md`. Exporter menus change between Blender and Studio versions: live-check names before quoting them.

## Output
```
ANIMATION IMPORT: Walk_Forward  rbxassetid://<owner supplies>
export ok | published | loads on Workspace.Dummy: length 0.83s, looped=true, priority Movement, time advanced 0.60s
Untested: deformation on the second rig, mobile playback
```

## Acceptance checks
- [ ] The play test ran in Play and its output is quoted (length, looped, priority, time advanced).
- [ ] Rig validation (`rig-checker`) passed before export.
- [ ] Export settings list was checked line by line, not recalled.
- [ ] The animation is published and owned by the experience's owner.
- [ ] Ids live in one module; none were guessed.
- [ ] Looping clips have the first pose copied to the last frame; replacement clips end in a keyframe named exactly `End`; emotes are CurveAnimations on R15.

## Pitfalls
Exporting several animations in one FBX. Blender's default scale and leaf bones. Leaving Bake Animation on for static models. Testing a clip owned by another account. Using R6 animations on R15 rigs (rig-type specific). Reading the Animator on the wrong model (player character vs NPC). A looping clip whose first and last frames differ.

## Related
`rig-checker`, `animation-priority-checker`, `accessory-fitting-guide`, `tween-helper-builder`, `asset-license-checker`.
