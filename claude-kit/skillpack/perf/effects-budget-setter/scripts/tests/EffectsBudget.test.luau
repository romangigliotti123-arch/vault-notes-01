--!nocheck
local t = require("../../../../../systems/_check/harness")
local EffectsBudget = require("../EffectsBudget")

t.test("live particles are rate times average lifetime", function()
	t.eq(EffectsBudget.live({ name = "a", rate = 20, lifeMin = 1, lifeMax = 3 }), 40)
	t.eq(EffectsBudget.live({ name = "a", rate = 20, lifeMin = 1, lifeMax = 3, enabled = false }), 0)
end)

t.test("a scene under the cap is left alone", function()
	local rows, total, cap = EffectsBudget.plan({ { name = "Fire", rate = 20, lifeMin = 1, lifeMax = 1 } }, "mid")
	t.eq(total, 20)
	t.eq(cap, 800)
	t.eq(rows[1].suggestedRate, 20)
end)

t.test("an over-cap scene is scaled down proportionally", function()
	local rows, total = EffectsBudget.plan({
		{ name = "Smoke", rate = 400, lifeMin = 2, lifeMax = 2 },
		{ name = "Sparks", rate = 200, lifeMin = 1, lifeMax = 1 },
	}, "low")
	t.eq(total, 1000)
	t.eq(rows[1].name, "Smoke")
	t.eq(rows[1].suggestedRate, 120)
	t.eq(rows[2].suggestedRate, 60)
end)

t.test("disabled emitters get rate 0 and unknown tiers fail loudly", function()
	local rows = EffectsBudget.plan({ { name = "Off", rate = 50, lifeMin = 1, lifeMax = 1, enabled = false } }, "high")
	t.eq(rows[1].suggestedRate, 0)
	t.falsy(pcall(EffectsBudget.plan, {}, "ultra"))
end)

t.test("highlight cap is 255", function()
	t.eq(EffectsBudget.highlightStatus(100), "ok")
	t.eq(EffectsBudget.highlightStatus(230), "near-cap")
	t.truthy(string.find(EffectsBudget.highlightStatus(256), "over-cap", 1, true) ~= nil)
end)

t.done()
