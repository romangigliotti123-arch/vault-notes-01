---
id: "rbx-remote-sec"
type: skill
category: "roblox"
source: "own"
license: "first-party"
repo_path: "skills/roblox/rbx-remote-sec/SKILL.md"
description: "Server-authoritative design and exploit review for RemoteEvents/RemoteFunctions: validate every argument, rate-limit, never trust client state. Use when writing client-server Luau or auditing a game for exploits and cheating."
orig_name: "rbx-remote-sec"
tags: [lib/skill, cat/roblox, src/own]
---

# rbx-remote-sec

> Server-authoritative design and exploit review for RemoteEvents/RemoteFunctions: validate every argument, rate-limit, never trust client state. Use when writing client-server Luau or auditing a game for exploits and cheating.

Type: skill | Category: [[categories/cat-roblox|roblox]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/roblox/rbx-remote-sec/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# Roblox remote security

Code comments: none by default (see rbx-luau, Comments).

Assume every client is hostile: anything on the client (LocalScripts, ReplicatedStorage code, physics ownership) can be changed by an exploiter. Remotes are the attack surface.

## Write rules
1. The server decides outcomes (damage, rewards, prices, cooldowns, inventory). The client only requests: `BuyItem:FireServer(itemId)`, never `GiveCoins:FireServer(500)`.
2. Validate on the server for each OnServerEvent / OnServerInvoke:
   - argument count and `typeof` of each arg (string, number, Instance, table); reject NaN and inf (`n ~= n`), clamp ranges, cap string length and table size/depth.
   - Instances: check `IsDescendantOf` an expected container and that it is the right class; never trust an Instance's name or attributes sent by the client.
   - Permission and state: the player is alive, owns the item, is in range, has the cooldown elapsed, is in the right game phase.
3. Rate-limit per player per remote (token bucket or last-fired timestamp). Drop silently or kick after repeated abuse.
4. Do not return secrets from RemoteFunctions. Never use `InvokeClient` (a client that never answers can hang the server thread).
5. Distance and speed checks for server-side movement-dependent actions use server positions, not client-sent positions. Use `SetNetworkOwner(nil)` on important physics parts.
6. Keep server-only secrets, admin logic and unreleased reward tables in ServerStorage / ServerScriptService, never ReplicatedStorage.
7. Log suspicious fires (player UserId, remote, args); do not auto-ban on one event (lag false positives).

## Review procedure
1. List every Remote (`Grep` for `RemoteEvent`, `RemoteFunction`, `OnServerEvent`, `OnServerInvoke`, `FireServer`, `InvokeServer`).
2. For each: who can fire it, what the server does with the args, worst case if fired 1000 times a second with garbage.
3. Report a table: remote | args validated | rate-limited | trust problem | fix, ordered by severity (currency/progress writes first, cosmetic last).
4. Patch the high-severity ones if asked; re-run the list afterwards.

## Sources

[cold:rbx-remote-sec/sources.md] read only to verify the source of this idea or its licence/attribution.
