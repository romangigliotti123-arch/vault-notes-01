--!strict
-- MinimapMath: world-to-minimap coordinate maths for the two usual designs. Top-down world plane is X/Z (Roblox Y is up).
--   static map: whole-world image, markers placed by `fromBounds`.
--   radar map: centred on the player, optionally rotating with their facing (`yaw` radians, 0 = looking toward -Z), range-limited,
--   off-range markers pinned to the rim by `clampToRim` (so a quest arrow still points the right way).
-- Output is in map pixels from the map's top-left; the caller maps them to a Scale position inside the minimap frame.
local MinimapMath = {}

export type V2 = { x: number, z: number }
export type Bounds = { minX: number, maxX: number, minZ: number, maxZ: number }
export type Point = { x: number, y: number, inside: boolean }

function MinimapMath.fromBounds(pos: V2, bounds: Bounds, mapPx: number): Point
	local u = (pos.x - bounds.minX) / (bounds.maxX - bounds.minX)
	local v = (pos.z - bounds.minZ) / (bounds.maxZ - bounds.minZ)
	return { x = u * mapPx, y = v * mapPx, inside = u >= 0 and u <= 1 and v >= 0 and v <= 1 }
end

-- Radar: `range` studs map to the map radius. rotate = true keeps "forward" pointing up on the map.
function MinimapMath.radar(pos: V2, centre: V2, yaw: number, range: number, mapRadiusPx: number, rotate: boolean): Point
	local dx, dz = pos.x - centre.x, pos.z - centre.z
	if rotate then
		-- rotate the offset by +yaw so the player's forward direction (-Z rotated by yaw) ends up as map-up
		local c, s = math.cos(yaw), math.sin(yaw)
		dx, dz = dx * c - dz * s, dx * s + dz * c
	end
	local scale = mapRadiusPx / range
	local px, py = dx * scale, dz * scale -- map-up is -Z, so +Z is down the screen
	local dist = math.sqrt(px * px + py * py)
	return { x = mapRadiusPx + px, y = mapRadiusPx + py, inside = dist <= mapRadiusPx }
end

-- Pin a point that is outside the circular map to its rim along the same bearing (inset keeps the marker fully inside).
function MinimapMath.clampToRim(p: Point, mapRadiusPx: number, inset: number?): Point
	local dx, dy = p.x - mapRadiusPx, p.y - mapRadiusPx
	local dist = math.sqrt(dx * dx + dy * dy)
	local limit = mapRadiusPx - (inset or 0)
	if dist <= limit or dist == 0 then
		return p
	end
	local k = limit / dist
	return { x = mapRadiusPx + dx * k, y = mapRadiusPx + dy * k, inside = false }
end

-- How many markers a minimap plan has vs a legibility budget. Heuristic ceiling: more than ~12 icons on a phone-sized map is noise.
function MinimapMath.cluttered(markerCount: number, ceiling: number?): boolean
	return markerCount > (ceiling or 12)
end

return MinimapMath
