--!strict
local Pivot = {}

export type V3 = { x: number, y: number, z: number }
export type Bounds = { min: V3, max: V3 }
export type Mode = "bottomCenter" | "center" | "bottomMinCorner"

function Pivot.target(b: Bounds, mode: Mode): V3
	local cx, cz = (b.min.x + b.max.x) / 2, (b.min.z + b.max.z) / 2
	if mode == "center" then
		return { x = cx, y = (b.min.y + b.max.y) / 2, z = cz }
	elseif mode == "bottomMinCorner" then
		return { x = b.min.x, y = b.min.y, z = b.min.z }
	end
	return { x = cx, y = b.min.y, z = cz }
end

local function inside(p: V3, b: Bounds, pad: number): boolean
	return p.x >= b.min.x - pad
		and p.x <= b.max.x + pad
		and p.y >= b.min.y - pad
		and p.y <= b.max.y + pad
		and p.z >= b.min.z - pad
		and p.z <= b.max.z + pad
end

export type Diagnosis = { ok: boolean, offset: V3, distance: number, outside: boolean, note: string }

function Pivot.diagnose(b: Bounds, pivot: V3, mode: Mode, tolerance: number?): Diagnosis
	local tol = tolerance or 0.05
	local want = Pivot.target(b, mode)
	local off = { x = want.x - pivot.x, y = want.y - pivot.y, z = want.z - pivot.z }
	local dist = math.sqrt(off.x ^ 2 + off.y ^ 2 + off.z ^ 2)
	local size = math.max(b.max.x - b.min.x, b.max.y - b.min.y, b.max.z - b.min.z)
	local outside = not inside(pivot, b, size * 0.01)
	local note = "pivot is where it should be"
	if dist > tol then
		local d = string.format("%.1f", dist)
		note = if outside
			then `pivot is outside the model: PivotTo will place the model {d} studs from where you aim`
			else `pivot is {d} studs from the {mode} point`
	end
	return { ok = dist <= tol, offset = off, distance = dist, outside = outside, note = note }
end

return Pivot
