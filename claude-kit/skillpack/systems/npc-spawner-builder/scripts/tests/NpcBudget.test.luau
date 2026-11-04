--!nocheck
local t = require("../../../../../systems/_check/harness")
local NpcBudget = require("../NpcBudget")

local function make()
	return NpcBudget.new({
		globalCap = 3,
		zoneCap = { Forest = 2, Cave = 2 },
		despawnDistance = 100,
		aggroRange = 30,
		leash = 60,
	})
end

t.test("zone and global caps are enforced before spawning", function()
	local n = make()
	t.truthy(n:add("a", "Forest"))
	t.truthy(n:add("b", "Forest"))
	t.falsy(n:add("c", "Forest"))
	t.truthy(n:add("d", "Cave"))
	t.falsy(n:add("e", "Cave"))
	t.eq(n:total(), 3)
end)

t.test("unknown zones and duplicate ids are refused", function()
	local n = make()
	t.falsy(n:canSpawn("Moon"))
	n:add("a", "Forest")
	t.falsy(n:add("a", "Cave"))
end)

t.test("remove frees budget and is safe twice", function()
	local n = make()
	n:add("a", "Forest")
	n:add("b", "Forest")
	n:remove("a")
	n:remove("a")
	t.eq(n:total(), 1)
	t.truthy(n:add("c", "Forest"))
end)

t.test("sweep returns NPCs with no player nearby", function()
	local n = make()
	local npcs = { near = { x = 10, y = 0, z = 0 }, far = { x = 500, y = 0, z = 0 } }
	t.eq(n:sweep(npcs, { { x = 0, y = 0, z = 0 } }), { "far" })
	t.eq(n:sweep(npcs, {}), { "far", "near" })
end)

t.test("decide: aggro in range, leash forces return, return ends at home", function()
	local n = make()
	t.eq(n:decide("idle", 20, 5), "aggro")
	t.eq(n:decide("idle", 50, 5), "idle")
	t.eq(n:decide("aggro", 10, 70), "return")
	t.eq(n:decide("return", 10, 20), "return")
	t.eq(n:decide("return", 10, 1), "idle")
end)

t.test("inconsistent ranges are rejected", function()
	t.falsy(pcall(NpcBudget.new, { globalCap = 1, zoneCap = {}, despawnDistance = 100, aggroRange = 50, leash = 20 }))
	t.falsy(pcall(NpcBudget.new, { globalCap = 1, zoneCap = {}, despawnDistance = 40, aggroRange = 50, leash = 60 }))
end)

t.done()
