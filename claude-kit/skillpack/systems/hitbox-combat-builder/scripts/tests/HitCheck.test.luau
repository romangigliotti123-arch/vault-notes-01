--!nocheck
-- Run from the kit's systems folder: lune run ../skillpack/systems/hitbox-combat-builder/scripts/tests/HitCheck.test.luau
local t = require("../../../../../systems/_check/harness")
local HitCheck = require("../HitCheck")

local clock = 0
local function make()
	return HitCheck.new({
		maxLag = 0.2,
		now = function()
			return clock
		end,
	})
end
local function claim(extra)
	local c = {
		swingId = "s1",
		attacker = { x = 0, y = 0, z = 0 },
		target = { x = 5, y = 0, z = 0 },
		look = { x = 1, y = 0, z = 0 },
		range = 6,
		maxAngle = 60,
	}
	for k, v in extra or {} do
		c[k] = v
	end
	return c
end

t.test("in range and facing is a hit", function()
	t.eq({ make():check(claim()) }, { true, "hit" })
end)

t.test("out of range is refused, lag allowance widens it by speed times capped lag", function()
	local h = make()
	local far = { x = 7, y = 0, z = 0 }
	t.eq({ h:check(claim({ target = far })) }, { false, "out of range" })
	t.eq({ h:check(claim({ target = far, targetSpeed = 10, lag = 0.1 })) }, { true, "hit" })
	t.eq(h:allowedRange(6, 10, 99), 8)
	t.eq(h:allowedRange(6, 10, -5), 6)
end)

t.test("facing the wrong way is refused unless the attack is area (no look)", function()
	local h = make()
	local behind = { x = -5, y = 0, z = 0 }
	t.eq({ h:check(claim({ target = behind })) }, { false, "not facing" })
	t.eq({ h:check(claim({ target = behind, look = false, swingId = "s2" })) }, { true, "hit" })
end)

t.test("one swing hits once; a new swing id is fine; old ids expire", function()
	local h = make()
	t.eq((h:check(claim())), true)
	t.eq({ h:check(claim()) }, { false, "swing already hit" })
	t.eq((h:check(claim({ swingId = "s9" }))), true)
	clock = 100
	t.eq((h:check(claim())), true)
end)

t.test("blocked line of sight and NaN or infinite positions are refused", function()
	local h = make()
	t.eq({ h:check(claim({ blocked = true })) }, { false, "blocked" })
	t.eq({ h:check(claim({ swingId = "n", target = { x = 0 / 0, y = 0, z = 0 } })) }, { false, "bad position" })
	t.eq({ h:check(claim({ swingId = "i", attacker = { x = math.huge, y = 0, z = 0 } })) }, { false, "bad position" })
end)

t.test("a refused claim does not burn the swing id", function()
	local h = make()
	h:check(claim({ blocked = true }))
	t.eq((h:check(claim())), true)
end)

t.done()
