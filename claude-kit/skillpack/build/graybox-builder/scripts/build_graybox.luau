--!strict
local BUILD = false
local REPLACE = false
local GRID = 4
local AVATAR_HEIGHT = 6.5

type Box = {
	name: string,
	x: number,
	y: number,
	z: number,
	sx: number,
	sy: number,
	sz: number,
	role: string,
	allowOverlap: boolean?,
}

local SPEC: { Box } = {
	{ name = "FloorA", x = 0, y = -1, z = 0, sx = 32, sy = 2, sz = 32, role = "floor" },
	{ name = "FloorB", x = 48, y = -1, z = 0, sx = 32, sy = 2, sz = 32, role = "floor" },
	{ name = "Bridge", x = 24, y = -1, z = 0, sx = 16, sy = 2, sz = 8, role = "corridor" },
	{ name = "Pillar", x = 0, y = 6, z = 0, sx = 4, sy = 12, sz = 4, role = "cover" },
}
local COLORS: { [string]: Color3 } = {
	floor = Color3.fromRGB(150, 150, 150),
	wall = Color3.fromRGB(120, 120, 125),
	door = Color3.fromRGB(190, 160, 100),
	corridor = Color3.fromRGB(140, 150, 160),
	platform = Color3.fromRGB(160, 160, 150),
	cover = Color3.fromRGB(110, 130, 110),
	spawn = Color3.fromRGB(100, 160, 100),
}

local ChangeHistoryService = game:GetService("ChangeHistoryService")

local function onGrid(v: number): boolean
	return math.abs(v / GRID - math.floor(v / GRID + 0.5)) < 1e-6
end

local function overlaps(a: Box, b: Box): boolean
	return math.abs(a.x - b.x) < (a.sx + b.sx) / 2
		and math.abs(a.y - b.y) < (a.sy + b.sy) / 2
		and math.abs(a.z - b.z) < (a.sz + b.sz) / 2
end

local function validate(): { string }
	local issues: { string } = {}
	local seen: { [string]: boolean } = {}
	for _, b in SPEC do
		if seen[b.name] then
			table.insert(issues, `{b.name}: duplicate name`)
		end
		seen[b.name] = true
		if b.sx <= 0 or b.sy <= 0 or b.sz <= 0 then
			table.insert(issues, `{b.name}: non-positive size`)
		end
		if not (onGrid(b.sx) and onGrid(b.sy) and onGrid(b.sz)) then
			table.insert(issues, `{b.name}: size not a multiple of {GRID}`)
		end
		if not (onGrid(b.x - b.sx / 2) and onGrid(b.z - b.sz / 2)) then
			table.insert(issues, `{b.name}: corner off the {GRID}-stud grid`)
		end
		if b.role == "door" and (b.sy < AVATAR_HEIGHT * 1.25 or math.min(b.sx, b.sz) < 4) then
			table.insert(issues, `{b.name}: doorway too small (needs >= 8.2 high, >= 4 wide)`)
		end
		if b.role == "corridor" and math.min(b.sx, b.sz) < 8 then
			table.insert(issues, `{b.name}: corridor under 8 studs wide`)
		end
	end
	for i = 1, #SPEC do
		for j = i + 1, #SPEC do
			if overlaps(SPEC[i], SPEC[j]) and not (SPEC[i].allowOverlap or SPEC[j].allowOverlap) then
				table.insert(issues, `{SPEC[i].name}: overlaps {SPEC[j].name}`)
			end
		end
	end
	return issues
end

local function run(): string
	local issues = validate()
	local lines = { `GRAYBOX: {#SPEC} boxes, {#issues} issues` }
	for _, i in issues do
		table.insert(lines, `  {i}`)
	end
	if not BUILD then
		table.insert(lines, "validate only: set BUILD = true to create Workspace.Graybox")
		return table.concat(lines, "\n")
	end
	if #issues > 0 then
		table.insert(lines, "BUILD refused: fix the issues above first (or mark intended overlaps allowOverlap)")
		return table.concat(lines, "\n")
	end
	local existing = workspace:FindFirstChild("Graybox")
	if existing and not REPLACE then
		table.insert(lines, "BUILD refused: Workspace.Graybox already exists (set REPLACE = true to rebuild it)")
		return table.concat(lines, "\n")
	end
	local recording = ChangeHistoryService:TryBeginRecording("graybox-builder")
	if existing then
		existing:Destroy()
	end
	local folder = Instance.new("Folder")
	folder.Name = "Graybox"
	for _, b in SPEC do
		local part = Instance.new("Part")
		part.Name = b.name
		part.Anchored = true
		part.Material = Enum.Material.SmoothPlastic
		part.Color = COLORS[b.role] or COLORS.floor
		part.Size = Vector3.new(b.sx, b.sy, b.sz)
		part.Position = Vector3.new(b.x, b.y, b.z)
		part.TopSurface = Enum.SurfaceType.Smooth
		part.BottomSurface = Enum.SurfaceType.Smooth
		part.Parent = folder
	end
	folder.Parent = workspace
	if recording then
		ChangeHistoryService:FinishRecording(recording, Enum.FinishRecordingOperation.Commit)
	end
	table.insert(lines, `built {#SPEC} boxes in Workspace.Graybox (one undo step)`)
	return table.concat(lines, "\n")
end

local report = run()
print(report)
return report
