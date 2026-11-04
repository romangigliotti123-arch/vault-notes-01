--!strict
local Pairwise = {}

export type Param = { name: string, values: { string } }
export type Row = { [string]: string }

local MAX_PRODUCT = 50000

local function product(params: { Param }): number
	local n = 1
	for _, p in params do
		n *= #p.values
	end
	return n
end

local function pairKey(i: number, a: string, j: number, b: string): string
	return `{i}={a}|{j}={b}`
end

function Pairwise.generate(
	params: { Param },
	exclude: ((row: Row) -> boolean)?
): { rows: { Row }, uncoverable: { string } }
	assert(product(params) <= MAX_PRODUCT, "too many combinations for the greedy search: reduce values per parameter")
	local candidates: { { string } } = {}
	local idx = table.create(#params, 1)
	local total = product(params)
	for _ = 1, total do
		local vals = {}
		for i, p in params do
			vals[i] = p.values[idx[i]]
		end
		local ok = true
		if exclude then
			local row: Row = {}
			for i, p in params do
				row[p.name] = vals[i]
			end
			ok = not exclude(row)
		end
		if ok then
			table.insert(candidates, vals)
		end
		for i = #params, 1, -1 do
			idx[i] += 1
			if idx[i] <= #params[i].values then
				break
			end
			idx[i] = 1
		end
	end
	local uncovered: { [string]: boolean } = {}
	local pairsLeft = 0
	for i = 1, #params do
		for j = i + 1, #params do
			for _, a in params[i].values do
				for _, b in params[j].values do
					uncovered[pairKey(i, a, j, b)] = true
					pairsLeft += 1
				end
			end
		end
	end
	local rows: { Row } = {}
	local function gain(vals: { string }): number
		local g = 0
		for i = 1, #params do
			for j = i + 1, #params do
				if uncovered[pairKey(i, vals[i], j, vals[j])] then
					g += 1
				end
			end
		end
		return g
	end
	while pairsLeft > 0 do
		local best, bestGain = nil, 0
		for _, vals in candidates do
			local g = gain(vals)
			if g > bestGain then
				best, bestGain = vals, g
			end
		end
		if best == nil then
			break
		end
		local row: Row = {}
		for i, p in params do
			row[p.name] = best[i]
		end
		table.insert(rows, row)
		for i = 1, #params do
			for j = i + 1, #params do
				local k = pairKey(i, best[i], j, best[j])
				if uncovered[k] then
					uncovered[k] = nil
					pairsLeft -= 1
				end
			end
		end
	end
	local left = {}
	for k in uncovered do
		table.insert(left, k)
	end
	table.sort(left)
	return { rows = rows, uncoverable = left }
end

function Pairwise.coverage(params: { Param }, rows: { Row }): (number, number)
	local seen: { [string]: boolean } = {}
	for _, row in rows do
		for i = 1, #params do
			for j = i + 1, #params do
				seen[pairKey(i, row[params[i].name], j, row[params[j].name])] = true
			end
		end
	end
	local covered, total = 0, 0
	for i = 1, #params do
		for j = i + 1, #params do
			for _, a in params[i].values do
				for _, b in params[j].values do
					total += 1
					if seen[pairKey(i, a, j, b)] then
						covered += 1
					end
				end
			end
		end
	end
	return covered, total
end

function Pairwise.format(params: { Param }, rows: { Row }): string
	local head = {}
	for _, p in params do
		table.insert(head, p.name)
	end
	local lines = { "| # | " .. table.concat(head, " | ") .. " |", "|---|" .. string.rep("---|", #params) }
	for n, row in rows do
		local cells = {}
		for _, p in params do
			table.insert(cells, row[p.name])
		end
		table.insert(lines, `| {n} | ` .. table.concat(cells, " | ") .. " |")
	end
	return table.concat(lines, "\n")
end

return Pairwise
