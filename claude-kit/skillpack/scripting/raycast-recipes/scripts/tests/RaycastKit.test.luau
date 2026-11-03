--!nocheck
-- Run: lune run RaycastKit.test.luau   (from the kit's systems folder, see check-scripts.sh)
-- Uses Lune's roblox library for Vector3 and a fake world; the real engine casts are not exercised.
local roblox = require("@lune/roblox")
local t = require("../../../../../systems/_check/harness")
local RaycastKit = require("../RaycastKit")
local V = roblox.Vector3

local function fakeWorld(hitAtX)
	local world = { calls = {} }
	function world.Raycast(_, origin, direction)
		table.insert(world.calls, { origin = origin, direction = direction })
		if hitAtX and origin.X <= hitAtX and origin.X + direction.X >= hitAtX then
			return { Position = V.new(hitAtX, 0, 0) }
		end
		return nil
	end
	return world
end

t.test("cast passes the vectors through and clamps to 15000 studs", function()
	local w = fakeWorld()
	RaycastKit.world = w
	RaycastKit.cast(V.new(0, 0, 0), V.new(100, 0, 0))
	t.eq(w.calls[1].direction.Magnitude, 100)
	RaycastKit.cast(V.new(0, 0, 0), V.new(50000, 0, 0))
	t.eq(math.floor(w.calls[2].direction.Magnitude + 0.5), 15000)
end)

t.test("lineOfSight is true when nothing is hit and false when blocked", function()
	RaycastKit.world = fakeWorld()
	t.truthy(RaycastKit.lineOfSight(V.new(0, 0, 0), V.new(10, 0, 0)))
	RaycastKit.world = fakeWorld(5)
	t.falsy(RaycastKit.lineOfSight(V.new(0, 0, 0), V.new(10, 0, 0)))
end)

t.test("sweep walks the path in steps and covers every stud", function()
	local w = fakeWorld()
	RaycastKit.world = w
	t.eq(RaycastKit.sweep(V.new(0, 0, 0), V.new(10, 0, 0), 4), nil)
	t.eq(#w.calls, 3)
	t.eq(w.calls[1].direction.Magnitude, 4)
	t.eq(w.calls[3].direction.Magnitude, 2)
	t.eq(w.calls[3].origin.X, 8)
end)

t.test("sweep finds a thin part inside a long frame step and stops at the first hit", function()
	local w = fakeWorld(5)
	RaycastKit.world = w
	local hit = RaycastKit.sweep(V.new(0, 0, 0), V.new(100, 0, 0), 4)
	t.truthy(hit)
	t.eq(#w.calls, 2)
end)

t.test("sweep over zero distance does nothing", function()
	local w = fakeWorld()
	RaycastKit.world = w
	t.eq(RaycastKit.sweep(V.new(1, 1, 1), V.new(1, 1, 1), 4), nil)
	t.eq(#w.calls, 0)
end)

t.done()
