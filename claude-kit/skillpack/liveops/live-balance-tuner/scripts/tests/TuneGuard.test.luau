--!nocheck
local t = require("../../../../../systems/_check/harness")
local TuneGuard = require("../TuneGuard")

local def = { min = 50, max = 5000, maxStepPct = 25, cooldown = 3600 }

t.test("a small change inside bounds with no history is allowed", function()
	local d = TuneGuard.check(def, 1000, 1200, {}, 10000)
	t.eq(d.ok, true)
	t.eq(d.value, 1200)
	t.eq(d.stepPct, 20)
end)

t.test("a change over the step limit is refused and the nearest allowed value is returned", function()
	local d = TuneGuard.check(def, 1000, 2000, {}, 10000)
	t.eq(d.ok, false)
	t.eq(d.value, 1250)
	local down = TuneGuard.check(def, 1000, 100, {}, 10000)
	t.eq(down.value, 750)
end)

t.test("outside bounds is refused and clamped", function()
	local d = TuneGuard.check(def, 4900, 9000, {}, 10000)
	t.eq(d.ok, false)
	t.eq(d.reason, "outside bounds")
	t.eq(d.value, 5000)
end)

t.test("cooldown blocks a second change too soon, allows it later", function()
	local hist = { { at = 9000, from = 800, to = 1000 } }
	t.eq(TuneGuard.check(def, 1000, 1100, hist, 10000).ok, false)
	t.eq(TuneGuard.check(def, 1000, 1100, hist, 13000).ok, true)
end)

t.test("NaN and infinity are refused", function()
	t.eq(TuneGuard.check(def, 1000, 0 / 0, {}, 1).ok, false)
	t.eq(TuneGuard.check(def, 1000, math.huge, {}, 1).ok, false)
end)

t.test("staged steps reach the target in equal parts", function()
	local s = TuneGuard.stages(1000, 1400, 4)
	t.eq(#s, 4)
	t.eq(s[1], 1100)
	t.eq(s[4], 1400)
end)

t.test("revert returns the value before the last change", function()
	t.eq(TuneGuard.revertValue({ { at = 1, from = 800, to = 1000 }, { at = 2, from = 1000, to = 1200 } }), 1000)
	t.eq(TuneGuard.revertValue({}), nil)
end)

t.test("a current value of zero allows a first move to zero but treats growth from zero as a full step", function()
	t.eq(TuneGuard.check({ min = 0, max = 10 }, 0, 0, {}, 1).ok, true)
	t.eq(TuneGuard.check({ min = 0, max = 10 }, 0, 5, {}, 1).ok, false)
end)

t.done()
