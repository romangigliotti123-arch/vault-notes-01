--!nocheck
-- Run: lune run UiMotion.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local M = require("../UiMotion")

local function step(name, role, d, props, loops, stoppable)
	return { name = name, role = role, duration = d, properties = props, loops = loops, stoppable = stoppable }
end

t.test("a sane plan has no findings", function()
	local plan = {
		step("press", "feedback", 0.08, { "Size" }),
		step("open", "transition", 0.25, { "GroupTransparency", "Position" }),
		step("glow", "ambient", 2, { "GroupTransparency" }, true, true),
	}
	t.eq(M.validate(plan), {})
end)
t.test("slow feedback and unknown role are flagged", function()
	local f = M.validate({ step("p", "feedback", 0.5, { "Size" }), step("x", "weird", 0.1, {}) })
	t.eq(f[1].rule, "too-slow-for-feedback")
	t.eq(f[2].rule, "unknown-role")
end)
t.test("text stroke tween and unstoppable loop are flagged", function()
	local f = M.validate({
		step("pop", "reward", 0.5, { "TextStrokeTransparency" }),
		step("pulse", "ambient", 1, { "Size" }, true, false),
	})
	t.eq(f[1].rule, "avoid-tweening-text-stroke")
	t.eq(f[2].rule, "loop-not-stoppable")
end)
t.test("more than the loop budget is flagged once for the plan", function()
	local plan = {}
	for i = 1, 4 do
		table.insert(plan, step("l" .. i, "ambient", 1, { "GroupTransparency" }, true, true))
	end
	local f = M.validate(plan)
	t.eq(#f, 1)
	t.eq(f[1].rule, "too-many-looping-tweens")
end)
t.test("reduced drops loops and motion, keeps short fades", function()
	local calm = M.reduced({
		step("open", "transition", 0.35, { "GroupTransparency", "Position" }),
		step("bounce", "reward", 1, { "Size" }),
		step("glow", "ambient", 2, { "GroupTransparency" }, true, true),
	})
	t.eq(#calm, 2)
	t.eq(calm[1].properties, { "GroupTransparency" })
	t.eq(calm[1].duration, 0.15)
	t.eq(calm[2].duration, 0)
	t.eq(M.validate(calm), {})
end)
t.done()
