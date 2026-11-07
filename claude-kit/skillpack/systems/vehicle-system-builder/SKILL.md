---
name: vehicle-system-builder
description: "Build vehicle ownership and lifecycle rules: per-player limit, spawn cooldown, owner-only driver seat, seat claiming, abandoned-vehicle sweep, with the network-ownership and cleanup checklist. Use for cars, boats and rideables; physics tuning is separate."
category: systems
tags: vehicles, cars, seats, ownership, network ownership, spawn, despawn, driver, cleanup
kb: Roblox/roblox-kb/case-studies-driving-empire.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/physics-pathfinding-and-npc-ai.md, Roblox/roblox-kb/optimization-and-streaming.md
related: spawn-system-builder, inventory-system-builder, game-optimizer, exploit-audit, remote-guard-builder
---

# vehicle-system-builder

One job: the rules around vehicles, not the driving feel. `scripts/Vehicles.luau` enforces a per-player vehicle limit and spawn cooldown, lets only the owner take the driver seat (seat 1), lets anyone take passenger seats, rejects bad seats and double seating, and sweeps vehicles whose owner left or that sat empty past `abandonSeconds` (never an occupied one). The glue builds the model and sets network ownership.

## When to use
Car/boat/plane spawners, rideable pets, rentable vehicles. Not for: handling physics and suspension, ownership of purchased vehicles across sessions (store the owned list in the Inventory; this module handles spawned instances).

## Inputs (max 2)
1. Vehicle types, seats and who may drive (default: owner drives, others ride). 2. Limit and abandon time (default: 1 per player, 120 s).

## Procedure
1. Split the data: owned vehicles are inventory items (`inventory-system-builder`, stack 1, tradable by design); spawned vehicles are instances tracked by `Vehicles`.
2. Copy `Vehicles.luau`; `Vehicles.new({ maxPerPlayer = 1, spawnCooldown = 5, abandonSeconds = 120, seats = 2, now = os.clock, newId = HttpService GUID })`.
3. Spawn remote (rate-limited): verify the player owns the vehicle in their inventory, then `local id, why = vehicles:spawn(userId)`; clone the model near the player, tag it with the id as an attribute, and parent it in a server-owned folder.
4. Seats: on a seat's `GetPropertyChangedSignal("Occupant")` (server) call `vehicles:sit` / `leaveSeat`; when `sit` refuses (not the owner), eject the humanoid. Seat numbers map to `VehicleSeat`/`Seat` parts by attribute.
5. Network ownership: while a driver is seated, `SetNetworkOwner(driverPlayer)` on the chassis root part is the usual choice for smooth driving; set it back to the server (`nil`) when the driver leaves and before despawn. Vault: network ownership given to clients is a known exploit surface, so keep speed/teleport sanity checks server-side.
6. Every 10 s: `for _, id in vehicles:sweep(presentPlayers) do destroyModel(id) end` and on `PlayerRemoving` despawn the owner's vehicles if empty. Destroy models fully (connections too).
7. Run `cd .rbx/claude-kit/systems && lune run ../skillpack/systems/vehicle-system-builder/scripts/tests/Vehicles.test.luau` (quote the "N passed, 0 failed" line).

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (or edit the Rojo files) to add `Vehicles.luau` and the spawn/seat scripts -> `start_stop_play` -> `execute_luau` (Server) to spawn for two test players, seat them and print the sweep result -> `get_console_output` to read the result. Physics, seat detection and ownership handover are Studio work: `untested` here.

## Fallback
Files + Lune tests only. Everything that needs a running Studio session (models, seats, network ownership handover, driving feel) stays `untested` until the owner runs it; the Lune tests below are the headless proof for the pure logic.

## Evidence
`Roblox/roblox-kb/anti-exploit-and-security.md` (clients owning parts can teleport them or fly them; set network ownership deliberately, keep critical objects under server control, validate speed), `Roblox/roblox-kb/case-studies-driving-empire.md` (vehicle collecting as a monetised progression loop; indie observations), `Roblox/roblox-kb/physics-pathfinding-and-npc-ai.md`, `Roblox/roblox-kb/optimization-and-streaming.md` (cleanup and instance counts).

## Output
`Vehicles.luau`, spawn/seat scripts, `design/vehicles.md` (limits, seat rules, ownership handover, cleanup rule).

## Acceptance checks
- [ ] One vehicle per player and a spawn cooldown (Vehicles test 1).
- [ ] Only the owner takes the driver seat; seat conflicts, bad seats and double seating are refused (tests 2-3).
- [ ] Sweep removes abandoned/ownerless empty vehicles and never an occupied one (test 4).
- [ ] A Studio run of 20 spawn/despawn cycles leaves the instance count at baseline (`untested` unless run).
- [ ] Vehicles Lune tests pass: `cd .rbx/claude-kit/systems && lune run ../skillpack/systems/vehicle-system-builder/scripts/tests/Vehicles.test.luau` (quote the "N passed, 0 failed" line).

## Pitfalls
Letting a client name the vehicle to spawn without an ownership check. Leaving network ownership on a player after they exit. Models that outlive their owner. Unlimited spawns that fill the server with parts. Trusting client-reported vehicle speed.

## Related
`spawn-system-builder`, `inventory-system-builder`, `game-optimizer`, `exploit-audit`, `remote-guard-builder`.
