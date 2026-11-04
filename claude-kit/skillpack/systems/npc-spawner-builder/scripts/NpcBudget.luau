--!strict
local NpcBudget = {}
NpcBudget.__index = NpcBudget

export type Pos = { x: number, y: number, z: number }
export type Config = {
	globalCap: number,
	zoneCap: { [string]: number },
	despawnDistance: number,
	aggroRange: number,
	leash: number,
}
export type NpcBudget = typeof(setmetatable(
	{} :: { _c: Config, _zone: { [string]: string }, _count: { [string]: number }, _total: number },
	NpcBudget
))

function NpcBudget.new(config: Config): NpcBudget
	assert(config.globalCap >= 1, "globalCap must be >= 1")
	assert(
		config.leash >= config.aggroRange,
		"leash must be at least the aggro range or NPCs give up as they notice you"
	)
	assert(config.despawnDistance > config.aggroRange, "despawnDistance must exceed aggroRange")
	return setmetatable({ _c = config, _zone = {}, _count = {}, _total = 0 }, NpcBudget)
end

function NpcBudget.canSpawn(self: NpcBudget, zone: string): boolean
	local cap = self._c.zoneCap[zone]
	if cap == nil or self._total >= self._c.globalCap then
		return false
	end
	return (self._count[zone] or 0) < cap
end

function NpcBudget.add(self: NpcBudget, id: string, zone: string): boolean
	if self._zone[id] ~= nil or not self:canSpawn(zone) then
		return false
	end
	self._zone[id] = zone
	self._count[zone] = (self._count[zone] or 0) + 1
	self._total += 1
	return true
end

function NpcBudget.remove(self: NpcBudget, id: string)
	local zone = self._zone[id]
	if zone then
		self._zone[id] = nil
		self._count[zone] -= 1
		self._total -= 1
	end
end

function NpcBudget.total(self: NpcBudget): number
	return self._total
end

local function dist(a: Pos, b: Pos): number
	local dx, dy, dz = a.x - b.x, a.y - b.y, a.z - b.z
	return math.sqrt(dx * dx + dy * dy + dz * dz)
end

function NpcBudget.sweep(self: NpcBudget, npcs: { [string]: Pos }, players: { Pos }): { string }
	local out = {}
	for id, pos in npcs do
		local near = false
		for _, p in players do
			if dist(pos, p) <= self._c.despawnDistance then
				near = true
				break
			end
		end
		if not near then
			table.insert(out, id)
		end
	end
	table.sort(out)
	return out
end

function NpcBudget.decide(self: NpcBudget, current: string, nearest: number?, home: number): string
	if home > self._c.leash then
		return "return"
	end
	if current == "return" then
		return if home <= 2 then "idle" else "return"
	end
	if nearest and nearest <= self._c.aggroRange then
		return "aggro"
	end
	return "idle"
end

return NpcBudget
