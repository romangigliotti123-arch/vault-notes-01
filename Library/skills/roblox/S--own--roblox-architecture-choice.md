---
id: "roblox-architecture-choice"
type: skill
category: "roblox"
source: "own"
license: "first-party"
repo_path: "skills/roblox/roblox-architecture-choice/SKILL.md"
description: "Chooses how to structure a Roblox system (plain module, OOP class, CollectionService components, ECS, state store, object pool) by evidence: existing code, lifetimes, profiler data. Use for 'should I use ECS or OOP', 'pool these', or a new multi-system feature."
orig_name: "roblox-architecture-choice"
tags: [lib/skill, cat/roblox, src/own]
---

# roblox-architecture-choice

> Chooses how to structure a Roblox system (plain module, OOP class, CollectionService components, ECS, state store, object pool) by evidence: existing code, lifetimes, profiler data. Use for 'should I use ECS or OOP', 'pool these', or a new multi-system feature.

Type: skill | Category: [[categories/cat-roblox|roblox]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/roblox/roblox-architecture-choice/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[S--own--roblox-code-rate]], [[S--own--roblox-luau-style]], [[S--own--roblox-performance-pass]], [[S--own--roblox-rojo-project-setup]]

---
# Roblox architecture choice

Code comments: none by default (see roblox-luau-style, Comments).

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
1. Is there an existing pattern for this area? Use it.
2. Does it have its own lifetime (spawns, dies, owns connections)? OOP or components, else a module.
3. Is the same behaviour reused across unrelated things? Components over inheritance.
4. Do many systems share data? Store. Single reader: a local table.
5. Is allocation or destruction in the profile? Pool, and measure again afterwards.
6. ECS only after 1-5 and a benchmark of equivalent behaviour (same physics, fidelity, replication) on the target device.

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

Component on tagged Instances (connect first, then sweep; attach is idempotent):
```lua
--!strict
local CollectionService = game:GetService("CollectionService")

type Component = { Destroy: (Component) -> () }

local TAG = "Spinner"
local active: { [Instance]: Component } = {}

local function attach(inst: Instance)
	if active[inst] then
		return
	end
	active[inst] = {
		Destroy = function() end,
	}
end

local function detach(inst: Instance)
	local component = active[inst]
	if component then
		active[inst] = nil
		component:Destroy()
	end
end

CollectionService:GetInstanceAddedSignal(TAG):Connect(attach)
CollectionService:GetInstanceRemovedSignal(TAG):Connect(detach)
for _, inst in CollectionService:GetTagged(TAG) do
	attach(inst)
end
```

Pool with a lease contract (acquire hands out ownership, release accepts only leased parts, idle cap):
```lua
--!strict
local Pool = {}
Pool.__index = Pool

export type Pool = typeof(setmetatable(
	{} :: {
		template: BasePart,
		idle: { BasePart },
		leased: { [BasePart]: boolean },
		idleCap: number,
	},
	Pool
))

function Pool.new(template: BasePart, prewarm: number, idleCap: number): Pool
	local self = setmetatable({ template = template, idle = {}, leased = {}, idleCap = idleCap }, Pool)
	for _ = 1, prewarm do
		table.insert(self.idle, template:Clone())
	end
	return self
end

function Pool.acquire(self: Pool): BasePart
	local part = table.remove(self.idle) or self.template:Clone()
	self.leased[part] = true
	return part
end

function Pool.release(self: Pool, part: BasePart): boolean
	if not self.leased[part] then
		return false
	end
	self.leased[part] = nil
	part.Parent = nil
	part.AssemblyLinearVelocity = Vector3.zero
	if #self.idle >= self.idleCap then
		part:Destroy()
	else
		table.insert(self.idle, part)
	end
	return true
end

return Pool
```

Before release the caller ends hit handlers, tweens and delayed work. Before reuse restore transform, velocity, collision/query/touch flags, transparency, attributes, emitters and children. Idle objects must be inert. Define teardown for active leases, and reject, grow or degrade on exhaustion.

State store (immutable updates, unsubscribe returned):
```lua
--!strict
export type State = { coins: number, zone: string }
export type Store = {
	get: (Store) -> State,
	set: (Store, (State) -> State) -> (),
	subscribe: (Store, (State, State) -> ()) -> () -> (),
}

local function newStore(initial: State): Store
	local state = table.freeze(initial)
	local listeners: { [number]: (State, State) -> () } = {}
	local nextId = 0
	local store = {} :: Store
	store.get = function()
		return state
	end
	store.set = function(_, update)
		local old = state
		state = table.freeze(update(old))
		for _, fn in listeners do
			fn(state, old)
		end
	end
	store.subscribe = function(_, fn)
		nextId += 1
		local id = nextId
		listeners[id] = fn
		return function()
			listeners[id] = nil
		end
	end
	return store
end

return newStore
```

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
roblox-luau-style (lifecycle and cleanup), roblox-performance-pass (measure first), roblox-rojo-project-setup, roblox-code-rate.

## Credit
Decision rules adapted in our own words from excaldev/ro-engineer (MIT, Copyright (c) 2026 excaldev); reference copies under Imported/ro-engineer.
