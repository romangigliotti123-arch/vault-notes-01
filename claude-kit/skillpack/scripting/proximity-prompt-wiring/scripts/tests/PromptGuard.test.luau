--!nocheck
-- Run: lune run PromptGuard.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local PromptGuard = require("../PromptGuard")

local function at(x, y, z)
	return { X = x, Y = y, Z = z }
end

t.test("distance is euclidean", function()
	t.eq(PromptGuard.distance(at(0, 0, 0), at(3, 4, 0)), 5)
end)

t.test("a nearby living player passes", function()
	local ok, why = PromptGuard.evaluate({ player = at(0, 0, 8), prompt = at(0, 0, 0), maxDistance = 10, alive = true })
	t.truthy(ok)
	t.eq(why, nil)
end)

t.test("slack is allowed but not more", function()
	local base = { prompt = at(0, 0, 0), maxDistance = 10, alive = true, slack = 4 }
	base.player = at(0, 0, 14)
	t.truthy((PromptGuard.evaluate(base)))
	base.player = at(0, 0, 14.5)
	local ok, why = PromptGuard.evaluate(base)
	t.falsy(ok)
	t.eq(why, "too far")
end)

t.test("default slack is 3 studs", function()
	t.truthy((PromptGuard.evaluate({ player = at(0, 0, 13), prompt = at(0, 0, 0), maxDistance = 10, alive = true })))
	t.falsy((PromptGuard.evaluate({ player = at(0, 0, 13.1), prompt = at(0, 0, 0), maxDistance = 10, alive = true })))
end)

t.test("missing character and dead players are rejected with a reason", function()
	local _, a = PromptGuard.evaluate({ player = nil, prompt = at(0, 0, 0), maxDistance = 10, alive = true })
	local _, b = PromptGuard.evaluate({ player = at(0, 0, 0), prompt = at(0, 0, 0), maxDistance = 10, alive = false })
	t.eq(a, "no character")
	t.eq(b, "dead")
end)

t.test("a prompt fired from across the map is rejected", function()
	local ok = PromptGuard.evaluate({ player = at(500, 0, 500), prompt = at(0, 0, 0), maxDistance = 10, alive = true })
	t.falsy(ok)
end)

t.done()
