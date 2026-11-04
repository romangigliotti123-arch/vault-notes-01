--!strict
local actor = script:GetActor()
assert(actor, "ParallelWorker must be a descendant of an Actor")

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
