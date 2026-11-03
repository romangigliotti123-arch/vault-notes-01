---
name: pass-ownership-cache-builder
description: "Check whether the kit Shop already covers pass ownership; if perks are read from other scripts or services, add a small server cache with retries, a stale fallback and a forced re-ask after the purchase prompt (never trusting wasPurchased). Use when many scripts check passes or ownership calls fail; adding the passes themselves is gamepass-maker."
category: money
tags: gamepass, ownership, cache, UserOwnsGamePassAsync, retry, refresh, purchase prompt, perks, server
kb: Roblox/roblox-kb/monetisation-gamepasses.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/data-persistence.md, Roblox/roblox-kb/_tools/CHECKLIST-monetization.md
related: gamepass-maker, receipt-flow-tester, vip-pass-designer, retry-wrapper-builder, remote-guard-builder
---

# pass-ownership-cache-builder

One job: make "does this player own this pass" fast, correct and non-spoofable wherever it is asked. The kit Shop system already verifies ownership with retries and exposes `ShopService.HasPass(player, "VIP")` for passes in its catalogue. This skill starts by checking whether that is enough; only when it is not (several services or places need the answer, passes outside the Shop catalogue, or a very hot path) does it add `scripts/OwnershipCache.luau`.

## When to use
Perks check passes in many scripts, ownership API calls fail or are called too often, or a mid-session purchase does not apply. Not for: designing passes (`gamepass-maker`), receipts for products (`receipt-flow-tester`).

## Inputs (max 2)
1. Where passes are checked now (default: search the project for `UserOwnsGamePassAsync` and `HasPass`). 2. How fresh answers must be (default: a refund may take up to 5 minutes to be noticed).

## Procedure
1. Search: list every call site of `UserOwnsGamePassAsync`, `PromptGamePassPurchase`, `PromptGamePassPurchaseFinished`, and `HasPass`. A table of file, function, client or server.
2. Decision: if every perk already uses `ShopService.HasPass` on the server, STOP and report "Shop covers it; no cache needed" with the search output. Do not add a second source of truth.
3. Otherwise copy `scripts/OwnershipCache.luau` into the server code and create one cache in a module (one per server): `OwnershipCache.new({ fetch = <wrapper of UserOwnsGamePassAsync>, now = os.clock, ttl = 300, attempts = 3, wait = task.wait })`.
4. Replace every perk check by `OwnershipCache.get(cache, userId, passId)`; use the returned status: `fresh`, `cached`, `stale` (last known answer after a failed lookup) or `unknown` (false, never throws). Decide per perk what `unknown` means (safe default: deny the perk, never grant).
5. Hook the purchase prompt on the server: on `PromptGamePassPurchaseFinished` call `OwnershipCache.onPromptFinished(cache, userId, passId, wasPurchased)`; it discards the cached answer and asks again whatever `wasPurchased` says (the vault and Shop both treat that flag as untrusted).
6. On player leaving call `OwnershipCache.clearPlayer`. Never persist pass ownership in your DataStore as truth; it is a cache.
7. Keep clients out: the client may display a locked/unlocked state from a server-sent flag but never decides.
8. Test: `lune run ../skillpack/money/pass-ownership-cache-builder/scripts/tests/OwnershipCache.test.luau` from `~/.claude/claude-kit/systems`.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (add the module, replace call sites) -> `start_stop_play` -> `execute_luau` (Server) to ask the cache twice for a test player (second must say `cached`) -> `get_console_output`. In Studio ownership of real passes depends on the account and the published place: a real purchase stays `untested`.

## Fallback
Files plus the Lune test (headless). Real purchase and refund behaviour stay `untested`.

## Evidence
`Roblox/roblox-kb/monetisation-gamepasses.md` (check ownership on the server; verify rather than trust the client), `Roblox/roblox-kb/anti-exploit-and-security.md` (never trust client-sent state), `Roblox/roblox-kb/scripting-and-performance.md` (avoid repeated yielding web calls), `Roblox/roblox-kb/data-persistence.md`, `systems/Shop/README.md` (existing HasPass, retries, `wasPurchased` never trusted). The 300 s ttl and 3 attempts are defaults to tune.

## Output
Search table, the decision (Shop covers it, or cache added), code changes and the test result.

## Acceptance checks
- [ ] The call-site search output is quoted and every site is accounted for.
- [ ] If the cache was added: no perk code calls `UserOwnsGamePassAsync` directly any more (search returns none outside the fetch wrapper).
- [ ] `lune run` OwnershipCache tests pass (quote "8 passed, 0 failed") and luau-check is clean.
- [ ] The spoof test (`wasPurchased=true`, not owned) returns false.
- [ ] `unknown` handling is decided per perk and written down.

## Pitfalls
Two sources of truth (Shop and the cache). Trusting `wasPurchased`. Granting on `unknown`. Never expiring answers so refunds are never seen. Persisting ownership as a boolean in saved data.

## Related
`gamepass-maker`, `receipt-flow-tester`, `vip-pass-designer`, `retry-wrapper-builder`, `remote-guard-builder`.
