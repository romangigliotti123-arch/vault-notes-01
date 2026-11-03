--!strict
-- CodeBook: the pure rules of a redeem-code system (normalise, window, per-player and global limits) with no DataStore and no
-- Instances, so it is testable under Lune. The server wires it to storage:
--   * `entry` comes from a server-only module/config (never replicated, never in a LocalScript)
--   * `state.used`   = global redemption count for the code. Persist it with DataStoreService:UpdateAsync so two servers cannot both
--                      take the last use; call CodeBook.check with the freshly read count, then increment inside UpdateAsync.
--   * `state.mine`   = the codes THIS player already redeemed (kept in the kit PlayerData profile, so a rejoin cannot redeem twice)
--   * the reward itself is granted by your own server code (kit Shop/PlayerData); this module only decides yes/no and why.
-- The client sends the typed text through a rate-limited RemoteFunction (kit RemoteGuard); it never receives the code list.
local CodeBook = {}

export type Entry = {
	reward: string, -- label your server maps to a grant
	startsAt: number?, -- unix seconds, inclusive
	expiresAt: number?, -- unix seconds, exclusive
	maxUses: number?, -- global limit across all players
	creator: string?, -- attribution label, for analytics only
}
export type State = { used: number, mine: { [string]: boolean } }
export type Result = { ok: boolean, reason: string?, code: string?, entry: Entry? }

-- trim, uppercase, drop inner spaces. Players type codes on phones: be forgiving about case and spaces, strict about everything else.
function CodeBook.normalise(raw: any): string?
	if type(raw) ~= "string" then
		return nil
	end
	if #raw > 64 then
		return nil
	end
	local s = string.upper((string.gsub(raw, "%s+", "")))
	if s == "" then
		return nil
	end
	if string.find(s, "[^A-Z0-9%-]") then
		return nil
	end
	return s
end

function CodeBook.check(book: { [string]: Entry }, raw: any, state: State, now: number): Result
	local code = CodeBook.normalise(raw)
	if code == nil then
		return { ok = false, reason = "invalid" }
	end
	local entry = book[code]
	if entry == nil then
		return { ok = false, reason = "unknown" } -- same message for unknown and expired-and-removed: do not leak which codes exist
	end
	if entry.startsAt and now < entry.startsAt then
		return { ok = false, reason = "unknown" }
	end
	if entry.expiresAt and now >= entry.expiresAt then
		return { ok = false, reason = "expired" }
	end
	if state.mine[code] then
		return { ok = false, reason = "already_redeemed" }
	end
	if entry.maxUses and state.used >= entry.maxUses then
		return { ok = false, reason = "used_up" }
	end
	return { ok = true, code = code, entry = entry }
end

-- every entry must be well formed before the game starts (catch typos in the book at server start, not when a player redeems)
function CodeBook.validateBook(book: { [string]: Entry }): { string }
	local problems = {}
	for code, e in book do
		if CodeBook.normalise(code) ~= code then
			table.insert(problems, `{code}: not in normalised form (A-Z, 0-9, dash)`)
		end
		if type(e.reward) ~= "string" or e.reward == "" then
			table.insert(problems, `{code}: missing reward label`)
		end
		if e.startsAt and e.expiresAt and e.expiresAt <= e.startsAt then
			table.insert(problems, `{code}: expiresAt is not after startsAt`)
		end
		if e.maxUses and e.maxUses < 1 then
			table.insert(problems, `{code}: maxUses must be at least 1`)
		end
	end
	table.sort(problems)
	return problems
end

return CodeBook
