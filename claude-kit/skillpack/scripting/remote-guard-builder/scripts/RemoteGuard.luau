--!strict
local RemoteGuard = {}

export type Validator = (value: any) -> boolean
export type Spec = {
	args: { Validator },
	limit: { calls: number, per: number }?,
	handler: (player: any, ...any) -> ...any,
	onReject: ((player: any, reason: string) -> ())?,
}
export type Limiter = { allow: (self: Limiter, key: any) -> boolean }

local function isFinite(n: number): boolean
	return n == n and n ~= math.huge and n ~= -math.huge
end

function RemoteGuard.number(min: number, max: number): Validator
	return function(v: any): boolean
		return type(v) == "number" and isFinite(v) and v >= min and v <= max
	end
end

function RemoteGuard.integer(min: number, max: number): Validator
	return function(v: any): boolean
		return type(v) == "number" and isFinite(v) and v >= min and v <= max and v == math.floor(v)
	end
end

function RemoteGuard.string(maxLength: number, pattern: string?): Validator
	return function(v: any): boolean
		if type(v) ~= "string" or #v > maxLength then
			return false
		end
		return pattern == nil or string.match(v, pattern) ~= nil
	end
end

function RemoteGuard.boolean(): Validator
	return function(v: any): boolean
		return type(v) == "boolean"
	end
end

function RemoteGuard.oneOf(allowed: { any }): Validator
	local set = {}
	for _, a in allowed do
		set[a] = true
	end
	return function(v: any): boolean
		return set[v] == true
	end
end

function RemoteGuard.vector3(maxMagnitude: number): Validator
	return function(v: any): boolean
		if typeof(v) ~= "Vector3" then
			return false
		end
		local vec = v :: Vector3
		return isFinite(vec.X) and isFinite(vec.Y) and isFinite(vec.Z) and vec.Magnitude <= maxMagnitude
	end
end

function RemoteGuard.instance(className: string, ancestor: Instance?): Validator
	return function(v: any): boolean
		if typeof(v) ~= "Instance" then
			return false
		end
		local inst = v :: Instance
		if not inst:IsA(className) or inst.Parent == nil then
			return false
		end
		return ancestor == nil or inst:IsDescendantOf(ancestor)
	end
end

function RemoteGuard.optional(inner: Validator): Validator
	return function(v: any): boolean
		return v == nil or inner(v)
	end
end

function RemoteGuard.newLimiter(calls: number, per: number, clock: (() -> number)?): Limiter
	local now = clock or os.clock
	local windows: { [any]: { start: number, count: number } } = {}
	local limiter = {} :: Limiter
	function limiter.allow(_self: Limiter, key: any): boolean
		local t = now()
		local w = windows[key]
		if not w or t - w.start >= per then
			windows[key] = { start = t, count = 1 }
			return true
		end
		if w.count >= calls then
			return false
		end
		w.count += 1
		return true
	end
	return limiter
end

function RemoteGuard.check(validators: { Validator }, ...: any): (boolean, string?)
	local n = select("#", ...)
	if n > #validators then
		return false, "too many arguments"
	end
	for i, validate in validators do
		local v = select(i, ...)
		if not validate(v) then
			return false, `argument {i} invalid`
		end
	end
	return true, nil
end

function RemoteGuard.bind(remote: any, spec: Spec): any
	local limiter = if spec.limit then RemoteGuard.newLimiter(spec.limit.calls, spec.limit.per) else nil
	local function run(player: any, ...: any): ...any
		if limiter and not limiter:allow(player.UserId) then
			if spec.onReject then
				spec.onReject(player, "rate limit")
			end
			return nil
		end
		local ok, why = RemoteGuard.check(spec.args, ...)
		if not ok then
			if spec.onReject then
				spec.onReject(player, why or "invalid")
			end
			return nil
		end
		return spec.handler(player, ...)
	end
	if remote:IsA("RemoteFunction") then
		remote.OnServerInvoke = run
		return nil
	end
	return remote.OnServerEvent:Connect(run)
end

return RemoteGuard
