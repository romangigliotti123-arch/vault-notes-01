--!nocheck
-- Run: lune run Pool.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local Pool = require("../Pool")

local function make(max, whenFull, prewarm)
	local made, resets = 0, 0
	local pool = Pool.new({
		create = function()
			made += 1
			return { id = made }
		end,
		reset = function()
			resets += 1
		end,
		max = max,
		whenFull = whenFull,
		prewarm = prewarm,
	})
	return pool, function()
		return made, resets
	end
end

t.test("Acquire creates until the cap, Release makes items reusable", function()
	local pool, counts = make(2)
	local a = pool:Acquire()
	local b = pool:Acquire()
	t.eq(pool:Acquire(), nil)
	t.truthy(pool:Release(a))
	local again = pool:Acquire()
	t.truthy(again == a)
	t.eq((counts()), 2)
	t.truthy(b ~= nil)
end)

t.test("double release and foreign items are refused", function()
	local pool = make(2)
	local a = pool:Acquire()
	t.truthy(pool:Release(a))
	t.falsy(pool:Release(a))
	t.falsy(pool:Release({ id = 99 }))
end)

t.test("prewarm fills the free list through reset, capped by max", function()
	local pool, counts = make(3, nil, 10)
	t.eq(pool:Stats().free, 3)
	local made, resets = counts()
	t.eq(made, 3)
	t.eq(resets, 3)
end)

t.test("recycleOldest reuses the oldest item in use when full", function()
	local pool = make(2, "recycleOldest")
	local a = pool:Acquire()
	local b = pool:Acquire()
	local c = pool:Acquire()
	t.truthy(c == a)
	t.truthy(b ~= c)
	t.eq(pool:Stats().recycled, 1)
	t.eq(pool:Stats().inUse, 2)
end)

t.test("refused acquires are counted when the policy is fail", function()
	local pool = make(1)
	pool:Acquire()
	pool:Acquire()
	pool:Acquire()
	t.eq(pool:Stats().refused, 2)
end)

t.test("Destroy hands every item to the destroy function and empties the pool", function()
	local pool = make(3, nil, 2)
	pool:Acquire()
	local destroyed = 0
	pool:Destroy(function()
		destroyed += 1
	end)
	t.eq(destroyed, 2)
	t.eq(pool:Stats().free, 0)
	t.eq(pool:Stats().inUse, 0)
end)

t.done()
