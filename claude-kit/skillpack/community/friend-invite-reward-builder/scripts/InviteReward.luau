--!strict
local InviteReward = {}

export type Config = {
	inviterDailyCap: number,
	inviteeReward: string,
	inviterReward: string,
}
export type State = {
	isFirstJoin: boolean,
	inviteeClaimed: boolean,
	inviterClaimsToday: number,
}
export type Result = { ok: boolean, reason: string?, inviter: string?, invitee: string? }

function InviteReward.decide(cfg: Config, referrerId: any, inviteeId: number, state: State): Result
	if type(referrerId) ~= "number" or referrerId <= 0 or referrerId ~= math.floor(referrerId) then
		return { ok = false, reason = "no_referrer" }
	end
	if referrerId == inviteeId then
		return { ok = false, reason = "self_referral" }
	end
	if state.inviteeClaimed then
		return { ok = false, reason = "already_claimed" }
	end
	if not state.isFirstJoin then
		return { ok = false, reason = "not_new" }
	end
	if state.inviterClaimsToday >= cfg.inviterDailyCap then
		return { ok = false, reason = "inviter_cap" }
	end
	return { ok = true, inviter = cfg.inviterReward, invitee = cfg.inviteeReward }
end

export type Step = { count: number, reward: string }

function InviteReward.milestonesCrossed(ladder: { Step }, before: number, after: number): { string }
	local out = {}
	for _, step in ladder do
		if before < step.count and after >= step.count then
			table.insert(out, step.reward)
		end
	end
	return out
end

function InviteReward.validate(cfg: Config, ladder: { Step }): { string }
	local problems = {}
	if cfg.inviterDailyCap < 1 then
		table.insert(problems, "inviterDailyCap must be at least 1")
	end
	if cfg.inviteeReward == "" or cfg.inviterReward == "" then
		table.insert(problems, "both sides need a reward label (mutual rewards)")
	end
	local last = 0
	for _, step in ladder do
		if step.count <= last then
			table.insert(problems, `ladder not strictly increasing at {step.count}`)
		end
		last = step.count
	end
	return problems
end

return InviteReward
