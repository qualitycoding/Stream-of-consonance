---
id: L-20261004T102005Z-calibration-targets-before-attainable-range
title: "Calibration targets were chosen before measuring the attainable score range"
status: active
supersedes: []
recurrence_of: null
occurrences: 1
severity: Low
tags: [domain:music-perception, tech:python, phase:verification, kind:wrong-assumption]
recorded_by: implementer
run: gen-20260919T204010Z-consonance-inverse
recorded_at: 2026-10-04T10:20:05Z
---
## Trigger
Choosing target values for a generator whose score has an unknown reachable range for the chosen sonority size.
## What went wrong
The first calibration script used targets 0.2-2.6 on the assumption they were all reachable. For 4-note sonorities the random-search maximum is about 2.0, so the highest targets under-shot and the output collapsed onto a few pitch classes.
## Correction
Revised targets to 0.4-2.4, added a random-search attainable-range table to scripts/calibration_report.py and docs/CALIBRATION.md, and reported the collapse at 2.4 as a limitation.
## Prevention rule
Estimate the attainable score range for each sonority size by random search before choosing calibration targets, and print that range beside the targets.
## Detection check
Run: grep -n 'Attainable' docs/CALIBRATION.md ; the table must be present and every target should sit inside it or be flagged.
## Evidence
scripts/calibration_report.py and docs/CALIBRATION.md in commit ab1b417. Recorded retroactively when the addendum was adopted mid-run.
