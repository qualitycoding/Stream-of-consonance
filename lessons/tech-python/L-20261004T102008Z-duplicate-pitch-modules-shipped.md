---
id: L-20261004T102008Z-duplicate-pitch-modules-shipped
title: "Two overlapping pitch-mode modules and test files were shipped; one is dead code"
status: active
supersedes: []
recurrence_of: null
occurrences: 1
severity: Medium
tags: [tech:python, phase:implementation, kind:scope]
recorded_by: implementer
run: gen-20260919T204010Z-consonance-inverse
recorded_at: 2026-10-04T10:20:08Z
---
## Trigger
Adding a module for a capability (here the standard/free pitch switch) in a package that may already contain one.
## What went wrong
consonance/pitchgrid.py (88 lines; adds note_name and DEFAULT_JUST_RATIOS) and tests/test_pitch_grid.py (10 tests) sit beside consonance/pitchset.py and tests/test_pitch_mode.py (7 tests), all in commit a445f41. generator.py imports only pitchset, so pitchgrid is exercised only by its own tests. The records available do not show how pitchgrid came to be written. The duplication was reported to the user only after the push.
## Correction
Not corrected: S-RETRO changes no deliverable. Consolidation is an open item in DEVIATIONS.md.
## Prevention rule
Before adding a module, grep the package for one with the same responsibility and extend it; if two exist, name the unused one in DEVIATIONS.md before the push.
## Detection check
Run: for m in consonance/*.py; do b=$(basename $m .py); [ $b = __init__ ] && continue; grep -rlw $b --include=*.py consonance scripts examples | grep -v "consonance/$b.py" >/dev/null || echo "unused: $m"; done
## Evidence
git show --stat a445f41; grep of imports in consonance/, scripts/ and examples/. Recorded during S-RETRO.
