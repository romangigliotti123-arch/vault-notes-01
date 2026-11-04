--!nocheck
local t = require("../../../../../systems/_check/harness")
local Boosts = require("../Boosts")

local clock = 1000
local function make()
	return Boosts.new({
		now = function()
			return clock
		end,
		groups = { luck = { mode = "add", cap = 3 }, xp = { mode = "max", cap = 10 } },
		defs = {
			Luck2x = { group = "luck", mult = 2, seconds = 600, maxSeconds = 1200 },
			Luck3x = { group = "luck", mult = 3, seconds = 600, maxSeconds = 1200 },
			Xp2x = { group = "xp", mult = 2, seconds = 300, maxSeconds = 900 },
			Xp4x = { group = "xp", mult = 4, seconds = 300, maxSeconds = 900 },
		},
	})
end

t.test("grant starts a timer and expiry removes it", function()
	local d, b = {}, make()
	b:grant(d, "Luck2x")
	t.eq(b:multiplier(d, "luck"), 2)
	clock += 599
	t.eq(b:multiplier(d, "luck"), 2)
	clock += 1
	t.eq(b:multiplier(d, "luck"), 1)
end)

t.test("re-granting the same boost extends time up to the cap", function()
	clock = 1000
	local d, b = {}, make()
	b:grant(d, "Luck2x")
	b:grant(d, "Luck2x")
	t.eq(d.Boosts.Luck2x, 1000 + 1200)
	b:grant(d, "Luck2x")
	t.eq(d.Boosts.Luck2x, 1000 + 1200)
end)

t.test("add groups add the bonuses and respect the cap; max groups take the best", function()
	clock = 1000
	local d, b = {}, make()
	b:grant(d, "Luck2x")
	b:grant(d, "Luck3x")
	t.eq(b:multiplier(d, "luck"), 3)
	b:grant(d, "Xp2x")
	b:grant(d, "Xp4x")
	t.eq(b:multiplier(d, "xp"), 4)
	t.eq(b:multiplier(d, "nothing"), 1)
end)

t.test("offline time counts (absolute stamps) and unknown saved names are dropped", function()
	clock = 1000
	local d, b = {}, make()
	b:grant(d, "Xp2x")
	local saved = { Boosts = { Xp2x = d.Boosts.Xp2x, Ghost = 99999 } }
	clock += 400
	t.eq(b:multiplier(saved, "xp"), 1)
	t.eq(saved.Boosts.Ghost, nil)
end)

t.test("active lists time left for the HUD, soonest first", function()
	clock = 1000
	local d, b = {}, make()
	b:grant(d, "Luck2x")
	b:grant(d, "Xp2x")
	local a = b:active(d)
	t.eq(a[1].name, "Xp2x")
	t.eq(a[1].left, 300)
end)

t.test("bad config is rejected", function()
	t.falsy(
		pcall(
			Boosts.new,
			{ now = os.time, groups = {}, defs = { A = { group = "g", mult = 2, seconds = 1, maxSeconds = 1 } } }
		)
	)
	t.falsy(pcall(Boosts.new, {
		now = os.time,
		groups = { g = { mode = "add", cap = 2 } },
		defs = { A = { group = "g", mult = 1, seconds = 1, maxSeconds = 1 } },
	}))
end)

t.done()
