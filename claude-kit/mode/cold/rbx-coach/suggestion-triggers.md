<!-- cold: rbx-coach/suggestion-triggers.md | read when: read when the job involves Blender/FBX/rig work, low D1 or ads, developer-product/receipt code, new-player offers, title/icon/thumbnail text, an A/B test under about 1,000 DAU, group play design, a long agent loop or a CLAUDE.md edit. -->

## From agents/rbx-coach.md :: 2b. Suggestion triggers (when you see X, suggest Y with the number; sources in critic-checks.md and the Blender cheat sheet `Roblox/blender/blender-cheat-sheet-claude-blender-roblox.md`)

- Blender, FBX, bpy, mesh, rig or texture work -> `/rbx model-rebuild`, `accessory-fitting-guide`, `rig-checker`, `animation-import-guide`; say the limits: 20,000 triangles per mesh (4,000 accessory), 4 bone influences, Add Leaf Bones off, FBX Unit Scale. Blender MCP: save the .blend first (the socket has no authentication).
- D1 under about 10 percent, or a plan to add rewards or ads to a leaking game -> audit the first 5 minutes first: `/rbx retention-diagnoser`. Ads only after eligibility, a stable build and a working funnel: `/rbx launch-day-planner` (campaign 1-2 weeks, judged after 3-5 days).
- Developer-product or receipt code -> `/rbx devproduct-handler`, `receipt-flow-tester` (`PurchaseGranted` only after the grant). New-player offers -> `/rbx starter-pack-designer` (cheap entry 25-100 Robux, nothing pushy in the first 10-30 minutes).
- Title, icon, thumbnail or description text -> `/rbx experience-name-checker`, `thumbnail-guideline-checker` (1920x1080 thumbnail, 512x512 icon, 160-character opening).
- An A/B test planned under about 1,000 DAU -> qualitative feedback instead (`/rbx ctr-ab-test-planner`). Group play designed to split friends or penalise solo players -> `/rbx social-hook-designer`.
- A long agent loop or a CLAUDE.md edit -> metric stop and iteration cap (`brief-preflight-checklist`); add instruction-file lines only for repeated mistakes after trying to fix the code first.
