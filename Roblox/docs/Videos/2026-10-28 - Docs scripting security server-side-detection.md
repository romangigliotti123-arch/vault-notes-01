---
title: "Docs: scripting / security / server-side-detection"
url: https://create.roblox.com/docs/scripting/security/server-side-detection.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: scripting / security / server-side-detection

[Open](https://create.roblox.com/docs/scripting/security/server-side-detection.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs on server-side detection and consequencing for exploits. Covers philosophy (server decides, prevent harm first, reversible actions), heuristics (fastest completion time, rate of gain, action cadence) with suspicion scoring, honeypot remotes, directional remote checks, and an escalating consequence ladder with BanAsync.

## Tips
- [page](https://create.roblox.com/docs/scripting/security/server-side-detection) **[[anti-exploit-and-security]]** Never ban based on client-side detections; exploiters can easily bypass them. Detection and consequences belong on the server.
- [page](https://create.roblox.com/docs/scripting/security/server-side-detection) **[[anti-exploit-and-security]]** Neutralize exploit impact quietly first, e.g. rubber-band a speed-hacking player back to their last valid position instead of kicking.
- [page](https://create.roblox.com/docs/scripting/security/server-side-detection) **[[anti-exploit-and-security]]** Prefer reversible actions (temporary suspensions, resource removal) over permanent bans, since false positives happen.
- [page](https://create.roblox.com/docs/scripting/security/server-side-detection) **[[anti-exploit-and-security]]** Treat robust validation and rate limiting as primary security; detection heuristics only supplement them.
- [page](https://create.roblox.com/docs/scripting/security/server-side-detection) **[[anti-exploit-and-security]]** Use heuristics comparing actions to a theoretical maximum or baseline, e.g. max legitimate coin earn rate per minute, or theoretical fastest obby completion time.
- [page](https://create.roblox.com/docs/scripting/security/server-side-detection) **[[anti-exploit-and-security]]** Check action cadence: robotically identical intervals between repeated actions (e.g. exactly 2.500s over 100 casts) signal macros or bots, since human timing varies.
- [page](https://create.roblox.com/docs/scripting/security/server-side-detection) **[[anti-exploit-and-security]]** Use a suspicion score: increment per failed heuristic and only kick or ban after multiple varied detections exceed a high threshold.
- [page](https://create.roblox.com/docs/scripting/security/server-side-detection) **[[anti-exploit-and-security]]** Correlate signals across time and systems before acting; a single record-time flag may be an unintended shortcut, not cheating.
- [page](https://create.roblox.com/docs/scripting/security/server-side-detection) **[[anti-exploit-and-security]]** Deploy honeypot RemoteEvents/RemoteFunctions that legitimate clients never use; any firing is high-confidence exploit traffic. Log and kick.
- [page](https://create.roblox.com/docs/scripting/security/server-side-detection) **[[client-server-and-remotes]]** Design remotes with fixed direction (client-to-server or server-to-client) and track which direction each should use; firing one the wrong way is a reliable detection.
- [page](https://create.roblox.com/docs/scripting/security/server-side-detection) **[[anti-exploit-and-security]]** Follow an escalating consequence ladder: silent logging, quiet mitigation, temporary restrictions, then visible enforcement like kicks or bans.
- [page](https://create.roblox.com/docs/scripting/security/server-side-detection) **[[anti-exploit-and-security]]** Delay visible consequences so exploiters can't learn exactly what triggered detection.
- [page](https://create.roblox.com/docs/scripting/security/server-side-detection) **[[anti-exploit-and-security]]** Match response to severity and community: minor economic exploits warrant lighter treatment than game-breaking physics cheats; competitive games need stricter enforcement.
- [page](https://create.roblox.com/docs/scripting/security/server-side-detection) **[[anti-exploit-and-security]]** For persistent offenders, use Players:BanAsync rather than only kicking; it blocks rejoining and tracks across the universe.
- [page](https://create.roblox.com/docs/scripting/security/server-side-detection) **[[anti-exploit-and-security]]** Version your detection rules and track consequence rates to find systems producing false positives; monitor player feedback on fairness.

## Numbers
- [page](https://create.roblox.com/docs/scripting/security/server-side-detection) Rate of gain example: **100 coins/min legitimate; flag a sudden 10,000 coins in one second** (Rate of Gain heuristic example from docs)
- [page](https://create.roblox.com/docs/scripting/security/server-side-detection) Obby fastest completion example: **World record 30s; 5s completion is strong exploit signal** (Fastest Completion Time heuristic example)
- [page](https://create.roblox.com/docs/scripting/security/server-side-detection) Action cadence example: **100 casts at exactly 2.500s intervals indicates macro or bot** (Fishing minigame action cadence example)

## Tools
Players:BanAsync

## He points to
- Roblox Creator Docs: Securing the client-server boundary

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
