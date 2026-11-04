--!strict
local ParallelBatch = {}

function ParallelBatch.partition<T>(items: { T }, workers: number): { { T } }
	local count = #items
	local n = math.max(1, math.min(math.floor(workers), count))
	if count == 0 then
		return {}
	end
	local chunks: { { T } } = {}
	local base, extra = count // n, count % n
	local cursor = 1
	for i = 1, n do
		local size = base + (if i <= extra then 1 else 0)
		local chunk: { T } = {}
		for k = cursor, cursor + size - 1 do
			table.insert(chunk, items[k])
		end
		table.insert(chunks, chunk)
		cursor += size
	end
	return chunks
end

function ParallelBatch.merge<T>(results: { [number]: { T } }): { T }
	local indexes = {}
	for i in results do
		table.insert(indexes, i)
	end
	table.sort(indexes)
	local out: { T } = {}
	for _, i in indexes do
		for _, v in results[i] do
			table.insert(out, v)
		end
	end
	return out
end

export type Plan = { parallel: boolean, workers: number, reason: string }

function ParallelBatch.plan(
	itemCount: number,
	perItemMs: number,
	frameBudgetMs: number,
	maxWorkers: number,
	overheadMs: number?
): Plan
	local overhead = overheadMs or 0.3
	local serialMs = itemCount * perItemMs
	if serialMs <= frameBudgetMs * 0.25 then
		return {
			parallel = false,
			workers = 1,
			reason = "serial work is under a quarter of the frame budget; keep it serial",
		}
	end
	local workers = math.max(1, math.min(maxWorkers, itemCount))
	local parallelMs = serialMs / workers + overhead * workers
	if parallelMs >= serialMs * 0.8 then
		return {
			parallel = false,
			workers = 1,
			reason = "estimated gain is under 20 percent after split and message overhead",
		}
	end
	return {
		parallel = true,
		workers = workers,
		reason = `estimated {string.format("%.1f", serialMs)} ms serial vs {string.format("%.1f", parallelMs)} ms across {workers} actors`,
	}
end

return ParallelBatch
