---
id: L-20261004T102009Z-stale-test-counts-in-reports
title: "Reported test counts and freeze status were wrong or stale in the report, README, state file and a reply"
status: active
supersedes: []
recurrence_of: null
occurrences: 1
severity: Medium
tags: [tech:pytest, phase:verification, kind:verification-gap]
recorded_by: implementer
run: gen-20260919T204010Z-consonance-inverse
recorded_at: 2026-10-04T10:20:09Z
---
## Trigger
Writing a report or reply that states how many tests exist or which are frozen.
## What went wrong
The pitch-mode reply and IMPLEMENTATION_REPORT.md item 9 said '7 new tests' sit outside the frozen manifest; there are 17 (7 in test_pitch_mode.py, 10 in test_pitch_grid.py). README.md says 'tests/ is FROZEN' although only 42 of 59 tests are. .checkpoints/state.json still said 42 total.
## Correction
Recounted with pytest --collect-only -q during S-RETRO and corrected .checkpoints/state.json. The report and README wording is listed as an open item.
## Prevention rule
Produce every test count in a report or reply from pytest --collect-only -q per file in the same turn, and never carry counts over from earlier text.
## Detection check
Run: python -m pytest --collect-only -q -p no:cacheprovider | grep '::' | cut -d: -f1 | sort | uniq -c ; compare with each count stated in README.md, IMPLEMENTATION_REPORT.md and .checkpoints/state.json.
## Evidence
IMPLEMENTATION_REPORT.md lines 2 and 29; README.md line 32; pytest --collect-only output in this turn. Recorded during S-RETRO.
