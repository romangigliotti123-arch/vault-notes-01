--!strict
local MinimapMath = {}

export type V2 = { x: number, z: number }
export type Bounds = { minX: number, maxX: number, minZ: number, maxZ: number }
export type Point = { x: number, y: number, inside: boolean }

function MinimapMath.fromBounds(pos: V2, bounds: Bounds, mapPx: number): Point
	local u = (pos.x - bounds.minX) / (bounds.maxX - bounds.minX)
	local v = (pos.z - bounds.minZ) / (bounds.maxZ - bounds.minZ)
	return { x = u * mapPx, y = v * mapPx, inside = u >= 0 and u <= 1 and v >= 0 and v <= 1 }
end

function MinimapMath.radar(pos: V2, centre: V2, yaw: number, range: number, mapRadiusPx: number, rotate: boolean): Point
	local dx, dz = pos.x - centre.x, pos.z - centre.z
	if rotate then
		local c, s = math.cos(yaw), math.sin(yaw)
		dx, dz = dx * c - dz * s, dx * s + dz * c
	end
	local scale = mapRadiusPx / range
	local px, py = dx * scale, dz * scale
	local dist = math.sqrt(px * px + py * py)
	return { x = mapRadiusPx + px, y = mapRadiusPx + py, inside = dist <= mapRadiusPx }
end

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

function MinimapMath.cluttered(markerCount: number, ceiling: number?): boolean
	return markerCount > (ceiling or 12)
end

return MinimapMath
