--!strict
-- Vehicles: the ownership and lifecycle rules for spawned vehicles: a per-player vehicle limit, spawn cooldown, who may drive
-- (the owner, or anyone in the owner's allowed set), seat claiming, and a sweep that removes abandoned vehicles. Pure logic;
-- the glue creates the model, calls SetNetworkOwner(driver) on the chassis only while seated, and destroys on sweep.
--   local v = Vehicles.new({ maxPerPlayer = 1, spawnCooldown = 5, abandonSeconds = 120, seats = 2, now = os.clock })
--   local id = v:spawn(userId) ; v:sit(id, userId, 1) ; v:leaveSeat(id, userId) ; for _, dead in v:sweep(present) do destroy(dead) end
local Vehicles = {}
Vehicles.__index = Vehicles

export type Config = {
	maxPerPlayer: number,
	spawnCooldown: number,
	abandonSeconds: number,
	seats: number,
	now: () -> number,
	newId: (() -> string)?,
}
type Vehicle = { owner: number, seatsTaken: { [number]: number }, lastUsed: number }
export type Vehicles = typeof(setmetatable(
	{} :: { _c: Config, _v: { [string]: Vehicle }, _lastSpawn: { [number]: number }, _n: number },
	Vehicles
))

function Vehicles.new(config: Config): Vehicles
	assert(config.maxPerPlayer >= 1 and config.seats >= 1 and config.abandonSeconds > 0, "bad vehicle config")
	return setmetatable({ _c = config, _v = {}, _lastSpawn = {}, _n = 0 }, Vehicles)
end

function Vehicles.countOf(self: Vehicles, userId: number): number
	local n = 0
	for _, v in self._v do
		if v.owner == userId then
			n += 1
		end
	end
	return n
end

-- returns the new vehicle id or nil, reason. Spawning past the limit is refused (or replaces: call despawnOwned first in the glue).
function Vehicles.spawn(self: Vehicles, userId: number): (string?, string)
	local now = self._c.now()
	if now - (self._lastSpawn[userId] or -math.huge) < self._c.spawnCooldown then
		return nil, "cooldown"
	end
	if self:countOf(userId) >= self._c.maxPerPlayer then
		return nil, "limit"
	end
	self._n += 1
	local id = if self._c.newId then self._c.newId() else "v" .. self._n
	self._v[id] = { owner = userId, seatsTaken = {}, lastUsed = now }
	self._lastSpawn[userId] = now
	return id, "ok"
end

-- seat 1 is the driver seat: only the owner may take it. Other seats are free for anyone.
function Vehicles.sit(self: Vehicles, id: string, userId: number, seat: any): (boolean, string)
	local v = self._v[id]
	if v == nil then
		return false, "no such vehicle"
	end
	if type(seat) ~= "number" or seat ~= math.floor(seat) or seat < 1 or seat > self._c.seats then
		return false, "bad seat"
	end
	if v.seatsTaken[seat] ~= nil then
		return false, "seat taken"
	end
	for s, u in v.seatsTaken do
		if u == userId then
			return false, "already seated in " .. s
		end
	end
	if seat == 1 and v.owner ~= userId then
		return false, "not the owner"
	end
	v.seatsTaken[seat] = userId
	v.lastUsed = self._c.now()
	return true, "ok"
end

function Vehicles.leaveSeat(self: Vehicles, id: string, userId: number)
	local v = self._v[id]
	if v then
		for s, u in v.seatsTaken do
			if u == userId then
				v.seatsTaken[s] = nil
				v.lastUsed = self._c.now()
			end
		end
	end
end

function Vehicles.driver(self: Vehicles, id: string): number?
	local v = self._v[id]
	return v and v.seatsTaken[1]
end

function Vehicles.remove(self: Vehicles, id: string)
	self._v[id] = nil
end

-- vehicles to destroy: owner left the server (present[owner] ~= true) and nobody is seated, or empty for abandonSeconds
function Vehicles.sweep(self: Vehicles, present: { [number]: boolean }): { string }
	local now = self._c.now()
	local out = {}
	for id, v in self._v do
		local occupied = next(v.seatsTaken) ~= nil
		if not occupied and (not present[v.owner] or now - v.lastUsed >= self._c.abandonSeconds) then
			table.insert(out, id)
		end
	end
	table.sort(out)
	for _, id in out do
		self._v[id] = nil
	end
	return out
end

return Vehicles
