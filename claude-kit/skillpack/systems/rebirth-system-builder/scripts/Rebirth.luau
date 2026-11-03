--!strict
-- Rebirth (prestige): pay a growing cost, reset the progress you list, keep what you list, gain a permanent multiplier.
-- State: data.Rebirth = { count = n }. The reset runs on the server in one synchronous step. The client sends "rebirth" with the
-- count it SAW; a double click or a replayed request carries a stale count and is refused (no double reset, no double multiplier).
--   local rebirth = Rebirth.new({ wallet = wallet, currency = "Coins", baseCost = 1000, growth = 2.5,
--       gainPerRebirth = 0.5, maxRebirths = 50, reset = function(data) ... end })
--   rebirth:attempt(data, seenCount)
local Rebirth = {}
Rebirth.__index = Rebirth

export type Data = { [any]: any }
export type Config = {
	wallet: any,
	currency: string, -- the currency that pays the cost and is reset
	baseCost: number,
	growth: number, -- cost(n) = floor(baseCost * growth ^ n)
	gainPerRebirth: number, -- multiplier = 1 + count * gainPerRebirth (additive keeps late numbers readable)
	maxRebirths: number?,
	reset: (data: Data) -> (), -- reset everything that should reset (zones, tools, currency, ...); keep gems, passes, pets, badges
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

-- the multiplier you would have after the next rebirth (show it before the player confirms)
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
