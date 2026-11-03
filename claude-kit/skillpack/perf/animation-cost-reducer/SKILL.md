---
name: animation-cost-reducer
description: "Cut the cost of animated rigs in crowds: count Animators, playing tracks and idle rigs by distance, enable client animator throttling, stop idle and distant animators, use non-humanoid rigs for crowds, and verify in the MicroProfiler. Use when NPC crowds, pets or many players make animation or physics bars long."
category: perf
tags: animation, animator, humanoid, crowd, npc, throttling, tracks, rig, ClientAnimatorThrottling, microprofiler
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/3d-modeling-rigging-and-animation.md, Roblox/roblox-kb/scripting-and-performance.md
related: npc-cost-reducer, game-optimizer, script-profiler, physics-load-reducer, animation-priority-checker, lag-hunter
---

# animation-cost-reducer

Every animated rig costs animation evaluation, bone/Motor6D transforms and replication. A crowd of fifty humanoids can dominate a frame even when each looks idle. This skill measures who is animating, throttles what players cannot see, and downgrades rigs that do not need humanoid features.

## When to use
Many NPCs, pets, or players in one view; the MicroProfiler shows animation or humanoid tasks; server CPU grows with NPC count. Not for: when and how often NPC AI thinks (`npc-cost-reducer`), animation priorities (`animation-priority-checker`), or physics of ragdolls (`physics-load-reducer`).

## Inputs (max 2)
1. The crowd scenario (count, area, server or client cost). 2. Which rigs must stay full quality (hero characters, bosses).

## Procedure
1. Census in Play on the Server datamodel and on a client: `scripts/anim_census.luau`. It reports Animators, Humanoids, playing tracks total, animators with tracks versus idle animators, ClientAnimatorThrottling, and rig counts by distance from the first player (100/250/500 studs). Capture a MicroProfiler frame in the same scene (Ctrl+Alt+F6, pause Ctrl+P) and note animation/humanoid task time. Stop if no rigs exist.
2. Quick wins, one at a time:
   a. Enable `Workspace.ClientAnimatorThrottling` so distant animators update less (creator-recommended).
   b. Anchor or disable the Animator of idle NPCs; a studio reported server CPU roughly halved by anchoring/disabling animators on idle NPCs (Dead Rails, creator report). On static NPC humanoids disable Evaluate State Machine.
   c. Disable unused humanoid states (climbing, swimming) and enable them when needed. A creator test found no measurable difference with dozens of humanoids, so measure; for crowds prefer non-humanoid rigs (AnimationController + Animator) over Humanoids.
   d. Stop tracks nobody can see: play only while within the near ring (`npc-cost-reducer` `UpdateRate.hzFor`), park far NPCs completely.
   e. Run visual-only movement and animation on the client; replicate state through attributes (one 200-NPC demo kept network near zero this way).
   f. Drive many replicated motions by animation playback instead of server tweens (one test: 60 tweened doors about 60 ms CPU and 1,800 KB/s received versus about 16 ms and about 0 KB/s with animation playback; indie).
3. Memory side: destroy references to unused AnimationTracks and Animations so they unload; animation assets are a common leak (scripts keep them alive after the model is destroyed). Check with Scene Analysis (audio/animation memory).
4. Re-run the census and the profiler capture in the same scene. Keep each change only if the animation tasks or frame time dropped and nothing popped visibly.
5. Record the settings (throttling on, ring distances, rig types) as the crowd budget.

## Studio MCP path
`list_roblox_studios` -> `start_stop_play` -> `execute_luau` (Server) `scripts/anim_census.luau` -> `execute_luau` (Edit) property edits (Workspace.ClientAnimatorThrottling, Animator parents; log old values) -> `screen_capture` a distant crowd to check pops -> `get_console_output`. MicroProfiler is manual.

## Fallback
Command bar in a Play session for the census. Without a profiler, report counts and label any time gain `untested`.

## Evidence
`Roblox/roblox-kb/optimization-and-streaming.md`: disable unused humanoid states and animator work; enable ClientAnimatorThrottling; animate NPCs only near the focus (test 100, final 500 studs); animation playback beats server tweens (60 doors test); destroy unused animation references. `Roblox/roblox-kb/scripting-and-performance.md`: anchor/disable animators on idle NPCs (Dead Rails halved server CPU; creator report). Official: `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization scene-analysis.md` (animation assets are a common production memory leak), `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization microprofiler.md`. Vendor gains are indie reports: your measurement decides.

## Output
```
ANIMATION CROWD REPORT <scene> <date>
Animators 420 (tracks playing 380, idle 40) | humanoids 210 | <=100 st: 30, <=250: 70, <=500: 110, beyond: 210
Animation task 6.4 ms -> 2.2 ms (MicroProfiler) after: throttling on, 180 far rigs parked, idle animators disabled
Visual check: no pops within 100 studs
```

## Acceptance checks
- [ ] Census saved before and after; the rig counts by ring are stated.
- [ ] Profiler animation time before/after quoted or labelled `untested`.
- [ ] Hero characters unchanged; near-ring rigs animate at full rate.
- [ ] Animation references destroyed on despawn (no growth in a 5-minute soak).
- [ ] Executed check: `anim_census.luau` passes the pack's luau-check run (stylua, selene, luau-lsp).

## Pitfalls
Disabling the Animator on rigs that then freeze mid-pose when they re-enter view. Believing humanoid-state toggles always help. Throttling hero characters. Forgetting to destroy animation tracks. Replicating cosmetic animation from the server.

## Related
`npc-cost-reducer`, `game-optimizer`, `script-profiler`, `physics-load-reducer`, `animation-priority-checker`.
