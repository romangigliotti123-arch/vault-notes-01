--!strict
-- organize.luau: sort loose top-level Workspace children into folders. Dry-run by default. Uses the rules in scripts/OrganizerPlan.luau
-- (tested under Lune; inlined here). Names are NEVER changed, only parents, so Rojo file names stay valid.
-- Paste into the Studio command bar or send through the Studio MCP `execute_luau` tool (datamodel_type Edit).
-- Safety: an object whose name appears in any script source is skipped when SKIP_REFERENCED is true (scripts like workspace.Door or
-- FindFirstChild("Door") would break). If script sources cannot be read, APPLY refuses to run.
local APPLY = false
local SKIP_REFERENCED = true
local MAX_LIST = 25

local ChangeHistoryService = game:GetService("ChangeHistoryService")

local KEEP: { [string]: boolean } = {
	Terrain = true,
	Camera = true,
	Folder = true,
	Script = true,
	LocalScript = true,
	ModuleScript = true,
}
local LIGHTS: { [string]: boolean } = { PointLight = true, SpotLight = true, SurfaceLight = true }
local PARTS: { [string]: boolean } =
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

local function folderFor(inst: Instance): string?
	local class = inst.ClassName
	if KEEP[class] then
		return nil
	elseif class == "SpawnLocation" then
		return "Spawns"
	elseif class == "Sound" then
		return "Audio"
	elseif LIGHTS[class] then
		return "Lights"
	elseif class == "Model" or PARTS[class] then
		if hasWord(inst.Name, ZONE_WORDS) then
			return "Zones"
		elseif hasWord(inst.Name, PROP_WORDS) then
			return "Props"
		elseif inst:FindFirstChildWhichIsA("LuaSourceContainer", true) then
			return "Interactive"
		end
		return "Map"
	end
	return "Misc"
end

local function sources(): (string, boolean)
	local chunks: { string } = {}
	local complete = true
	for _, inst in game:GetDescendants() do
		if inst:IsA("LuaSourceContainer") then
			local ok, src = pcall(function()
				return (inst :: any).Source
			end)
			if ok and type(src) == "string" then
				table.insert(chunks, src)
			else
				complete = false
			end
		end
	end
	return table.concat(chunks, "\n"), complete
end

local function run(): string
	local allSource, complete = sources()
	local moves: { { inst: Instance, folder: string } } = {}
	local referenced: { string } = {}
	local kept = 0
	for _, child in workspace:GetChildren() do
		local folder = folderFor(child)
		if not folder then
			kept += 1
		elseif SKIP_REFERENCED and string.find(allSource, child.Name, 1, true) then
			table.insert(referenced, child.Name)
		else
			table.insert(moves, { inst = child, folder = folder })
		end
	end
	local lines = {
		`WORKSPACE ORGANIZER: {#moves} to move, {#referenced} skipped (name found in a script), {kept} kept in place`,
	}
	for i = 1, math.min(MAX_LIST, #moves) do
		table.insert(lines, `  {moves[i].inst.Name} ({moves[i].inst.ClassName}) -> {moves[i].folder}`)
	end
	for i = 1, math.min(MAX_LIST, #referenced) do
		table.insert(lines, `  skipped (referenced): {referenced[i]}`)
	end
	if APPLY and not complete then
		table.insert(lines, "APPLY refused: some script sources could not be read, so references are unknown")
	elseif APPLY and #moves > 0 then
		local recording = ChangeHistoryService:TryBeginRecording("workspace-organizer")
		local function folderNamed(name: string): Folder
			local existing = workspace:FindFirstChild(name)
			if existing and existing:IsA("Folder") then
				return existing
			end
			local f = Instance.new("Folder")
			f.Name = name
			f.Parent = workspace
			return f
		end
		for _, m in moves do
			m.inst.Parent = folderNamed(m.folder)
		end
		if recording then
			ChangeHistoryService:FinishRecording(recording, Enum.FinishRecordingOperation.Commit)
		end
		table.insert(lines, `moved {#moves} objects (one undo step)`)
	else
		table.insert(lines, "dry run: nothing moved")
	end
	return table.concat(lines, "\n")
end

local report = run()
print(report)
return report
