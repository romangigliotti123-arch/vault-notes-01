--!strict
local Mocks = {}

export type Clock = { now: number, read: () -> number, advance: (seconds: number) -> () }
export type Spy = { calls: { { any } }, count: number, fn: (...any) -> ...any }
export type Signal = {
	Connect: (self: Signal, fn: (...any) -> ()) -> { Disconnect: (self: any) -> () },
	Fire: (self: Signal, ...any) -> (),
	ConnectionCount: (self: Signal) -> number,
}

function Mocks.clock(start: number?): Clock
	local clock = { now = start or 0 } :: Clock
	clock.read = function()
		return clock.now
	end
	clock.advance = function(seconds: number)
		clock.now += seconds
	end
	return clock
end

function Mocks.spy(inner: ((...any) -> ...any)?): Spy
	local spy = { calls = {}, count = 0 } :: Spy
	spy.fn = function(...: any): ...any
		spy.count += 1
		table.insert(spy.calls, { ... })
		if inner then
			return inner(...)
		end
		return
	end
	return spy
end

function Mocks.signal(): Signal
	local handlers: { (...any) -> () } = {}
	local signal = {} :: Signal
	function signal.Connect(_self: Signal, fn: (...any) -> ())
		table.insert(handlers, fn)
		return {
			Disconnect = function()
				local at = table.find(handlers, fn)
				if at then
					table.remove(handlers, at)
				end
			end,
		}
	end
	function signal.Fire(_self: Signal, ...: any)
		for _, fn in table.clone(handlers) do
			fn(...)
		end
	end
	function signal.ConnectionCount(_self: Signal): number
		return #handlers
	end
	return signal
end

export type Remote = {
	OnServerEvent: Signal,
	OnClientEvent: Signal,
	sent: { { player: any, args: { any } } },
	FireFromClient: (self: Remote, player: any, ...any) -> (),
	FireClient: (self: Remote, player: any, ...any) -> (),
}

function Mocks.remote(): Remote
	local remote = { OnServerEvent = Mocks.signal(), OnClientEvent = Mocks.signal(), sent = {} } :: Remote
	function remote.FireFromClient(self: Remote, player: any, ...: any)
		self.OnServerEvent:Fire(player, ...)
	end
	function remote.FireClient(self: Remote, player: any, ...: any)
		table.insert(self.sent, { player = player, args = { ... } })
	end
	return remote
end

export type Player = { UserId: number, Name: string, Parent: any, Leave: (self: Player) -> () }

function Mocks.player(userId: number, name: string?): Player
	local player = { UserId = userId, Name = name or ("Player" .. userId), Parent = {} } :: Player
	function player.Leave(self: Player)
		self.Parent = nil
	end
	return player
end

export type Store = {
	data: { [string]: any },
	calls: number,
	failNext: (self: Store, count: number) -> (),
	GetAsync: (self: Store, key: string) -> any,
	SetAsync: (self: Store, key: string, value: any) -> (),
	UpdateAsync: (self: Store, key: string, fn: (old: any) -> any) -> any,
}

function Mocks.store(): Store
	local failures = 0
	local store = { data = {}, calls = 0 } :: Store
	local function enter()
		store.calls += 1
		if failures > 0 then
			failures -= 1
			error("DataStore request was added to queue. If request queue fills, further requests will be dropped.", 0)
		end
	end
	function store.failNext(_self: Store, count: number)
		failures = count
	end
	function store.GetAsync(self: Store, key: string): any
		enter()
		return self.data[key]
	end
	function store.SetAsync(self: Store, key: string, value: any)
		enter()
		self.data[key] = value
	end
	function store.UpdateAsync(self: Store, key: string, fn: (old: any) -> any): any
		enter()
		local new = fn(self.data[key])
		if new ~= nil then
			self.data[key] = new
		end
		return new
	end
	return store
end

return Mocks
