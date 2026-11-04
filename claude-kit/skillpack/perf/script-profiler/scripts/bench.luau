--!strict
local bench = {}

export type Result = { name: string, perCallMicros: number, batches: { number } }

local BATCHES = 7

function bench.run(name: string, fn: () -> (), iterations: number): Result
	for _ = 1, math.max(1, iterations // 10) do
		fn()
	end
	local batches = {}
	for _ = 1, BATCHES do
		local t0 = os.clock()
		for _ = 1, iterations do
			fn()
		end
		table.insert(batches, (os.clock() - t0) / iterations * 1e6)
	end
	table.sort(batches)
	return { name = name, perCallMicros = batches[(BATCHES + 1) // 2], batches = batches }
end

function bench.noise(r: Result): number
	local med = r.perCallMicros
	if med <= 0 then
		return 0
	end
	return (r.batches[#r.batches] - r.batches[1]) / med
end

function bench.compare(nameA: string, fnA: () -> (), nameB: string, fnB: () -> (), iterations: number): string
	local a = bench.run(nameA, fnA, iterations)
	local b = bench.run(nameB, fnB, iterations)
	local faster, slower = a, b
	if b.perCallMicros < a.perCallMicros then
		faster, slower = b, a
	end
	local ratio = if faster.perCallMicros > 0 then slower.perCallMicros / faster.perCallMicros else math.huge
	local trust = if math.max(bench.noise(a), bench.noise(b)) > 0.2
		then " (NOISY: rerun with more iterations before trusting this)"
		else ""
	return string.format(
		"%s: %.3f us/call | %s: %.3f us/call | %s is %.2fx faster%s",
		a.name,
		a.perCallMicros,
		b.name,
		b.perCallMicros,
		faster.name,
		ratio,
		trust
	)
end

return bench
