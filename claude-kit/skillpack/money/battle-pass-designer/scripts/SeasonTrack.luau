--!strict
local SeasonTrack = {}

export type Track = "free" | "premium"
export type Config = {
	tiers: number,
	xpPerTier: number,
	startsAt: number,
	endsAt: number,
	free: { [number]: string },
	premium: { [number]: string },
}
export type State = { xp: number, premium: boolean, claimed: { [string]: boolean } }

function SeasonTrack.newState(): State
	return { xp = 0, premium = false, claimed = {} }
end

function SeasonTrack.validate(cfg: Config): { string }
	local problems: { string } = {}
	if cfg.endsAt <= cfg.startsAt then
		table.insert(problems, "endsAt must be after startsAt (a season needs a stated end)")
	end
	if cfg.tiers < 1 or cfg.xpPerTier < 1 then
		table.insert(problems, "tiers and xpPerTier must be >= 1")
	end
	for _, track in { "free", "premium" } do
		for tier in (cfg :: any)[track] do
			if type(tier) ~= "number" or tier < 1 or tier > cfg.tiers or tier ~= math.floor(tier) then
				table.insert(problems, `{track} reward at tier {tostring(tier)} is outside 1..{cfg.tiers}`)
			end
		end
	end
	local freeCount, premiumCount = 0, 0
	for _ in cfg.free do
		freeCount += 1
	end
	for _ in cfg.premium do
		premiumCount += 1
	end
	if freeCount == 0 then
		table.insert(problems, "free track is empty: free players need something to earn")
	end
	if premiumCount == 0 then
		table.insert(problems, "premium track is empty")
	end
	return problems
end

function SeasonTrack.active(cfg: Config, now: number): boolean
	return now >= cfg.startsAt and now < cfg.endsAt
end

function SeasonTrack.tierFor(cfg: Config, xp: number): number
	return math.min(cfg.tiers, math.floor(math.max(0, xp) / cfg.xpPerTier))
end

function SeasonTrack.addXp(cfg: Config, state: State, amount: number, now: number): number
	if amount <= 0 or amount ~= amount or not SeasonTrack.active(cfg, now) then
		return state.xp
	end
	state.xp = math.min(cfg.tiers * cfg.xpPerTier, state.xp + amount)
	return state.xp
end

local function ck(track: Track, tier: number): string
	return `{track}:{tier}`
end

function SeasonTrack.claim(cfg: Config, state: State, track: Track, tier: number, now: number): (boolean, string)
	if track ~= "free" and track ~= "premium" then
		return false, "unknown track"
	end
	if not SeasonTrack.active(cfg, now) then
		return false, "season is not active"
	end
	local reward = cfg[track][tier]
	if reward == nil then
		return false, "no reward at that tier"
	end
	if tier > SeasonTrack.tierFor(cfg, state.xp) then
		return false, "tier not reached"
	end
	if track == "premium" and not state.premium then
		return false, "premium pass not owned"
	end
	if state.claimed[ck(track, tier)] then
		return false, "already claimed"
	end
	state.claimed[ck(track, tier)] = true
	return true, reward
end

function SeasonTrack.claimable(cfg: Config, state: State): { { track: Track, tier: number, reward: string } }
	local out: { { track: Track, tier: number, reward: string } } = {}
	local reached = SeasonTrack.tierFor(cfg, state.xp)
	local function consider(track: Track, tier: number)
		local reward = cfg[track][tier]
		if reward and not state.claimed[ck(track, tier)] and (track == "free" or state.premium) then
			table.insert(out, { track = track, tier = tier, reward = reward })
		end
	end
	for tier = 1, reached do
		consider("free", tier)
		consider("premium", tier)
	end
	return out
end

function SeasonTrack.pacing(cfg: Config, xpPerDay: number): (number, string?)
	assert(xpPerDay > 0, "xpPerDay must be > 0")
	local days = math.ceil(cfg.tiers * cfg.xpPerTier / xpPerDay)
	local seasonDays = (cfg.endsAt - cfg.startsAt) / 86400
	if days > seasonDays then
		return days,
			`needs {days} days at {xpPerDay} xp/day but the season is {math.floor(seasonDays)} days: a casual player cannot finish`
	end
	return days, nil
end

return SeasonTrack
