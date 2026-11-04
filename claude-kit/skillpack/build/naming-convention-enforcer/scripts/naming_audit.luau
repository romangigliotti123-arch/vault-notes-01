--!strict
local ROOTS: { Instance }? = nil
local APPLY = false
local RENAMES: { [string]: string } = {}
local MAX_LIST = 15

local ReplicatedStorage = game:GetService("ReplicatedStorage")
local ChangeHistoryService = game:GetService("ChangeHistoryService")

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

local function isDefault(name: string): boolean
	local base = string.gsub(name, "[%s_]*%d+$", "")
	return DEFAULTS[base] == true
end

local function isPascal(name: string): boolean
	return string.match(name, "^[A-Z][A-Za-z0-9]*$") ~= nil
end

local function isSegmented(name: string): boolean
	if
		name == ""
		or string.sub(name, 1, 1) == "_"
		or string.sub(name, -1) == "_"
		or string.find(name, "__", 1, true)
	then
		return false
	end
	for seg in string.gmatch(name, "[^_]+") do
		if not (string.match(seg, "^[A-Z][A-Za-z0-9]*$") or string.match(seg, "^%d+$")) then
			return false
		end
	end
	return true
end

local function suggest(name: string, segmented: boolean): string
	local parts: { string } = {}
	for word in string.gmatch(name, "[A-Za-z0-9]+") do
		table.insert(parts, string.upper(string.sub(word, 1, 1)) .. string.sub(word, 2))
	end
	return table.concat(parts, if segmented then "_" else "")
end

local function resolve(path: string): Instance?
	local cur: Instance = game
	for segment in string.gmatch(path, "[^%.]+") do
		local nextInst = cur:FindFirstChild(segment) or (cur == game and game:GetService(segment) or nil)
		if not nextInst then
			return nil
		end
		cur = nextInst
	end
	return cur
end

local function run(): string
	local roots: { Instance } = ROOTS or ({ workspace, ReplicatedStorage } :: { Instance })
	local counts: { [string]: number } = { ["default-name"] = 0, convention = 0, whitespace = 0, duplicate = 0 }
	local examples: { [string]: { string } } = {}
	local function note(kind: string, inst: Instance, extra: string?)
		counts[kind] += 1
		local list = examples[kind]
		if not list then
			list = {}
			examples[kind] = list
		end
		if #list < MAX_LIST then
			table.insert(list, inst:GetFullName() .. (if extra then ` -> {extra}` else ""))
		end
	end
	local scanned = 0
	for _, root in roots do
		local all = root:GetDescendants()
		local seen: { [Instance]: { [string]: boolean } } = {}
		for _, inst in all do
			if not inst:IsA("Terrain") and not inst:IsA("Camera") and inst.Parent then
				scanned += 1
				local name = inst.Name
				local isPart = inst:IsA("BasePart")
				if name ~= string.gsub(string.gsub(name, "^%s+", ""), "%s+$", "") then
					note("whitespace", inst)
				elseif isDefault(name) then
					note("default-name", inst)
				elseif isPart and not isSegmented(name) then
					note("convention", inst, suggest(name, true))
				elseif not isPart and not isPascal(name) then
					note("convention", inst, suggest(name, false))
				end
				local siblings = seen[inst.Parent]
				if not siblings then
					siblings = {}
					seen[inst.Parent] = siblings
				end
				if siblings[name] then
					note("duplicate", inst)
				end
				siblings[name] = true
			end
		end
	end
	local lines = { `NAMING AUDIT: scanned {scanned} instances` }
	for kind, n in counts do
		if n > 0 then
			table.insert(lines, `[{n}] {kind}`)
			for _, e in examples[kind] do
				table.insert(lines, `  e.g. {e}`)
			end
		end
	end
	table.insert(
		lines,
		"before renaming: grep scripts for the old name (FindFirstChild/WaitForChild/paths) and check Rojo file names"
	)
	local renamed = 0
	if APPLY then
		local recording = ChangeHistoryService:TryBeginRecording("naming-convention-enforcer renames")
		for path, newName in RENAMES do
			local inst = resolve(path)
			if inst and inst ~= game then
				inst.Name = newName
				renamed += 1
			else
				table.insert(lines, `rename skipped, path not found: {path}`)
			end
		end
		if recording then
			ChangeHistoryService:FinishRecording(recording, Enum.FinishRecordingOperation.Commit)
		end
		table.insert(lines, `renamed {renamed} instances (one undo step)`)
	else
		table.insert(lines, "read-only run: nothing renamed")
	end
	return table.concat(lines, "\n")
end

local report = run()
print(report)
return report
