--!nocheck
-- Run from the kit's systems folder: lune run ../skillpack/community/friend-invite-reward-builder/scripts/tests/InviteReward.test.luau
local t = require("../../../../../systems/_check/harness")
local InviteReward = require("../InviteReward")

local cfg = { inviterDailyCap = 3, inviteeReward = "StarterPet", inviterReward = "Coins200" }
local function st(over)
	local s = { isFirstJoin = true, inviteeClaimed = false, inviterClaimsToday = 0 }
	for k, v in over or {} do
		s[k] = v
	end
	return s
end

t.test("a new player joining through a friend rewards both sides", function()
	local r = InviteReward.decide(cfg, 111, 222, st())
	t.truthy(r.ok)
	t.eq(r.inviter, "Coins200")
	t.eq(r.invitee, "StarterPet")
end)

t.test("no referrer, junk referrer and self referral are refused", function()
	t.eq(InviteReward.decide(cfg, nil, 222, st()).reason, "no_referrer")
	t.eq(InviteReward.decide(cfg, "111", 222, st()).reason, "no_referrer")
	t.eq(InviteReward.decide(cfg, -5, 222, st()).reason, "no_referrer")
	t.eq(InviteReward.decide(cfg, 1.5, 222, st()).reason, "no_referrer")
	t.eq(InviteReward.decide(cfg, 222, 222, st()).reason, "self_referral")
end)

t.test("an invitee can claim once, and only if new to the experience", function()
	t.eq(InviteReward.decide(cfg, 111, 222, st({ inviteeClaimed = true })).reason, "already_claimed")
	t.eq(InviteReward.decide(cfg, 111, 222, st({ isFirstJoin = false })).reason, "not_new")
end)

t.test("the inviter daily cap stops farming", function()
	t.truthy(InviteReward.decide(cfg, 111, 222, st({ inviterClaimsToday = 2 })).ok)
	t.eq(InviteReward.decide(cfg, 111, 222, st({ inviterClaimsToday = 3 })).reason, "inviter_cap")
end)

t.test("milestones pay every step crossed, once", function()
	local ladder = { { count = 1, reward = "A" }, { count = 5, reward = "B" }, { count = 10, reward = "C" } }
	t.eq(InviteReward.milestonesCrossed(ladder, 0, 1)[1], "A")
	t.eq(#InviteReward.milestonesCrossed(ladder, 1, 4), 0)
	t.eq(#InviteReward.milestonesCrossed(ladder, 4, 10), 2)
	t.eq(#InviteReward.milestonesCrossed(ladder, 10, 10), 0)
end)

t.test("validate catches a bad config", function()
	t.eq(#InviteReward.validate(cfg, { { count = 1, reward = "A" }, { count = 5, reward = "B" } }), 0)
	local bad = { inviterDailyCap = 0, inviteeReward = "", inviterReward = "x" }
	t.eq(#InviteReward.validate(bad, { { count = 5, reward = "A" }, { count = 5, reward = "B" } }), 3)
end)

t.done()
