--!nocheck
-- Run: lune run TerrainPlan.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local TP = require("../TerrainPlan")

t.test("snap rounds to the 4 stud voxel grid", function()
	t.eq(TP.snap(10), 12)
	t.eq(TP.snap(9), 8)
	t.eq(TP.snap(0), 0)
end)

t.test("a 5x5 px area is a 20x20 stud cell", function()
	t.eq(TP.pxFor(20), 5)
	t.eq(TP.pxFor(21), 6)
end)

t.test("voxelCount rounds up per axis", function()
	t.eq(TP.voxelCount(8, 8, 8), 8)
	t.eq(TP.voxelCount(9, 4, 4), 3 * 1 * 1)
end)

t.test("a 2000x1000 stud map is one image", function()
	local p = TP.heightmap(2000, 1000)
	t.eq(p.pxW, 500)
	t.eq(p.pxD, 250)
	t.truthy(p.single)
end)

t.test("a 20000 stud map needs two tiles across and tile sizes add up", function()
	local p = TP.heightmap(20000, 4000)
	t.eq(p.pxW, 5000)
	t.falsy(p.single)
	t.eq(#p.tiles, 2)
	t.eq(p.tiles[1].pxW + p.tiles[2].pxW, 5000)
	t.eq(p.tiles[1].pxW, 4096)
end)

t.test("zero size is rejected", function()
	t.eq(pcall(TP.heightmap, 0, 10), false)
end)

t.test("work order includes water and roads only when asked", function()
	local a = TP.order(false, false)
	local b = TP.order(true, true)
	t.eq(#b, #a + 2)
end)

t.done()
