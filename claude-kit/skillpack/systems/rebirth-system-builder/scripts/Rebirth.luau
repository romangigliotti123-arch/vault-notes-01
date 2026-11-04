--!strict
local Rebirth = {}
Rebirth.__index = Rebirth

export type Data = { [any]: any }
export type Config = {
	wallet: any,
	currency: string,
	baseCost: number,
	growth: number,
	gainPerRebirth: number,
	maxRebirths: number?,
	reset: (data: Data) -> (),
	log: ((string) -> ())?,
}
export type Rebirth = typeof(setmetatable({} :: { _c: Config }, Rebirth))

function Rebirth.new(config: Config): Rebirth
	assert(config.baseCost >= 1, "baseCost must be >= 1")
	assert(config.growth >= 1, "growth must be >= 1 (a falling cost makes rebirth free)")
	assert(config.gainPerRebirth > 0, "gainPerRebirth must be > 0 (otherwise rebirth is a pure loss)")
	return setmetatable({ _c = config }, Rebirth)
end

function Rebirth.count(_self: Rebirth, data: Data): number
	local r = data.Rebirth
	if type(r) ~= "table" then
		r = { count = 0 }
		data.Rebirth = r
	end
	return r.count
end

function Rebirth.cost(self: Rebirth, count: number): number
	return math.floor(self._c.baseCost * self._c.growth ^ count)
end

function Rebirth.multiplier(self: Rebirth, data: Data): number
	return 1 + self:count(data) * self._c.gainPerRebirth
end

function Rebirth.nextMultiplier(self: Rebirth, data: Data): number
	return 1 + (self:count(data) + 1) * self._c.gainPerRebirth
end

function Rebirth.attempt(self: Rebirth, data: Data, seenCount: number): (boolean, string)
	local n = self:count(data)
	if seenCount ~= n then
		return false, "stale request"
	end
	if self._c.maxRebirths and n >= self._c.maxRebirths then
		return false, "max rebirths"
	end
	local cost = self:cost(n)
	if not self._c.wallet:canAfford(data, self._c.currency, cost) then
		return false, "cannot afford"
	end
	local ok = self._c.wallet:spend(data, self._c.currency, cost, "rebirth")
	if not ok then
		return false, "cannot afford"
	end
	self._c.reset(data)
	data.Rebirth.count = n + 1
	if self._c.log then
		self._c.log(`rebirth {n + 1} cost {cost}`)
	end
	return true, "ok"
end

return Rebirth
