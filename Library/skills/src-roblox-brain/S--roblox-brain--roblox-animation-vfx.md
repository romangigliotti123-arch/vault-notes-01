---
id: "roblox-brain/roblox-animation-vfx"
type: skill
category: "src-roblox-brain"
source: "roblox-brain"
license: "MIT"
repo_path: "sources/roblox-brain/skills/gameplay/roblox-animation-vfx/SKILL.md"
description: "Use when adding, changing, or fixing Roblox animations, particles, beams, trails, tweens, camera shake, or other visual effects."
orig_name: "roblox-animation-vfx"
orig_when_to_use: "Also when an effect is invisible, too weak, laggy or doesn't clean up, an animation won't play or blend, and when reviewing game feel or hit feedback."
orig_last_reviewed: "2026-10-14"
tags: [lib/skill, cat/src-roblox-brain, src/roblox-brain]
---

# roblox-brain/roblox-animation-vfx

> Use when adding, changing, or fixing Roblox animations, particles, beams, trails, tweens, camera shake, or other visual effects.

Type: skill | Category: [[categories/cat-src-roblox-brain|src-roblox-brain]] | Source: [[sources/src-roblox-brain|roblox-brain]] | License: MIT
Repo file: `sources/roblox-brain/skills/gameplay/roblox-animation-vfx/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# roblox animation and vfx

## When to Load

Load when implementing character animation, particle or beam effects, tweens, camera feedback, or visual cleanup.

## Quick Reference

- Load tracks through an `Animator` on a `Humanoid` or `AnimationController`; set `AnimationTrack.Priority` deliberately.
- Use `GetMarkerReachedSignal()` for named gameplay or presentation cues, then disconnect or replace the listener when the track ends.
- Track lifecycle: `Ended` is post-fade cleanup; `Stopped` includes explicit stops. Same-priority tracks blend by weight; see full.md for control and loading guards.
- A burst `ParticleEmitter` usually has `Rate = 0` and uses `:Emit(count)` with a bounded lifetime; use pooling for frequent effects.
- Shape each effect as readable phases: warning, contact, brief peak, and fade. Give impact a clear silhouette before adding secondary particles, light, sound, or camera feedback.
- Use native particle flipbooks for animated textures; choose OneShot for a single impact or vary start frames for organic repetition. Custom mesh/image flipbooks may need their own playback code.
- Beams and trails need two attachments with a stable world-space relationship and a cleanup owner.
- Tween a bounded set of properties with `TweenService:Create`; cancel or destroy temporary effects when their owner ends, and use `Debris:AddItem` for simple lifetimes.
- In Server Authority projects, keep synchronized animation logic in `RunService:BindToSimulation()` (requires `Workspace.UseFixedSimulation` enabled in Studio), query current tracks instead of caching handles across rollback, and make predicted effects reversible.
- Profile particle counts, lights, post-processing, and per-frame camera work on the target device class.

**Need the details?** Load `references/full.md` for animation and effect recipes.
