--!strict
local RaycastKit = { world = workspace :: any }

local MAX_RAY = 15000

function RaycastKit.exclude(instances: { Instance }, collisionGroup: string?): RaycastParams
	local params = RaycastParams.new()
	params.FilterType = Enum.RaycastFilterType.Exclude
	params.ExcludeInstances = instances
	if collisionGroup then
		params.CollisionGroup = collisionGroup
	end
	return params
end

function RaycastKit.include(instances: { Instance }, collisionGroup: string?): RaycastParams
	local params = RaycastParams.new()
	params.FilterType = Enum.RaycastFilterType.Include
	params.IncludeInstances = instances
	if collisionGroup then
		params.CollisionGroup = collisionGroup
	end
	return params
end

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
