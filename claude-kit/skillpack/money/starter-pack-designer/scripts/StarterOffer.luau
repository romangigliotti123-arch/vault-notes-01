--!strict
local StarterOffer = {}

export type Config = {
	windowSeconds: number?,
	singleUse: boolean,
	maxDismissals: number?,
}
export type PlayerState = { milestoneAt: number?, purchased: boolean, dismissedCount: number }

function StarterOffer.newState(): PlayerState
	return { purchased = false, dismissedCount = 0 }
end

function StarterOffer.markMilestone(state: PlayerState, now: number)
	if state.milestoneAt == nil then
		state.milestoneAt = now
	end
end

function StarterOffer.eligible(cfg: Config, state: PlayerState, now: number): (boolean, string)
	if state.purchased then
		return false, "already bought"
	end
	if state.milestoneAt == nil then
		return false, "no milestone yet: do not sell before the player understands the game"
	end
	if state.dismissedCount >= (cfg.maxDismissals or 2) then
		return false, "player declined enough times"
	end
	if cfg.windowSeconds and now >= state.milestoneAt + cfg.windowSeconds then
		return false, "window closed"
	end
	return true, "ok"
end

function StarterOffer.remaining(cfg: Config, state: PlayerState, now: number): number?
	if cfg.windowSeconds == nil or state.milestoneAt == nil then
		return nil
	end
	return math.max(0, state.milestoneAt + cfg.windowSeconds - now)
end

function StarterOffer.lint(cfg: Config): { string }
	local issues: { string } = {}
	if not cfg.singleUse then
		table.insert(issues, "singleUse=false: a window that can restart is fake urgency")
	end
	if cfg.windowSeconds ~= nil and cfg.windowSeconds < 300 then
		table.insert(issues, "window under 5 minutes: too short to read and decide (the vault example is 15 minutes)")
	end
	return issues
end

return StarterOffer
