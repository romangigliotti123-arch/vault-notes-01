--!strict
local OfferGate = {}

export type Config = {
	allowedTriggers: { string }?,
	firstSessionTriggers: { string }?,
	globalCooldown: number?,
	offerCooldown: number?,
	maxPerSession: number?,
}
export type State = {
	sessionsPlayed: number,
	modalOpen: boolean,
	canPause: boolean,
	lastShownAt: number?,
	lastByOffer: { [string]: number },
	shownThisSession: number,
}

function OfferGate.newState(sessionsPlayed: number): State
	return {
		sessionsPlayed = sessionsPlayed,
		modalOpen = false,
		canPause = true,
		lastByOffer = {},
		shownThisSession = 0,
	}
end

local function has(list: { string }, v: string): boolean
	return table.find(list, v) ~= nil
end

function OfferGate.canShow(cfg: Config, state: State, offerId: string, trigger: string, now: number): (boolean, string)
	if trigger == "join" then
		return false, "no sales on join"
	end
	if not has(cfg.allowedTriggers or { "need", "milestone", "shopOpen" }, trigger) then
		return false, "trigger is not a moment of need (random pop-up)"
	end
	if state.sessionsPlayed <= 1 and not has(cfg.firstSessionTriggers or { "shopOpen" }, trigger) then
		return false, "first session: only player-initiated offers"
	end
	if state.modalOpen then
		return false, "another modal is open (no stacking)"
	end
	if trigger ~= "shopOpen" and not state.canPause then
		return false, "gameplay cannot pause here"
	end
	if trigger ~= "shopOpen" then
		if state.lastShownAt and now - state.lastShownAt < (cfg.globalCooldown or 300) then
			return false, "global cooldown"
		end
		local last = state.lastByOffer[offerId]
		if last and now - last < (cfg.offerCooldown or 1800) then
			return false, "offer cooldown"
		end
		if state.shownThisSession >= (cfg.maxPerSession or 4) then
			return false, "session cap reached"
		end
	end
	return true, "ok"
end

function OfferGate.record(state: State, offerId: string, now: number)
	state.lastShownAt = now
	state.lastByOffer[offerId] = now
	state.shownThisSession += 1
end

return OfferGate
