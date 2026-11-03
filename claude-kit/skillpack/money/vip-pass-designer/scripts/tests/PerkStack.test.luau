--!nocheck
-- Run from the kit's systems folder: lune run ../skillpack/money/vip-pass-designer/scripts/tests/PerkStack.test.luau
local t = require("../../../../../systems/_check/harness")
local P = require("../PerkStack")

t.test("no perks is 1x", function()
	t.eq(P.multiplier({}, "coins"), 1)
end)

t.test("multipliers add their bonus instead of compounding", function()
	local perks = {
		{ source = "VIP", target = "coins", multiplier = 2 },
		{ source = "Bundle", target = "coins", multiplier = 1.5 },
		{ source = "Luck", target = "luck", multiplier = 2 },
	}
	t.eq(P.multiplier(perks, "coins"), 2.5)
	t.eq(P.multiplier(perks, "luck"), 2)
end)

t.test("the total is clipped to the cap", function()
	local perks = {
		{ source = "A", target = "coins", multiplier = 3 },
		{ source = "B", target = "coins", multiplier = 3 },
	}
	t.eq(P.multiplier(perks, "coins"), 3)
	t.eq(P.multiplier(perks, "coins", 10), 5)
end)

t.test("audit lists targets that would exceed the cap if one player owned everything", function()
	local perks = {
		{ source = "A", target = "coins", multiplier = 2 },
		{ source = "B", target = "coins", multiplier = 2 },
		{ source = "C", target = "coins", multiplier = 2 },
		{ source = "D", target = "xp", multiplier = 2 },
	}
	local a = P.audit(perks)
	t.eq(#a, 1)
	t.eq(a[1].target, "coins")
	t.eq(a[1].raw, 4)
end)

t.test("perk share of income", function()
	t.eq(P.perkShare(1), 0)
	t.eq(P.perkShare(2), 0.5)
end)

t.test("sub-1x multipliers are rejected", function()
	t.falsy(pcall(P.multiplier, { { source = "x", target = "coins", multiplier = 0.5 } }, "coins"))
	t.falsy(pcall(P.audit, { { source = "x", target = "coins", multiplier = 0 } }))
end)

t.done()
