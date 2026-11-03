---
title: "Docs: scripting / security / network-ownership"
url: https://create.roblox.com/docs/scripting/security/network-ownership.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: scripting / security / network-ownership

[Open](https://create.roblox.com/docs/scripting/security/network-ownership.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on network ownership and movement validation. Explains that clients owning unanchored parts/characters can teleport, change speed, bypass collisions and fling parts. Advises manual ownership control for gameplay-critical parts, and notes server authority (beta) as the most reliable fix. Client-side validation needs averaging, leaky-bucket accumulators, XZ-plane projection and teleport exemptions.

## Tips
- [page](https://create.roblox.com/docs/scripting/security/network-ownership) **[[anti-exploit-and-security]]** For gameplay-critical unanchored parts or assemblies, set network ownership manually via the network ownership API or turn off automatic ownership.
- [page](https://create.roblox.com/docs/scripting/security/network-ownership) **[[anti-exploit-and-security]]** Server authority moves physics and movement validation fully to the server; it is the most reliable fix for movement and physics exploits (beta at time of writing).
- [page](https://create.roblox.com/docs/scripting/security/network-ownership) **[[anti-exploit-and-security]]** Do not rely on client-side speed or property checks: exploiters can set WalkSpeed locally without events the server can read.
- [page](https://create.roblox.com/docs/scripting/security/network-ownership) **[[anti-exploit-and-security]]** Average position updates over time when validating movement, since internet latency causes noisy position data.
- [page](https://create.roblox.com/docs/scripting/security/network-ownership) **[[anti-exploit-and-security]]** Use leaky bucket-style accumulators to tolerate legitimate bursts while still catching sustained movement violations.
- [page](https://create.roblox.com/docs/scripting/security/network-ownership) **[[anti-exploit-and-security]]** Project movement onto a plane (e.g. XZ for ground movement) so legitimate vertical movement is not flagged as teleporting.
- [page](https://create.roblox.com/docs/scripting/security/network-ownership) **[[anti-exploit-and-security]]** Build explicit exemption systems for legitimate teleport mechanics so they do not trigger movement violations.
- [page](https://create.roblox.com/docs/scripting/security/network-ownership) **[[anti-exploit-and-security]]** Tune validation frequency, tolerance and enforcement per game; basic heuristics can falsely flag players with unstable connections.

## Tools
Network ownership API, Server authority (beta)

## He points to
- Roblox docs: sidebar security topics

## Topics
[[anti-exploit-and-security]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
