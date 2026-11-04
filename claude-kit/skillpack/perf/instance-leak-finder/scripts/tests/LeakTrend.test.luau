--!nocheck
local t = require("../../../../../systems/_check/harness")
local LeakTrend = require("../LeakTrend")

t.test("a steady climb is growing with the right slope", function()
	local s = {}
	for i = 1, 11 do
		s[i] = 1000 + (i - 1) * 30
	end
	local r = LeakTrend.analyze(s, 30)
	t.eq(r.verdict, "growing")
	t.truthy(math.abs(r.slopePerMinute - 60) < 1e-6)
	t.truthy(r.r2 > 0.99)
end)

t.test("a flat series is flat", function()
	local r = LeakTrend.analyze({ 500, 501, 500, 499, 500, 500 }, 30)
	t.eq(r.verdict, "flat")
end)

t.test("a sawtooth that returns to baseline is not called a leak", function()
	local r = LeakTrend.analyze({ 100, 400, 100, 400, 100, 400, 100, 400 }, 30)
	t.truthy(r.verdict ~= "growing")
end)

t.test("too few samples are refused", function()
	t.eq(LeakTrend.analyze({ 1, 2, 3 }, 30).verdict, "too-few-samples")
end)

t.test("diff lists the classes that grew, biggest first", function()
	local d = LeakTrend.diff(
		{ Part = 100, Sound = 5, Attachment = 50 },
		{ Part = 100, Sound = 45, Attachment = 80, Beam = 3 }
	)
	t.eq(#d, 3)
	t.eq(d[1].class, "Sound")
	t.eq(d[1].delta, 40)
	t.eq(d[3].class, "Beam")
end)

t.test("shrinking series is reported", function()
	local s = {}
	for i = 1, 8 do
		s[i] = 800 - (i - 1) * 20
	end
	t.eq(LeakTrend.analyze(s, 30).verdict, "shrinking")
end)

t.done()
