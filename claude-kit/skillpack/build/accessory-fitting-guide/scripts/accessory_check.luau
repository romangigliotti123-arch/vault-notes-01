--!strict
local TARGET: Instance? = nil
local HAT_TRIANGLE_LIMIT = 4000

local Selection = game:GetService("Selection")

local ATTACHMENTS: { [string]: boolean } = {
	HatAttachment = true,
	HairAttachment = true,
	FaceFrontAttachment = true,
	FaceCenterAttachment = true,
	NeckAttachment = true,
	BodyFrontAttachment = true,
	BodyBackAttachment = true,
	LeftCollarAttachment = true,
	RightCollarAttachment = true,
	WaistFrontAttachment = true,
	WaistCenterAttachment = true,
	WaistBackAttachment = true,
	LeftShoulderAttachment = true,
	RightShoulderAttachment = true,
	LeftGripAttachment = true,
	RightGripAttachment = true,
}

local function checkAccessory(acc: Accessory, lines: { string }): number
	local problems = 0
	local function bad(msg: string)
		problems += 1
		table.insert(lines, `  [problem] {msg}`)
	end
	table.insert(lines, `{acc.Name}:`)
	local handle = acc:FindFirstChild("Handle")
	if not handle or not handle:IsA("BasePart") then
		bad("no Handle part")
		return problems
	end
	local part = handle :: BasePart
	local wrap = part:FindFirstChildWhichIsA("WrapLayer")
	local rigidAttachment: Attachment? = nil
	for _, child in part:GetChildren() do
		if child:IsA("Attachment") and ATTACHMENTS[child.Name] then
			rigidAttachment = child
		end
	end
	if wrap then
		table.insert(lines, "  type: layered clothing (WrapLayer found)")
		local cage = (wrap :: any).CageMeshId
		if cage == nil or tostring(cage) == "" then
			bad("WrapLayer has no CageMeshId: use the Accessory Fitting Tool to set the inner cage")
		end
		local ref = (wrap :: any).ReferenceMeshId
		if ref == nil or tostring(ref) == "" then
			bad("WrapLayer has no ReferenceMeshId")
		end
		if not string.find(part.Name, "Handle", 1, true) then
			bad("handle renamed; layered items keep Handle")
		end
	elseif rigidAttachment then
		table.insert(lines, `  type: rigid accessory on {rigidAttachment.Name}`)
	else
		bad("no WrapLayer and no known R15 attachment (e.g. HatAttachment) inside Handle: it will not attach")
	end
	if part:IsA("MeshPart") then
		if part.Transparency ~= 0 then
			bad(`MeshPart Transparency is {part.Transparency}; must be exactly 0 for upload`)
		end
		if (part :: MeshPart).MeshId == "" then
			bad("MeshPart has no MeshId")
		end
	end
	if part.CanCollide then
		bad("Handle CanCollide is on: accessories should not collide with the body (turn it off)")
	end
	if not part.Massless then
		table.insert(
			lines,
			"  [note] Handle is not Massless; the character rig-checker treats non-massless accessory parts as a fault"
		)
	end
	local seen: { [string]: boolean } = {}
	for _, d in acc:GetDescendants() do
		if d:IsA("BasePart") then
			if seen[d.Name] then
				bad(`duplicate part name {d.Name}`)
			end
			seen[d.Name] = true
		end
	end
	table.insert(
		lines,
		`  not checked here: triangle count (limit {HAT_TRIANGLE_LIMIT} for hats), cage fit, UVs, textures`
	)
	return problems
end

local function run(): string
	local base = TARGET or Selection:Get()[1]
	if not base then
		return "ACCESSORY CHECK: select an Accessory (or a model of accessories) first"
	end
	local lines = { `ACCESSORY CHECK: {base:GetFullName()}` }
	local problems, count = 0, 0
	local list: { Accessory } = {}
	if base:IsA("Accessory") then
		table.insert(list, base)
	else
		for _, d in base:GetDescendants() do
			if d:IsA("Accessory") then
				table.insert(list, d)
			end
		end
	end
	for _, acc in list do
		count += 1
		problems += checkAccessory(acc, lines)
	end
	table.insert(lines, `{count} accessories, {problems} problems; read-only run: nothing changed`)
	return table.concat(lines, "\n")
end

local report = run()
print(report)
return report
