<!-- cold: rbx-arch/pattern-examples.md | read when: read only when you must write a component (tags), pool or state-store implementation and want a reference shape. -->

## From skills/rbx-arch/SKILL.md :: Component on tagged Instances (connect first, then sweep; at

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

## From skills/rbx-arch/SKILL.md :: State store (immutable updates, unsubscribe returned):

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
