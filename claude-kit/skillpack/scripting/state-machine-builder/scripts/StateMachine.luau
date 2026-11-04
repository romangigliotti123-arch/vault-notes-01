--!strict
local StateMachine = {}
StateMachine.__index = StateMachine

export type State = {
	to: { string }?,
	enter: ((ctx: any, from: string?, ...any) -> ())?,
	exit: ((ctx: any, to: string) -> ())?,
	update: ((ctx: any, dt: number) -> ())?,
}
export type Definition = { initial: string, states: { [string]: State }, onChange: ((from: string?, to: string) -> ())? }
export type Machine = typeof(setmetatable(
	{} :: {
		_def: Definition,
		_ctx: any,
		_current: string,
		_busy: boolean,
		_queue: { { to: string, args: { any } } },
		_history: { string },
	},
	StateMachine
))

function StateMachine.validate(def: Definition): { string }
	local problems: { string } = {}
	if def.states[def.initial] == nil then
		table.insert(problems, `initial state '{def.initial}' is not defined`)
	end
	for name, state in def.states do
		for _, target in (state.to or {}) :: { string } do
			if def.states[target] == nil then
				table.insert(problems, `{name} -> {target}: target state is not defined`)
			end
		end
	end
	table.sort(problems)
	return problems
end

function StateMachine.new(def: Definition, ctx: any): Machine
	local problems = StateMachine.validate(def)
	if #problems > 0 then
		error("StateMachine: " .. table.concat(problems, "; "), 2)
	end
	local self = setmetatable({
		_def = def,
		_ctx = ctx,
		_current = def.initial,
		_busy = false,
		_queue = {},
		_history = { def.initial },
	}, StateMachine)
	local enter = def.states[def.initial].enter
	if enter then
		enter(ctx, nil)
	end
	return self
end

function StateMachine.Current(self: Machine): string
	return self._current
end

function StateMachine.Is(self: Machine, name: string): boolean
	return self._current == name
end

function StateMachine.History(self: Machine): { string }
	return table.clone(self._history)
end

function StateMachine.CanTransition(self: Machine, to: string): boolean
	local target = self._def.states[to]
	if target == nil then
		return false
	end
	local allowed = self._def.states[self._current].to
	return allowed == nil or table.find(allowed, to) ~= nil
end

local function apply(self: Machine, to: string, args: { any })
	local from = self._current
	local exit = self._def.states[from].exit
	if exit then
		exit(self._ctx, to)
	end
	self._current = to
	table.insert(self._history, to)
	if #self._history > 32 then
		table.remove(self._history, 1)
	end
	local enter = self._def.states[to].enter
	if enter then
		enter(self._ctx, from, table.unpack(args))
	end
	if self._def.onChange then
		self._def.onChange(from, to)
	end
end

function StateMachine.Transition(self: Machine, to: string, ...: any): boolean
	if not self:CanTransition(to) then
		return false
	end
	if self._busy then
		table.insert(self._queue, { to = to, args = { ... } })
		return true
	end
	self._busy = true
	apply(self, to, { ... })
	while #self._queue > 0 do
		local nextMove = table.remove(self._queue, 1) :: { to: string, args: { any } }
		if self:CanTransition(nextMove.to) then
			apply(self, nextMove.to, nextMove.args)
		end
	end
	self._busy = false
	return true
end

function StateMachine.Update(self: Machine, dt: number)
	local update = self._def.states[self._current].update
	if update then
		self._busy = true
		update(self._ctx, dt)
		self._busy = false
		local queued = self._queue
		self._queue = {}
		for _, move in queued do
			self:Transition(move.to, table.unpack(move.args))
		end
	end
end

return StateMachine
