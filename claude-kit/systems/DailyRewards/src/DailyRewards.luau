--!strict

export type State = {
	lastDay: number?,
	streak: number,
	total: number,
}

export type Config = {
	rewardCount: number,
	graceDays: number?,
	dayLength: number?,
	dayOffset: number?,
	capStreak: number?,
}

export type Status = {
	canClaim: boolean,
	streak: number,
	cycleDay: number,
	nextClaimAt: number,
	reason: string?,
}

export type ClaimResult = {
	ok: boolean,
	reason: string?,
	streak: number,
	cycleDay: number,
	nextClaimAt: number,
	brokeStreak: boolean?,
}

local DailyRewards = {}

function DailyRewards.newState(): State
	return { lastDay = nil, streak = 0, total = 0 }
end

function DailyRewards.sanitize(state: any): State
	local s: any = type(state) == "table" and state or {}
	if type(s.lastDay) ~= "number" or s.lastDay ~= s.lastDay then
		s.lastDay = nil
	end
	if type(s.streak) ~= "number" or s.streak < 0 or s.streak ~= s.streak then
		s.streak = 0
	end
	if type(s.total) ~= "number" or s.total < 0 or s.total ~= s.total then
		s.total = 0
	end
	return s :: State
end

local function dayOf(now: number, cfg: Config): number
	return math.floor((now + (cfg.dayOffset or 0)) / (cfg.dayLength or 86400))
end

local function plan(state: State, now: number, cfg: Config): (string?, number, boolean)
	local day = dayOf(now, cfg)
	local last = state.lastDay
	if last == nil then
		return nil, 1, false
	end
	if day == last then
		return "already", state.streak, false
	end
	if day < last then
		return "clock", state.streak, false
	end
	local missed = day - last - 1
	if missed <= (cfg.graceDays or 0) then
		return nil, math.min(state.streak + 1, cfg.capStreak or 10000), false
	end
	return nil, 1, state.streak > 1
end

local function cycleDay(streak: number, cfg: Config): number
	return ((math.max(streak, 1) - 1) % cfg.rewardCount) + 1
end

function DailyRewards.Status(state: State, now: number, cfg: Config): Status
	local reason, newStreak = plan(state, now, cfg)
	local len = cfg.dayLength or 86400
	if reason == nil then
		return { canClaim = true, streak = newStreak, cycleDay = cycleDay(newStreak, cfg), nextClaimAt = 0 }
	end
	local day = dayOf(now, cfg)
	return {
		canClaim = false,
		streak = state.streak,
		cycleDay = cycleDay(state.streak + 1, cfg),
		nextClaimAt = (day + 1) * len - (cfg.dayOffset or 0),
		reason = reason,
	}
end

function DailyRewards.Claim(state: State, now: number, cfg: Config): ClaimResult
	local reason, newStreak, broke = plan(state, now, cfg)
	if reason ~= nil then
		local st = DailyRewards.Status(state, now, cfg)
		return {
			ok = false,
			reason = reason,
			streak = state.streak,
			cycleDay = st.cycleDay,
			nextClaimAt = st.nextClaimAt,
		}
	end
	local today = dayOf(now, cfg)
	state.lastDay = today
	state.streak = newStreak
	state.total += 1
	local len = cfg.dayLength or 86400
	return {
		ok = true,
		streak = newStreak,
		cycleDay = cycleDay(newStreak, cfg),
		nextClaimAt = (today + 1) * len - (cfg.dayOffset or 0),
		brokeStreak = broke,
	}
end

return DailyRewards
