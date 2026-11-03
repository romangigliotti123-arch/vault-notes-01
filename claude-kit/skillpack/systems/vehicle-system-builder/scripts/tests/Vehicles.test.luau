--!nocheck
-- Run from the kit's systems folder: lune run ../skillpack/systems/vehicle-system-builder/scripts/tests/Vehicles.test.luau
local t = require("../../../../../systems/_check/harness")
local Vehicles = require("../Vehicles")

local clock = 0
local function make()
	return Vehicles.new({
		maxPerPlayer = 1,
		spawnCooldown = 5,
		abandonSeconds = 60,
		seats = 2,
		now = function()
			return clock
		end,
	})
end

t.test("one vehicle per player and a spawn cooldown", function()
	clock = 0
	local v = make()
	t.truthy((v:spawn(1)))
	t.eq({ v:spawn(1) }, { nil, "cooldown" })
	clock = 6
	t.eq({ v:spawn(1) }, { nil, "limit" })
	t.truthy((v:spawn(2)))
end)

t.test("only the owner takes the driver seat; passengers take others", function()
	clock = 0
	local v = make()
	local id = v:spawn(1)
	t.eq({ v:sit(id, 2, 1) }, { false, "not the owner" })
	t.eq({ v:sit(id, 2, 2) }, { true, "ok" })
	t.eq({ v:sit(id, 1, 1) }, { true, "ok" })
	t.eq(v:driver(id), 1)
end)

t.test("seat taken, bad seat, double seating, unknown vehicle", function()
	clock = 0
	local v = make()
	local id = v:spawn(1)
	v:sit(id, 1, 1)
	t.eq({ v:sit(id, 3, 1) }, { false, "seat taken" })
	for _, bad in { 0, 3, 1.5, "1", 0 / 0 } do
		t.eq((v:sit(id, 3, bad)), false)
	end
	t.eq((v:sit(id, 1, 2)), false)
	t.eq({ v:sit("nope", 3, 2) }, { false, "no such vehicle" })
end)

t.test("sweep removes vehicles whose owner left, or that sat empty too long, never occupied ones", function()
	clock = 0
	local v = make()
	local a = v:spawn(1)
	local b = v:spawn(2)
	local c = v:spawn(3)
	v:sit(c, 3, 1)
	t.eq(v:sweep({ [1] = true, [2] = true, [3] = false }), {})
	t.eq(v:sweep({ [1] = true, [2] = false, [3] = false }), { b })
	clock = 60
	t.eq(v:sweep({ [1] = true, [3] = true }), { a })
	v:leaveSeat(c, 3)
	clock = 121
	t.eq(v:sweep({ [3] = true }), { c })
end)

t.done()
