--!nocheck
local t = require("../../../../../systems/_check/harness")
local Leaderboard = require("../Leaderboard")

local clock, fetches, failing = 0, 0, false
local function make(extra)
	local cfg = {
		now = function()
			return clock
		end,
		ttl = 60,
		fetch = function(limit)
			fetches += 1
			if failing then
				return nil
			end
			local page = {}
			for i = 1, math.min(limit, 5) do
				table.insert(page, { key = "u" .. i, value = 100 - i })
			end
			return page
		end,
	}
	for k, v in extra or {} do
		cfg[k] = v
	end
	return Leaderboard.new(cfg)
end

t.test("top is cached for the ttl then refreshed", function()
	clock, fetches = 0, 0
	local b = make()
	b:top(3)
	b:top(3)
	t.eq(fetches, 1)
	clock = 60
	b:top(3)
	t.eq(fetches, 2)
end)

t.test("asking for a bigger page refetches, a smaller one does not", function()
	clock, fetches = 0, 0
	local b = make()
	t.eq(#b:top(2), 2)
	t.eq(#b:top(5), 5)
	t.eq(fetches, 2)
	t.eq(#b:top(3), 3)
	t.eq(fetches, 2)
end)

t.test("a failing fetch serves the stale page, or an empty one if there is none", function()
	clock, fetches, failing = 0, 0, true
	local b = make()
	t.eq(#b:top(3), 0)
	failing = false
	t.eq(#b:top(3), 3)
	clock, failing = 100, true
	t.eq(#b:top(3), 3)
	failing = false
end)

t.test("clean rejects negative, NaN, infinite, huge and non-numbers; floors fractions", function()
	local b = make()
	for _, bad in { -1, 0 / 0, math.huge, 1e13, "5", true } do
		t.eq(b:clean(bad), nil)
	end
	t.eq(b:clean(12.9), 12)
end)

t.test("shouldWrite needs improvement and respects the gap", function()
	clock = 1000
	local b = make()
	t.truthy(b:shouldWrite(1, 10))
	t.falsy(b:shouldWrite(1, 20))
	clock = 1031
	t.falsy(b:shouldWrite(1, 10))
	t.falsy(b:shouldWrite(1, -4))
	t.truthy(b:shouldWrite(1, 11))
	t.truthy(b:shouldWrite(2, 1))
end)

t.test("rank and short labels", function()
	local page = { { key = "a", value = 1 }, { key = "b", value = 1 } }
	t.eq(Leaderboard.rank(page, "b"), 2)
	t.eq(Leaderboard.rank(page, "z"), nil)
	t.eq(Leaderboard.short(999), "999")
	t.eq(Leaderboard.short(1500), "1.5K")
	t.eq(Leaderboard.short(2400000), "2.4M")
	t.eq(Leaderboard.short(150000), "150K")
end)

t.done()
