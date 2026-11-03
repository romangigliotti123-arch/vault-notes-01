---
name: sound-placement-planner
description: "Plan music, ambience and sound effects for a map: a 2D ambient bed per zone, 3D spot sounds and volumetric emitters sized by area, a bus and priority mix with music at about 0.2, feedback sounds for every interaction, and an audit of the Sounds already in the place. Use when a map is silent, noisy, or sounds play map-wide."
category: build
tags: sound, audio, music, ambience, emitter, volumetric, mix, sfx, rolloff, bus, soundgroup
kb: Roblox/roblox-kb/sound-and-music.md, Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/building-art-and-assets.md
related: particle-effect-planner, lighting-preset-picker, art-bible-writer, settings-menu-builder, asset-license-checker
---

# sound-placement-planner

Sound is placed in layers: a constant 2D bed so the game never feels silent, 3D spot sounds that pull attention around, volumetric emitters for areas like rain and oceans, and a mix where UI and weapons sit above music. This plans the layers per zone with a tested module and audits the current sounds against the vault's rules.

## When to use
A map feels dead, sounds are heard across the map, music buries effects, or before a content update. Not for: composing or licensing music (`asset-license-checker`), or the settings sliders UI (`settings-menu-builder`).

## Inputs (max 2)
1. Zones: name, kind (`outdoor`, `indoor`, `event`, `hub`) and area in studs squared. 2. Mix buses wanted (default: music, sfx, ui, weapons, dialogue, ambience).

## Procedure
1. List zones from the graybox or map. Decide each zone's bed first (a looping 2D ambience; indoor zones get a quiet room tone with reverb).
2. Run `scripts/SoundPlan.luau` under Lune: `SoundPlan.plan(zones, cap)` returns, per zone, the bed, how many spot ambiences (one per 1600 studs squared, at least one, at most 12) and whether the area is big enough (6400 studs squared) for a volumetric emitter instead; the total spots; issues when it exceeds the concurrent 3D emitter guide (24, this skill's assumption). These densities are defaults to tune by ear.
3. Choose objects: new work uses Audio objects (AudioPlayer, AudioEmitter, AudioListener wiring) per the docs; legacy Sound and SoundGroup still work. Positional sounds attach to a part or attachment; global sounds (music, UI) are non-positional. Set falloff deliberately: RollOffMin for full volume, RollOffMax for silence; the default of 10000 studs is audible map-wide.
4. Mix: check with `SoundPlan.checkMix({ {name, volume, priority} })`: music volume near 0.2 (the official example), UI, weapons and dialogue with higher priority than music so it ducks. Give every player-facing interaction a feedback sound. Pair every important sound cue with a visual cue (accessibility) and offer separate volume sliders per bus.
5. Loops: make them seamless (match at a zero crossing); layer loops of different lengths to hide repetition.
6. Audit the place with `scripts/sound_audit.luau` (read-only): legacy vs Audio objects, empty ids, sounds parked in SoundService (create at runtime instead: one game cut memory from about 500 MB to 58 MB), looped 3D sounds with the default roll-off, music too loud, sounds with no group.
7. Test in Play with headphones and on a phone speaker (`start_stop_play`, `get_console_output` for load errors).

## Studio MCP path
`list_roblox_studios` -> `execute_luau` (Edit) with `scripts/sound_audit.luau` -> offline `SoundPlan` run -> owner imports licensed audio -> `start_stop_play` -> `get_console_output`.

## Fallback
Planning is offline. The audit is command-bar Luau. What it sounds like and the real mix are `untested` without listening.

## Evidence
`Roblox/roblox-kb/sound-and-music.md` (prefer Audio objects; 3D for place-bound sounds, 2D for global; constant ambient bed; background music Volume about 0.2; seamless loops at zero crossing; layered loops of different lengths; volumetric emitters for area sounds; RollOffMin/Max falloff; duck low-priority audio with a compressor; separate volume controls), `Roblox/roblox-kb/optimization-and-streaming.md` (store sound ids in scripts and create at runtime, not in SoundService; release unused audio references), `Roblox/roblox-kb/building-art-and-assets.md` (pair every sound with a visual cue). Spot density and caps are this skill's own.

## Output
```
SOUND PLAN: 6 zones | spots 14 (cap 24) | volumetric: Forest, Ocean
Mix: music 0.2 (prio 1) < ui, weapons, dialogue | issues: none
AUDIT: Sounds 61 (3D 22) | [6] looped 3D with default roll-off | [3] stored in SoundService
```

## Acceptance checks
- [ ] Each zone has a bed, a spot count and a volumetric decision from the module.
- [ ] The mix check passed or its issues are explained.
- [ ] The audit ran and its counts are quoted.
- [ ] Every interaction has a feedback sound and, where it matters, a visual cue.
- [ ] Only licensed or owned audio ids are used (ids are never invented).

## Pitfalls
Silence in idle moments. Looped sounds at default roll-off. Music at full volume. Hundreds of always-loaded sounds. One long loop instead of layered loops. Positional audio for UI. Audio ids from the Creator Store without a licence check.

## Related
`particle-effect-planner`, `lighting-preset-picker`, `art-bible-writer`, `settings-menu-builder`, `asset-license-checker`.
