--!strict
local FlagConfig = {}
FlagConfig.__index = FlagConfig

export type Def = {
	kind: "number" | "boolean" | "string" | "rollout",
	default: any,
	min: number?,
	max: number?,
	allowed: { string }?,
}
export type Defs = { [string]: Def }

local function valid(def: Def, v: any): (boolean, string?)
	if def.kind == "number" or def.kind == "rollout" then
		if type(v) ~= "number" or v ~= v or v == math.huge or v == -math.huge then
			return false, "not a finite number"
		end
		local lo = def.min
		local hi = def.max
		if def.kind == "rollout" then
			lo, hi = 0, 100
		end
		if lo and v < lo then
			return false, "below min " .. tostring(lo)
		end
		if hi and v > hi then
			return false, "above max " .. tostring(hi)
		end
		return true, nil
	elseif def.kind == "boolean" then
		return type(v) == "boolean", "not a boolean"
	elseif def.kind == "string" then
		if type(v) ~= "string" then
			return false, "not a string"
		end
		if def.allowed and not table.find(def.allowed, v) then
			return false, "not an allowed value"
		end
		return true, nil
	end
	return false, "unknown kind"
end

function FlagConfig.new(defs: Defs)
	local values = {}
	for name, def in defs do
		local ok, why = valid(def, def.default)
		assert(ok, `FlagConfig: default for {name} is invalid: {why}`)
		values[name] = def.default
	end
	return setmetatable({ defs = defs, values = values, killed = {} :: { [string]: boolean } }, FlagConfig)
end

function FlagConfig.Apply(self: any, raw: { [string]: any }): { string }
	local problems = {}
	for name, def in self.defs do
		local v = raw[name]
		if v == nil then
			self.values[name] = def.default
		else
			local ok, why = valid(def, v)
			if ok then
				self.values[name] = v
			else
				self.values[name] = def.default
				table.insert(problems, `{name}: {why}, using default`)
			end
		end
	end
	for name in raw do
		if self.defs[name] == nil then
			table.insert(problems, `{name}: unknown key ignored`)
		end
	end
	table.sort(problems)
	return problems
end

function FlagConfig.Get(self: any, name: string): any
	assert(self.defs[name], "unknown flag " .. name)
	if self.killed[name] then
		return self.defs[name].default
	end
	return self.values[name]
end

function FlagConfig.Kill(self: any, name: string)
	assert(self.defs[name], "unknown flag " .. name)
	self.killed[name] = true
end

function FlagConfig.Revive(self: any, name: string)
	self.killed[name] = nil
end

local function bucket(name: string, userId: number): number
	local h = 2166136261
	for i = 1, #name do
		h = (h * 31 + string.byte(name, i)) % 4294967296
	end
	h = (h + userId * 2654435761) % 4294967296
	h = (h * 1103515245 + 12345) % 4294967296
	return math.floor(h / 65536) % 100
end
FlagConfig.bucket = bucket

function FlagConfig.IsOn(self: any, name: string, userId: number): boolean
	local def: Def = self.defs[name]
	assert(def, "unknown flag " .. name)
	local v = self:Get(name)
	if def.kind == "boolean" then
		return v == true
	elseif def.kind == "rollout" then
		return bucket(name, userId) < (v :: number)
	end
	error("IsOn needs a boolean or rollout flag: " .. name)
end

function FlagConfig.Snapshot(self: any): { [string]: any }
	local out = {}
	for name in self.defs do
		out[name] = self:Get(name)
	end
	return out
end

return FlagConfig
