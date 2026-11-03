--!strict
--[[
	Analytics: a thin, validated wrapper over AnalyticsService (economy, funnel, onboarding, progression, custom events).
	Pure module (service injected) so the rules are unit-tested headless. Glue: AnalyticsGlue.luau. See ../README.md.

	What it adds over calling AnalyticsService directly:
	  - arguments are validated against the documented rules, bad calls are dropped and logged (never thrown into game code)
	  - the documented per-experience caps (5 currencies, 20 transaction types, 100 SKUs, 10 funnels) are enforced locally,
	    so a typo'd dynamic name cannot silently burn the cap and hide real data
	  - funnel/onboarding steps are sent once per player per step
	  - a per-player, per-event rate limit stops a loop from flooding the pipeline
]]

export type PlayerLike = { UserId: number }

export type Config = {
	service: any, -- AnalyticsService (or a mock)
	flowTypes: { Source: any, Sink: any }, -- Enum.AnalyticsEconomyFlowType.Source / .Sink
	progressionTypes: { Start: any, Complete: any, Fail: any }?, -- Enum.AnalyticsProgressionType.*
	now: () -> number,
	customFieldKeys: { any }?, -- allowed Enum.AnalyticsCustomFieldKeys items (CustomField01..03); other keys are dropped
	maxPerMinute: number?, -- per player per event name (default 30)
	log: ((string) -> ())?,
}

export type Analytics = {
	Economy: (
		self: Analytics,
		player: PlayerLike,
		flow: "Source" | "Sink",
		currency: string,
		amount: number,
		endingBalance: number,
		transactionType: string,
		sku: string,
		fields: { [any]: any }?
	) -> boolean,
	Onboarding: (self: Analytics, player: PlayerLike, step: number, stepName: string) -> boolean,
	Funnel: (
		self: Analytics,
		player: PlayerLike,
		funnel: string,
		sessionId: string,
		step: number,
		stepName: string
	) -> boolean,
	Progression: (
		self: Analytics,
		player: PlayerLike,
		path: string,
		status: "Start" | "Complete" | "Fail",
		level: number,
		levelName: string
	) -> boolean,
	Custom: (self: Analytics, player: PlayerLike, name: string, value: number?, fields: { [any]: any }?) -> boolean,
	ClearPlayer: (self: Analytics, player: PlayerLike) -> (),
}

type Impl = {
	_c: Config,
	_currencies: { [string]: boolean },
	_txTypes: { [string]: boolean },
	_skus: { [string]: boolean },
	_funnels: { [string]: boolean },
	_sent: { [number]: { [string]: boolean } }, -- userId -> "onboarding:3" / "funnel:name:sid:2"
	_rate: { [string]: { start: number, n: number } },
}

local Analytics = {}
Analytics.__index = Analytics

local CAP_CURRENCY, CAP_TX, CAP_SKU, CAP_FUNNEL = 5, 20, 100, 10

local function log(self: Impl, msg: string)
	local f = self._c.log
	if f then
		f("[Analytics] " .. msg)
	end
end

local function reject(self: Impl, why: string): boolean
	log(self, "dropped: " .. why)
	return false
end

local function finite(n: any): boolean
	return type(n) == "number" and n == n and n ~= math.huge and n ~= -math.huge
end

local function nonEmpty(s: any, max: number): boolean
	return type(s) == "string" and #s > 0 and #s <= max
end

function Analytics.new(config: Config): Analytics
	local self = setmetatable({
		_c = config,
		_currencies = {},
		_txTypes = {},
		_skus = {},
		_funnels = {},
		_sent = {},
		_rate = {},
	}, Analytics)
	return (self :: any) :: Analytics
end

-- Counts a never-seen value against a cap. true = ok to send.
local function admit(set: { [string]: boolean }, value: string, cap: number): boolean
	if set[value] then
		return true
	end
	local n = 0
	for _ in set do
		n += 1
	end
	if n >= cap then
		return false
	end
	set[value] = true
	return true
end

local function rateOk(self: Impl, player: PlayerLike, name: string): boolean
	local key = player.UserId .. ":" .. name
	local now = self._c.now()
	local r = self._rate[key]
	if r == nil or now - r.start >= 60 then
		self._rate[key] = { start = now, n = 1 }
		return true
	end
	r.n += 1
	return r.n <= (self._c.maxPerMinute or 30)
end

local function cleanFields(self: Impl, fields: { [any]: any }?): { [any]: any }?
	if fields == nil then
		return nil
	end
	local allowed = self._c.customFieldKeys
	local out: { [any]: any } = {}
	local any = false
	for k, v in fields do
		local keyOk = allowed == nil or table.find(allowed, k) ~= nil
		if keyOk and (type(v) == "string" and #v <= 100) then
			out[k] = v
			any = true
		else
			log(self, "custom field dropped: " .. tostring(k))
		end
	end
	return if any then out else nil
end

local function send(self: Impl, method: string, ...: any): boolean
	local svc = self._c.service
	local args = table.pack(...)
	local ok, err = pcall(function()
		svc[method](svc, table.unpack(args, 1, args.n))
	end)
	if not ok then
		log(self, method .. " failed: " .. tostring(err))
	end
	return ok
end

function Analytics.Economy(
	self: Impl,
	player: PlayerLike,
	flow: "Source" | "Sink",
	currency: string,
	amount: number,
	endingBalance: number,
	transactionType: string,
	sku: string,
	fields: { [any]: any }?
): boolean
	if flow ~= "Source" and flow ~= "Sink" then
		return reject(self, "economy flow must be Source or Sink")
	end
	if not finite(amount) or amount <= 0 then
		return reject(self, "economy amount must be a positive number (use flow Sink for spending)")
	end
	if not finite(endingBalance) or endingBalance < 0 then
		return reject(self, "economy endingBalance must be >= 0")
	end
	if not (nonEmpty(currency, 50) and nonEmpty(transactionType, 50) and nonEmpty(sku, 100)) then
		return reject(self, "economy currency, transactionType and sku must be non-empty strings")
	end
	if not rateOk(self, player, "economy") then
		return reject(self, "economy rate limit")
	end
	if
		not (
			admit(self._currencies, currency, CAP_CURRENCY)
			and admit(self._txTypes, transactionType, CAP_TX)
			and admit(self._skus, sku, CAP_SKU)
		)
	then
		return reject(
			self,
			"economy cap reached (5 currencies / 20 transaction types / 100 skus): "
				.. currency
				.. "/"
				.. transactionType
				.. "/"
				.. sku
		)
	end
	return send(
		self,
		"LogEconomyEvent",
		player,
		self._c.flowTypes[flow],
		currency,
		amount,
		endingBalance,
		transactionType,
		sku,
		cleanFields(self, fields)
	)
end

local function once(self: Impl, player: PlayerLike, key: string): boolean
	local mine = self._sent[player.UserId]
	if mine == nil then
		mine = {}
		self._sent[player.UserId] = mine
	end
	if mine[key] then
		return false
	end
	mine[key] = true
	return true
end

function Analytics.Onboarding(self: Impl, player: PlayerLike, step: number, stepName: string): boolean
	if not finite(step) or step < 1 or step > 100 or step ~= math.floor(step) then
		return reject(self, "onboarding step must be an integer 1-100")
	end
	if not nonEmpty(stepName, 100) then
		return reject(self, "onboarding stepName required")
	end
	if not once(self, player, "onboarding:" .. step) then
		return false
	end
	return send(self, "LogOnboardingFunnelStepEvent", player, step, stepName)
end

function Analytics.Funnel(
	self: Impl,
	player: PlayerLike,
	funnel: string,
	sessionId: string,
	step: number,
	stepName: string
): boolean
	if not (nonEmpty(funnel, 100) and nonEmpty(sessionId, 100) and nonEmpty(stepName, 100)) then
		return reject(self, "funnel name, sessionId and stepName required")
	end
	if not finite(step) or step < 1 or step > 100 or step ~= math.floor(step) then
		return reject(self, "funnel step must be an integer 1-100")
	end
	if not admit(self._funnels, funnel, CAP_FUNNEL) then
		return reject(self, "funnel cap reached (10): " .. funnel)
	end
	if not once(self, player, "funnel:" .. funnel .. ":" .. sessionId .. ":" .. step) then
		return false
	end
	return send(self, "LogFunnelStepEvent", player, funnel, sessionId, step, stepName)
end

function Analytics.Progression(
	self: Impl,
	player: PlayerLike,
	path: string,
	status: "Start" | "Complete" | "Fail",
	level: number,
	levelName: string
): boolean
	if not nonEmpty(path, 100) or string.find(path, "[,\"'\n]") then
		return reject(self, "progression path must be non-empty without comma, quotes or newline")
	end
	local types = self._c.progressionTypes
	if types == nil or types[status] == nil then
		return reject(self, "progression status must be Start, Complete or Fail (and progressionTypes configured)")
	end
	if not finite(level) or not nonEmpty(levelName, 100) then
		return reject(self, "progression level and levelName required")
	end
	if not rateOk(self, player, "progression") then
		return reject(self, "progression rate limit")
	end
	return send(self, "LogProgressionEvent", player, path, types[status], level, levelName)
end

function Analytics.Custom(
	self: Impl,
	player: PlayerLike,
	name: string,
	value: number?,
	fields: { [any]: any }?
): boolean
	if not nonEmpty(name, 100) then
		return reject(self, "custom event name required")
	end
	if value ~= nil and not finite(value) then
		return reject(self, "custom event value must be finite")
	end
	if not rateOk(self, player, "custom:" .. name) then
		return reject(self, "rate limit for " .. name)
	end
	return send(self, "LogCustomEvent", player, name, value or 1, cleanFields(self, fields))
end

function Analytics.ClearPlayer(self: Impl, player: PlayerLike)
	self._sent[player.UserId] = nil
	local prefix = player.UserId .. ":"
	for k in self._rate do
		if string.sub(k, 1, #prefix) == prefix then
			self._rate[k] = nil
		end
	end
end

return Analytics
