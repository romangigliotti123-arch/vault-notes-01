--!nocheck
-- Run: lune run PropKit.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local PK = require("../PropKit")

local kit = {
	{ name = "tree", variants = 3, instancesPer = 12, per1000 = 2 },
	{ name = "rock", variants = 2, instancesPer = 2, per1000 = 5 },
}

t.test("placed counts follow area and density", function()
	local r = PK.plan(100000, kit)
	t.eq(r.placed.tree, 200)
	t.eq(r.placed.rock, 500)
	t.eq(r.instances, 200 * 12 + 500 * 2)
	t.eq(r.uniqueMeshes, 5)
end)

t.test("load time and memory use the vault estimates", function()
	local r = PK.plan(100000, kit)
	t.truthy(math.abs(r.loadSeconds - 0.34) < 1e-9)
	t.truthy(math.abs(r.clientMB - 3400 * 500 / 1048576) < 1e-9)
end)

t.test("going over the instance guide raises an issue", function()
	local r = PK.plan(100000, kit, 3000)
	t.eq(#r.issues, 1)
	t.eq(#PK.plan(100000, kit).issues, 0)
end)

t.test("more variants than placed copies is flagged", function()
	local r = PK.plan(1000, { { name = "statue", variants = 5, instancesPer = 30, per1000 = 2 } })
	t.eq(#r.issues, 1)
end)

t.test("reuse ratio is copies per unique mesh", function()
	local r = PK.plan(100000, kit)
	t.eq(PK.reuse(r), 700 / 5)
	t.eq(PK.reuse(PK.plan(1000, {})), 0)
end)

t.done()
