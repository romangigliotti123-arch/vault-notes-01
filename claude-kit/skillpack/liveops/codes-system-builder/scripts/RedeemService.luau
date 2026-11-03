--!strict
-- RedeemService: the server flow around a redeem-code book, with the storage and the reward injected so it is testable under Lune.
-- It adds what CodeBook (marketing/codes-campaign-planner) deliberately does not: the atomic global-use counter, undo when the grant fails,
-- brute-force throttling of wrong guesses, and one log call per attempt (wire `log` to kit Analytics.Custom, never log the raw typed text).
--
--   local svc = RedeemService.new({
--       checker = CodeBook,                      -- anything with .check(book, raw, state, now)
--       book = serverOnlyBook,                   -- never replicated; validate with CodeBook.validateBook at start
--       store = { read = readUsed, take = takeOne, release = giveBack },   -- DataStore-backed, see SKILL.md
--       now = os.time,
--       grant = function(userId, code, entry) ... return true end,         -- kit Shop/PlayerData grant; false = could not grant
--       markRedeemed = function(userId, code) ... end,                     -- write to the player's profile (PlayerData)
--       log = function(event, userId, fields) ... end,
--   })
--   local res = svc:Redeem(userId, typedText, profileRedeemedSet)
local RedeemService = {}
RedeemService.__index = RedeemService

export type Entry = { reward: string, startsAt: number?, expiresAt: number?, maxUses: number?, creator: string? }
export type CheckResult = { ok: boolean, reason: string?, code: string?, entry: Entry? }
export type Checker = {
	check: (
		book: { [string]: Entry },
		raw: any,
		state: { used: number, mine: { [string]: boolean } },
		now: number
	) -> CheckResult,
}
export type Store = {
	read: (code: string) -> number, -- how many times the code has been redeemed globally
	take: (code: string, maxUses: number?) -> boolean, -- atomically add one use; false when maxUses is already reached (use UpdateAsync)
	release: (code: string) -> (), -- give the use back (grant failed)
}
export type Options = {
	checker: Checker,
	book: { [string]: Entry },
	store: Store,
	now: () -> number,
	grant: (userId: number, code: string, entry: Entry) -> boolean,
	markRedeemed: (userId: number, code: string) -> (),
	log: ((event: string, userId: number, fields: { [string]: any }) -> ())?,
	maxMisses: number?, -- wrong guesses allowed per window before throttling (default 5)
	missWindow: number?, -- seconds (default 60)
}
export type Result = { ok: boolean, reason: string?, reward: string? }

function RedeemService.new(opts: Options)
	assert(
		opts.checker and opts.book and opts.store and opts.now and opts.grant and opts.markRedeemed,
		"RedeemService.new: missing option"
	)
	local self = {
		opts = opts,
		misses = {} :: { [number]: { number } },
		busy = {} :: { [number]: boolean },
	}
	return setmetatable(self, RedeemService)
end

local function note(self: any, event: string, userId: number, fields: { [string]: any })
	if self.opts.log then
		self.opts.log(event, userId, fields)
	end
end

local function throttled(self: any, userId: number, now: number): boolean
	local window = self.opts.missWindow or 60
	local list = self.misses[userId]
	if not list then
		return false
	end
	local keep = {}
	for _, at in list do
		if now - at < window then
			table.insert(keep, at)
		end
	end
	self.misses[userId] = keep
	return #keep >= (self.opts.maxMisses or 5)
end

function RedeemService.Redeem(self: any, userId: number, raw: any, mine: { [string]: boolean }): Result
	local o: Options = self.opts
	local now = o.now()
	if self.busy[userId] then
		return { ok = false, reason = "busy" } -- one redeem at a time per player: two quick clicks must not both pass the checks
	end
	if throttled(self, userId, now) then
		note(self, "redeem_throttled", userId, {})
		return { ok = false, reason = "slow_down" }
	end
	self.busy[userId] = true
	local ok, result = pcall(function(): Result
		local probe = o.checker.check(o.book, raw, { used = 0, mine = mine }, now)
		local used = 0
		if probe.code and probe.entry and probe.entry.maxUses then
			used = o.store.read(probe.code)
		end
		local res = o.checker.check(o.book, raw, { used = used, mine = mine }, now)
		if not res.ok or not res.code or not res.entry then
			local list = self.misses[userId] or {}
			if res.reason == "unknown" or res.reason == "invalid" then
				table.insert(list, now) -- only wrong guesses count toward the throttle
				self.misses[userId] = list
			end
			note(self, "redeem_rejected", userId, { reason = res.reason or "unknown" })
			return { ok = false, reason = res.reason }
		end
		local code, entry = res.code, res.entry
		if not o.store.take(code, entry.maxUses) then
			note(self, "redeem_rejected", userId, { reason = "used_up", code = code })
			return { ok = false, reason = "used_up" }
		end
		local granted = o.grant(userId, code, entry)
		if not granted then
			o.store.release(code)
			note(self, "redeem_grant_failed", userId, { code = code })
			return { ok = false, reason = "grant_failed" }
		end
		o.markRedeemed(userId, code)
		mine[code] = true
		note(self, "redeem_ok", userId, { code = code, creator = entry.creator or "", reward = entry.reward })
		return { ok = true, reward = entry.reward }
	end)
	self.busy[userId] = nil
	if not ok then
		note(self, "redeem_error", userId, {})
		return { ok = false, reason = "error" }
	end
	return result :: Result
end

return RedeemService
