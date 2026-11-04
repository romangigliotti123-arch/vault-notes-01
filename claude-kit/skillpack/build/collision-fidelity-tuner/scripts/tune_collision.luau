--!strict
local ROOT: Instance? = nil
local APPLY_DECOR = false
local APPLY_FIDELITY = false
local FIDELITY_TARGET = Enum.CollisionFidelity.Hull
local DECOR_WORDS =
	{ "grass", "vine", "flower", "leaf", "leaves", "bush", "decor", "detail", "pebble", "weed", "petal" }
local MAX_LIST = 12

local ChangeHistoryService = game:GetService("ChangeHistoryService")

local function scriptNames(): (string, boolean)
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

local function looksDecor(name: string): boolean
	local lower = string.lower(name)
	for _, w in DECOR_WORDS do
		if string.find(lower, w, 1, true) then
			return true
		end
	end
	return false
end

local function run(): string
	local root = ROOT or workspace
	local sources, sourcesComplete = scriptNames()
	local decor: { BasePart } = {}
	local precise: { BasePart } = {}
	local invisibleWalls, touchOnInvisible, total = 0, 0, 0
	local mentioned = 0
	for _, inst in root:GetDescendants() do
		if inst:IsA("BasePart") and not inst:IsA("Terrain") then
			local part = inst :: BasePart
			total += 1
			local isMentioned = string.find(sources, part.Name, 1, true) ~= nil
			if looksDecor(part.Name) and (part.CanCollide or part.CanTouch or part.CanQuery) then
				if isMentioned then
					mentioned += 1
				else
					table.insert(decor, part)
				end
			end
			if part:IsA("MeshPart") or part:IsA("UnionOperation") then
				local fid = (part :: any).CollisionFidelity
				if fid == Enum.CollisionFidelity.PreciseConvexDecomposition then
					table.insert(precise, part)
				end
			end
			if part.Transparency >= 1 and part.CanCollide then
				invisibleWalls += 1
				if part.CanTouch then
					touchOnInvisible += 1
				end
			end
		end
	end
	local lines = {
		`COLLISION AUDIT: {root:GetFullName()} parts={total}`,
		`[{#decor}] decorative-looking parts still collide/touch/query (not named in any script) -> APPLY_DECOR turns all three off`,
		`[{mentioned}] decorative-looking parts left alone because a script mentions their name`,
		`[{#precise}] PreciseConvexDecomposition -> APPLY_FIDELITY sets {FIDELITY_TARGET.Name} (check the shape still blocks players correctly)`,
		`[{invisibleWalls}] invisible collidable parts (intended walls?); {touchOnInvisible} also fire Touched: CanTouch off if nothing listens`,
	}
	for i = 1, math.min(MAX_LIST, #decor) do
		table.insert(lines, `  decor e.g. {decor[i]:GetFullName()}`)
	end
	for i = 1, math.min(MAX_LIST, #precise) do
		table.insert(lines, `  precise e.g. {precise[i]:GetFullName()}`)
	end
	if APPLY_DECOR and not sourcesComplete then
		table.insert(
			lines,
			"APPLY_DECOR refused: some script sources could not be read, so name references are unknown"
		)
		APPLY_DECOR = false
	end
	if APPLY_DECOR or APPLY_FIDELITY then
		local recording = ChangeHistoryService:TryBeginRecording("collision-fidelity-tuner")
		local changed = 0
		if APPLY_DECOR then
			for _, part in decor do
				part.CanCollide, part.CanTouch, part.CanQuery = false, false, false
				changed += 1
			end
		end
		if APPLY_FIDELITY then
			for _, part in precise do
				(part :: any).CollisionFidelity = FIDELITY_TARGET
				changed += 1
			end
		end
		if recording then
			ChangeHistoryService:FinishRecording(recording, Enum.FinishRecordingOperation.Commit)
		end
		table.insert(lines, `changed {changed} parts (one undo step)`)
	else
		table.insert(lines, "read-only run: nothing changed")
	end
	return table.concat(lines, "\n")
end

local report = run()
print(report)
return report
