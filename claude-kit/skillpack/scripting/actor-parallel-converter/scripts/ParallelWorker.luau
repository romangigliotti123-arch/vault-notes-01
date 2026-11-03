--!strict
-- ParallelWorker: template for the Script that lives inside each Actor. Copy it, then replace `compute` with your pure function.
-- `compute` must only read data it was given (the chunk is deep-copied into the message) and call parallel-safe APIs; check each
-- API's thread-safety tier in the docs before using it here. Anything that writes to the DataModel happens after task.synchronize().
local actor = script:GetActor()
assert(actor, "ParallelWorker must be a descendant of an Actor")

-- replace with the real per-item work: no yields, no instance writes, no globals shared with other Actors
local function compute(item: any): any
	return item
end

actor:BindToMessageParallel("Work", function(chunkIndex: number, chunk: { any }, done: BindableEvent)
	local output: { any } = table.create(#chunk)
	for i, item in chunk do
		output[i] = compute(item)
	end
	task.synchronize()
	done:Fire(chunkIndex, output)
end)
