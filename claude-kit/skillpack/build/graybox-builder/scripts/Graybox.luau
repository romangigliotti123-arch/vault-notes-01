--!strict
local Graybox = {}

export type Box = {
	name: string,
	x: number,
	y: number,
	z: number,
	sx: number,
	sy: number,
	sz: number,
	role: string?,
	allowOverlap: boolean?,
}
export type Issue = { box: string, kind: string, note: string }

Graybox.AVATAR_HEIGHT = 6.5
Graybox.GRID = 4

local function onGrid(v: number, grid: number): boolean
	return math.abs(v / grid - math.floor(v / grid + 0.5)) < 1e-6
end

local function overlaps(a: Box, b: Box): boolean
	return math.abs(a.x - b.x) < (a.sx + b.sx) / 2
		and math.abs(a.y - b.y) < (a.sy + b.sy) / 2
		and math.abs(a.z - b.z) < (a.sz + b.sz) / 2
end

function Graybox.validate(spec: { Box }, grid: number?): { Issue }
	local g = grid or Graybox.GRID
	local issues: { Issue } = {}
	local seen: { [string]: boolean } = {}
	for _, b in spec do
		if seen[b.name] then
			table.insert(issues, { box = b.name, kind = "name", note = "duplicate name" })
		end
		seen[b.name] = true
		if b.sx <= 0 or b.sy <= 0 or b.sz <= 0 then
			table.insert(issues, { box = b.name, kind = "size", note = "non-positive size" })
		end
		if not (onGrid(b.sx, g) and onGrid(b.sy, g) and onGrid(b.sz, g)) then
			table.insert(issues, { box = b.name, kind = "grid", note = `size not a multiple of {g}` })
		end
		if not (onGrid(b.x - b.sx / 2, g) and onGrid(b.z - b.sz / 2, g)) then
			table.insert(issues, { box = b.name, kind = "grid", note = `corner off the {g}-stud grid` })
		end
		if b.role == "door" and (b.sy < Graybox.AVATAR_HEIGHT * 1.25 or math.min(b.sx, b.sz) < 4) then
			table.insert(
				issues,
				{ box = b.name, kind = "avatar", note = "doorway too small: needs >= 8.2 high, >= 4 wide" }
			)
		end
		if b.role == "corridor" and math.min(b.sx, b.sz) < 8 then
			table.insert(
				issues,
				{ box = b.name, kind = "avatar", note = "corridor under 8 studs wide: players snag on it" }
			)
		end
	end
	for i = 1, #spec do
		for j = i + 1, #spec do
			local a, b = spec[i], spec[j]
			if overlaps(a, b) and not (a.allowOverlap or b.allowOverlap) then
				table.insert(issues, { box = a.name, kind = "overlap", note = `overlaps {b.name}` })
			end
		end
	end
	return issues
end

function Graybox.stats(spec: { Box }): { boxes: number, floorArea: number }
	local area = 0
	for _, b in spec do
		if b.role == "floor" or b.role == "platform" then
			area += b.sx * b.sz
		end
	end
	return { boxes = #spec, floorArea = area }
end

return Graybox
