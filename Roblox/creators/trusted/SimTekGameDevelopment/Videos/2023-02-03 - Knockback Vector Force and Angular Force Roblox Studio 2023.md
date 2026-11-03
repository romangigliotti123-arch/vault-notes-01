---
title: "Knockback: Vector Force and Angular Force | Roblox Studio 2023"
url: https://youtu.be/-sQHMwuVAu4
creator: SimTek Game Development
official: false
advice_density: medium
date: 2023-02-03
views: 40905
transcript: auto-captions
confidence: high
tags: [roblox, simtekgamedevelopment, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Knockback: Vector Force and Angular Force | Roblox Studio 2023

[Watch](https://youtu.be/-sQHMwuVAu4) | SimTekGameDevelopment | 40,905 views | 2023-02-03

## Summary
Tutorial on adding knockback to a Roblox pistol using the modern VectorForce and AngularVelocity constraints instead of legacy BodyMovers. Covers attachments, direction math, platform stand, debris cleanup, and testing on R6 and R15 rigs.

## Tips
- [0:00](https://youtu.be/-sQHMwuVAu4?t=0) **[[genre-mechanics]]** Use VectorForce and AngularVelocity constraints for knockback rather than legacy BodyMovers; both need an Attachment on the target's HumanoidRootPart.
- [2:45](https://youtu.be/-sQHMwuVAu4?t=165) **[[scripting-and-performance]]** Guard knockback with nil and existence checks on both characters' HumanoidRootParts before applying forces to avoid errors when players are respawning.
- [3:26](https://youtu.be/-sQHMwuVAu4?t=206) **[[scripting-and-performance]]** Normalize the direction vector with .Unit and add a small upward component so knocked targets lift off the ground.
- [5:28](https://youtu.be/-sQHMwuVAu4?t=328) **[[scripting-and-performance]]** Set VectorForce RelativeTo to World or Attachment and tune force magnitude (example 10000) by testing values; the result varies a lot.
- [6:49](https://youtu.be/-sQHMwuVAu4?t=409) **[[scripting-and-performance]]** Set Humanoid.PlatformStand to true during knockback so the character stays in a free-falling state, then reset it after about 2 seconds.
- [8:10](https://youtu.be/-sQHMwuVAu4?t=490) **[[scripting-and-performance]]** Unanchor test rigs before testing knockback, since anchored HumanoidRootParts won't move.
- [10:15](https://youtu.be/-sQHMwuVAu4?t=615) **[[scripting-and-performance]]** Set AngularVelocity MaxTorque to math.huge so the spin is applied reliably.
- [11:37](https://youtu.be/-sQHMwuVAu4?t=697) **[[scripting-and-performance]]** Clean up temporary constraints and attachments with Debris:AddItem after about 0.2 seconds so they don't accumulate.

## Numbers
- [5:28](https://youtu.be/-sQHMwuVAu4?t=328) VectorForce magnitude: **10000 (example, tune as needed)** (Multiplier applied to normalized direction for knockback force)
- [10:15](https://youtu.be/-sQHMwuVAu4?t=615) AngularVelocity magnitude: **random between -30 and 30 per axis** (Scalar multiplier on vector for spin)
- [11:37](https://youtu.be/-sQHMwuVAu4?t=697) Constraint lifetime: **0.2 seconds** (Debris time-to-live for force, angular velocity and attachment)
- [11:37](https://youtu.be/-sQHMwuVAu4?t=697) PlatformStand reset delay: **2 seconds** (Time before re-enabling movement after knockback)

## Tools
Roblox Studio, VectorForce, AngularVelocity, Attachment, Debris service, Humanoid.PlatformStand

## He points to
- Roblox PlatformStand documentation (linked in video description)
- Simple pistol gun model from Toolbox (linked in description)

## Topics
[[genre-mechanics]] [[scripting-and-performance]]

Back to [[SimTekGameDevelopment - How to make successful Roblox games]]
