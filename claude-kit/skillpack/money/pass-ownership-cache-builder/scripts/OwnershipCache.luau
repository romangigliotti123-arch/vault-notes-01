--!strict
-- OwnershipCache: cache "does this player own this pass?" for perk checks, with retries, a stale fallback and refresh on purchase.
-- The answer always comes from Roblox (`fetch` = a wrapper around MarketplaceService:UserOwnsGamePassAsync); the client never supplies it.
-- If you already use the kit's Shop system, ShopService.HasPass does this for the passes in its catalogue: use that and skip this module.
--   local cache = OwnershipCache.new({ fetch = function(userId, passId) return Marketplace:UserOwnsGamePassAsync(userId, passId) end, now = os.clock, wait = task.wait })
--   local owned, status = OwnershipCache.get(cache, userId, passId)       -- status: "fresh" | "cached" | "stale" | "unknown"
--   -- PromptGamePassPurchaseFinished: OwnershipCache.onPromptFinished(cache, userId, passId, wasPurchased)   (wasPurchased is NOT trusted)
local OwnershipCache = {}

export type Config = {
	fetch: (userId: number, passId: number) -> boolean, -- may error (HTTP failures happen)
	now: () -> number,
	ttl: number?, -- seconds a result is trusted (default 300) so refunds and revokes are eventually seen
	attempts: number?, -- fetch tries per lookup (default 3)
	wait: ((seconds: number) -> ())?, -- backoff between tries (default none)
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

-- Returns (owned, status). On total failure it falls back to the last known answer ("stale") or false ("unknown"); never throws.
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

-- Purchase prompt closed: forget the old answer and ask Roblox again whatever `wasPurchased` says (it can be wrong or spoofed).
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
