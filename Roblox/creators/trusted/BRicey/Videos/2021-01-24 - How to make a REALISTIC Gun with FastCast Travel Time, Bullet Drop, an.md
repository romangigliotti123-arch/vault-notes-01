---
title: "How to make a REALISTIC Gun with FastCast: Travel Time, Bullet Drop, and More (Ep.1) - Roblox Studio"
url: https://youtu.be/mJZWY3G7wa4
creator: B Ricey
official: false
advice_density: medium
date: 2021-01-24
views: 114586
transcript: manual-subs
confidence: high
tags: [roblox, bricey, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to make a REALISTIC Gun with FastCast: Travel Time, Bullet Drop, and More (Ep.1) - Roblox Studio

[Watch](https://youtu.be/mJZWY3G7wa4) | BRicey | 114,586 views | 2021-01-24

## Summary
Tutorial on building a realistic gun in Roblox Studio using the FastCast: Redux module. Covers tool setup with a Handle and FirePoint attachment, client-server communication via RemoteEvent, creating a caster with raycast-based bullets, adding acceleration for bullet drop, filtering with RaycastParams, cosmetic bullet parts, and applying damage on hit.

## Tips
- [1:37](https://youtu.be/mJZWY3G7wa4?t=97) **[[scripting-and-performance]]** Name the tool's main part exactly 'Handle' (capital H); tools will not recognize any other name.
- [3:12](https://youtu.be/mJZWY3G7wa4?t=192) **[[scripting-and-performance]]** Use raycasting (FastCast) instead of velocity-based projectiles; velocity is laggier and less accurate with .Touched.
- [3:53](https://youtu.be/mJZWY3G7wa4?t=233) **[[client-server-and-remotes]]** Split gun logic into a LocalScript for client input and a Script for server handling, linked by a RemoteEvent.
- [4:36](https://youtu.be/mJZWY3G7wa4?t=276) **[[client-server-and-remotes]]** On the client, use WaitForChild for tool children since tools take time to load; the server can reference them directly.
- [5:22](https://youtu.be/mJZWY3G7wa4?t=322) **[[ui-ux-design]]** Use mouse.Hit.Position from the built-in Roblox mouse for aiming; a custom mouse module is optional.
- [9:12](https://youtu.be/mJZWY3G7wa4?t=552) **[[scripting-and-performance]]** Set the cast origin to the attachment's world position (not .Position), and use a unit vector for direction.
- [10:45](https://youtu.be/mJZWY3G7wa4?t=645) **[[physics-pathfinding-and-npc-ai]]** Set CastBehavior.Acceleration to Vector3 with negative Y to produce gravity-based bullet drop.
- [12:09](https://youtu.be/mJZWY3G7wa4?t=729) **[[scripting-and-performance]]** Filter the raycast with RaycastParams ignoring the shooter's character and the bullets folder; set IgnoreWater true for guns.
- [12:53](https://youtu.be/mJZWY3G7wa4?t=773) **[[scripting-and-performance]]** Rebuild the filter list on Equipped so the tool's parent character is ignored; set AutoIgnoreContainer to false to avoid redundancy.
- [14:29](https://youtu.be/mJZWY3G7wa4?t=869) **[[scripting-and-performance]]** Create the bullets folder in code if missing so the gun stays standalone and portable across projects.
- [16:58](https://youtu.be/mJZWY3G7wa4?t=1018) **[[building-art-and-assets]]** Avoid models for cosmetic bullets in FastCast; they are too laggy. Use simple in-code parts such as a small metal ball.
- [19:48](https://youtu.be/mJZWY3G7wa4?t=1188) **[[scripting-and-performance]]** Offset the bullet by its segment length so it stops behind walls instead of phasing through them.
- [21:57](https://youtu.be/mJZWY3G7wa4?t=1317) **[[scripting-and-performance]]** Use a starting velocity around 1000 for realistic gun speed with visible travel time and drop.
- [24:01](https://youtu.be/mJZWY3G7wa4?t=1441) **[[combat-and-gameplay-systems]]** Check that hit.Parent is a model with a Humanoid before applying damage; this example deals 50 damage per hit.
- [24:01](https://youtu.be/mJZWY3G7wa4?t=1441) **[[scripting-and-performance]]** Clean up bullets with Debris:AddItem so spent bullets do not persist in the world.
- [24:47](https://youtu.be/mJZWY3G7wa4?t=1487) **[[combat-and-gameplay-systems]]** Hook caster.RayHit to apply damage; the event fires whenever the ray collides and stops updating.

## Numbers
- [21:57](https://youtu.be/mJZWY3G7wa4?t=1317) Starting bullet velocity: **1000** (FastCast velocity for gun-realistic speed in demo)
- [24:01](https://youtu.be/mJZWY3G7wa4?t=1441) Damage per hit: **50** (Demo damage applied to humanoid on hit)
- [24:01](https://youtu.be/mJZWY3G7wa4?t=1441) Bullet cleanup delay: **2 seconds** (Debris:AddItem lifetime for spent bullets in demo)

## Tools
FastCast: Redux (EtiTheSpirit), Roblox Studio, RaycastParams, RemoteEvent, Debris service, Built-in Roblox mouse, Toolbox

## He points to
- FastCast: Redux module (Toolbox, EtiTheSpirit)
- Creator's custom mouse module (linked in description)
- Creator's raycasting video
- Creator's upcoming PartCache video

## Topics
[[building-art-and-assets]] [[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[BRicey - How to make successful Roblox games]]
