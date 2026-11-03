---
title: "How to Add Knockback to Walls for Players"
url: https://youtu.be/zimfV0QYV2w
creator: SimTek Game Development
official: false
advice_density: medium
date: 2024-11-02
views: 31636
transcript: auto-captions
confidence: high
tags: [roblox, simtekgamedevelopment, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to Add Knockback to Walls for Players

[Watch](https://youtu.be/zimfV0QYV2w) | SimTekGameDevelopment | 31,636 views | 2024-11-02

## Summary
Tutorial on adding knockback to players who run into solid walls at speed in Roblox. Covers a speed pellet that boosts WalkSpeed, a CollectionService "solid" tag, an invisible wall buffer part that triggers a touch check on HumanoidRootPart velocity, VectorForce and AngularVelocity constraints with Debris cleanup, and a client-side sound via RemoteEvent.

## Tips
- [0:00](https://youtu.be/zimfV0QYV2w?t=0) **[[core-loops-and-game-design]]** Gate a mechanic on player speed (linear velocity magnitude > ~20 studs/s) so knockback only triggers when running fast, not during normal movement.
- [13:22](https://youtu.be/zimfV0QYV2w?t=802) **[[common-mistakes]]** Touched events on HumanoidRootPart miss by a small gap; add an invisible, non-collidable buffer part slightly larger than the wall to fire the trigger earlier.
- [13:22](https://youtu.be/zimfV0QYV2w?t=802) **[[scripting-and-performance]]** Don't attach touch events to too many parts; use one buffer part per wall to limit how often the event fires.
- [5:55](https://youtu.be/zimfV0QYV2w?t=355) **[[scripting-and-performance]]** Use CollectionService tags (e.g. 'solid') to mark bounceable objects, so one script handles all tagged parts instead of per-object code.
- [16:46](https://youtu.be/zimfV0QYV2w?t=1006) **[[scripting-and-performance]]** Use a flag instance on the HumanoidRootPart plus Debris:AddItem to debounce repeated touch events so forces aren't applied multiple times.
- [18:50](https://youtu.be/zimfV0QYV2w?t=1130) **[[scripting-and-performance]]** Set VectorForce and AngularVelocity RelativeTo Attachment0 on the HumanoidRootPart so the push direction follows the character, not world orientation.
- [20:13](https://youtu.be/zimfV0QYV2w?t=1213) **[[scripting-and-performance]]** Destroy VectorForce and AngularVelocity constraints after ~0.1s with Debris so the forces are short impulses, not continuous.
- [22:52](https://youtu.be/zimfV0QYV2w?t=1372) **[[scripting-and-performance]]** Tune knockback by adjusting VectorForce Z magnitude (thrust) and AngularVelocity X (spin) values; the video used 10,000 force and 50 spin for stronger effect.
- [24:50](https://youtu.be/zimfV0QYV2w?t=1490) **[[client-server-and-remotes]]** Fire a RemoteEvent to the client to play sound effects, keeping audio playback out of server logic.
- [4:09](https://youtu.be/zimfV0QYV2w?t=249) **[[core-loops-and-game-design]]** Make a speed pellet using a neon, anchored, non-collidable part with CanTouch and CanQuery on, then destroy it on touch after setting WalkSpeed (e.g. 16 to 50).
- [11:30](https://youtu.be/zimfV0QYV2w?t=690) **[[scripting-and-performance]]** Connect CharacterAdded per player so touch detection is reapplied after respawns, not just on first join.

## Numbers
- [4:09](https://youtu.be/zimfV0QYV2w?t=249) WalkSpeed boost: **16 normal to 50 with speed pellet** (Speed pellet sets Humanoid.WalkSpeed to 50)
- [10:49](https://youtu.be/zimfV0QYV2w?t=649) Knockback speed threshold: **20 studs/s** (Linear velocity magnitude check before applying forces)
- [18:10](https://youtu.be/zimfV0QYV2w?t=1090) Force duration: **0.1 seconds** (VectorForce and AngularVelocity destroyed via Debris after 0.1s)
- [14:45](https://youtu.be/zimfV0QYV2w?t=885) Wall buffer size: **~3/10 stud enlargement** (Invisible buffer part slightly larger than wall, approximate)
- [26:54](https://youtu.be/zimfV0QYV2w?t=1614) Demo force values: **VectorForce 10000, AngularVelocity 50** (Stronger knockback values used at end of demo)

## Tools
Roblox Studio, Luau, CollectionService, Debris service, VectorForce, AngularVelocity, RemoteEvent, Toolbox audio

## He points to
- Roblox developer docs for VectorForce (linked in video description)
- Roblox developer docs for AngularVelocity (linked in video description)

## Topics
[[client-server-and-remotes]] [[common-mistakes]] [[core-loops-and-game-design]] [[scripting-and-performance]]

Back to [[SimTekGameDevelopment - How to make successful Roblox games]]
