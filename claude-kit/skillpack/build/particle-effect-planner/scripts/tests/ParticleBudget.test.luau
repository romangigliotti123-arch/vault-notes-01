--!nocheck
-- Run: lune run ParticleBudget.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local PB = require("../ParticleBudget")

t.test("looping live count is rate times lifetime times copies", function()
	t.eq(PB.live({ name = "smoke", rate = 40, lifeMax = 3, emitters = 2 }), 240)
end)

t.test("lifetime is clamped to 20 s in the live count", function()
	t.eq(PB.live({ name = "x", rate = 10, lifeMax = 60 }), 200)
end)

t.test("one-shot bursts multiply burst size by overlap", function()
	t.eq(PB.live({ name = "hit", rate = 0, lifeMax = 1, burst = 30, bursts = 4, loop = false }), 120)
end)

t.test("mobile rate cap is 100 and desktop 400", function()
	t.eq(#PB.assess({ name = "a", rate = 110, lifeMax = 0.5 }, "mobile").issues, 1)
	t.eq(#PB.assess({ name = "a", rate = 110, lifeMax = 0.5 }, "desktop").issues, 0)
	t.eq(#PB.assess({ name = "a", rate = 500, lifeMax = 0.5 }, "desktop").issues, 1)
end)

t.test("long lifetime is flagged", function()
	local c = PB.assess({ name = "fog", rate = 1, lifeMax = 30 }, "desktop")
	t.eq(#c.issues, 1)
end)

t.test("an effect over a quarter of the budget is flagged", function()
	local c = PB.assess({ name = "blizzard", rate = 100, lifeMax = 10 }, "mobile")
	t.truthy(#c.issues >= 1)
end)

t.test("plan sums effects, finds the heaviest and checks the budget", function()
	local p = PB.plan({
		{ name = "a", rate = 10, lifeMax = 2 },
		{ name = "b", rate = 50, lifeMax = 4 },
	}, "mobile")
	t.eq(p.totalLive, 220)
	t.eq(p.heaviest, "b")
	t.falsy(p.over)
	t.truthy(PB.plan({ { name = "c", rate = 100, lifeMax = 20 } }, "mobile").over)
end)

t.done()
