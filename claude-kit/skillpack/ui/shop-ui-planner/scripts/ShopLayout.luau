--!strict
local ShopLayout = {}

export type Offer = { id: string, price: number, featured: boolean?, oneTime: boolean?, available: boolean? }
export type Spec = {
	priceVisibleOnCard: boolean,
	closeTargetPx: number,
	hasTimer: boolean,
	timerIsReal: boolean?,
	ownedHidesBuy: boolean,
	confirmsRobuxPurchase: boolean,
	coversWholeScreenWithoutClose: boolean,
	popsUpUnprompted: boolean,
}

function ShopLayout.buttonState(offer: Offer, owned: { [string]: boolean }, balance: number): string
	if offer.available == false then
		return "unavailable"
	end
	if offer.oneTime and owned[offer.id] then
		return "owned"
	end
	if balance < offer.price then
		return "needsCurrency"
	end
	return "buy"
end

function ShopLayout.order(offers: { Offer }): { Offer }
	local indexed = {}
	for i, o in offers do
		table.insert(indexed, { o = o, i = i })
	end
	table.sort(indexed, function(a, b)
		local fa, fb = a.o.featured == true, b.o.featured == true
		if fa ~= fb then
			return fa
		end
		if a.o.price ~= b.o.price then
			return a.o.price < b.o.price
		end
		return a.i < b.i
	end)
	local out = {}
	for _, r in indexed do
		table.insert(out, r.o)
	end
	return out
end

function ShopLayout.audit(spec: Spec): { string }
	local failed = {}
	local function need(ok: boolean, rule: string)
		if not ok then
			table.insert(failed, rule)
		end
	end
	need(spec.priceVisibleOnCard, "price-visible-before-tap")
	need(spec.closeTargetPx >= 44, "close-target-44px")
	need(not spec.hasTimer or spec.timerIsReal == true, "no-fake-countdown")
	need(spec.ownedHidesBuy, "owned-hides-buy")
	need(spec.confirmsRobuxPurchase, "confirm-before-robux")
	need(not spec.coversWholeScreenWithoutClose, "closable-fullscreen")
	need(not spec.popsUpUnprompted, "no-unprompted-popups")
	return failed
end

return ShopLayout
