--!strict
-- OfferGate: the server-side rule for WHEN an offer may be shown. Encodes the vault's timing rules so a shop prompt cannot become a spammy pop-up:
-- no sales on join, no stacked modals, only at a moment of need (or when the player opens the shop), never where gameplay cannot pause,
-- cooldowns per offer and overall, and a per-session cap. Defaults are starting points to A/B test, not platform rules.
--   local ok, why = OfferGate.canShow(cfg, state, "StarterPack", "need", os.time())
--   if ok then OfferGate.record(state, "StarterPack", os.time()) --[[ then tell the client to show it ]] end
local OfferGate = {}

export type Config = {
	allowedTriggers: { string }?, -- default { "need", "milestone", "shopOpen" }
	firstSessionTriggers: { string }?, -- allowed in the player's first session (default { "shopOpen" })
	globalCooldown: number?, -- seconds between any two offers (default 300)
	offerCooldown: number?, -- seconds before the same offer again (default 1800)
	maxPerSession: number?, -- default 4
}
export type State = {
	sessionsPlayed: number, -- 1 = this is the first session
	modalOpen: boolean, -- another offer or dialog is on screen
	canPause: boolean, -- gameplay can pause now (not mid-fight, not mid-run)
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

-- call when the offer is actually shown (a player opening the shop themselves is not counted against the caps)
function OfferGate.record(state: State, offerId: string, now: number)
	state.lastShownAt = now
	state.lastByOffer[offerId] = now
	state.shownThisSession += 1
end

return OfferGate
