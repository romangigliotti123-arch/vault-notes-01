---
id: "rbx-datastore"
type: skill
category: "roblox"
source: "own"
license: "first-party"
repo_path: "skills/roblox/rbx-datastore/SKILL.md"
description: "Pattern and review checklist for saving player data without loss or duplication: UpdateAsync, retries, session lock, BindToClose, autosave, schema versioning. Use when writing or reviewing Luau that persists progress, currency or purchases."
orig_name: "rbx-datastore"
orig_description: "Pattern and review checklist for saving player data without loss or duplication: UpdateAsync, retries, session lock, BindToClose, autosave, schema versioning. Use when writing or reviewing Luau that persists progress, currency or purchases, or when progress or items vanish or duplicate on rejoin."
tags: [lib/skill, cat/roblox, src/own]
---

# rbx-datastore

> Pattern and review checklist for saving player data without loss or duplication: UpdateAsync, retries, session lock, BindToClose, autosave, schema versioning. Use when writing or reviewing Luau that persists progress, currency or purchases.

Type: skill | Category: [[categories/cat-roblox|roblox]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/roblox/rbx-datastore/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[S--own--rbx-monetize]]

---
# Roblox DataStore: safe save

Code comments: none by default (see rbx-luau, Comments).

Output: working Luau module plus the test list below, or a review verdict with line-level findings.

## Rules
1. Server only. Never touch DataStoreService from a LocalScript. The client never sends "my coins are N"; it requests actions and the server computes.
2. One profile table per player under one key (`Player_<UserId>`). Key limit 50 chars, value limit about 4 MB; keep profiles small and flat.
3. Write with `UpdateAsync` (read-modify-write), not `SetAsync`, for anything that can change from two servers.
4. Wrap every DataStore call in `pcall`; retry with exponential backoff (e.g. 1s, 2s, 4s, max 5 tries). Respect request budgets (`DataStoreService:GetRequestBudgetForRequestType`); never save in a tight loop.
5. Session lock: store `{ jobId, t }` in the profile. On load, if another live JobId holds a fresh lock, wait and retry; a stale lock (older than a few minutes) may be taken. Release it on the final save. If this is too much, use a maintained library (ProfileService / ProfileStore) instead of a hand-rolled lock, and say so.
6. On load failure do NOT let the player play with default data that would later overwrite the real save: kick with a message, or run in a "not saving" mode.
7. Save on `Players.PlayerRemoving`, on `game:BindToClose` (all players in parallel, wait until done, inside the shutdown window of about 30s), and autosave every 60-120s only when data changed (dirty flag).
8. Schema versioning: a `version` field plus `migrate(profile)` with default fill, so new fields never nil-crash old saves.
9. Studio: enable API Services; use a separate test store name so tests never touch live data.
10. Purchases and currency: record the processed `PurchaseId` in the profile so a receipt never grants twice (see rbx-monetize).

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
