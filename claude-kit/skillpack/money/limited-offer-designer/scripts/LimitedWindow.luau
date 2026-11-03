--!strict
-- LimitedWindow: a limited-TIME offer with one shared, honest window (same start and end for everyone, server clock), plus a lint for dark patterns.
-- Vault rules encoded: limited time over limited stock, keep non-consumable limited items owned afterwards, a stated end date, no fake urgency.
--   local issues = LimitedWindow.lint(offer)            -- design-time check, list of strings
--   local ok, why = LimitedWindow.canBuy(offer, os.time(), alreadyOwned)   -- run on the server at purchase time
local LimitedWindow = {}

export type Offer = {
	id: string,
	startsAt: number,
	endsAt: number,
	consumable: boolean, -- true = used up (boost); false = a permanent item (skin, pet)
	keepOwned: boolean?, -- non-consumables must stay owned after the window closes
	perPlayerReset: boolean?, -- the countdown restarts for each player or on every join (fake urgency)
	stockCap: number?, -- hard quantity limit (players race each other)
	oneAtATime: boolean?, -- true if buying twice is meaningless (non-consumable)
}

function LimitedWindow.status(o: Offer, now: number): "upcoming" | "live" | "ended"
	if now < o.startsAt then
		return "upcoming"
	end
	if now >= o.endsAt then
		return "ended"
	end
	return "live"
end

function LimitedWindow.remaining(o: Offer, now: number): number
	return math.max(0, o.endsAt - math.max(now, o.startsAt))
end

function LimitedWindow.canBuy(o: Offer, now: number, alreadyOwned: boolean): (boolean, string)
	if LimitedWindow.status(o, now) ~= "live" then
		return false, "window is not open"
	end
	if alreadyOwned and not o.consumable then
		return false, "already owned"
	end
	return true, "ok"
end

function LimitedWindow.lint(o: Offer): { string }
	local issues: { string } = {}
	if o.endsAt <= o.startsAt then
		table.insert(issues, "endsAt must be after startsAt: a limited offer needs a stated end")
	end
	if o.perPlayerReset then
		table.insert(
			issues,
			"fake urgency: the window restarts per player or per join (use one shared window for everyone)"
		)
	end
	if not o.consumable and not o.keepOwned then
		table.insert(
			issues,
			"a non-consumable limited item must stay owned after the window (players who buy must keep it)"
		)
	end
	if o.stockCap ~= nil then
		table.insert(
			issues,
			"stock cap: players who lose the race get frustrated; prefer limited time (one creator reports stock caps sell well, self-reported: test it)"
		)
	end
	if o.consumable and o.oneAtATime then
		table.insert(issues, "consumable marked oneAtATime: pick one, a consumable can be bought again")
	end
	return issues
end

return LimitedWindow
