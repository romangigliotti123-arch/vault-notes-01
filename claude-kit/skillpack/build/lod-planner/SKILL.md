---
name: lod-planner
description: "Plan instance streaming and level of detail for a detail-heavy place: which models are Persistent, Atomic or default, which are SLIM candidates, which are too big or too part-heavy and need splitting, with an audit of the current streaming settings and an opt-in write of ModelStreamingMode only. Use when join time, memory or pop-in is the problem."
category: build
tags: streaming, lod, slim, modelstreamingmode, persistent, atomic, instance streaming, culling, memory, join time
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/building-and-level-design.md, Roblox/roblox-kb/building-art-and-assets.md
related: workspace-organizer, part-to-mesh-planner, prop-set-planner, game-optimizer, lag-hunter
---

# lod-planner

Instance streaming sends only what is near the player; SLIM gives distant static models cheap stand-ins. The vault calls streaming the highest-impact way to cut client memory and join time, and also warns what breaks: scripts that assume every part exists, and overuse of Persistent. This plans the per-model decisions and checks the current settings.

## When to use
Large or detailed maps, mobile crashes from memory, long joins, pop-in, or before enabling streaming. Not for: general frame-time hunting (`lag-hunter`), or part merging (`part-to-mesh-planner`).

## Inputs (max 2)
1. Scope (Workspace default). 2. Which models are essential for every client and which are dynamic (moved, animated, edited at runtime). Mark them with the attribute or tag `Essential` / `Dynamic`; scripted models are found automatically.

## Procedure
1. Connect (below). Streaming development advice: turn streaming on early and write code with it on.
2. Run `scripts/lod_audit.luau` (read-only). It prints Workspace streaming settings (enabled, min and target radius, integrity mode, model streaming behaviour, predictive streaming), then each top-level model: part count, current ModelStreamingMode and LevelOfDetail, and notes.
3. Decisions come from `scripts/LodPlan.luau` (Lune-tested, inlined in the audit): essential -> Persistent (never streams out; use sparingly, warn above 10 percent of models); scripted -> Atomic (parts load together so scripts wait only on the model); everything else default; static and not essential -> SLIM candidate; dynamic models keep default level of detail; extent above about 64 studs or more than 2000 parts -> split the model.
4. Workspace settings (vault defaults): Streaming on; StreamingMinRadius 64 and StreamingTargetRadius 1024 left at defaults; StreamingIntegrityMode PauseOutsideLoadedArea; ModelStreamingBehavior Improved; PredictiveStreamingMode enabled. Change them in the Workspace properties by hand (live-check names in Creator Docs).
5. Optional write: `APPLY_MODES = true` sets ONLY ModelStreamingMode (Persistent or Atomic) on models still at Default, one undo step. Level of detail is never written by the script: the property's enum value name varies, so set SLIM in the Properties panel on the listed models after a live-check.
6. Fix client code for streaming: use `Instance:WaitForChild` with timeouts, `StreamingEnabled`-safe patterns, and `handle:Get()`/`handle:Wait(timeout)` where targets may stream in; never reparent streamed instances locally.
7. Test: low-end device profile, join time, pop-in on fast travel, and `get_console_output` for missing-child errors. Compare instance counts on the client (about 1 s per 10,000 instances).

## Studio MCP path
`list_roblox_studios` -> `execute_luau` (Edit) with `scripts/lod_audit.luau` -> tag/attribute essentials with `execute_luau` -> apply modes -> `start_stop_play` -> `get_console_output` -> `screen_capture` for pop-in.

## Fallback
Command bar for the audit. The planning module is offline. Real join time, memory and pop-in are `untested` without a device.

## Evidence
`Roblox/roblox-kb/optimization-and-streaming.md` (StreamingEnabled is the highest-impact way to cut client memory; Persistent for always-needed content, Atomic when scripts need all children; SLIM for static models only; Improved behaviour; defaults 64 and 1024; PauseOutsideLoadedArea; predictive streaming; write streaming-safe code; flatten nested persistent/atomic), `Roblox/roblox-kb/building-and-level-design.md` (SLIM needs streaming on; keep model extent small, about 64 studs per the docs: live-check). The 10 percent Persistent threshold is this skill's own. Late-2026 adaptive streaming features are announced only: do not design around them.

## Output
```
LOD / STREAMING AUDIT: StreamingEnabled=true | models=84 | SLIM candidates 61 | Persistent wanted 6
 Castle: parts=3100 mode=Default LOD=Automatic extent 310 -> split; 
Applied (optional): ModelStreamingMode on 9 models (one undo step)   Untested: join time on device
```

## Acceptance checks
- [ ] The audit ran; settings and counts are quoted.
- [ ] Persistent is under about 10 percent of models, each with a reason.
- [ ] Client scripts were checked for streaming safety (grep for direct paths) or marked untested.
- [ ] LevelOfDetail changes were made by hand after a live-check.
- [ ] A Play/device test result is recorded.

## Pitfalls
Persistent everywhere. A Persistent model nested in an Atomic one (the parent behaves Persistent). SLIM on models scripts modify. Hand-rolled streaming on top of the engine's. Client code that indexes a part directly. Large models that can never stream partially. Turning streaming off at the end after building without it.

## Related
`workspace-organizer`, `part-to-mesh-planner`, `prop-set-planner`, `game-optimizer`, `lag-hunter`.
