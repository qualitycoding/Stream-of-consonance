---
id: L-20261004T102006Z-placeholder-arithmetic-left-in-code
title: "Placeholder arithmetic was written into a function and replaced only on review"
status: active
supersedes: []
recurrence_of: null
occurrences: 1
severity: Low
tags: [tech:python, phase:implementation, kind:process]
recorded_by: implementer
run: gen-20260919T204010Z-consonance-inverse
recorded_at: 2026-10-04T10:20:06Z
---
## Trigger
Writing an expression whose intended form is not yet worked out (here a neutral log-probability for unsupported chords).
## What went wrong
consonance/familiarity.py first contained float((p*np.log(p)).sum()*0 + ...), a placeholder that multiplied one term by zero. Caught on review before any test ran.
## Correction
Replaced it with the intended count-weighted mean log-probability, float((counts / counts.sum() * np.log(p)).sum()).
## Prevention rule
Write the intended expression directly and grep the staged diff for multiply-by-zero, TODO and FIXME before committing.
## Detection check
Run: git diff --cached | grep -nE '^\+.*(\* ?0\b|TODO|FIXME)' ; empty output means none were staged.
## Evidence
consonance/familiarity.py history within commit ab1b417. Recorded retroactively when the addendum was adopted mid-run.
