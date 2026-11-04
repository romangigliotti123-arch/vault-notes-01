--!strict
local TagBinder = {}
TagBinder.__index = TagBinder

export type Cleanup = (() -> ()) | { Destroy: (self: any) -> () } | nil
export type SignalLike = { Connect: (self: any, fn: (instance: any) -> ()) -> { Disconnect: (self: any) -> () } }
export type ServiceLike = {
	GetTagged: (self: any, tag: string) -> { any },
	GetInstanceAddedSignal: (self: any, tag: string) -> SignalLike,
	GetInstanceRemovedSignal: (self: any, tag: string) -> SignalLike,
}
type Binding = { cleanups: { [any]: Cleanup }, connections: { { Disconnect: (self: any) -> () } } }
export type Binder = typeof(setmetatable(
	{} :: {
		_service: ServiceLike,
		_bindings: { [string]: Binding },
		_onError: (tag: string, instance: any, err: string) -> (),
	},
	TagBinder
))

function TagBinder.new(service: ServiceLike, onError: ((tag: string, instance: any, err: string) -> ())?): Binder
	local report = onError or function(tag: string, _instance: any, err: string)
		warn(`TagBinder {tag}: {err}`)
	end
	return setmetatable({ _service = service, _bindings = {}, _onError = report }, TagBinder)
end

local function runCleanup(cleanup: Cleanup)
	if type(cleanup) == "function" then
		cleanup()
	elseif type(cleanup) == "table" then
		cleanup:Destroy()
	end
end

function TagBinder.Bind(self: Binder, tag: string, behaviour: (instance: any) -> Cleanup)
	assert(self._bindings[tag] == nil, `tag {tag} is already bound`)
	local binding: Binding = { cleanups = {}, connections = {} }
	self._bindings[tag] = binding

	local function attach(instance: any)
		if binding.cleanups[instance] ~= nil then
			return
		end
		binding.cleanups[instance] = false :: any
		local ok, result = pcall(behaviour :: (any) -> any, instance)
		if ok then
			binding.cleanups[instance] = result or false :: any
		else
			binding.cleanups[instance] = nil
			self._onError(tag, instance, tostring(result))
		end
	end
	local function detach(instance: any)
		local cleanup = binding.cleanups[instance]
		binding.cleanups[instance] = nil
		if cleanup then
			local ok, err = pcall(runCleanup :: (any) -> any, cleanup)
			if not ok then
				self._onError(tag, instance, tostring(err))
			end
		end
	end

	table.insert(binding.connections, self._service:GetInstanceAddedSignal(tag):Connect(attach))
	table.insert(binding.connections, self._service:GetInstanceRemovedSignal(tag):Connect(detach))
	for _, instance in self._service:GetTagged(tag) do
		attach(instance)
	end
end

function TagBinder.Count(self: Binder, tag: string): number
	local binding = self._bindings[tag]
	local n = 0
	if binding then
		for _ in binding.cleanups do
			n += 1
		end
	end
	return n
end

function TagBinder.Unbind(self: Binder, tag: string)
	local binding = self._bindings[tag]
	if binding == nil then
		return
	end
	self._bindings[tag] = nil
	for _, c in binding.connections do
		c:Disconnect()
	end
	for instance, cleanup in binding.cleanups do
		if cleanup then
			local ok, err = pcall(runCleanup :: (any) -> any, cleanup)
			if not ok then
				self._onError(tag, instance, tostring(err))
			end
		end
	end
end

function TagBinder.Destroy(self: Binder)
	for tag in table.clone(self._bindings) do
		self:Unbind(tag)
	end
end

return TagBinder
