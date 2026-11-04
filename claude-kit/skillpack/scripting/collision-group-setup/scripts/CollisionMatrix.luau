--!strict
local CollisionMatrix = {}

export type Spec = {
	groups: { string },
	collide: { { string } }?,
	noCollide: { { string } }?,
	limit: number?,
}
export type Plan = {
	register: { string },
	pairs: { { a: string, b: string, collidable: boolean } },
	problems: { string },
}
export type Adapter = {
	register: (name: string) -> (),
	setCollidable: (a: string, b: string, collidable: boolean) -> (),
}

local function key(a: string, b: string): string
	if a > b then
		a, b = b, a
	end
	return a .. "|" .. b
end

function CollisionMatrix.plan(spec: Spec): Plan
	local problems: { string } = {}
	local known: { [string]: boolean } = { Default = true }
	local register: { string } = {}
	for _, name in spec.groups do
		if name == "Default" then
			table.insert(problems, "Default always exists, remove it from groups")
		elseif known[name] then
			table.insert(problems, `duplicate group {name}`)
		elseif not string.match(name, "^[%w_ ]+$") or #name > 100 then
			table.insert(
				problems,
				`group name '{name}' must be letters, digits, space or underscore, at most 100 characters`
			)
		else
			known[name] = true
			table.insert(register, name)
		end
	end
	local limit = spec.limit or 32
	local total = #register + 1
	if total > limit then
		table.insert(problems, `{total} groups including Default exceeds the budget of {limit}`)
	end

	local wanted: { [string]: boolean } = {}
	local order: { string } = {}
	local pairNames: { [string]: { string } } = {}
	local function note(list: { { string } }?, collidable: boolean)
		for _, pair in (list or {}) :: { { string } } do
			local a, b = pair[1], pair[2]
			if a == nil or b == nil or not known[a] or not known[b] then
				table.insert(problems, `pair {tostring(a)}/{tostring(b)} names an unknown group`)
			else
				local k = key(a, b)
				if wanted[k] ~= nil and wanted[k] ~= collidable then
					table.insert(problems, `pair {a}/{b} is listed as both colliding and not colliding`)
				end
				if wanted[k] == nil then
					table.insert(order, k)
					pairNames[k] = if a < b then { a, b } else { b, a }
				end
				wanted[k] = collidable
			end
		end
	end
	note(spec.noCollide, false)
	note(spec.collide, true)

	table.sort(order)
	local pairs: { { a: string, b: string, collidable: boolean } } = {}
	for _, k in order do
		if not wanted[k] then
			table.insert(pairs, { a = pairNames[k][1], b = pairNames[k][2], collidable = false })
		end
	end
	table.sort(problems)
	return { register = register, pairs = pairs, problems = problems }
end

function CollisionMatrix.matrix(spec: Spec): string
	local plan = CollisionMatrix.plan(spec)
	local off: { [string]: boolean } = {}
	for _, p in plan.pairs do
		off[key(p.a, p.b)] = true
	end
	local names = { "Default" }
	for _, g in plan.register do
		table.insert(names, g)
	end
	local lines = { "        " .. table.concat(names, " ") }
	for _, a in names do
		local row = {}
		for _, b in names do
			table.insert(row, string.rep(" ", math.max(0, #b - 1)) .. (if off[key(a, b)] then "." else "X"))
		end
		table.insert(lines, string.format("%-7s %s", a, table.concat(row, " ")))
	end
	return table.concat(lines, "\n")
end

function CollisionMatrix.apply(plan: Plan, adapter: Adapter): boolean
	if #plan.problems > 0 then
		return false
	end
	for _, name in plan.register do
		adapter.register(name)
	end
	for _, p in plan.pairs do
		adapter.setCollidable(p.a, p.b, p.collidable)
	end
	return true
end

function CollisionMatrix.assign(root: Instance, group: string): RBXScriptConnection
	local function set(inst: Instance)
		if inst:IsA("BasePart") then
			inst.CollisionGroup = group
		end
	end
	set(root)
	for _, inst in root:GetDescendants() do
		set(inst)
	end
	return root.DescendantAdded:Connect(set)
end

return CollisionMatrix
