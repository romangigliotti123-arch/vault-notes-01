--!strict
local Inventory = {}
Inventory.__index = Inventory

export type Data = { [any]: any }
export type ItemDef = { stack: number, tradable: boolean? }
export type Config = { capacity: number, items: { [string]: ItemDef }, newUid: () -> string, maxQty: number? }
export type Inventory = typeof(setmetatable({} :: { _c: Config }, Inventory))
export type Slot = { id: string, qty: number, uid: string? }

local DEFAULT_MAX_QTY = 1e6

function Inventory.new(config: Config): Inventory
	assert(
		config.capacity >= 1 and config.capacity == math.floor(config.capacity),
		"capacity must be a positive integer"
	)
	for id, def in config.items do
		assert(def.stack >= 1 and def.stack == math.floor(def.stack), `item {id}: stack must be a positive integer`)
	end
	return setmetatable({ _c = config }, Inventory)
end

function Inventory.init(self: Inventory, data: Data): Data
	local inv = data.Inventory
	if type(inv) ~= "table" then
		inv = { slots = {} }
		data.Inventory = inv
	end
	inv.slots = inv.slots or {}
	inv.cap = inv.cap or self._c.capacity
	return inv
end

local function validQty(self: Inventory, n: any): boolean
	return type(n) == "number" and n == n and n >= 1 and n <= (self._c.maxQty or DEFAULT_MAX_QTY) and n == math.floor(n)
end

function Inventory.count(self: Inventory, data: Data, id: string): number
	local inv = self:init(data)
	local total = 0
	for _, s in inv.slots do
		if s.id == id then
			total += s.qty
		end
	end
	return total
end

function Inventory.has(self: Inventory, data: Data, id: string, qty: number): boolean
	return self:count(data, id) >= qty
end

function Inventory.freeSlots(self: Inventory, data: Data): number
	local inv = self:init(data)
	local used = 0
	for _ in inv.slots do
		used += 1
	end
	return inv.cap - used
end

function Inventory.room(self: Inventory, data: Data, id: string): number
	local def = self._c.items[id]
	if def == nil then
		return 0
	end
	local inv = self:init(data)
	local room = self:freeSlots(data) * def.stack
	for _, s in inv.slots do
		if s.id == id and not s.uid then
			room += def.stack - s.qty
		end
	end
	return room
end

function Inventory.canAdd(self: Inventory, data: Data, id: string, qty: number): boolean
	return self._c.items[id] ~= nil and validQty(self, qty) and self:room(data, id) >= qty
end

function Inventory.add(self: Inventory, data: Data, id: string, qty: number, uid: string?): (boolean, string)
	local def = self._c.items[id]
	if def == nil then
		return false, "unknown item"
	end
	if not validQty(self, qty) then
		return false, "bad quantity"
	end
	if self:room(data, id) < qty then
		return false, "no room"
	end
	if uid ~= nil and (def.stack ~= 1 or qty ~= 1 or self:findUid(data, uid) ~= nil) then
		return false, "bad uid"
	end
	local inv = self:init(data)
	local left = qty
	if def.stack > 1 then
		for _, s in inv.slots do
			if left == 0 then
				break
			end
			if s.id == id and s.qty < def.stack then
				local put = math.min(left, def.stack - s.qty)
				s.qty += put
				left -= put
			end
		end
	end
	local i = 1
	while left > 0 do
		while inv.slots[i] ~= nil do
			i += 1
		end
		local put = math.min(left, def.stack)
		local slot: Slot = { id = id, qty = put }
		if def.stack == 1 then
			slot.uid = uid or self._c.newUid()
		end
		inv.slots[i] = slot
		left -= put
	end
	return true, "ok"
end

function Inventory.remove(self: Inventory, data: Data, id: string, qty: number): (boolean, string)
	if self._c.items[id] == nil then
		return false, "unknown item"
	end
	if not validQty(self, qty) then
		return false, "bad quantity"
	end
	if self:count(data, id) < qty then
		return false, "not enough"
	end
	local inv = self:init(data)
	local order = {}
	for i, s in inv.slots do
		if s.id == id then
			table.insert(order, i)
		end
	end
	table.sort(order, function(a, b)
		return inv.slots[a].qty < inv.slots[b].qty
	end)
	local left = qty
	for _, i in order do
		if left == 0 then
			break
		end
		local s = inv.slots[i]
		local take = math.min(left, s.qty)
		s.qty -= take
		left -= take
		if s.qty == 0 then
			inv.slots[i] = nil
		end
	end
	return true, "ok"
end

function Inventory.removeUid(self: Inventory, data: Data, uid: string): (boolean, string)
	local inv = self:init(data)
	for i, s in inv.slots do
		if s.uid == uid then
			inv.slots[i] = nil
			return true, "ok"
		end
	end
	return false, "not found"
end

function Inventory.findUid(self: Inventory, data: Data, uid: string): Slot?
	local inv = self:init(data)
	for _, s in inv.slots do
		if s.uid == uid then
			return s
		end
	end
	return nil
end

function Inventory.tradable(self: Inventory, id: string): boolean
	local def = self._c.items[id]
	return def ~= nil and def.tradable == true
end

function Inventory.uids(self: Inventory, data: Data): { string }
	local out = {}
	for _, s in self:init(data).slots do
		if s.uid then
			table.insert(out, s.uid)
		end
	end
	return out
end

function Inventory.validate(self: Inventory, data: Data): { string }
	local problems = {}
	local seenUid: { [string]: boolean } = {}
	local inv = self:init(data)
	for i, s in inv.slots do
		local def = self._c.items[s.id]
		if def == nil then
			table.insert(problems, `slot {i}: unknown item {tostring(s.id)}`)
		elseif type(s.qty) ~= "number" or s.qty < 1 or s.qty > def.stack or s.qty ~= math.floor(s.qty) then
			table.insert(problems, `slot {i}: bad quantity {tostring(s.qty)}`)
		elseif def.stack == 1 and not s.uid then
			table.insert(problems, `slot {i}: unique item without uid`)
		end
		if s.uid then
			if seenUid[s.uid] then
				table.insert(problems, `slot {i}: duplicate uid {s.uid}`)
			end
			seenUid[s.uid] = true
		end
		if type(i) ~= "number" or i < 1 or i > inv.cap then
			table.insert(problems, `slot {tostring(i)}: outside capacity`)
		end
	end
	return problems
end

return Inventory
