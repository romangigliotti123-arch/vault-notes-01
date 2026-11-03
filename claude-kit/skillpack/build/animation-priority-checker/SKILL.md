---
name: animation-priority-checker
description: "Load every animation in a place onto a rig in Play and check each track's Priority and Looped against its role (idle, movement, action), naming the exact clip that gets overridden, never loops, or blocks other animations, with the fix to make in the Animation Editor or on the track. Use when an animation does not play, plays under idle, or loops forever."
category: build
tags: animation, priority, animationtrack, looped, idle, action, override, animator, humanoid
kb: Roblox/roblox-kb/3d-modeling-rigging-and-animation.md, Roblox/roblox-kb/combat-and-gameplay-systems.md, Roblox/roblox-kb/physics-pathfinding-and-npc-ai.md
related: rig-checker, animation-import-guide, accessory-fitting-guide, tween-helper-builder, npc-spawner-builder
---

# animation-priority-checker

When several animations touch the same joint, the highest AnimationPriority wins; equal priority blends or the newest wins. Wrong priority is the usual reason an attack "does nothing" (it is under Idle/Movement) or a pose never lets go (idle set to Action). This checks every clip against naming rules and reports; the fix is a property on the published asset or the track.

## When to use
An animation seems ignored, a pose sticks, a death or emote is overridden by walk, a clip loops when it should not, or after importing a batch of clips. Not for: rig joint problems (`rig-checker`), or upload and wiring (`animation-import-guide`).

## Inputs (max 2)
1. The rig (a Model with an Animator in Workspace; default: the first found). 2. Any role words beyond the defaults (for example `gather`, `dodge`), with the priority each should have.

## Procedure
1. Connect and enter play mode on the server (below): Edit mode has no running Animator.
2. Run `scripts/anim_audit.luau`. For each Animation instance with an id it loads a track on the rig's Animator (never plays it), reads `Priority`, `Looped` and `Length`, applies the rules in `scripts/AnimRules.luau` (Lune-tested), destroys the track and prints one line per clip.
3. The default rules (vault: seven priority levels, Core lowest up to Action4 highest; idle lowest gameplay level; jump above idle):
   - idle, stand, breath: Idle, looped.
   - walk, run, sprint, swim, climb: Movement, looped.
   - jump, fall, land: at least Movement, not looped.
   - attack, swing, punch, slash, shoot, reload, cast, emote, dance, wave: Action or higher, not looped.
   - Core is always flagged: it loses to every default animation.
4. For each flagged clip, fix at the source: open the animation in the Animation Editor, set the priority (and Looped), republish, update the id. For a quick runtime override while you test: `track.Priority = Enum.AnimationPriority.Action` in a script.
5. Stack check for combat: a hit-react should sit above the attack it interrupts; a death above everything. Set the levels as a table in the report, not per clip.
6. Re-run until clean; then behaviour-test (see `animation-import-guide` play test) and screenshot a layered pose (walk + attack).

## Studio MCP path
`list_roblox_studios` -> `start_stop_play` (play) -> `execute_luau` (datamodel_type Server) with `scripts/anim_audit.luau` -> `get_console_output` -> `start_stop_play` (stop) -> fixes in the Animation Editor (owner) -> repeat.

## Fallback
Without a running Studio, list animations and their intended roles from the project, and apply `AnimRules.check(name, priority, looped)` under Lune to the values the owner reads from the editor; the engine behaviour is `untested`.

## Evidence
`Roblox/roblox-kb/3d-modeling-rigging-and-animation.md` (overlapping animations resolve by priority, seven levels Action4 highest to Core lowest, give idle a lower priority; loops: copy the first pose to the last frame; publish before referencing). The keyword table is the skill's convention, extend it per game. Animations published by another account cannot be loaded by this rig: reported as "could not load".

## Output
```
ANIM AUDIT: rig Workspace.Dummy
 Attack_Slash: Movement, looped=true, length=0.60s <- priority below Action; should not loop
 Idle_Main: Action, looped=true <- priority above Idle: it will block actions
checked 14 animations, 2 with problems; read-only run
```

## Acceptance checks
- [ ] Ran in play mode on the server; the report shows the rig used.
- [ ] Every flagged clip lists the property to change and where.
- [ ] A re-run after fixes shows zero flags or states why a flag is intended.
- [ ] A layered play test (move plus action) was screenshotted or marked untested.
- [ ] No asset or instance was changed by this skill.

## Pitfalls
Setting everything to Action4 "to be safe": then nothing can interrupt anything. Fixing priority on the track at runtime but not in the asset (it returns on the next load). Looped clips whose first and last poses differ (visible pop). Animation ids the rig owner does not own fail to load: that is not a priority problem. NPC and player animators are separate; check the one in use.

## Related
`rig-checker`, `animation-import-guide`, `accessory-fitting-guide`, `tween-helper-builder`, `npc-spawner-builder`.
