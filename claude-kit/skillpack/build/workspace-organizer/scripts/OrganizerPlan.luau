--!strict
local OrganizerPlan = {}

export type Item = { name: string, class: string, tagged: boolean?, hasScripts: boolean? }
export type Move = { name: string, folder: string, reason: string }
export type Plan = { moves: { Move }, keep: { string }, folders: { string } }

local KEEP_CLASSES: { [string]: boolean } = {
	Terrain = true,
	Camera = true,
	Folder = true,
	Script = true,
	LocalScript = true,
	ModuleScript = true,
}
local LIGHTS: { [string]: boolean } = { PointLight = true, SpotLight = true, SurfaceLight = true }
local PART_CLASSES: { [string]: boolean } =
	{ Part = true, MeshPart = true, UnionOperation = true, WedgePart = true, TrussPart = true }

local PROP_WORDS = { "tree", "rock", "lamp", "crate", "barrel", "bush", "fence", "prop", "decor", "flower", "sign" }
local ZONE_WORDS = { "zone", "trigger", "region", "hitbox", "killbrick", "checkpoint" }

local function hasWord(name: string, words: { string }): boolean
	local lower = string.lower(name)
	for _, w in words do
		if string.find(lower, w, 1, true) then
			return true
		end
	end
	return false
end

function OrganizerPlan.folderFor(it: Item): (string?, string)
	if KEEP_CLASSES[it.class] then
		return nil, "engine/organising class"
	end
	if it.class == "SpawnLocation" then
		return "Spawns", "spawn"
	end
	if it.class == "Sound" then
		return "Audio", "sound"
	end
	if LIGHTS[it.class] then
		return "Lights", "light"
	end
	if it.class == "Model" or PART_CLASSES[it.class] then
		if hasWord(it.name, ZONE_WORDS) then
			return "Zones", "name looks like a trigger/zone"
		end
		if hasWord(it.name, PROP_WORDS) then
			return "Props", "name looks like a prop"
		end
		if it.hasScripts then
			return "Interactive", "contains scripts"
		end
		return "Map", "loose model/part"
	end
	return "Misc", "other class " .. it.class
end

function OrganizerPlan.plan(items: { Item }): Plan
	local moves: { Move } = {}
	local keep: { string } = {}
	local seen: { [string]: boolean } = {}
	local folders: { string } = {}
	for _, it in items do
		local folder, reason = OrganizerPlan.folderFor(it)
		if folder then
			table.insert(moves, { name = it.name, folder = folder, reason = reason })
			if not seen[folder] then
				seen[folder] = true
				table.insert(folders, folder)
			end
		else
			table.insert(keep, it.name)
		end
	end
	table.sort(folders)
	return { moves = moves, keep = keep, folders = folders }
end

return OrganizerPlan
