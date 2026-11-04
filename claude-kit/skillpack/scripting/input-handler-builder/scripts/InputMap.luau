--!strict
local InputMap = {}
InputMap.__index = InputMap

export type Binding = {
	inputs: { any },
	touchButton: boolean?,
	priority: number?,
	title: string?,
	throttle: number?,
}
export type Handler = (phase: string) -> ()
export type CasLike = {
	BindAction: (
		self: any,
		name: string,
		fn: (name: string, state: any, input: any) -> any,
		touch: boolean,
		...any
	) -> (),
	BindActionAtPriority: (
		self: any,
		name: string,
		fn: (name: string, state: any, input: any) -> any,
		touch: boolean,
		priority: number,
		...any
	) -> (),
	UnbindAction: (self: any, name: string) -> (),
	SetTitle: (self: any, name: string, title: string) -> (),
}
export type Results = { sink: any, pass: any }
type Entry = { binding: Binding, handler: Handler, down: boolean, lastBegin: number }
export type Map = typeof(setmetatable(
	{} :: { _cas: CasLike, _results: Results, _clock: () -> number, _entries: { [string]: Entry } },
	InputMap
))

function InputMap.new(cas: CasLike, results: Results, clock: (() -> number)?): Map
	return setmetatable({ _cas = cas, _results = results, _clock = clock or os.clock, _entries = {} }, InputMap)
end

local function register(self: Map, name: string, entry: Entry)
	local function callback(_: string, state: any, _input: any): any
		local phase: string = state.Name
		if phase == "Begin" then
			local now = self._clock()
			local limit = entry.binding.throttle
			if limit and now - entry.lastBegin < limit then
				return self._results.sink
			end
			entry.lastBegin = now
			entry.down = true
		elseif phase == "End" or phase == "Cancel" then
			entry.down = false
		end
		entry.handler(phase)
		return self._results.sink
	end
	local binding = entry.binding
	local touch = binding.touchButton == true
	if binding.priority then
		self._cas:BindActionAtPriority(name, callback, touch, binding.priority, table.unpack(binding.inputs))
	else
		self._cas:BindAction(name, callback, touch, table.unpack(binding.inputs))
	end
	if touch and binding.title then
		self._cas:SetTitle(name, binding.title)
	end
end

function InputMap.Bind(self: Map, name: string, binding: Binding, handler: Handler)
	if self._entries[name] then
		self:Unbind(name)
	end
	local entry: Entry = { binding = binding, handler = handler, down = false, lastBegin = -math.huge }
	self._entries[name] = entry
	register(self, name, entry)
end

function InputMap.Rebind(self: Map, name: string, inputs: { any }): boolean
	local entry = self._entries[name]
	if entry == nil then
		return false
	end
	self._cas:UnbindAction(name)
	entry.binding = table.clone(entry.binding)
	entry.binding.inputs = inputs
	entry.down = false
	register(self, name, entry)
	return true
end

function InputMap.IsDown(self: Map, name: string): boolean
	local entry = self._entries[name]
	return entry ~= nil and entry.down
end

function InputMap.Unbind(self: Map, name: string)
	if self._entries[name] then
		self._cas:UnbindAction(name)
		self._entries[name] = nil
	end
end

function InputMap.UnbindAll(self: Map)
	for name in table.clone(self._entries) do
		self:Unbind(name)
	end
end

function InputMap.Bound(self: Map): { string }
	local names = {}
	for name in self._entries do
		table.insert(names, name)
	end
	table.sort(names)
	return names
end

return InputMap
