---
name: rbx-arch
description: "Chooses how to structure a Roblox system (plain module, OOP class, CollectionService components, ECS, state store, object pool) by evidence: existing code, lifetimes, profiler data. Use for 'should I use ECS or OOP', 'pool these', or a new multi-system feature."
---

# Roblox architecture choice

Code comments: none by default (see rbx-luau, Comments).

Pick the smallest structure that fits the evidence. Output: a decision record (see end), then code in the chosen pattern.

## Rules
1. Read the project first. Extend the pattern already in use before adding a second one. A small fix keeps the existing pattern.
2. Entity count alone is not a reason. ECS is not inherently faster than OOP; frequent spawning alone does not justify a pool. Profiler data, a bulk-query need or an existing ECS codebase do.
3. Choices combine. Give every state field one writer; no two-way mirrors between an ECS world and Instances.
4. For a substantial change write fit, main trade-offs, why the alternatives lose, the migration boundary and the rollback.

## Decision table
| Pattern | Pick when | Check first |
|---|---|---|
| Plain module / typed data | Local logic, one owner, server-lifetime service | Not duplicating existing behaviour |
| OOP class | Independent identity, state and lifetime (vehicle, round, session, boss) | Teardown contract, who mutates state |
| Components (tags) | The same behaviours combine in many ways on level-placed Instances | Idempotent attach, detach on tag removal, destroy, stream-out |
| ECS | Project already uses it, or repeated bulk queries and ordered systems, backed by a benchmark | Library API from its own docs (not assumed), debugging cost, replication, team skill |
| State store | Several unrelated systems or UI read the same changing data | One owner, unsubscribe on teardown, no derived values stored |
| Object pool | Profile shows creation/destruction spikes (bullets, hit effects, respawning NPCs) | Reset correctness, peak demand, exhaustion rule, retained memory |

## Order of questions
1. Existing pattern for this area? Use it.
2. Own lifetime (spawns, dies, owns connections)? OOP or components, else a module. Same behaviour reused across unrelated things? Components over inheritance.
3. Many systems share data? Store; single reader: a local table.
4. Allocation or destruction in the profile? Pool, then measure again.
5. ECS only after 1-4 and a benchmark of equivalent behaviour (same physics, fidelity, replication) on the target device.

## Examples
OOP object that ends with its Instance:
```lua
--!strict
local Turret = {}
Turret.__index = Turret

export type Turret = typeof(setmetatable(
	{} :: {
		model: Model,
		conns: { RBXScriptConnection },
		alive: boolean,
	},
	Turret
))

function Turret.new(model: Model): Turret
	local self = setmetatable({ model = model, conns = {}, alive = true }, Turret)
	table.insert(
		self.conns,
		model.Destroying:Connect(function()
			self:Destroy()
		end)
	)
	return self
end

function Turret.Destroy(self: Turret)
	if not self.alive then
		return
	end
	self.alive = false
	for _, conn in self.conns do
		conn:Disconnect()
	end
	table.clear(self.conns)
end

return Turret
```

Reference shapes for the other patterns: components on tagged Instances (connect the added/removed signals first, then sweep `GetTagged`; attach is idempotent; detach on tag removal); a pool with a lease contract (`acquire` hands out ownership, `release` accepts only leased parts, resets velocity and parent, idle cap destroys the surplus); a state store (`--!strict`, frozen immutable state, `get`/`set`/`subscribe` returning an unsubscribe function). [cold:rbx-arch/pattern-examples.md] read only when you must write a component (tags), pool or state-store implementation and want a reference shape.
Before release the caller ends hit handlers, tweens and delayed work. Before reuse restore transform, velocity, collision/query/touch flags, transparency, attributes, emitters and children. Idle objects must be inert. Define teardown for active leases, and reject, grow or degrade on exhaustion.

[cold:rbx-arch/pattern-examples.md] read only when you must write a component (tags), pool or state-store implementation and want a reference shape.
Server owns gameplay state; clients get a snapshot when ready, then diffs, with a sequence number to detect gaps. Never accept state from a client.

## Ownership map (fill for multi-system work)
| System | Owns | Writes | Reads | Replicates |
|---|---|---|---|---|
| Inventory | items | Inventory only | UI, Shop | owner client |

## Decision record
```
Area / feature:
Existing pattern:
Chosen: pattern + why (evidence)
Rejected: pattern + why
Migration boundary / rollback:
How verified: profile, test, playtest (state which)
```

## Related
rbx-luau (lifecycle and cleanup), rbx-perf (measure first), rbx-rojo, rbx-code-rate.

## Credit

Decision rules adapted in our own words from excaldev/ro-engineer (MIT). [cold:rbx-arch/credit.md] read only to verify the source or licence of these rules.