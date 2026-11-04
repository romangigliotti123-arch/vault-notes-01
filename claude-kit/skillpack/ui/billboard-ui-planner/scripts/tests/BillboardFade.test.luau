--!nocheck
local t = require("../../../../../systems/_check/harness")
local B = require("../BillboardFade")

t.test("transparency fades linearly between the two ranges", function()
	t.eq(B.transparency(10, 40, 60), 0)
	t.eq(B.transparency(50, 40, 60), 0.5)
	t.eq(B.transparency(90, 40, 60), 1)
	t.eq(B.transparency(10, 30, 30), 0)
	t.eq(B.transparency(31, 30, 30), 1)
end)
t.test("select keeps the nearest few within range", function()
	local _, list = B.select({
		{ id = "far", distance = 90 },
		{ id = "b", distance = 20 },
		{ id = "a", distance = 10 },
		{ id = "c", distance = 30 },
	}, { maxCount = 2, maxDistance = 60 })
	t.eq(list, { "a", "b" })
end)
t.test("priority beats distance", function()
	local _, list = B.select(
		{ { id = "near", distance = 5 }, { id = "npc", distance = 50, priority = 1 } },
		{ maxCount = 1, maxDistance = 60 }
	)
	t.eq(list, { "npc" })
end)
t.test("hysteresis keeps the previous one when two are nearly tied", function()
	local set = B.select(
		{ { id = "old", distance = 21 }, { id = "new", distance = 20 } },
		{ maxCount = 1, maxDistance = 60, previous = { old = true }, slack = 3 }
	)
	t.truthy(set.old)
	t.falsy(set.new)
end)
t.test("changes lists only what must be toggled", function()
	local on, off = B.changes({ a = true, b = true }, { b = true, c = true })
	t.eq(on, { "c" })
	t.eq(off, { "a" })
end)
t.done()
