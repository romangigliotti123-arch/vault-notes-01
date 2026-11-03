--!nocheck
-- Run: lune run MobileSession.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local MobileSession = require("../MobileSession")

local function series(minutes: number, frameFn, memFn)
	local out = {}
	for i = 0, minutes * 60 do
		table.insert(out, { t = i, frameMs = frameFn(i), memMB = memFn(i) })
	end
	return out
end

t.test("a steady session has no flags", function()
	local r = MobileSession.analyze(series(12, function()
		return 20
	end, function()
		return 400
	end))
	t.eq(#r.flags, 0)
	t.eq(r.avgMs, 20)
	t.eq(r.memGrowthMBPerMin, 0)
end)

t.test("thermal decline is flagged when late frames are 30 percent slower", function()
	local r = MobileSession.analyze(series(12, function(i)
		return if i < 360 then 20 else 28
	end, function()
		return 400
	end))
	t.truthy(r.thermalDeclinePct > 25)
	local found = false
	for _, f in r.flags do
		if string.find(f, "thermal-decline", 1, true) then
			found = true
		end
	end
	t.truthy(found)
end)

t.test("memory growth per minute is computed from first and last sample", function()
	local r = MobileSession.analyze(series(10, function()
		return 20
	end, function(i)
		return 400 + i / 60 * 5
	end))
	t.truthy(math.abs(r.memGrowthMBPerMin - 5) < 1e-6)
end)

t.test("spikes count frames over twice the budget and p95 is reported", function()
	local r = MobileSession.analyze(series(10, function(i)
		return if i % 100 == 0 then 120 else 15
	end, function()
		return 300
	end))
	t.eq(r.spikes, 7)
	t.eq(r.worstMs, 120)
	t.eq(r.p95Ms, 15)
end)

t.test("short sessions warn that thermal behaviour is unknown", function()
	local r = MobileSession.analyze(series(3, function()
		return 16
	end, function()
		return 300
	end))
	t.truthy(string.find(r.flags[1], "short-session", 1, true) ~= nil)
end)

t.done()
