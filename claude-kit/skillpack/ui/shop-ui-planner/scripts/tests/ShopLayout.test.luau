--!nocheck
-- Run: lune run ShopLayout.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local S = require("../ShopLayout")

t.test("owned one-time offer shows owned, repeatable stays buyable", function()
	t.eq(S.buttonState({ id = "a", price = 5, oneTime = true }, { a = true }, 100), "owned")
	t.eq(S.buttonState({ id = "b", price = 5 }, { b = true }, 100), "buy")
end)
t.test("not enough currency and unavailable states", function()
	t.eq(S.buttonState({ id = "a", price = 50 }, {}, 10), "needsCurrency")
	t.eq(S.buttonState({ id = "a", price = 1, available = false }, {}, 10), "unavailable")
end)
t.test("order puts featured first then cheaper first, stable on ties", function()
	local out = S.order({
		{ id = "x", price = 9 },
		{ id = "y", price = 3 },
		{ id = "f", price = 99, featured = true },
		{ id = "z", price = 3 },
	})
	local ids = {}
	for _, o in out do
		table.insert(ids, o.id)
	end
	t.eq(ids, { "f", "y", "z", "x" })
end)
local good = {
	priceVisibleOnCard = true,
	closeTargetPx = 48,
	hasTimer = false,
	ownedHidesBuy = true,
	confirmsRobuxPurchase = true,
	coversWholeScreenWithoutClose = false,
	popsUpUnprompted = false,
}
t.test("audit passes a clean spec", function()
	t.eq(S.audit(good), {})
end)
t.test("audit names each dark pattern", function()
	local bad = table.clone(good)
	bad.closeTargetPx = 20
	bad.hasTimer = true
	bad.timerIsReal = false
	bad.popsUpUnprompted = true
	t.eq(S.audit(bad), { "close-target-44px", "no-fake-countdown", "no-unprompted-popups" })
end)
t.done()
