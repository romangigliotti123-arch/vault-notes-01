--!nocheck
local t = require("../../../../../systems/_check/harness")
local S = require("../StarterOffer")

local cfg = { windowSeconds = 900, singleUse = true }

t.test("not eligible before the first milestone", function()
	local s = S.newState()
	t.eq(select(2, S.eligible(cfg, s, 100)):sub(1, 12), "no milestone")
	t.falsy(S.eligible(cfg, s, 100))
end)

t.test("eligible right after the milestone, closes at the window end", function()
	local s = S.newState()
	S.markMilestone(s, 1000)
	t.truthy(S.eligible(cfg, s, 1000))
	t.truthy(S.eligible(cfg, s, 1899))
	t.eq(select(2, S.eligible(cfg, s, 1900)), "window closed")
	t.eq(S.remaining(cfg, s, 1400), 500)
end)

t.test("the milestone time is recorded once", function()
	local s = S.newState()
	S.markMilestone(s, 1000)
	S.markMilestone(s, 5000)
	t.eq(s.milestoneAt, 1000)
end)

t.test("buying or declining twice ends the offer", function()
	local s = S.newState()
	S.markMilestone(s, 0)
	s.dismissedCount = 2
	t.eq(select(2, S.eligible(cfg, s, 10)), "player declined enough times")
	s.dismissedCount = 0
	s.purchased = true
	t.eq(select(2, S.eligible(cfg, s, 10)), "already bought")
end)

t.test("no timer means no remaining and no expiry", function()
	local open = { singleUse = true }
	local s = S.newState()
	S.markMilestone(s, 0)
	t.truthy(S.eligible(open, s, 999999))
	t.eq(S.remaining(open, s, 5), nil)
end)

t.test("lint flags restartable and too-short windows", function()
	t.eq(#S.lint(cfg), 0)
	t.eq(#S.lint({ singleUse = false, windowSeconds = 60 }), 2)
end)

t.done()
