--!strict
-- ClanRules: the pure permission and validation rules of an in-game clan, no DataStore and no Instances (testable under Lune).
-- The server wires it up:
--   * every action arrives from a RemoteEvent the SERVER validates (kit RemoteGuard); the client never states its own rank, the server
--     reads it from the clan record.
--   * the clan name (and any tag or message) is also passed through TextService:FilterStringAsync on the server before it is stored
--     or shown. ClanRules.validName only checks shape, it is not the filter.
--   * clan records are saved with UpdateAsync so two officers acting at once cannot both take the last slot.
local ClanRules = {}

export type Rank = "member" | "officer" | "leader"
export type Clan = {
	name: string,
	members: { [number]: Rank }, -- userId -> rank
	banned: { [number]: boolean },
	maxSize: number,
}

local LEVEL: { [string]: number } = { member = 1, officer = 2, leader = 3 }

-- 3-20 chars, letters, digits and single inner spaces; no leading, trailing or doubled spaces
function ClanRules.validName(name: any): boolean
	if type(name) ~= "string" or #name < 3 or #name > 20 then
		return false
	end
	if string.find(name, "[^%w ]") or string.find(name, "^ ") or string.find(name, " $") or string.find(name, "  ") then
		return false
	end
	return true
end

local function size(clan: Clan): number
	local n = 0
	for _ in clan.members do
		n += 1
	end
	return n
end
ClanRules.size = size

function ClanRules.canJoin(clan: Clan, userId: number): (boolean, string?)
	if clan.members[userId] then
		return false, "already_member"
	end
	if clan.banned[userId] then
		return false, "banned"
	end
	if size(clan) >= clan.maxSize then
		return false, "full"
	end
	return true, nil
end

-- an actor may remove someone strictly below their own rank; the leader can never be kicked; leaving is separate
function ClanRules.canKick(clan: Clan, actor: number, target: number): (boolean, string?)
	local a, b = clan.members[actor], clan.members[target]
	if not a or not b then
		return false, "not_member"
	end
	if actor == target then
		return false, "use_leave"
	end
	if LEVEL[a] <= LEVEL[b] or LEVEL[a] < LEVEL.officer then
		return false, "rank_too_low"
	end
	return true, nil
end

-- only the leader promotes to officer or hands over leadership; officers cannot promote anyone
function ClanRules.canSetRank(clan: Clan, actor: number, target: number, newRank: Rank): (boolean, string?)
	local a, b = clan.members[actor], clan.members[target]
	if not a or not b or LEVEL[newRank] == nil then
		return false, "invalid"
	end
	if a ~= "leader" then
		return false, "rank_too_low"
	end
	if actor == target then
		return false, "invalid"
	end
	return true, nil
end

-- the leader cannot just leave: the clan must have a leader at all times (transfer first, or disband when alone)
function ClanRules.canLeave(clan: Clan, userId: number): (boolean, string?)
	local r = clan.members[userId]
	if not r then
		return false, "not_member"
	end
	if r == "leader" and size(clan) > 1 then
		return false, "transfer_first"
	end
	return true, nil
end

-- shape of a clan record loaded from storage: exactly one leader, size within the cap
function ClanRules.validate(clan: Clan): { string }
	local problems = {}
	local leaders = 0
	for _, r in clan.members do
		if LEVEL[r] == nil then
			table.insert(problems, "unknown rank")
		elseif r == "leader" then
			leaders += 1
		end
	end
	if leaders ~= 1 then
		table.insert(problems, `needs exactly one leader, has {leaders}`)
	end
	if size(clan) > clan.maxSize then
		table.insert(problems, "over max size")
	end
	if not ClanRules.validName(clan.name) then
		table.insert(problems, "bad name")
	end
	return problems
end

return ClanRules
