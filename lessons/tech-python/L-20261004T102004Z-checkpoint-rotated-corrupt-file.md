---
id: L-20261004T102004Z-checkpoint-rotated-corrupt-file
title: "First checkpoint save would have rotated a corrupt file over the only good backup"
status: active
supersedes: []
recurrence_of: null
occurrences: 1
severity: Medium
tags: [tech:python, phase:implementation, kind:integrity]
recorded_by: implementer
run: gen-20260919T204010Z-consonance-inverse
recorded_at: 2026-10-04T10:20:04Z
---
## Trigger
Writing a save routine that keeps a rolling backup (current -> .bak, then write new current).
## What went wrong
The first Checkpoint.save moved the current file to .bak without validating it, with convoluted exception handling. If the current file was corrupt, the next save replaced the last good backup with it. Found on self-review before any test ran.
## Correction
Rewrote consonance/checkpoint.py: read and validate the current file first; rotate it to .bak only when it is valid (or fails only on schema version); a corrupt current file is simply overwritten and the backup is kept.
## Prevention rule
In any rotate-to-backup routine, validate the file being rotated, never replace a backup with an unvalidated file, and test a save that follows a corrupted current file.
## Detection check
Run: grep -n 'def test_.*corrupt' tests/*.py ; one test must save, corrupt the current file, save again, and assert the backup still loads. The frozen suite has no such test.
## Evidence
commit ab1b417 (consonance/checkpoint.py). Recorded retroactively when the addendum was adopted mid-run.
