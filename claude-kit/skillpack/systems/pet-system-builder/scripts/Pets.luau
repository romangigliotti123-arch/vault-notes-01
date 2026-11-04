--!strict
local Pets = {}
Pets.__index = Pets

export type Data = { [any]: any }
export type Def = { power: number, next: string? }
export type Config = { inventory: any, defs: { [string]: Def }, equipLimit: number, fuseCount: number? }
export type Pets = typeof(setmetatable({} :: { _c: Config }, Pets))

function Pets.new(config: Config): Pets
	for id, def in config.defs do
		assert(def.power >= 0, `pet {id}: power must be >= 0`)
		if def.next then
			assert(config.defs[def.next] ~= nil, `pet {id}: next {def.next} is not defined`)
			assert(def.next ~= id, `pet {id}: next points at itself`)
		end
	end
	assert(config.equipLimit >= 1, "equipLimit must be at least 1")
	return setmetatable({ _c = config }, Pets)
end

function Pets.init(self: Pets, data: Data): Data
	local p = data.Pets
	if type(p) ~= "table" then
		p = { equipped = {} }
		data.Pets = p
	end
	p.equipped = p.equipped or {}
	for i = #p.equipped, 1, -1 do
		if self._c.inventory:findUid(data, p.equipped[i]) == nil then
			table.remove(p.equipped, i)
		end
	end
	return p
end

function Pets.isEquipped(self: Pets, data: Data, uid: string): boolean
	return table.find(self:init(data).equipped, uid) ~= nil
end

function Pets.locked(self: Pets, data: Data, uid: string): boolean
	return self:isEquipped(data, uid)
end

function Pets.equip(self: Pets, data: Data, uid: string): (boolean, string)
	local p = self:init(data)
	local slot = self._c.inventory:findUid(data, uid)
	if slot == nil or self._c.defs[slot.id] == nil then
		return false, "not a pet you own"
	end
	if table.find(p.equipped, uid) then
		return false, "already equipped"
	end
	if #p.equipped >= self._c.equipLimit then
		return false, "equip slots full"
	end
	table.insert(p.equipped, uid)
	return true, "ok"
end

function Pets.unequip(self: Pets, data: Data, uid: string): boolean
	local p = self:init(data)
	local i = table.find(p.equipped, uid)
	if i then
		table.remove(p.equipped, i)
		return true
	end
	return false
end

function Pets.power(self: Pets, data: Data, multiplier: number?): number
	local total = 0
	for _, uid in self:init(data).equipped do
		local slot = self._c.inventory:findUid(data, uid)
		if slot then
			total += self._c.defs[slot.id].power
		end
	end
	return total * (multiplier or 1)
end

function Pets.fuse(self: Pets, data: Data, id: string): (boolean, string)
	local def = self._c.defs[id]
	if def == nil or def.next == nil then
		return false, "cannot fuse this pet"
	end
	local need = self._c.fuseCount or 3
	local p = self:init(data)
	local picks: { string } = {}
	for _, uid in self._c.inventory:uids(data) do
		local slot = self._c.inventory:findUid(data, uid)
		if slot and slot.id == id and not table.find(p.equipped, uid) then
			table.insert(picks, uid)
			if #picks == need then
				break
			end
		end
	end
	if #picks < need then
		return false, "not enough unequipped pets"
	end
	for _, uid in picks do
		self._c.inventory:removeUid(data, uid)
	end
	local ok, why = self._c.inventory:add(data, def.next, 1)
	if not ok then
		for _ = 1, need do
			self._c.inventory:add(data, id, 1)
		end
		return false, why
	end
	return true, "ok"
end

return Pets
