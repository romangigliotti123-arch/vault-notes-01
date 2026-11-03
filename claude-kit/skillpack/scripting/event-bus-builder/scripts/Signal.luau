--!strict
-- Signal: a small typed signal for decoupled systems. Handlers run in connection order; disconnecting during a Fire is safe;
-- Destroy drops every handler so nothing keeps a module alive. Server and client.
--   local Signal = require(script.Parent.Signal)
--   local died = Signal.new() :: Signal.Signal<Player, string>
--   local c = died:Connect(function(player, cause) end)
--   died:Fire(player, "fall")        c:Disconnect()       died:Destroy()
-- Handlers that yield are started with task.spawn, so a slow handler never blocks Fire or the other handlers.
local Signal = {}

export type Connection = { Connected: boolean, Disconnect: (self: Connection) -> () }
export type Signal<T...> = {
	Connect: (self: Signal<T...>, handler: (T...) -> ()) -> Connection,
	Once: (self: Signal<T...>, handler: (T...) -> ()) -> Connection,
	Wait: (self: Signal<T...>) -> T...,
	Fire: (self: Signal<T...>, T...) -> (),
	Count: (self: Signal<T...>) -> number,
	DisconnectAll: (self: Signal<T...>) -> (),
	Destroy: (self: Signal<T...>) -> (),
}

type Spawner = (target: any, ...any) -> ()

-- task.spawn in Roblox. Outside Roblox (Lune tests) fall back to a plain call or resume.
local function defaultSpawn(target: any, ...: any)
	if task then
		(task.spawn :: any)(target, ...)
	elseif type(target) == "thread" then
		coroutine.resume(target, ...)
	else
		target(...)
	end
end

type Node = { handler: (...any) -> (), connection: Connection, once: boolean }

function Signal.new<T...>(spawner: Spawner?): Signal<T...>
	local spawn: Spawner = spawner or defaultSpawn
	local nodes: { Node } = {}
	local destroyed = false
	local self = {} :: any

	local function connect(handler: (...any) -> (), once: boolean): Connection
		local connection: Connection
		connection = {
			Connected = not destroyed,
			Disconnect = function(c: Connection)
				c.Connected = false
				for i, node in nodes do
					if node.connection == c then
						table.remove(nodes, i)
						break
					end
				end
			end,
		}
		if not destroyed then
			table.insert(nodes, { handler = handler, connection = connection, once = once })
		end
		return connection
	end

	function self.Connect(_s: any, handler: (...any) -> ()): Connection
		return connect(handler, false)
	end

	function self.Once(_s: any, handler: (...any) -> ()): Connection
		return connect(handler, true)
	end

	function self.Fire(_s: any, ...: any)
		if destroyed then
			return
		end
		local snapshot = table.clone(nodes)
		for _, node in snapshot do
			if node.connection.Connected then
				if node.once then
					node.connection:Disconnect()
				end
				spawn(node.handler, ...)
			end
		end
	end

	function self.Wait(_s: any): ...any
		local thread = coroutine.running()
		connect(function(...: any)
			spawn(thread, ...)
		end, true)
		return coroutine.yield()
	end

	function self.Count(_s: any): number
		return #nodes
	end

	function self.DisconnectAll(_s: any)
		for _, node in table.clone(nodes) do
			node.connection.Connected = false
		end
		table.clear(nodes)
	end

	function self.Destroy(_s: any)
		self:DisconnectAll()
		destroyed = true
	end

	return self :: Signal<T...>
end

return Signal
