--!nocheck
-- Run from the kit's systems folder: lune run ../skillpack/community/clan-system-planner/scripts/tests/ClanRules.test.luau
local t = require("../../../../../systems/_check/harness")
local ClanRules = require("../ClanRules")

local function clan()
	return { name = "Night Owls", members = { [1] = "leader", [2] = "officer", [3] = "member", [4] = "member" }, banned = { [9] = true }, maxSize = 5 }
end

t.test("names: shape rules", function()
	t.truthy(ClanRules.validName("Night Owls"))
	t.truthy(ClanRules.validName("ABC"))
	t.falsy(ClanRules.validName("ab"))
	t.falsy(ClanRules.validName(string.rep("a", 21)))
	t.falsy(ClanRules.validName(" lead"))
	t.falsy(ClanRules.validName("trail "))
	t.falsy(ClanRules.validName("two  spaces"))
	t.falsy(ClanRules.validName("sym!bol"))
	t.falsy(ClanRules.validName(5))
end)

t.test("join: member, banned and full are refused", function()
	local c = clan()
	local ok, why = ClanRules.canJoin(c, 5)
	t.truthy(ok)
	ok, why = ClanRules.canJoin(c, 3)
	t.eq(why, "already_member")
	ok, why = ClanRules.canJoin(c, 9)
	t.eq(why, "banned")
	c.members[5] = "member"
	ok, why = ClanRules.canJoin(c, 6)
	t.eq(why, "full")
end)

t.test("kick: only strictly higher ranks, never the leader, never yourself", function()
	local c = clan()
	t.truthy((ClanRules.canKick(c, 1, 2)))
	t.truthy((ClanRules.canKick(c, 2, 3)))
	local ok, why = ClanRules.canKick(c, 2, 1)
	t.eq(why, "rank_too_low")
	ok, why = ClanRules.canKick(c, 3, 4)
	t.eq(why, "rank_too_low")
	ok, why = ClanRules.canKick(c, 2, 2)
	t.eq(why, "use_leave")
	ok, why = ClanRules.canKick(c, 1, 99)
	t.eq(why, "not_member")
end)

t.test("rank changes: leader only", function()
	local c = clan()
	t.truthy((ClanRules.canSetRank(c, 1, 3, "officer")))
	t.falsy((ClanRules.canSetRank(c, 2, 3, "officer")))
	t.falsy((ClanRules.canSetRank(c, 1, 3, "boss")))
	t.falsy((ClanRules.canSetRank(c, 1, 1, "member")))
end)

t.test("leader cannot leave a populated clan", function()
	local c = clan()
	local ok, why = ClanRules.canLeave(c, 1)
	t.eq(why, "transfer_first")
	t.truthy((ClanRules.canLeave(c, 3)))
	local solo = { name = "Solo Run", members = { [1] = "leader" }, banned = {}, maxSize = 5 }
	t.truthy((ClanRules.canLeave(solo, 1)))
end)

t.test("validate: one leader, size cap, good name", function()
	t.eq(#ClanRules.validate(clan()), 0)
	local two = clan()
	two.members[2] = "leader"
	t.eq(#ClanRules.validate(two), 1)
	local none = clan()
	none.members[1] = "member"
	none.name = "x"
	none.maxSize = 3
	t.eq(#ClanRules.validate(none), 3)
end)

t.done()
