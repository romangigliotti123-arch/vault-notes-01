---
title: "Docs: scripting / security / client-server-boundary"
url: https://create.roblox.com/docs/scripting/security/client-server-boundary.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: scripting / security / client-server-boundary

[Open](https://create.roblox.com/docs/scripting/security/client-server-boundary.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs on securing the client-server boundary: validating remote inputs (context, type/structure, value, NaN), server-side rate limiting with a token bucket, securing ProximityPrompt/ClickDetector/DragDetector events, making servers gatekeepers for client-to-client relays, DataStore-safe sanitisation, and ProcessReceipt-only purchase granting.

## Tips
- [page](https://create.roblox.com/docs/scripting/security/client-server-boundary) **[[client-server-and-remotes]]** Validate every piece of client data on the server before use; a client can send any value, type, or structure to a RemoteEvent or RemoteFunction.
- [page](https://create.roblox.com/docs/scripting/security/client-server-boundary) **[[anti-exploit-and-security]]** Check context on the server: distance to shop, key ownership, character alive, and other permissions before granting rewards or changing shared state.
- [page](https://create.roblox.com/docs/scripting/security/client-server-boundary) **[[anti-exploit-and-security]]** Verify instance arguments by checking IsDescendantOf the expected folder and class, since exploiters can send fake tables mimicking Instances.
- [page](https://create.roblox.com/docs/scripting/security/client-server-boundary) **[[anti-exploit-and-security]]** Use math.isfinite() to reject inf and NaN; NaN fails all comparisons, so range and balance checks silently pass.
- [page](https://create.roblox.com/docs/scripting/security/client-server-boundary) **[[anti-exploit-and-security]]** Never rely solely on client-side rate limits; enforce rate limits on the server for every client-triggerable action.
- [page](https://create.roblox.com/docs/scripting/security/client-server-boundary) **[[anti-exploit-and-security]]** Use a token bucket limiter: TokenBucket.new(5, 10) allows bursts of 5 and refills one token every 2 seconds. Clear per-player buckets on PlayerRemoving.
- [page](https://create.roblox.com/docs/scripting/security/client-server-boundary) **[[anti-exploit-and-security]]** Treat ProximityPrompt, ClickDetector and DragDetector events as remotes: exploiters can fire them from any distance and ignore Enabled or MaxActivationDistance.
- [page](https://create.roblox.com/docs/scripting/security/client-server-boundary) **[[anti-exploit-and-security]]** Only ProximityPrompt.Triggered has a server-side distance check; re-check distance, state and cooldowns yourself for the other events.
- [page](https://create.roblox.com/docs/scripting/security/client-server-boundary) **[[anti-exploit-and-security]]** For critical actions, anchor parts or use the network ownership API, since unanchored parents let exploiters take ownership and bypass distance checks.
- [page](https://create.roblox.com/docs/scripting/security/client-server-boundary) **[[client-server-and-remotes]]** For weapons, have the client send shot origin and hit position; server checks origin near character, hit near reported part, and no static walls in between, with latency tolerance.
- [page](https://create.roblox.com/docs/scripting/security/client-server-boundary) **[[combat-and-gameplay-systems]]** Server-side weapon checks: track last fire time, ammo count, teammate/alive status, and block firing during reload or sprint state.
- [page](https://create.roblox.com/docs/scripting/security/client-server-boundary) **[[client-server-and-remotes]]** Make the server a gatekeeper, not a relay: validate, rate limit per player, then FireAllClients. Relays let exploiters spam effects or send invalid data to all clients.
- [page](https://create.roblox.com/docs/scripting/security/client-server-boundary) **[[data-persistence]]** Sanitise client input before saving: no Instances, cap string length, reject NaN/nil table keys, and check strings with utf8.len() since DataStores only accept valid UTF-8.
- [page](https://create.roblox.com/docs/scripting/security/client-server-boundary) **[[data-persistence]]** Validate all data before trade operations and revert every change if any step fails, to prevent item duplication from race conditions.
- [page](https://create.roblox.com/docs/scripting/security/client-server-boundary) **[[monetisation-devproducts]]** Grant passes and developer products only inside ProcessReceipt on the server; never trust PromptProductPurchaseFinished, which can be spoofed.
- [page](https://create.roblox.com/docs/scripting/security/client-server-boundary) **[[monetisation-devproducts]]** In ProcessReceipt, handle repeat receipts: a product may already have been granted for a given receipt.
- [page](https://create.roblox.com/docs/scripting/security/client-server-boundary) **[[scripting-and-performance]]** Rate limit server operations that hit DataStoreService or BadgeService, since exceeding their built-in limits makes requests fail.

## Numbers
- [page](https://create.roblox.com/docs/scripting/security/client-server-boundary) Token bucket example: **TokenBucket.new(5, 10): burst of 5, refill 1 token per 2 seconds** (Example rate limiter from docs for a custom chat RemoteEvent)
- [page](https://create.roblox.com/docs/scripting/security/client-server-boundary) Hold events: **Server accepts PromptButtonHoldBegan even when server HoldDuration is 0** (ProximityPrompt exploit note in docs)

## Tools
TokenBucket module (example), math.isfinite, utf8.len, ProcessReceipt

## He points to
- Roblox docs: Securing the client-server boundary

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[data-persistence]] [[monetisation-devproducts]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
