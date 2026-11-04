<!-- cold: rbx-luau/cleaner-module.md | read when: read only when the project has no Maid, Janitor or Trove and you must write the Cleaner module. -->

## From skills/rbx-luau/SKILL.md :: ```lua

```lua
--!strict
local Cleaner = {}
Cleaner.__index = Cleaner

type Item = RBXScriptConnection | Instance | thread | () -> () | { Destroy: (any) -> () }

export type Cleaner = typeof(setmetatable({} :: { items: { Item } }, Cleaner))

function Cleaner.new(): Cleaner
	return setmetatable({ items = {} }, Cleaner)
end

function Cleaner.add(self: Cleaner, item: Item): Item
	table.insert(self.items, item)
	return item
end

function Cleaner.destroy(self: Cleaner)
	local items = self.items
	self.items = {}
	for i = #items, 1, -1 do
		local item = items[i]
		local kind = typeof(item)
		if kind == "RBXScriptConnection" then
			local conn = item :: RBXScriptConnection
			conn:Disconnect()
		elseif kind == "Instance" then
			local inst = item :: Instance
			inst:Destroy()
		elseif kind == "function" then
			local fn = item :: () -> ()
			fn()
		elseif kind == "thread" then
			pcall(task.cancel, item :: thread)
		else
			local obj = item :: { Destroy: (any) -> () }
			obj:Destroy()
		end
	end
end

return Cleaner
```
