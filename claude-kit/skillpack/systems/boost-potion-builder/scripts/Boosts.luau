--!strict
local Boosts = {}
Boosts.__index = Boosts

export type Data = { [any]: any }
export type Def = { group: string, mult: number, seconds: number, maxSeconds: number }
export type Group = { mode: "add" | "max", cap: number }
export type Config = { defs: { [string]: Def }, groups: { [string]: Group }, now: () -> number }
export type Boosts = typeof(setmetatable({} :: { _c: Config }, Boosts))

function Boosts.new(config: Config): Boosts
	for name, d in config.defs do
		assert(config.groups[d.group] ~= nil, `boost {name}: unknown group {d.group}`)
		assert(d.mult > 1, `boost {name}: mult must be > 1`)
		assert(d.seconds > 0 and d.maxSeconds >= d.seconds, `boost {name}: seconds > 0 and maxSeconds >= seconds`)
	end
	for g, grp in config.groups do
		assert(grp.cap >= 1, `group {g}: cap must be >= 1`)
	end
	return setmetatable({ _c = config }, Boosts)
end

function Boosts.init(self: Boosts, data: Data): Data
	local b = data.Boosts
	if type(b) ~= "table" then
		b = {}
		data.Boosts = b
	end
	local now = self._c.now()
	for name, exp in b do
		if self._c.defs[name] == nil or type(exp) ~= "number" or exp <= now then
			b[name] = nil
		end
	end
	return b
end

function Boosts.grant(self: Boosts, data: Data, name: string): number?
	local def = self._c.defs[name]
	if def == nil then
		return nil
	end
	local b = self:init(data)
	local now = self._c.now()
	local base = math.max(now, b[name] or 0)
	b[name] = math.min(base + def.seconds, now + def.maxSeconds)
	return b[name]
end

function Boosts.multiplier(self: Boosts, data: Data, group: string): number
	local grp = self._c.groups[group]
	if grp == nil then
		return 1
	end
	local b = self:init(data)
	local result = 1
	for name in b do
		local d = self._c.defs[name]
		if d.group == group then
			if grp.mode == "add" then
				result += d.mult - 1
			else
				result = math.max(result, d.mult)
			end
		end
	end
	return math.min(result, grp.cap)
end

function Boosts.active(self: Boosts, data: Data): { { name: string, left: number, mult: number } }
	local now = self._c.now()
	local out = {}
	for name, exp in self:init(data) do
		table.insert(out, { name = name, left = exp - now, mult = self._c.defs[name].mult })
	end
	table.sort(out, function(a, b)
		return a.left < b.left
	end)
	return out
end

return Boosts
