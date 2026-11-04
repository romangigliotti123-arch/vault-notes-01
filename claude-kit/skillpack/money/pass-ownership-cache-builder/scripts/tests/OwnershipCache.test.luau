--!nocheck
local t = require("../../../../../systems/_check/harness")
local OwnershipCache = require("../OwnershipCache")

local function make(over)
	local env = { owned = {}, fetches = 0, errors = 0, clock = 0, waits = {} }
	local cfg = {
		fetch = function(u, p)
			env.fetches += 1
			if env.errors > 0 then
				env.errors -= 1
				error("http 500")
			end
			return env.owned[u .. ":" .. p] == true
		end,
		now = function()
			return env.clock
		end,
		wait = function(s)
			table.insert(env.waits, s)
		end,
		ttl = 100,
	}
	for k, v in over or {} do
		cfg[k] = v
	end
	return OwnershipCache.new(cfg), env
end

t.test("second lookup inside the ttl is served from cache", function()
	local c, env = make()
	env.owned["1:9"] = true
	local a, sa = OwnershipCache.get(c, 1, 9)
	local b, sb = OwnershipCache.get(c, 1, 9)
	t.eq(a, true)
	t.eq(sa, "fresh")
	t.eq(sb, "cached")
	t.eq(b, true)
	t.eq(env.fetches, 1)
end)

t.test("after the ttl it asks Roblox again (a refund is eventually seen)", function()
	local c, env = make()
	env.owned["1:9"] = true
	OwnershipCache.get(c, 1, 9)
	env.owned["1:9"] = nil
	env.clock = 101
	local owned, status = OwnershipCache.get(c, 1, 9)
	t.eq(owned, false)
	t.eq(status, "fresh")
end)

t.test("a failing fetch is retried with backoff and then succeeds", function()
	local c, env = make()
	env.owned["1:9"] = true
	env.errors = 2
	local owned, status = OwnershipCache.get(c, 1, 9)
	t.eq(owned, true)
	t.eq(status, "fresh")
	t.eq(#env.waits, 2)
end)

t.test("total failure with history falls back to the stale answer", function()
	local c, env = make()
	env.owned["1:9"] = true
	OwnershipCache.get(c, 1, 9)
	env.clock = 500
	env.errors = 99
	local owned, status = OwnershipCache.get(c, 1, 9)
	t.eq(owned, true)
	t.eq(status, "stale")
end)

t.test("total failure without history says unknown and false, never throws", function()
	local c, env = make()
	env.errors = 99
	local owned, status = OwnershipCache.get(c, 1, 9)
	t.eq(owned, false)
	t.eq(status, "unknown")
end)

t.test("a spoofed wasPurchased=true is ignored when Roblox says not owned", function()
	local c = make()
	t.eq(OwnershipCache.onPromptFinished(c, 1, 9, true), false)
end)

t.test("a real purchase replaces a cached 'not owned'", function()
	local c, env = make()
	t.eq(OwnershipCache.get(c, 1, 9), false)
	env.owned["1:9"] = true
	t.eq(OwnershipCache.onPromptFinished(c, 1, 9, true), true)
	t.eq(OwnershipCache.get(c, 1, 9), true)
end)

t.test("clearPlayer forgets only that player", function()
	local c, env = make()
	env.owned["1:9"] = true
	env.owned["2:9"] = true
	OwnershipCache.get(c, 1, 9)
	OwnershipCache.get(c, 2, 9)
	OwnershipCache.clearPlayer(c, 1)
	local before = env.fetches
	OwnershipCache.get(c, 2, 9)
	t.eq(env.fetches, before)
	OwnershipCache.get(c, 1, 9)
	t.eq(env.fetches, before + 1)
end)

t.done()
