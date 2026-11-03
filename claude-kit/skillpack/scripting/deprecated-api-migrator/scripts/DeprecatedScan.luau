--!strict
-- DeprecatedScan: find deprecated or legacy Roblox API use in source text and say what replaces it. Text only.
--   local hits = DeprecatedScan.scan(source)       -- { { line, rule, found, replacement, confidence, note } }
-- confidence "vault" = the vault's knowledge base states it (official or DevForum, with the date in `source`);
-- confidence "general" = widely known but NOT in the vault: live-check the docs before changing code. The deprecation list moves:
-- always re-check the current API reference and release notes before a mass migration.
local DeprecatedScan = {}

export type Rule = {
	id: string,
	kind: string, -- "global" (a bare function call), "method" (:Name( ), "member" (.Name / plain text)
	name: string,
	replacement: string,
	confidence: string,
	source: string,
	note: string?,
}
export type Hit = {
	line: number,
	rule: string,
	found: string,
	replacement: string,
	confidence: string,
	note: string?,
}

DeprecatedScan.RULES = {
	{
		id = "wait",
		kind = "global",
		name = "wait",
		replacement = "task.wait",
		confidence = "vault",
		source = "luau-language-and-types.md (Creator Docs 2026-10)",
	},
	{
		id = "spawn",
		kind = "global",
		name = "spawn",
		replacement = "task.spawn (immediate) or task.defer (next resume point)",
		confidence = "vault",
		source = "luau-language-and-types.md",
	},
	{
		id = "delay",
		kind = "global",
		name = "delay",
		replacement = "task.delay",
		confidence = "vault",
		source = "luau-language-and-types.md",
	},
	{
		id = "ypcall",
		kind = "global",
		name = "ypcall",
		replacement = "pcall",
		confidence = "vault",
		source = "luau-language-and-types.md (DevForum 2021-08)",
	},
	{
		id = "FindPartOnRay",
		kind = "method",
		name = "FindPartOnRay",
		replacement = "workspace:Raycast(origin, direction, params)",
		confidence = "vault",
		source = "scripting-and-performance.md",
	},
	{
		id = "FindPartOnRayWithIgnoreList",
		kind = "method",
		name = "FindPartOnRayWithIgnoreList",
		replacement = "workspace:Raycast with RaycastParams.ExcludeInstances",
		confidence = "vault",
		source = "scripting-and-performance.md",
	},
	{
		id = "FindPartOnRayWithWhitelist",
		kind = "method",
		name = "FindPartOnRayWithWhitelist",
		replacement = "workspace:Raycast with RaycastParams.IncludeInstances",
		confidence = "vault",
		source = "scripting-and-performance.md",
	},
	{
		id = "FilterDescendantsInstances",
		kind = "member",
		name = "FilterDescendantsInstances",
		replacement = "RaycastParams.ExcludeInstances / IncludeInstances (faster, 2026 API)",
		confidence = "vault",
		source = "scripting-and-performance.md (DevForum 2026-04)",
		note = "older but still works; migrate new code",
	},
	{
		id = "PromptProductPurchaseFinished",
		kind = "member",
		name = "PromptProductPurchaseFinished",
		replacement = "MarketplaceService.ProcessReceipt (grant, then return PurchaseGranted)",
		confidence = "vault",
		source = "anti-exploit-and-security.md",
		note = "never grant from the client-side prompt events",
	},
	{
		id = "PromptGamePassPurchaseFinished",
		kind = "member",
		name = "PromptGamePassPurchaseFinished",
		replacement = "UserOwnsGamePassAsync check on the server after the prompt closes",
		confidence = "vault",
		source = "anti-exploit-and-security.md",
	},
	{
		id = "CollisionGroupSetCollidable",
		kind = "method",
		name = "CollisionGroupSetCollidable",
		replacement = "the WorldRoot equivalent (read the current docs for the exact name)",
		confidence = "vault",
		source = "building-art-and-assets.md (official 2026-09-03)",
	},
	{
		id = "RegisterCollisionGroup",
		kind = "method",
		name = "RegisterCollisionGroup",
		replacement = "the WorldRoot equivalent (read the current docs for the exact name)",
		confidence = "vault",
		source = "building-art-and-assets.md (official 2026-09-03)",
	},
	{
		id = "CollisionGroupsAreCollidable",
		kind = "method",
		name = "CollisionGroupsAreCollidable",
		replacement = "the WorldRoot equivalent",
		confidence = "vault",
		source = "building-art-and-assets.md (official 2026-09-03)",
	},
	{
		id = "GetRegisteredCollisionGroups",
		kind = "method",
		name = "GetRegisteredCollisionGroups",
		replacement = "the WorldRoot equivalent",
		confidence = "vault",
		source = "building-art-and-assets.md (official 2026-09-03)",
	},
	{
		id = "getfenv",
		kind = "global",
		name = "getfenv",
		replacement = "restructure; modules and explicit parameters",
		confidence = "vault",
		source = "luau-language-and-types.md",
		note = "also disables native-code optimisations",
	},
	{
		id = "setfenv",
		kind = "global",
		name = "setfenv",
		replacement = "restructure; modules and explicit parameters",
		confidence = "vault",
		source = "luau-language-and-types.md",
	},
	{
		id = "BodyVelocity",
		kind = "member",
		name = "BodyVelocity",
		replacement = "LinearVelocity",
		confidence = "general",
		source = "not in vault",
	},
	{
		id = "BodyPosition",
		kind = "member",
		name = "BodyPosition",
		replacement = "AlignPosition",
		confidence = "general",
		source = "not in vault",
	},
	{
		id = "BodyGyro",
		kind = "member",
		name = "BodyGyro",
		replacement = "AlignOrientation",
		confidence = "general",
		source = "not in vault",
	},
	{
		id = "BodyForce",
		kind = "member",
		name = "BodyForce",
		replacement = "VectorForce",
		confidence = "general",
		source = "not in vault",
	},
	{
		id = "SetPrimaryPartCFrame",
		kind = "method",
		name = "SetPrimaryPartCFrame",
		replacement = "Model:PivotTo(cframe)",
		confidence = "general",
		source = "not in vault",
	},
	{
		id = "Humanoid:LoadAnimation",
		kind = "method",
		name = "LoadAnimation",
		replacement = "Animator:LoadAnimation (get the Animator from the Humanoid or AnimationController)",
		confidence = "general",
		source = "not in vault",
		note = "only when called on a Humanoid; Animator:LoadAnimation is the supported form",
	},
	{
		id = "unpack",
		kind = "global",
		name = "unpack",
		replacement = "table.unpack",
		confidence = "general",
		source = "not in vault",
	},
	{
		id = "lowercase-connect",
		kind = "method",
		name = "connect",
		replacement = ":Connect",
		confidence = "general",
		source = "not in vault",
	},
	{
		id = "lowercase-remove",
		kind = "method",
		name = "remove",
		replacement = ":Destroy()",
		confidence = "general",
		source = "not in vault",
	},
} :: { Rule }

-- true when `name` at `position` is a standalone identifier (not task.wait, not :Wait, not my_wait)
local function isBare(code: string, position: number): boolean
	local before = if position > 1 then string.sub(code, position - 1, position - 1) else ""
	return not string.match(before, "[%w_%.:]")
end

local function stripComment(line: string): string
	return (string.gsub(line, "%-%-.*$", ""))
end

function DeprecatedScan.scan(source: string, rules: { Rule }?): { Hit }
	local active: { Rule } = rules or DeprecatedScan.RULES
	local hits: { Hit } = {}
	local n = 0
	for line in string.gmatch(source .. "\n", "(.-)\n") do
		n += 1
		local code = stripComment(line)
		for _, rule in active do
			local found = false
			if rule.kind == "global" then
				local from = 1
				while true do
					local s = string.find(code, rule.name .. "%s*%(", from)
					if s == nil then
						break
					end
					if isBare(code, s) then
						found = true
						break
					end
					from = s + 1
				end
			elseif rule.kind == "method" then
				found = string.find(code, ":" .. rule.name .. "%s*%(") ~= nil
				if rule.id == "Humanoid:LoadAnimation" then
					found = found and string.find(code, "[Hh]umanoid[%w_]*%s*:LoadAnimation") ~= nil
				end
			else
				local s = string.find(code, rule.name, 1, true)
				found = s ~= nil and not string.match(string.sub(code, s - 1, s - 1), "[%w_]")
			end
			if found then
				table.insert(hits, {
					line = n,
					rule = rule.id,
					found = rule.name,
					replacement = rule.replacement,
					confidence = rule.confidence,
					note = rule.note,
				})
			end
		end
	end
	return hits
end

-- counts per rule, vault-backed rules first, for the migration plan
function DeprecatedScan.summarize(hits: { Hit }): { { rule: string, count: number, confidence: string } }
	local counts: { [string]: { rule: string, count: number, confidence: string } } = {}
	for _, h in hits do
		local c = counts[h.rule]
		if c == nil then
			c = { rule = h.rule, count = 0, confidence = h.confidence }
			counts[h.rule] = c
		end
		c.count += 1
	end
	local list = {}
	for _, c in counts do
		table.insert(list, c)
	end
	table.sort(list, function(a, b)
		if a.confidence ~= b.confidence then
			return a.confidence == "vault"
		end
		return a.rule < b.rule
	end)
	return list
end

return DeprecatedScan
