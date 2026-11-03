--!strict
-- Settings: schema-driven preferences. One schema shared by client (to build the controls) and server (to validate what the client
-- sends before saving it into the player's profile, kit PlayerData). The server NEVER trusts raw client values: `sanitize` drops
-- unknown keys, coerces types and clamps numbers.
--   local clean = Settings.sanitize(SCHEMA, rawFromClient)       -- always a full, valid table
--   local changed = Settings.diff(old, clean)                    -- only send/save what changed
--   local saved = Settings.migrate(savedTable, 2, MIGRATIONS)    -- older saves gain new keys
local Settings = {}

export type Def = {
	key: string,
	kind: string, -- "toggle" | "slider" | "choice"
	default: any,
	min: number?,
	max: number?,
	step: number?,
	options: { string }?,
}
export type Values = { [string]: any }

function Settings.defaults(schema: { Def }): Values
	local out: Values = {}
	for _, d in schema do
		out[d.key] = d.default
	end
	return out
end

local function clean(d: Def, v: any): any
	if d.kind == "toggle" then
		if type(v) == "boolean" then
			return v
		end
	elseif d.kind == "slider" then
		if type(v) == "number" and v == v and v ~= math.huge and v ~= -math.huge then
			local lo, hi = d.min or 0, d.max or 1
			local x = math.clamp(v, lo, hi)
			if d.step and d.step > 0 then
				x = lo + math.floor((x - lo) / d.step + 0.5) * d.step
				x = math.clamp(tonumber(string.format("%.9g", x)) or x, lo, hi)
			end
			return x
		end
	elseif d.kind == "choice" then
		if type(v) == "string" and d.options and table.find(d.options, v) then
			return v
		end
	end
	return d.default
end

function Settings.sanitize(schema: { Def }, raw: any): Values
	local source: { [any]: any } = if type(raw) == "table" then raw else {}
	local out: Values = {}
	for _, d in schema do
		out[d.key] = clean(d, source[d.key])
	end
	return out
end

function Settings.diff(old: Values, new: Values): Values
	local changed: Values = {}
	for k, v in new do
		if old[k] ~= v then
			changed[k] = v
		end
	end
	return changed
end

-- migrations[n] upgrades a table from version n to n+1 in place. Returns the table and the new version.
function Settings.migrate(
	saved: Values,
	fromVersion: number,
	migrations: { [number]: (Values) -> () }
): (Values, number)
	local v = fromVersion
	while migrations[v] do
		migrations[v](saved)
		v += 1
	end
	return saved, v
end

return Settings
