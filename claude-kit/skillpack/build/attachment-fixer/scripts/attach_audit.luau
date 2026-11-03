--!strict
-- attach_audit.luau: find broken attachments, welds and constraints that make models fall apart. Audit-only by default.
-- Paste into the Studio command bar or send through the Studio MCP `execute_luau` tool (datamodel_type Edit).
-- Checks: Attachments parented to non-parts; Constraints with a missing or shared Attachment0/Attachment1; WeldConstraints, Welds and
-- Motor6Ds with a missing or identical Part0/Part1; welds that join two different top-level models; models that split into several
-- free (unanchored) assemblies. Two opt-in fixes, one undo step together:
--   APPLY_REMOVE_DEAD : destroy WeldConstraints/Welds whose Part0 or Part1 is nil (they hold nothing).
--   APPLY_REWELD      : in a Model with a PrimaryPart, add a WeldConstraint from each loose free assembly's root to the PrimaryPart.
local ROOT: Instance? = nil -- nil = the current Selection, or Workspace when nothing is selected
local APPLY_REMOVE_DEAD = false
local APPLY_REWELD = false
local MAX_LIST = 12

local Selection = game:GetService("Selection")
local ChangeHistoryService = game:GetService("ChangeHistoryService")

local function topModel(inst: Instance): Instance?
	local cur: Instance? = inst
	local found: Instance? = nil
	while cur and cur ~= workspace and cur ~= game do
		if cur:IsA("Model") then
			found = cur
		end
		cur = cur.Parent
	end
	return found
end

local function run(): string
	local base = ROOT or Selection:Get()[1] or workspace
	local problems: { [string]: { string } } = {}
	local function note(kind: string, inst: Instance)
		local list = problems[kind]
		if not list then
			list = {}
			problems[kind] = list
		end
		table.insert(list, inst:GetFullName())
	end
	local deadWelds: { Instance } = {}
	local models: { Model } = {}
	local all = base:GetDescendants()
	table.insert(all, 1, base)
	for _, inst in all do
		if inst:IsA("Attachment") then
			if not (inst.Parent and (inst.Parent:IsA("BasePart") or inst.Parent:IsA("Attachment"))) then
				note("attachment not under a part", inst)
			end
		elseif inst:IsA("Constraint") then
			local c = inst :: Constraint
			if not c.Attachment0 or not c.Attachment1 then
				note("constraint with a missing attachment", inst)
			elseif c.Attachment0 == c.Attachment1 then
				note("constraint joins an attachment to itself", inst)
			elseif c.Attachment0.Parent == c.Attachment1.Parent then
				note("constraint attachments on the same part", inst)
			end
		elseif inst:IsA("WeldConstraint") or inst:IsA("Weld") then
			local w = inst :: any
			if w.Part0 == nil or w.Part1 == nil then
				note("weld with a missing part", inst)
				table.insert(deadWelds, inst)
			elseif w.Part0 == w.Part1 then
				note("weld joins a part to itself", inst)
			elseif topModel(w.Part0) ~= topModel(w.Part1) then
				note("weld joins two different top-level models", inst)
			end
		elseif inst:IsA("Motor6D") then
			local m = inst :: Motor6D
			if m.Part0 == nil or m.Part1 == nil then
				note("Motor6D with a missing part", inst)
			end
		elseif inst:IsA("Model") then
			table.insert(models, inst :: Model)
		end
	end
	local reweldPlan: { { model: Model, part: BasePart } } = {}
	for _, m in models do
		local roots: { [BasePart]: boolean } = {}
		for _, d in m:GetDescendants() do
			if d:IsA("BasePart") and not d.Anchored and not d:IsA("Terrain") then
				local r = (d :: BasePart).AssemblyRootPart
				if r and not r.Anchored then
					roots[r] = true
				end
			end
		end
		local n = 0
		for _ in roots do
			n += 1
		end
		if n > 1 and not m:FindFirstChildOfClass("Humanoid") then
			note(`model splits into {n} free assemblies`, m)
			if m.PrimaryPart then
				for r in roots do
					if r ~= m.PrimaryPart.AssemblyRootPart then
						table.insert(reweldPlan, { model = m, part = r })
					end
				end
			end
		end
	end
	local lines = { `ATTACHMENT AUDIT: {base:GetFullName()}` }
	local any = false
	for kind, list in problems do
		any = true
		table.insert(lines, `[{#list}] {kind}`)
		for i = 1, math.min(MAX_LIST, #list) do
			table.insert(lines, `  e.g. {list[i]}`)
		end
	end
	if not any then
		table.insert(lines, "no joint problems found")
	end
	if (APPLY_REMOVE_DEAD and #deadWelds > 0) or (APPLY_REWELD and #reweldPlan > 0) then
		local recording = ChangeHistoryService:TryBeginRecording("attachment-fixer")
		if APPLY_REMOVE_DEAD then
			for _, w in deadWelds do
				w:Destroy()
			end
			table.insert(lines, `removed {#deadWelds} dead welds`)
		end
		if APPLY_REWELD then
			for _, item in reweldPlan do
				local primary = item.model.PrimaryPart
				if primary then
					local weld = Instance.new("WeldConstraint")
					weld.Name = "AutoWeld"
					weld.Part0 = primary
					weld.Part1 = item.part
					weld.Parent = item.part
				end
			end
			table.insert(lines, `added {#reweldPlan} welds to PrimaryPart (one undo step with the removals)`)
		end
		if recording then
			ChangeHistoryService:FinishRecording(recording, Enum.FinishRecordingOperation.Commit)
		end
	else
		table.insert(lines, "read-only run: nothing changed")
	end
	return table.concat(lines, "\n")
end

local report = run()
print(report)
return report
