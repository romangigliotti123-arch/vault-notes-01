--!strict
local StrictPlan = {}

export type Graph = {
	build: (modules: { [string]: string }) -> { edges: { [string]: { string } }, unknown: { [string]: { string } } },
	layers: (edges: { [string]: { string } }) -> { layers: { { string } }, cyclic: { string } },
}
export type Scanner = {
	scan: (source: string) -> { mode: string, anyCount: number },
	score: (report: any) -> number,
}
export type Row = { name: string, layer: number, mode: string, score: number, effort: string, note: string? }
export type Plan = { rows: { Row }, done: { string } }

function StrictPlan.effort(score: number): string
	if score <= 5 then
		return "small"
	elseif score <= 20 then
		return "medium"
	end
	return "large"
end

function StrictPlan.order(sources: { [string]: string }, graph: Graph, scanner: Scanner): Plan
	local built = graph.build(sources)
	local layered = graph.layers(built.edges)
	local rows: { Row } = {}
	local done: { string } = {}

	local function row(name: string, layer: number, note: string?): Row?
		local report = scanner.scan(sources[name])
		local score = scanner.score(report)
		local result: Row = {
			name = name,
			layer = layer,
			mode = report.mode,
			score = score,
			effort = StrictPlan.effort(score),
			note = note,
		}
		if result.mode == "strict" and score == 0 then
			table.insert(done, name)
			return nil
		end
		return result
	end

	for i, layer in layered.layers do
		local batch: { Row } = {}
		for _, name in layer do
			local r = row(name, i, nil)
			if r then
				table.insert(batch, r)
			end
		end
		table.sort(batch, function(a, b)
			if a.score ~= b.score then
				return a.score < b.score
			end
			return a.name < b.name
		end)
		for _, r in batch do
			table.insert(rows, r)
		end
	end
	for _, name in layered.cyclic do
		local r = row(
			name,
			#layered.layers + 1,
			"in a require cycle: break the cycle first (require-cycle-finder), types across a cycle are unreliable"
		)
		if r then
			table.insert(rows, r)
		end
	end
	table.sort(done)
	return { rows = rows, done = done }
end

return StrictPlan
