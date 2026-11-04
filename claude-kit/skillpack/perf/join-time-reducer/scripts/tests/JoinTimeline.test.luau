--!nocheck
local t = require("../../../../../systems/_check/harness")
local JoinTimeline = require("../JoinTimeline")

local marks = {
	{ name = "start", t = 0 },
	{ name = "data loaded", t = 1.5 },
	{ name = "analytics init", t = 9.5 },
	{ name = "character", t = 10 },
	{ name = "hud", t = 12 },
}

t.test("phases are ordered and shares sum to one", function()
	local phases, total = JoinTimeline.phases({ marks[3], marks[1], marks[5], marks[2], marks[4] })
	t.eq(total, 12)
	t.eq(#phases, 4)
	t.eq(phases[1].from, "start")
	local sum = 0
	for _, p in phases do
		sum += p.share
	end
	t.truthy(math.abs(sum - 1) < 1e-9)
end)

t.test("long pole is the 8 second gap", function()
	local phases = JoinTimeline.phases(marks)
	local pole = JoinTimeline.longPole(phases)
	t.eq(pole.to, "analytics init")
	t.eq(pole.seconds, 8)
end)

t.test("blocking finds slow third-party phases only", function()
	local phases = JoinTimeline.phases(marks)
	t.eq(#JoinTimeline.blocking(phases, { "analytics" }, 3), 1)
	t.eq(#JoinTimeline.blocking(phases, { "hud" }, 3), 0)
end)

t.test("verdict compares to budget and previous run", function()
	t.eq(JoinTimeline.verdict(12, 10, nil), "over-budget")
	t.eq(JoinTimeline.verdict(12, nil, 10), "regressed")
	t.eq(JoinTimeline.verdict(8, nil, 10), "improved")
	t.eq(JoinTimeline.verdict(10.5, 11, 10), "ok")
end)

t.test("fewer than two marks gives no phases", function()
	local phases, total = JoinTimeline.phases({ marks[1] })
	t.eq(#phases, 0)
	t.eq(total, 0)
end)

t.done()
