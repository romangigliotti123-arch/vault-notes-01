--!strict
-- Portals: the decisions around a hub's portals: which destinations exist (server whitelist; the client sends a NAME, never a place id),
-- per-player teleport cooldown, grouping a party into TeleportAsync batches, and retry/backoff for failures.
-- The glue calls TeleportService:TeleportAsync inside pcall and handles TeleportInitFailed; place ids of 0 mean SET IN CREATOR HUB.
--   local portals = Portals.new({ now = os.clock, maxGroup = 50, cooldown = 3, maxAttempts = 5,
--       destinations = { Forest = { placeId = 0, reserved = true, maxParty = 4 } } })
--   local plan = portals:plan("Forest", { 11, 12 })   -- { placeId=, reserved=, groups={ {11,12} } } or nil, reason
local Portals = {}
Portals.__index = Portals

export type Destination = { placeId: number, reserved: boolean?, maxParty: number? }
export type Config = {
	destinations: { [string]: Destination },
	now: () -> number,
	maxGroup: number?,
	cooldown: number,
	maxAttempts: number?,
}
export type Plan = { placeId: number, reserved: boolean, groups: { { number } } }
export type Portals = typeof(setmetatable({} :: { _c: Config, _last: { [number]: number } }, Portals))

function Portals.new(config: Config): Portals
	assert(config.cooldown >= 0, "cooldown must be >= 0")
	return setmetatable({ _c = config, _last = {} }, Portals)
end

function Portals.plan(self: Portals, destination: any, userIds: { number }): (Plan?, string)
	local dest = if type(destination) == "string" then self._c.destinations[destination] else nil
	if dest == nil then
		return nil, "unknown destination"
	end
	if dest.placeId == 0 then
		return nil, "place id not set (SET IN CREATOR HUB)"
	end
	if #userIds == 0 or #userIds > (dest.maxParty or 50) then
		return nil, "party size"
	end
	local now = self._c.now()
	for _, id in userIds do
		if now - (self._last[id] or -math.huge) < self._c.cooldown then
			return nil, "cooldown"
		end
	end
	local size = self._c.maxGroup or 50
	local groups: { { number } } = {}
	for i, id in userIds do
		local g = math.ceil(i / size)
		groups[g] = groups[g] or {}
		table.insert(groups[g], id)
	end
	for _, id in userIds do
		self._last[id] = now
	end
	return { placeId = dest.placeId, reserved = dest.reserved == true, groups = groups }, "ok"
end

-- seconds to wait before attempt n (1-based) or nil when out of attempts: 1, 2, 4, 8, 8 ...
function Portals.retryDelay(self: Portals, attempt: number): number?
	if attempt > (self._c.maxAttempts or 5) then
		return nil
	end
	return math.min(2 ^ (attempt - 1), 8)
end

-- release the cooldown after a failed teleport so the player can try again
function Portals.failed(self: Portals, userIds: { number })
	for _, id in userIds do
		self._last[id] = nil
	end
end

function Portals.forget(self: Portals, userId: number)
	self._last[userId] = nil
end

return Portals
