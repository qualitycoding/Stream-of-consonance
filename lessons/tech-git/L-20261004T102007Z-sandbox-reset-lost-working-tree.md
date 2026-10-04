---
id: L-20261004T102007Z-sandbox-reset-lost-working-tree
title: "Assumed the working tree persisted across turns; the sandbox had been reset"
status: active
supersedes: []
recurrence_of: null
occurrences: 1
severity: Medium
tags: [applies:all, tech:git, tech:github, phase:implementation, kind:environment]
recorded_by: implementer
run: gen-20260919T204010Z-consonance-inverse
recorded_at: 2026-10-04T10:20:07Z
---
## Trigger
A later turn continues a run and the first command is cd into a directory created in an earlier turn.
## What went wrong
cd /home/claude/cons-plan failed: /home/claude had been reset. The exported bundle in /mnt/user-data/outputs predated the merge commit (made after export), so only the GitHub copy held the full history.
## Correction
Re-cloned the public repository from GitHub, recreated the generation branch from origin and fast-forwarded it to main.
## Prevention rule
At the start of each turn that continues a run, verify the working tree with git -C <dir> rev-parse HEAD, restore from the remote if it fails, and refresh the exported bundle after every push.
## Detection check
Run: git -C /home/claude/cons-plan rev-parse HEAD && git ls-remote origin ; then git bundle list-heads /mnt/user-data/outputs/consonance-repo.bundle ; heads must match the pushed ones.
## Evidence
This turn's first command output (no such directory); /mnt/user-data/outputs file dates (before the merge). Recorded during this turn, when the failure happened.
