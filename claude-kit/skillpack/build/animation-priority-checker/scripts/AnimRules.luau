--!strict
local AnimRules = {}

export type Rule = { keywords: { string }, minPriority: string, maxPriority: string?, looped: boolean? }
export type Issue = { animation: string, kind: string, note: string }

local ORDER: { string } = { "Core", "Idle", "Movement", "Action", "Action2", "Action3", "Action4" }
local RANK: { [string]: number } = {}
for i, p in ORDER do
	RANK[p] = i
end

AnimRules.RULES = {
	{ keywords = { "idle", "stand", "breath" }, minPriority = "Idle", maxPriority = "Idle", looped = true },
	{
		keywords = { "walk", "run", "sprint", "swim", "climb" },
		minPriority = "Movement",
		maxPriority = "Movement",
		looped = true,
	},
	{ keywords = { "jump", "fall", "land" }, minPriority = "Movement", looped = false },
	{
		keywords = { "attack", "swing", "punch", "slash", "shoot", "reload", "cast", "emote", "dance", "wave" },
		minPriority = "Action",
		looped = false,
	},
} :: { Rule }

function AnimRules.rank(priority: string): number?
	return RANK[priority]
end

local function ruleFor(name: string): Rule?
	local lower = string.lower(name)
	for _, rule in AnimRules.RULES do
		for _, k in rule.keywords do
			if string.find(lower, k, 1, true) then
				return rule
			end
		end
	end
	return nil
end

function AnimRules.check(name: string, priority: string, looped: boolean): { Issue }
	local issues: { Issue } = {}
	local r = RANK[priority]
	if not r then
		table.insert(issues, { animation = name, kind = "priority", note = "unknown priority " .. priority })
		return issues
	end
	local rule = ruleFor(name)
	if not rule then
		if priority == "Core" then
			table.insert(issues, {
				animation = name,
				kind = "priority",
				note = "Core is the lowest level and loses to every default animation",
			})
		end
		return issues
	end
	if r < (RANK[rule.minPriority] :: number) then
		table.insert(issues, {
			animation = name,
			kind = "priority",
			note = `{priority} is below {rule.minPriority}: the default animations will override it`,
		})
	end
	if rule.maxPriority and r > (RANK[rule.maxPriority] :: number) then
		table.insert(issues, {
			animation = name,
			kind = "priority",
			note = `{priority} is above {rule.maxPriority}: it will block actions that should play over it`,
		})
	end
	if rule.looped ~= nil and rule.looped ~= looped then
		table.insert(issues, {
			animation = name,
			kind = "looped",
			note = if rule.looped then "should loop" else "should not loop (it would repeat forever)",
		})
	end
	return issues
end

return AnimRules
