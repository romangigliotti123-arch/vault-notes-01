--!strict
local Wallet = {}
Wallet.__index = Wallet

export type Data = { [any]: any }
export type Def = { max: number?, start: number? }
export type Config = { currencies: { [string]: Def }, keyLimit: number?, maxChange: number? }
export type Wallet = typeof(setmetatable({} :: { _c: Config }, Wallet))

local DEFAULT_KEY_LIMIT = 200
local DEFAULT_MAX_CHANGE = 1e12

function Wallet.new(config: Config): Wallet
	for name, def in config.currencies do
		assert(type(name) == "string" and name ~= "", "currency needs a name")
		assert(def.max == nil or def.max > 0, `currency {name}: max must be positive`)
	end
	return setmetatable({ _c = config }, Wallet)
end

function Wallet.init(self: Wallet, data: Data): Data
	local w = data.Wallet
	if type(w) ~= "table" then
		w = { bal = {}, keys = {}, sources = {}, sinks = {} }
		data.Wallet = w
	end
	w.bal = w.bal or {}
	w.keys = w.keys or {}
	w.sources = w.sources or {}
	w.sinks = w.sinks or {}
	for name, def in self._c.currencies do
		if w.bal[name] == nil then
			w.bal[name] = def.start or 0
		end
	end
	return w
end

local function validAmount(self: Wallet, n: any): boolean
	local limit = self._c.maxChange or DEFAULT_MAX_CHANGE
	return type(n) == "number" and n == n and n > 0 and n <= limit and n == math.floor(n)
end

function Wallet.balance(self: Wallet, data: Data, name: string): number
	local w = self:init(data)
	return w.bal[name] or 0
end

local function seen(w: Data, key: string?): boolean
	if key == nil then
		return false
	end
	return table.find(w.keys, key) ~= nil
end

local function remember(self: Wallet, w: Data, key: string?)
	if key == nil then
		return
	end
	table.insert(w.keys, key)
	local limit = self._c.keyLimit or DEFAULT_KEY_LIMIT
	while #w.keys > limit do
		table.remove(w.keys, 1)
	end
end

function Wallet.add(
	self: Wallet,
	data: Data,
	name: string,
	amount: number,
	source: string,
	key: string?
): (boolean, string)
	local def = self._c.currencies[name]
	if def == nil then
		return false, "unknown currency"
	end
	if not validAmount(self, amount) then
		return false, "bad amount"
	end
	local w = self:init(data)
	if seen(w, key) then
		return true, "duplicate"
	end
	local cur: number = w.bal[name]
	local new = cur + amount
	local reason = "ok"
	if def.max and new > def.max then
		new = def.max
		reason = "capped"
	end
	w.bal[name] = new
	w.sources[source] = (w.sources[source] or 0) + (new - cur)
	remember(self, w, key)
	return true, reason
end

function Wallet.spend(
	self: Wallet,
	data: Data,
	name: string,
	amount: number,
	sink: string,
	key: string?
): (boolean, string)
	if self._c.currencies[name] == nil then
		return false, "unknown currency"
	end
	if not validAmount(self, amount) then
		return false, "bad amount"
	end
	local w = self:init(data)
	if seen(w, key) then
		return true, "duplicate"
	end
	if w.bal[name] < amount then
		return false, "insufficient"
	end
	w.bal[name] -= amount
	w.sinks[sink] = (w.sinks[sink] or 0) + amount
	remember(self, w, key)
	return true, "ok"
end

function Wallet.canAfford(self: Wallet, data: Data, name: string, amount: number): boolean
	return validAmount(self, amount) and self:balance(data, name) >= amount
end

function Wallet.report(self: Wallet, data: Data): { sources: { [string]: number }, sinks: { [string]: number } }
	local w = self:init(data)
	return { sources = w.sources, sinks = w.sinks }
end

return Wallet
