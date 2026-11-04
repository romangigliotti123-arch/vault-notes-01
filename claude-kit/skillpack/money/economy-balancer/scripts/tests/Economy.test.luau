--!nocheck
local t = require("../../../../../systems/_check/harness")
local Economy = require("../Economy")

t.test("sinks that match income are balanced", function()
	local r = Economy.simulate({
		sources = { { name = "mine", perHour = 600 } },
		sinks = { { name = "upgrade", perHour = 560 } },
		hours = 10,
	})
	t.eq(r.verdict, "balanced")
	t.truthy(r.sinkRatio > 0.9)
end)

t.test("weak sinks inflate: balance piles up", function()
	local r = Economy.simulate({
		sources = { { name = "mine", perHour = 1000 } },
		sinks = { { name = "cosmetic", perHour = 100 } },
		hours = 24,
	})
	t.eq(r.verdict, "inflating")
	t.eq(r.endBalance, 21600)
	t.eq(#r.balances, 24)
end)

t.test("sinks far above income starve the player", function()
	local r = Economy.simulate({
		sources = { { name = "mine", perHour = 100 } },
		sinks = { { name = "gacha", perHour = 1000 } },
		hours = 5,
	})
	t.eq(r.verdict, "starved")
	t.eq(r.endBalance, 0)
	t.truthy(r.unmet > 0)
end)

t.test("spending is capped by what the player has (no negative balance)", function()
	local r = Economy.simulate({
		sources = { { name = "daily", perHour = 10 } },
		sinks = { { name = "x", perHour = 50 } },
		hours = 3,
		startBalance = 20,
	})
	for _, b in r.balances do
		t.truthy(b >= 0)
	end
end)

t.test("hoursToEarn rounds up and guards zero income", function()
	t.eq(Economy.hoursToEarn(1000, 300), 4)
	t.eq(Economy.hoursToEarn(100, 300, 500), 0)
	t.falsy(pcall(Economy.hoursToEarn, 10, 0))
end)

t.test("shares sort largest first and sum to 1", function()
	local s = Economy.shares({ { name = "a", perHour = 25 }, { name = "b", perHour = 75 } })
	t.eq(s[1].name, "b")
	t.eq(s[1].share + s[2].share, 1)
end)

t.test("bad flows are rejected", function()
	t.falsy(pcall(Economy.simulate, { sources = { { name = "x", perHour = -1 } }, sinks = {}, hours = 1 }))
	t.falsy(pcall(Economy.simulate, { sources = {}, sinks = {}, hours = 0 }))
end)

t.done()
