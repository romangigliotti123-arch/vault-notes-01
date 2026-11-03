--!strict
-- RequireGraph: pure-string analysis of ModuleScript require() calls. Offline tool (run under Lune or in the command bar).
--   local g = RequireGraph.build({ A = sourceA, B = sourceB })
--   RequireGraph.findCycles(g.edges)      -> { { "A", "B" } }   one concrete cycle per tangled group
--   RequireGraph.layers(g.edges)          -> load order, leaves first
-- It reads text only: it never requires anything and never runs the modules.
local RequireGraph = {}

export type Edges = { [string]: { string } }
export type Built = { edges: Edges, unknown: { [string]: { string } } }
export type Layers = { layers: { { string } }, cyclic: { string } }

-- remove -- comments (line and block) so commented-out requires are not counted
function RequireGraph.stripComments(source: string): string
	local noBlock = string.gsub(source, "%-%-%[(=*)%[.-%]%1%]", "")
	local lines = {}
	for line in string.gmatch(noBlock .. "\n", "(.-)\n") do
		local cut = string.find(line, "--", 1, true)
		table.insert(lines, if cut then string.sub(line, 1, cut - 1) else line)
	end
	return table.concat(lines, "\n")
end

local function lastName(raw: string): string?
	local arg = string.gsub(raw, "[%)%s]+$", "")
	local literal = string.match(arg, "[\"']([^\"']+)[\"']%s*$")
	if literal then
		return string.match(literal, "([%w_%-]+)$")
	end
	return string.match(arg, "([%a_][%w_]*)%s*$")
end

-- names of modules a source requires: require(x.y.Name), require(x:WaitForChild("Name")), require("./Name")
function RequireGraph.extractRequires(source: string): { string }
	local clean = RequireGraph.stripComments(source)
	local found: { string } = {}
	local seen: { [string]: boolean } = {}
	for arg in string.gmatch(clean, "require%s*(%b())") do
		local name = lastName(string.sub(arg, 2, -2))
		if name and not seen[name] then
			seen[name] = true
			table.insert(found, name)
		end
	end
	return found
end

-- modules: name -> source. edges[name] = sorted list of required modules that exist in the set.
function RequireGraph.build(modules: { [string]: string }): Built
	local edges: Edges = {}
	local unknown: { [string]: { string } } = {}
	for name, source in modules do
		local deps, missing = {}, {}
		for _, dep in RequireGraph.extractRequires(source) do
			if modules[dep] ~= nil then
				table.insert(deps, dep)
			else
				table.insert(missing, dep)
			end
		end
		table.sort(deps)
		table.sort(missing)
		edges[name] = deps
		if #missing > 0 then
			unknown[name] = missing
		end
	end
	return { edges = edges, unknown = unknown }
end

local function sortedKeys(edges: Edges): { string }
	local keys = {}
	for k in edges do
		table.insert(keys, k)
	end
	table.sort(keys)
	return keys
end

-- Tarjan strongly connected components; returns groups with more than one member or a self-require
local function components(edges: Edges): { { string } }
	local index = 0
	local indices: { [string]: number } = {}
	local low: { [string]: number } = {}
	local onStack: { [string]: boolean } = {}
	local stack: { string } = {}
	local out: { { string } } = {}
	local function visit(v: string)
		index += 1
		indices[v] = index
		low[v] = index
		table.insert(stack, v)
		onStack[v] = true
		for _, w in (edges[v] or {}) :: { string } do
			if indices[w] == nil then
				visit(w)
				low[v] = math.min(low[v], low[w])
			elseif onStack[w] then
				low[v] = math.min(low[v], indices[w])
			end
		end
		if low[v] == indices[v] then
			local group = {}
			repeat
				local w = table.remove(stack) :: string
				onStack[w] = false
				table.insert(group, w)
			until w == v
			local selfLoop = #group == 1 and table.find(edges[v] or {}, v) ~= nil
			if #group > 1 or selfLoop then
				table.sort(group)
				table.insert(out, group)
			end
		end
	end
	for _, v in sortedKeys(edges) do
		if indices[v] == nil then
			visit(v)
		end
	end
	table.sort(out, function(a, b)
		return a[1] < b[1]
	end)
	return out
end

-- one concrete cycle (A, B, C means A -> B -> C -> A) per tangled group
function RequireGraph.findCycles(edges: Edges): { { string } }
	local cycles = {}
	for _, group in components(edges) do
		local inGroup: { [string]: boolean } = {}
		for _, m in group do
			inGroup[m] = true
		end
		local start = group[1]
		local path: { string } = {}
		local visited: { [string]: boolean } = {}
		local function walk(v: string): boolean
			table.insert(path, v)
			visited[v] = true
			for _, w in (edges[v] or {}) :: { string } do
				if w == start then
					return true
				end
				if inGroup[w] and not visited[w] and walk(w) then
					return true
				end
			end
			table.remove(path)
			return false
		end
		if walk(start) then
			table.insert(cycles, path)
		end
	end
	return cycles
end

-- heuristic: cut the edge whose source has the fewest dependencies (cheapest to make lazy or to invert)
function RequireGraph.suggestBreak(edges: Edges, cycle: { string }): (string, string)
	local bestFrom, bestTo, bestCost = cycle[1], cycle[2] or cycle[1], math.huge
	for i, from in cycle do
		local cost = #(edges[from] or {})
		if cost < bestCost then
			bestFrom, bestTo, bestCost = from, cycle[i % #cycle + 1], cost
		end
	end
	return bestFrom, bestTo
end

-- load order: layer 1 has no dependencies, layer n depends only on earlier layers. Tangled modules go to cyclic.
function RequireGraph.layers(edges: Edges): Layers
	local placed: { [string]: boolean } = {}
	local layers: { { string } } = {}
	local remaining = sortedKeys(edges)
	while #remaining > 0 do
		local layer: { string }, rest: { string } = {}, {}
		for _, m in remaining do
			local ready = true
			for _, d in edges[m] do
				if not placed[d] then
					ready = false
					break
				end
			end
			table.insert(if ready then layer else rest, m)
		end
		if #layer == 0 then
			return { layers = layers, cyclic = remaining }
		end
		for _, m in layer do
			placed[m] = true
		end
		table.insert(layers, layer)
		remaining = rest
	end
	return { layers = layers, cyclic = {} }
end

return RequireGraph
