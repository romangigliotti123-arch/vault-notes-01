--!strict
-- TerrainPlan: size a terrain job in voxels and heightmap pixels before sculpting. Pure logic, unit-tested under Lune.
-- Vault facts used (Creator Docs via the building KB): terrain voxels are 4x4x4 studs; a heightmap is a .jpg or .png of at most
-- 4096x4096 px where 1 px = 4 studs (so one image spans about 16384 studs). Tile bigger maps.
local TerrainPlan = {}

TerrainPlan.VOXEL = 4
TerrainPlan.MAX_PX = 4096

export type Tile = { col: number, row: number, pxW: number, pxD: number, studsW: number, studsD: number }
export type Plan = { pxW: number, pxD: number, tiles: { Tile }, single: boolean, voxelsPerLayer: number }

function TerrainPlan.snap(studs: number): number
	return math.floor(studs / TerrainPlan.VOXEL + 0.5) * TerrainPlan.VOXEL
end

function TerrainPlan.pxFor(studs: number): number
	return math.ceil(studs / TerrainPlan.VOXEL)
end

function TerrainPlan.voxelCount(w: number, d: number, h: number): number
	local v = TerrainPlan.VOXEL
	return math.ceil(w / v) * math.ceil(d / v) * math.ceil(h / v)
end

-- Heightmap plan for a rectangular map. Splits into tiles of at most MAX_PX when either side is too large.
function TerrainPlan.heightmap(widthStuds: number, depthStuds: number): Plan
	assert(widthStuds > 0 and depthStuds > 0, "map size must be positive")
	local pxW, pxD = TerrainPlan.pxFor(widthStuds), TerrainPlan.pxFor(depthStuds)
	local cols, rows = math.ceil(pxW / TerrainPlan.MAX_PX), math.ceil(pxD / TerrainPlan.MAX_PX)
	local tiles: { Tile } = {}
	for r = 1, rows do
		for c = 1, cols do
			local w = math.min(TerrainPlan.MAX_PX, pxW - (c - 1) * TerrainPlan.MAX_PX)
			local d = math.min(TerrainPlan.MAX_PX, pxD - (r - 1) * TerrainPlan.MAX_PX)
			table.insert(tiles, {
				col = c,
				row = r,
				pxW = w,
				pxD = d,
				studsW = w * TerrainPlan.VOXEL,
				studsD = d * TerrainPlan.VOXEL,
			})
		end
	end
	return {
		pxW = pxW,
		pxD = pxD,
		tiles = tiles,
		single = #tiles == 1,
		voxelsPerLayer = pxW * pxD,
	}
end

-- Share of the map that is water or land determines what to hollow or fill. Returns a sorted work order (vault build order:
-- terrain/hills, zones and roads, buildings, props).
function TerrainPlan.order(hasWater: boolean, hasRoads: boolean): { string }
	local steps =
		{ "set map bounds and snap to the 4-stud grid", "sculpt base land from top-down", "round edges and vary sizes" }
	if hasWater then
		table.insert(steps, "fill water and set the island edge")
	end
	table.insert(steps, "hollow or delete hidden terrain (Subtract), keep surfaces")
	if hasRoads then
		table.insert(steps, "flatten road and plaza corridors")
	end
	table.insert(steps, "paint materials last, fewest distinct materials that read")
	return steps
end

return TerrainPlan
