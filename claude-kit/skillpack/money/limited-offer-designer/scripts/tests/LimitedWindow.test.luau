--!nocheck
-- Run from the kit's systems folder: lune run ../skillpack/money/limited-offer-designer/scripts/tests/LimitedWindow.test.luau
local t = require("../../../../../systems/_check/harness")
local L = require("../LimitedWindow")

local offer = { id = "WinterSkin", startsAt = 1000, endsAt = 2000, consumable = false, keepOwned = true }

t.test("status follows the shared server clock", function()
	t.eq(L.status(offer, 999), "upcoming")
	t.eq(L.status(offer, 1000), "live")
	t.eq(L.status(offer, 1999), "live")
	t.eq(L.status(offer, 2000), "ended")
end)

t.test("remaining counts down and never goes negative", function()
	t.eq(L.remaining(offer, 1500), 500)
	t.eq(L.remaining(offer, 5000), 0)
	t.eq(L.remaining(offer, 0), 1000)
end)

t.test("canBuy only inside the window and not twice for permanent items", function()
	t.falsy(L.canBuy(offer, 500, false))
	t.truthy(L.canBuy(offer, 1500, false))
	t.eq(select(2, L.canBuy(offer, 1500, true)), "already owned")
	t.falsy(L.canBuy(offer, 2500, false))
	local boost = { id = "Boost", startsAt = 1000, endsAt = 2000, consumable = true }
	t.truthy(L.canBuy(boost, 1500, true))
end)

t.test("a clean offer has no lint issues", function()
	t.eq(#L.lint(offer), 0)
end)

t.test("dark patterns and risky designs are flagged", function()
	local bad = {
		id = "x",
		startsAt = 100,
		endsAt = 100,
		consumable = false,
		perPlayerReset = true,
		stockCap = 100,
	}
	t.eq(#L.lint(bad), 4) -- no end, per-player reset, not kept, stock cap
	t.eq(#L.lint({ id = "y", startsAt = 1, endsAt = 2, consumable = true, oneAtATime = true }), 1)
end)

t.done()
