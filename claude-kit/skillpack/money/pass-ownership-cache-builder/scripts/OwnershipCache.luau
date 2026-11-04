--!strict
local OwnershipCache = {}

export type Config = {
	fetch: (userId: number, passId: number) -> boolean,
	now: () -> number,
	ttl: number?,
	attempts: number?,
	wait: ((seconds: number) -> ())?,
}
type Entry = { owned: boolean, at: number }
export type Cache = { _c: Config, _e: { [string]: Entry } }
export type Status = "fresh" | "cached" | "stale" | "unknown"

function OwnershipCache.new(cfg: Config): Cache
	return { _c = cfg, _e = {} }
end

local function key(userId: number, passId: number): string
	return `{userId}:{passId}`
end

local function lookup(cache: Cache, userId: number, passId: number): boolean?
	local c = cache._c
	for attempt = 1, c.attempts or 3 do
		local ok, owns = pcall(c.fetch, userId, passId)
		if ok then
			cache._e[key(userId, passId)] = { owned = owns == true, at = c.now() }
			return owns == true
		end
		if c.wait and attempt < (c.attempts or 3) then
			c.wait(attempt)
		end
	end
	return nil
end

function OwnershipCache.get(cache: Cache, userId: number, passId: number): (boolean, Status)
	local e = cache._e[key(userId, passId)]
	if e and cache._c.now() - e.at < (cache._c.ttl or 300) then
		return e.owned, "cached"
	end
	local fresh = lookup(cache, userId, passId)
	if fresh ~= nil then
		return fresh, "fresh"
	end
	if e then
		return e.owned, "stale"
	end
	return false, "unknown"
end

function OwnershipCache.onPromptFinished(cache: Cache, userId: number, passId: number, _wasPurchased: boolean): boolean
	cache._e[key(userId, passId)] = nil
	local owned = OwnershipCache.get(cache, userId, passId)
	return owned
end

function OwnershipCache.clearPlayer(cache: Cache, userId: number)
	local prefix = `{userId}:`
	for k in cache._e do
		if string.sub(k, 1, #prefix) == prefix then
			cache._e[k] = nil
		end
	end
end

return OwnershipCache
