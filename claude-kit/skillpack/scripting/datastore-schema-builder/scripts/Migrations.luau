--!strict
-- Migrations: OFFLINE test and lint layer for a save schema (pure Luau, no Roblox globals, runs in Lune).
-- The runtime owner of loading, locking and migrating is the kit system PlayerData (systems/PlayerData): it takes
-- { template, version, migrations } and stores records as { v = version, data = table }. This module applies the SAME
-- rules to fixtures so the schema file you ship is tested before it ever touches a DataStore:
--   migrations[n] upgrades data from version n to n+1 and returns the table; a record newer than `target` is refused;
--   a missing step is an error; afterwards missing template keys are filled in.
-- Use the same Schema.luau (TEMPLATE, VERSION, MIGRATIONS) in the game and in tests/Schema.test.luau.
local Migrations = {}

export type Data = { [string]: any }
export type Step = (data: Data) -> Data
export type Steps = { [number]: Step }
export type Record = { v: number?, data: Data }

function Migrations.deepCopy<T>(value: T): T
	if type(value) ~= "table" then
		return value
	end
	local out = {}
	for k, v in value :: any do
		out[k] = Migrations.deepCopy(v)
	end
	return out :: any
end

-- fill keys missing in data from template; nested dictionaries recurse, arrays (empty-table defaults) are left alone
function Migrations.reconcile(data: Data, template: Data)
	for key, def in template do
		local cur = data[key]
		if cur == nil then
			data[key] = Migrations.deepCopy(def)
		elseif type(cur) == "table" and type(def) == "table" and next(def) ~= nil and #def == 0 then
			Migrations.reconcile(cur, def)
		end
	end
end

-- step numbers in [from, target-1] without a function (empty = the chain is complete)
function Migrations.missingSteps(from: number, target: number, steps: Steps): { number }
	local missing = {}
	for n = from, target - 1 do
		if steps[n] == nil then
			table.insert(missing, n)
		end
	end
	return missing
end

-- apply the rules to one stored record. Returns data, nil or nil, reason ("newer", "missing migration N", "migration N failed: ...")
function Migrations.migrate(record: Record, target: number, steps: Steps, template: Data): (Data?, string?)
	local v = record.v or 1
	if v > target then
		return nil, "newer"
	end
	local data = Migrations.deepCopy(record.data)
	while v < target do
		local step = steps[v]
		if step == nil then
			return nil, `missing migration {v}`
		end
		local ok, result = pcall(step, data)
		if not ok then
			return nil, `migration {v} failed: {tostring(result)}`
		end
		if type(result) == "table" then
			data = result
		end
		v += 1
	end
	Migrations.reconcile(data, template)
	return data, nil
end

local function isArray(t: { [any]: any }): boolean
	local n = 0
	for _ in t do
		n += 1
	end
	return n == #t
end

-- problems that DataStore serialisation or later migrations will hit; empty list = template is storable
function Migrations.validateTemplate(template: Data): { string }
	local problems = {}
	local function walk(value: any, path: string, depth: number)
		local kind = typeof(value)
		if kind == "number" then
			if value ~= value or value == math.huge or value == -math.huge then
				table.insert(problems, `{path}: NaN or infinite number`)
			end
		elseif kind == "string" or kind == "boolean" then
			return
		elseif kind == "table" then
			if depth > 6 then
				table.insert(problems, `{path}: nested deeper than 6 levels`)
				return
			end
			local t = value :: { [any]: any }
			if next(t) ~= nil and not isArray(t) then
				for k in t do
					if type(k) ~= "string" then
						table.insert(
							problems,
							`{path}: mixed or non-string keys ({tostring(k)}); use string keys, or a pure array`
						)
						break
					end
				end
			end
			for k, v in t do
				walk(v, `{path}.{tostring(k)}`, depth + 1)
			end
		else
			table.insert(problems, `{path}: {kind} cannot be saved (store numbers, strings, booleans, tables)`)
		end
	end
	walk(template, "template", 0)
	return problems
end

return Migrations
