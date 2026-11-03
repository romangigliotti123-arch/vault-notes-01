---
id: "roblox-performance-pass"
type: skill
category: "roblox"
source: "own"
license: "first-party"
repo_path: "skills/roblox/roblox-performance-pass/SKILL.md"
description: "Find and fix performance problems in a Roblox experience: server and client frame time, memory, part count, streaming, script hot spots, network traffic. Use when a Roblox game lags, crashes on phones or has high memory."
orig_name: "roblox-performance-pass"
tags: [lib/skill, cat/roblox, src/own]
---

# roblox-performance-pass

> Find and fix performance problems in a Roblox experience: server and client frame time, memory, part count, streaming, script hot spots, network traffic. Use when a Roblox game lags, crashes on phones or has high memory.

Type: skill | Category: [[categories/cat-roblox|roblox]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/roblox/roblox-performance-pass/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# Roblox performance pass

Measure first, change one thing, measure again. Test on a low-end phone profile, not only the dev PC.

## Measure
1. Developer Console (F9 in game): Memory (PlaceMemory, Instances, Scripts, Sounds, Textures), Network, Script activity and Server Jobs. Studio: MicroProfiler (Ctrl+F6) for frame breakdown, Script Profiler, Performance stats.
2. Creator Dashboard Performance tab: crash rate, memory and frame rate by device.
3. Record baseline numbers: client FPS on a mobile emulation profile, server heartbeat, memory MB after 10 minutes, part count.

## Common fixes, in order of payoff
1. Streaming: enable `StreamingEnabled` with sensible radii; keep critical gameplay objects near the player; use `ModelStreamingMode` Persistent only where needed.
2. Part and mesh budget: merge static parts into MeshParts or unions, reduce meshes' triangle counts, set `CastShadow = false` and `CanTouch/CanQuery/CanCollide = false` on decoration, `Anchored = true` for static parts, avoid thousands of unique small parts.
3. Textures and sounds: right-size textures, avoid 4K textures on small objects, stream long audio, cap simultaneous sounds.
4. Scripts: remove per-frame loops over many instances, use events instead of polling, tag-based systems via `CollectionService`, batch updates, avoid creating/destroying instances every frame (pool them), avoid `GetDescendants()` in loops.
5. Network: send less often, batch remotes, send ids and small numbers not whole tables, use attributes sparingly for replicated state, unreliable remotes (UnreliableRemoteEvent) for cosmetic high-frequency data.
6. Physics: fewer unanchored parts, simplify collision geometry (`CollisionFidelity`), clean up leftover debris with `Debris` or pooling, set network ownership deliberately.
7. UI: avoid hundreds of live GuiObjects updating each frame, use `UIListLayout` sparingly in huge lists (paginate or virtualise), disable invisible `ScreenGui`.

## Report
Before/after table (metric, device profile, value), what changed, what remains, risk of each change. Do not claim improvement without a measured before and after.
