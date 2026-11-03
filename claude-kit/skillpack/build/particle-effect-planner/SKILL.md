---
name: particle-effect-planner
description: "Design cheap, readable particle effects with a budget per effect: live-particle maths (rate x lifetime), the 400/s desktop and 100/s mobile rate caps, lifetime clamp, texture and glow rules, one-shot bursts, and an audit of every ParticleEmitter in the place with an opt-in rate cap. Use when planning VFX or when effects hurt mobile frame rate."
category: build
tags: particles, vfx, particleemitter, rate, lifetime, budget, mobile, beam, trail, overdraw, effects
kb: Roblox/roblox-kb/vfx-and-particles.md, Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/building-art-and-assets.md
related: lighting-preset-picker, sound-placement-planner, game-optimizer, lag-hunter, tween-helper-builder
---

# particle-effect-planner

An effect is a budget line before it is art: how many particles are alive at once. The vault gives the caps (rate per emitter, lifetime) and the trap (high emission, long lifetime, low speed = overdraw). This costs effects on paper with a tested module, then audits what the place already has.

## When to use
Planning explosions, auras, ambient dust, hit sparks; frame drops near effects; mobile complaints. Not for: sound for the same effect (`sound-placement-planner`), tween-driven motion (`tween-helper-builder`).

## Inputs (max 2)
1. The effects: name, loop or one-shot, rough rate, lifetime, how many can overlap. 2. Device tier: `mobile` (default) or `desktop`.

## Procedure
1. For each effect decide the look first (mood, size, colour); keep Rate low and get impact from Size, Speed and Lighting rather than count.
2. Cost it with `scripts/ParticleBudget.luau` under Lune: `live` (rate x min(lifetime, 20) x copies for loops; burst x overlap for one-shots), `assess(effect, tier)` for issues (rate above the tier cap of 400 or 100 per second, lifetime above the 20 s clamp, one effect over a quarter of the scene budget), `plan(effects, tier)` for the total, the budget (this skill's default of 2000 desktop and 500 mobile live particles: assumptions, tune from a profile) and the heaviest effect.
3. Prefer one-shot bursts: `emitter:Emit(count)` for hits and pops instead of a high Rate; fade out with a Transparency NumberSequence ending at 1 instead of popping off; randomise Lifetime and Rotation ranges.
4. Texture and glow: grayscale PNG with transparent blurred edges, tint with Color; glowing particles use LightEmission 1 and LightInfluence 0 so they stay bright in any lighting.
5. Sphere and Cylinder shapes need a BasePart parent, not an Attachment.
6. Audit what exists with `scripts/particle_audit.luau`: counts, estimated live particles, and flags (rate over cap, lifetime over 20, one-emitter live above 250, no texture, glow with LightInfluence, slow long-lived continuous emitters). `APPLY_CAP_RATE = true` lowers Rate on enabled over-cap emitters to the cap in one undo step; it changes the look, so review first.
7. Test every effect at the lowest and the highest Editor Quality Level (vault) and on a phone; compare with the plan.

## Studio MCP path
`list_roblox_studios` -> `execute_luau` (Edit) with `scripts/particle_audit.luau` -> offline `ParticleBudget` run -> optionally cap rates -> `start_stop_play` -> `screen_capture` of the effect at both quality levels -> `get_console_output`.

## Fallback
Command bar for the audit; the budget maths is offline. Visual quality and real frame cost are `untested` without a device.

## Evidence
`Roblox/roblox-kb/vfx-and-particles.md` (max Rate 400/s desktop and 100/s mobile, default 20/s; Lifetime above 20 s silently clamped; grayscale textures tinted by Color; LightEmission 1 and LightInfluence 0 for glow; fade with Transparency sequences; budget VFX against frame cost and test at both quality extremes; Sphere/Cylinder shapes need a BasePart), `Roblox/roblox-kb/optimization-and-streaming.md` (test emission rate, lifetime and speed; avoid high emission with long lifetime and low speed). The live-particle budgets are this skill's assumptions.

## Output
```
PARTICLE PLAN (mobile): hit_spark 120 live | campfire 40 | blizzard 500 (heaviest)
total 660 / 500 -> OVER: shorten blizzard lifetime, raise size and speed
AUDIT: emitters=42 enabled=30 est-live=1,900 | [4] Rate above 100/s | capped (optional): 4
```

## Acceptance checks
- [ ] Each effect has a live-particle number from the module.
- [ ] The plan total is under the tier budget or the overage is justified.
- [ ] The audit ran and its counts are quoted.
- [ ] Both quality extremes were tested, or marked untested.
- [ ] Any rate cap was reviewed visually first.

## Pitfalls
Raising Rate for impact. Long-lived slow smoke on phones. Textures with opaque backgrounds. Effects parented to parts that stream out. Judging only on a desktop GPU. Highlights, beams and trails have their own costs the live-particle count does not include.

## Related
`lighting-preset-picker`, `sound-placement-planner`, `game-optimizer`, `lag-hunter`, `tween-helper-builder`.
