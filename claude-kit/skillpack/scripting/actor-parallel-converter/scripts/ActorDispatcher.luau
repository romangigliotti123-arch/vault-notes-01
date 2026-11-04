--!strict
-- The worker fires the BindableEvent after task.synchronize() because most write APIs are not allowed in the parallel phase.
local ActorDispatcher = {}
ActorDispatcher.__index = ActorDispatcher

export type Batch = {
	partition: (items: { any }, workers: number) -> { { any } },
	merge: (results: { [number]: { any } }) -> { any },
}
export type ActorLike = { SendMessage: (self: any, topic: string, ...any) -> () }
export type EventLike = {
	Event: { Connect: (self: any, fn: (...any) -> ()) -> { Disconnect: (self: any) -> () } },
	Destroy: (self: any) -> (),
}
export type IO = { newEvent: () -> EventLike, wait: () -> (), clock: () -> number }
export type Dispatcher = typeof(setmetatable(
	{} :: { _actors: { ActorLike }, _topic: string, _batch: Batch, _io: IO },
	ActorDispatcher
))

local function defaultIO(): IO
	return {
		newEvent = function(): EventLike
			return Instance.new("BindableEvent") :: any
		end,
		wait = function()
			task.wait()
		end,
		clock = os.clock,
	}
end

function ActorDispatcher.new(actors: { ActorLike }, topic: string, batch: Batch, io: IO?): Dispatcher
	assert(#actors > 0, "ActorDispatcher needs at least one Actor")
	return setmetatable({ _actors = actors, _topic = topic, _batch = batch, _io = io or defaultIO() }, ActorDispatcher)
end

function ActorDispatcher.Run(self: Dispatcher, items: { any }, timeoutSeconds: number): ({ any }?, string?)
	local chunks = self._batch.partition(items, #self._actors)
	if #chunks == 0 then
		return {}, nil
	end
	local done = self._io.newEvent()
	local results: { [number]: { any } } = {}
	local pending = #chunks
	local connection = done.Event:Connect(function(chunkIndex: number, output: { any })
		results[chunkIndex] = output
		pending -= 1
	end)
	for i, chunk in chunks do
		self._actors[i]:SendMessage(self._topic, i, chunk, done)
	end
	local started = self._io.clock()
	while pending > 0 and self._io.clock() - started < timeoutSeconds do
		self._io.wait()
	end
	connection:Disconnect()
	done:Destroy()
	if pending > 0 then
		return nil, `{pending} of {#chunks} chunks did not return within {timeoutSeconds}s`
	end
	return self._batch.merge(results), nil
end

return ActorDispatcher
