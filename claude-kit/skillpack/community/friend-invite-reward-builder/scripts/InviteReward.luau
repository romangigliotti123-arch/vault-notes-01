--!strict
-- InviteReward: the pure rules of a friend-invite reward (who qualifies, caps, milestone ladder) with no DataStore and no Instances,
-- so it is testable under Lune. The server wires it up:
--   * `referrerId` comes from the joining player's join data on the SERVER (Player:GetJoinData().ReferredByPlayerId; live-check the
--     field name and when it is filled) or from a share-link LaunchData value you set. The client never says who invited it.
--   * `state` is read from the kit PlayerData profiles (invitee's `claimedInvite`, inviter's `claimsToday`, `isFirstJoin`), saved
--     with UpdateAsync, and the grant itself goes through your own server code (kit Shop/PlayerData). This module only says yes/no.
--   * Prompt the invite UI with SocialService:PromptGameInvite behind SocialService:CanSendGameInviteAsync in a pcall.
local InviteReward = {}

export type Config = {
	inviterDailyCap: number, -- rewarded invites per inviter per UTC day
	inviteeReward: string, -- label your server maps to a grant (small, cosmetic or soft currency)
	inviterReward: string,
}
export type State = {
	isFirstJoin: boolean, -- the invitee has never joined this experience before
	inviteeClaimed: boolean, -- the invitee already used an invite reward
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
		return { ok = false, reason = "not_new" } -- only brand-new players count, or players reward each other in a loop
	end
	if state.inviterClaimsToday >= cfg.inviterDailyCap then
		return { ok = false, reason = "inviter_cap" } -- the invitee still joined; they just get no reward and the inviter is not told why
	end
	return { ok = true, inviter = cfg.inviterReward, invitee = cfg.inviteeReward }
end

export type Step = { count: number, reward: string }

-- milestone ladder: returns the rewards crossed when the total goes from `before` to `after` (so skipping several steps at once pays all)
function InviteReward.milestonesCrossed(ladder: { Step }, before: number, after: number): { string }
	local out = {}
	for _, step in ladder do
		if before < step.count and after >= step.count then
			table.insert(out, step.reward)
		end
	end
	return out
end

-- configuration mistakes caught at server start
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
