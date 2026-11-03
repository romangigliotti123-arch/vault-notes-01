---
title: "Docs: tutorials / use-case-tutorials / scripting / intermediate-scripting / hit-detection-with-lasers"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/hit-detection-with-lasers.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / scripting / intermediate-scripting / hit-detection-with-lasers

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/hit-detection-with-lasers.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs tutorial on building a laser blaster tool: raycasting from the mouse through the camera to find the aim point, firing a second raycast from the tool handle with the character filtered out, rendering a neon part beam via a ModuleScript, enforcing fire rate, and server-side validation of damage requests (distance and wall checks).

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/hit-detection-with-lasers) **[[scripting-and-performance]]** Use RaycastParams.FilterDescendantsInstances to exclude the firing player's character so the shot does not hit yourself.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/hit-detection-with-lasers) **[[scripting-and-performance]]** Normalise direction vectors with .Unit before multiplying by a max distance so the ray length is predictable.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/hit-detection-with-lasers) **[[anti-exploit-and-security]]** Validate remote damage requests on the server: check hit distance to the target HumanoidRootPart and raycast for walls before applying damage.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/hit-detection-with-lasers) **[[anti-exploit-and-security]]** Keep damage remotes secure as an ongoing effort; determined exploiters often find ways around validation.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/hit-detection-with-lasers) **[[combat-and-gameplay-systems]]** Enforce weapon fire rate with a timestamp check (tick() minus last shot time against FIRE_RATE) to limit damage per second.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/hit-detection-with-lasers) **[[vfx-and-particles]]** Render laser beams as anchored, non-collidable neon parts sized to the distance, and remove them with Debris after about 0.15 s.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/hit-detection-with-lasers) **[[client-server-and-remotes]]** Fire laser visuals to all clients from the server, skipping the shooter's own client to avoid a duplicate beam.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/hit-detection-with-lasers) **[[testing-debugging-and-qa]]** Test multiplayer combat with a local server and multiple clients (multi-client simulation) before relying on hit detection.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/hit-detection-with-lasers) **[[code-architecture-and-frameworks]]** Put reusable rendering code such as the laser beam in a ModuleScript so multiple scripts can require it.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/hit-detection-with-lasers) Max mouse raycast distance: **1000 studs** (MAX_MOUSE_DISTANCE in tutorial example)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/hit-detection-with-lasers) Max laser distance: **500 studs (example), 300 in later code** (MAX_LASER_DISTANCE; chosen per weapon)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/hit-detection-with-lasers) Fire rate delay: **0.3 seconds** (FIRE_RATE example minimum time between shots)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/hit-detection-with-lasers) Laser visible duration: **0.15 seconds** (SHOT_DURATION before Debris removes beam)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/hit-detection-with-lasers) Max character hit proximity: **10 studs** (Server check: hit position must be within 10 of target HumanoidRootPart)

## Tools
Roblox Studio, RaycastParams, Workspace:Raycast, Camera:ViewportPointToRay, UserInputService, Debris service, Toolbox / Inventory

## He points to
- Create player tools tutorial
- Detecting User Input tutorial
- multi-client simulation guide

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[combat-and-gameplay-systems]] [[scripting-and-performance]] [[testing-debugging-and-qa]] [[vfx-and-particles]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
