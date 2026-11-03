--!nocheck
-- Run: lune run tests/DailyRewards.test.luau   (from the DailyRewards folder)
local t = require("../../_check/harness")
local D = require("../src/DailyRewards")

local DAY = 86400
local T0 = 20000 * DAY -- a UTC midnight
local cfg = { rewardCount = 7 }

print("DailyRewards")

t.test("first claim starts streak 1 on cycle day 1", function()
	local s = D.newState()
	local r = D.Claim(s, T0 + 100, cfg)
	t.truthy(r.ok)
	t.eq(r.streak, 1)
	t.eq(r.cycleDay, 1)
	t.eq(r.nextClaimAt, T0 + DAY)
	t.eq(s.total, 1)
end)

t.test("second claim the same UTC day is refused and changes nothing", function()
	local s = D.newState()
	D.Claim(s, T0 + 100, cfg)
	local r = D.Claim(s, T0 + DAY - 1, cfg)
	t.falsy(r.ok)
	t.eq(r.reason, "already")
	t.eq(r.nextClaimAt, T0 + DAY)
	t.eq(s.streak, 1)
	t.eq(s.total, 1)
end)

t.test("claiming on consecutive days grows the streak and walks the cycle", function()
	local s = D.newState()
	for i = 0, 6 do
		local r = D.Claim(s, T0 + i * DAY + 5, cfg)
		t.eq(r.streak, i + 1)
		t.eq(r.cycleDay, i + 1)
	end
	local r = D.Claim(s, T0 + 7 * DAY, cfg) -- day 8 wraps to cycle day 1
	t.eq(r.streak, 8)
	t.eq(r.cycleDay, 1)
end)

t.test("missing a day resets the streak to 1 and reports it", function()
	local s = D.newState()
	D.Claim(s, T0, cfg)
	D.Claim(s, T0 + DAY, cfg)
	local r = D.Claim(s, T0 + 3 * DAY, cfg)
	t.truthy(r.ok)
	t.eq(r.streak, 1)
	t.truthy(r.brokeStreak)
end)

t.test("grace days keep the streak through a short gap", function()
	local s = D.newState()
	local g = { rewardCount = 7, graceDays = 1 }
	D.Claim(s, T0, g)
	local r = D.Claim(s, T0 + 2 * DAY, g) -- missed exactly one day
	t.eq(r.streak, 2)
	r = D.Claim(s, T0 + 5 * DAY, g) -- missed two days
	t.eq(r.streak, 1)
end)

t.test("server clock going backwards is refused, never resets", function()
	local s = D.newState()
	D.Claim(s, T0 + 5 * DAY, cfg)
	local r = D.Claim(s, T0 + 2 * DAY, cfg)
	t.falsy(r.ok)
	t.eq(r.reason, "clock")
	t.eq(s.streak, 1)
end)

t.test("Status previews without mutating", function()
	local s = D.newState()
	local st = D.Status(s, T0, cfg)
	t.truthy(st.canClaim)
	t.eq(st.cycleDay, 1)
	D.Claim(s, T0, cfg)
	st = D.Status(s, T0 + 10, cfg)
	t.falsy(st.canClaim)
	t.eq(st.cycleDay, 2)
	t.eq(st.nextClaimAt, T0 + DAY)
	st = D.Status(s, T0 + DAY, cfg)
	t.truthy(st.canClaim)
	t.eq(st.streak, 2)
	t.eq(s.total, 1)
end)

t.test("day offset moves the reset boundary (midnight UTC-5)", function()
	local c = { rewardCount = 7, dayOffset = -5 * 3600 }
	local s = D.newState()
	local r = D.Claim(s, T0 + 4 * 3600, c) -- 04:00 UTC = 23:00 local previous day
	t.truthy(r.ok)
	t.eq(r.nextClaimAt, T0 + 5 * 3600)
	t.falsy(D.Claim(s, T0 + 5 * 3600 - 1, c).ok)
	t.truthy(D.Claim(s, T0 + 5 * 3600, c).ok)
end)

t.test("sanitize repairs garbage from old or edited data", function()
	local s = D.sanitize({ lastDay = "x", streak = -4, total = 0 / 0 })
	t.eq(s.lastDay, nil)
	t.eq(s.streak, 0)
	t.eq(s.total, 0)
	t.eq(D.sanitize(nil).streak, 0)
end)

t.test("streak cap holds", function()
	local s = D.newState()
	local c = { rewardCount = 7, capStreak = 3 }
	for i = 0, 6 do
		D.Claim(s, T0 + i * DAY, c)
	end
	t.eq(s.streak, 3)
end)

t.done()
