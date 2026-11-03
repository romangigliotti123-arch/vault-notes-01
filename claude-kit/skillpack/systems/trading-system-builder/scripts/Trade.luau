--!strict
-- Trade: server-authoritative, duplication-safe player-to-player trades on top of the kit's PlayerData data tables.
-- The client only ever sends "set my offer" (item ids/uids + coin count) and "accept"; the server owns the session, validates every
-- offer against the real inventories, and commits in ONE synchronous step (no yield between the check and the change) with a
-- snapshot rollback. Inventory and Wallet are the pack modules (inventory-system-builder, currency-system-builder), injected.
--   local trade = Trade.new({ inventory = inv, wallet = wallet, currency = "Coins", getData = ..., now = os.clock,
--       newId = function() return HttpService:GenerateGUID(false) end, lockSeconds = 5, maxItems = 8, log = print })
--   local id = trade:open(userA, userB)        -- nil if either is already trading
--   trade:setOffer(id, userA, { items = { { uid = "..." }, { id = "Wood", qty = 5 } }, coins = 10 })
--   trade:accept(id, userA, version) ; trade:accept(id, userB, version)    -- both accept the SAME version -> commit
local Trade = {}
Trade.__index = Trade

export type Data = { [any]: any }
export type OfferItem = { id: string?, qty: number?, uid: string? }
export type Offer = { items: { OfferItem }, coins: number }
export type Config = {
	inventory: any, -- Inventory object
	wallet: any, -- Wallet object
	currency: string,
	getData: (userId: number) -> Data?,
	now: () -> number,
	newId: () -> string,
	lockSeconds: number?, -- accept is refused this long after the last offer change (no bait-and-switch)
	maxItems: number?, -- offer lines per side (default 8)
	maxCoins: number?, -- per trade (default 1e6)
	locked: ((data: Data, uid: string) -> boolean)?, -- e.g. equipped pets: a locked uid cannot be offered
	log: ((entry: { [string]: any }) -> ())?,
}
type Session = {
	id: string,
	a: number,
	b: number,
	offers: { [number]: Offer },
	accepted: { [number]: boolean },
	version: number,
	changedAt: number,
	state: "open" | "done" | "cancelled",
}
export type Trade = typeof(setmetatable(
	{} :: { _c: Config, _s: { [string]: Session }, _by: { [number]: string } },
	Trade
))

local function deepCopy(v: any): any
	if type(v) ~= "table" then
		return v
	end
	local out = {}
	for k, x in v do
		out[k] = deepCopy(x)
	end
	return out
end

function Trade.new(config: Config): Trade
	return setmetatable({ _c = config, _s = {}, _by = {} }, Trade)
end

local function finish(self: Trade, s: Session, state: "done" | "cancelled")
	s.state = state
	self._by[s.a] = nil
	self._by[s.b] = nil
	self._s[s.id] = nil
end

function Trade.open(self: Trade, a: number, b: number): string?
	if a == b or self._by[a] or self._by[b] then
		return nil
	end
	if self._c.getData(a) == nil or self._c.getData(b) == nil then
		return nil
	end
	local id = self._c.newId()
	local s: Session = {
		id = id,
		a = a,
		b = b,
		offers = { [a] = { items = {}, coins = 0 }, [b] = { items = {}, coins = 0 } },
		accepted = { [a] = false, [b] = false },
		version = 0,
		changedAt = self._c.now(),
		state = "open",
	}
	self._s[id] = s
	self._by[a] = id
	self._by[b] = id
	return id
end

function Trade.sessionOf(self: Trade, userId: number): string?
	return self._by[userId]
end

-- resolve an offer against the owner's real inventory; returns the concrete lines or a reason. Never trusts client numbers.
local function resolve(self: Trade, userId: number, offer: Offer): ({ OfferItem }?, string)
	local data = self._c.getData(userId)
	if data == nil then
		return nil, "no data"
	end
	local inv = self._c.inventory
	local lines: { OfferItem } = {}
	local usedUid: { [string]: boolean } = {}
	local need: { [string]: number } = {}
	if #offer.items > (self._c.maxItems or 8) then
		return nil, "too many lines"
	end
	for _, it in offer.items do
		if type(it) ~= "table" then
			return nil, "bad line"
		end
		if it.uid ~= nil then
			if type(it.uid) ~= "string" or usedUid[it.uid] then
				return nil, "bad uid"
			end
			local slot = inv:findUid(data, it.uid)
			if slot == nil then
				return nil, "uid not owned"
			end
			if not inv:tradable(slot.id) then
				return nil, "not tradable"
			end
			if self._c.locked and self._c.locked(data, it.uid) then
				return nil, "item is locked"
			end
			usedUid[it.uid] = true
			table.insert(lines, { id = slot.id, qty = 1, uid = it.uid })
		else
			if type(it.id) ~= "string" or not inv:tradable(it.id) then
				return nil, "not tradable"
			end
			local q = it.qty
			if type(q) ~= "number" or q ~= q or q < 1 or q ~= math.floor(q) or q > 1e6 then
				return nil, "bad quantity"
			end
			need[it.id] = (need[it.id] or 0) + q
			table.insert(lines, { id = it.id, qty = q })
		end
	end
	for id, q in need do
		if inv:count(data, id) < q then
			return nil, "not enough " .. id
		end
	end
	local coins = offer.coins
	if
		type(coins) ~= "number"
		or coins ~= coins
		or coins < 0
		or coins ~= math.floor(coins)
		or coins > (self._c.maxCoins or 1e6)
	then
		return nil, "bad coins"
	end
	if coins > 0 and not self._c.wallet:canAfford(data, self._c.currency, coins) then
		return nil, "not enough coins"
	end
	return lines, "ok"
end

-- replaces the user's whole offer; resets both accepts and bumps the version
function Trade.setOffer(self: Trade, id: string, userId: number, offer: Offer): (boolean, string)
	local s = self._s[id]
	if s == nil or (userId ~= s.a and userId ~= s.b) then
		return false, "no such trade"
	end
	local lines, why = resolve(self, userId, offer)
	if lines == nil then
		return false, why
	end
	s.offers[userId] = { items = lines, coins = offer.coins }
	s.accepted[s.a] = false
	s.accepted[s.b] = false
	s.version += 1
	s.changedAt = self._c.now()
	return true, "ok"
end

function Trade.version(self: Trade, id: string): number?
	local s = self._s[id]
	return s and s.version
end

function Trade.cancel(self: Trade, id: string, reason: string?)
	local s = self._s[id]
	if s then
		finish(self, s, "cancelled")
		if self._c.log then
			self._c.log({ event = "trade_cancelled", id = id, a = s.a, b = s.b, reason = reason or "cancel" })
		end
	end
end

-- call from PlayerRemoving: a leaving player cancels their trade (before the data is released)
function Trade.playerLeft(self: Trade, userId: number)
	local id = self._by[userId]
	if id then
		self:cancel(id, "player left")
	end
end

local function takeSide(self: Trade, fromData: Data, offer: Offer): boolean
	local inv, wallet = self._c.inventory, self._c.wallet
	for _, line in offer.items do
		if line.uid then
			if not inv:removeUid(fromData, line.uid :: string) then
				return false
			end
		elseif not inv:remove(fromData, line.id :: string, line.qty :: number) then
			return false
		end
	end
	if offer.coins > 0 and not wallet:spend(fromData, self._c.currency, offer.coins, "trade") then
		return false
	end
	return true
end

-- the original uid travels with the item, so one item is never two different records
local function giveSide(self: Trade, toData: Data, offer: Offer): boolean
	local inv, wallet = self._c.inventory, self._c.wallet
	for _, line in offer.items do
		if not inv:add(toData, line.id :: string, line.qty :: number, line.uid) then
			return false
		end
	end
	if offer.coins > 0 and not wallet:add(toData, self._c.currency, offer.coins, "trade") then
		return false
	end
	return true
end

-- accept at a given offer version. When both sides accepted the same version the trade commits. Returns state: "waiting", "done" or an error reason.
function Trade.accept(self: Trade, id: string, userId: number, version: number): (string, string?)
	local s = self._s[id]
	if s == nil or (userId ~= s.a and userId ~= s.b) then
		return "error", "no such trade"
	end
	if version ~= s.version then
		return "error", "offer changed"
	end
	if self._c.now() - s.changedAt < (self._c.lockSeconds or 0) then
		return "error", "locked"
	end
	s.accepted[userId] = true
	if not (s.accepted[s.a] and s.accepted[s.b]) then
		return "waiting"
	end
	local da, db = self._c.getData(s.a), self._c.getData(s.b)
	if da == nil or db == nil then
		self:cancel(id, "data missing")
		return "error", "data missing"
	end
	-- re-validate against the CURRENT inventories (they may have changed since the offers were set)
	local la, wa = resolve(self, s.a, s.offers[s.a])
	local lb, wb = resolve(self, s.b, s.offers[s.b])
	if la == nil or lb == nil then
		self:cancel(id, "revalidation failed: " .. (la == nil and wa or wb))
		return "error", "revalidation failed"
	end
	-- commit with rollback: nothing below yields
	local snapA, snapB = deepCopy(da.Inventory), deepCopy(db.Inventory)
	local walA, walB = deepCopy(da.Wallet), deepCopy(db.Wallet)
	local offA: Offer = { items = la, coins = s.offers[s.a].coins }
	local offB: Offer = { items = lb, coins = s.offers[s.b].coins }
	local ok = takeSide(self, da, offA)
		and takeSide(self, db, offB)
		and giveSide(self, db, offA)
		and giveSide(self, da, offB)
	if not ok then
		da.Inventory, db.Inventory, da.Wallet, db.Wallet = snapA, snapB, walA, walB
		self:cancel(id, "commit failed (no room?)")
		return "error", "commit failed"
	end
	finish(self, s, "done")
	if self._c.log then
		self._c.log({ event = "trade_done", id = id, a = s.a, b = s.b, gaveA = offA, gaveB = offB })
	end
	return "done"
end

return Trade
