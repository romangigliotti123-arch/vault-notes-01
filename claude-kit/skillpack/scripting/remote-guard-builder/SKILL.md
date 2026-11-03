---
name: remote-guard-builder
description: "Generate and install a validated, rate-limited wrapper for every RemoteEvent and RemoteFunction a game uses: argument validators (type, range, length, instance class), per-player limits, a rejection hook and a table of remotes with their spec. Use when adding remotes or hardening existing ones; exploit-audit finds the weak ones first."
category: scripting
tags: remote, remoteevent, remotefunction, validation, rate limit, server authority, exploit, security, anti-cheat, onserverevent
kb: Roblox/roblox-kb/client-server-and-remotes.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/_tools/CHECKLIST-launch.md
related: exploit-audit, roblox-remote-security, cooldown-manager-builder, input-validation-auditor, server-authority-checker, remote-fuzzer, proximity-prompt-wiring
---

# remote-guard-builder

The client is the exploiter's. A remote is a public API that anyone can call with any values at any rate. This skill puts one small, tested guard in front of every handler. The review of existing code is `exploit-audit`; the kit skill `roblox-remote-security` has the checklist; this one writes the code.

## When to use
Adding a remote, or after `exploit-audit` listed weak handlers. Not for: deciding game design, or client-side "anti-cheat" (the vault is explicit: client checks can be disabled or spoofed).

## Inputs (max 2)
1. The remotes (default: scan with `exploit-audit/scripts/audit_remotes.luau` or `script_grep` for `OnServerEvent`). 2. For each: what the client may ask for (default: a minimal action name + ids, nothing derived).

## Procedure
1. Inventory every RemoteEvent, RemoteFunction, UnreliableRemoteEvent, ProximityPrompt, ClickDetector and DragDetector. Treat prompts/detectors as remotes: exploiters can fire them from any distance and ignore `Enabled` or `MaxActivationDistance`.
2. For each remote write the spec in the table `remotes.md`: name, direction, args (type, min/max, allowed values), limit (calls per seconds), server checks beyond the arguments (distance, ownership, cooldown, state, currency), and what the handler does. Send identifiers (item id, slot), never values the server can look up (price, damage, position).
3. Copy `scripts/RemoteGuard.luau` to `src/server/RemoteGuard.luau` (not replicated). Bind each remote:
   ```lua
   RemoteGuard.bind(remote, {
       args = { RemoteGuard.oneOf({ "buy", "sell" }), RemoteGuard.integer(1, 99) },
       limit = { calls = 5, per = 1 },
       handler = function(player, action, qty) ... end,
       onReject = function(player, why) log(player, why) end,
   })
   ```
   Validators: `number`, `integer`, `string(maxLen, pattern?)`, `boolean`, `oneOf`, `vector3(maxMagnitude)`, `instance(class, ancestor?)`, `optional`. Extra or missing arguments are rejected.
4. Inside every handler, re-verify context on the server (the guard checks shape, not meaning): the player is alive, within range of the shop/target (`(root.Position - target.Position).Magnitude`), owns the item, has enough currency, and the action is allowed in the current state. Mutate state only after all checks.
5. Rate limits: set from the real use. Spammable actions (attack, collect) allow the legitimate rate plus slack; purchases are low. A rejection counter per player can feed a flag/kick policy (log first; kick only on clear abuse; `honeypot-remote-builder` for high-confidence detection).
6. RemoteFunctions: never let a client-invoked function yield on untrusted values or return secrets; prefer events with server-to-client replies. Never `InvokeClient` from the server without a timeout path.
7. Test: Lune (`lune run ../skillpack/scripting/remote-guard-builder/scripts/tests/RemoteGuard.test.luau` from `~/.claude/claude-kit/systems`) for the guard; then a bad-input pass against each real remote (`remote-fuzzer`): nil, NaN, huge, wrong type, negative, string too long, wrong Instance.
8. Update `remotes.md`; keep it in the repo.

## Studio MCP path
`list_roblox_studios` -> `script_grep` for `OnServerEvent|OnServerInvoke` -> `multi_edit` to add the module and rewrite each handler -> `start_stop_play` -> `execute_luau` (Client) firing bad values at each remote, `get_console_output` (Server) to confirm rejections. If a Rojo session is active, edit files instead of `multi_edit`.

## Fallback
Files plus the Lune tests; the bad-input pass against real remotes is `untested` without a running place.

## Evidence
`Roblox/roblox-kb/anti-exploit-and-security.md` (validate every client argument: type, nil, range, length, Instance class and location; never rely on client-side security; keep authority in server-only containers; re-verify context and economy; rate-limit per player on the server; treat ProximityPrompt/ClickDetector/DragDetector as remotes; honeypot remotes), `Roblox/roblox-kb/client-server-and-remotes.md` (send minimal identifiers; gatekeeper not relay; prediction then reconcile), `Roblox/roblox-kb/scripting-and-performance.md` (debounce remotes).

## Output
`src/server/RemoteGuard.luau`, rewritten bindings, `remotes.md` (spec table), test results quoted (counts and the bad-input matrix).

## Acceptance checks
- [ ] Every remote and prompt in the inventory is bound or removed.
- [ ] Each binding has argument validators AND a rate limit.
- [ ] Each handler re-checks context (range, ownership, state) before changing anything.
- [ ] Lune guard tests pass (quote the final line); luau-check clean.
- [ ] Bad-input matrix run against each remote, or marked untested.
- [ ] No server logic or secrets in replicated containers.

## Pitfalls
Validating types but not meaning (a valid item id the player does not own). A rate limit keyed by player name instead of UserId. Trusting `Instance` arguments without class and location checks. Letting the client send price or damage. One shared limiter for all remotes (a busy remote starves the rest; each bind has its own).

## Related
`exploit-audit`, `roblox-remote-security`, `cooldown-manager-builder`, `input-validation-auditor`, `remote-fuzzer`, `honeypot-remote-builder`.
