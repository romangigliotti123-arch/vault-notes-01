--!nocheck
-- Run: lune run Graybox.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local Graybox = require("../Graybox")

local function box(name, x, z, sx, sz, role)
	return { name = name, x = x, y = 2, z = z, sx = sx, sy = 4, sz = sz, role = role }
end

t.test("a clean spec has no issues", function()
	local spec = { box("FloorA", 0, 0, 32, 32, "floor"), box("FloorB", 40, 0, 32, 32, "floor") }
	t.eq(#Graybox.validate(spec), 0)
end)

t.test("sizes and corners off the grid are flagged", function()
	local issues = Graybox.validate({ box("Odd", 0, 0, 30, 32, "floor") })
	t.truthy(#issues >= 1)
	t.eq(issues[1].kind, "grid")
end)

t.test("overlaps are flagged unless allowed", function()
	local a, b = box("A", 0, 0, 16, 16), box("B", 8, 0, 16, 16)
	t.eq(#Graybox.validate({ a, b }), 1)
	b.allowOverlap = true
	t.eq(#Graybox.validate({ a, b }), 0)
end)

t.test("touching boxes are not overlapping", function()
	t.eq(#Graybox.validate({ box("A", 0, 0, 16, 16), box("B", 16, 0, 16, 16) }), 0)
end)

t.test("doors need avatar clearance and corridors width", function()
	local door = { name = "Door", x = 2, y = 4, z = 2, sx = 4, sy = 8, sz = 4, role = "door" }
	t.eq(#Graybox.validate({ door }), 1)
	door.sy = 12
	t.eq(#Graybox.validate({ door }), 0)
	local corridor = box("Hall", 2, 0, 4, 32, "corridor")
	t.eq(#Graybox.validate({ corridor }), 1)
end)

t.test("duplicate names and zero sizes are flagged", function()
	local issues = Graybox.validate({ box("A", 0, 0, 16, 16), box("A", 100, 0, 16, 16) })
	t.eq(issues[1].kind, "name")
	t.eq(Graybox.validate({ box("Z", 0, 0, 0, 16) })[1].kind, "size")
end)

t.test("stats sum floor area", function()
	local s = Graybox.stats({ box("F", 0, 0, 16, 16, "floor"), box("W", 0, 0, 16, 4, "wall") })
	t.eq(s.floorArea, 256)
	t.eq(s.boxes, 2)
end)

t.done()
