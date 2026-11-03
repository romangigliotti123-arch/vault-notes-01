--!strict
-- Janitor: one object that owns everything a system creates and releases it in reverse order. The fix for most leak findings.
--   local jan = Janitor.new()
--   jan:Add(part)                       -- Instance: Destroy
--   jan:Connect(signal, handler)        -- RBXScriptSignal: stores the connection
--   jan:Add(function() ... end)         -- function: called
--   jan:Add(task.spawn(loop))           -- thread: cancelled
--   jan:Cleanup()                       -- run once when the player leaves / the round ends / the model is removed
-- Cleanup is idempotent and keeps going if one item throws (the first error is returned, not raised).
local Janitor = {}
Janitor.__index = Janitor

export type Janitor = typeof(setmetatable({} :: { _items: { any }, _cleaning: boolean }, Janitor))

function Janitor.new(): Janitor
	return setmetatable({ _items = {}, _cleaning = false }, Janitor)
end

local function release(item: any): ()
	local kind = typeof(item)
	if kind == "function" then
		item()
	elseif kind == "thread" then
		if task then
			task.cancel(item)
		else
			coroutine.close(item)
		end
	elseif kind == "RBXScriptConnection" then
		item:Disconnect()
	elseif kind == "Instance" then
		item:Destroy()
	elseif kind == "table" then
		if type(item.Destroy) == "function" then
			item:Destroy()
		elseif type(item.Disconnect) == "function" then
			item:Disconnect()
		end
	end
end

function Janitor.Add<T>(self: Janitor, item: T): T
	if self._cleaning then
		pcall(release, item)
		return item
	end
	table.insert(self._items, item)
	return item
end

function Janitor.Connect(self: Janitor, signal: any, handler: (...any) -> ()): any
	return self:Add(signal:Connect(handler))
end

function Janitor.Count(self: Janitor): number
	return #self._items
end

-- release everything, newest first; returns the first error message, if any
function Janitor.Cleanup(self: Janitor): string?
	if self._cleaning then
		return nil
	end
	self._cleaning = true
	local firstError: string? = nil
	for i = #self._items, 1, -1 do
		local item = self._items[i]
		self._items[i] = nil
		local ok, err = pcall(release :: (any) -> any, item)
		if not ok and firstError == nil then
			firstError = tostring(err)
		end
	end
	self._cleaning = false
	return firstError
end

Janitor.Destroy = Janitor.Cleanup

return Janitor
