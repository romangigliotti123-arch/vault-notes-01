---
id: "roblox-datastore-safe-save"
type: skill
category: "roblox"
source: "own"
license: "first-party"
repo_path: "skills/roblox/roblox-datastore-safe-save/SKILL.md"
description: "Pattern and review checklist for saving player data in Roblox DataStores without loss or duplication: UpdateAsync, retries, session lock, BindToClose, autosave, schema versioning. Use when writing or reviewing any Luau that persists player progress, currency or purchases."
orig_name: "roblox-datastore-safe-save"
tags: [lib/skill, cat/roblox, src/own]
---

# roblox-datastore-safe-save

> Pattern and review checklist for saving player data in Roblox DataStores without loss or duplication: UpdateAsync, retries, session lock, BindToClose, autosave, schema versioning. Use when writing or reviewing any Luau that persists player progress, currency or purchases.

Type: skill | Category: [[categories/cat-roblox|roblox]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/roblox/roblox-datastore-safe-save/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[S--own--roblox-luau-style]], [[S--own--roblox-monetisation-setup]]

---
# Roblox DataStore: safe save

Code comments: none by default (see roblox-luau-style, Comments).

Use when a script loads or saves player data. Output: working Luau module plus the test list below, or a review verdict with line-level findings.

## Rules
1. Server only. Never touch DataStoreService from a LocalScript. The client never sends "my coins are N"; it requests actions and the server computes.
2. One profile table per player under one key (`Player_<UserId>`). Key length limit is 50 chars and a value limit is about 4 MB; keep profiles small and flat.
3. Write with `UpdateAsync` (read-modify-write), not `SetAsync`, for anything that can change from two servers.
4. Wrap every DataStore call in `pcall`; retry with exponential backoff (for example 1s, 2s, 4s, max 5 tries). Respect request budgets (`DataStoreService:GetRequestBudgetForRequestType`) and do not save in a tight loop.
5. Session lock: store `{ jobId, t }` in the profile. On load, if another live JobId holds a fresh lock, wait and retry; if the lock is stale (older than a few minutes) take it. Release the lock on the final save. If this is too much, use a maintained library (ProfileService / ProfileStore) rather than a hand-rolled lock, and say so.
6. Load failure means do NOT let the player play with default data that will later overwrite the real save. Kick with a message, or run in a "not saving" mode.
7. Save on `Players.PlayerRemoving`, on `game:BindToClose` (loop all players, save in parallel, wait until done, stay inside the shutdown window of about 30s), and autosave every 60-120s only when data changed (dirty flag).
8. Schema versioning: a `version` field plus a `migrate(profile)` function with default fill, so new fields never nil-crash old saves.
9. Studio: enable API Services for Studio to test; use a separate test store name so test runs do not touch live data.
10. Purchases and currency: record the processed `PurchaseId` in the profile so a receipt can never grant twice (see roblox-monetisation-setup).

## Skeleton
```lua
local DataStoreService = game:GetService("DataStoreService")
local store = DataStoreService:GetDataStore("PlayerData_v1")
local DEFAULT = { version = 1, coins = 0, receipts = {} }

local function retry(fn, tries)
	local lastErr
	for i = 1, tries or 5 do
		local ok, res = pcall(fn)
		if ok then return true, res end
		lastErr = res
		task.wait(2 ^ (i - 1))
	end
	return false, lastErr
end

local function load(userId)
	local ok, data = retry(function()
		return store:UpdateAsync("Player_" .. userId, function(old)
			old = old or table.clone(DEFAULT)
			old.lock = { jobId = game.JobId, t = os.time() }
			return old
		end)
	end)
	return ok and data or nil
end
```

## Test list (run all before saying done)
- New player, leave, rejoin: data present.
- Shut the server down with players in (Studio Stop and a live test server): `BindToClose` saved.
- Rejoin fast across two servers (Local Server, 2 clients): no duplicated or lost coins.
- Simulate DataStore failure (toggle API off): player is not given default data that gets saved.
- Old-schema profile loads and gains new fields.

Report: pass/fail per item, plus any risk left (no session lock, no retry, SetAsync used).
