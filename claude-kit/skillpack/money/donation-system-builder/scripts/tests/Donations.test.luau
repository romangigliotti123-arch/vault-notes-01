--!nocheck
local t = require("../../../../../systems/_check/harness")
local D = require("../Donations")

local cfg = { min = 10, max = 500, presets = { 10, 50, 100, 500 } }

t.test("valid preset passes", function()
	t.truthy(D.validate(cfg, 1, 2, 50))
end)

t.test("junk amounts are refused", function()
	for _, bad in { "50", 0 / 0, 12.5, -10, 5, 501, 75 } do
		t.falsy(D.validate(cfg, 1, 2, bad))
	end
end)

t.test("without presets any whole amount in range passes", function()
	t.truthy(D.validate({ min = 10, max = 500 }, 1, 2, 75))
end)

t.test("self donations are refused", function()
	t.eq(select(2, D.validate(cfg, 1, 1, 50)), "you cannot donate to yourself")
end)

t.test("the board counts a receipt once", function()
	local b = D.newBoard()
	t.truthy(D.add(b, "r1", 7, "Ann", 50))
	t.falsy(D.add(b, "r1", 7, "Ann", 50))
	t.eq(b.totals[7], 50)
end)

t.test("top sorts by total, ties by user id, and trims to n", function()
	local b = D.newBoard()
	D.add(b, "a", 3, "C", 100)
	D.add(b, "b", 1, "A", 100)
	D.add(b, "c", 2, "B", 300)
	D.add(b, "d", 1, "A", 10)
	local top = D.top(b, 2)
	t.eq(#top, 2)
	t.eq(top[1].userId, 2)
	t.eq(top[2].userId, 1)
	t.eq(top[2].total, 110)
	t.eq(#D.top(b, 99), 3)
end)

t.test("non-positive amounts cannot be added", function()
	t.falsy(pcall(D.add, D.newBoard(), "z", 1, "x", 0))
end)

t.done()
