---
title: "Full Beginner's Guide on scripting Anime/Fighting VFX(Visual Effects) [Part 1]"
url: https://devforum.roblox.com/t/full-beginners-guide-on-scripting-animefighting-vfxvisual-effects-part-1/1610853
creator: Roblox DevForum
official: false
advice_density: high
date: 2022-01-02
views: 586
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Full Beginner's Guide on scripting Anime/Fighting VFX(Visual Effects) [Part 1]

[Open](https://devforum.roblox.com/t/full-beginners-guide-on-scripting-animefighting-vfxvisual-effects-part-1/1610853) | Roblox DevForum | 586 views | 2022-01-02

## Summary
DevForum beginner guide (Part 1) for scripting anime/fighting-style VFX in Roblox: input detection with UserInputService, client-server RemoteEvent communication, server-sided debounce, hitbox damage detection with Touched, and spawning VFX server-side vs client-replicated via FireAllClients.

## Tips
- [page](https://devforum.roblox.com/t/full-beginners-guide-on-scripting-animefighting-vfxvisual-effects-part-1/1610853) **[[client-server-and-remotes]]** Spawn VFX on the client via FireAllClients from the server, not on the server; server-sided VFX increases server load and raises ping.
- [page](https://devforum.roblox.com/t/full-beginners-guide-on-scripting-animefighting-vfxvisual-effects-part-1/1610853) **[[anti-exploit-and-security]]** Use server-sided debounces (a table keyed by player name) instead of client-sided bool/time debounces, since exploiters can spam FireServer.
- [page](https://devforum.roblox.com/t/full-beginners-guide-on-scripting-animefighting-vfxvisual-effects-part-1/1610853) **[[combat-and-gameplay-systems]]** Prevent multi-hit damage with a per-player debounce value inside the humanoid, named with the player name plus attack key, removed after 1-4 seconds via Debris.
- [page](https://devforum.roblox.com/t/full-beginners-guide-on-scripting-animefighting-vfxvisual-effects-part-1/1610853) **[[combat-and-gameplay-systems]]** Filter hitbox Touched events with IsDescendantOf so the caster never damages themselves.
- [page](https://devforum.roblox.com/t/full-beginners-guide-on-scripting-animefighting-vfxvisual-effects-part-1/1610853) **[[client-server-and-remotes]]** Send the same CFrame and Position from server to all clients so client-spawned VFX stay in sync with the server hitbox.
- [page](https://devforum.roblox.com/t/full-beginners-guide-on-scripting-animefighting-vfxvisual-effects-part-1/1610853) **[[core-loops-and-game-design]]** Use UserInputService and check GameProcessedEvent so inputs typed in chat or textboxes are ignored.
- [page](https://devforum.roblox.com/t/full-beginners-guide-on-scripting-animefighting-vfxvisual-effects-part-1/1610853) **[[building-art-and-assets]]** Set hitboxes to Neon, Transparency 0.5, CanCollide false, CanTouch true, CastShadow false for visible, non-blocking debug hitboxes.
- [page](https://devforum.roblox.com/t/full-beginners-guide-on-scripting-animefighting-vfxvisual-effects-part-1/1610853) **[[development-process-and-speed]]** Keep client-replicated VFX assets in ReplicatedStorage and clone then delete them after use to avoid leaking instances.

## Numbers
- [page](https://devforum.roblox.com/t/full-beginners-guide-on-scripting-animefighting-vfxvisual-effects-part-1/1610853) Time to learn VFX scripting: **2 months before commissioned work at high prices** (Author's own experience scripting VFX)
- [page](https://devforum.roblox.com/t/full-beginners-guide-on-scripting-animefighting-vfxvisual-effects-part-1/1610853) Example fireball damage: **5 damage parameter; 25 dealt without debounce** (Duplicate Touched detections multiply damage)
- [page](https://devforum.roblox.com/t/full-beginners-guide-on-scripting-animefighting-vfxvisual-effects-part-1/1610853) Hitbox lifetime: **1 second tween then delete** (Fireball hitbox removed after tween completes)
- [page](https://devforum.roblox.com/t/full-beginners-guide-on-scripting-animefighting-vfxvisual-effects-part-1/1610853) Hit debounce lifetime: **1-4 seconds** (Time before debounce value is removed via Debris)

## Tools
Roblox Studio, UserInputService, ContextActionService, RemoteEvent, TweenService, Debris service, ReplicatedStorage

## He points to
- SushiScripter DevForum article on server-sided debounce
- SushiScripter DevForum article on client-replication VFX

## Quotes
- [page](https://devforum.roblox.com/t/full-beginners-guide-on-scripting-animefighting-vfxvisual-effects-part-1/1610853) "server-sided effects are a sin"
- [page](https://devforum.roblox.com/t/full-beginners-guide-on-scripting-animefighting-vfxvisual-effects-part-1/1610853) "Exploiters can do anything a local script can do, which includes firing servers"

## Topics
[[anti-exploit-and-security]] [[building-art-and-assets]] [[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[core-loops-and-game-design]] [[development-process-and-speed]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
