--!strict
-- RaycastKit: the spatial queries games actually need, with the parameters set correctly. The casts need a running place; the
-- cast, clamp and sweep logic is unit-tested under Lune with a fake world (RaycastKit.world), the real engine behaviour is not:
-- run the calls in a play test (execute_luau / command bar) before you rely on them.
--   local params = RaycastKit.exclude({ character })                    -- ExcludeInstances: the fast 2026 filter
--   local hit = RaycastKit.cast(origin, direction, params)             -- direction length IS the ray length (max 15,000 studs)
--   RaycastKit.lineOfSight(from, to, params)                            -- true when nothing blocks the segment
--   RaycastKit.groundBelow(position, params, 50)                        -- RaycastResult or nil
--   RaycastKit.sphereHit(origin, radius, direction, params)             -- thick ray: bullets, melee sweeps, camera probes
--   RaycastKit.partsInRadius(position, radius, overlapParams)           -- overlap query, no ray
-- Always nil-check the result. Server-authoritative damage and hits run these on the SERVER; a client may run the same cast for
-- instant visual feedback only.
local RaycastKit = { world = workspace :: any } -- `world` is replaced by a fake in tests; it is the real workspace in a place

local MAX_RAY = 15000 -- studs, from the vault (scripting-and-performance: ray length is the direction magnitude, max 15,000)

-- everything except these (the shooter's character, the projectile itself, effects)
function RaycastKit.exclude(instances: { Instance }, collisionGroup: string?): RaycastParams
	local params = RaycastParams.new()
	params.FilterType = Enum.RaycastFilterType.Exclude
	params.ExcludeInstances = instances
	if collisionGroup then
		params.CollisionGroup = collisionGroup
	end
	return params
end

-- only these (a hit-scan against a known target list)
function RaycastKit.include(instances: { Instance }, collisionGroup: string?): RaycastParams
	local params = RaycastParams.new()
	params.FilterType = Enum.RaycastFilterType.Include
	params.IncludeInstances = instances
	if collisionGroup then
		params.CollisionGroup = collisionGroup
	end
	return params
end

-- clamps the length to the engine maximum so a long direction vector cannot silently return nil
function RaycastKit.cast(origin: Vector3, direction: Vector3, params: RaycastParams?): RaycastResult?
	if direction.Magnitude > MAX_RAY then
		direction = direction.Unit * MAX_RAY
	end
	return RaycastKit.world:Raycast(origin, direction, params)
end

function RaycastKit.lineOfSight(from: Vector3, to: Vector3, params: RaycastParams?): boolean
	return RaycastKit.cast(from, to - from, params) == nil
end

function RaycastKit.groundBelow(position: Vector3, params: RaycastParams?, maxDrop: number?): RaycastResult?
	return RaycastKit.cast(position, Vector3.new(0, -(maxDrop or 100), 0), params)
end

function RaycastKit.sphereHit(
	origin: Vector3,
	radius: number,
	direction: Vector3,
	params: RaycastParams?
): RaycastResult?
	return RaycastKit.world:Spherecast(origin, radius, direction, params)
end

function RaycastKit.blockHit(cframe: CFrame, size: Vector3, direction: Vector3, params: RaycastParams?): RaycastResult?
	return RaycastKit.world:Blockcast(cframe, size, direction, params)
end

function RaycastKit.partsInRadius(position: Vector3, radius: number, params: OverlapParams?): { BasePart }
	return RaycastKit.world:GetPartBoundsInRadius(position, radius, params)
end

function RaycastKit.partsInBox(cframe: CFrame, size: Vector3, params: OverlapParams?): { BasePart }
	return RaycastKit.world:GetPartBoundsInBox(cframe, size, params)
end

-- walk a fast mover's path in steps so it cannot tunnel through thin parts between frames
function RaycastKit.sweep(from: Vector3, to: Vector3, stepStuds: number, params: RaycastParams?): RaycastResult?
	local delta = to - from
	local length = delta.Magnitude
	if length == 0 then
		return nil
	end
	local step = math.max(1, stepStuds)
	local dir = delta.Unit
	local travelled = 0
	while travelled < length do
		local segment = math.min(step, length - travelled)
		local hit = RaycastKit.cast(from + dir * travelled, dir * segment, params)
		if hit then
			return hit
		end
		travelled += segment
	end
	return nil
end

return RaycastKit
