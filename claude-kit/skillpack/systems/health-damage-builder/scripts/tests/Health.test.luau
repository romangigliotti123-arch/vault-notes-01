--!nocheck
local t = require("../../../../../systems/_check/harness")
local Health = require("../Health")

local clock = 0
local function make(extra)
	local cfg = {
		max = 100,
		armor = 2,
		resist = { Fire = 0.5 },
		regenDelay = 5,
		regenPerSec = 2,
		now = function()
			return clock
		end,
	}
	for k, v in extra or {} do
		cfg[k] = v
	end
	return Health.new(cfg)
end

t.test("resist then armor, minimum damage, True ignores both", function()
	local h = make()
	local s = h:newState()
	t.eq({ h:damage(s, 30, "Fire") }, { 13, false })
	t.eq({ h:damage(s, 1, "Physical") }, { 1, false })
	t.eq({ h:damage(s, 10, "True") }, { 10, false })
	t.eq(s.hp, 100 - 13 - 1 - 10)
end)

t.test("bad amounts do nothing (negative would heal)", function()
	local h = make()
	local s = h:newState()
	for _, bad in { -50, 0, 0 / 0, math.huge, "9", true } do
		t.eq({ h:damage(s, bad) }, { 0, false })
	end
	t.eq(s.hp, 100)
end)

t.test("death fires once and the dead take no more damage or healing", function()
	local h = make()
	local s = h:newState()
	t.eq({ h:damage(s, 999, "True") }, { 100, true })
	t.eq({ h:damage(s, 5, "True") }, { 0, false })
	t.eq(h:heal(s, 50), 0)
	h:revive(s)
	t.eq(s.hp, 100)
end)

t.test("heal is capped at max", function()
	local h = make()
	local s = h:newState()
	h:damage(s, 20, "True")
	t.eq(h:heal(s, 500), 20)
	t.eq(s.hp, 100)
end)

t.test("regen waits for the delay after a hit", function()
	clock = 0
	local h = make()
	local s = h:newState()
	h:damage(s, 20, "True")
	clock = 4
	h:tick(s, 1)
	t.eq(s.hp, 80)
	clock = 5
	h:tick(s, 1)
	t.eq(s.hp, 82)
end)

t.test("resist above 1 is rejected", function()
	t.falsy(pcall(make, { resist = { Fire = 1.5 } }))
end)

t.done()
