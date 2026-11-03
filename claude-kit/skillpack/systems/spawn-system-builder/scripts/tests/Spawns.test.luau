--!nocheck
-- Run from the kit's systems folder: lune run ../skillpack/systems/spawn-system-builder/scripts/tests/Spawns.test.luau
local t = require("../../../../../systems/_check/harness")
local Spawns = require("../Spawns")

local clock = 0
local function make()
	return Spawns.new({
		protectSeconds = 3,
		now = function()
			return clock
		end,
	})
end
local list = {
	{ id = "R1", team = "Red", pos = { x = 0, y = 0, z = 0 } },
	{ id = "R2", team = "Red", pos = { x = 100, y = 0, z = 0 } },
	{ id = "B1", team = "Blue", pos = { x = 50, y = 0, z = 0 } },
}

t.test("picks the team spawn farthest from enemies", function()
	local s = make()
	t.eq(s:pick(list, "Red", { { x = 5, y = 0, z = 0 } }).id, "R2")
	t.eq(s:pick(list, "Red", { { x = 95, y = 0, z = 0 } }).id, "R1")
end)

t.test("only the player's team spawns are used; no spawn gives nil", function()
	local s = make()
	t.eq(s:pick(list, "Blue", {}).id, "B1")
	t.eq(s:pick(list, "Green", {}), nil)
end)

t.test("with no enemies it rotates instead of reusing the last spawn", function()
	local s = make()
	local a = s:pick(list, "Red", {}).id
	local b = s:pick(list, "Red", {}).id
	t.truthy(a ~= b)
end)

t.test("protection lasts its window and ends when the player attacks", function()
	clock = 10
	local s = make()
	s:protect(7)
	t.truthy(s:isProtected(7))
	t.eq(s:damageFor(7, 25), 0)
	clock = 12.9
	t.truthy(s:isProtected(7))
	clock = 13
	t.falsy(s:isProtected(7))
	s:protect(7)
	s:attacked(7)
	t.eq(s:damageFor(7, 25), 25)
end)

t.test("long protection windows are rejected", function()
	t.falsy(pcall(Spawns.new, { protectSeconds = 60, now = os.clock }))
end)

t.done()
