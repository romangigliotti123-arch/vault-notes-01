---
name: rig-checker
description: "Validate a Roblox character or NPC rig before it ships: R15 parts, Motor6D joints and their Part0/Part1, Humanoid and Animator, PrimaryPart, anchoring, accessory mass, duplicate names - then explain each failure and the repair. Use when a custom rig will not animate, an NPC T-poses or collapses, or after importing a model with a skeleton."
category: build
tags: rig, r15, humanoid, motor6d, animator, npc, character, skeleton, animation, joints
kb: Roblox/roblox-kb/3d-modeling-rigging-and-animation.md, Roblox/roblox-kb/ugc-and-avatar-economy.md, Roblox/roblox-kb/physics-pathfinding-and-npc-ai.md, Roblox/roblox-kb/building-art-and-assets.md
related: animation-priority-checker, animation-import-guide, accessory-fitting-guide, attachment-fixer, pivot-fixer, npc-spawner-builder, model-cleaner
---

# rig-checker

A rig is a contract: named parts, joints between them in the expected direction, and a Humanoid that drives them. Animations only work if the contract holds. This checks the contract and names the exact break.

## When to use
Custom or imported characters/NPCs; "my animation does nothing"; an NPC that falls apart or floats; before uploading animations. Not for: UGC accessory fitting (`accessory-fitting-guide`), non-humanoid creatures (custom rigs with their own joint names need their own spec).

## Inputs (max 2)
1. The rig Model (selection/path). 2. Intended use: player-like R15 NPC, static display dummy, or custom skeleton (default: R15 NPC).

## Procedure
1. Run `scripts/check_rig.luau` with TARGET set. It checks: Humanoid exists and `RigType` is R15; Animator present; all 16 R15 parts (HumanoidRootPart, Head, UpperTorso, LowerTorso, both arms (Upper/Lower/Hand) and legs (Upper/Lower/Foot)); the 15 Motor6Ds (Root, Waist, Neck, shoulders, elbows, wrists, hips, knees, ankles) with correct names, living in Part1, and Part0/Part1 pointing at the right neighbours; PrimaryPart = HumanoidRootPart; HumanoidRootPart not anchored (unless a static dummy); accessory parts Massless; duplicate part names.
2. Map each failure to a repair:
   - Missing part/motor: restore from Roblox's official R15 rig template (Rig Builder or the downloadable template) instead of hand-making it; copy the part, keep the name.
   - Motor6D with wrong Part0/Part1: set Part0 to the parent-side part and Part1 to the child part; keep the Motor6D inside Part1.
   - Wrong names: joint and part names are what animations target; rename exactly (case sensitive).
   - RigType R6 vs R15 mismatch: animations are rig-type specific.
   - Anchored root: the rig cannot be driven by Humanoid physics.
   - Non-massless accessory parts: set Massless true for parts that should not change mass.
3. Re-run until the report says RIG OK.
4. Behaviour test (needs Studio): put the rig in a test place, play a simple animation through `Humanoid.Animator:LoadAnimation` (see `animation-import-guide`), and check no limb detaches. Walk it with `Humanoid:MoveTo`. Screenshot.
5. Blender rig prep (official unless marked; `Roblox/blender/blender-cheat-sheet-claude-blender-roblox.md` section 4): start from Roblox's Rig_and_Attachments_Template.blend, Root and LowerTorso at 0,0,0, all 15 meshes parented to ONE armature; before auto weights apply scale and rotation, weld duplicate vertices and delete loose parts (corroborated: islands make auto weights fail); at most 4 bone influences per vertex and none on Root or HumanoidRootNode; bones frozen at scale 1 and rotation 0; test each joint in Pose mode (Alt+R resets). Export FBX with Add Leaf Bones off.
5b. For imported skeletons (Blender/Maya): export rules from the vault: correct FBX scale and orientation, standard R15 bone hierarchy and names, unique mesh and bone names, one animation track per export at 30 FPS or higher, bake animation only when exporting animation.

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` -> `execute_luau` (Edit) with `scripts/check_rig.luau` -> repairs via `execute_luau` -> re-run -> `start_stop_play` -> `execute_luau` (Server) to `MoveTo` and play an animation -> `screen_capture` -> `get_console_output`.

## Fallback
Command bar with the rig selected. Without Studio, review the rig's hierarchy printout (names, classes, Motor6D targets) the owner pastes; behaviour tests are `untested`.

## Evidence
`Roblox/roblox-kb/3d-modeling-rigging-and-animation.md` (start from official templates; FBX scale/orientation; unique and standard bone and mesh names; one animation track per file; bake animation only when exporting animation), `Roblox/roblox-kb/ugc-and-avatar-economy.md` (reference bodies, templates, never destroy cage geometry), `Roblox/roblox-kb/physics-pathfinding-and-npc-ai.md`. R15 part and joint names are from the Roblox character model; verify against a fresh Rig Builder rig when in doubt.

## Output
```
RIG OK: Workspace.Guard passes the R15 structure checks
or
RIG PROBLEMS (3) in Workspace.Guard:
- LeftElbow.Part1 should be LeftLowerArm
- missing part RightHand
- Humanoid has no Animator
```
plus the repair list and the behaviour-test result.

## Acceptance checks
- [ ] The script ran and its output is quoted before and after repairs.
- [ ] Each problem has a specific repair; none left as "fix the rig".
- [ ] The behaviour test result is stated (animated, walked, screenshot) or `untested`.
- [ ] Rig type matches the animations that will be used.
- [ ] For a Blender rig: max influences per vertex is 4, Root/HumanoidRootNode carry none, transforms are frozen, and Add Leaf Bones was off (checked in the export settings or file, not recalled).
- [ ] The script passes the pack luau-check run.

## Pitfalls
Trusting a rig because it looks right (joint direction decides animation). Fixing symptoms in animation instead of the rig. Re-parenting Motor6Ds into the wrong part. Mixing R6 animations with an R15 rig. Forgetting Animator on server-spawned NPCs.

## Related
`animation-priority-checker`, `animation-import-guide`, `accessory-fitting-guide`, `attachment-fixer`, `pivot-fixer`, `model-cleaner`.
