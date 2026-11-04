--!strict

export type ArgSpec = {
	name: string,
	kind: "player" | "number" | "string" | "rest",
	min: number?,
	max: number?,
	optional: boolean?,
	outranks: boolean?,
}

export type Command = {
	minRank: number,
	help: string?,
	args: { ArgSpec },
	run: (actorId: number, args: { [string]: any }) -> string?,
}

export type Config = {
	commands: { [string]: Command },
	getRank: (userId: number) -> number,
	findPlayers: (query: string) -> { number },
	now: () -> number,
	prefix: string?,
	rateLimit: { count: number, window: number }?,
	audit: ((entry: AuditEntry) -> ())?,
}

export type AuditEntry = { actor: number, rank: number, command: string, args: string, ok: boolean, note: string? }

export type Result = { handled: boolean, ok: boolean, message: string? }

export type Admin = {
	Execute: (self: Admin, actorId: number, text: string) -> Result,
}

type Impl = {
	_c: Config,
	_times: { [number]: { number } },
}

local Admin = {}
Admin.__index = Admin

function Admin.new(config: Config): Admin
	local self = setmetatable({ _c = config, _times = {} }, Admin)
	return (self :: any) :: Admin
end

local function split(text: string): { string }
	local out = {}
	for w in string.gmatch(text, "%S+") do
		table.insert(out, w)
	end
	return out
end

local function audit(self: Impl, actor: number, rank: number, command: string, args: string, ok: boolean, note: string?)
	local f = self._c.audit
	if f then
		f({ actor = actor, rank = rank, command = command, args = args, ok = ok, note = note })
	end
end

local function limited(self: Impl, actor: number): boolean
	local rl = self._c.rateLimit or { count = 10, window = 10 }
	local now = self._c.now()
	local list = self._times[actor]
	if list == nil then
		list = {}
		self._times[actor] = list
	end
	local keep = {}
	for _, ts in list do
		if now - ts < rl.window then
			table.insert(keep, ts)
		end
	end
	if #keep >= rl.count then
		self._times[actor] = keep
		return true
	end
	table.insert(keep, now)
	self._times[actor] = keep
	return false
end

local function parseArg(
	self: Impl,
	spec: ArgSpec,
	words: { string },
	i: number,
	actor: number,
	actorRank: number
): (any, number, string?)
	if spec.kind == "rest" then
		local s = table.concat(words, " ", i)
		if s == "" then
			if spec.optional then
				return nil, #words + 1, nil
			end
			return nil, i, spec.name .. " is required"
		end
		if #s > (spec.max or 200) or #s < (spec.min or 0) then
			return nil, i, spec.name .. " has a bad length"
		end
		return s, #words + 1, nil
	end
	local w = words[i]
	if w == nil then
		if spec.optional then
			return nil, i, nil
		end
		return nil, i, spec.name .. " is required"
	end
	if spec.kind == "number" then
		local n = tonumber(w)
		if n == nil or n ~= n or n == math.huge or n == -math.huge then
			return nil, i, spec.name .. " must be a number"
		end
		if (spec.min and n < spec.min) or (spec.max and n > spec.max) then
			return nil, i, spec.name .. " out of range"
		end
		return n, i + 1, nil
	elseif spec.kind == "string" then
		if #w > (spec.max or 200) or #w < (spec.min or 0) then
			return nil, i, spec.name .. " has a bad length"
		end
		return w, i + 1, nil
	else
		local found = self._c.findPlayers(w)
		if #found == 0 then
			return nil, i, "no player matches '" .. string.sub(w, 1, 30) .. "'"
		end
		if #found > 1 then
			return nil, i, "several players match '" .. string.sub(w, 1, 30) .. "', be more specific"
		end
		local target = found[1]
		if spec.outranks ~= false and target ~= actor and self._c.getRank(target) >= actorRank then
			return nil, i, "you cannot target that player"
		end
		return target, i + 1, nil
	end
end

function Admin.Execute(self: Impl, actorId: number, text: string): Result
	local prefix = self._c.prefix or "/"
	if type(text) ~= "string" or #text > 300 or string.sub(text, 1, #prefix) ~= prefix then
		return { handled = false, ok = false }
	end
	local rank = self._c.getRank(actorId)
	if rank <= 0 then
		return { handled = false, ok = false }
	end
	local words = split(string.sub(text, #prefix + 1))
	local name = string.lower(words[1] or "")
	local cmd = self._c.commands[name]
	if cmd == nil or rank < cmd.minRank then
		audit(self, actorId, rank, name, "", false, "unknown or not allowed")
		return { handled = true, ok = false, message = "Unknown command." }
	end
	if limited(self, actorId) then
		audit(self, actorId, rank, name, "", false, "rate limited")
		return { handled = true, ok = false, message = "Slow down." }
	end
	local parsed: { [string]: any } = {}
	local i = 2
	for _, spec in cmd.args do
		local v, nextI, err = parseArg(self, spec, words, i, actorId, rank)
		if err then
			audit(self, actorId, rank, name, table.concat(words, " ", 2), false, err)
			return { handled = true, ok = false, message = err }
		end
		parsed[spec.name] = v
		i = nextI
	end
	local argText = table.concat(words, " ", 2)
	local ok, reply = pcall(cmd.run, actorId, parsed)
	if not ok then
		audit(self, actorId, rank, name, argText, false, "error: " .. tostring(reply))
		return { handled = true, ok = false, message = "Command failed." }
	end
	audit(self, actorId, rank, name, argText, true, nil)
	return { handled = true, ok = true, message = reply :: string? }
end

return Admin
