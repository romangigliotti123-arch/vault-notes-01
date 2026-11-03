---
name: private-server-settings-setter
description: "Plan private (VIP) server access and the teleport/reserved-server setup around it: public prerequisite, price and the subscription-cancelling price-change rule, conflicts with paid access, who earns what, server-side teleports and secure teleport data. Use before enabling or changing private servers."
category: publish
tags: private servers, VIP servers, reserved servers, teleport, pricing, subscriptions, access control, settings
kb: Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/matchmaking-and-teleport.md, Roblox/roblox-kb/pricing.md, Roblox/roblox-kb/_tools/CHECKLIST-monetization.md
related: private-server-planner, experience-settings-configurator, matchmaking-settings-setter, devex-planner, publish-readiness-gate, pay-to-win-checker
---

# private-server-settings-setter

One job: get the private server settings right and avoid the two expensive mistakes (changing the price and cancelling every subscription; leaking value through teleport data). Deciding whether private servers are worth offering and what they should contain is `private-server-planner`; this skill checks the settings plan with `scripts/server_plan.py` and scans the code for teleport mistakes. Every price, rule and cap is `live-check`: the Creator Docs pages change and the owner reads the live dashboard.

## When to use
Before enabling private servers, before changing their price, and when adding teleports or reserved servers. Not for: pricing strategy (`price-optimization-readiness`), the feature's content (`private-server-planner`), matchmaking (`matchmaking-settings-setter`).

## Inputs (max 2)
1. Intended setup (public?, price, paid access?). 2. Project folder for the teleport scan (default: current).

## Procedure
1. Open the live private-servers and teleport pages (Evidence); copy the current rules (public prerequisite, price-change effect, Roblox Plus rule, teleport guidance) with the date.
2. `python -I ~/.claude/claude-kit/skillpack/publish/private-server-settings-setter/scripts/server_plan.py --template > release/servers.json`, fill it; read the price from the live dashboard, never invent one. Put the old price in `previous_price_robux` when changing it.
3. Run `python -I .../server_plan.py release/servers.json --scan <project>`. FAIL examples: private servers on a non-public game, paid access together with private servers, a price change without the acknowledgement flag, `SetTeleportData` carrying value-bearing data.
4. Price change: it cancels all active subscriptions and players get an inbox message, so change it only when necessary, announce first, and set `ack_price_change_cancels_subs` deliberately.
5. Teleports: server-side `TeleportAsync` only; `ReservedServerId` from `HttpService:GenerateGUID(false)`; wrap in `pcall` with retries (flooded and failure results need different waits per the page); persist money and inventory in DataStores or MemoryStores, never in teleport data (it is client-visible and unencrypted).
6. Access control: decide Secure Within Universe Only for places that must not be reachable by outside teleports; migrate legacy client teleports first.
7. Revenue notes: the creator earns the set price; Plus subscribers get private servers free but pay-outs follow the live rules (cap and rate are `live-check`).
8. Write `release/servers.md` with the JSON, script output, page dates, and an owner click list. Dashboard behaviour stays `untested`.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `script_grep` (`TeleportAsync`, `SetTeleportData`, `ReserveServer`) -> `start_stop_play` -> `execute_luau` (Server) in a published test place to run a reserved-server teleport -> `get_console_output`. Teleports need a published place; local play only simulates.

## Fallback
The plan check and scan run offline. Anything needing a published test universe (reserved server routing, access control effect, private server join) is `untested`.

## Evidence
Official (live-check): `Roblox/docs/Videos/2026-10-28 - Docs production monetization private-servers.md` (public prerequisite; paid access and private servers exclusive; price change cancels subscriptions; Plus earnings), `... Docs projects teleport.md` (server-side TeleportAsync, secure access control, GenerateGUID for ReservedServerId, never secure data in teleport data, retry by result). Pack: `Roblox/roblox-kb/monetisation-other.md`, `Roblox/roblox-kb/matchmaking-and-teleport.md`.

## Output
`release/servers.json`, `release/servers.md`.

## Acceptance checks
- [ ] `server_plan.py release/servers.json --scan <project>` exits 0 (quote the OK line).
- [ ] No price was typed from memory: the dashboard value and date are noted.
- [ ] Price changes carry the written acknowledgement.
- [ ] No client-side `Teleport(` remains; teleport data holds no value.
- [ ] `server_plan.py --selftest` prints `selftest ok`.

## Pitfalls
Fiddling with the price to test conversion (each change cancels subscribers). Trusting `SetTeleportData` for the player's coins. Reusing one `ReservedServerId` for unrelated groups. Offering private servers on a game that is still friends-only.

## Related
`private-server-planner`, `experience-settings-configurator`, `matchmaking-settings-setter`, `devex-planner`, `publish-readiness-gate`.
