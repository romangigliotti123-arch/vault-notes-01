--!strict
-- anchor_check.luau: find parts that will fall, drift or jitter because nothing anchors them. Audit-only by default.
-- Paste into the Studio command bar or send through the Studio MCP `execute_luau` tool (datamodel_type Edit).
-- A part is "free" when its whole assembly (the parts welded to it) has no anchored part. Characters, NPCs, Tools, Accessories and
-- anything marked with the attribute KeepUnanchored (on the part or any ancestor) are skipped: those are meant to move.
local ROOT: Instance? = nil -- nil = Workspace; set to a model/folder to limit the scan
local APPLY_ANCHOR = false -- true: anchor every free part found (one undo step). Review the list first.
local SKIP_ATTRIBUTE = "KeepUnanchored"
local MAX_LIST = 15

local ChangeHistoryService = game:GetService("ChangeHistoryService")

local function movesOnPurpose(part: BasePart, root: Instance): boolean
	local cur: Instance? = part
	while cur and cur ~= root.Parent do
		if cur:GetAttribute(SKIP_ATTRIBUTE) == true then
			return true
		end
		if cur:IsA("Tool") or cur:IsA("Accessory") or cur:IsA("Seat") or cur:IsA("VehicleSeat") then
			return true
		end
		if cur:IsA("Model") and cur:FindFirstChildOfClass("Humanoid") then
			return true
		end
		cur = cur.Parent
	end
	return false
end

local function run(): string
	local root = ROOT or workspace
	local total, anchored, skipped = 0, 0, 0
	local free: { BasePart } = {}
	local assemblies: { [BasePart]: number } = {}
	for _, inst in root:GetDescendants() do
		if inst:IsA("BasePart") and not inst:IsA("Terrain") then
			total += 1
			local part = inst :: BasePart
			if part.Anchored then
				anchored += 1
			elseif movesOnPurpose(part, root) then
				skipped += 1
			else
				local rootPart = part.AssemblyRootPart
				if rootPart and not rootPart.Anchored then
					table.insert(free, part)
					assemblies[rootPart] = (assemblies[rootPart] or 0) + 1
				end
			end
		end
	end
	local assemblyCount = 0
	for _ in assemblies do
		assemblyCount += 1
	end
	local lines = {
		`ANCHOR CHECK: {root:GetFullName()}`,
		`parts={total} anchored={anchored} skipped-on-purpose={skipped} free={#free} free-assemblies={assemblyCount}`,
	}
	if #free > 0 then
		table.insert(
			lines,
			`[{#free}] free parts -> each unanchored assembly costs physics and falls or drifts; anchor scenery`
		)
		for i = 1, math.min(MAX_LIST, #free) do
			table.insert(lines, `  e.g. {free[i]:GetFullName()}`)
		end
		table.insert(lines, `  tip: mark things that must move with the attribute {SKIP_ATTRIBUTE}=true and re-run`)
	end
	if APPLY_ANCHOR and #free > 0 then
		local recording = ChangeHistoryService:TryBeginRecording("anchor-checker anchor free parts")
		for _, part in free do
			part.Anchored = true
		end
		if recording then
			ChangeHistoryService:FinishRecording(recording, Enum.FinishRecordingOperation.Commit)
		end
		table.insert(lines, `anchored {#free} parts (one undo step)`)
	else
		table.insert(lines, "read-only run: nothing changed")
	end
	return table.concat(lines, "\n")
end

local report = run()
print(report)
return report
