--!strict
local AttributeConfig = {}
AttributeConfig.__index = AttributeConfig

export type Field = { kind: string, default: any, min: number?, max: number?, allowed: { any }? }
export type Schema = { [string]: Field }
export type InstanceLike = {
	GetAttribute: (self: any, name: string) -> any,
	SetAttribute: (self: any, name: string, value: any) -> (),
	GetAttributeChangedSignal: (
		self: any,
		name: string
	) -> { Connect: (self: any, fn: () -> ()) -> { Disconnect: (self: any) -> () } },
}
export type Bound = typeof(setmetatable(
	{} :: {
		_instance: InstanceLike,
		_schema: Schema,
		_good: { [string]: any },
		_connections: { { Disconnect: (self: any) -> () } },
		_writing: boolean,
		_onChange: ((name: string, new: any, old: any) -> ())?,
	},
	AttributeConfig
))

function AttributeConfig.coerce(field: Field, value: any): (boolean, any)
	if type(value) ~= field.kind then
		return false, nil
	end
	if field.kind == "number" then
		local n = value :: number
		if n ~= n or n == math.huge or n == -math.huge then
			return false, nil
		end
		if field.min and n < field.min then
			n = field.min
		end
		if field.max and n > field.max then
			n = field.max
		end
		return true, n
	end
	if field.allowed and not table.find(field.allowed, value) then
		return false, nil
	end
	return true, value
end

function AttributeConfig.validateSchema(schema: Schema): { string }
	local problems = {}
	for name, field in schema do
		if field.kind ~= "number" and field.kind ~= "string" and field.kind ~= "boolean" then
			table.insert(problems, `{name}: kind must be number, string or boolean`)
		elseif field.min and field.max and field.min > field.max then
			table.insert(problems, `{name}: min is above max`)
		else
			local ok, fixed = AttributeConfig.coerce(field, field.default)
			if not ok or fixed ~= field.default then
				table.insert(problems, `{name}: default is not valid for its own rules`)
			end
		end
	end
	table.sort(problems)
	return problems
end

local function write(self: Bound, name: string, value: any)
	self._writing = true
	self._instance:SetAttribute(name, value)
	self._writing = false
end

function AttributeConfig.bind(
	instance: InstanceLike,
	schema: Schema,
	onChange: ((name: string, new: any, old: any) -> ())?
): Bound
	local problems = AttributeConfig.validateSchema(schema)
	if #problems > 0 then
		error("AttributeConfig: " .. table.concat(problems, "; "), 2)
	end
	local self = setmetatable({
		_instance = instance,
		_schema = schema,
		_good = {},
		_connections = {},
		_writing = false,
		_onChange = onChange,
	}, AttributeConfig)
	for name, field in schema do
		local ok, value = AttributeConfig.coerce(field, instance:GetAttribute(name))
		if not ok then
			value = field.default
		end
		self._good[name] = value
		if instance:GetAttribute(name) ~= value then
			write(self, name, value)
		end
		table.insert(
			self._connections,
			instance:GetAttributeChangedSignal(name):Connect(function()
				if self._writing then
					return
				end
				local accepted, clean = AttributeConfig.coerce(field, instance:GetAttribute(name))
				if not accepted then
					write(self, name, self._good[name])
					return
				end
				if clean ~= instance:GetAttribute(name) then
					write(self, name, clean)
				end
				local old = self._good[name]
				self._good[name] = clean
				if old ~= clean and self._onChange then
					self._onChange(name, clean, old)
				end
			end)
		)
	end
	return self
end

function AttributeConfig.Get(self: Bound, name: string): any
	return self._good[name]
end

function AttributeConfig.Set(self: Bound, name: string, value: any): boolean
	local field = self._schema[name]
	if field == nil then
		return false
	end
	local ok, clean = AttributeConfig.coerce(field, value)
	if not ok then
		return false
	end
	local old = self._good[name]
	self._good[name] = clean
	write(self, name, clean)
	if old ~= clean and self._onChange then
		self._onChange(name, clean, old)
	end
	return true
end

function AttributeConfig.Snapshot(self: Bound): { [string]: any }
	return table.clone(self._good)
end

function AttributeConfig.Destroy(self: Bound)
	for _, c in self._connections do
		c:Disconnect()
	end
	table.clear(self._connections)
end

return AttributeConfig
