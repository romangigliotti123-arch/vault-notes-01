---
title: "Docs: scripting / security / access-control"
url: https://create.roblox.com/docs/scripting/security/access-control.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: scripting / security / access-control

[Open](https://create.roblox.com/docs/scripting/security/access-control.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs on access control and confidentiality. Covers client-side teleportation within universes, using Secure within universe only access setting, defense-in-depth for restricted places, replication security, and why server logic must not be in shared ModuleScripts since they can be decompiled.

## Tips
- [page](https://create.roblox.com/docs/scripting/security/access-control) **[[anti-exploit-and-security]]** Set Access Control for Places to 'Secure within universe only' in the Creator Dashboard for any game with restricted subplaces, progression-gated areas, or test places.
- [page](https://create.roblox.com/docs/scripting/security/access-control) **[[anti-exploit-and-security]]** Disabling 'Direct Access' only hides the Join button on the website; it does not prevent client-initiated teleports.
- [page](https://create.roblox.com/docs/scripting/security/access-control) **[[anti-exploit-and-security]]** Do not rely on kicking unauthorized players from a subplace; content replicates before server kick logic runs.
- [page](https://create.roblox.com/docs/scripting/security/access-control) **[[data-persistence]]** Keep development and test places in separate, private universes to ensure confidentiality of unreleased content.
- [page](https://create.roblox.com/docs/scripting/security/access-control) **[[anti-exploit-and-security]]** Disallow incoming players by default so that failed or errored verification still blocks entry.
- [page](https://create.roblox.com/docs/scripting/security/access-control) **[[anti-exploit-and-security]]** Add server-side group role or badge checks and verify player state or progression before allowing entry into restricted places.
- [page](https://create.roblox.com/docs/scripting/security/access-control) **[[anti-exploit-and-security]]** Use Players.BanAsync for players who fail validation so they cannot keep retrying joins on the same account.
- [page](https://create.roblox.com/docs/scripting/security/access-control) **[[optimization-and-streaming]]** Use streaming where feasible to limit how much of the world replicates to a new player.
- [page](https://create.roblox.com/docs/scripting/security/access-control) **[[anti-exploit-and-security]]** Never ship confidential event assets, scripts, or UI to production before they are meant to be active; assume exploiters will find them.
- [page](https://create.roblox.com/docs/scripting/security/access-control) **[[anti-exploit-and-security]]** Use vague names for sensitive instances (scripts, remotes, models); predictable DataModel hierarchies make exploits easier.
- [page](https://create.roblox.com/docs/scripting/security/access-control) **[[client-server-and-remotes]]** Keep server code in Script instances or ServerStorage/ServerScriptService; LocalScripts, client Scripts and ModuleScripts can be decompiled by exploiters.
- [page](https://create.roblox.com/docs/scripting/security/access-control) **[[scripting-and-performance]]** Do not mix server-only and client-only code in one ModuleScript; server logic and secrets like passwords get exposed through decompilation.

## Tools
Creator Dashboard, Players.BanAsync, Roblox Studio Play Solo

## He points to
- Teleport between places (docs)
- Data model guide (docs)
- Studio testing modes (docs)

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[data-persistence]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
