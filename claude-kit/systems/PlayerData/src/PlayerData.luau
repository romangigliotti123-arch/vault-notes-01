--!strict

export type Data = { [any]: any }

export type Lock = { owner: string, t: number }

export type StoredRecord = { v: number, data: Data, lock: Lock?, saved: number }

export type StoreLike = {
	UpdateAsync: (self: any, key: string, transform: (old: any) -> any) -> any,
}

export type Session = {
	Key: string,
	Data: Data,
	State: "active" | "released" | "lost",
	LastSave: number,
	Saving: boolean,
}

export type Config = {
	store: StoreLike,
	jobId: string,
	template: Data,
	version: number?,
	migrations: { [number]: (Data) -> Data }?,
	now: () -> number,
	wait: (number) -> any,
	spawn: (() -> ()) -> (),
	lockTimeout: number?,
	autosaveInterval: number?,
	loadAttempts: number?,
	saveAttempts: number?,
	lockWait: number?,
	backoffBase: number?,
	onLost: ((Session, string) -> ())?,
	log: ((string) -> ())?,
}

export type PlayerData = {
	LoadAsync: (self: PlayerData, key: string, cancel: (() -> boolean)?) -> (Session?, string?),
	SaveAsync: (self: PlayerData, session: Session) -> boolean,
	ReleaseAsync: (self: PlayerData, session: Session) -> boolean,
	AutosaveDue: (self: PlayerData) -> number,
	ReleaseAll: (self: PlayerData, timeout: number?) -> (),
	GetSession: (self: PlayerData, key: string) -> Session?,
	ActiveCount: (self: PlayerData) -> number,
}

type Impl = {
	_c: Config,
	_sessions: { [string]: Session },
	_version: number,
}

local PlayerData = {}
PlayerData.__index = PlayerData

local function deepCopy(v: any): any
	if type(v) == "table" then
		local out = {}
		for k, x in v do
			out[k] = deepCopy(x)
		end
		return out
	end
	return v
end

local function checkSerializable(v: any, path: string, depth: number): (boolean, string)
	local t = type(v)
	if t == "string" or t == "boolean" then
		return true, ""
	elseif t == "number" then
		if v ~= v or v == math.huge or v == -math.huge then
			return false, path .. " (NaN/inf)"
		end
		return true, ""
	elseif t == "table" then
		if depth > 20 then
			return false, path .. " (too deep or cyclic)"
		end
		local n, strKeys, arrKeys = 0, 0, 0
		for k, x in v do
			n += 1
			if type(k) == "string" then
				strKeys += 1
			elseif type(k) == "number" and k >= 1 and k == math.floor(k) then
				arrKeys += 1
			else
				return false, path .. " (key type " .. type(k) .. ")"
			end
			local ok, where = checkSerializable(x, path .. "." .. tostring(k), depth + 1)
			if not ok then
				return false, where
			end
		end
		if strKeys > 0 and arrKeys > 0 then
			return false, path .. " (mixed keys)"
		end
		for i = 1, arrKeys do
			if v[i] == nil then
				return false, path .. " (array with holes)"
			end
		end
		return true, ""
	end
	return false, path .. " (" .. t .. ")"
end

local function reconcile(data: Data, template: Data)
	for k, tv in template do
		if data[k] == nil then
			data[k] = deepCopy(tv)
		elseif type(tv) == "table" and type(data[k]) == "table" and #tv == 0 then
			reconcile(data[k], tv)
		end
	end
end

local function log(self: Impl, msg: string)
	local f = self._c.log
	if f then
		f(msg)
	end
end

local function backoff(self: Impl, attempt: number)
	local base = self._c.backoffBase or 1
	self._c.wait(math.min(base * 2 ^ (attempt - 1), 30))
end

function PlayerData.new(config: Config): PlayerData
	assert(config.store and config.jobId and config.template, "PlayerData.new: store, jobId, template are required")
	local self = setmetatable({
		_c = config,
		_sessions = {},
		_version = config.version or 1,
	}, PlayerData)
	return (self :: any) :: PlayerData
end

local function write(self: Impl, session: Session, release: boolean): boolean
	local c = self._c
	if session.State ~= "active" then
		return session.State == "released"
	end
	if session.Saving then
		return false
	end
	local okData, where = checkSerializable(session.Data, "Data", 0)
	if not okData then
		log(self, "refusing to save " .. session.Key .. ": unserialisable " .. where)
		if c.onLost then
			c.onLost(session, "unserialisable:" .. where)
		end
		return false
	end
	session.Saving = true
	local snapshot = deepCopy(session.Data)
	local maxAttempts = c.saveAttempts or 5
	local lost = false
	local wasLost = false
	local result = false
	for attempt = 1, maxAttempts do
		lost = false
		local ok, res = pcall(function()
			return c.store:UpdateAsync(session.Key, function(old: any)
				lost = false
				if old == nil or old.lock == nil or old.lock.owner ~= c.jobId then
					lost = true
					return nil
				end
				local now = c.now()
				local rec: StoredRecord = { v = self._version, data = snapshot, saved = now }
				if not release then
					rec.lock = { owner = c.jobId, t = now }
				end
				return rec
			end)
		end)
		if ok and not lost then
			result = true
			break
		elseif ok and lost then
			wasLost = true
			session.State = "lost"
			log(self, "session lost " .. session.Key)
			break
		else
			log(self, "save error " .. session.Key .. ": " .. tostring(res))
			if attempt < maxAttempts then
				backoff(self, attempt)
			end
		end
	end
	session.Saving = false
	if result then
		session.LastSave = c.now()
		if release then
			session.State = "released"
			self._sessions[session.Key] = nil
		end
	elseif wasLost then
		self._sessions[session.Key] = nil
		if c.onLost then
			c.onLost(session, "lost")
		end
	end
	return result
end

function PlayerData.LoadAsync(self: Impl, key: string, cancel: (() -> boolean)?): (Session?, string?)
	local existing = self._sessions[key]
	if existing ~= nil and existing.State == "active" then
		return existing, nil
	end
	local c = self._c
	local lockTimeout = c.lockTimeout or 600
	local maxErr = c.loadAttempts or 6
	local lockWait = c.lockWait or 30
	local errAttempts, waited = 0, 0
	while true do
		if cancel and cancel() then
			return nil, "cancelled"
		end
		local blocked, tooNew = false, false
		local ok, res = pcall(function()
			return c.store:UpdateAsync(key, function(old: any)
				blocked, tooNew = false, false
				local now = c.now()
				local rec: StoredRecord
				if old == nil then
					rec = { v = self._version, data = deepCopy(c.template), saved = now }
				else
					local lock = old.lock
					if lock ~= nil and lock.owner ~= c.jobId and (now - lock.t) < lockTimeout then
						blocked = true
						return nil
					end
					if type(old.v) == "number" and old.v > self._version then
						tooNew = true
						return nil
					end
					local data = deepCopy(old.data)
					local v: number = old.v or 1
					while v < self._version do
						local m = c.migrations and c.migrations[v]
						if m == nil then
							error("missing migration " .. v .. " -> " .. (v + 1))
						end
						data = m(data)
						v += 1
					end
					reconcile(data, c.template)
					rec = { v = self._version, data = data, saved = old.saved or now }
				end
				rec.lock = { owner = c.jobId, t = now }
				return rec
			end)
		end)
		if not ok then
			errAttempts += 1
			log(self, "load error " .. key .. ": " .. tostring(res))
			if errAttempts >= maxErr then
				return nil, "failed"
			end
			backoff(self, errAttempts)
		elseif tooNew then
			return nil, "newer"
		elseif blocked or res == nil then
			if waited >= lockWait then
				return nil, "locked"
			end
			c.wait(3)
			waited += 3
		else
			local session: Session = {
				Key = key,
				Data = (res :: StoredRecord).data,
				State = "active",
				LastSave = c.now(),
				Saving = false,
			}
			self._sessions[key] = session
			if cancel and cancel() then
				write(self, session, true)
				return nil, "cancelled"
			end
			return session, nil
		end
	end
end

function PlayerData.SaveAsync(self: Impl, session: Session): boolean
	return write(self, session, false)
end

function PlayerData.ReleaseAsync(self: Impl, session: Session): boolean
	return write(self, session, true)
end

function PlayerData.AutosaveDue(self: Impl): number
	local c = self._c
	local interval = c.autosaveInterval or 120
	local now = c.now()
	local started = 0
	for _, s in self._sessions do
		if s.State == "active" and not s.Saving and now - s.LastSave >= interval then
			started += 1
			c.spawn(function()
				write(self, s, false)
			end)
		end
	end
	return started
end

function PlayerData.ReleaseAll(self: Impl, timeout: number?)
	local c = self._c
	local pending = 0
	for _, s in self._sessions do
		pending += 1
		c.spawn(function()
			write(self, s, true)
			pending -= 1
		end)
	end
	local waited, limit = 0, timeout or 25
	while pending > 0 and waited < limit do
		c.wait(0.25)
		waited += 0.25
	end
end

function PlayerData.GetSession(self: Impl, key: string): Session?
	return self._sessions[key]
end

function PlayerData.ActiveCount(self: Impl): number
	local n = 0
	for _ in self._sessions do
		n += 1
	end
	return n
end

return PlayerData
