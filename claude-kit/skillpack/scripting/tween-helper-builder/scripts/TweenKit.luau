--!strict
local TweenKit = {}
TweenKit.__index = TweenKit

export type ConnectionLike = { Disconnect: (self: ConnectionLike) -> () }
export type TweenLike = {
	Play: (self: TweenLike) -> (),
	Cancel: (self: TweenLike) -> (),
	Completed: { Connect: (self: any, fn: (state: any) -> ()) -> ConnectionLike },
}
export type ServiceLike = { Create: (self: ServiceLike, instance: any, info: any, goal: { [string]: any }) -> TweenLike }
export type Step = { any }
export type Handle = { Cancel: (self: Handle) -> () }

type Active = { tween: TweenLike, props: { [string]: boolean }, cancel: () -> () }

export type Kit = typeof(setmetatable({} :: { _service: ServiceLike, _active: { [any]: { Active } } }, TweenKit))

function TweenKit.new(service: ServiceLike): Kit
	return setmetatable({ _service = service, _active = {} }, TweenKit)
end

local function overlaps(a: { [string]: boolean }, b: { [string]: boolean }): boolean
	for k in a do
		if b[k] then
			return true
		end
	end
	return false
end

function TweenKit.Play(
	self: Kit,
	instance: any,
	info: any,
	goal: { [string]: any },
	onDone: ((completed: boolean) -> ())?
): Handle
	local props: { [string]: boolean } = {}
	for k in goal do
		props[k] = true
	end
	for _, other in table.clone((self._active[instance] or {}) :: { Active }) do
		if overlaps(other.props, props) then
			other.cancel()
		end
	end
	local list = self._active[instance]
	if list == nil then
		list = {}
		self._active[instance] = list
	end

	local tween = self._service:Create(instance, info, goal)
	local finished = false
	local connection: ConnectionLike? = nil
	local entry: Active
	local function finish(completed: boolean)
		if finished then
			return
		end
		finished = true
		if connection then
			connection:Disconnect()
		end
		local current = self._active[instance]
		if current then
			local at = table.find(current, entry)
			if at then
				table.remove(current, at)
			end
			if #current == 0 then
				self._active[instance] = nil
			end
		end
		if onDone then
			onDone(completed)
		end
	end
	entry = {
		tween = tween,
		props = props,
		cancel = function()
			if not finished then
				tween:Cancel()
				finish(false)
			end
		end,
	}
	table.insert(list :: { Active }, entry)
	connection = tween.Completed:Connect(function()
		finish(true)
	end)
	tween:Play()
	return {
		Cancel = function()
			entry.cancel()
		end,
	} :: Handle
end

function TweenKit.Chain(self: Kit, steps: { Step }, onDone: ((completed: boolean) -> ())?): Handle
	local cancelled = false
	local current: Handle? = nil
	local function run(i: number)
		if cancelled then
			return
		end
		local step = steps[i]
		if step == nil then
			if onDone then
				onDone(true)
			end
			return
		end
		current = self:Play(step[1], step[2], step[3], function(completed: boolean)
			if completed then
				run(i + 1)
			elseif not cancelled then
				cancelled = true
				if onDone then
					onDone(false)
				end
			end
		end)
	end
	run(1)
	return {
		Cancel = function()
			if not cancelled then
				cancelled = true
				if current then
					current:Cancel()
				end
				if onDone then
					onDone(false)
				end
			end
		end,
	} :: Handle
end

function TweenKit.Cancel(self: Kit, instance: any)
	local list = self._active[instance]
	if list then
		for _, entry in table.clone(list) do
			entry.cancel()
		end
	end
end

function TweenKit.ActiveCount(self: Kit): number
	local n = 0
	for _, list in self._active do
		n += #list
	end
	return n
end

function TweenKit.Destroy(self: Kit)
	for instance in table.clone(self._active) do
		self:Cancel(instance)
	end
end

return TweenKit
