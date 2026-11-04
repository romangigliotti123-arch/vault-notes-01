--!nocheck
local t = require("../../../../../systems/_check/harness")
local Pivot = require("../Pivot")

local box = { min = { x = 0, y = 0, z = 0 }, max = { x = 10, y = 4, z = 6 } }

t.test("targets for each mode", function()
	t.eq(Pivot.target(box, "bottomCenter"), { x = 5, y = 0, z = 3 })
	t.eq(Pivot.target(box, "center"), { x = 5, y = 2, z = 3 })
	t.eq(Pivot.target(box, "bottomMinCorner"), { x = 0, y = 0, z = 0 })
end)

t.test("a pivot at the wanted point is ok", function()
	local d = Pivot.diagnose(box, { x = 5, y = 0, z = 3 }, "bottomCenter")
	t.truthy(d.ok)
	t.eq(d.distance, 0)
end)

t.test("a centred pivot is off by half the height for bottomCenter", function()
	local d = Pivot.diagnose(box, { x = 5, y = 2, z = 3 }, "bottomCenter")
	t.falsy(d.ok)
	t.eq(d.offset, { x = 0, y = -2, z = 0 })
	t.eq(d.distance, 2)
	t.falsy(d.outside)
end)

t.test("a pivot far outside the bounds is reported as outside", function()
	local d = Pivot.diagnose(box, { x = 500, y = 0, z = 3 }, "bottomCenter")
	t.truthy(d.outside)
	t.falsy(d.ok)
	t.truthy(string.find(d.note, "outside", 1, true))
end)

t.test("tolerance is respected", function()
	t.truthy(Pivot.diagnose(box, { x = 5.04, y = 0, z = 3 }, "bottomCenter", 0.1).ok)
	t.falsy(Pivot.diagnose(box, { x = 5.04, y = 0, z = 3 }, "bottomCenter", 0.01).ok)
end)

t.done()
