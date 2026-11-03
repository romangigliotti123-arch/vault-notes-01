# Luau verification ladder

Cheapest first; run in order and record command plus output excerpt in the ledger `verify` column. Computational checks come before any LLM review.
1. File exists and is non-empty: `ls -l`, `wc -c`.
2. Static: `luau-check.sh` (selene, stylua, luau-lsp); read the last 10 lines. Tools missing = "tools missing: manual review"; never claim lint-clean.
3. Pattern sensors (grep): `loadstring`, `wait(`, `spawn(`, fake `rbxassetid://`; every `OnServerEvent`/`OnServerInvoke` handler validates its arguments; `BindToClose`/`UpdateAsync`/release present for data. Each sensor's failure message says how to fix it.
4. Behaviour: Studio MCP playtest reading Output when present; otherwise the code-walk path (weaker; label it).
5. Independent read-only reviewer (fresh context, binary pass/fail per criterion) for data saving, purchases, remotes or economy.
6. Human playtest for feel, onboarding and the first 30 seconds; no agent check replaces it.

Seeded-bad test: a sensor that never fires proves nothing. Once per project, run each pattern sensor on a tiny known-bad Luau snippet (for example `wait(1)`, `loadstring(x)`, an `OnServerEvent` handler with no checks) and confirm it is flagged; record the output. If it is not flagged, fix the sensor before trusting any clean result.

Playtest loop per milestone: build, static checks, run the plan's observable acceptance test, bug list, at most one fix round per bug batch, re-run only the failed tests, next milestone. When a check or eval result looks surprising, read the raw trace or output before trusting the score.

Source: manager knowledge base topic `topic-managing-ai-agents-for-roblox-game-dev` (rules 3, 4, 6, 7, 8) and addendum items A1-A4.
