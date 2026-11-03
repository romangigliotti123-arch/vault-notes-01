--!nocheck
-- Run from the kit's systems folder: lune run ../skillpack/money/pay-to-win-checker/scripts/tests/OfferLint.test.luau
local t = require("../../../../../systems/_check/harness")
local OfferLint = require("../OfferLint")

local function rules(findings)
	local n = {}
	for _, f in findings do
		table.insert(n, f.severity)
	end
	return n
end

t.test("a clean cosmetic passes with no findings", function()
	local f, blocked = OfferLint.check({ { name = "Hat", priceRobux = 75 } })
	t.eq(#f, 0)
	t.falsy(blocked)
end)

t.test("gating core progress blocks", function()
	local _, blocked = OfferLint.check({ { name = "Unlock World 2", gatesCoreProgress = true } })
	t.truthy(blocked)
end)

t.test("combat power in pvp blocks but the same item in a non-pvp mode does not", function()
	local _, a = OfferLint.check({ { name = "Dmg+", pvp = true, grantsCombatPower = true } })
	local _, b = OfferLint.check({ { name = "Dmg+", pvp = false, grantsCombatPower = true } })
	t.truthy(a)
	t.falsy(b)
end)

t.test("random offers need shown odds AND the restriction path", function()
	local f1, b1 = OfferLint.check({ { name = "Crate", randomized = true } })
	t.truthy(b1)
	t.eq(#f1, 2)
	local f2, b2 =
		OfferLint.check({ { name = "Crate", randomized = true, oddsShown = true, restrictionPathHandled = true } })
	t.falsy(b2)
	t.eq(#f2, 0)
	local _, b3 = OfferLint.check({ { name = "Crate", randomized = true, oddsShown = true } })
	t.truthy(b3)
end)

t.test("soft problems warn without blocking", function()
	local f, blocked = OfferLint.check({
		{
			name = "Skip",
			timerSkipOrAppointment = true,
			popupOnJoin = true,
			limitedStock = true,
			requiresHardCurrency = true,
		},
	})
	t.falsy(blocked)
	t.eq(#f, 4)
	for _, s in rules(f) do
		t.eq(s, "warn")
	end
end)

t.test("summary counts both kinds", function()
	local f = OfferLint.check({ { name = "x", gatesCoreProgress = true, popupOnJoin = true } })
	t.eq(OfferLint.summary(f), "1 block, 1 warn")
end)

t.test("bad input is rejected", function()
	t.falsy(pcall(OfferLint.check, { { name = "" } }))
	t.falsy(pcall(OfferLint.check, { { name = "x", priceRobux = -1 } }))
end)

t.done()
