--!strict
local Catalogue = {}

export type Data = { [any]: any }
export type Entry = {
	name: string,
	id: number,
	grant: (userId: number, data: Data) -> boolean,
	refuseWith: Data?,
}
export type Product = { name: string, grant: (userId: number, data: Data) -> boolean }

local function deepCopy(value: any): any
	if type(value) ~= "table" then
		return value
	end
	local out = {}
	for k, v in value do
		out[k] = deepCopy(v)
	end
	return out
end

local function sameData(a: any, b: any): boolean
	if type(a) ~= "table" or type(b) ~= "table" then
		return a == b
	end
	for k, v in a do
		if not sameData(v, b[k]) then
			return false
		end
	end
	for k in b do
		if a[k] == nil then
			return false
		end
	end
	return true
end

function Catalogue.build(entries: { Entry }): ({ [number]: Product }, { string })
	local products: { [number]: Product } = {}
	local notes: { string } = {}
	local names: { [string]: boolean } = {}
	for _, e in entries do
		assert(type(e.name) == "string" and e.name ~= "", "product needs a name")
		assert(not names[e.name], `duplicate product name {e.name}`)
		names[e.name] = true
		if e.id == 0 then
			table.insert(notes, `product {e.name}: id 0 (SET IN CREATOR HUB), skipped`)
		else
			assert(products[e.id] == nil, `duplicate product id {e.id}`)
			products[e.id] = { name = e.name, grant = e.grant }
		end
	end
	return products, notes
end

local function storable(value: any, path: string, problems: { string })
	local kind = typeof(value)
	if kind == "number" then
		if value ~= value or value == math.huge or value == -math.huge then
			table.insert(problems, `{path}: NaN or infinite`)
		end
	elseif kind == "table" then
		for k, v in value do
			storable(v, `{path}.{tostring(k)}`, problems)
		end
	elseif kind ~= "string" and kind ~= "boolean" then
		table.insert(problems, `{path}: {kind} cannot be saved`)
	end
end

function Catalogue.verify(entries: { Entry }, template: Data): { string }
	local problems: { string } = {}
	for _, e in entries do
		local data = deepCopy(template)
		local before = deepCopy(data)
		local ok, result = pcall(e.grant, 1, data)
		if not ok then
			table.insert(problems, `{e.name}: grant threw ({tostring(result)})`)
		elseif result ~= true then
			table.insert(problems, `{e.name}: grant on a fresh player did not return true`)
		elseif sameData(data, before) then
			table.insert(problems, `{e.name}: grant returned true but changed nothing`)
		else
			storable(data, e.name, problems)
		end
		if e.refuseWith then
			local refuse = deepCopy(e.refuseWith)
			local refuseBefore = deepCopy(refuse)
			local rok, rres = pcall(e.grant, 1, refuse)
			if not rok or rres ~= false then
				table.insert(problems, `{e.name}: grant must return false on the refuseWith data`)
			elseif not sameData(refuse, refuseBefore) then
				table.insert(
					problems,
					`{e.name}: grant changed data and then refused (refuse BEFORE changing anything)`
				)
			end
		end
	end
	return problems
end

return Catalogue
