<!-- cold: rbx-manager/probe-examples.md | read when: read only when choosing the probe command for a claim (file, process, repo, config, counts, remote, research quotes). -->

## From skills/rbx-manager/references/report-reading-protocol.md :: 4. One command per claim (the probe must be able to fail)

- file made: exists, size, hash/head
- process/service/task: list it
- repo/publication: `git status`, `git log -1 --stat`, `gh repo view --json visibility,url`
- config edit: diff against backup; parse the file
- counts: `find | wc -l`
- remote machine: run the status command there and read the exit code
- research numbers/quotes: open 1-2 cited URLs and compare the quote (a source that does not contain the quote = claim unverified)
- "excerpt from a real run": grep it in the worker transcript
