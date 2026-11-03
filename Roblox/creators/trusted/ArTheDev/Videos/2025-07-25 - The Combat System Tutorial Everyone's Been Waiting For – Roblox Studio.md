---
title: "The Combat System Tutorial Everyone's Been Waiting For – Roblox Studio"
url: https://youtu.be/Pi8rQ9gGTKE
creator: ArTheDev
official: false
advice_density: high
date: 2025-07-25
views: 54889
transcript: auto-captions
confidence: high
tags: [roblox, arthedev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.5
---

> [!note] Trust: TRUSTED (credibility audit score 8.5): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# The Combat System Tutorial Everyone's Been Waiting For – Roblox Studio

[Watch](https://youtu.be/Pi8rQ9gGTKE) | ArTheDev | 54,889 views | 2025-07-25

## Summary
Tutorial building a modular Roblox combat system from scratch: server-side hitboxes via GetPartBoundsInBox, knockback, stun, blocking with perfect-block window, guard break, combo M1 chain, M2, evasive i-frames, and equip gating. Uses a skill-set folder structure, ContextActionService input binding, and a state manager plus animation handler.

## Tips
- [1:23](https://youtu.be/Pi8rQ9gGTKE?t=83) **[[development-process-and-speed]]** Organise combat code by skill set folders (e.g. base, sword) so swapping weapons only changes a combat-type StringValue on the player.
- [3:54](https://youtu.be/Pi8rQ9gGTKE?t=234) **[[code-architecture-and-frameworks]]** Keep a require cache table in the input handler so modules are required once, then reused on every input.
- [7:35](https://youtu.be/Pi8rQ9gGTKE?t=455) **[[scripting-and-performance]]** Bind R for block rather than Mouse Button 2 with ContextActionService, since MB2 interferes with camera movement.
- [12:58](https://youtu.be/Pi8rQ9gGTKE?t=778) **[[3d-modeling-rigging-and-animation]]** Set combat animations to Action priority and note the strike timestamp so the server hitbox fires at the right moment.
- [15:11](https://youtu.be/Pi8rQ9gGTKE?t=911) **[[combat-and-gameplay-systems]]** Do combat hit detection on the server and fire client effects with FireAllClients; the client only handles animation and input.
- [21:59](https://youtu.be/Pi8rQ9gGTKE?t=1319) **[[combat-and-gameplay-systems]]** Use a per-attack hit table to prevent multi-hits from one swing, and delete an opponent's hitbox if you hit them first.
- [26:02](https://youtu.be/Pi8rQ9gGTKE?t=1562) **[[combat-and-gameplay-systems]]** Use OverlapParams excluding the attacker's character and hitbox; set MaxParts high, since too low a limit can miss targets.
- [28:08](https://youtu.be/Pi8rQ9gGTKE?t=1688) **[[combat-and-gameplay-systems]]** Compute knockback direction from attacker to target position, not from camera look direction, and scale it up on the final combo hit.
- [29:32](https://youtu.be/Pi8rQ9gGTKE?t=1772) **[[player-psychology-and-game-feel]]** Make perfect block a short window (about 0.1s) after pressing block, applying a stun to the attacker on success and a normal hit otherwise.
- [30:15](https://youtu.be/Pi8rQ9gGTKE?t=1815) **[[combat-and-gameplay-systems]]** Use a dot-product angle threshold for hitbox facing so attacks only connect from the front; tune the threshold to widen or narrow the arc.
- [31:36](https://youtu.be/Pi8rQ9gGTKE?t=1896) **[[combat-and-gameplay-systems]]** Let heavy attacks (M2, or a late combo hit) set a guard-break flag that disables the target's block and deals damage through it.
- [36:18](https://youtu.be/Pi8rQ9gGTKE?t=2178) **[[scripting-and-performance]]** Gate every action with a shared can't-do-anything state so players cannot attack, block or evade while stunned, attacking or blocking.
- [42:38](https://youtu.be/Pi8rQ9gGTKE?t=2558) **[[combat-and-gameplay-systems]]** Implement evasive as a timed i-frame state with its own cooldown state, and cancel it early if the player attacks.
- [45:03](https://youtu.be/Pi8rQ9gGTKE?t=2703) **[[combat-and-gameplay-systems]]** Implement equip toggling as a server state and check it in both client and server attack handlers so unequipped attacks are rejected.
- [14:25](https://youtu.be/Pi8rQ9gGTKE?t=865) **[[client-server-and-remotes]]** Validate attacks on the server with a state check and reject if blocked or stunned, sending a decline response back to stop the client animation.
- [14:25](https://youtu.be/Pi8rQ9gGTKE?t=865) **[[anti-exploit-and-security]]** Never trust client hit results; the client only requests attacks and the server decides hits, damage and knockback.

## Numbers
- [0:00](https://youtu.be/Pi8rQ9gGTKE?t=0) Combo max: **3 hits in demo** (M1 combo chain length in the demo; changing it needs edits in server script)
- [15:11](https://youtu.be/Pi8rQ9gGTKE?t=911) Combo reset time: **1.5 s** (M1 combo resets if no hit within this window)
- [15:11](https://youtu.be/Pi8rQ9gGTKE?t=911) M1 cooldown: **0.5 s** (Client-side cooldown between M1 attacks)
- [29:32](https://youtu.be/Pi8rQ9gGTKE?t=1772) Perfect block window: **0.1 s** (Time after pressing block that counts as a perfect block)
- [24:00](https://youtu.be/Pi8rQ9gGTKE?t=1440) Attack can't-do-anything state: **0.5 s** (Lockout applied to all actions after an attack)
- [29:32](https://youtu.be/Pi8rQ9gGTKE?t=1772) Stun duration on hit: **6 s** (Stun applied to target on hit in server attack logic)
- [34:22](https://youtu.be/Pi8rQ9gGTKE?t=2062) Hit effect lifetime: **0.5 s** (Debris cleanup time for cloned effect attachments)
- [42:38](https://youtu.be/Pi8rQ9gGTKE?t=2558) Evasive i-frame duration: **1.5 s** (I-frame duration in the demo evasive)
- [43:19](https://youtu.be/Pi8rQ9gGTKE?t=2599) Evasive cooldown: **10 s** (Cooldown preventing evasive spam)

## Tools
Roblox Studio, ContextActionService, OverlapParams / GetPartBoundsInBox, Animation Editor, Toolbox, Custom state manager module (from prior videos), Custom animation handler module (from prior videos)

## He points to
- Creator's previous videos on state manager and animation handler (channel playlist linked in description)

## Topics
[[3d-modeling-rigging-and-animation]] [[anti-exploit-and-security]] [[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[combat-and-gameplay-systems]] [[development-process-and-speed]] [[player-psychology-and-game-feel]] [[scripting-and-performance]]

Back to [[ArTheDev - How to make successful Roblox games]]
