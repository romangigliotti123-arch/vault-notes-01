--!strict
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

function Migrations.missingSteps(from: number, target: number, steps: Steps): { number }
	local missing = {}
	for n = from, target - 1 do
		if steps[n] == nil then
			table.insert(missing, n)
		end
	end
	return missing
end

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
