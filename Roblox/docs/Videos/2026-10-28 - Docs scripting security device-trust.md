---
title: "Docs: scripting / security / device-trust"
url: https://create.roblox.com/docs/scripting/security/device-trust.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: scripting / security / device-trust

[Open](https://create.roblox.com/docs/scripting/security/device-trust.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Device Trust API docs. Explains IntegrityService.EvaluatePlayerDeviceTrust and Player.DeviceTrustLevel, the five trust levels, supported platforms, the measures table, and how to route, gate, or reject players by trust. Includes code examples and common mistakes.

## Tips
- [page](https://create.roblox.com/docs/scripting/security/device-trust) **[[anti-exploit-and-security]]** Read DeviceTrustLevel on the server only. Send the client the result to enable or hide features, and re-check on the server before every sensitive action.
- [page](https://create.roblox.com/docs/scripting/security/device-trust) **[[anti-exploit-and-security]]** Treat Pending as untrusted. Every player starts there, and it may stay Pending for the whole session if the check can't finish.
- [page](https://create.roblox.com/docs/scripting/security/device-trust) **[[anti-exploit-and-security]]** Don't compare trust levels by Value. Unknown sorts before None, so a greater-than-None check silently excludes Unknown players. List allowed levels in a table instead.
- [page](https://create.roblox.com/docs/scripting/security/device-trust) **[[anti-exploit-and-security]]** Don't reject in PlayerAdded. The level usually isn't ready yet. Return Reject from the EvaluatePlayerDeviceTrust callback instead.
- [page](https://create.roblox.com/docs/scripting/security/device-trust) **[[anti-exploit-and-security]]** Keep callback work minimal. It times out after about 10 seconds, and on timeout Roblox accepts the player. Limit DataStore reads and HTTP calls inside it.
- [page](https://create.roblox.com/docs/scripting/security/device-trust) **[[anti-exploit-and-security]]** Don't treat a device passing all measures as Full. A measure also reads true when unavailable. Check DeviceTrustLevel first and use measures only to find failed checks.
- [page](https://create.roblox.com/docs/scripting/security/device-trust) **[[anti-exploit-and-security]]** Device trust is one layer only. Still validate positions, scores and currency on the server, since exploits on weak server validation work on trusted devices.
- [page](https://create.roblox.com/docs/scripting/security/device-trust) **[[player-psychology-and-game-feel]]** Avoid hard rejection. Only reject at None as a last resort, and prefer routing or feature gating. Rejection also hits legitimate players on old or unfixable devices.
- [page](https://create.roblox.com/docs/scripting/security/device-trust) **[[player-psychology-and-game-feel]]** Write a custom rejection message that points players to a mode they can still play. Otherwise Roblox shows a generic default message.
- [page](https://create.roblox.com/docs/scripting/security/device-trust) **[[genre-mechanics]]** For competitive FPS, allow Unknown in casual only. Put Standard and Full in ranked. For fighting games, use separate or trusted servers. For racing, keep Unknown and None off leaderboards.
- [page](https://create.roblox.com/docs/scripting/security/device-trust) **[[genre-mechanics]]** For idle or tycoon games, withhold AFK rewards from None but not Unknown. For trade hangouts, block trading only at None. Roleplay or social games can give full access to all levels.
- [page](https://create.roblox.com/docs/scripting/security/device-trust) **[[testing-debugging-and-qa]]** Studio always reports Pending and never runs the callback. Put the trust policy in a function, skip the check when IsStudio is true, and print the result for each level to test it.
- [page](https://create.roblox.com/docs/scripting/security/device-trust) **[[analytics-metrics]]** Before enforcing a policy, check the Anti-cheat page under Safety in Creator Hub. It estimates DAU, playtime and revenue by trust level on supported platforms.
- [page](https://create.roblox.com/docs/scripting/security/device-trust) **[[common-mistakes]]** Don't assume Unknown means untrusted. Roblox only says it can't tell, so decide per feature or per part of the game how to treat it.
- [page](https://create.roblox.com/docs/scripting/security/device-trust) **[[scripting-and-performance]]** Hold a player in PlayerAdded only when routing needs the level before spawn. Resume with a timeout of about 10 seconds so no player waits forever, and handle PlayerRemoving.
- [page](https://create.roblox.com/docs/scripting/security/device-trust) **[[matchmaking-and-teleport]]** Route by trust level with TeleportAsync from a casual place to a ranked place. Also set the callback in the ranked place, because players can join there directly through friends.

## Numbers
- [page](https://create.roblox.com/docs/scripting/security/device-trust) callback timeout: **about 10 seconds, then player accepted** (EvaluatePlayerDeviceTrust callback; Roblox accepts on timeout)
- [page](https://create.roblox.com/docs/scripting/security/device-trust) trust levels: **5: Pending, Unknown, None, Standard, Full** (Enum.PlayerDeviceTrustLevel values)
- [page](https://create.roblox.com/docs/scripting/security/device-trust) supported platforms now: **Android, Chromebook, Meta Quest (None/Standard/Full); web None; iOS, macOS, Windows, Xbox, PlayStation Unknown** (Other platforms are coming soon and report Unknown)

## Tools
IntegrityService.EvaluatePlayerDeviceTrust, Player.DeviceTrustLevel, Player:IsVerified(), TeleportService:TeleportAsync(), Creator Hub Anti-cheat page

## He points to
- Help Center: supported Android devices and device troubleshooting steps
- Configure secure teleportation
- Securing the client-server boundary
- Cheat mitigation tactics

## Topics
[[analytics-metrics]] [[anti-exploit-and-security]] [[common-mistakes]] [[genre-mechanics]] [[matchmaking-and-teleport]] [[player-psychology-and-game-feel]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
