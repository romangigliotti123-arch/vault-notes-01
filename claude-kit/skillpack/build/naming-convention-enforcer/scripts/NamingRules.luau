--!strict
-- NamingRules: the naming convention checker behind naming_audit.luau. Pure logic, unit-tested under Lune.
-- Convention (default, change per project): Models, Folders, Scripts and Modules are PascalCase; parts may use PascalCase segments
-- joined by underscores (Wall_North_02); no default engine names; no leading/trailing spaces; unique among siblings. Names are
-- API: scripts find children by name and Rojo maps them to file names, so rename with care (see SKILL.md Pitfalls).
local NamingRules = {}

export type Issue = { name: string, class: string, kind: string, suggestion: string? }

local DEFAULTS: { [string]: boolean } = {
	Part = true,
	MeshPart = true,
	UnionOperation = true,
	Model = true,
	Folder = true,
	WedgePart = true,
	Script = true,
	LocalScript = true,
	ModuleScript = true,
	SpawnLocation = true,
	Attachment = true,
	Decal = true,
	Texture = true,
	Sound = true,
}

local SEGMENT_CLASSES: { [string]: boolean } = { BasePart = true }

function NamingRules.isDefault(name: string): boolean
	local base = string.gsub(name, "[%s_]*%d+$", "")
	return DEFAULTS[base] == true
end

local function validSegment(seg: string): boolean
	return string.match(seg, "^[A-Z][A-Za-z0-9]*$") ~= nil or string.match(seg, "^%d+$") ~= nil
end

function NamingRules.isPascal(name: string): boolean
	return string.match(name, "^[A-Z][A-Za-z0-9]*$") ~= nil
end

function NamingRules.isSegmented(name: string): boolean
	if name == "" then
		return false
	end
	for seg in string.gmatch(name, "[^_]+") do
		if not validSegment(seg) then
			return false
		end
	end
	return string.sub(name, 1, 1) ~= "_" and string.sub(name, -1) ~= "_" and not string.find(name, "__", 1, true)
end

-- Suggest a convention-friendly spelling. Never invents meaning: default names get no suggestion.
function NamingRules.suggest(name: string, segmented: boolean): string
	local trimmed = string.gsub(name, "^%s+", "")
	trimmed = string.gsub(trimmed, "%s+$", "")
	local parts: { string } = {}
	for word in string.gmatch(trimmed, "[A-Za-z0-9]+") do
		table.insert(parts, string.upper(string.sub(word, 1, 1)) .. string.sub(word, 2))
	end
	return table.concat(parts, if segmented then "_" else "")
end

local function expectsSegments(class: string): boolean
	return SEGMENT_CLASSES[class] == true
end

-- class group: "BasePart" for any part, otherwise the ClassName
function NamingRules.check(name: string, classGroup: string): { Issue }
	local issues: { Issue } = {}
	local function add(kind: string, suggestion: string?)
		table.insert(issues, { name = name, class = classGroup, kind = kind, suggestion = suggestion })
	end
	if name ~= string.gsub(string.gsub(name, "^%s+", ""), "%s+$", "") then
		add("whitespace", NamingRules.suggest(name, expectsSegments(classGroup)))
		return issues
	end
	if NamingRules.isDefault(name) then
		add("default-name", nil)
		return issues
	end
	if expectsSegments(classGroup) then
		if not NamingRules.isSegmented(name) then
			add("convention", NamingRules.suggest(name, true))
		end
	elseif not NamingRules.isPascal(name) then
		add("convention", NamingRules.suggest(name, false))
	end
	return issues
end

function NamingRules.duplicates(siblings: { string }): { string }
	local count: { [string]: number } = {}
	local out: { string } = {}
	for _, n in siblings do
		count[n] = (count[n] or 0) + 1
		if count[n] == 2 then
			table.insert(out, n)
		end
	end
	return out
end

return NamingRules
