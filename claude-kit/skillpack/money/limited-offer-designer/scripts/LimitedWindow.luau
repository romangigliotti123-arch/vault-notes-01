--!strict
local LimitedWindow = {}

export type Offer = {
	id: string,
	startsAt: number,
	endsAt: number,
	consumable: boolean,
	keepOwned: boolean?,
	perPlayerReset: boolean?,
	stockCap: number?,
	oneAtATime: boolean?,
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
