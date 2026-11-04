--!strict
local ROOT: Instance? = nil
local APPLY_MODES = false
local MAX_EXTENT = 64
local MAX_PARTS = 2000
local MAX_LIST = 25

local CollectionService = game:GetService("CollectionService")
local ChangeHistoryService = game:GetService("ChangeHistoryService")

local function read(inst: Instance, prop: string): string
	local ok, value = pcall(function()
		return (inst :: any)[prop]
	end)
	return if ok then tostring(value) else "n/a"
end

type Row = {
	model: Model,
	parts: number,
	scripted: boolean,
	essential: boolean,
	dynamic: boolean,
	extent: number,
	want: string,
}

local function run(): string
	local root = ROOT or workspace
	local lines = { "LOD / STREAMING AUDIT" }
	for _, prop in
		{
			"StreamingEnabled",
			"StreamingMinRadius",
			"StreamingTargetRadius",
			"StreamingIntegrityMode",
			"ModelStreamingBehavior",
			"PredictiveStreamingMode",
		}
	do
		table.insert(lines, `Workspace.{prop} = {read(workspace, prop)}`)
	end
	if read(workspace, "StreamingEnabled") ~= "true" then
		table.insert(
			lines,
			"streaming is OFF: SLIM falls back to traditional LOD and models stream nothing (vault: enable it, develop with it on)"
		)
	end
	local rows: { Row } = {}
	local persistent, slim = 0, 0
	for _, child in root:GetChildren() do
		if child:IsA("Model") and not child:FindFirstChildOfClass("Humanoid") then
			local m = child :: Model
			local parts = 0
			for _, d in m:GetDescendants() do
				if d:IsA("BasePart") then
					parts += 1
				end
			end
			local scripted = m:FindFirstChildWhichIsA("LuaSourceContainer", true) ~= nil
			local essential = m:GetAttribute("Essential") == true or CollectionService:HasTag(m, "Essential")
			local dynamic = m:GetAttribute("Dynamic") == true or CollectionService:HasTag(m, "Dynamic")
			local _, size = m:GetBoundingBox()
			local want = if essential then "Persistent" elseif scripted then "Atomic" else "Default"
			if want == "Persistent" then
				persistent += 1
			end
			if not scripted and not essential and not dynamic then
				slim += 1
			end
			table.insert(rows, {
				model = m,
				parts = parts,
				scripted = scripted,
				essential = essential,
				dynamic = dynamic,
				extent = math.max(size.X, size.Y, size.Z),
				want = want,
			})
		end
	end
	table.sort(rows, function(a, b)
		return a.parts > b.parts
	end)
	table.insert(lines, `models={#rows} SLIM candidates={slim} Persistent wanted={persistent}`)
	local toSet: { Row } = {}
	for i, r in rows do
		local current = read(r.model, "ModelStreamingMode")
		local notes: { string } = {}
		if r.extent > MAX_EXTENT then
			table.insert(notes, `extent {string.format("%.0f", r.extent)} > {MAX_EXTENT}: split`)
		end
		if r.parts > MAX_PARTS then
			table.insert(notes, `{r.parts} parts: split`)
		end
		if r.want ~= "Default" and current == "Default" then
			table.insert(notes, `set ModelStreamingMode {r.want}`)
			table.insert(toSet, r)
		end
		if i <= MAX_LIST then
			table.insert(
				lines,
				`  {r.model.Name}: parts={r.parts} mode={current} LOD={read(r.model, "LevelOfDetail")} {table.concat(
					notes,
					"; "
				)}`
			)
		end
	end
	if #rows > 0 and persistent / #rows > 0.1 then
		table.insert(
			lines,
			"more than 10 percent of models want Persistent: overuse hurts performance, re-check which are really always needed"
		)
	end
	if APPLY_MODES and #toSet > 0 then
		local recording = ChangeHistoryService:TryBeginRecording("lod-planner streaming modes")
		for _, r in toSet do
			local ok = pcall(function()
				(r.model :: any).ModelStreamingMode = (Enum.ModelStreamingMode :: any)[r.want]
			end)
			if not ok then
				table.insert(lines, `could not set {r.model.Name}`)
			end
		end
		if recording then
			ChangeHistoryService:FinishRecording(recording, Enum.FinishRecordingOperation.Commit)
		end
		table.insert(lines, `set ModelStreamingMode on {#toSet} models (one undo step)`)
	else
		table.insert(lines, "read-only run: nothing changed")
	end
	return table.concat(lines, "\n")
end

local report = run()
print(report)
return report
