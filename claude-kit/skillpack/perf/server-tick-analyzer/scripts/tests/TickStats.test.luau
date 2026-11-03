--!nocheck
-- Run: lune run TickStats.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local TickStats = require("../TickStats")

local function repeatValue(v, n)
	local out = {}
	for i = 1, n do
		out[i] = v
	end
	return out
end

t.test("a clean 60 Hz server is ok", function()
	local s = TickStats.summarise(repeatValue(1 / 60, 600))
	t.eq(s.verdict, "ok")
	t.truthy(math.abs(s.avgFps - 60) < 1e-6)
	t.eq(s.overBudgetPct, 0)
end)

t.test("a server averaging 40 FPS is slow", function()
	local s = TickStats.summarise(repeatValue(1 / 40, 600))
	t.eq(s.verdict, "slow-average")
	t.truthy(s.overBudgetPct == 100)
end)

t.test("three consecutive long frames are a stall", function()
	local d = repeatValue(1 / 60, 600)
	d[100], d[101], d[102] = 0.08, 0.08, 0.08
	local s = TickStats.summarise(d)
	t.eq(s.longestStallRun, 3)
	t.eq(s.verdict, "stalls")
	t.truthy(math.abs(s.worstMs - 80) < 1e-6)
end)

t.test("rare isolated spikes make it spiky not stalled", function()
	local d = repeatValue(1 / 60, 1200)
	for i = 1, 1200, 80 do
		d[i] = 0.05
	end
	local s = TickStats.summarise(d)
	t.eq(s.longestStallRun, 1)
	t.eq(s.verdict, "spiky")
end)

t.test("short captures are refused", function()
	t.eq(TickStats.summarise(repeatValue(1 / 60, 10)).verdict, "too-few-samples")
end)

t.done()
